from flask import render_template, redirect, url_for, request, send_file,session
import os
from werkzeug.utils import secure_filename
from . import app
from .form import Creating_Steg, Getting_Message
from .model import *
import tempfile

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form1 = Creating_Steg()
    form2 = Getting_Message()

    if form1.validate_on_submit():
        file1 = form1.file.data
        filename1 = secure_filename(file1.filename)
        filename_only1 = filename1.split(".")[0]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        file1.save(file_path)
        key = generate_key()
        message=form1.message.data
        enc_msg=encrypt_message(message, key)

        convert_to_png(file_path, os.path.join(app.config['UPLOAD_FOLDER'], "modified" + filename_only1 + ".png"))

        new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], "modified" + filename_only1 + ".png")

        output = os.path.join(app.config['UPLOAD_FOLDER'], "stg" + filename_only1 + ".png")
        steg_encode(new_file_path, enc_msg.decode(), output)
        return render_template('download.html', key=key.decode(), filename="stg" + filename_only1 + ".png")

    return render_template('index1.html', form1=form1, form2=form2)


@app.route('/validate_form2',methods=['POST'])
def validate_form2():
    form2 = Getting_Message()
    if form2.validate_on_submit():
        file2 = form2.file.data
        filename2 = secure_filename(file2.filename)
        file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
        file2.save(file_path2)  
        key2 = form2.key.data
        msg2 = steg_decode(file_path2) 
        decrypted_message = decrypt_message(msg2, key2.encode())
        return render_template('message.html', message2=decrypted_message)
    return redirect(url_for('home'))


@app.route('/download/<filename>')
def download_file(filename):
    path = os.path.join("C:\\Users\\Veena V\\Desktop\\PROJECTS\\Stegnography\\Stegnography_webpage\\app\\static\\files", filename)
    return send_file(path, as_attachment=True)
