file = open("test.txt", "r")
sample = file.read()

keywords = ["for"]
keywords_language = ["shuru"]
specials = set(["=", "+", "-", "}", ",", "{", "/", ";", "\\", "(", ")", "<", ">", ":", "|", "~", "*" ])
syntactic_sugar_elements = set(["+", "-", '*', "/", "|", "~"])



x = 0

def tokenise(sample):
    x = 0
    i = 0
    stack = []
    final_stack = []
    while(i < len(sample)):

        #Example: Sup world
        if sample[i] == " " or sample[i] == "\n" and sample[i - 1] not in specials and sample[x+1:i] not in keywords:
            # print("TAG-C", sample[x:i])
            stack.append(sample[x:i])
            x = i + 1
            i += 1
            continue

        # Example: "Hello, world! :)" (String)
        elif sample[i] == '"':
            stack.append(sample[i])

            for j in range(i + 1, len(sample)):
                
                if sample[j] == '"':
                    new_string = sample[i+1:j]
                    substring_length = len(new_string)
                    break

            k = 0
            for l in range(len(new_string)):
                if new_string[l] == " ":
                    stack.append(new_string[k:l])
                    k = l + 1

                elif l == len(new_string) - 1:
                    stack.append(new_string[k:l+1]) 

            stack.append('"')
            i += substring_length + 2
            x = i + 1
            continue

        # Example: for-loop()
        # elif sample[x:i] == "for-loop":
        #     #print("FORLOOP", sample[x:i])
        #     stack.append(sample[x+1:i])
        #     x = i + 1
        #     i += 1
        #     continue   
        
        #Example: i=
        elif sample[i] in specials and sample[i - 1] not in specials and sample[x+1:i] not in keywords:
            # print("TAG-A", sample[x], "and", sample[x:i],"and", sample[i])
            stack.append(sample[x:i])        
            stack.append(sample[i])
            x = i + 1
            i += 1
            continue
        
        #Example: ++
        elif sample[i] in specials and sample[x+1:i] not in keywords:
            # print("TAG-B", sample[i])
            stack.append(sample[i])
            x = i + 1
            i += 1
            continue

        #Example: End of the code
        elif i == len(sample) - 1:

            stack.append(sample[x:i+1])
            x = i + 1
            i += 1
            continue

        else:
            i += 1
            continue
        
    for new_line in stack:
        final_stack.append(new_line.replace("\n", ""))
    
    while("" in final_stack):
        final_stack.remove("")

    return final_stack


final_stack = tokenise(sample)
#Syntactic sugar
for i in range(len(final_stack)):
    if final_stack[i] in syntactic_sugar_elements and final_stack[i + 1] == "=":
        final_stack.insert(i + 2, final_stack[i])
        final_stack[i] = "="
        final_stack[i + 1] = final_stack[i - 1]

def main():
    print(final_stack)

if __name__ == "__main__":
    main()