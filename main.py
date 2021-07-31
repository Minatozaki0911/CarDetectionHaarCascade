import pyscreenshot
import cv2
import numpy as np
import time

def TakeScreenshot():
    img = pyscreenshot.grab(bbox=(20, 220, 1340, 800))
    img = np.array(img)
    img = img[:,:,::-1]
    return img

if __name__ == '__main__':
    poscount = 0
    negcount = 0
    cascade = cv2.CascadeClassifier('./cascade/cascade.xml')
    while True:
        prev = time.time()
        img = TakeScreenshot()
        img = np.array(img)
        box = cascade.detectMultiScale(img)
        for (x,y,w,h) in box:
            cv2.rectangle(img, (x,y), (x+w, y+h), (100,250,20), 3)
        cv2.imshow("Capture Screen", img)
        print('FPS: {}'.format(1/ (time.time()-prev)))
        key = cv2.waitKey(1)

        if key == ord('q'):
            cv2.destroyAllWindows()
            break
        if key == ord('p'):
            poscount += 1
            cv2.imwrite('./pos/positive{}.jpg'.format(poscount), img)
        if key == ord('n'):
            negcount += 1
            cv2.imwrite('./neg/negative{}.jpg'.format(negcount), img)

    cv2.destroyAllWindows()
