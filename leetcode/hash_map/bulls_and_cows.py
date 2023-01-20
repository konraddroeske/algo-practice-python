from collections import defaultdict


def get_hint(secret: str, guess: str) -> str:
    bulls = 0
    cows = 0
    hash_table = defaultdict(lambda: 0)

    for index, secret_char in enumerate(secret):
        guess_char = guess[index]

        if secret_char == guess[index]:
            bulls += 1
        else:
            if hash_table[secret_char] < 0:
                cows += 1

            if hash_table[guess_char] > 0:
                cows += 1

            hash_table[secret_char] += 1
            hash_table[guess_char] -= 1

    return f"{bulls}A{cows}B"


# print(get_hint("1807", "7810"))  # 1A3B
# print(get_hint("1123", "0111"))  # 1A1B
print(get_hint("1122", "2211"))  # 0A4B
# print(get_hint("2962", "7236"))  # 0A2B
# print(get_hint("5289", "2944"))  # 0A2B
