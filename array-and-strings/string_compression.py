
def count_compressions(str1: str) -> int:
    compressed_length = 0
    count_consecutive = 0
    for i in range(len(str1)):
        count_consecutive += 1
        if i + 1 >= len(str1) or str1[i] != str1[i+1]:
            compressed_length += 1 + len(str(count_consecutive))
            count_consecutive = 0
    return compressed_length

def compress_string(str1: str) -> str:
    final_length = count_compressions(str1)
    if final_length >= len(str1):
        return str1

    compressed = ''
    count_consecutive = 0
    for i in range(len(str1)):
        count_consecutive += 1
        if i + 1 >= len(str1) or str1[i] != str1[i+1]:
            compressed += str1[i] + str(count_consecutive)
            count_consecutive = 0
    return compressed

if __name__ == "__main__":
    assert compress_string("aabcccccaaa") == "a2b1c5a3"
    print("Passed all!")