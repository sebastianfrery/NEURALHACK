🛸 TRAFFIC ANALYTICS SYSTEM - NEURALHACK TEAM PRO
Este proyecto presenta una solución integral para el análisis inteligente de tráfico rodado mediante imágenes aéreas capturadas por UAVs (Drones). El sistema automatiza la generación de métricas de movilidad urbana y garantiza la integridad de los datos mediante el registro de evidencias en la red Blockchain.


📑 Tabla de Contenidos
Descripción del Proyecto

Características Técnicas

Instalación y Uso

Métricas de Movilidad

Integración Blockchain

Licencia

📋 Descripción del Proyecto
El sistema ha sido diseñado para responder a las necesidades de administraciones públicas y proyectos de Smart Cities que requieren datos con alta fiabilidad técnica y transparencia metodológica.


La solución procesa secuencias de imágenes aéreas para detectar vehículos, clasificarlos y generar informes de densidad y riesgo vial, registrando cada análisis de forma inmutable.



🛠️ Características Técnicas

Visión Artificial: Implementación de YOLOv8 para la detección y clasificación de vehículos en tres categorías principales: turismos, motocicletas y vehículos pesados.



Análisis Geoespacial: Vinculación de métricas a coordenadas geográficas (latitud/longitud) y marcas temporales (timestamps).


Procesamiento por Lotes: Optimización del rendimiento mediante inferencia en batch (32 imágenes por lote).


Métricas Avanzadas: Cálculo de intensidad de tráfico, porcentaje de ocupación de la vía y Nivel de Servicio (LOS).


🚀 Instalación y Uso
Requisitos Previos
Python 3.10+

Entorno con soporte CUDA (recomendado para procesamiento de visión artificial).

Instalación
Clona el repositorio:

Bash

git clone https://github.com/sebastianfrery/NEURALHACK.git
cd nombre-del-repo
Instala las dependencias:

Bash

pip install -r requirements.txt
Ejecución
Para procesar los datasets y generar el registro de evidencias:

Bash

python main.py
📊 Métricas de Movilidad
El sistema genera automáticamente los siguientes indicadores para cada escena analizada:



Conteo por categoría: Desglose exacto de tipos de vehículos.


Densidad e Intensidad: Vehículos promedio por captura temporal.


Riesgo Vial: Clasificación de incidentes críticos (Bajo, Moderado, Crítico) basada en la saturación de la vía.


Nivel de Servicio: Evaluación del flujo vehicular según estándares de ingeniería de movilidad.


🔗 Integración Blockchain
Para garantizar que los datos sean trazables, auditables e inmutables, el sistema realiza las siguientes acciones:



Hasehado Criptográfico: Generación de un hash SHA-256 único por cada análisis realizado.


Timestamping: Registro del momento exacto del análisis.


Referencia BSV: Preparado para la infraestructura de BSV Association, asegurando la integridad de la evidencia técnica.



📄 Licencia
Este proyecto se distribuye bajo una licencia abierta, permitiendo su reutilización, auditoría y mejora por parte de terceros para fomentar la transparencia en proyectos de movilidad sostenible.


Equipo: NEURALHACK TEAM PRO


Reto: Sistema Inteligente de Análisis de Tráfico Rodado - NeuralHack
