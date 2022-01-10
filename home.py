import ipapi
from flask import Flask, request, render_template
 
app = Flask(__name__, static_url_path='')
 
@app.route('/', methods = ['GET', 'POST'])
def main():
    return render_template('homepage.html')

@app.route('/login.html', methods = ['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/register.html', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)