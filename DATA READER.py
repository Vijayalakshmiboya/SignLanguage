import cv2
import mediapipe as mp
import pandas as pd
import os
from math import sqrt
asl_dataset_directory = r"asl_dataset"
def read_files(dataset_directory):
    file_list, sub_list = [], []
    start_dir = dataset_directory
    subdirs = [x[0] for x in os.walk(start_dir)]
    for subdir in subdirs:
        files = os.walk(subdir).__next__()[2]
        if (len(files) > 0):
            for file in files:
                file_list.append(os.path.join(subdir, file))
                sub_list.append(str(subdir)[-1])
    zipped = zip(file_list, sub_list)
    return zipped
def scale(Ax, Ay, Bx, By, Cx, Cy):  
    return round(
        sqrt(((float(Bx) - (float(Ax) + float(Cx)) / 2) ** 2) + (float(By) - (float(Ay) + float(Cy)) / 2) ** 2), 2)
def distance(point_1, point_2):    
    return round(sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] + point_2[1]) ** 2), 2)
def angle(point_1, point_2):
   
    return round((point_1[1] - point_2[1]) / (point_1[0] - point_2[0]), 4)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
angle_list = []
df = pd.DataFrame(columns=range(21))  

files_subs = read_files(asl_dataset_directory)
with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.8) as hands:
    for file, sub in files_subs:
        img_flipped = cv2.imread(file)
        img = cv2.flip(img_flipped, 1)      
        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))       
        if not results.multi_hand_landmarks:
            continue
        image_height, image_width, _ = img.shape

        for hand_landmarks in results.multi_hand_landmarks:
           
            wrist = (hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * image_width,
                     hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * image_height)
            thumb_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width,
                         hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height)
            pointer_palm = (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x * image_width,
                            hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y * image_height)
            pointer_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width,
                           hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
            middle_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width,
                          hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height)
            ring_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width,
                        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height)
            pinky_palm = (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x * image_width,
                          hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y * image_height)
            pinky_tip = (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width,
                         hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height)
          
            angle_list = [
                sub,  
                angle(wrist, thumb_tip), 
                angle(wrist, pointer_tip),
                angle(wrist, middle_tip),
                angle(wrist, ring_tip),
                angle(wrist, pinky_tip),
                angle(thumb_tip, pointer_tip),
                angle(thumb_tip, middle_tip),
                angle(thumb_tip, ring_tip),
                angle(thumb_tip, pinky_tip),
                angle(middle_tip, ring_tip),
                angle(middle_tip, pinky_tip),
                angle(pointer_palm, pointer_tip),
                angle(pointer_palm, middle_tip),
                angle(pointer_palm, ring_tip),
                angle(pointer_palm, pinky_tip),
                angle(pinky_palm, pointer_tip),
                angle(pinky_palm, middle_tip),
                angle(pinky_palm, ring_tip),
                angle(pinky_palm, pinky_tip),
                angle(pointer_palm, pinky_palm)
            ]
            df = df.append(pd.Series(angle_list, index=df.columns), ignore_index=True)
            print(angle_list)
df.to_csv(asl_dataset_directory + ".csv", header=False, index=False)