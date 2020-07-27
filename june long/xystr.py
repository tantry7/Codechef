final_array = []
def xystr(t):
	for i in range(t):
		final_sum,i = 0,0
		sample_string = input()
		main_string = [char for char in sample_string]
		main_string.append('f')
		#print(main_string)
		while i!= (len(main_string)):	
			if main_string[i]=='x':
				if main_string[i+1]=='y':
					#print(main_string[i],main_string[i+1])
					final_sum = final_sum +1
					i = i+2
				else:
					i = i+1
			elif main_string[i]=='y':
				if main_string[i+1]=='x':
					#print(main_string[i],main_string[i+1])
					final_sum = final_sum +1
					i = i+2
				else:
					i = i+1
			else:
				i = i+1
		final_array.append(final_sum)

test_cases = int(input())
answer = xystr(test_cases)
for i in range(len(final_array)):
	print(final_array[i])
