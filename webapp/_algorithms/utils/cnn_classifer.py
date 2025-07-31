import numpy as np
from PIL import Image

IMAGE_SIZE = 64
HIDDEN_SIZE = 16

# Load weights once
weights = np.load("_algorithms/model_weights.npz")


class SimpleCNN:
    def __init__(self):
        self.fc_weights = weights["fc_weights"]
        self.fc_bias = weights["fc_bias"]
        self.out_weights = weights["out_weights"]
        self.out_bias = weights["out_bias"]

    def relu(self, x):
        return np.maximum(0, x)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict(self, img_arr):
        x = img_arr.reshape(-1, 1)
        z1 = np.dot(self.fc_weights, x) + self.fc_bias
        a1 = self.relu(z1)
        z2 = np.dot(self.out_weights, a1) + self.out_bias
        a2 = self.sigmoid(z2)
        return a2.item()  # Return probability


def classify_pothole(image_file):
    model = SimpleCNN()
    # Convert uploaded image file (InMemoryUploadedFile) to PIL
    image = (
        Image.open(image_file)
        .convert("L")
        .resize(
            (
                IMAGE_SIZE,
                IMAGE_SIZE,
            )
        )
    )
    img_arr = np.array(image) / 255.0
    prob = model.predict(img_arr)

    label = "pothole" if prob > 0.5 else "not_pothole"
    return label, prob
