from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image
from ultralytics import YOLO

# Configuration
MODEL_PATH = "pothole_yolo_final.pt"
TEST_DIR = "dataset/images/test"
IMG_SIZE = 640


def predict_image(model, img_path):
    """Predict potholes in a single image and display results."""
    results = model.predict(img_path, imgsz=IMG_SIZE, conf=0.5, verbose=False)
    img = Image.open(img_path)
    plt.imshow(img)
    pothole_count = 0
    for box in results[0].boxes:
        if box.cls.item() == 0:
            pothole_count += 1
            xyxy = box.xyxy[0].cpu().numpy()
            conf = box.conf.item()
            plt.gca().add_patch(
                plt.Rectangle(
                    (xyxy[0], xyxy[1]),
                    xyxy[2] - xyxy[0],
                    xyxy[3] - xyxy[1],
                    fill=False,
                    edgecolor="red",
                    linewidth=2,
                )
            )
            plt.text(xyxy[0], xyxy[1], f"Pothole: {conf:.2f}", color="red", fontsize=10)
    predicted_class = "pothole" if pothole_count > 0 else "no_pothole"
    plt.title(f"Prediction: {predicted_class} (Potholes: {pothole_count})")
    plt.axis("off")
    plt.show()
    print(f"Image: {img_path}")
    print(f"Prediction: {predicted_class} (Potholes detected: {pothole_count})")
    return predicted_class, pothole_count


if __name__ == "__main__":
    # Load model
    model = YOLO(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")

    # Test all images in test directory
    test_dir = Path(TEST_DIR)
    if not test_dir.exists():
        print(f"Test directory not found: {test_dir}")
        exit(1)

    test_images = list(test_dir.glob("*.png"))
    if not test_images:
        print(f"No images found in {test_dir}")
        exit(1)

    predictions = []
    for img_file in test_images:
        predicted_class, pothole_count = predict_image(model, str(img_file))
        predictions.append(predicted_class)

    # Print prediction summary
    print("\nPrediction Summary:")
    for class_name in ["no_pothole", "pothole"]:
        count = predictions.count(class_name)
        print(f"  {class_name}: {count} images ({count / len(predictions) * 100:.1f}%)")
