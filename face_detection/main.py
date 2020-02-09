from FaceDetectionNN import FaceDetectionNN
import glob
import cv2
import numpy as np


def main():
    train = True
    test = True
    detect_saliency = False

    nn = FaceDetectionNN(train)

    if train:
        nn.train()

    if test:

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


    if detect_saliency:

        saliencyFile = "./testing/Mark Sanford/Mark Sanford-135.jpeg"
        # saliencyFile = "./Other/Niko.jpg"

        img = cv2.imread(saliencyFile)
        img = cv2.resize(img, (64, 64),interpolation = cv2.INTER_AREA)

        name = "Results/saliency_" + saliencyFile.split('/')[-1]

        nn.showSaliencyMap(img, name)

        prediction = nn.predict(np.asarray([img]))[0]
        index = np.where(prediction == max(prediction))[0][0]


        candidateFiles = sorted(glob.glob("./testing/*"))
        print(candidateFiles[index].split('/')[-1])




if __name__ == "__main__":
    main()
