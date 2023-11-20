from module7_mod import user_input
from sklearn.neighbors import KNeighborsRegressor

inputdata = user_input()
N,k,X_train,y_train = inputdata.get_data()

print("x for prediction, seperate the numbers by space")
inputx = input().split()
X_predict = [[float(x)] for x in inputx]


neigh = KNeighborsRegressor(n_neighbors=k)
neigh.fit(X_train, y_train)
y_predict = neigh.predict(X_predict)
coefficient = neigh.score(X_predict,y_predict)
print(f'predicted y is {y_predict}, coefficient of determination is {coefficient}')