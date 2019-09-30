def day(y,m):
	if m == 2:
		if y%4 == 0:
			if y%100 == 0 and y%400!= 0:
				return days[m]
			else :
				return 29
		else :
			return days[m]
	else :
		return days[m]

n = int(input())
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for _ in range(n) :
	y,m,d = map(int,input().split(":"))
	if d%2 == 0:
		date = 0
	else:
		date = 1
	meds = 0
	while day(y,m)%2 == 0:
		if date == 1:
			meds += (day(y,m)+1-d)//2
			d = 1
		else :
			meds += (day(y,m)-d)//2 +1
			d = 2
		m += 1
		if m == 13:
			m = 1
	meds += (day(y,m) - d)//2 +1
	print(meds)
	


