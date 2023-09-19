from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import pyrebase

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