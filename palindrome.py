#to check whether the string is palindrome or not
a = input("Enter a string: ")
a = a.lower()
def isPalindrome(a):
    return a == a[::-1]
ans = isPalindrome(a)

if ans:
    print("Yes")
else:
    print("No")
