final_array = []
def xystr(t):
	for i in range(t):
		intput_string,final_result = input(),0
		split_intput_string = [char for char in intput_string]
		lens = (len(split_intput_string))-1
		for j in range(lens):
			if split_intput_string[j]=="x" and split_intput_string[j+1]=="y":
				final_result = final_result + 1
				split_intput_string.remove(split_intput_string[j])
				split_intput_string.remove(split_intput_string[j+1])
			elif split_intput_string[j]=="y" and split_intput_string[j+1]=="x":
				final_result = final_result + 1
				split_intput_string.remove(split_intput_string[j])
				split_intput_string.remove(split_intput_string[j+1])
			else:
				final_result =0
		final_array.append(final_result)
	return(final_array)



test_cases = int(input())
t = xystr(test_cases)
for i in range(len(t)):
	print(t[i])