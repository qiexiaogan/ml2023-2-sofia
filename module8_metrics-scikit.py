import numpy as np
import sklearn.metrics as sm


#collect inputs
print('integer for N:') #asks the user for input N (positive integer) and reads it
N = int(input())

x_label = np.empty(0,dtype=int)
y_predict = np.empty(0,dtype=int)
for i in range(N):
    print(f'value for x{i}')
    x = int(input())
    x_label=np.append(x_label,x)
    print(f'value for y{i}')
    y = int(input())
    y_predict=np.append(y_predict,y)


#precision and recall
precision = sm.precision_score(x_label,y_predict)
recall = sm.recall_score(x_label,y_predict)
print(f'precision is {precision}')
print(f'recall is {recall}')
