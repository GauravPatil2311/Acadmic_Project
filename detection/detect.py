# !pip install easyocr
# !pip install imutils

import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr
import os

from django.conf.urls.static import static
from django.conf import settings


# ### importing required libraries
# import torch
# import cv2
# import time
# # import pytesseract
# import re
# import numpy as np
# import easyocr


# ##### DEFINING GLOBAL VARIABLE
# EASY_OCR = easyocr.Reader(['en']) ### initiating easyocr
# OCR_TH = 0.2




# ### -------------------------------------- function to run detection ---------------------------------------------------------
# def detectx (frame):
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))


#         bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
#         edged = cv2.Canny(bfilter, 30, 200) #Edge detection
#         plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))


#         keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         contours = imutils.grab_contours(keypoints)
#         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

#         location = 0
#         for contour in contours:
#             approx = cv2.approxPolyDP(contour, 10, True)
#             if len(approx) == 4:
#                 location = approx
#                 break
                
#         mask = np.zeros(gray.shape, np.uint8)

#         (x,y) = np.where(mask==255)
#         if(len(x)>0):
#             (x1, y1) = (np.min(x), np.min(y))
#             (x2, y2) = (np.max(x), np.max(y))
#             cropped_image = gray[x1:x2+1, y1:y2+1]


#             plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))


#             reader = easyocr.Reader(['en'])
#             result = reader.readtext(cropped_image)
#             print(result)


# ### ------------------------------------ to plot the BBox and results --------------------------------------------------------
# def plot_boxes(result, frame):

#     """
#     --> This function takes results, frame and classes
#     --> results: contains labels and coordinates predicted by model on the given frame
#     --> classes: contains the strting labels
#     """
#     cord = result

#     x_shape, y_shape = frame.shape[1], frame.shape[0]

#     ### looping through the detections
#     # for i in range(n):
#     for i in range(1):
#         row = cord
#         if row[4] >= 0.55: ### threshold value for detection. We are discarding everything below this value
#             print(f"[INFO] Extracting BBox coordinates. . . ")
#             x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape) ## BBOx coordniates
            
#             # cv2.imwrite("./output/dp.jpg",frame[int(y1):int(y2), int(x1):int(x2)])

#             coords = [x1,y1,x2,y2]

#             plate_num = recognize_plate_easyocr(img = frame, coords= coords, reader= EASY_OCR, region_threshold= OCR_TH)


#             # if text_d == 'mask':
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) ## BBox
#             cv2.rectangle(frame, (x1, y1-20), (x2, y1), (0, 255,0), -1) ## for text label background
#             cv2.putText(frame, f"{plate_num}", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255), 2)

#             # cv2.imwrite("./output/np.jpg",frame[int(y1)-25:int(y2)+25, int(x1)-25:int(x2)+25])

#     return frame



# #### ---------------------------- function to recognize license plate --------------------------------------


# # function to recognize license plate numbers using Tesseract OCR
# def recognize_plate_easyocr(img, coords,reader,region_threshold):
#     # separate coordinates from box
#     xmin, ymin, xmax, ymax = coords
#     # get the subimage that makes up the bounded region and take an additional 5 pixels on each side
#     # nplate = img[int(ymin)-5:int(ymax)+5, int(xmin)-5:int(xmax)+5]
#     nplate = img[int(ymin):int(ymax), int(xmin):int(xmax)] ### cropping the number plate from the whole image


#     ocr_result = reader.readtext(nplate)



#     text = filter_text(region=nplate, ocr_result=ocr_result, region_threshold= region_threshold)

#     if len(text) ==1:
#         text = text[0].upper()
#     return text


# ### to filter out wrong detections 

# def filter_text(region, ocr_result, region_threshold):
#     rectangle_size = region.shape[0]*region.shape[1]
    
#     plate = [] 
#     print(ocr_result)
#     for result in ocr_result:
#         length = np.sum(np.subtract(result[0][1], result[0][0]))
#         height = np.sum(np.subtract(result[0][2], result[0][1]))
        
