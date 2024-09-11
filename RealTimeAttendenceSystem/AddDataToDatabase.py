
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#database connection code

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-16ca5-default-rtdb.firebaseio.com/"
})

#student data send to database

ref = db.reference('Students')

data = {
    "10930623063":
        {
            "name": "DHRUBOJYOTI MONDAL",
            "major": "AIML",
            "starting_year": 2023,
            "total_attendance": 0,
            "section": "A",
            "year": 2,
            "last_attendance_time": "2023-12-11 00:54:34"
        },
    "10930623066":
        {
            "name": "Ayaan Gopal Ray",
            "major": "AIML",
            "starting_year": 2023,
            "total_attendance": 0,
            "section": "A",
            "year": 2,
            "last_attendance_time": "2024-03-11 19:55:34"
        },
"10900223203":
        {
            "name": "Ankur Dhol",
            "major": "IT",
            "starting_year": 2023,
            "total_attendance": 0,
            "section": "C",
            "year": 2,
            "last_attendance_time": "2024-03-05 00:54:34"
        },
 "10930623067":
        {
            "name": "Shweta Dutta",
            "major": "AIML",
            "starting_year": 2023,
            "total_attendance": 0,
            "section": "C",
            "year": 2,
            "last_attendance_time": "2024-03-05 00:54:34"
        },
"10900223199":
        {
            "name": "Sumanta Mandal",
            "major": "IT",
            "starting_year": 2023,
            "total_attendance": 0,
            "section": "C",
            "year": 2,
            "last_attendance_time": "2024-03-05 00:54:34"
        },
"109306230690":
        {
            "name": "Sayan Banerjee",
            "major": "CST",
            "starting_year": 2023,
            "total_attendance": 0,
            "section": "A",
            "year": 2,
            "last_attendance_time": "2024-03-05 00:54:34"
        },




}

for key, value in data.items():
    ref.child(key).set(value)

