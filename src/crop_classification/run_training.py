import sys
from src.crop_classification.train_model import train_crop_classifier


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python3 -m src.crop_classification.run_training <dataset_path>")
        sys.exit(1)

    dataset_path = sys.argv[1]

    train_crop_classifier(dataset_path)