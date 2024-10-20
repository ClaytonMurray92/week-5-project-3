import math
low = int(input("Enter the Low number: "))
high = int(input("Enter the High number: "))
maxattempt = math.log(high - low, 2)
count = 0
guess = int((low + high) / 2)
while count != maxattempt:
    count += 1
    guess = int((low + high) / 2)
    print(low, high)
    print("Your number is: ", guess)
    hle = input("Enter e, h, or l: ")
    if hle == 'h':
        low = guess + 1
    elif hle == 'l':
        high = guess - 1
    elif hle == 'e':
        print("The computer guessed right in", count, "tries.")
        break
    else:
        print(" Invald input, Please enter 'e', 'h', or 'l'.")
    if low > high:
        print("Cheater...")
        break
    
