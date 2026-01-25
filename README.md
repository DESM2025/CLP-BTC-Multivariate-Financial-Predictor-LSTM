Este pequeño proyecto utiliza una red neuronal recurente LSTM simple para predecir el precio de cierre del bitcoin y peso chileno  
El modelo se entrena con datos de yahoo finance y utiliza ventanas de observacion de diferentes dias para las dos monedas con tal de proyectar el valor del dia siguiente

Posteriormente se incluyo un modelo multivariado usando como features el clp,dolar index y precio del cobre,
Incluye un dashboard  en Streamlit para visualizar datos historicos, pero solo usa el de los modelos univariados por ahora
tambien se incluye un nootebok con graficos y pequeño analisis, esta en la carpeta nootebooks

El proyecto esta diseñado para ejecutarse en conda,`bitcoin_env`

conda env create -f environment.yml
conda activate bitcoin_env

streamlit run src/05_dashboard_v2.py

primero se debe descargar el dataset mediante los archivos 01_get_data y get_data_multi en la carpeta src