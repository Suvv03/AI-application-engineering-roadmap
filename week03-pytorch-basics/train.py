import torch
import torch.nn as nn
import torch.optim as optim

from utils.dataset import get_mnist_loaders
from models.simple_cnn import SimpleCNN


def train_one_epoch(model, train_loader, criterion, optimizer, device):
    model.train()

    total_loss = 0.0
    total_samples = 0

    for batch_idx, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        batch_size = images.size(0)
        total_loss += loss.item() * batch_size
        total_samples += batch_size

        if (batch_idx + 1) % 100 == 0:
            print(f"Batch {batch_idx + 1}, loss: {loss.item():.4f}")

    avg_loss = total_loss / total_samples
    return avg_loss


def evaluate(model, test_loader, device):
    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            predictions = outputs.argmax(dim=1)

            correct += (predictions == labels).sum().item()
            total += labels.size(0)

    accuracy = correct / total
    return accuracy


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)

    train_loader, test_loader = get_mnist_loaders(batch_size=64)

    model = SimpleCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    train_loss = train_one_epoch(
        model=model,
        train_loader=train_loader,
        criterion=criterion,
        optimizer=optimizer,
        device=device
    )

    test_accuracy = evaluate(
        model=model,
        test_loader=test_loader,
        device=device
    )

    print(f"Train loss: {train_loss:.4f}")
    print(f"Test accuracy: {test_accuracy:.4f}")


if __name__ == "__main__":
    main()
