
testcase = int(input())
i = 0
	
while (i<testcase):
	i += 1	
	n = 0
	num = int(input())
	
	arr = (input().split(" "))
	
	array = []
	length = len(arr)

	while(n<length):
		array.append(int(arr[n]))
		n = n+1

	array = array[:num]
	array = sorted(array)
	
	j = 2
	m1 = array[0]%array[1]
	while(j<num):
		m1 = (m1%array[j])
		j =j+1
		
	print(m1)

