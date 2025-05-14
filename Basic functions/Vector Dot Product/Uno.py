def dot(v1, v2):    
    results =  0
    pd = []
    
    for a in range(len(v1)):
        pd.append(v1[a] * v2[a])
        results += pd[a]
    
    return results
    
    