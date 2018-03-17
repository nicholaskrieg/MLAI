"""
K-Means Algorithm Machine Learning:

Python3

This is a K-Means Algorithm machine learning code that determines centroid points
for different data clusters. This clustering methodology is very important in
categorical data analysis.

To run, enter the number of centroids you wish to learn. The program will produce
a list of graphs that are displayed on the Python console. Depending on personal
Python consoles, you might have to sift through the graphs or delete each proceeding
window to view next graph. This program does not yet have graphical capabilities to
implement an animation of the graphs.
"""

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
        clrs = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
        plt.scatter(data[:, 0], data[:, 1], c = [clrs[c] for c in clusters], s = 10)
        plt.scatter(centroids[:, 0], centroids[:, 1], s = 500, c = clrs, marker = '*')
        plt.show()

    def distances(self, point, centroid):
        sumC = [np.sum(((point - centroid) ** 2), axis = 1).reshape((-1, 1)) for centroid in centroid]
        return np.concatenate(sumC, axis = 1)

    def smdist(self, distances):
        return distances.argmin(axis = 1)

    def runFull(self, data, centroids):
        minDist = np.array([])
        while True:
            prev = minDist.copy()
            minDist = self.smdist(self.distances(data, centroids))

            if np.all(prev == minDist):
                break

            for i in range(self.N):
                centroids[i] = np.average(data[minDist == i], axis = 0)

            self.plotting(data, centroids, minDist)

def main():
    N = int(input("\nHow many centroids do you want to test for? (1-7): "))
    KMeans = KMeansAlgorithm(N)

    mData = KMeans.clusterNumber()
    mRows = random.sample(range(mData.shape[0]), KMeans.N)
    mCentroids = mData[mRows]

    KMeans.runFull(mData, mCentroids)

if __name__ == '__main__':
    main()
