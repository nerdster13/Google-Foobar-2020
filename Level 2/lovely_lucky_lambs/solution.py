def solution(total_lambs):
    generous=[]
 
    i = 0
    sum = 0
    while i <= total_lambs:
        cur = 2**i
        generous.append(cur)
        sum += cur
        if sum > total_lambs:
            break
        i += 1
        
    stingy = [1,1]
    sum = 2
    i = 2
    while i <= total_lambs:
        new = stingy[i-1] + stingy[i-2]
        stingy.append(new)
        sum += int(stingy[i])
        if sum > total_lambs:
            break
        i += 1
                
    return abs(len(stingy) - len(generous))    

