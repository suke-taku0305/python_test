s = []
while True:
	a = input()
	if a == "":
		break
	else:
		s.append(input())

n = len(s)
i = 0
l = []
m = []
for i in range(n-1):
	a,b = s[i].split(':')
	l.append(int(a))
	m.append(b)

c = zip(l,m)
d = sorted(c)
ll = []
mm = []
for l,m in d:
	ll.append(l)
	mm.append(m)
judge = False

ll.append(int(s[n-1]))
for i in range(n-1):
	if(ll[n-1]%ll[i] == 0):
		print(mm[i],end="")
		judge = True

if judge == False:
	print(ll[n-1])
else:
	print()