try:
    num = int(input("Enter the number: "))
    if num == 1:
        print("1 is neither prime nor composite")
    elif num > 1:
        for i in range(2, int(num **0.5)+1):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else: 
        print(num, "is not a prime number")
except ValueError:
    print("Invalid input")
    
        
