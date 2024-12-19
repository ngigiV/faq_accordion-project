def capitalize_words(input_string):
    # Split the string into words, capitalize each word, and join them back together
    capitalized_string = ' '.join(word.capitalize() for word in input_string.split())
    return capitalized_string

# Prompt the user to input a string
user_input = input("Please enter a sentence or word: ")

# Capitalize the words and print the result
result = capitalize_words(user_input)
print("Result:", result)
