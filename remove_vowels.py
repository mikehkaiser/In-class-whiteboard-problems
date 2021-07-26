

# Write a function that will remove all vowels from a given string.
# The function should return a string.
# Example:
# Input: ‘Joel’
# Output: ‘Jl’


# def remove_vowels(a_string):
#     # provide starter string
#     vowels = 'aeiouAEIOU'
#     no_vowels = ''
#     for i in a_string:
#         if i not in 'aeiouAEIOU':
#             no_vowels += i
#     return no_vowels

def remove_vowels(a_string):
    return (x if x not in 'aeiouAEIOU' for x in a_string)


remove_vowels('Joel')
print(remove_vowels('Joel'))
