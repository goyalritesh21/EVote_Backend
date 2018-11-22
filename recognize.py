import os

import cv2


def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    # Converting image to gray-scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecting features in gray-scale image, returns coordinates, width and height of features
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    # drawing rectangle around the feature and labeling it
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        # Predicting the id of the user
        id, predictionScore = clf.predict(gray_img[y:y+h, x:x+w])
        # Check for id of user and label the rectangle accordingly
        if predictionScore > 65:
            cv2.putText(img, str(id), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
            return id
        coords = [x, y, w, h]

    return id

# Method to recognize the person
def recognize(img, clf, faceCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255), "green": (0, 255, 0), "white": (255, 255, 255)}
    id = draw_boundary(img, faceCascade, 1.1, 10, color["white"], "Face", clf)
    return id


def load_images_from_folder(folder, filename):
    image = cv2.imread(os.path.join(folder, filename))
    return image


# Loading classifier
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Loading custom classifier to recognize
clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("classifier.yml")

Folder = "static/images/"


def recognize_adhaar(filename):
    # Reading image from video stream
    img = load_images_from_folder(Folder, filename)
    # Call method we defined above
    id = recognize(img, clf, faceCascade)
    # Writing processed image in a new window
    #cv2.imshow("face detection", img)
    return id
