import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

x,y=make_blobs(n_samples=100,centers=4,cluster_std=0.60,random_state=0)

plt.scatter(x[:,0],x[:,1],s=50)
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.title("Synthetic data for k-means clustering")
plt.show()

kmeans = KMeans(n_clusters=4,random_state=0)
kmeans.fit(x)

y_kmeans = kmeans.predict(x)

plt.scatter(x[:,0],x[:,1],s=50,c=y_kmeans,cmap='viridis')
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.title("Synthetic data for k-means clustering")
plt.show()

kmeans = KMeans(n_clusters=4,random_state=0)
kmeans.fit(x)

y_kmeans = kmeans.predict(x)

plt.scatter(x[:,0],x[:,1],s=50,c=y_kmeans,cmap='viridis')
centers=kmeans.cluster_centers_
plt.scatter(centers[:,0],centers[:,1],c='red',s=200,alpha=0.75)
plt.xlabel('feature 1')
plt.ylabel('feature 2')
plt.title('k-means clustering results')
plt.show()

sil_score=silhouette_score(x,y_kmeans)
print(f'Silhouette score is: {sil_score:2f}')