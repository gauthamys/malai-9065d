from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def one():
	return 'OK'
@app.route('/two')
def two():
	return render_template('index.html')
if __name__=='__main__':
	app.run()
