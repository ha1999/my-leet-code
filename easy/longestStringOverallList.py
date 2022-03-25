def longestCommonPrefix(strs):
    def longestPrefixToString(s1, s2):
        s = ""
        for ind in range(len(s1)):
            try:
                if s2[0:ind + 1] == s + s1[ind]:
                    s += s1[ind]
                else:
                    break
            except:
                break
        return s

    prefix = strs[0]
    for i in range(1, len(strs)):
        prefix = longestPrefixToString(prefix, strs[i])
        if prefix == "":
            return ""
    return prefix
