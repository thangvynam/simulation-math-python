characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
			'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
			'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# n là co so của p
n = input('Enter N: ')

p = input('Enter p: ')

#co so can chuyen qua
q = input('Enter q: ')


#chuyen to so thap phan n sang co so q
def int_to_q(n, q):
	q_str = ''
	l = []

	while n >= q:
		l.append(n % q)
		n = n // q
	l.append(n % q)

	l.reverse()
	for x in l:
		q_str = q_str + characters[int(x)]

	return q_str


#chuyen tu so co he so la p sang thap phan
def np_to_dec(n, p):
	dec = 0
	n = n[::-1]
	length = len(n)

	for x in range(0, length):
		dec = dec + characters.index(n[x]) * p ** x

	return dec


if __name__ == '__main__':
	dec = np_to_dec(n.lower(), int(p))
	result = int_to_q(dec, int(q))
	print (result)