from collections import defaultdict, Counter


def longest_palindrome(words: list[str]) -> int:
    prev_words = defaultdict(lambda: 0)
    count = 0
    double_counter = 0

    for word in words:
        if word[0] == word[1]:
            double_counter += 1

        reversed_word = word[::-1]

        if prev_words[reversed_word] > 0:
            prev_words[reversed_word] -= 1
            count += 4
        else:
            prev_words[word] += 1

    double_word = next(
        (
            word
            for word, count in prev_words.items()
            if count > 0 and word[0] == word[1]
        ),
        None,
    )

    return count + 2 if double_word else count


def longest_palindrome_counter(words: list[str]) -> int:
    word_counts = Counter(words)

    result = 0
    middle = False

    for word, count in word_counts.items():
        if word[0] == word[1]:
            if count % 2 == 0:
                result += count
            else:
                middle = True
                result += count - 1
        elif word[0] < word[1]:
            reverse_count = word_counts[word[1] + word[0]]
            result += 2 * min(count, reverse_count)

    if middle:
        result += 1

    return 2 * result


input_1 = ["lc", "cl", "gg"]
input_2 = ["ab", "ty", "yt", "lc", "cl", "ab"]
input_3 = ["cc", "ll", "xx"]

print(longest_palindrome_counter(input_1))
print(longest_palindrome_counter(input_2))
print(longest_palindrome_counter(input_3))
