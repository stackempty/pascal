def pascal(n):
    set = [1]
    for x in range(n):
        set.append(0)
        set.insert(0, 0)

        new_set = []
        for y in range(len(set) - 1):
            a = set[y] + set[y + 1]
            new_set.append(a)
        
        set = new_set
    return set


def pascal_v2(n):
    line = [1]
    for x in range(n):
        line.append(line[x] * (n - x) / (x + 1))
    
    return line
