# electricscooter

**공유 전동 킥보드 불법 주차 예방 및 주차 입지 추천 웹 서비스**

<p align="center"><img src="https://user-images.githubusercontent.com/70839563/131092082-efd87497-86ca-4adc-a17d-fe35324c8bd9.png" width="30%"/><img src="https://user-images.githubusercontent.com/70839563/131092097-137abb99-8baf-455c-8b77-eb17768476b5.png" width="30%"/></p>

[웹 사이트 바로가기](https://1.222.84.186:5550/upload).

- **Contributors** : 이종헌, 윤영민, 최인수, 이가원, 석주애
- **Team Leader** : 이종헌
- **Project integration management & Web FullStack Development** : 이종헌
- **DeepLearning model fitting & fine tuing** : 이종헌, 윤영민
- **Image Dataset crawling & preprocessing** : 윤영민
- **Collecting Public Data & preprocessing** : 최인수, 이가원, 석주애
- **Location Data Analysis using Python, QGIS** : 최인수, 이가원, 석주애
- **Project Mentor** : 김상수
---------------------------------------

## Configuration
```
pip3 install flask 
pip3 install torch #reference https://pytorch.org/get-started/locally/ 
pip install -qr https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt 
```
Start from a Python>=3.8 environment with PyTorch>=1.7 installed. 
To install PyTorch see https://pytorch.org/get-started/locally/.

---------------------------------------
## Project Structure
1. es_project/
  - Yolo v5 dataset
2. images/
  - raw image dataset (4 classes)
3. static/
   1. css/
       - web stylesheets
   2. icon/
       - icon image files
   3. models/
       - Yolo v5 custom weight models
   4. photos/
       - user upload images
   5. results/
       - object detected image
4. runs/
 - test image data results
5. analysis/
 - Open Data Analysis
 1. code/ 
       - source code
 3. rawdata/
       - raw open data files
6. templates/
- html files
7. yolov5/
- yolov5 repository
8. app.py
- flask web server code
9. electricScooter.ipynb
- Yolo v5 model training Jupyter notebook code.
10. result_es.ipynb
- Yolo v5 model detect code with cv2

---------------------------------------
## Activity Diagram

<img width="578" alt="image" src="https://user-images.githubusercontent.com/70839563/131221688-541cc682-8d54-4040-9c3c-b7b20b9bad9f.png">

<img width="933" alt="image" src="https://user-images.githubusercontent.com/70839563/131221774-92fef9a2-a3e4-4582-860c-fb8d11f9c20a.png">




