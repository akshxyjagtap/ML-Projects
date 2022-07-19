import random
import pytesseract
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import glob
from datetime import datetime
import os

import easyocr
reader = easyocr.Reader(['en'])


df = pd.read_csv("indian_license_plates.csv")
df["image_name"] = df["image_name"] + ".jpeg"
df.drop(["image_width", "image_height"], axis=1, inplace=True)


WIDTH = 224
HEIGHT = 224



def detect(index):

    image = cv2.imread("Indian Number Plates/" + df["image_name"].iloc[index])
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, dsize=(WIDTH, HEIGHT))

    tx = int(df["top_x"].iloc[index] * WIDTH)
    ty = int(df["top_y"].iloc[index] * HEIGHT)
    bx = int(df["bottom_x"].iloc[index] * WIDTH)
    by = int(df["bottom_y"].iloc[index] * HEIGHT)
    # print(tx, bx, ty, by)
    # image = cv2.rectangle(image, (tx, ty), (bx, by), (0, 0, 255), 1)
    # # plt.imshow(image)
    # cropped_image = image[ty:by,tx:bx,]

    # plt.imshow(cropped_image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("greyed image", gray_image)
    # cv2.imwrite('./' + "greyed image" + '.png', gray_image)
    # cv2.waitKey(0)

    gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
    # cv2.imshow("smoothened image", gray_image)
    # cv2.imwrite('./' + "smoothened image" + '.png', gray_image)
    # cv2.waitKey(0)

    edged = cv2.Canny(gray_image, 30, 200)
    # cv2.imshow("edged image", edged)
    # cv2.imwrite('./' + "edged" + '.png', edged)
    # cv2.waitKey(0)

    image_identified = cv2.rectangle(gray_image, (tx, ty), (bx, by), (0, 0, 255), 1)
    print_image = cv2.rectangle(image, (tx, ty), (bx, by), (0, 0, 255), 1)

    # for ui
    cropped_image = image[ty:by,tx:bx,]
    # for ocr
    cropped_image_identifed = image_identified[ty:by, tx:bx,]

    #1
    pytesseract.pytesseract.tesseract_cmd = 'C:/Install/tesseract/tesseract.exe'
    predicted_result = pytesseract.image_to_string(cropped_image_identifed, lang='eng')

    # 2
    result = reader.readtext(cropped_image_identifed,detail=0)
    print(result)

    with open("recognized.csv", mode='a') as file1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        file1.write(" \n")
        # final = str(current_time) + " , "+ str(result)
        # final = pd.DataFrame( [[current_time, str(result)]], columns=['time', 'recognised_plate'])
        final = pd.DataFrame([[current_time, str(result)]])

        final.to_csv(file1, index= False)


    plt.imshow(print_image)
    title = "Identified Plate : " + " ".join(result)
    plt.title(title)
    plt.show()


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# to generate samples
for i in range(0,50):
    detect(random.randint(0,210))


