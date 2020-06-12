from flask import Flask,render_template,request,redirect,url_for
#from firebaseapp import firebaseapp
app = Flask(__name__)

@app.route('/')
def one():
	return render_template('index.html',title='one')

'''@app.route('/two',methods=['GET','POST'])
def two():
	data = dict()
	data['field 1'] = request.form['name']
	data['field 2'] = request.form['name2']

	data2 = firebaseapp.get('/sensor1',None)
	return data2
	
	#return render_template('two.html',title='two',data=data2)'''

@app.route('/facts')
def gay():
	return render_template("tusharisgay.html",title="GayLord")

if __name__ == '__main__':
	app.run()


