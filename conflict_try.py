# Generate a random gene
gene = "Aa1Bb2Cc3Da1Eb2Fc3Ga1Aa2Bb3Ca1Db2Ec3Fa1Ga2Ab3Ba1Cb2Dc3Ea1Fa2Ga3Aa1Ba2Cb3Da1Ea2Fa3Ga1Ab2Bb3Cc1Dc2Ea3Fa1Ga2Aa3Ba1Bb2Cb3Da1Ec2Fa3Ga1Ab2Bb3Cc1Dc2Ea3Fa1Ga2Aa3Ba1Bb2Cb3"

# Initialize an empty list to store the chromosomes
chromosomes = []

# Count for conflicts
count = 0

# Define the combinations to check
# HAVE TO INTEGRATE WITH RUBY'S SAMPLE SPACE

combinations = [f"{big}{small}" for big in "ABCDEF" for small in "abc" if f"{big}{small}" not in ["Ga", "Gb", "Gc"]]

# Initialize the count the occurrences of each combination
combination_counts = {combo: 0 for combo in combinations}

# Iterate over the string in chunks of 9 characters and append them to the list
#  INTEGRATE WITH THE DECOMPOSITION FUNCTION 

for i in range(0, len(gene), 9):
    #Chromosome is of 9 character each element is one slot
    chromosome = gene[i:i+9]
    chromosomes.append(chromosome)
    #to count occurance of Aa to Fc - not G as G is for break and can occur multiple times
    for a in range(0,3):
        combination = chromosome[0+3*a:2+3*a]
        #print(combination) #check the combination saved if it matches gene and is 54 element long
        if combination in combination_counts:
            combination_counts[combination] += 1

# Check if all Aa to Fc is of count 2 and update the conflict count for every Aa to Fc that isnt repeated twice
for combo, combo_count in combination_counts.items():
    if combo_count != 2:
        count += 1

# Define a function to check if a chromosome meets the specified conditions
def is_valid_chromosome(chromosome):
    # Check if the chromosome contains 'a', 'b', and 'c' in any order
    # All the student groups are accounted for
    has_abc = all(char in chromosome for char in 'abc')
    # Check if the chromosome contains '1', '2', and '3' in any order
    # All the rooms are accounted for
    has_123 = all(char in chromosome for char in '123')
    return has_abc and has_123

# Increment the count for each valid chromosome
for chromosome in chromosomes:
    if not is_valid_chromosome(chromosome):
        count += 1

# Now, 'chromosomes' is an array with 18 elements, each representing a chromosome
# print("Chromosomes:", chromosomes)
print("Conflict Count:", count)




'''
Conflict
1 clash of same student group in one slot
1 clash of same classroom in one slot
each course and student group combo is repeated twice
'''