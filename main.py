
from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    form = jinja_env.get_template('form.html')
    return form.render()

@app.route("/new-user", methods=['POST'])
def new_user():
    username = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    email = request.form['email']
    invalid_username = ''
    invalid_password = ''
    password_mismatch = ''
    invalid_email = ''
    error_present = False

    if not username or len(username) < 3 or len(username)>20 or ' ' in username:
        invalid_username = "Please enter a valid username!"
        username = ''
        error_present= True


    if not password1 or len(password1) < 3 or len(password1)>20 or ' ' in password1:
        invalid_password = "Please enter a valid password!"
        error_present= True

    if password1 != password2:
         password_mismatch = "Passwords don't match!!!"
         error_present= True

    if email:
        if '@' not in email or '.' not in email or ' ' in email or len(email) < 3 or len(email)>20:
            invalid_email = "Please enter a valid email!"
            email = ''
            error_present = True
    
    if not error_present:
        greeting = jinja_env.get_template('greeting.html')
        return greeting.render(username= username)
    else:
        password1 =''
        password2 =''
        form = jinja_env.get_template('form.html')
        return form.render(username=username, invalid_username=invalid_username, password1=password1, 
                invalid_password=invalid_password, password2 =password2, password_mismatch= password_mismatch,
                email=email, invalid_email=invalid_email)


app.run()