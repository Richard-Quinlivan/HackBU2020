from FaceDetectionNN import FaceDetectionNN
import glob
import cv2
import numpy as np


def main():
    train = False

    nn = FaceDetectionNN()

    if train:
        nn.train()

    testFiles = glob.glob("./TrainImages/*/*")


    for file in testFiles:

        img = cv2.imread(file)
        img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)

        img = np.asarray([img])

        prediction = nn.predict(img)[0]
        print(prediction)

        print(np.where(prediction == max(prediction))[0][0])


if __name__ == "__main__":
    main()
