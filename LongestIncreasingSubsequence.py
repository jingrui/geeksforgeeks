def lis(l):
	lislen = [1]*len(l)
	prev = dict()
	res = []

	for i in range(1,len(l)):
		for j in range(0,i):
			if l[i] > l[j] and lislen[i] < lislen[j] + 1:
				lislen[i] = lislen[j]+1
				prev[l[i]] = l[j]

	# for ele in zip(l,lislen):
	# 	print ele

	lisEnding = max(lislen)
	print 'longest length is ',lisEnding

	indx = lislen.index(lisEnding)
	key = l[indx]
	res.insert(0,key)
	while prev.has_key(key):
		key = prev[key]
		res.insert(0,key)

	print res

ip = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# 0, 2, 6, 9, 13, 15
ip = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# 10, 22, 33, 50, 60, 80
lis(ip)