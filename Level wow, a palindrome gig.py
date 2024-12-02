#This project functions to analyze the words entered by the user to determine if it is a palindrome.
#Reflecting a boolean to corroborate 
#True in case of a positive result, or false otherwise


def Check_word(p):
    '''Convert to lowercase and determine if it is a palindrome'''
    #Convert to lowercase to avoid errors due to uppercase letters
    p= p.lower()
    return p == p[::-1]


def main():
    '''Input the word, the function analyzes it, and gives us the result'''
    p = input("Enter the word you want to analize:\n")
    print(Check_word(p))

main()