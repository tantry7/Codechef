T = int(input())
final_array = []
for i in range(T):
    n = int(input())
    sum,final_sum = 0,0
    str = list(map(int,input().split()))
    for i in range(len(str)-1):
        sum = abs(str[i]-str[i+1])-1
        final_sum = final_sum + sum
    final_array.append(int(final_sum))
   
       

for i in range(len(final_array)):
    print(final_array[i])
    
