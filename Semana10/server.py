from flask import Flask, send_file

app = Flask(__name__)
    
@app.route('/')
def home():
    return send_file('mysuperawesome.html')

if __name__ == '__main__':
    app.run(debug=True)