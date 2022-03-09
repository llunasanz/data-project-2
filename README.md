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
A.Y.U.D.A se trata de una solución (...)

# Tecnología
## Implementación en Google Cloud
### Requisitos# A.Y.U.D.A
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
A.Y.U.D.A es una startup enfocada a la protección de la salud. Su primer reto es la asistencia médica y psicológica de los adultos de mayor edad, seguido por el de escalar su solución a bebés y colectivos más vulnerables, a nivel de salud, que puedan necesitalo. Para lograr este desafío, la startup ha lanzado una RFP para monitorear la frecuencia cardiaca, la temperatura, (...).


# Tecnología
## Arquitectura
![arquitectura](/media/Arquitectura_BUENA_final.jpg")

## Setup
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
Se crea el registro _deviceRegistry_ y, dentro del mismo, el dispositivo _ayuDevice_ que simulará las medidas del dispositivo. Además, 

### Cloud Storage
Se crea un nuevo bucket 
