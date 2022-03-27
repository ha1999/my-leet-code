def longest_squence(strs):
    left, max_size, char_dict = 0, 0, {}
    for right, c in enumerate(strs):
        if c not in char_dict or char_dict[c] < left:
            max_size = max(max_size, right - left + 1)
        else:
            left = char_dict[c] + 1
        char_dict[c] = right
    return max_size

print(longest_squence("abcabcbbbhdjhehdjjsjdiebf"))