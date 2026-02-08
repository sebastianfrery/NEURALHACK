# 🛸 TRAFFIC ANALYTICS SYSTEM - NEURALHACK TEAM SEBASTIAN

Sistema inteligente de análisis de tráfico rodado mediante imágenes aéreas (UAV) con registro de evidencias en Blockchain.

## 📑 Tabla de Contenidos
1. [Objeto del Proyecto](#objeto-del-proyecto)
2. [Características Técnicas](#características-técnicas)
3. [Métricas de Movilidad](#métricas-de-movilidad)
4. [Integración Blockchain](#integración-blockchain)
5. [Instalación y Uso](#instalación-y-uso)
6. [Licencia](#licencia)

---

## 📋 Objeto del Proyecto
Esta solución permite el diseño y desarrollo de un sistema capaz de generar métricas de movilidad automatizadas a partir de imágenes capturadas por vehículos aéreos no tripulados. El objetivo es garantizar que los datos producidos sean **precisos, trazables, auditables e inmutables**, permitiendo su uso en contextos institucionales y de planificación urbana.

## 🛠️ Características Técnicas

### 👁️ Visión Artificial
Implementación avanzada para el procesamiento de imágenes UAV:
* **Detección Automática**: Localización de vehículos en tiempo real mediante modelos de aprendizaje profundo.
* **Clasificación por Tipología**: Identificación y conteo de turismos, motocicletas y vehículos pesados.
* **Arquitectura Robusta**: Basado en arquitecturas de última generación como **YOLOv8** para garantizar precisión en la detección.

### 📊 Métricas de Movilidad
A partir del análisis visual, el sistema genera indicadores objetivos:
* **Conteo y Densidad**: Cálculo del flujo vehicular y ocupación de escenas o rotondas.
* **Seguridad Vial**: Detección de incidentes críticos y análisis de factores de riesgo.
* **Comparativa Temporal**: Capacidad de contrastar datos entre distintas capturas espaciales.

## 🔗 Integración Blockchain (BSV)
Para asegurar que los resultados sean evidencias técnicas auditables, el sistema utiliza la tecnología de **BSV Association**:
* **Hash Criptográfico**: Generación de una firma única de los resultados del análisis.
* **Registro de Tiempo (Timestamp)**: Marca temporal inmutable para cada proceso.
* **Integridad de Datos**: Garantía de que la información no ha sido alterada tras su registro.

---

## 🚀 Instalación y Uso

### Requisitos Previos
* Python 3.10+
* GPU con soporte CUDA (recomendado)

### Configuración
1. **Clonar el repositorio**:
   ```bash
   git clone [https://github.com/sebastianfrery/NEURALHACK.git]
   cd NEURALHACK

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt

3. **Ejecutar el Pipeline**:
   ```bash
   python main.py
---

## 📦 Entregables
* **Código Fuente**: [Carpeta /src](./src/main.py) con la lógica de IA y Blockchain.
* **Documentación Técnica**: [Descargar Memoria en PDF](./docs/Memoria_Tecnica_NeuralHack_Team_Pro.pdf) 📄
* **Demo**: [Vídeo del funcionamiento](enlace-a-tu-video) 🎥


---

### 📄 Licencia
Este proyecto se distribuye bajo una licencia abierta, permitiendo su reutilización, auditoría y mejora por terceros según los requisitos del reto.

---

### TEAM: NEURALHACK SEBASTIAN
