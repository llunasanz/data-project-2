# A.Y.U.D.A
**Protected senior**

# Data Project 2
## Máster en Data Analytics - EDEM
### Curso 2021/2022

- [Ramón Cansans Camp](https://www.linkedin.com/in/ramon-casans-camp/)
- [Marta Castillo García](https://www.linkedin.com/in/marta-castillo-garc%C3%ADa-041bb169/)
- [Rafa Pérez Soláns](https://www.linkedin.com/in/rafa-perez-solans/)
- [Mª Ángeles Sanmartin Martinez](https://www.linkedin.com/in/m%C2%AAangeles-sanmart%C3%ADn-mart%C3%ADnez-76b4b9129/)
- [Lluna Sanz Montrull](https://www.linkedin.com/in/llunasmontrull/)

# Proyecto
## Contexto
EDEM ha creado el día 12 de Marzo un evento de lanzamiento de empresas con productos IoT. Es vuestro momento! En este evento podréis presentar vuestro producto IoT como SaaS.
Durante estas tres semanas, debéis pensar un producto IoT, desarrollarlo y simular su uso.
De cara a participar en este evento, vuestra solución debe ser escalable, opensource y  cloud.

## ¿Qué es A.Y.U.D.A?
A.Y.U.D.A es una startup enfocada a la protección de la salud. Su primer reto es la asistencia médica y psicológica de los adultos de mayor edad, seguido por el de escalar su solución a bebés y colectivos más vulnerables, a nivel de salud, que puedan necesitalo. Para lograr este desafío, la startup ha lanzado una RFP para monitorear la frecuencia cardiaca, la temperatura, 


# Tecnología
## Arquitectura
[arquitectura](/media/Arquitectura_BUENA_final.jpg")

## Setup (parte 1)
### Iniciar servicios en Google Cloud
```
gcloud services enable dataflow.googleapis.com
gcloud services enable cloudiot.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

### Crear entorno de Python e instalar las dependencias
```
virtualenv -p python3 device
source device/bin/activate
```
```
pip install -U -r setup_dependencies.txt
```

### Pub/Sub
Se crean dos temas en Pub/Sub:
- iotToBigQuery
- users\_data

### IoT Core
En [IoT Core](https://console.cloud.google.com/iot) se  crea el registro _deviceRegistry_. Luego, se genera una clave RSA con el estándar X.509 ejecutando el siguiente comando, dentro de la carpeta <em>01_IoTCore></em> en la consola de comandos:
```
openssl req -x509 -nodes -newkey rsa:2048 -keyout rsa_private.pem
  \ -out rsa_cert.pem -subj "/CN=unused"
```
Con la clave obtenida, se crea el dispositivo dentro del registro _deviceRegistry_ con el nombre _ayuDevice_ que simulará las medidas del dispositivo de A.Y.U.D.A se accede a la pestaña de _autenticación_ del registro creado y se agrega la clave pública generada en el apartado _comunicación, cloud logging y autenticación_.

### Cloud Storage
Se crea un nuevo bucket con el nombre que mejor se considere (en este caso, _el-bucket-definitiu_) con la opción de región preferida.

### BigQuery
En la página de [BigQuery](https://console.cloud.google.com/bigquery), se crea un dataset con el que se trabajará. En este proyecto, se tratará del llamado _pleaseDataset_.

## Setup (parte 2)
### Cloud Functions

### Firebase

### App Engine

## Ejecución del pipeline
En la consola, se accede a la carpeta <em>02_Dataflow</em> y se ejecutan los siguientes comandos:

```
gcloud builds submit --tag 'gcr.io/data-project-2-ayuda/dataflow/device:latest' .
gcloud dataflow flex-template build "gs://el-bucket-definitiu/dataflowtemplate.json" \
  --image "gcr.io/data-project-2-ayuda/dataflow/device:latest" \
  --sdk-language "PYTHON" 
gcloud dataflow flex-template run "device-dataflow-job" \
    --template-file-gcs-location "gs://el-bucket-definitiu/dataflowtemplate.json" \
    --region "europe-west1"
```
Una vez se han ejecutado exitosamente los comandos, se accede a la carpeta <em>01_IoTCore</em> y ejecutamos el siguiente para iniciar el script del dispositivo IoT:
```
python DeviceData.py \
    --algorithm RS256 \
    --cloud_region europe-west1 \
    --device_id ayuDevice \
    --private_key_file rsa_private.pem \
    --project_id data-project-2-ayuda \
    --registry_id  deviceRegistry
```

# Demo
[![video demo](https://img.youtube.com/vi/J-ISejCfPTA/0.jpg)](https://www.youtube.com/watch?v=J-ISejCfPTA)

