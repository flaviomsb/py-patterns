import tensorflow as tf
import os
import random
import numpy as np

print("Number of GPUs available", len(tf.config.list_physical_devices('GPU')))
