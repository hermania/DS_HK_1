import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets, feature_selection
# Load in the data and seperate the class labels and input data
import re
url = 'http://www-958.ibm.com/software/analytics/manyeyes/datasets/af-er-beer-dataset/versions/1.txt'
beer = pd.read_csv(url, delimiter="\t")
# Create the training (and test) set using the rng in numpy