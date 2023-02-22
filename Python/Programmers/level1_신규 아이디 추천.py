def solution(new_id):
    print(new_id)
    
    #level 1
    new_id = new_id.lower()
    
    #level2
    s = [chr(i) for i in range(ord('a'),ord('z')+1)]
    s += [chr(i) for i in range(ord('A'),ord('Z')+1)]
    s += [chr(i) for i in range(ord('0'),ord('9')+1)]
    s += ['-', '_', '.']
    p = []
    print(s)
    for x in range(len(new_id)-1, -1, -1):
        if new_id[x] not in s:
            p.append(x)
    for x in p:
        if x == len(new_id)-1:
            new_id = new_id[:-1]
        else:
            new_id = new_id[:x] + new_id[x+1:]            
    print(new_id)
    
    #level3
    while True:
        if '..' in new_id:
            a = new_id.split('..')
            new_id = ""
            for x in a:
                new_id = new_id + x + "."
            new_id = new_id[0:-1:1]
        else:
            break
    print(new_id)
    
    #level4 
    if new_id and new_id[0] == '.':
        if len(new_id) == 1:
            new_id = ''
        else :
            new_id = new_id[1:]
            
    if new_id and new_id[-1] == '.':
        if len(new_id) == 1:
            new_id = ''
        new_id = new_id[:-1]
    print(new_id)

    # level 5
    if not new_id:
        new_id = 'a'
    
    #level 6
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    
    #level 7
    while len(new_id) <= 2:
        new_id += new_id[-1]
    
    return new_id
