def solution(s):
    s = s.lstrip('<')
    s = s.rstrip('>')
    
    count = 0
    for i,char in enumerate(s[::-1]):
        if char == "<":
            ite = len(s) - i
            count += s[:ite].count(">")
    
    return 2*count

