from firebase import firebase
from firebaseapp import firebaseapp
firebaseapp=firebaseapp
def machagiveno(firebaseapp,time):
    res = firebaseapp.get('/sensor1',None)
    for i in res.values():
        for j in i.keys():
            if time == j:
                return i[j]


