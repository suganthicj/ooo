x111=str(input())
for j in range(1,len(x111)):
	if(x111[j].isdigit()==True):
		z111=int(x111[j])
		for j in range(0,z111):
			print(x111[j-1],end="")
