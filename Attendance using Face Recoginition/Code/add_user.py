import cv2
import numpy as np

#file_name=input("Enter Name of the person")
def datset(name):
    dataset_path = './data/'
    face_data = []
    skip = 0
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    haar_file = 'haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(haar_file)

    while True:
        (ret, im) = webcam.read()
        if ret == False:
            continue

        gray_frame = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(im, 1.3, 5)
        faces = sorted(faces, key=lambda f: f[2] * f[3])

        for face in faces[-1:]:
            x, y, w, h = face
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)

            offset = 10
            face_section = im[y - offset:y + h + offset, x - offset:x + w + offset]
            face_section = cv2.resize(face_section, (100, 100))

            # global skip
            # global face_data
            skip =skip+ 1
            if skip % 2 == 0:
                face_data.append(face_section)
                print(len(face_data))

            cv2.imshow("Frame", im)
            cv2.imshow("Face Section", face_section)

        key = cv2.waitKey(60) & 0xFF
        if key == ord(' '):
            break

    webcam.release()
    cv2.destroyAllWindows()

    file_name=name
    facedata = np.asarray(face_data)
    facedata = facedata.reshape((facedata.shape[0], -1))
    print(facedata.shape)


    np.save(dataset_path + file_name + '.npy', facedata)
    print(("Data saved successfully at", dataset_path + file_name + '.npy'))

    return facedata.shape[0]

# datset()


