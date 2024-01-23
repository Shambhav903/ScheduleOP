
import math as m

#possible combination in one slot/ Atom
x = 7*3*3

# We have 54 slots
sample_space = x**54
print(sample_space)

# valid gene
# for one student group routine we have 6 subject 
# Each can take 2 slots out of 18
subject = m.comb(18,2)*m.comb(16,2)*m.comb(14,2)*m.comb(12,2)*m.comb(10,2)*m.comb(8,2)

# We repeat the process for 3 student group
subject = subject**3 

# For class room there are 6 possible permutations for each 3 slots
# and we have 54/3 = 18 slots
classroom = 6**18

# same case for student group
std_group = classroom

# so valid combinations 
valid_comb = subject * classroom * std_group

print(valid_comb)

#so our possibility of success in random gene generation is
p = valid_comb/sample_space
print(p)

#and if X is the variable denoting number of attempt till success
# P(X = x) = p(1-p)^(x-1)
# SO likely geometric distribution may be

# Sample Space = 14601237679858996298815301366968746851833158530173472717993494362270603799169733577011077734556289
# Valid Combinations = 27664999286436887987370227579581082669168654880526565376000000
# p = 1.8947023459934562e-36



