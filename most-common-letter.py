# most common letter in the string regardless of capitalization.
# ignore spaces
# ex) "John Loves to Play Baseball and Joanie Loves to Play Basketball, but Jenny Likes To Dance"
#output: l

# so we need to do a for loop over ever character, including spaces, in the sentence and assign its own count
# probably a dictionary, right?
# we need the letter and the associated count
# for x in sentence
# if char is already a key, add to count
# return the key with the highest value

def mostCommonLetter(a_string):
    letter_count = {}
    for char in a_string:
