import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from test import recognize_adhaar

IVote = Flask(__name__)
CORS(IVote)


@IVote.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('upload.html')


UPLOAD_FOLDER: str = "static/images/"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

IVote.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@IVote.route('/upload', methods=['GET', 'POST'])
def upload_file():
    print(request.method)
    data = request.data
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('welcome'))
        file = request.files['file']
        print(file)
        # if user does not select file, browser also
        # submit a empty part without filename
        print("Reached in function")
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('welcome'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(IVote.config['UPLOAD_FOLDER'], filename))
            print("File Saved")
            user_id = recognize_adhaar(filename)
            print(user_id)
            return jsonify({'ACK': 'SUCCESS', 'id': user_id})
    return jsonify({'ACK': 'FAILED'})


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 8000))
    #IVote.debug = True
    #print("u")
    IVote.run(host='0.0.0.0', port=8000, debug=True)
