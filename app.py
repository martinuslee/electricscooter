import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
from PIL.ExifTags import TAGS

app = Flask(__name__)

@app.route('/upload')
def render_file():
    return render_template('upload.html')

@app.route('/fileUpload', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        #저장할 경로 + 파일명
        f.save('/Users/jongheon/dev/electricscooter/static/uploads/' + secure_filename(f.filename))
        #f = request.files['file1'].read()
        image = Image.open('/Users/jongheon/dev/electricscooter/static/uploads/' + secure_filename(f.filename))
        info = image._getexif();
        image.close()
        # 새로운 딕셔너리 생성
        taglabel = {}
        
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            taglabel[decoded] = value

        exifGPS = taglabel['GPSInfo']
        latData = exifGPS[2]
        lonData = exifGPS[4]

        # 도, 분, 초 계산
        latDeg = latData[0][0] / float(latData[0][1])
        latMin = latData[1][0] / float(latData[1][1])
        latSec = latData[2][0] / float(latData[2][1])
        
        lonDeg = lonData[0][0] / float(lonData[0][1])
        lonMin = lonData[1][0] / float(lonData[1][1])
        lonSec = lonData[2][0] / float(lonData[2][1])
        
        # 도, 분, 초로 나타내기
        Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
        Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]
        
        print(Lat, Lon)
        
        # 도 decimal로 나타내기
        # 위도 계산
        Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
        # 북위, 남위인지를 판단, 남위일 경우 -로 변경
        if exifGPS[1] == 'S': Lat = Lat * -1
        
        # 경도 계산
        Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
        # 동경, 서경인지를 판단, 서경일 경우 -로 변경
        if exifGPS[3] == 'W': Lon = Lon * -1
        
        print(Lat, ",",  Lon)
        value = [Lat,Lon]
    return value


@app.route('/map')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)