
class user_input():
    def get_data(self):
        print('integer for N:') #asks the user for input N (positive integer) and reads it
        N = int(input())
        print('integer for k') # asks the user for input k (positive integer) and reads it
        k = int(input())
        x_train = []
        y_train = []
        for i in range(N):
            print('value for x%i:' %i)
            x_train.append([float(input())]) 
            print('value for y%i:'%i)
            y_train.append(float(input())) 
        return N,k,x_train, y_train


