import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

data = load_iris()
x = data.data
y = data.target

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

pca=PCA(n_components=2)
x_pca= pca.fit_transform(x_scaled)

plt.figure(figsize=(8,6))
plt.bar(range(1,len(pca.explained_variance_ratio_)),pca.explained_variance_ratio_,alpha=0.5,align='center')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance')
plt.title('Explained Variance Plot')
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=y,cmap='viridis',edgecolors='k',s=50)
plt.xlabel('Principal Component1')
plt.ylabel('Principal Component2')
plt.title('PCA of iris dataset')
plt.colorbar()
plt.show()
