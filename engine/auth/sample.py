"""
Vishwakarma AI - Face Sample Capture Module
© 2025 Vishwakarma Industries

This module captures face samples for training the face recognition model.
"""
import cv2
import os
from engine.config import CASCADE_PATH, SAMPLES_PATH

# Constants
SAMPLE_COUNT = 100

class FaceSampleCollector:
    """
    Handles the collection of face samples for training.
    """
    def __init__(self, user_id):
        self.user_id = user_id
        self.detector = cv2.CascadeClassifier(CASCADE_PATH)
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam.set(3, 640)
        self.cam.set(4, 480)

        if not os.path.exists(SAMPLES_PATH):
            os.makedirs(SAMPLES_PATH)

    def collect_samples(self):
        """
        Starts the process of collecting face samples.
        """
        print("Taking samples, look at the camera...")
        count = 0
        while True:
            ret, img = self.cam.read()
            if not ret:
                print("Failed to grab frame")
                break

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.detector.detectMultiScale(gray_img, 1.3, 5)

            if self._process_faces(img, gray_img, faces, count):
                count += 1

            cv2.imshow('image', img)
            if cv2.waitKey(100) & 0xFF == 27 or count >= SAMPLE_COUNT:
                break

        print("Samples taken. Closing the program.")
        self.cam.release()
        cv2.destroyAllWindows()

    def _process_faces(self, img, gray_img, faces, count):
        """
        Processes detected faces and saves the samples.

        Args:
            img (numpy.ndarray): The original image.
            gray_img (numpy.ndarray): The grayscale image.
            faces (list): A list of detected faces.
            count (int): The current sample count.

        Returns:
            bool: True if a sample was saved, False otherwise.
        """
        sample_saved = False
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sample_path = os.path.join(SAMPLES_PATH, f"face.{self.user_id}.{count + 1}.jpg")
            cv2.imwrite(sample_path, gray_img[y:y+h, x:x+w])
            sample_saved = True
        return sample_saved

if __name__ == '__main__':
    try:
        user_id = input("Enter a Numeric user ID: ")
        if not user_id.isdigit():
            print("Invalid user ID. Please enter a numeric value.")
        else:
            collector = FaceSampleCollector(user_id)
            collector.collect_samples()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
