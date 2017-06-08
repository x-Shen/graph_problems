def w_prefer_m1_over_m(w, m, m1, women_pref_list):
    for i in range(len(women_pref_list)):
        if women_pref_list[w][i] == m1:
            return True
        if women_pref_list[w][i] == m:
            return False
        
def gale_shapley(men_pref_list, women_pref_list):
    n = len(women_pref_list)
    w_match = [-1]*n
    m_free = [True]*n
    free_count = n
    
    while free_count > 0:
        for m in range(n):
            if m_free[m] == True:
                break
        for i in range(n):
            if m_free[m] == True:
                w = men_pref_list[m][i]
                if w_match[w] == -1:
                    w_match[w] = m
                    m_free[m] = False
                    free_count-=1
                else:
                    m_a = w_match[w]
                    if w_prefer_m1_over_m(w, m_a, m, women_pref_list):
                        w_match[w] = m
                        m_free[m] = False
                        m_free[m_a] = True
    print("Woman Man")
    for i in range(n):
        print(str(i) + " ", w_match[i])
    return w_match

mp = [[1,0,2,3],[3,0,1,2],[0,2,1,3],[1,2,0,3]]
                    
wp = [[0,2,1,3],[2,3,0,1],[3,1,2,0],[2,1,0,3]]                    
    
gale_shapley(mp,wp)
