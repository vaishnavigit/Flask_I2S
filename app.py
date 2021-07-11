from flask import Flask
from flask import request,redirect,render_template,url_for
from werkzeug.utils import secure_filename
import os
import pytesseract
from PIL import ImageFilter
from PIL import Image
import importlib
import sys
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract"
importlib.reload(sys)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './pictures'

@app.route('/')
def index():
    return render_template('firstpage.html')

@app.route('/submitImage/',methods=['POST',])
def submitImage():
    image = request.files['ocrImage']
    text = ''
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    text = pytesseract.image_to_string(img)
    f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename)+'.txt','w')
    f.write(text)
    f.close()
    return render_template('intotext.html',text=text,filename=f)


if __name__ == '__main__':
    app.run('0.0.0.0',8000,debug=True)
