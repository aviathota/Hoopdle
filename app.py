from flask import Flask, render_template
app = Flask(__name__)

page = 0

@app.route("/")
def home():
    return render_template('main.html')

@app.route('/rules', methods=['POST'])
def rules():
    print("Rules button clicked!")
    return render_template('rules.html')

@app.route('/home', methods=['POST'])
def back():
    print("Back button clicked!")
    return render_template('main.html')