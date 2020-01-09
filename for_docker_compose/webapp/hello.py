import os

import numpy as np
from werkzeug.utils import secure_filename

import pandas as pd
import sklearn
from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, send_file, url_for)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from joblib import load
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
clf = load('knn.pkl')

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))




@app.route('/')
def hello_world():
    #print('hi')
    return "Hello, my best friend!"


def predict_iris(param):
    param = [float(num) for num in param.split(',')]
    param = np.array(param).reshape((1, -1))

    predict = {'class': str(clf.predict(param)[0])}
    return predict
    
@app.route('/mean/<nums>')
def mean_flask(nums):
    nums = [float(num) for num in nums.split(',')]
    mean = sum(nums)/len(nums)
    print(nums)
    return str(mean)

@app.route('/iris/<param>')
def iris (param):
    predict = predict_iris(param)
    return jsonify(predict)



@app.route("/iris_post", methods=['POST'])
def iris_post():
    try:
        param = request.get_json()
        predict = predict_iris(param['flower'])
    except:
        return redirect(url_for('bad_request'))
    
    return jsonify(predict)

@app.route("/image")
def show_im():
    return '<img src="./static/setosa.jpg" alt="Iris setosa">'

@app.route('/badrequest400')
def bad_request():
    abort(400)

class MyForm(FlaskForm):
    name = StringField('name', default='final_prediction.csv', validators=[DataRequired()])
    photo = FileField()

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():

        f = form.photo.data
        fname = os.path.join('static', form.name.data)
        #f.save()

        df = pd.read_csv(f, header=None)
        predict = clf.predict(df)
        p = pd.DataFrame(predict)
        p.to_csv(fname, index=False)

        # predict = {'obj_%s' % (i): str(c)  for i, c in enumerate(predict)}
        # return jsonify(predict)

        return send_file(fname, 
                        mimetype='text/csv',
                        attachment_filename=fname,
                        as_attachment=True)
    return render_template('submit.html', form=form)

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'csv', 'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename+'uploaded')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded'
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
