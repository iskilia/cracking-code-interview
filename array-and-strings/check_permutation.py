from collections import defaultdict

def check_permutation(str1: str, str2: str) -> bool:
    char_occurence_counter = defaultdict(int)
    for char in str1:
        char_occurence_counter[char] += 1

    for char in str2:
        char_occurence_counter[char] -= 1

    for value in char_occurence_counter.values():
        if value != 0:
            return False
    return True

if __name__ == "__main__":
    assert check_permutation("abcd", "dcba") == True
    assert check_permutation("aaa", "bbb") == False
    print("Passed all!")