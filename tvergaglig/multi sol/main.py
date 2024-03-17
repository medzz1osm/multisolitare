from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Here you would add the user to the database
        return 'Thanks for registering!'
    elif request.method == 'GET':
        return '''
            <form method="POST">
                Username: <input type="text" name="username"><br>
                Email: <input type="text" name="email"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Register">
            </form>
        '''
    else:
        return 'Form not submitted'

if __name__ == '__main__':
    app.run(debug=True)