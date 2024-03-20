def monk_index(u,k):
    #get covers of u
    u_covers = Permutation(u).bruhat_succ_iterator()
    
    #should check to make sure k is valid
    #lengths of u and w?
    
    u_k_covers = []
    #check which covers are k-Bruhat covers
    for w in u_covers:
        size_w = w.size()
        kb_cover = True
        for a in range(k+1):
            if not u[a] <= w[a]:
                kb_cover = False
                break
        if kb_cover == False:
            continue
        for b in range(k+1,size_w):
            if not u[b] >= w[b]:
                kb_cover = False
                break
        if kb_cover == False:
            continue
        for a in range(size_w):
            for b in range(a+1,size_w):
                if u[a] < u[b] and w[a] > w[b]:
                    if not (a <= k and k < b):
                        kb_cover = False
                        break
            if kb_cover == False:
                break
        if kb_cover == False:
            continue
        elif kb_cover == True:
            u_k_covers.append(w)
    return u_k_covers

print(monk_index([1,3,5,6,4,2],4))
