from FaceDetectionNN import FaceDetectionNN
import glob
import cv2
import numpy as np


def main():
    train = False

    nn = FaceDetectionNN()

    if train:
        nn.train()




    candidateFiles = sorted(glob.glob("./testing/*"))

    labelGeneric = [0]*len(candidateFiles)
    index = 0

    correct = 0
    total = 0
    for candiditeFile in candidateFiles:
        imageFiles = glob.glob(candiditeFile + '/*')
        label = labelGeneric.copy()
        label[index] = 1

        for file in imageFiles:
            img = cv2.imread(file)
            img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)
            img = np.asarray([img])

            prediction = nn.predict(img)[0]
            print(np.where(prediction == max(prediction))[0][0])
            print(index)
            print()

            if index == np.where(prediction == max(prediction))[0][0]:
                correct += 1
            total += 1

        index += 1

    print(correct/total, "% correct")

    # testFiles = glob.glob("./TestImages/*/*")
    #
    # for file in testFiles:
    #
    #     img = cv2.imread(file)
    #     img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)
    #
    #     img = np.asarray([img])
    #
    #     prediction = nn.predict(img)[0]
    #     print(prediction)
    #
    #     print(np.where(prediction == max(prediction))[0][0])

    img = cv2.imread(testFiles[2])
    img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)

    name = "Results/saliency_" + testFiles[2].split('/')[-1]

    nn.showSaliencyMap(img, name)


if __name__ == "__main__":
    main()
