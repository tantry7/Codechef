finally_array = []
#def logic_part():
	
#def cheficecream(t):
ts = int(input())
for i in range(ts):
	len_N = int(input())
	string_N = list(map (int, input().strip().split()))
	string_N.append(999)
	c_5,c_10 = 0,0
	tt = len(string_N)+1
	for i in range(1,tt):
		if string_N[0]>5:
			(finally_array.append("NO"))
			break
		else:
			if i == tt:
				finally_array.append("YES")
			else:
				if (string_N[i])== 10:
					if c_5>=1:
						c_5 = c_5 - 1
						c_10 = c_10+1
						#print(c_5,c_10)
					else:
						(finally_array.append("NO"))
						break
				elif (string_N[i])==15:
					if c_10>0:
						c_10 = c_10 -1
						c_10 = c_10 +1
						c_5 = c_5 +1
						#print(c_5,c_10)
					elif c_5>1:
						c_5 = c_5-2
						c_10 = c_10 +1
						c_5 = c_5 +1
						#print(c_5,c_10)	
					else:

						(finally_array.append("NO"))
						break
				else:
					c_5 = c_5 +1
					

for i in range(len(finally_array)):
	print(finally_array[i])
