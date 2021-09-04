def knightDialer(n):
        f = [10,20,46,104]
        if n <= 4:
            return f[n-1]
        cnt = 5
        while cnt <= n:
            temp = f[3]- f[2]*2
            if cnt % 2 != 0: temp+= f[1]    
            else: temp *= 2
            f.append((f[3]*2 + temp)%(10**9+7))
            f.pop(0)
            cnt+=1
        return f[-1]%(10**9+7)

n = int(input())
print(knightDialer(n))
