import numpy as np

def distance(x1,x2):
    return np.sqrt((x1-x2)**2)

class KNN:
    def set_k(self,k):
        self.k = k

    def train (self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self,x_test):
        distances = [distance(x_test,x_train) for x_train in self.x_train]
        indexes = np.argsort(distances)[:self.k]
        neighbors = [self.y_train[i] for i in indexes]
        prediction = np.average(neighbors)
        return prediction