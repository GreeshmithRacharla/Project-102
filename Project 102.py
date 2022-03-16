import cv2
import time
import dropbox
import random


start_time = time.time()


def take_snapshot():
    number = random.randint(0,50)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True 
    while(result):
        ret , frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name , frame)
        result = False

    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BDzOiPsXPxSNfLsD36CFR2uGkEhhw4wRzEoQUysZPZD0SBalsMPcQY50ob1atOv3VU8lH-FXzvemVZTLSXvdztllE6qSPS6uljm1wXUxZHv2Bb8uBglOFGElC7INpuNUu6ivodVeYEjn"
    file = img_name
    file_from = file
    file_to = "/testfolder/" + img_name
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to , mode = dropbox.files.WriteMode.overwrite)
        print("files uploded")

def main():
    while(True):
        if((time.time() - start_time) >= 2):
            name = take_snapshot()
            upload_file(name)

main()

    