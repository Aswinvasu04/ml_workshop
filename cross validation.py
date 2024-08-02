import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier

data=load_iris()
x = data.data
y = data.target

clf = RandomForestClassifier(random_state=42)

kf=KFold(n_splits=5,shuffle=True, random_state=42)
scores = cross_val_score(clf, x, y, cv=kf)

print(f'cross validation scores: {scores}')
print(f'mean cross validation score: {scores.mean():.2f}')