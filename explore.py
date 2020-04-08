import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def plot_variable_pairs(dataframe, hue=None):
    g = sns.pairplot(dataframe, hue=hue, kind="reg")
    g.fig.suptitle("Scatterplot with Regression for Continuous Variables")
    plt.show()

def plot_categorical_and_continuous_vars(categorical_var, continuous_var, df):
    plt.figure(figsize=(32, 18))
    plt.subplot(221)
    sns.barplot(x=categorical_var, y=continuous_var, data=df, palette=sns.color_palette("colorblind"))
    plt.figure(figsize=(32, 18))
    plt.subplot(222)
    sns.boxplot(x=categorical_var, y=continuous_var, data=df, palette=sns.color_palette("colorblind"))
    plt.figure(figsize=(32, 18))
    plt.subplot(223)
    sns.swarmplot(x=categorical_var, y=continuous_var, data=df, palette=sns.color_palette("colorblind"))
    plt.show()