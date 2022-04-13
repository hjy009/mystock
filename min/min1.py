import pandas as pd
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame()

df = pd.read_csv(filepath_or_buffer='600000.txt',delimiter='\t',encoding='GB2312',header=1)
df.columns = df.columns.str.strip()
df = df.drop(index=df.index[-1])

df.head()


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

