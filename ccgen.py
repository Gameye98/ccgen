# author: DedSecTL/Gameye98
# team: BlackHole Security
# sample script for luhn algorithm
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
	for i in range(random.randrange(13, 17)):
		num.append(random.randrange(0,10))
	for num_x in num[:len(num)-1][::-1]:
		if x == 0:
			num_xx = num_x * 2
			if num_xx > 9:
				num_xx = num_xx % 10 + 1
			num_n.append(num_xx)
			x = 1
		elif x == 1:
			num_n.append(num_x)
			x = 0
	for n in num: num_s.append(str(n))
	for n in num_n: nvar+=n
	if int(str(nvar * 9)[-1]) == num[-1]:
		print(f"{g}{''.join(num_s)}{n}")
		f.write("".join(num_s)+"\n")
		result.append("".join(num_s))
