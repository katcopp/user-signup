from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<style>
    .error {{color:red;}}
</style>
<!doctype html>
<html>
    <body>
        <form action="/new-user" method="post">
            <label for="username">Username:       </label>
            <input id="username" type="text" name="username" value='{username}' /> 
            <p class = "error"> {invalid_username}</p> <br>
            <label for="password">Password:       </label>
            <input id="password1" type="password" name="password1" value='{password1}'/>
            <p class = "error"> {invalid_password}</p> <br>
            <label for="password">Verify Password:</label>
            <input id="password2" type="password" name="password2" value='{password2}'/>
            <p class = "error"> {password_mismatch}</p> <br>
            <label for="email">Email (optional):</label>
            <input id="email" type="text" name="email" value='{email}'/>
            <p class = "error"> {invalid_email}</p> <br>
            <input type="submit" />
        </form>


    </body>
</html>
"""
    

@app.route("/")
def index():
    return form.format(username='', invalid_username='', password1='', 
                invalid_password='', password2 ='', password_mismatch='',
                email='', invalid_email='')

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
        password1 = ''
        error_present= True

    if password1 != password2:
         password_mismatch = "Passwords don't match!!!"
         password2 = ''
         password1 = ''
         error_present= True
    
    if not error_present:
        return '<h1>Hello, ' + username + '! </h1>'
    else:
        return form.format(username=username, invalid_username=invalid_username, password1=password1, 
                invalid_password=invalid_password, password2 =password2, password_mismatch= password_mismatch,
                email=email, invalid_email=invalid_email)


app.run()