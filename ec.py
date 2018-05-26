from collections import namedtuple
import math

Point = namedtuple("Point", "x y")
O = 'Origin'

# y^2 = x^3 + ax + b
# input a,b:
a = int(input('a: '))
b = int(input('b: '))
# input prime p > 3:
p = int(input('p > 3: '))

# check valid input:
def valid(P):
	if P == O:
		return True
	else:
		return (
			(P.y**2 - (P.x**3 + a*P.x+b))%p == 0 and (0 <= P.x < p) and (0 <= P.y < p)
		)

# an inverse for x modulo p:
def modularInverse_p(x):
	# x is not divisible by p
	if x%p == 0:
		raise ZeroDivisionError("Impossible inverse!")
	return pow(x, p-2, p)

# inverse of the point P on the elliptic curve y^2 = x^3 + ax + b
def EC_modularInverse_p(P):
	if P == O:
		return P
	return Point(P.x, (-P.y)%p)

# sum of P and Q on the EC
def EC_add(P, Q):
	if not (valid(P) and valid(Q)):
		raise ValueError("Invalid inputs!")

	# Deal with special cases where either P,Q or P+Q is the origin
	if P == O:
		result = Q
	elif Q == O:
		result = P
	elif Q == EC_modularInverse_p(P):
		result = O
	else:
		# cases not involving the origin
		if P == Q:
			dydx = (3 * P.x**2 + a) * modularInverse_p(2 * P.y)
		else:
			dydx = (Q.y - P.y) * modularInverse_p(Q.x - P.x)
		x = (dydx**2 - P.x - Q.x) % p
		y = (dydx * (P.x - x) - P.y) % p
		result = Point(x, y)

	# check whether the result is valid (different)
	assert valid(result)
	return result

def display(P):
	for name in P._fields:
		print (name, getattr(P,  name))

# main funtion
def main():
	x1 = int(input('P.x: '))
	y1 = int(input('P.y: '))
	P = Point(x1, y1)

	x2 = int(input('Q.x: '))
	y2 = int(input('Q.y: '))
	Q = Point(x2 ,y2)

	R = EC_add(P, Q)

	print('Point P: ')
	display(P)
	print('Point Q: ')
	display(Q)
	print('Point R = P + Q: ')
	display(R)

# execute:
if __name__ == "__main__":
	main()