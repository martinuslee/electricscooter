# electricscooter

**공유 전동 킥보드 불법 주차 예방 및 주차 입지 추천 웹 서비스**

<table style="border: 1px solid transparent" align="center">
  <tr>
    <td><img src="https://user-images.githubusercontent.com/70839563/131092082-efd87497-86ca-4adc-a17d-fe35324c8bd9.png" width="30%"/><td>
    <td><img src="https://user-images.githubusercontent.com/70839563/131092097-137abb99-8baf-455c-8b77-eb17768476b5.png" width="30%"/><td>
  </tr>
</table>

[웹 사이트 바로가기](https://1.222.84.186:5550/upload).

- **Contributors** : 이종헌, 윤영민, 최인수, 이가원, 석주애
- **Project integration management & Web FullStack Development** : 이종헌
- **DeepLearning model fitting & fine tuing** : 이종헌, 윤영민
- **Image Dataset crawling & preprocessing** : 윤영민
- **Collecting Public Data & preprocessing** : 최인수, 이가원, 석주애
- **Location Data Analysis using Python, QGIS** : 최인수, 이가원, 석주애
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
5. templates/
- html files
6. yolov5/
- yolov5 repository
7. app.py
- flask web server code
8. electricScooter.ipynb
- Yolo v5 model training Jupyter notebook code.
9. result_es.ipynb
- Yolo v5 model detect code with cv2






