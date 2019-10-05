t = int(input())
for _ in range(t):
	n,m = list(map(int,input().split()))
	arr = list(map(int,input().split()))
	temp = []
	flag = True
	for i in range(m):
		if len(temp) == n:
			temp = []
			temp.append(arr[i])
		elif arr[i] not in temp:
			temp.append(arr[i])
		else :
			if len(temp)<n and arr[i] in temp:
				flag = False
				break
	if flag == True:
		print("YES")
	else :
		print("NO")
	
	
