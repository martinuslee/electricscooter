import os
import torch
from flask import Flask, jsonify, url_for, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import ssl
from PIL import Image
import uuid
#from PIL.ExifTags import TAGS,GPSTAGS
#from GPSPhoto import gpsphoto
#import io, os, requests

app = Flask(__name__)


model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='./static/models/best.pt')  # default
# torch model include
model.eval()  # evaluation print
model.conf = 0.25  # confidence threshold (0-1)
model.iou = 0.45  # NMS IoU threshold (0-1)


# nohup python3 -u app.py &
# tail -f nohup.out
# 종료 lsof -i :5550

# image model output save function return results object
def get_prediction(img_bytes):
    # Inference
    results = model(img_bytes, size=640)  # includes NMS
    PATH = 'static/results/'
    results.save(PATH)
    return results


object_list = list()  # empty list


def results_img(results):
    object_list.clear()  # make it clear
    global msg  # global variable declaration
    print(results.names)  # print object elements name
    pred = results.pred  # prediction allocation
    for i in pred[0]:  # for loop for predicted objs
        # print(int(i[-1]))
        # print(results.names[int(i[-1])])
        objects = results.names[int(i[-1])]
        object_list.append(objects)
        #detected = object_list
        #detected = copy.deepcopy(object_list)

        # if(objects != 'electric_scooter'):
        #     msg = '주차하시면안되용!'
        # else:
        #     msg = '주차하셔도 좋은 장소 입니다.'
        # return msg

    if(any('electric_scooter' in i for i in object_list) != True):  # not e-scooter in photo
        return '킥보드가 검출되지 않았습니다. 재촬영 해주세요!'

    # if any object in photo
    output = any(
        'brailleblock' in i or 'crosswalk' in i or 'fireplug' in i for i in object_list)
    print(output)

    if output:
        return "주차 불가 구역입니다."  # why? reference info page
    else:
        return "주차 가능한 장소입니다."

# print(results.names[int(results.pred[0][0][-1])])


@app.route('/upload')
def render_file():
    return render_template('upload.html')  # render upload (main) page

@app.route('/info')
def render_info():
    return render_template('info.html')  # render upload (main) page


@app.route('/fileUpload', methods=['GET', 'POST'])
def upload_file():
    global check_msg
    if request.method == 'POST':  # REST API POST METHOD
        if 'file' not in request.files:
            return redirect(request.url)  # bad access redirect
        f = request.files['file']  # variable allocate file
        # 저장할 경로 + 파일명 save
        #newname = str(uuid.uuid4()) + '.jpg' #random string name image
        #f.filename = os.rename(f.filename, newname)
        f.save('/home/dkjh/datacampus/electricscooter/static/photos/' +
               secure_filename(f.filename))  # file save path to ./static
        # print(uuid.uuid4())

        print(secure_filename(f.filename))  # print file(photo name)

        image = Image.open(request.files['file'].stream)  # open image
        #img_bytes = file.read()
        results = get_prediction(image)  # predict

        #image_names = os.listdir(img_path)

        #data = gpsphoto.getGPSData('/home/dkjh/datacampus/electricscooter/static/photos/' + secure_filename(f.filename))
        # print(data)
        #print(data['Latitude'], data['Longitude'])
        #geocode = data['Latitude'], data['Longitude']
        #img_path = '/home/dkjh/datacampus/electricscooter/runs/detect/exp/image0.jpg'

        check_msg = results_img(results)
    # return render_template('index.html', geocode = geocode, check = check_msg)
    return render_template('index.html', check=check_msg, obj=object_list)


if __name__ == '__main__':
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='/usr/local/ssl/server.crt',
                                keyfile='/usr/local/ssl/server.key', password='bluesea34')
    app.run(host='0.0.0.0', port='5550', debug=True, ssl_context=ssl_context)
