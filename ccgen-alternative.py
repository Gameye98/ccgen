# author: DedSecTL/Gameye98
# team: BlackHole Security
# alternative method for luhn algorithm
import random

g = "\x1b[1;32m" # green color format
n = "\x1b[0m" # normal color format

result = []
f = open("result.txt","w")
while True:
	if len(result) > 10: break
	x = 0
	nvar = 0
	num = []
	num_n = []
	num_s = []
	for i in range(random.randrange(13, 16)):
		num.append(random.randrange(0,9))
	for num_x in num[::-1]:
		if x == 1:
			num_xx = num_x * 2
			if num_xx > 9:
				num_xx = num_xx % 10 + 1
			num_n.append(num_xx)
			x = 0
		elif x == 0:
			num_n.append(num_x)
			x = 1
	for n in num: num_s.append(str(n))
	for n in num_n: nvar+=n
	if nvar == 70:
		print(f"{g}{''.join(num_s)}{n}")
		f.write("".join(num_s)+"\n")
		result.append("".join(num_s))
