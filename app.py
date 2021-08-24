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
        #f.save('/Users/jongheon/dev/electricscooter/static/uploads/' + secure_filename(f.filename))
        #f = request.files['file1'].read()
        image = Image.open(request.files['file'].stream)
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
        #latDeg = latData[0][0] / (latData[0][1])
        #latMin = latData[1][0] / (latData[1][1])
        #latSec = latData[2][0] / (latData[2][1])
        latDeg = latData[0]
        latMin = latData[1] 
        latSec = latData[2]         
        
        lonDeg = lonData[0]
        lonMin = lonData[1]
        lonSec = lonData[2]     
        #lonDeg = lonData[0][0] / (lonData[0][1])
        #lonMin = lonData[1][0] / (lonData[1][1])
        #lonSec = lonData[2][0] / (lonData[2][1])
        
        # 도, 분, 초로 나타내기
        #Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
        #Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]
        
        #print(Lat, Lon)
        
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
        geocode = Lat, Lon
    return render_template('index.html', geocode = geocode)

'''
@app.route('/map')
def index():
    return render_template('index.html')
'''

if __name__ == '__main__':
    app.run(port=8080, debug=True)