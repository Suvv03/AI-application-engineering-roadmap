import torch
from torchvision import datasets, transforms

from models.simple_cnn import SimpleCNN


def load_model(checkpoint_path: str, device):
    model = SimpleCNN().to(device)

    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])

    model.eval()
    return model


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    test_dataset = datasets.MNIST(
        root="data",
        train=False,
        download=True,
        transform=transform
    )

    image, label = test_dataset[0]

    model = load_model(
        checkpoint_path="checkpoints/simple_cnn_mnist.pt",
        device=device
    )

    image = image.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        prediction = output.argmax(dim=1).item()

    print("True label:", label)
    print("Predicted label:", prediction)


if __name__ == "__main__":
    main()
