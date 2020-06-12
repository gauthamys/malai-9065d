from flask import Flask,render_template,request,redirect,url_for
from firebaseapp import firebaseapp
from functions import machagiveno
from time import ctime
app = Flask(__name__)

firebaseapp=firebaseapp

@app.route('/',methods = ['GET','POST'])
def one():
	if request.method == 'GET':
		return render_template('index.html',title='one',time=ctime())
	else:
		time = request.form['time']
		data = machagiveno(firebaseapp,time=time)
		if data:
			return render_template('two.html',title='two',time=time,data=data)
		else:
			return render_template('two.html',title='two',time=time)


@app.route('/facts')
def gay():
	return render_template("tusharisgay.html",title="GayLord")

if __name__ == '__main__':
	app.run()


