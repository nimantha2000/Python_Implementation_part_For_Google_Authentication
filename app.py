from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    recaptcha_response = request.form.get('g-recaptcha-response')
    secret_key = '6Lc-vmwpAAAAAGWkZH1U0H3MamR52V3Q9rP4zg6g'

    # Verify reCAPTCHA response
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', 
                             data={'secret': secret_key, 'response': recaptcha_response})

    data = response.json()
    if data['success']:
        # reCAPTCHA verification success
        # Proceed with your login logic
        return "Login successful"
    else:
        # reCAPTCHA verification failed
        return "reCAPTCHA verification failed"

if __name__ == '__main__':
    app.run(debug=True)
