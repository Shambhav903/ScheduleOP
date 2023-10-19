import random
random.seed(10)
prob = 0.49

def create_gene():
    '''
    create chromosome or string of genes
    Ruby
    '''
    possible_combinations = [f"{subject}{group}{classroom}" for subject in "ABCDEFG" for group in "abc" for classroom in "123"]
    a = ''
    for i in range (0,54) : 
        random_num = random.choice(possible_combinations)
        a = a + str(random_num)
    return a

def pick_an_atom_for_me(atom_1,atom_2):
    possible_combinations = [f"{subject}{group}{classroom}" for subject in "ABCDEFG" for group in "abc" for classroom in "123"]
    x = random.uniform(0, 1)
    if x <= prob:
        return atom_1
    elif x <= prob*2:
        return atom_2
    return random.choice(possible_combinations)

def give_me_my_child(parent_1,parent_2):
    n = size_of_atom = 3 
    child = []
    parent_1_separated_into_atoms = [parent_1[i:i+n] for i in range(0, len(parent_1), size_of_atom)]
    parent_2_separated_into_atoms = [parent_1[i:i+n] for i in range(0, len(parent_2), size_of_atom)]
    for i in range(len(parent_1_separated_into_atoms)):
        child.append(pick_an_atom_for_me(parent_1_separated_into_atoms[i],parent_2_separated_into_atoms[i]))
    return ''.join(child)

def sort_my_genes(unsorted_list):
    test_list = []
    sorted_list = []
    for i in unsorted_list:
        test_list.append((i,get_reward(i)))
    test_list.sort(key = lambda x: x[1],reverse=True)
    for i in test_list:
        sorted_list.append(i[0])
    return sorted_list

def genetic_algotithm(list_of_parent_genes):
    # Crossbreeding
    children_genes = []
    for j in range(3):
        random.shuffle(list_of_parent_genes)
        for i in range(0,len(list_of_parent_genes)-1):
            children_genes.append(give_me_my_child(list_of_parent_genes[i],list_of_parent_genes[i+1]))
        # for i in range(0,int(len(list_of_parent_genes)/2)):
        #     children_genes.append(give_me_my_child(list_of_parent_genes[i],list_of_parent_genes[i+1]))
                
        
    children_genes = sort_my_genes(children_genes)
    return children_genes[0:500]

def get_my_average_reward(generation):
    total_reward = 0
    gen = generation[0:200]
    for i in gen:
        total_reward += get_reward(i)
    return total_reward/len(gen)

rewards_data = []

def run_my_algo():

    ancestory = []
    gen_temp = []
    gen_temp2 = []

    for i in range(0,500):
        gen_temp.append(create_gene())

    for i in range(0,500):
        gen_temp2.append(create_gene())
    
    print(get_my_average_reward(gen_temp))
    ancestory.append(get_my_average_reward(gen_temp))
    print(f"my average reward is {ancestory[0]} for gen {0}")

    for i in range(0,550):
        gen_temp = genetic_algotithm(gen_temp)
        ancestory.append(get_my_average_reward(gen_temp))
        print(f"my average reward is {ancestory[i+1]} for gen {i+1}")
        if i == 300: prob= 0.45
        if i == 445: prob= 0.49
        


    return ancestory,gen_temp

all_rewards,reward5 = run_my_algo()