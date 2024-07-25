import threading
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import os

from django.conf.urls.static import static
from django.conf import settings

from .models import *
from .SMSLab import sendsms

def trash():
    directory = settings.MEDIA_ROOT
        # Change the current directory 
        # to specified directory 
    os.chdir(directory)

    vid = cv2.VideoCapture(0)
    vid.set(cv2.CAP_PROP_POS_FRAMES, 1)

    count = 0

    prev_vehicle = None
    
    while (True):

            # Capture the video frame by frame
            ret, img = vid.read()

            # # Display the resulting frame
            # cv2.imshow('frame', img)

            # img = cv2.imread('image4.jpg')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)

            bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # Noise reduction
            edged = cv2.Canny(bfilter, 30, 200)  # Edge detection
            # plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

            keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(keypoints)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

            location = 0
            for contour in contours:
                approx = cv2.approxPolyDP(contour, 10, True)
                if len(approx) == 4:
                    location = approx
                    break

            mask = np.zeros(gray.shape, np.uint8)

            try:
                new_image = cv2.drawContours(mask, [location], 0, 255, -1)
                new_image = cv2.bitwise_and(img, img, mask=mask)

                # plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))

                (x, y) = np.where(mask == 255)
                (x1, y1) = (np.min(x), np.min(y))
                (x2, y2) = (np.max(x), np.max(y))
                cropped_image = gray[x1:x2+1, y1:y2+1]

                # plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))
                count=count+1
                videodirname = str(os.getcwd())
                cv2.imwrite(str(videodirname+"\\"+str(count)+".jpg"),new_image)

                reader = easyocr.Reader(['en'])
                result = reader.readtext(cropped_image)
                print(result)

            
                text = result[0][-2]
                text = text.upper()
                text = text[0:10:1]

                curr_vehicle = Vehicle.objects.get(registration_no = text)
                if(curr_vehicle!=None and curr_vehicle.registration_no != prev_vehicle):
                    print("Detected")
                    # sendsms(curr_vehicle.email)
                    print(curr_vehicle.mobile)
                    t = threading.Thread(target = sendsms,args=(curr_vehicle.mobile,))
                    t.start()
                
                prev_vehicle = text

                # curr_vehicle = Vehicle.objects.get(registration_no = text)
                # if(prev_vehicle.registration_no != curr_vehicle.registration_no):
                #     prev_vehicle=curr_vehicle
                #     # sendsms(curr_vehicle.mobile)
                #     t = threading.Thread(target = sendsms,args=(curr_vehicle.mobile,))
                #     t.start()

                font = cv2.FONT_HERSHEY_SIMPLEX
                res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
                res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
                # plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

                # cv2.imshow('Processed Frame',res)

                # the 'q' button is set as the
                # quitting button you may use any
                # desired button of your choice
                if (cv2.waitKey(30) & 0xff) == (ord('q') or ret):
                    break
            except:
                continue

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
