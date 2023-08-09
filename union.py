def union(a,b,n,m):
    a.extend(b)
    s = set(a)
    print("output",len(s))
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n,m = map(int,input().split())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
    # c = 0
        union(a,b,n,m)



