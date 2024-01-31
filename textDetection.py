import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

img = cv2.imread('/Users/seb/Documents/intermediatePython/white2.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert to RGB
#print(pytesseract.image_to_string(img))

#Detecintg characters


himg, wimg, _ = img.shape
cong = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_boxes(img, config=cong)
for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,himg-y), (w,himg-h), (0,0,255), 3)
    cv2.putText(img, b[0], (x,himg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)


#Detecintg words

#himg, wimg, _ = img.shape
#boxes = pytesseract.image_to_data(img)
#print(boxes)
#for x,b in enumerate(boxes.splitlines()):
#    if x!=0:
#        b = b.split( )
#        print(b)
#        if len(b)==12:
#            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#            cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 3)
#            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)

#Detecting digits

#himg, wimg, _ = img.shape
#config1 = r'--oem 3 --psm 6 outputbase digits'
#boxes = pytesseract.image_to_data(img, config=config1)
#print(boxes)
#for x,b in enumerate(boxes.splitlines()):
#   if x!=0:
#       b = b.split( )
#        print(b)
#        if len(b)==12:
#            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#            cv2.rectangle(img, (x,y), (w+x,h+y), (0,0,255), 3)
#            cv2.putText(img, b[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 2)


cv2.imshow('Result', img)
cv2.waitKey(0)




