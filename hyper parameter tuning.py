import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score,KFold,GridSearchCV
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

data = load_iris()
X = data.data
y = data.target

clf=RandomForestClassifier(random_state=42)

kf=KFold(n_splits=5,shuffle=True, random_state=42)

scores = cross_val_score(clf,X,y,cv=kf)

print(f' cross validation score: {scores}')
print(f' mean cross validation  score: {scores.mean():.2f}')

param_grid={
    'n_estimators':[10,50,100],
    'max_depth':[None,3,5,7],
    'min_samples_split':[2,5,10],
    'min_samples_leaf':[1,2,4],
}

grid_search=GridSearchCV(estimator=clf,param_grid=param_grid,cv=5,scoring='accuracy',n_jobs=-1)
grid_search.fit(X,y)

best_params=grid_search.best_params_
best_score=grid_search.best_score_

print(f'Best parameters :{best_params}')
print(f'Best Cross validation score :{best_score:.2f}')