sample = "This is a sample extract from a code ; i=i+1 {lmao,}"

stack = []
specials = "=+-"
x = 0

for i in range(len(sample)):
    if sample[i] == " ":
        stack.append(sample[x:i])
        x = i + 1
    
    elif sample[i] in specials:
        stack.append(sample[i-1])
        stack.append(sample[i])
        x = i
    
    elif sample[i-1] in specials:
        stack.append(sample[x+1:i])
        x = i
    
print(stack)