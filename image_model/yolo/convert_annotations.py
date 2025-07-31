import os
import random
import shutil
import xml.etree.ElementTree as ET

from PIL import Image


def convert_to_yolo(xml_path, img_path, output_path, img_output_path):
    """Convert PASCAL VOC XML to YOLO format and copy image."""
    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        return False
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        img = Image.open(img_path)
        img_width, img_height = img.size

        with open(output_path, "w") as f:
            objects_found = False
            for obj in root.findall("object"):
                if obj.find("name").text != "pothole":
                    continue
                objects_found = True
                bndbox = obj.find("bndbox")
                xmin = float(bndbox.find("xmin").text)
                ymin = float(bndbox.find("ymin").text)
                xmax = float(bndbox.find("xmax").text)
                ymax = float(bndbox.find("ymax").text)

                x_center = ((xmin + xmax) / 2) / img_width
                y_center = ((ymin + ymax) / 2) / img_height
                width = (xmax - xmin) / img_width
                height = (ymax - ymin) / img_height

                f.write(f"0 {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

            if not objects_found:
                f.write("")

        shutil.copy(img_path, img_output_path)
        return True
    except Exception as e:
        print(f"Error processing {xml_path}: {str(e)}")
        return False


def process_directory(xml_dir, img_dir, label_dirs, img_dirs, split_ratio=(0.8, 0.1)):
    """Process XML files and split into train/val/test."""
    os.makedirs(label_dirs["train"], exist_ok=True)
    os.makedirs(label_dirs["val"], exist_ok=True)
    os.makedirs(label_dirs["test"], exist_ok=True)
    os.makedirs(img_dirs["train"], exist_ok=True)
    os.makedirs(img_dirs["val"], exist_ok=True)
    os.makedirs(img_dirs["test"], exist_ok=True)

    xml_files = [f for f in os.listdir(xml_dir) if f.endswith(".xml")]
    total_files = len(xml_files)
    if total_files == 0:
        print(f"No XML files found in {xml_dir}")
        exit(1)

    random.seed(42)
    random.shuffle(xml_files)
    train_end = int(split_ratio[0] * total_files)
    val_end = train_end + int(split_ratio[1] * total_files)
    splits = {
        "train": xml_files[:train_end],
        "val": xml_files[train_end:val_end],
        "test": xml_files[val_end:],
    }

    for split in ["train", "val", "test"]:
        print(f"Processing {split} split...")
        for xml_file in splits[split]:
            img_name = xml_file.replace(".xml", ".png")
            xml_path = os.path.join(xml_dir, xml_file)
            img_path = os.path.join(img_dir, img_name)
            label_path = os.path.join(
                label_dirs[split], xml_file.replace(".xml", ".txt")
            )
            img_output_path = os.path.join(img_dirs[split], img_name)
            if convert_to_yolo(xml_path, img_path, label_path, img_output_path):
                print(f"Processed: {xml_file} -> {label_path}")


if __name__ == "__main__":
    xml_dir = "dataset/annotations"
    img_dir = "dataset/images"
    label_dirs = {
        "train": "dataset/labels/train",
        "val": "dataset/labels/val",
        "test": "dataset/labels/test",
    }
    img_dirs = {
        "train": "dataset/images/train",
        "val": "dataset/images/val",
        "test": "dataset/images/test",
    }
    process_directory(xml_dir, img_dir, label_dirs, img_dirs)
