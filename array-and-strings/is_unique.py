def is_unique(input_str: str):
    char_set = set()
    for char in input_str:
        if char in char_set:
            return False
        char_set.add(char)
    return True

if __name__ == "__main__":
    assert is_unique("abcdefghijklmnop") == True
    assert is_unique("aaaaaa") == False
    assert is_unique("gaslihd") == True
    print("Passed all!")