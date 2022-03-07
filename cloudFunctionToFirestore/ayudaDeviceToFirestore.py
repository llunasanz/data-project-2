import base64
import json
from google.cloud import firestore
from datetime import datetime

client = firestore.Client(project='data-project-2-ayuda')

def ayudaDeviceToFirestore(event, context):
    message = ''
    if 'data' in event:
        message = base64.b64decode(event['data']).decode('utf-8')
        ayudaVariable = json.loads(message)


    doc = client.collection('deviceAyuda').document(ayudaVariable["timeStamp"])
    doc.set({
    'battery_level': ayudaVariable["battery_level"],
    'temperature': ayudaVariable["temperature"],
    'bpm': ayudaVariable["bpm"],
    'blood_pressure': ayudaVariable["blood_pressure"],
    'bloodPresiondos' : ayudaVariable["bloodPresiondos"],
    'longitude' : ayudaVariable["longitude"],
    'latitude' : ayudaVariable["latitude"]
    })
    print(f'message: {message}')