from flask import Flask,render_template,request,redirect,url_for
import firebase
from firebase import FirebaseApplication

firebase = FirebaseApplication('https://malai-9065d.firebaseio.com/')
app = Flask(__name__)

@app.route('/')
def one():
	return render_template('index.html',title='one')

@app.route('/two',methods=['GET','POST'])
def two():
	'''data = dict()
	data['field 1'] = request.form['name']
	data['field 2'] = request.form['name2']'''
	data = firebase.get('/sensor1')
	
	return render_template('two.html',title='two',data=data)


if __name__=='__main__':
	app.run()
