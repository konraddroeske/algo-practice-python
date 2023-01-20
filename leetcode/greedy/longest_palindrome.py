from collections import defaultdict


def longest_palindrome(s: str) -> int:
    chars = defaultdict(lambda: 0)
    palindrome_length = 0

    for char in s:
        chars[char] += 1

    max_odd = 0

    for key, val in chars.items():
        if val % 2 == 0:
            palindrome_length += val
        else:
            palindrome_length += val - 1

            if val > max_odd:
                max_odd = val

    if max_odd:
        return palindrome_length + 1

    return palindrome_length

def longest_palindrome_one_pass(s: str) -> int:
    chars = defaultdict(lambda: 0)
    odd_chars = defaultdict(lambda: True)
    palindrome_length = 0

    for char in s:
        chars[char] += 1

        if chars[char] % 2 == 0:
            palindrome_length += 2
            del odd_chars[char]
        else:
            odd_chars[char] = True

    if odd_chars:
        return palindrome_length + 1

    return palindrome_length


input_1 = "abccccdd"
input_2 = "a"
input_3 = """
"civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
"""


print(longest_palindrome_one_pass(input_1))
print(longest_palindrome_one_pass(input_2))
print(longest_palindrome_one_pass(input_3))
# 983
