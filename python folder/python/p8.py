def count_same_first_last(words):
    return sum(1 for word in words if len(word) > 1 and word[0] == word[-1])

if __name__ == "__main__":
    words = ['aba', 'xyz', 'abc', '121']
    print(f"문자열의 개수 = {count_same_first_last(words)}")