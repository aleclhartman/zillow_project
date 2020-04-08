import numpy as np
import pandas as pd

import sklearn.preprocessing
from sklearn.model_selection import train_test_split

def split_my_data(df, train_pct=0.8, seed=56):
    train, test = train_test_split(df, train_size=train_pct, random_state=seed)
    return train, test