from flask import Flask, request, render_template_string, render_template
import secrets
import subprocess


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if email != '':
	        thanks = 'We have sent a confirmation to your email {}'.format(email)
        else:
	        thanks = ''
        template = '''
    <!DOCTYPE html>
<html>
  <head>
    <title>Subscribe Now</title>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        font-family: "Inter", sans-serif;
      }
      .formbold-main-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 48px;
      }

      .formbold-form-wrapper {
        margin: 0 auto;
        max-width: 550px;
        width: 100%;
        background: white;
      }

      .formbold-form-title {
        margin-bottom: 40px;
      }
      .formbold-form-title h3 {
        color: #07074D;
        font-weight: 700;
        font-size: 28px;
        line-height: 35px;
        width: 60%;
        margin-bottom: 20px;
      }
      .formbold-form-title p {
        font-size: 16px;
        line-height: 24px;
        color: #536387;
        width: 70%;
      }
      .formbold-form-input {
        text-align: center;
        width: 100%;
        padding: 14px 22px;
        border-radius: 6px;
        border: 1px solid #DDE3EC;
        background: #FAFAFA;
        font-weight: 500;
        font-size: 16px;
        color: #536387;
        outline: none;
        resize: none;
      }
      .formbold-form-input:focus {
        border-color: #6a64f1;
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.05);
      }

      .formbold-btn {
        text-align: center;
        width: 100%;
        font-size: 16px;
        border-radius: 5px;
        padding: 14px 25px;
        border: none;
        font-weight: 500;
        background-color: #6A64F1;
        color: white;
        cursor: pointer;
        margin-top: 15px;
      }
      .formbold-btn:hover {
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.05);
      }

    </style>
</head>
<body>
<div class="formbold-main-wrapper">
  <!-- Author: FormBold Team -->
  <!-- Learn More: https://formbold.com -->
  <div class="formbold-form-wrapper">
    <div class="formbold-form-title">
        <h3>Thanks for subscribing!</h3>
        <p>'''+ thanks+'''</p>
    </div>
  </div>
</div>
</body>
</html>'''
        return render_template_string(template)
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=False)
