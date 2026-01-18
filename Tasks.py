import random,time


print("Game name :  << Guess the number >>")


time.sleep(2)


while True:
    answer = input("Do u wanna to start the game? yes or no :  ")
    time.sleep(1)
    if answer.lower() == "yes":
        print("Okay game starting...")
        break
    else:
        print("Okay, let's keep asking...")


arr = [1,2,3,4,5,6,7,8,9]   
    

x = random.sample(arr,4)  
    

result = "".join(map(str, x))
    

k = list(map(int, str(result)))  


time.sleep(1)


q = int(input("Guess the number: "))
    

number = list(map(int, str(q)))  
    

results = [] 


for i in range(4):
    if number[i] == k[i]:
        results.append("бык")
    elif number[i] in k:
         results.append("корова")
            
            
print(" ".join(results))
print(f"The given number was : {result}")


if q == result:
    print("Ты победил!")