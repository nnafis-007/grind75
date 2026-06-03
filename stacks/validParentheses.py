def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    matching = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    st = []
    for ch in s:
        if ch in ['(', '{', '[']:
            st.append(ch)
        else:
            if len(st) > 0 and st[-1] == matching[ch]:
                st.pop()
            else:
                return False
    return len(st) == 0



s = input("Enter Parentheses : ")
while s:
    print(isValid(s))
    s = input("Enter Parentheses : ")


        