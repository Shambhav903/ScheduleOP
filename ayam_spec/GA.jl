
include("rewardFunc.jl")
using .reward
using Random
using TypedTables

Random.seed!(10)
prob = 0.492

function create_gene()
    possible_combinations = []
    # calculate possible combinations outside for speed
    possible_combinations=[string(a,b,c) for a in "ABCEEF" for b in "abc" for c in "123"]
    random_num = rand(possible_combinations,54)
    return join(random_num)
end

function pick_an_atom_for_me(atom_1, atom_2)
    # calculate possible combinations outside for speed
    possible_combinations=[string(a,b,c) for a in "ABCEEF" for b in "abc" for c in "123"]
    x = rand()
    if x <= prob
        return atom_1
    elseif x <= (prob*2)
        return atom_2
    end
    return rand(possible_combinations)
end


function give_me_my_child(parent_1, parent_2)
    n = 3
    size_of_atom = 3
    child = []
    parent_1_separated_into_atoms = [parent_1[i:i+n-1] for i in 1: size_of_atom: length(parent_1)]
    parent_2_separated_into_atoms = [parent_1[i:i+n-1] for i in 1: size_of_atom: length(parent_2)]
    for i in (1:length(parent_1_separated_into_atoms))
        push!(child, pick_an_atom_for_me(parent_1_separated_into_atoms[i], parent_2_separated_into_atoms[i]));
    end
    return join(child)
end

# probably can be done with one line
function sort_my_genes(unsorted_list)

    # @time sort!(unsorted_list,by = x->reward.get_reward(x),rev = true)
    test_list = []
    sorted_list = []
    for i in unsorted_list
        push!(test_list, (i, float(reward.get_reward(i))))
    end
    # in descending order
    # println(test_list)
    sort!(test_list, by = x -> x[2],rev = true)
    for i in test_list
        push!(sorted_list, i[1]);
    end
    return sorted_list
end

function genetic_algotithm(list_of_parent_genes)
    children_genes = []
    for j in 1:3
        shuffle!(list_of_parent_genes)
        for i in 1:(length(list_of_parent_genes)-1)
            push!(children_genes, give_me_my_child(list_of_parent_genes[i], list_of_parent_genes[i + 1]))
        end
    end
    @time children_genes = sort_my_genes(children_genes)
    return children_genes[1:500]
end


function get_my_average_reward(generation)
    total_reward = 0
    gen = generation[1:200]
    # gen = generation
    for i in gen
        total_reward += reward.get_reward(i)
    end
    return (total_reward/length(gen))
end


function display2(gene)
    n = 3
    new_list = [gene[i:i+n-1] for i in 1:n:length(gene)]
    table_student_group_1 = [] 
    table_student_group_2 = [] 
    table_student_group_3 = []
    days = ["sunday","monday","tuesday","wednesday","thursday","friday"]
    for j in 1:length(new_list)
        if new_list[j][2] == 'a'
            push!(table_student_group_1, new_list[j])
        elseif new_list[j][2] == 'b'
            push!(table_student_group_2, new_list[j])
        elseif new_list[j][2] == 'c'
            push!(table_student_group_3, new_list[j])
        end
    end

    t1 = Table(first = [table_student_group_1[i] for i in 1:3:length(table_student_group_1)], second = [table_student_group_1[i] for i in 2:3:length(table_student_group_1)], third = [table_student_group_1[i] for i in 3:3:length(table_student_group_1)],day = days)
    t2 = Table(first = [table_student_group_2[i] for i in 1:3:length(table_student_group_2)], second = [table_student_group_2[i] for i in 2:3:length(table_student_group_2)], third = [table_student_group_2[i] for i in 3:3:length(table_student_group_2)],day = days)
    t3 = Table(first = [table_student_group_3[i] for i in 1:3:length(table_student_group_3)], second = [table_student_group_3[i] for i in 2:3:length(table_student_group_3)], third = [table_student_group_3[i] for i in 3:3:length(table_student_group_3)],day = days)
    # println(t1)
    return t1
end


rewards_data = []


function run_my_algo()

    ancestory = []
    gen_temp = []
    gen_temp2 = []
    for i in (1:500)
        push!(gen_temp, create_gene());
    end

    println(get_my_average_reward(gen_temp));
    push!(ancestory, get_my_average_reward(gen_temp));

    println("my average reward is ", string(ancestory[1]), " for gen ", string(0));
    println(length(gen_temp))

    for i in (1:250)
        gen_temp = genetic_algotithm(gen_temp);
        push!(ancestory, get_my_average_reward(gen_temp));
        println("my average reward is ", string(ancestory[i+1]), " for gen ", string(i+1));
        # display2(gen_temp[1])
        # if i == 300

    #     prob = 0.45;
    # end
    # if i == 445
    #     prob = 0.49;
    # end
    end
    return (ancestory, gen_temp)
end
