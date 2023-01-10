import cv2
from pyzbar.pyzbar import decode
import re

def write_name(name):
    res = re.search("b'(.*)'", str(name))
    with open('data/presenze.csv', 'a') as f:
        f.write(str(res.group(1)) + "\n")


def BarcodeReader(image):
    
    # convert in numpy array
    img = cv2.imread(image)

    # decode image
    detectedBarcodes = decode(img)

    # if nothing is detected
    if detectedBarcodes:
        for barcode in detectedBarcodes:
            # locate barcode in image
            (x, y, w, h) = barcode.rect
            # cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2)

            if barcode.data!="":
                write_name(barcode.data)
                print(barcode.data)

    # the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Take the image from user
    image="data\MarioRossi.png"
    BarcodeReader(image)