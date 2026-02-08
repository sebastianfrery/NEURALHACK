# 🛸 TRAFFIC ANALYTICS SYSTEM - NEURALHACK TEAM SEBASTIAN

Sistema inteligente de análisis de tráfico rodado mediante imágenes aéreas (UAV) con registro de evidencias en Blockchain.

## 📑 Tabla de Contenidos
1. [Objeto del Proyecto](#objeto-del-proyecto)
2. [Características Técnicas](#características-técnicas)
3. [Métricas de Movilidad](#métricas-de-movilidad)
4. [Integración Blockchain](#integración-blockchain)
5. [Instalación y Uso](#instalación-y-uso)
6. [Datasets](#datasets)
7. [Licencia](#licencia)

---

## 📋 Objeto del Proyecto
[cite_start]Esta solución consiste en el diseño y desarrollo de un sistema inteligente de análisis de tráfico a partir de imágenes aéreas capturadas mediante UAV[cite: 3]. [cite_start]El objetivo es generar métricas de movilidad automatizadas y registrar los resultados como evidencia verificable, garantizando que los datos sean precisos, trazables, auditables e inmutables[cite: 3, 4].

## 🛠️ Características Técnicas

### 👁️ Visión Artificial
[cite_start]Implementación avanzada para el procesamiento de imágenes UAV basada en **YOLOv8**[cite: 17, 20]:
* [cite_start]**Detección Automática**: Localización de vehículos en tiempo real[cite: 18].
* [cite_start]**Clasificación por Tipología**: Identificación de turismos, motocicletas y vehículos pesados[cite: 19].
* [cite_start]**Capacidad de Procesamiento**: Optimizado para los conjuntos de datos de Kaggle proporcionados[cite: 54].

### 📊 Métricas de Movilidad
[cite_start]Generación de indicadores objetivos de movilidad a partir de los resultados de visión artificial[cite: 22]:
* [cite_start]**Conteo y Densidad**: Cálculo de vehículos por categoría y densidad de tráfico en la escena[cite: 23, 24].
* [cite_start]**Ocupación**: Estimación de ocupación en intersecciones o rotondas[cite: 25].
* [cite_start]**Seguridad Vial**: Detección de incidentes críticos y análisis de factores de riesgo[cite: 27, 58].

## 🔗 Integración Blockchain (BSV)
[cite_start]Para garantizar la integridad y transparencia, el sistema utiliza la infraestructura de **BSV Association**[cite: 34]:
* [cite_start]**Hash Criptográfico**: Generación de una firma única de los resultados del análisis[cite: 30, 61].
* [cite_start]**Timestamping**: Registro de marca temporal inmutable para cada proceso[cite: 31, 61].
* [cite_start]**Trazabilidad**: Asociación directa a identificadores de escena y ubicación[cite: 32].

---

## 🚀 Instalación y Uso

### Requisitos Previos
* Cuenta en **Kaggle** para acceder a los datos.
* Python 3.10+
* GPU con soporte CUDA (recomendado para procesamiento de visión artificial).

### Configuración
1. **Clonar el repositorio**:
   ```bash
   git clone [https://github.com/sebastianfrery/NEURALHACK.git](https://github.com/sebastianfrery/NEURALHACK.git)
   cd NEURALHACK

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt

3. **Ejecución en Kaggle (Recomendado)**
Para procesar las imágenes con aceleración de hardware:

   a. Cree un nuevo Notebook en Kaggle.

   b. Añada los datasets indicados en la sección siguiente.

   c. Copie el contenido de src/main.py y ejecute las celdas para generar el archivo output/estudio_final_neuralhack_v2.csv.
   
---

📅 Datasets

El sistema ha sido diseñado y evaluado utilizando los siguientes recursos oficiales:

Dataset 1: Traffic Images captured from UAVs. 
https://www.kaggle.com/datasets/javiersanchezsoriano/traffic-images-captured-from-uavs/data

Dataset 2: Roundabout Aerial Images for Vehicle Detection. 
https://www.kaggle.com/datasets/javiersanchezsoriano/roundabout-aerial-images-for-vehicle-detection

---

## 📦 Entregables
* **Código Fuente**: [Carpeta /src](./src/main.py) con la lógica de IA y Blockchain.
* **Resultados**: [Carpeta /output/](./output/estudio_final_neuralhack_v2.csv). Resultados del codigo fuente.
* **Documentación Técnica**: [Descargar Memoria en PDF](./docs/Memoria_Tecnica_NeuralHack_Team_Pro.pdf) 📄
* **Demo**: [Vídeo del funcionamiento](enlace-a-tu-video) 🎥
* **Frontend**:

  ### 🖥️ Ejecución del Dashboard (Local)
Para visualizar los resultados de forma interactiva sin depender de servicios externos:
1. Instale las dependencias: `pip install -r requirements.txt`
2. Ejecute la aplicación: `streamlit run app.py`
3. El dashboard se abrirá automáticamente en su navegador en `http://localhost:8501`

---

### 📄 Licencia
Este proyecto se distribuye bajo una licencia abierta, permitiendo su reutilización, auditoría y mejora por terceros según los requisitos del reto.

---

### TEAM: NEURALHACK SEBASTIAN
