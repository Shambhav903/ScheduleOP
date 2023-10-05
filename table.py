from prettytable import PrettyTable

#splitting the string into 3 elements each
random = "Aa1Bb2Cc3Da1Eb2Fc3Ga1Aa2Bb3Ca1Db2Ec3Fa1Ga2Ab3Ba1Cb2Dc3Ea1Fa2Ga3Aa1Ba2Cb3Da1Ea2Fa3Ga1Ab2Bb3Cc1Dc2Ea3Fa1Ga2Aa3Ba1Bb2Cb3Da1Ec2Fa3Ga1Ab2Bb3Cc1Dc2Ea3Fa1Ga2Aa3Ba1Bb2Cb3"
n = 3
new_list = [random[i:i+n] for i in range(0, len(random), n)]

table_1 = [] 
table_2 = [] 
table_3 = [] 

t1 = PrettyTable(['9-11','12-2','2-4'])
t2 = PrettyTable(['9-11','12-2','2-4'])
t3 = PrettyTable(['9-11','12-2','2-4'])

for j in range(0, len(new_list)):
    if (new_list[j][1]== 'a'):
        table_1.append(new_list[j])
    if (new_list[j][1]== 'b'):
        table_2.append(new_list[j])
    if (new_list[j][1]== 'c'):
        table_3.append(new_list[j])

new_t_1 = [table_1[i:i+n] for i in range(0, len(table_1), n)]
new_t_2 = [table_2[i:i+n] for i in range(0, len(table_2), n)]
new_t_3 = [table_3[i:i+n] for i in range(0, len(table_3), n)]

t1.add_rows(new_t_1)
t2.add_rows(new_t_2)
t3.add_rows(new_t_3)


print(t1)
print(t2)
print(t3)
