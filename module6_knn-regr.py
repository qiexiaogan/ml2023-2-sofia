from module6_mod import user_input
from module6_knn import KNN

inputdata = user_input()
N,k,x_train,y_train = inputdata.get_data()

if k >= N:
    print("k cannot be larger than N")

else:
    knn = KNN()
    knn.set_k(k)
    knn.train(x_train,y_train)

    print("give x for prediction")
    x_test = float(input())
    prediction = knn.predict(x_test)
    print("prediction for the given x=%.1f is %.1f" %(x_test,prediction))