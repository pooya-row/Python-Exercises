import gzip
import idx2numpy


def MNIST_import(files):
    data = []

    for file in files:
        with gzip.open(file, 'r') as f:
            data.append(idx2numpy.convert_from_file(f))

    train_images = data.pop(0)
    train_labels = data.pop(0)
    t10k_images = data.pop(0)
    t10k_labels = data.pop(0)

    return train_images, train_labels, t10k_images, t10k_labels
