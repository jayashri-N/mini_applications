
'''def countkDist(str1, k):
    n = len(str1)
    ans1,ans2=0,0
    res = 0
    #print("d  c")
    for i in range(0, n):
        dist_count = 0
        cnt = [0] * 27
        for j in range(i, n):
            if(cnt[ord(str1[j]) - 97] == 0):
                dist_count += 1
                cnt[ord(str1[j]) - 97] += 1
            else:
                cnt[ord(str1[j]) - 97] += 1

            if(dist_count <= k):
                res += 1
                #print(dist_count,sum(cnt))
                if sum(cnt)>ans2:
                    ans2=sum(cnt)
                
            if(dist_count > k):
                break
    return ans2	
# Driver Code
str1 = "abcbcae"
k = 2

print(countkDist(str1, k))

# This code is contributed by
# Sairahul Jella
'''

