def Match(s):
	if s[0] not in teams.keys():
		teams.update({s[0]:[0,0]})
	if s[3] not in teams.keys():
		teams.update({s[3]:[0,0]})

	if int(s[1])>int(s[2]):
		teams[s[0]][0] = teams[s[0]][0] + 3
	elif int(s[2])>int(s[1]):
		teams[s[3]][0] = teams[s[3]][0] + 3
	else:
		teams[s[3]][0] = teams[s[3]][0] + 1
		teams[s[0]][0] = teams[s[0]][0] + 1

	teams[s[0]][1] = teams[s[0]][1] + int(s[1]) - int(s[2])
	teams[s[3]][1] = teams[s[3]][1] + int(s[2]) - int(s[1])

n = int(input())

output = []

for i in range(n):
	matches = []
	teams = {}
	for j in range(12):
		inp = input().split()
		inp.remove("vs.")
		matches.append(inp)

	for i in matches:
		Match(i)

	teams_sorted = sorted(teams.items(), key=lambda x : x[0], reverse=True)
	teams_sorted = sorted(teams.items(), key=lambda x : x[1], reverse=True)

	output.append((teams_sorted[0][0],teams_sorted[1][0]))

for i in output:
	print(i[0],i[1])