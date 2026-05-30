# Program to check if both numbers have opposite signs

def check_sign(a: int, b: int):
    if (a ^ b) < 0:
        print("Both have opposite signs.")
    else:
        print("Both have same signs")
    
check_sign(5, -10)