def check_palindrome(n):
    num = n
    reversed =0
    while num > 0:
        rem = num % 10
        reversed = reversed *10 + rem
        num //= 10 
    if n == reversed:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if(check_palindrome(n)):
    print("Palindrome")
else:
    print("Not Palindrome")