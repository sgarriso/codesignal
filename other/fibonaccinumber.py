import json

def readtext(file='answers.json'):
    with open(file, 'r') as fp:
        data = json.load(fp)
    return data
fibcheat=readtext()
def writetext(dic,file='answers.json'):
    with open(file, 'w') as fp:
        json.dump(dic, fp)
def fibonacciNumber(n):
    if str(n) in fibcheat.keys():
        return fibcheat[str(n)]
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else: 
        return fibonacciNumber(n-1)+fibonacciNumber(n-2)

print(fibcheat)
dic= {}
for i in range(0,100):
    if str(i) in fibcheat.keys():
        
        dic[i] = fibcheat[str(i)]
    else:
        dic[i]=fibonacciNumber(i)
        fibcheat[str(i)] = dic[(i)]

writetext(dic)
