from flask import Flask, render_template, url_for, request
from config import Config
from project.forms import GameProfile

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quest', methods=['GET', "POST"])
def quest():
    information = ''
    direction = ''
    step = ''
    if request.method == 'POST':
        information = 'Go!'
        direction = request.form.get('direction')
        step = request.form.get('step')
        return render_template('quest.html', direction=direction, step=step, information=information)
    return render_template('quest.html')

if __name__ == '__main__':
    app.run(debug=True)