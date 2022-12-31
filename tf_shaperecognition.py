# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 14:47:28 2022

@author: Maximilian
"""

# import section ------------------------------------------------------------ #
# model libraries ----------------------------------------------------------- #
import os
import pathlib as pl
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops
from PIL import Image

# visualization libraries --------------------------------------------------- #
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

# global variables ---------------------------------------------------------- #
img_size = (28,28)
class_names = ["Square", "Cross"]

# importing the dataset ----------------------------------------------------- #
path = "./images"

data_dir = pl.Path(path)

image_count = len(list(data_dir.glob("*.png")))
print(image_count)

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  labels="inferred",
  class_names=["cross","square"],
  color_mode="rgb",
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=img_size,
  batch_size=None
  )

val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  labels="inferred",
  class_names=["cross","square"],
  color_mode="rgb",
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=img_size,
  batch_size=None
  )








