import math
def PhucHoiSoHuuTi(m,c):
	u = [1,0,m]
	v = [0,1,c]

	while (math.sqrt(m/2)<v[2]):

		q=u[2]//v[2]
		print(q)
		r=[u[0]-q*v[0],u[1]-q*v[1],u[2]-q*v[2]]
		u=v
		v=r
	if(abs(v[2])>=math.sqrt(m/2)):
		return "no value"
	return [v[2],v[1]]

print(PhucHoiSoHuuTi(15,7))