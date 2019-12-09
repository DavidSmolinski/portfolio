# The Palindrome Problem:
# Make a function that makes a palindrome out of the letters in a string and
# returns -1 if this is not possible. Convert a list of strings with the
# function.

# from collections import defaultdict
from collections import Counter


def palify(string):
    """If possible, rearrange chars in string to make a palindrome. 
    Else, return -1.

    Arguments:
        string {[str]}

    Returns:
        [str or int] -- [palindrome or -1]
    """
    
    # # old code
    # letter_count = defaultdict(int)
    # for letter in string:
    #     letter_count[letter] += 1
    
    # Improved with these suggestions:
    # Dominic Thorn (https://www.linkedin.com/in/dominic-thorn/):
    # Replace "defaultdict(int)" with "Counter()".
    # Steven Lott (https://www.linkedin.com/in/steven-lott-029835/):
    # Replace loop with "Counter(string)".
    
    # dictionary like object: keys: letters in string, vals: letter frequency
    letter_count = Counter(string)
    
    odds = 0
    pal_beginning = ''
    pal_mid = ''
        
    for letter, count in letter_count.items():
        if count % 2 == 0:
            pal_beginning += int(count/2)*letter
        else:
            pal_mid += letter*count
            odds += 1

    if odds < 2:
        pal = pal_beginning+pal_mid+pal_beginning[::-1]
        return pal
    else:
        return -1


not_pals = ('','eedd', 'wgerar', 'uiuiqii')
pals = [palify(not_pal) for not_pal in not_pals]

print(pals)