import numpy as np 

import matplotlib.pyplot as plt


class KMeans: 
    def __init__(self, k):
        self.k = k
        self.centroids = None 

    @staticmethod
    def euclidian_distance(data_point, centroids):
        return np.sqrt(np.sum((centroids-data_point)**2, axis=1))


    def fit(self, X, max_iterations=200):
        self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0),
                                           size= (self.k, X.shape[1]))
        
        for _ in range(max_iterations):
            y= []

            for data_point in X: 
                distances = KMeans.euclidian_distance(data_point, self.centroids)
                cluster_num = np.argmin(distances)
                y.append(cluster_num)

            y = np.array(y)

            cluster_indices = []

            for i in range(self.k):
                cluster_indices.append(np.argwhere(y==i))

            cluster_centers = []

            for i, indices in enumerate(cluster_indices):
                if len(indices) == 0:
                    cluster_centers.append(self.centroids[i])
                else: 
                    cluster_centers.append(np.mean(X[indices],axis=0)[0])

            if np.max(self.centroids - np.array(cluster_centers))<0.0001:
                break
            else:
                self.centroids = np.array(cluster_centers)
        return y
    

# On importe notre dataset
data = np.genfromtxt('./centred_2.csv', delimiter=",")
print(data)

#création d'une instance de kmeans
kmeans = KMeans(k=3)

# entrainement du modèle
labels = kmeans.fit(data)


#un petit graphique 

plt.scatter(data[:, 0], data[:, 1], c= labels)

plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], c=range(len(kmeans.centroids)), 
            marker = "*", s=200)

plt.show()
