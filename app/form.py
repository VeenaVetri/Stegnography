from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FileField,HiddenField,PasswordField

class Creating_Steg(FlaskForm):
    file=FileField("File", render_kw={"placeholder": "Choose a file to upload"})
    message=StringField("Message", render_kw={"placeholder": "Enter message"})
    submit=SubmitField("Submit", render_kw={"class": "submit-button"})

class Getting_Message(FlaskForm):
    file=FileField("File", render_kw={"placeholder": "Choose a file to upload"})
    key=StringField("Key", render_kw={"placeholder": "Enter key"})
    Submit2=SubmitField("Submit", render_kw={"class": "submit-button"})