#         if length*height / rectangle_size > region_threshold:
#             plate.append(result[1])
#     return plate





# ### ---------------------------------------------- Main function -----------------------------------------------------

# def main():

#     ## reading the video
#     cap = cv2.VideoCapture(0)

#     # assert cap.isOpened()
#     frame_no = 1

#     while True:
#         # start_time = time.time()
#         ret, frame = cap.read()
#         cv2.imshow('frame', frame)

#         if ret  and frame_no %1 == 0:
#             print(f"[INFO] Working with frame {frame_no} ")

#             frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
#             result = detectx(frame)
#             frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)


#             # frame = plot_boxes(result, frame)

#             if cv2.waitKey(5) & 0xFF == ord('q'):
#                 break
#             frame_no += 1
        
#         print(f"[INFO] Clening up. . . ")
#     ### releaseing the writer
#     cap.release()
        
#     ## closing all windows
#     cv2.destroyAllWindows()



### -------------------  calling the main function-------------------------------


# main(vid_path="./test_images/vid_1.mp4",vid_out="vid_1.mp4") ### for custom video
# main(vid_path=0,vid_out="webcam_facemask_result.mp4") #### for webcam

# main(img_path="./test_images/Cars74.jpg") ## for image


# def detect():
#     # main()
#     # define a video capture object
#     vid = cv2.VideoCapture(0)
    
#     while(True):
        
#         # Capture the video frame by frame
#         ret, img = vid.read()
    
#         # Display the resulting frame
#         cv2.imshow('frame', img)
        
#         #img = cv2.imread('image4.jpg')
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))


#         bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
#         edged = cv2.Canny(bfilter, 30, 200) #Edge detection
#         plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))


#         keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         contours = imutils.grab_contours(keypoints)
#         contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

#         location = 0
#         for contour in contours:
#             approx = cv2.approxPolyDP(contour, 10, True)
#             if len(approx) == 4:
#                 location = approx
#                 break
                
#         mask = np.zeros(gray.shape, np.uint8)
#         new_image = cv2.drawContours(mask, [location], 0,255, -1)
#         new_image = cv2.bitwise_and(img, img, mask=mask)


#         plt.imshow(cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB))


#         (x,y) = np.where(mask==255)
#         (x1, y1) = (np.min(x), np.min(y))
#         (x2, y2) = (np.max(x), np.max(y))
#         cropped_image = gray[x1:x2+1, y1:y2+1]


#         plt.imshow(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB))


#         reader = easyocr.Reader(['en'])
#         result = reader.readtext(cropped_image)
#         print(result)


#         # text = result[0][-2]
#         # font = cv2.FONT_HERSHEY_SIMPLEX
#         # res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
#         # res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
#         # plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
        
#         # the 'q' button is set as the
#         # quitting button you may use any
#         # desired button of your choice
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # After the loop release the cap object
#     vid.release()
#     # Destroy all the windows
#     cv2.destroyAllWindows()


def detect():
    directory = settings.MEDIA_ROOT
        # Change the current directory 
        # to specified directory 
    os.chdir(directory)

    vid = cv2.VideoCapture(0)
    vid.set(cv2.CAP_PROP_POS_FRAMES, 1)

    count = 0

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
            font = cv2.FONT_HERSHEY_SIMPLEX
            res = cv2.putText(img, text=text, org=(approx[0][0][0], approx[1][0][1]+60), fontFace=font, fontScale=1, color=(0,255,0), thickness=2, lineType=cv2.LINE_AA)
            res = cv2.rectangle(img, tuple(approx[0][0]), tuple(approx[2][0]), (0,255,0),3)
            # plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

            cv2.imshow('Processed Frame',res)

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
            if (cv2.waitKey(30) & 0xff) == (ord('q') or ret):
                break

        # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
