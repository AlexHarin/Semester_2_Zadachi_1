def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
input_string = input("Введите строку: ")
if is_palindrome(input_string):
    print("Это палиндром!")
else:
    print("Это не палиндром.")