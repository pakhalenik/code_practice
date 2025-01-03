#palindrome
#from src.Coding_Question.list.Sum_of_element import result

def is_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return string == string[::-1]


# Test the function
string = "mam"
result = is_palindrome(string)
print(result)
