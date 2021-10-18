#The Normal Python Function
def pow1(a,b):
	return a**b

#Computes a^b (integers a,b)
#Only works for b >= 0
def pow2(a,b):
	total=1
	for i in range(0,b):
		total=total*a
	return total

#Computes a^b (integers a,b)
#Only works for b >= 0
def pow3(a,b):
	if b==0:
		return 1
	elif b%2==1:
		return a*pow3(a,b-1)
	else:
		temp=pow3(a,b//2)
		return temp*temp