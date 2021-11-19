import cv2
import numpy
import torch

!git clone https://github.com/ultralytics/yolov3
#YOLOv3 (You Only Look Once, Version 3) is a real-time object detection algorithm that identifies specific objects in videos, live feeds, or images.

%cd yolov3/

%ls

%pip install -r requirements.txt

!python detect.py --source 'car.jpg'

!python detect.py --source 'test.mkv'
