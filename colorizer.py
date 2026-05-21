import cv2
import numpy as np
import os
import urllib.request


MODEL_URL = "https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1"


def download_model_if_missing(model_path):
    if not os.path.exists(model_path):
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        print("Downloading colorization model...")
        urllib.request.urlretrieve(MODEL_URL, model_path)
        print("Model downloaded successfully.")


class ImageColorizer:

    def __init__(self):

        self.model_dir = "models"

        self.prototxt_path = os.path.join(
            self.model_dir,
            "colorization_deploy_v2.prototxt"
        )

        self.model_path = os.path.join(
            self.model_dir,
            "colorization_release_v2.caffemodel"
        )

        self.points_path = os.path.join(
            self.model_dir,
            "pts_in_hull.npy"
        )

        self.net = None

    def load_model(self):

        if not os.path.exists(self.prototxt_path):
            raise FileNotFoundError(
                "Missing colorization_deploy_v2.prototxt"
            )

        if not os.path.exists(self.model_path):
            download_model_if_missing(self.model_path)

        if not os.path.exists(self.points_path):
            raise FileNotFoundError(
                "Missing pts_in_hull.npy"
            )

        self.net = cv2.dnn.readNetFromCaffe(
            self.prototxt_path,
            self.model_path
        )

        points = np.load(self.points_path)

        points = points.transpose().reshape(2, 313, 1, 1)

        self.net.getLayer(
            self.net.getLayerId("class8_ab")
        ).blobs = [points.astype("float32")]

        self.net.getLayer(
            self.net.getLayerId("conv8_313_rh")
        ).blobs = [
            np.full([1, 313], 2.606, dtype="float32")
        ]

    def colorize(self, image):

        if self.net is None:
            self.load_model()

        image = np.array(image)

        image = cv2.cvtColor(
            image,
            cv2.COLOR_RGB2BGR
        )

        scaled = image.astype("float32") / 255.0

        lab = cv2.cvtColor(
            scaled,
            cv2.COLOR_BGR2LAB
        )

        resized = cv2.resize(lab, (224, 224))

        L = cv2.split(resized)[0]

        L -= 50

        self.net.setInput(
            cv2.dnn.blobFromImage(L)
        )

        ab = self.net.forward()[0, :, :, :]

        ab = ab.transpose((1, 2, 0))

        ab = cv2.resize(
            ab,
            (image.shape[1], image.shape[0])
        )

        L_original = cv2.split(lab)[0]

        colorized = np.concatenate(
            (
                L_original[:, :, np.newaxis],
                ab
            ),
            axis=2
        )

        colorized = cv2.cvtColor(
            colorized,
            cv2.COLOR_LAB2BGR
        )

        colorized = np.clip(colorized, 0, 1)

        colorized = (255 * colorized).astype("uint8")

        colorized = cv2.cvtColor(
            colorized,
            cv2.COLOR_BGR2RGB
        )

        return colorized