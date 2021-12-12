#ajit kerle
#function to demonstrate printing patterns of number
def numpat(n):
    num=1
    for i in range(0,n):
        num=1
        for i in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print("\r")
#Driver node
n=5
numpat(n)            
