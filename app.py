from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html', t="Home")

@app.route('/skills')
def skills():
	return render_template('skills.html', t="Skills")

@app.route('/projects')
def projects():
	return render_template('projects.html', t="Projects")

# Run the application
if __name__ == '__main__':
	app.run(debug=True)