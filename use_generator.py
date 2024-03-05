import tensorflow as tf
import keras
import PIL
from PIL import Image
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import os

@keras.saving.register_keras_serializable()
class PixelShuffler(tf.keras.layers.Layer):
    def __init__(self, scale, **kwargs):
        super(PixelShuffler, self).__init__(**kwargs)
        self.scale = scale

    def call(self, inputs):
        return self.depth_to_space(inputs, self.scale)

    def compute_output_shape(self, input_shape):
        batch_size, height, width, channels = input_shape
        new_height = height * self.scale if height is not None else None
        new_width = width * self.scale if width is not None else None
        new_channels = channels // (self.scale ** 2) if channels is not None else None
        return (batch_size, new_height, new_width, new_channels)

    def depth_to_space(self, inputs, scale):
        x = tf.nn.depth_to_space(inputs, scale)
        return x


generator = keras.models.load_model('models/generator/generator2.keras')

images = []

for file in os.listdir("use_images"):
    image = Image.open(os.path.join("use_images", file))
    image = image.resize((100, 100), Image.LANCZOS)

    image = np.asarray(image)

    images.append(image)

images = np.asarray(images)

hr = np.asarray(generator(images))





for i in range(len(hr)):
    plt.imshow(images[i])
    plt.show()
    plt.imshow(hr[i])
    plt.savefig("output/image" + str(i) + ".png")
    plt.show()
