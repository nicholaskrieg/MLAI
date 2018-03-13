import numpy as np
import matplotlib.pyplot as plt
import random

class KMeansAlgorithm():
    def __init__(self, num):
        self.N = num

    def cluster(self):
        x0 = random.random() * 10
        y0 = random.random() * 10
        return np.random.normal((x0, y0), 1, (300, 2))

    def clusterNumber(self):
        return np.concatenate([self.cluster() for i in range(self.N)])

    def plotting(self, data, centroids, clusters):
        clrs = ('blue', 'm', 'black', 'red')
        plt.scatter(data[:, 0], data[:, 1], c = [clrs[c] for c in clusters], s = 10)
        plt.scatter(centroids[:, 0], centroids[:, 1], s = 500, c = clrs, marker = '*')
        plt.show()

    def distances(self, point, centroid):
        sumC = [np.sum(((point - centroid) ** 2), axis = 1).reshape((-1, 1)) for centroid in centroid]
        return np.concatenate(sumC, axis = 1)

    def smdist(self, distances):
        return distances.argmin(axis = 1)


def main():
    KMeans = KMeansAlgorithm(4)
    mData = KMeans.clusterNumber()
    mRows = random.sample(range(mData.shape[0]), KMeans.N)
    mCentroids = mData[mRows]

    minDist = np.array([])
    while True:
        prev = minDist.copy()
        minDist = KMeans.smdist(KMeans.distances(mData, mCentroids))

        if np.all(prev == minDist):
            break

        for i in range(KMeans.N):
            mCentroids[i] = np.average(mData[minDist == i], axis = 0)

        KMeans.plotting(mData, mCentroids, minDist)

if __name__ == '__main__':
    main()
