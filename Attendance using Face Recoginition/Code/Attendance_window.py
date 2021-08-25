import cv2
import numpy as np
import os
from datetime import datetime
import pandas as pd


def detect():
    ################# KNN CODE ##################
    def distance(v1, v2):
        # Eucledian
        return np.sqrt(((v1 - v2) ** 2).sum())

    def knn(train, test, k=5):
        dist = []
        for i in range(train.shape[0]):
            # Get the vector and label
            ix = train[i, :-1]
            iy = train[i, -1]

            # Compute the distance from test point
            d = distance(test, ix)
            dist.append([d, iy])

        # Sort based on distance and get top k
        dk = sorted(dist, key=lambda x: x[0])[: k]

        # Retrieve only the labels
        labels = np.array(dk)[:, -1]

        # Get frequencies of each label
        output = np.unique(labels, return_counts=True)

        # Find max frequency and corresponding label
        index = np.argmax(output[1])
        return output[0][index]

    ###############################################

    # init camer
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # face detection
    haar_file = 'haarcascade_frontalface_alt.xml'
    face_cascade = cv2.CascadeClassifier(haar_file)

    skip = 0
    face_data = []
    labels = []
    dataset_path = './data/'
    class_id = 0
    names = {}
    global pred_name

    # Data Preparation
    for fx in os.listdir(dataset_path):
        if fx.endswith('.npy'):
            names[class_id] = fx[:-4]
            print("Loaded " + fx)
            data_item = np.load(dataset_path + fx)
            face_data.append(data_item)

            # Create Labels for the class
            target = class_id * np.ones((data_item.shape[0],))
            class_id += 1
            labels.append(target)

    face_dataset = np.concatenate(face_data, axis=0)
    face_labels = np.concatenate(labels, axis=0).reshape((-1, 1))

    print(face_dataset.shape)
    print(face_labels.shape)

    trainset = np.concatenate((face_dataset, face_labels), axis=1)
    print(trainset.shape)

    def markAttendance(name):
        with open('attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            now = datetime.now()
            time = now.strftime('%I:%M:%S')
            day = now.day
            month = now.month
            year = now.year
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])

            f.writelines(f'\n{name},{day},{month},{year},{time}')
            f.close()

    # testing
    while True:
        ret, im = cap.read()
        if ret == False:
            continue

        faces = face_cascade.detectMultiScale(im, 1.3, 5)

        for face in faces:
            x, y, w, h = face
            offset = 10
            face_section = im[y - offset:y + h + offset, x - offset:x + w + offset]
            face_section = cv2.resize(face_section, (100, 100))
            out = knn(trainset, face_section.flatten())
            # global pred_name
            pred_name = names[int(out)]
            cv2.putText(im, pred_name, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 255), 2)

        cv2.imshow("Faces", im)
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            break

    markAttendance(pred_name)
    cap.release()
    cv2.destroyAllWindows()

    df = pd.read_csv('attendance.csv')
    df.drop_duplicates(['name', 'day', 'month', 'year'], inplace=True)
    df.to_csv('attendance.csv', index=False)

# detect()