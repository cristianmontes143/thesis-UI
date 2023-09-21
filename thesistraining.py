import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import pandas as pd
import seaborn as sns
from sklearn import linear_model


data = pd.read_csv('FinalData.csv')
