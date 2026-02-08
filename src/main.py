"""
TRAFFIC ANALYTICS SYSTEM - NEURALHACK TEAM SEBASTIAN
Integración de Visión Artificial (YOLOv8), Análisis de Smart City y Blockchain.
"""

import os
import glob
import hashlib
import pandas as pd
import numpy as np
import torch
from datetime import datetime
from typing import Dict, List, Optional
from tqdm.auto import tqdm
from ultralytics import YOLO

# ==========================================================
# CONFIGURACIÓN GLOBAL
# ==========================================================
CONFIG = {
    "TEAM_ID": "NEURALHACK_TEAM_PRO",
    "MODEL_PATH": "yolov8n.pt",
    "D1": {
        "GEO": '/kaggle/input/traffic-images-captured-from-uavs/scenes.csv',
        "BASE": '/kaggle/input/traffic-images-captured-from-uavs/dataset',
        "IMGSZ": 960,
        "CONF": 0.15
    },
    "D2": {
        "GEO": '/kaggle/input/roundabout-aerial-images-for-vehicle-detection/roundabouts.csv',
        "DATA": '/kaggle/input/roundabout-aerial-images-for-vehicle-detection/data.csv',
        "IMGS": '/kaggle/input/roundabout-aerial-images-for-vehicle-detection/original/original/imgs',
        "IMGSZ": 1280,
        "CONF": 0.08
    },
    "OUTPUT_FILE": "estudio_final_neuralhack_v2.csv",
    "RESOLUTION": (1920, 1080)
}

