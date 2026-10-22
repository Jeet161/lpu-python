def pal(x):
    if x == x[::-1]:
        print("yes, it is a palindrome")
    else:
        print("No, it is NOT a palindrome")


pal('1234321')
pal('lovely')

def is_palindrome(text):
    text = text.lower().replace(" ", "")

    if text == text[::-1]:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


is_palindrome("mad D am")