def fizzbuzz(n:int):
    for i in range(1,n+1):
        if i%3==0:
            print("fizz")
        else:
            print(i)

if __name__=='__main__':
    fizzbuzz(15)
