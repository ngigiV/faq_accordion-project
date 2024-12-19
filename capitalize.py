def capitalize(input_string):

    capitalized_string = ' '.join(word.capitalize() for word in input_string.split())
    return capitalized_string

user_input = input("Please enter a sentence or word: ")

result = capitalize(user_input)
print("Result:", result)
