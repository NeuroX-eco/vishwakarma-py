"""
Vishwakarma AI - Face Recognition Trainer Module
© 2025 Vishwakarma Industries

This module trains the face recognition model using captured samples.
"""
import cv2
import numpy as np
from PIL import Image
import os

from engine.config import SAMPLES_PATH, TRAINER_PATH, TRAINER_FILE, CASCADE_PATH

class FaceTrainer:
    """
    Handles the training of the face recognition model.
    """
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier(CASCADE_PATH)

        if not os.path.exists(SAMPLES_PATH):
            raise FileNotFoundError(f"Samples directory not found at {SAMPLES_PATH}. Please collect samples first.")
        if not os.path.exists(TRAINER_PATH):
            os.makedirs(TRAINER_PATH)

    def train_model(self):
        """
        Trains the face recognition model and saves it to a file.
        """
        print("Training faces. This may take a few seconds...")
        faces, ids = self._get_images_and_labels()
        if not faces:
            print("No faces found for training. Please collect more samples.")
            return

        self.recognizer.train(faces, np.array(ids))
        self.recognizer.write(TRAINER_FILE)
        print(f"Model trained and saved as {TRAINER_FILE}")

    def _get_images_and_labels(self):
        """
        Fetches the images and corresponding labels from the samples directory.

        Returns:
            tuple: A tuple containing a list of face samples and a list of corresponding IDs.
        """
        image_paths = [os.path.join(SAMPLES_PATH, f) for f in os.listdir(SAMPLES_PATH)]
        face_samples = []
        ids = []

        for image_path in image_paths:
            try:
                gray_img = Image.open(image_path).convert('L')
                img_arr = np.array(gray_img, 'uint8')

                user_id = int(os.path.split(image_path)[-1].split(".")[1])
                faces = self.detector.detectMultiScale(img_arr)

                for (x, y, w, h) in faces:
                    face_samples.append(img_arr[y:y+h, x:x+w])
                    ids.append(user_id)
            except Exception as e:
                print(f"Error processing image {image_path}: {e}")

        return face_samples, ids

if __name__ == '__main__':
    try:
        trainer = FaceTrainer()
        trainer.train_model()
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
