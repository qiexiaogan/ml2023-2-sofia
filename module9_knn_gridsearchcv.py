import numpy as np
import sklearn.metrics as sm
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

def UserInput(N):
    Set_x = np.empty((0,1),dtype = float)
    Set_y = np.empty(0,dtype=int)
    #set input, x(real number) as feature, y (int) as class label
    for i in range(N):
        #ask for x
        print(f'value for x{i}')
        x = float(input())
        Set_x = np.append(Set_x,np.array([[x]]),axis = 0)
        #ask for y
        print(f'value for y{i}')
        y = int(input())
        if y < 0 :
            raise ValueError("input y needs to be non-negative integer")
        Set_y = np.append(Set_y,y)
    return Set_x, Set_y

#training data inputs
print('integer for N:') 
N = int(input())
Train_x,Train_y = UserInput(N)
unique_elements, counts = np.unique(Train_y, return_counts=True)



#train model
params = {'n_neighbors': [k for k in range(10)]}
classifier = KNeighborsClassifier()
gs_knn = GridSearchCV(classifier,param_grid=params,scoring='accuracy',cv=2)
gs_knn.fit(Train_x, Train_y)
K = gs_knn.best_params_['n_neighbors']
knn = KNeighborsClassifier(n_neighbors=K)
knn.fit(Train_x,Train_y)

#testing data inputs
print('integer for M:') 
M = int(input())
Test_x,Test_y = UserInput(M)
predict_y = knn.predict(Test_x)

    
accuracy = sm.accuracy_score(Test_y,predict_y)
print(f'best k is {K}, corresponding test accuracy is {accuracy}')