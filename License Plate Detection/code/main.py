import cv2
import imutils
import pytesseract
import pandas as pd

def detect(index):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Install/tesseract/tesseract.exe'
    df = pd.read_csv("indian_license_plates.csv")
    df["image_name"] = df["image_name"] + ".jpeg"
    df.drop(["image_width", "image_height"], axis=1, inplace=True)

    image = cv2.imread("Indian Number Plates/" + df["image_name"].iloc[index])
    image = imutils.resize(image, width=300 )
    # cv2.imshow("original image", image)
    # cv2.imwrite('./' + "original image" + '.png', image)
    cv2.waitKey(0)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("greyed image", gray_image)
    # cv2.imwrite('./' + "greyed image" + '.png', gray_image)
    cv2.waitKey(0)

    gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
    # cv2.imshow("smoothened image", gray_image)
    # cv2.imwrite('./' + "smoothened image" + '.png', gray_image)
    cv2.waitKey(0)

    edged = cv2.Canny(gray_image, 30, 200)
    # cv2.imshow("edged image", edged)
    # cv2.imwrite('./' + "edged" + '.png', edged)
    cv2.waitKey(0)

    cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image1 = image.copy()
    cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
    # cv2.imshow("contours", image1)
    cv2.waitKey(0)

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    screenCnt = None
    image2 = image.copy()
    cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
    # cv2.imshow("Top 30 contours", image2)
    cv2.waitKey(0)

    i = 7
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
            screenCnt = approx
            x, y, w, h = cv2.boundingRect(c)
            new_img = image[y:y + h, x:x + w]
            cv2.imwrite('./' + str(i) + '.png', new_img)
            i += 1
            break

    Cropped_loc = './7.png'
    cv2.imshow("cropped", cv2.imread(Cropped_loc))
    plate = pytesseract.image_to_string(Cropped_loc, lang='eng')
    print("Number plate is:", plate)

    import easyocr
    reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
    plate = reader.readtext(Cropped_loc, detail=0)
    print("Number plate is:", plate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect(15)