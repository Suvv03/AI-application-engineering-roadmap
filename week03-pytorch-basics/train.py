from utils.dataset import get_mnist_loaders


def main():
    train_loader, test_loader = get_mnist_loaders(batch_size=64)

    images, labels = next(iter(train_loader))

    print("Train batches:", len(train_loader))
    print("Test batches:", len(test_loader))
    print("Image batch shape:", images.shape)
    print("Label batch shape:", labels.shape)
    print("First 10 labels:", labels[:10])


if __name__ == "__main__":
    main()
