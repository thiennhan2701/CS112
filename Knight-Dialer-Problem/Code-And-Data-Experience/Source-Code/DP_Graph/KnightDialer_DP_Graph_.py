def knightDialer(n):
	if n == 1:
		return 10
	graph = {0:[4, 6], 1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4]}
	cnt = {0:1, 1:1, 2:1, 3:1, 4:1, 6:1, 7:1, 8:1, 9:1}
	for i in range(n - 1):
		tmp = {0:0, 1:0, 2:0, 3:0, 4:0, 6:0, 7:0, 8:0, 9:0}
		for k in cnt:
			for v in graph[k]:
				tmp[v]  += cnt[k]
		cnt = tmp
	return sum(cnt.values()) % (10 **9 + 7)

n = int(input())
print(knightDialer(n))
