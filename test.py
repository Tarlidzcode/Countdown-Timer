import time

val = input("Enter the number of seconds you wish to countdown on:  ")

def countdown():
    try:
        t = int(val)
        while t > 0:
          print(f"Time remaining: {t} seconds")
          time.sleep(1)
          t -= 1
         
    except ValueError:
        print("Please enter a valid number ")
        



countdown()  
print("Time set is up")


