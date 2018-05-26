# a^b mod n
def bisectionModule(a,b,n):
	r = 1
	while b>0:
		if b%2==1:
			a %= n
			r *= a
		a *= a
		b = int(b/2)
	return r%n
print(bisectionModule(2,3,3))