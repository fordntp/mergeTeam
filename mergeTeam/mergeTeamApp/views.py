from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pyrebase
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

config={
  'apiKey': "AIzaSyBArKezZu3iFNLPLZ3RcBBPy0sFqCnZ-Lc",
  'authDomain': "mergeteams.firebaseapp.com",
  'databaseURL': "https://mergeteams-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "mergeteams",
  'storageBucket': "mergeteams.appspot.com",
  'messagingSenderId': "218618412652",
  'appId': "1:218618412652:web:1d638527f3be2a7bd66249",
  'measurementId': "G-SX5JC9NLLG"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def main(request):
    teamName = database.child('data').child('teams').get().val()
    template = loader.get_template('index.html')
    return render(request , 'index.html', {"teamName":teamName})
    # return HttpResponse(template.render(),{"teamName":teamName})

def some_view(request):
    # Your code to update the data
    updated_data = get_updated_data()

    # Broadcast the updated data to WebSocket consumers
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "your_group_name",  # Use a unique group name for your WebSocket consumers
        {"type": "update_data", "data": updated_data},
    )