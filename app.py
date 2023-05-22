from flask import Flask, render_template, request
import re
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_emails', methods=['POST'])
def fetch_emails():
    url = request.form['url']

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors

        text = response.text

        reg = re.findall(r"[A-Za-z0-9_%+-.]+"
                         r"@[A-Za-z0-9.-]+"
                         r"\.[A-Za-z]{2,5}", text)

        if reg:
            emails = "<ul>"
            for email in reg:
                emails += f"<li>{email}</li>"
            emails += "</ul>"
            return emails
        else:
            return "No valid email addresses found."

    except requests.RequestException:
        return "Error occurred during the request"

if __name__ == '__main__':
    app.run()
