class integertest:
    def run():
        print('Enter a positive integer')
        N = int(input())
        Nlist = []
        for n in range(0,N):
            print("provide number #"+ str(n+1))
            Nlist.append(float(input()))

        print("Enter an integer to check if it's in the numbers you inputed")
        Ncheck = float(input())
        try:
            print(Nlist.index(Ncheck)+1)
        except:
            print("-1")