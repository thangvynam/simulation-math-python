import random

pa = 59
qa = 71

def gen_e(o):
	while True:
		e = random.randint(1, 100)
		if gcd(e, o) == 1:
			return e


def gcd(p, q):
	while q != 0:
		r = p % q
		p = q
		q = r
	return p


def extend_euclid(p, q):
	xp, yp = 1, 0
	xq, yq = 0, 1
	while q != 0:
		a = p // q
		r = p % q
		p = q
		q = r
		xr = xp - a * xq
		yr = yp - a * yq
		xp, yp = xq, yq
		xq, yq = xr, yr
	return xp, yp


def rsa(p, q):
	na = p * q
	o = (p - 1) * (q - 1)

	# tam co dinh ea
	ea = 671
	# ea = gen_e(o)

	yield [na, ea]

	d = extend_euclid(671, o)[0]
	if d < 0:
		yield d + o
	else:
		yield d


def encrypt(n, e, plantext):
	plantext_bin = ''
	for s in plantext:
		# plantext_bin = plantext_bin + bin(ord(s))[2::]
		s_bin =  bin(ord(s))[2::]
		if len(s_bin) < 8:
			plantext_bin = plantext_bin + '0' * (8 - len(s_bin)) + s_bin
	# print(plantext_bin)
	plantext_split = []
	# chon moi so thap phan la 12 bit
	t = len(plantext_bin)
	i = 0
	while not i >= t:
		plantext_split.append(int(plantext_bin[i:i + 12], 2))
		# plantext_split.append(plantext_bin[i:i + 12])
		i = i + 12
	# print(plantext_split)
	cirpher_text = []

	# print('e: {}'.format(e))
	# print('n: {}'.format(n))

	for m in plantext_split:
		M = m ** e % n
		cirpher_text.append(M)
	return cirpher_text

def decrypt(n, d, cirpher_text):
	plantext = []
	for m in cirpher_text:
		p = m ** d % n 
		plantext.append(p)
	plantext_bin = ''
	for x in plantext:
		str_x = str(bin(x))[2::]
		len_str_x = len(str_x)
		if len_str_x < 12:
			s = '0' * (12 - len_str_x) + str_x
			plantext_bin = plantext_bin + s
	plantext_bin_length = len(plantext_bin)

	p = ''
	i = 0
	while not i >= plantext_bin_length:
		# print(plantext_bin[i:i+8])
		s = chr(int(plantext_bin[i:i+8], 2))
		i = i + 8
		p = p + s
	return p

if __name__ == '__main__':
	pub, private = rsa(pa, qa)
	# print(pub, private)
	cirpher = encrypt(pub[0], pub[1], 'RSA')
	# print(cirpher)
	print(decrypt(pub[0], private, cirpher))