module reward

    function get_reward(gene;test::Bool=false)
        n = length_of_atom = 3
        primary_conflict = 0
        secondary_conflict = 0
        random = gene
        new_list = [random[i:i+n-1] for i in 1:n:length(random)]
        
        table_student_group_1 = [] 
        table_student_group_2 = [] 
        table_student_group_3 = []
        
        table_class_1 = []
        table_class_2 = []
        table_class_3 = []
        
        
        chromosomes = []
        
        for j in 1:length(new_list)
            if new_list[j][2] == 'a'
                push!(table_student_group_1, new_list[j])
            elseif new_list[j][2] == 'b'
                push!(table_student_group_2, new_list[j])
            elseif new_list[j][2] == 'c'
                push!(table_student_group_3, new_list[j])
            end
        end
        
        for j in 1:length(new_list)
            if new_list[j][3] == '1'
                push!(table_class_1, new_list[j])
            elseif new_list[j][3] == '2'
                push!(table_class_2, new_list[j])
            elseif new_list[j][3] == '3'
                push!(table_class_3, new_list[j])
            end
        end
        
        # for i in 1:9:length(gene)
        #     chromosome = gene[i:i+8]
        #     push!(chromosomes, chromosome)
        # end

        for i in 1:9:length(gene)
            chromosome = gene[i:i+8]
            push!(chromosomes, chromosome)
            group_count = Dict(combo => 0 for combo in "abc")
            class_count = Dict(combo => 0 for combo in "123")
            
            if test == true
                println(chromosome)
            end

            
            for j in 1:3
                if occursin(chromosome[3+3*(j-1)],"123")
                    class_count[chromosome[3+3*(j-1)]] += 1
                end
                if occursin(chromosome[2+3*(j-1)], "abc")
                    group_count[chromosome[2+3*(j-1)]] += 1
                end
            end
            
            if maximum(values(group_count)) > 1
                primary_conflict += 1
                if test == true
                    println("group conflict in chromosone ", i/9)
                end
            end
            if maximum(values(class_count)) > 1
                primary_conflict += 1
                if test == true
                    println("class conflict in chromosone ", i/9)
                end
            end

            if test == true
                println(group_count)
                println(class_count)
            end
        end
        
        

        if length(table_student_group_1) != 18
            primary_conflict += 1
            if(test == true)
                println("primary conflict in group 1")
            end
        end
        if length(table_student_group_2) != 18
            primary_conflict += 1
            if(test == true)
                println("primary conflict in group 2")
            end
        end
        if length(table_student_group_3) != 18
            primary_conflict += 1
            if(test == true)
                println("primary conflict in group 3")
            end
        end

        ###########################################################
        # For Secondary Conflicts

        
        secondary_conflict = 0

        if test == true
            println(table_student_group_1)
        end
        
        subject_repetitions_count = Dict('A'=>0, 'B'=>0, 'C'=>0, 'D'=>0, 'E'=>0, 'F'=>0)
        for i in table_student_group_1
            if i[1] in "ABCDEF"
                subject_repetitions_count[i[1]] += 1
            end
        end
        
        for subject_repetitions_key in "ABCDEF"
            if subject_repetitions_count[subject_repetitions_key] != 2
                secondary_conflict += abs(subject_repetitions_count[subject_repetitions_key] - 2)
                if test == true
                    println("subject ", subject_repetitions_key, " is repeated ", subject_repetitions_count[subject_repetitions_key], " times")
                end
            end
        end

        if test == true
            println(table_student_group_2)
        end
        
        subject_repetitions_count = Dict('A'=>0, 'B'=>0, 'C'=>0, 'D'=>0, 'E'=>0, 'F'=>0)
        for i in table_student_group_2
            if i[1] in "ABCDEF"
                subject_repetitions_count[i[1]] += 1
            end
        end
        
        for subject_repetitions_key in "ABCDEF"
            if subject_repetitions_count[subject_repetitions_key] != 2
                secondary_conflict += abs(abs(subject_repetitions_count[subject_repetitions_key]) - 2)
                if test == true
                    println("subject ", subject_repetitions_key, " is repeated ", subject_repetitions_count[subject_repetitions_key], " times")
                end
            end
        end

        if test == true
            println(table_student_group_3)
        end
        
        subject_repetitions_count = Dict('A'=>0, 'B'=>0, 'C'=>0, 'D'=>0, 'E'=>0, 'F'=>0)
        for i in table_student_group_3
            if i[1] in keys(subject_repetitions_count)
                subject_repetitions_count[i[1]] += 1
            end
        end
        
        for subject_repetitions_key in keys(subject_repetitions_count)
            if subject_repetitions_count[subject_repetitions_key] != 2
                secondary_conflict += abs(abs(subject_repetitions_count[subject_repetitions_key]) - 2)
                if test == true
                    println("subject ", subject_repetitions_key, " is repeated ", subject_repetitions_count[subject_repetitions_key], " times")
                end
            end
        end

        final_reward = primary_conflict*-100 -50*secondary_conflict
        return final_reward
    end
end
