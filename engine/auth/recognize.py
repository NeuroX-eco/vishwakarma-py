"""
Vishwakarma AI - Face Authentication Module
© 2025 Vishwakarma Industries

This module handles face authentication using a trained model.
"""
import cv2
import os
from engine.config import TRAINER_FILE, CASCADE_PATH

# Constants
FONT = cv2.FONT_HERSHEY_SIMPLEX
CONFIDENCE_THRESHOLD = 100

class FaceAuthenticator:
    """
    Handles face authentication using a pre-trained LBPH face recognizer.
    """
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
        self.authenticated_user_id = None
        self.names = ['', 'User']  # Names corresponding to user IDs

        if not os.path.exists(TRAINER_FILE):
            raise FileNotFoundError(f"No trained model found at {TRAINER_FILE}. Please train the model first.")
        self.recognizer.read(TRAINER_FILE)

    def get_authenticated_user_id(self):
        """
        Returns the ID of the authenticated user.
        """
        return self.authenticated_user_id

    def authenticate(self):
        """
        Starts the face authentication process.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cam.set(3, 640)
        cam.set(4, 480)

        min_w = 0.1 * cam.get(3)
        min_h = 0.1 * cam.get(4)

        while True:
            ret, img = cam.read()
            if not ret:
                print("Failed to grab frame")
                break

            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(
                gray_img,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(min_w), int(min_h))
            )

            auth_successful = self._process_faces(img, gray_img, faces)
            cv2.imshow('camera', img)

            if cv2.waitKey(10) & 0xFF == 27 or auth_successful:
                break

        cam.release()
        cv2.destroyAllWindows()
        return auth_successful

    def _process_faces(self, img, gray_img, faces):
        """
        Processes detected faces and predicts the user.

        Args:
            img (numpy.ndarray): The original image.
            gray_img (numpy.ndarray): The grayscale image.
            faces (list): A list of detected faces.

        Returns:
            bool: True if a user is successfully authenticated, False otherwise.
        """
        auth_successful = False
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            user_id, confidence = self.recognizer.predict(gray_img[y:y+h, x:x+w])

            if confidence < CONFIDENCE_THRESHOLD:
                self.authenticated_user_id = user_id
                display_name = self.names[user_id] if user_id < len(self.names) else "User"
                confidence_text = f"{round(100 - confidence)}%"
                auth_successful = True
            else:
                self.authenticated_user_id = None
                display_name = "Unknown"
                confidence_text = f"{round(100 - confidence)}%"

            self._draw_text(img, display_name, x + 5, y - 5)
            self._draw_text(img, confidence_text, x + 5, y + h - 5, color=(255, 255, 0))

        return auth_successful

    def _draw_text(self, img, text, x, y, color=(255, 255, 255)):
        """
        Draws text on the image.

        Args:
            img (numpy.ndarray): The image to draw on.
            text (str): The text to draw.
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            color (tuple, optional): The color of the text. Defaults to (255, 255, 255).
        """
        cv2.putText(img, text, (x, y), FONT, 1, color, 2)

if __name__ == '__main__':
    try:
        authenticator = FaceAuthenticator()
        if authenticator.authenticate():
            print(f"Authenticated user ID: {authenticator.get_authenticated_user_id()}")
        else:
            print("Authentication failed.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
