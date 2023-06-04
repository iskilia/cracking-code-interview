def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return s2 in s1s1
    return False

if __name__ == "__main__":
    assert is_rotation("waterbottle", "erbottlewat") == True
    print("Passed all!")
