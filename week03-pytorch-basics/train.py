import torch

from utils.dataset import get_mnist_loaders
from models.simple_cnn import SimpleCNN


def main():
    train_loader, test_loader = get_mnist_loaders(batch_size=64)
    images, labels = next(iter(train_loader))

    model = SimpleCNN()
    outputs = model(images)

    print("Input shape:", images.shape)
    print("Output shape:", outputs.shape)
    print("Label shape:", labels.shape)


if __name__ == "__main__":
    main()
