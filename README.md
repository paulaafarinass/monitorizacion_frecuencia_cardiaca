# 🏥 Central de Triaje IoT: Monitorización Médica en Tiempo Real

## 📖 Sobre el Proyecto
Este proyecto es una Prueba de Concepto (PoC) de un sistema de telemedicina diseñado para monitorizar constantes vitales en tiempo real y **reducir la fatiga de alertas hospitalarias**. 

A través de la integración de múltiples sensores simulados (frecuencia cardíaca y movimiento), el sistema aplica algoritmos de triaje para distinguir entre emergencias médicas reales y falsos positivos (por ejemplo, alteraciones del pulso debidas a que el paciente se está moviendo), mostrando los datos en un panel web interactivo.

## ✨ Características Principales
* **Telemetría en Tiempo Real:** Visualización continua de datos sin bloqueos del servidor utilizando manejo de estado asíncrono (`st.session_state` y `st.rerun`).
* **Algoritmo de Triaje Inteligente:** Lógica condicional que evalúa el estado del paciente (Estable, Alerta Médica, Parada Cardíaca) cruzando datos de ritmo cardíaco con detectores de movimiento para anular falsas alarmas.
* **Visualización Dinámica:** Gráficos de evolución temporal que simulan un monitor de constantes (electrocardiograma básico) guardando el historial en la memoria de la sesión.
* **Interfaz de Usuario (UI) Clínica:** Panel limpio y centrado en la accesibilidad, con indicadores de color estándar en la industria médica.

## 🏗️ Arquitectura del Sistema
El proyecto está dividido en componentes modulares para facilitar la escalabilidad futura hacia hardware real:
1. **Generación de Datos (`sensor_pulsaciones.py`, `sensor_movimiento.py`):** Módulos independientes que actúan como "Hardware Virtual", generando datos biométricos.
2. **Motor Lógico:** Capa de procesamiento que aplica las reglas de validación clínica.
3. **Frontend (`app.py`):** Interfaz web desarrollada íntegramente en Python puro.

## 🚀 Tecnologías Utilizadas
* **Python 3.x:** Lenguaje principal.
* **Streamlit:** Framework para el despliegue de la aplicación web y manejo del panel interactivo.
* **Plotly / Streamlit Native Charts:** Para la renderización gráfica de señales biomédicas.

## 💻 Instalación y Ejecución Local
Si deseas clonar este proyecto y ejecutarlo en tu propia máquina, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)

