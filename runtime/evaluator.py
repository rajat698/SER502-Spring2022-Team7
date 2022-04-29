# stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))


class Evaluator:

    def __init__(self):
        self.env = {}


    def readTree(self, tree):
        tree=tree.strip()
        start=0
        # NODE
        i=start
        while i<len(tree):
            if tree[i]=='(':
                node = tree[:i]
                start = i+1
                break 
            i+=1
        #print('NODE: ', node)
        # LEFT CHILD
        i=start
        bracketsCount = 0
        while i<len(tree):
            if tree[i]=='(':
                bracketsCount+=1
            elif tree[i]==')':
                bracketsCount-=1
            elif tree[i]==',' and bracketsCount == 0:
                leftChild = tree[start:i]
                start = i+1
                break
            i+=1
        #print('LEFT: ', leftChild)
        #print('RIGHT: ', tree[start:len(tree)-1])
        return [node, leftChild, tree[start:len(tree)-1]]
    

if __name__=='__main__':
    eval = Evaluator()
    s = 'stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))'
    eval.readTree(s)