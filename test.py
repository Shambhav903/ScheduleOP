import random

subject = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
batch = ['a', 'b', 'c']
room = ['1','2','3']
seq = [N + n + l for N in subject for n in batch for l in room]
print(seq)
size = len(seq)
print(size)

a = ''
for i in range (0,54) : 
    random_num = random.choice(seq)
    #print( str(random_num))
    a = a + str(random_num)

print(a)

# subject = ['A', 'B', 'C', 'D', 'E', 'F','Break']
# batch = ['Second year', 'Third Year', 'Fourth year']
# room = ['S4','S5','S6']
# seq = [N + n + l for N in subject for n in batch for l in room]
# print(seq)