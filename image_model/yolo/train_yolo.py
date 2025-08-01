from ultralytics import YOLO

# Parameters
data_yaml = "./dataset/data.yaml"
model_name = "yolov8n"
epochs = 50
img_size = 640
batch_size = 16

# Initialize model
model = YOLO(f"{model_name}.pt")

# Train
print("Starting training...")
results = model.train(
    data=data_yaml,
    epochs=epochs,
    imgsz=img_size,
    batch=batch_size,
    name="pothole_yolo",
    patience=10,
    device="cpu",
    verbose=True,
)

# Save model
model.save("pothole_yolo_final.pt")
print("Model saved as pothole_yolo_final.pt")

# Evaluate on validation set
metrics = model.val()
print("Validation Metrics:")
print(f"  mAP@0.5: {metrics.box.map50:.4f}")
print(f"  mAP@0.5:0.95: {metrics.box.map:.4f}")
