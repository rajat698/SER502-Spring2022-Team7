# stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))


class Evaluator:

    def __init__(self):
        self.env = {'x':5, 'y':2}


    def readTree(self, tree):
        tree=tree.strip()
        leaves = []
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
        # CHILDREN
        i=start
        bracketsCount = 0
        while i<len(tree):
            if tree[i]=='(':
                bracketsCount+=1
            elif tree[i]==')':
                bracketsCount-=1
                if bracketsCount == -1:
                    leaves.append(tree[start:i])
            elif tree[i]==',' and bracketsCount == 0:
                leaves.append(tree[start:i])
                start = i+1
            i+=1
        return node, leaves

    
    def evaluate(self, tree):
        if '(' not in tree:
            print('EMPTY: ', tree)
            return


        #TODO: add logic to evaluate base case nodes
        node, leaves = self.readTree(tree)
        print(node, " : ", leaves)
        
        # numbers
        if node=='num':
            val = int(leaves[1])
            if leaves[0]=='neg':
                val*=-1
            return val
        
        # identifiers
        elif node == 'id':
            #TODO: Error: variable not initialized
            return self.env[leaves[0]]

        # string
        elif node == 'str':
            return leaves[1]

        # boolean
        elif node == 'bool':
            return leaves[1]=='True'

        
        
        



        for l in leaves:
            #TODO: recursively evaluate leaves
            self.evaluate(l)


        

    

if __name__=='__main__':
    eval = Evaluator()
    s = 'stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))'
    s1 = 'display(id(y))'
    s2 = 'forT( assign(id(x), 0), lt(id(x), 10), assign(id(x), t_add(id(x), 1)), stmt_list( display(id(x)), display(id(y)) ) )'
    s3 = 'id(x)'
    s4 = 'num(neg,6)'
    print(eval.evaluate(s4))