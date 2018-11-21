import os

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('upload.html')


UPLOAD_FOLDER: str = "static/images"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    #print(request.method)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('welcome'))
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        #print("Reached in function")
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('welcome'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print("File Saved")
            return redirect(url_for('welcome',
                                    filename=filename))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
