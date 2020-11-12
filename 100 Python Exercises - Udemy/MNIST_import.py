import gzip
import idx2numpy
import matplotlib.pyplot as plt
import utils

files = [
    'train-images-idx3-ubyte.gz',
    'train-labels-idx1-ubyte.gz',
    't10k-images-idx3-ubyte.gz',
    't10k-labels-idx1-ubyte.gz'
]

# data = []
#
# for file in files:
#     with gzip.open(file, 'r') as f:
#         data.append(idx2numpy.convert_from_file(f))
#
# train_images = data.pop(0)
# train_labels = data.pop(0)
# t10k_images = data.pop(0)
# t10k_labels = data.pop(0)

train_images, train_labels, t10k_images, t10k_labels = utils.MNIST_import(files)

print(train_images.shape)
print(train_labels.shape)
print(t10k_images.shape)
print(t10k_labels.shape)

# for i in range(len(data)):
#     print(data[i].shape)
#     print(type(data[i]))

# train_1 = 'train-images-idx3-ubyte.gz'
# train_2 = 'train-labels-idx1-ubyte.gz'
#
# with gzip.open(train_1, 'rb') as f:
#     train_images = idx2numpy.convert_from_file(f)
#
# with gzip.open(train_2, 'rb') as f:
#     train_labels = idx2numpy.convert_from_file(f)
#
#
# print(train_images.shape)
# print(train_labels.shape)
# print(type(train_images))
# print(type(train_labels))
# print(arr[654])

# cv.imshow("Image", arr[4])
# plt.imshow(arr[4], cmap='Greys')#plt.cm.binary)
# plt.show()
# import numpy as np
# file = 'data/train-images-idx3-ubyte'
# parser = argparse.ArgumentParser(
#     description='Download the MNIST dataset from the internet')
# parser.add_argument(
#     '-d', '--destination', default='.', help='Destination directory')
# parser.add_argument(
#     '-q',
#     '--quiet',
#     action='store_true',
#     help="Don't report about progress")
# options = parser.parse_args()

# arr = idx2numpy.convert_from_file(path)

# path = os.getcwd() + '\\train-images-idx3-ubyte.gz'
# print(cPickle.HIGHEST_PROTOCOL)
# print(pickle.DEFAULT_PROTOCOL)
# with open(path) as file:
#     train = pickle.Unpickler(file, encoding='utf8')
#     nn = train.load()


#     train = pickle.Unpickler(f, fix_imports=True, encoding="ASCII")
#     tt = train.load()
# train=pickle.load(f)

# f.close()
# utils.unzip(path, options.quiet)