class TrafficAnalyzer:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO(CONFIG["MODEL_PATH"]).to(self.device)
        self.results_registry = []

    # ------------------------------------------------------
    # LÓGICA DE NEGOCIO (SMART CITY)
    # ------------------------------------------------------
    @staticmethod
    def calculate_vial_risk(intensity: float, occupancy: float) -> str:
        score = (intensity * 0.5) + (occupancy * 0.5)
        if score > 10: return "CRÍTICO"
        if score > 5:  return "MODERADO"
        return "BAJO"

    @staticmethod
    def get_service_level(intensity: float) -> str:
        if intensity < 1.5: return "A - Flujo Libre"
        if intensity < 4.0: return "C - Flujo Restringido"
        return "F - Saturación/Congestión"

    @staticmethod
    def generate_blockchain_proof(payload: str) -> str:
        return hashlib.sha256(payload.encode()).hexdigest()

    # ------------------------------------------------------
    # PROCESAMIENTO DE IMÁGENES
    # ------------------------------------------------------
    def run_inference(self, image_paths: List[str], img_size: int, conf_thresh: float) -> Dict:
        """Ejecuta inferencia por lotes y extrae métricas de tráfico."""
        total_counts = {"car": 0, "moto": 0, "heavy": 0, "area": 0.0}
        batch_size = 32
        
        for i in range(0, len(image_paths), batch_size):
            batch = image_paths[i : i + batch_size]
            results = self.model.predict(
                source=batch, 
                conf=conf_thresh, 
                imgsz=img_size, 
                half=True, 
                verbose=False
            )
            
            for r in results:
                cls = r.boxes.cls.cpu().numpy().astype(int)
                counts = np.bincount(cls, minlength=10)
                
                total_counts["car"] += counts[2]
                total_counts["moto"] += counts[3]
                total_counts["heavy"] += (counts[5] + counts[7]) # Bus + Truck
                
                if r.boxes.xywh.numel() > 0:
                    # Suma de áreas de bboxes
                    total_counts["area"] += (r.boxes.xywh[:, 2] * r.boxes.xywh[:, 3]).sum().item()
                    
        return total_counts

    # ------------------------------------------------------
    # PROCESADORES DE DATASETS
    # ------------------------------------------------------
    def process_uav_traffic(self):
        print("🚀 Procesando Dataset 1: UAV Traffic...")
        df_geo = pd.read_csv(CONFIG["D1"]["GEO"])
        df_geo.columns = df_geo.columns.str.strip()

        for _, row in tqdm(df_geo.iterrows(), total=len(df_geo)):
            seq = row['Sequence']
            # Obtener Ground Truth (GT)
            gt_files = glob.glob(os.path.join(CONFIG["D1"]["BASE"], seq, "**", "*.txt"), recursive=True)
            c_gt = 0
            for f_path in gt_files:
                with open(f_path, 'r') as f:
                    c_gt += sum(1 for line in f if line.split() and int(line.split()[0]) in [0, 1])
            
            gt_int = round(c_gt / len(gt_files), 2) if gt_files else 0.0

            # IA Inferencia
            images = []
            for ext in ['*.jpg', '*.png', '*.jpeg']:
                images.extend(glob.glob(os.path.join(CONFIG["D1"]["BASE"], seq, "**", ext), recursive=True))
            
            if not images: continue
            
            metrics = self.run_inference(images, CONFIG["D1"]["IMGSZ"], CONFIG["D1"]["CONF"])
            self._register_data(seq, "UAV_Traffic", row['lat'], row['long'], len(images), metrics, gt_int)

    def process_roundabout_aerial(self):
        print("\n🚀 Procesando Dataset 2: Roundabout Aerial...")
        df_data = pd.read_csv(CONFIG["D2"]["DATA"])
        df_geo = pd.read_csv(CONFIG["D2"]["GEO"])
        
        # Mapeo de GT
        df_data['scene_id'] = df_data['image_name'].str.extract(r'(\d{5})')
        gt_map = df_data.groupby('scene_id').size().to_dict()

        # Agrupar imágenes por escena
        all_imgs = sorted(glob.glob(os.path.join(CONFIG["D2"]["IMGS"], "*.jpg")))
        scenes = {}
        for f in all_imgs:
            sid = os.path.basename(f).split('_')[0]
            scenes.setdefault(sid, []).append(f)

        for sid, img_list in tqdm(scenes.items()):
            try:
                geo = df_geo[df_geo['scene'].astype(int) == int(sid)].iloc[0]
                lat, lon = geo['lat'], geo['long']
            except:
                lat, lon = 0.0, 0.0

            metrics = self.run_inference(img_list, CONFIG["D2"]["IMGSZ"], CONFIG["D2"]["CONF"])
            gt_int = round(gt_map.get(sid, 0) / len(img_list), 2)
            
            self._register_data(sid, "Roundabout_Aerial", lat, lon, len(img_list), metrics, gt_int)

    def _register_data(self, seq_id, ds_name, lat, lon, n_imgs, metrics, gt_int):
        div = n_imgs if n_imgs > 0 else 1
        ia_int = round((metrics["car"] + metrics["moto"] + metrics["heavy"]) / div, 2)
        ia_ocup = round(((metrics["area"] / div) / (CONFIG["RESOLUTION"][0] * CONFIG["RESOLUTION"][1])) * 100, 2)
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = {
            'id_secuencia': seq_id,
            'dataset': ds_name,
            'team_id': CONFIG["TEAM_ID"],
            'latitud': lat, 'longitud': lon,
            'avg_turismos': round(metrics["car"] / div, 2),
            'avg_motos': round(metrics["moto"] / div, 2),
            'avg_pesados': round(metrics["heavy"] / div, 2),
            'ia_intensidad': ia_int,
            'gt_intensidad': gt_int,
            'error_abs': round(ia_int - gt_int, 2),
            'ia_ocupacion_%': ia_ocup,
            'riesgo_vial': self.calculate_vial_risk(ia_int, ia_ocup),
            'nivel_servicio': self.get_service_level(ia_int),
            'blockchain_hash': self.generate_blockchain_proof(f"{CONFIG['TEAM_ID']}|{seq_id}|{ia_int}|{ts}"),
            'timestamp': ts
        }
        self.results_registry.append(entry)

    def export(self):
        df = pd.DataFrame(self.results_registry)
        df.to_csv(CONFIG["OUTPUT_FILE"], index=False)
        return df

# ==========================================================
# EJECUCIÓN PRINCIPAL
# ==========================================================
if __name__ == "__main__":
    analyzer = TrafficAnalyzer()
    
    # Procesar ambos orígenes de datos
    analyzer.process_uav_traffic()
    analyzer.process_roundabout_aerial()
    
    # Generar entregable
    df_final = analyzer.export()
    print(f"\n✅ Proceso finalizado. Archivo guardado como: {CONFIG['OUTPUT_FILE']}")
    print(df_final.head())
