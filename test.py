import time

def countdown(t):
    try:
        t = int(val)
        while t > 0:
          print(t)
          time.sleep(1)
          t -= 1
         
    except ValueError:
        print("Please enter a valid number ")
        
val = input("Enter the number of seconds you wish to countdown on:  ")


countdown(val)  
print("Time set is up")

