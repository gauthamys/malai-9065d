from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def one():
	return render_template('index.html',title='one')
@app.route('/two')
def two():
	return render_template('two.html',title='two')
if __name__=='__main__':
	app.run()
