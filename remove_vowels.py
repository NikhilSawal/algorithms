input = "leetcodeisacommunityforcoders"

def remove_vowels(inp):
    vowels = ['a','e','i','o','u']
    return(''.join(i for i in inp if not i in vowels))

print(remove_vowels(input))
