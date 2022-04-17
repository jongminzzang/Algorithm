def solution(id_list, report, k):
    len_m = len(id_list)
    d = {x : i for i,x in enumerate(id_list)}
    r = [[0 for _ in range(len_m)] for _ in range(len_m)]
    
    for x in report:
        a, b = x.split(' ') 
        r[d[b]][d[a]] = 1
        
    for x in r:
        if sum(x) >= k:
            pass
        else:
            x[:] = [0]*len_m
    
    answer = []
    r2 = list(zip(*r))
    for x in r2:
        answer.append(sum(x))    
    return answer
