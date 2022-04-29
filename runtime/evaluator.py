# stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))


class Evaluator:

    def __init__(self):
        self.env = {}
        self.defaultValues = {'int':0, 'str':'', 'bool':False }


    def readTree(self, tree):
        tree=tree.strip()
        leaves = []
        start=0
        # NODE
        i=start
        while i<len(tree):
            if tree[i]=='(':
                node = tree[:i].strip()
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
                    leaves.append(tree[start:i].strip())
            elif tree[i]==',' and bracketsCount == 0:
                leaves.append(tree[start:i].strip())
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
        print(self.env)
        print('*******************')
        
        # numbers
        if node=='num':
            val = int(leaves[1])
            if leaves[0]=='neg':
                val*=-1
            return val
        
        # identifiers
        elif node == 'id':
            #TODO: init error
            return self.env[leaves[0]]['val']

        # string
        elif node == 'str':
            return leaves[0]

        # boolean
        elif node == 'bool':
            return leaves[1]=='True'

        # addition
        elif node == 't_add':
            #TODO: data type errors
            return self.evaluate(leaves[0]) + self.evaluate(leaves[1])

        # subtraction
        elif node == 't_sub':
            #TODO: data type errors
            return self.evaluate(leaves[0]) - self.evaluate(leaves[1])
        
        # multiplication
        elif node == 't_mul':
            #TODO: data type errors
            return self.evaluate(leaves[0]) * self.evaluate(leaves[1])

        # division
        elif node == 't_div':
            #TODO: data type errors
            return int(self.evaluate(leaves[0]) / self.evaluate(leaves[1]))

        # modulo
        elif node == 't_mod':
            #TODO: data type errors
            return self.evaluate(leaves[0]) % self.evaluate(leaves[1])

        elif node == 'dec':
            #TODO: multiple init errors
            self.env[leaves[1]] = {'type': leaves[0], 'val': self.defaultValues[leaves[0]]}

        elif node == 'assign':
            #TODO: type mismatch errors, init errors
            self.env[leaves[0]]['val'] = self.evaluate(leaves[1])

        elif node == 'decAssign':
            #TODO: multiple init errors
            self.env[leaves[1]] = {'type': leaves[0], 'val': self.evaluate(leaves[2])}
            pass

        elif node == 'display':
            print(self.evaluate(leaves[0]))

        elif node == 'stmt_list':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])


        
        
        



        # for l in leaves:
        #     #TODO: recursively evaluate leaves
        #     self.evaluate(l)


        

    

if __name__=='__main__':
    eval = Evaluator()
    s = 'stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))'
    s1 = 'display(id(y))'
    s2 = 'forT( assign(id(x), 0), lt(id(x), 10), assign(id(x), t_add(id(x), 1)), stmt_list( display(id(x)), display(id(y)) ) )'
    s3 = 'id(x)'
    s4 = 'num(neg,6)'
    print(eval.evaluate(s4))