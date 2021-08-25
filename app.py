import io
import os
import requests
import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect
from werkzeug.utils import secure_filename
from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS
from GPSPhoto import gpsphoto

app = Flask(__name__)

model = torch.hub.load('ultralytics/yolov5', 'custom', path='v5s_e300_best.pt')  # default
model.eval()

def get_prediction(img_bytes):
    # Inference
    results = model(img_bytes, size=640)  # includes NMS
    PATH = './static/'
    results.save(PATH)
    return results



def results_img(results):
    print(results.names)
    pred = results.pred
    for i in pred[0]:
    #print(int(i[-1]))
    #print(results.names[int(i[-1])])
        objects = results.names[int(i[-1])]
        print(objects)
        if(objects != 'electric_scooter'):
            msg = '주차하시면안되용!'
        else:
            msg = '주차하셔도 좋은 장소 입니다.'
    
    return msg
        
  

#print(results.names[int(results.pred[0][0][-1])])

@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        f = request.files['file']
        #저장할 경로 + 파일명
        f.save('/home/dkjh/datacampus/electricscooter/static/photos/' + secure_filename(f.filename))
        #f = request.files['file1'].read()
        image = Image.open(request.files['file'].stream)
        #img_bytes = file.read()
        results = get_prediction(image)
        
        #image_names = os.listdir(img_path)
        
        data = gpsphoto.getGPSData('/home/dkjh/datacampus/electricscooter/static/photos/' + secure_filename(f.filename))
        print(data)
        #print(data['Latitude'], data['Longitude'])
        geocode = data['Latitude'], data['Longitude']
        #img_path = '/home/dkjh/datacampus/electricscooter/runs/detect/exp/image0.jpg'

        check_msg = results_img(results)
    return render_template('index.html', geocode = geocode, check = check_msg)

'''
@app.route('/map')
def index():
    return render_template('index.html')
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5550', debug=True)
