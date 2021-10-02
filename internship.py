all_lines=[]
#Taking file name input to read through and opening the files.
file_name=input("Enter file name you want to test(.txt): ")
with open(file_name+".txt", "r") as f:
    with open("result.txt", "w+") as k: 
        #converting each line of the file to a list, where each line is represented as a element of the list.      
        for line in f:
            stripped_line = line.rstrip()
            all_lines.append(stripped_line)
        #basic question tags which is used to identify a statement is a question.
        question_tags=['which','who','?','when','where','what','how','why']
        #iterating to each statement
        for i in all_lines:
            #iterating to check each statement and an occurence of a question tag.
            for j in question_tags:
                #when a question statement is found adding it to the result file with a YES.
                if j in i:
                    temp=i+" "*(50-len(i))+"Yes"
                    k.write(f'{temp}\n')
                    break
            #when a question statement is not found and adding it to the result file with a NO.
            else:
                temp1=i+" "*(50-len(i))+"No"
                k.write(f'{temp1}\n')
