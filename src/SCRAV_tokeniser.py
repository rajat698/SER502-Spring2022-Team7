file = open("/Users/rajat/Documents/Uni/SER502/SER502-Spring2022-Team7/src/test.txt", "r")
sample = file.read()

# sample = sample.replace("\n", " ")
keywords = ["for"]
keywords_language = ["shuru"]
specials = '\=+-},{/;\()<>\"\"'

stack = []
final_stack = []
x = 0

for i in range(len(sample)):
    if sample[i] == " " and sample[x+1:i] not in keywords:
        stack.append(sample[x:i])
        x = i + 1

    elif sample[x:i] == "for-loop":
        stack.append(sample[x:i])
        x = i + 1
        continue

    elif sample[x:i] in keywords_language:
        stack.append(sample[x:i])
        x = i + 1
        continue     
    
    #Example: i=
    elif sample[i] in specials and sample[i - 1] not in specials and sample[x+1:i] not in keywords:
        stack.append(sample[x:i])        
        stack.append(sample[i])
        x = i + 1
    
    #Example: ++
    elif sample[i] in specials and sample[x+1:i] not in keywords:
        stack.append(sample[i])
        x = i + 1
    


for new_line in stack:
    final_stack.append(new_line.replace("\n", ""))

while("" in final_stack):
    final_stack.remove("")

print(final_stack)