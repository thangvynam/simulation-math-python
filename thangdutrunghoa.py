def gcd(a,b):	
	while (b!=0):
		t=a%b
		a=b	
		b=t
	return a
def modulo_inverse_euclidean(a,n):
	if(gcd(a,n)!=1):
		return [0,0]
	else:
		u1,u2,u3=1,0,a
		v1,v2,v3=0,1,n
		while (v3!=0):
			q=(u3//v3)
			t1,t2,t3=u1-q*v1,u2-q*v2,u3-q*v3
			u1,u2,u3=v1,v2,v3
			v1,v2,v3=t1,t2,t3
		return [u1,u2]
def phandu_trunghoa(listA,listM):
	Mi=1
	sum=0
	for i in range(len(listA)):
		 for j in range(len(listA)):
		 	if(i!=j):
		 		Mi*=listM[j]
		 res = modulo_inverse_euclidean(Mi,listM[i])
		 if(res[0]<0):
				res[0]+=listM[i]
		 print(res[0]*Mi)
		 sum+=(res[0]*Mi*listA[i])
		 Mi=1
	M=1
	print(sum)
	for i in range(len(listM)):
		M*=listM[i]
	return (sum%M)
listA=[2,3,1]
listM=[3,4,5]
print(phandu_trunghoa(listA,listM))