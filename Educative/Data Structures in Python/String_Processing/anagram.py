def solution1(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

def solution2(s1, s2):
    ## normalizing the strings
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()


    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    return True



s1 = "fairy tales"
s2 = "rail safety"
print(solution1(s1, s2))
print(solution2(s1, s2))
