def longestCommonPrefix(strs):
    def longestPrefixToString(sts, s2):
        prefix = []
        for s1 in sts:
            for pre in range(0, len(s1)):
                s = ''
                for nex in range(pre, len(s1)):
                    s += s1[nex]
                    try:
                        s2.index(s)
                    except ValueError:
                        s = '' if pre == nex else s[0:len(s) - 1]
                        break
                print("S is", s)
                if s != '':
                    if len(prefix) == 0:
                        prefix.append(s)
                    else:
                        if len(s) >= len(prefix[0]) and s != prefix[0]:
                            prefix.append(s)

        return prefix

    abc = strs[0:1]
    for idex in strs:
        print("abc is ", abc, "idex is", idex)
        abc = longestPrefixToString(abc, idex)
    print(abc)


longestCommonPrefix(["reflower", "flow", "flight"])
