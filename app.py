from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/send_email', methods=['POST'])
def send_email():
    email_text = request.form['contact']
    app.logger.info(f'Email text: "{email_text}"')
    return email_text
