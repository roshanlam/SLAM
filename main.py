from typing import Tuple
import cv2
import numpy as np
from display import Display
from extractor import Extractor
import json
from datetime import datetime

W, H = 1920 // 2, 1080 // 2
SIZE: Tuple[int, int] = (W, H)
F = 270
K = np.array(([F, 0, W // 2], [0, F, H // 2], [0, 0, 1]))
display = Display(SIZE)
ex = Extractor(K)

class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def process_frame(img):
    img = cv2.resize(img, SIZE)
    matches = ex.extract(img)
    print("%d matches" % (len(matches)))
    now = datetime.now()
    current_date = now.strftime("%d/%m/%Y %H:%M:%S")
    info = json.dumps(matches, cls=NumpyArrayEncoder)
    output_list = [{
        'date': current_date,
        'matches': info,
    }]
    with open('data.json', 'w') as file:
        json.dump(output_list, file, indent=4)
    for pt1, pt2 in matches:
        u1, v1 = ex.denormalise(pt1)
        u2, v2 = ex.denormalise(pt2)
        cv2.circle(img, (u1, v1), color=(0, 255, 0), radius=3)
        cv2.line(img, (u1, v1), (u2, v2), (255, 0, 0))
    display.paint(img)

if __name__ == "__main__":
    cap = cv2.VideoCapture("countryroad.mp4")
    while cap.isOpened():
        display.poll()
        ret, frame = cap.read()
        if ret:
            process_frame(frame)
        else:
            break