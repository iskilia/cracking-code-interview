
## We have to consider replacement, insertion, and removal
def one_edit_replace(str1: str, str2: str) -> bool:
    found_diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_diff:
                return False
            found_diff = True
    return True

def one_edit_insert(str1: str, str2: str) -> bool:
    index_1, index_2 = 0, 0
    while(index_2 < len(str2) && index_1 < len(str1)):
        if str1[index_1] != str2[index_2]:
            if index_1 != index_2:
                return False
            index_2 += 1
        else:
            index_2 += 1
            index_1 += 1
    return True


def is_one_away(str1: str, str2: str) -> bool:
    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return one_edit_insert(str1, str2)
    elif len(str1) - 1 == len(str2):
        return one_edit_insert(str2, str1)
    return False

if __name__ == "__main__":
    assert is_one_away("pale", "ple") == True
    assert is_one_away("pales", "pale") == True
    assert is_one_away("pale", "bale") == True
    assert is_one_away("pale", "bae") == False
    print("Passed all!")