def reverseWord(s):
    #your code here
    #return s[::-1]
    #s = list(s)
    new_s = []
    start = 0
    end = len(s)-1
    while end>=0:
        # s[start],s[end] = s[end],s[start]
        # start += 1
        # end -= 1
        new_s.append(s[end])
        end -= 1
    return ''.join(new_s)
if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1