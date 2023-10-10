
# function that takes in gene and returns the reward/penalty allocated

def get_reward(gene,test = True):
    n = length_of_atom = 3

    primary_conflict = 0
    secondary_conflict = 0

    random = gene
    new_list = [random[i:i+n] for i in range(0, len(random), n)]

    # separate into according to subject group 
    table_student_group_1 = [] 
    table_student_group_2 = [] 
    table_student_group_3 = []

    # according to classes
    table_class_1 = []
    table_class_2 = []
    table_class_3 = []
    # chromosome is the 3 atoms that represent classes at a certain time slot 
    # i.e classes in sunday 9-11 time slot
    chromosomes = []

    # tables 
    for j in range(0, len(new_list)):
        if (new_list[j][1]== 'a'):
            table_student_group_1.append(new_list[j])
        elif (new_list[j][1]== 'b'):
            table_student_group_2.append(new_list[j])
        elif (new_list[j][1]== 'c'):
            table_student_group_3.append(new_list[j])

    for j in range(0, len(new_list)):
        if (new_list[j][2]== '1'):
            table_class_1.append(new_list[j])
        elif (new_list[j][2]== '2'):
            table_class_2.append(new_list[j])
        elif (new_list[j][2]== '3'):
            table_class_3.append(new_list[j])


    # separate into chromosomes ie. 3 atoms representing classes at a time
    
    for i in range(0, len(gene), 9):
        chromosome = gene[i:i+9]
        chromosomes.append(chromosome)
        group_count = {combo: 0 for combo in 'abc'}
        class_count = {combo: 0 for combo in '123'}
        # check if two classes at the same classroom
        # and check if two subject group at same time
        print(chromosome)
        for a in range(0,3):
            if chromosome[2+3*a] in '123':
                class_count[chromosome[2+3*a]] += 1
            if chromosome[1+3*a] in 'abc':
                group_count[chromosome[1+3*a]] += 1
        
        # main checking part
        if  (max([a for a in group_count.values()])>1):
            primary_conflict+=1
        
            if test == True:
                # for testing only
                print(f"group conflict in chromosone {i/9}")

        if  (max([a for a in class_count.values()])>1):
            primary_conflict+=1
            if test == True:
                # for testing only
                print(f"class conflict in chromosone {i/9}")
            
    # to take into account more or less than 18 classes of a subject group 
    if table_student_group_1.count != 18:primary_conflict += 1
    if table_student_group_2.count != 18:primary_conflict += 1
    if table_student_group_3.count != 18:primary_conflict += 1

    ###########################################################
    # For Secondary Conflicts
    
    # Once subject more than twice or less then once per week
    # Check student group table individually, if subject represented by "ABCDEF"
    # is not repeated exactly twice, then conflict occurs
    # count conflict for each repeated occurance of subject and for each student group table    
    if test == True:
        print(table_student_group_1)


    # For student_group_a
    subject_repetitions_count = {combo: 0 for combo in 'ABCDEF'}
    for i in table_student_group_1:
        if i[0] in subject_repetitions_count:
            subject_repetitions_count[i[0]] += 1

    for subject_repetitions_key in subject_repetitions_count.keys():
        if subject_repetitions_count[subject_repetitions_key]!=2:
            secondary_conflict += 1 
            
            if test == True:
                # for testing only
                print(f"subject {subject_repetitions_key} is repeated {subject_repetitions_count[subject_repetitions_key]} times")
                #

    if test == True:
        print(table_student_group_2)

    # For student_group_b
    subject_repetitions_count = {combo: 0 for combo in 'ABCDEF'}
    for i in table_student_group_2:
        if i[0] in subject_repetitions_count:
            subject_repetitions_count[i[0]] += 1

    for subject_repetitions_key in subject_repetitions_count.keys():
        if subject_repetitions_count[subject_repetitions_key]!=2:
            secondary_conflict += 1 

            if test == True:
                # for testing only
                print(f"subject {subject_repetitions_key} is repeated {subject_repetitions_count[subject_repetitions_key]} times")
                #
            

    if test == True:
        print(table_student_group_3)
    # For student_group_c
    subject_repetitions_count = {combo: 0 for combo in 'ABCDEF'}
    for i in table_student_group_3:
        if i[0] in subject_repetitions_count:
            subject_repetitions_count[i[0]] += 1

    for subject_repetitions_key in subject_repetitions_count.keys():
        if subject_repetitions_count[subject_repetitions_key]!=2:
            secondary_conflict += 1 
            
            if test == True:
                # for testing only
                print(f"subject {subject_repetitions_key} is repeated {subject_repetitions_count[subject_repetitions_key]} times")
                #    
    print(table_class_3)            
    return primary_conflict,secondary_conflict