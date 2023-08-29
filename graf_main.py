from flask import Flask, render_template

app = Flask(__name__, template_folder='.')# forma original: app = Flask(__name__)

app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



