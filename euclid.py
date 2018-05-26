a = input('Enter a: ')
b = input('Enter b: ')
a=int(a)
b=int(b)
#Euclid
def ucln(a, b):
	while b != 0:
		r = a % b
		a = b
		b = r
	return a

def gcd_extend(a,b):
	x=1
	y=0
	x1=0
	y1=1
	while (b!=0):
		q=a//b
		r = a%b
		a=b
		b=r
		x2=x-x1*q
		y2=y-y1*q
		x=x1
		y=y1
		x1=x2
		y1=y2

	print("x = ",x)
	print("y = ",y)
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
print("Nhap n=")
n=int(input())
print("Nhap a=")
a=int(input())
res = modulo_inverse_euclidean(a,n)
if(a==0):
	print("Khong co nghich dao")
else:
	if(n%a==0):
		print("Khong co nghich dao")
	else:
		if(res[0] == 0 & res[1]==0):
			print("Khong co nghich dao")
		else:
			if(res[0]<0):
				c=res[0]+n
				print("a'=%d" % (c))
			else:
				print("a'=%d" % (res[0]))

if __name__ == '__main__':
	gcd_extend(a,b)