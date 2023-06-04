from collections import defaultdict

def is_permutation_of_palindrome(input_str: str) -> bool:
    char_occurences = defaultdict(int)
    for char in input_str:
        if char != " ":
            char_occurences[char] += 1
    found_odd = False
    for value in char_occurences.values():
        if (value % 2 == 1):
            if (found_odd):
                return False
            found_odd = True
    return True

if __name__ == "__main__":
    assert is_permutation_of_palindrome("tact coa") == True
    print("Passed all!")