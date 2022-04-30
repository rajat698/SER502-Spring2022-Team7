# stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))


class Evaluator:

    def __init__(self):
        self.env = {}
        self.functions = {}
        self.defaultValues = {'int': 0, 'str': '', 'bool': False}

    def readTree(self, tree):
        tree = tree.strip()
        leaves = []
        start = 0
        # NODE
        i = start
        while i < len(tree):
            if tree[i] == '(':
                node = tree[:i].strip()
                start = i+1
                break
            i += 1
        #print('NODE: ', node)
        # CHILDREN
        i = start
        bracketsCount = 0
        while i < len(tree):
            if tree[i] == '(':
                bracketsCount += 1
            elif tree[i] == ')':
                bracketsCount -= 1
                if bracketsCount == -1:
                    leaves.append(tree[start:i].strip())
            elif tree[i] == ',' and bracketsCount == 0:
                leaves.append(tree[start:i].strip())
                start = i+1
            i += 1
        return node, leaves

    def evaluate(self, tree):
        node, leaves = self.readTree(tree)
        #print(node, " : ", leaves)
        #print(self.env)
        #print('*******************')

        # NUMBERS
        if node == 'num':
            val = int(leaves[1])
            if leaves[0] == 'neg':
                val *= -1
            return val

        # STRING
        elif node == 'str':
            return leaves[0]

        # BOOLEAN
        elif node == 'bool':
            return leaves[1] == 'True'

        # IDENTIFIERS
        elif node == 'id':
            # TODO: init error
            return self.env[leaves[0]]['val']

        # ARITHMETIC EXPRESSIONS
        elif node == 't_add':
            # TODO: data type errors
            return self.evaluate(leaves[0]) + self.evaluate(leaves[1])
        elif node == 't_sub':
            # TODO: data type errors
            return self.evaluate(leaves[0]) - self.evaluate(leaves[1])
        elif node == 't_mul':
            # TODO: data type errors
            return self.evaluate(leaves[0]) * self.evaluate(leaves[1])
        elif node == 't_div':
            # TODO: data type errors
            return int(self.evaluate(leaves[0]) / self.evaluate(leaves[1]))
        elif node == 't_mod':
            # TODO: data type errors
            return self.evaluate(leaves[0]) % self.evaluate(leaves[1])

        # BOOLEAN EXPRESSIONS
        elif node == 'or':
            # TODO: type errors
            return self.evaluate(leaves[0]) or self.evaluate(leaves[1])
        elif node == 'and':
            # TODO: type errors
            return self.evaluate(leaves[0]) or self.evaluate(leaves[1])
        elif node == 'equals':
            # TODO: type mismatch error
            return self.evaluate(leaves[0]) == self.evaluate(leaves[1])
        elif node == 'lt':
            # TODO: type mismatch error
            return self.evaluate(leaves[0]) < self.evaluate(leaves[1])
        elif node == 'gt':
            # TODO: type mismatch error
            return self.evaluate(leaves[0]) > self.evaluate(leaves[1])
        elif node == 'lteq':
            # TODO: type mismatch error
            return self.evaluate(leaves[0]) <= self.evaluate(leaves[1])
        elif node == 'gteq':
            # TODO: type mismatch error
            return self.evaluate(leaves[0]) >= self.evaluate(leaves[1])
        elif node == 'not':
            # TODO: type mismatch error
            return not self.evaluate(leaves[0])

        # STATEMENTS
        elif node == 'stmt_list':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        # declaration
        elif node == 'dec':
            # TODO: multiple init errors
            self.env[leaves[1]] = {'type': leaves[0],
                                   'val': self.defaultValues[leaves[0]]}
        elif node == 'decAssign':
            # TODO: multiple init errors
            self.env[leaves[1]] = {'type': leaves[0],
                                   'val': self.evaluate(leaves[2])}
            pass
        # assignment
        elif node == 'assign':
            # TODO: type mismatch errors, init errors
            self.env[leaves[0]]['val'] = self.evaluate(leaves[1])
        elif node == 'addAssign':
            # TODO: type mismatch errors, init errors
            self.env[leaves[0]]['val'] += self.evaluate(leaves[1])
        elif node == 'subAssign':
            # TODO: type mismatch errors, init errors
            self.env[leaves[0]]['val'] -= self.evaluate(leaves[1])
        elif node == 'mulAssign':
            # TODO: type mismatch errors, init errors
            self.env[leaves[0]]['val'] *= self.evaluate(leaves[1])
        elif node == 'divAssign':
            # TODO: type mismatch errors, init errors
            self.env[leaves[0]]['val'] = int(self.evaluate(
                self.env[leaves[0]]['val'] / leaves[1]))
        elif node == 'display':
            print(self.evaluate(leaves[0]))
        # if-else
        elif node == 'ifelse':
            if self.evaluate(leaves[0]):
                self.evaluate(leaves[1])
            else:
                self.evaluate(leaves[2])
        # for-loop
        elif node == 'forT':
            self.evaluate(leaves[0])
            while(self.evaluate(leaves[1])):
                self.evaluate(leaves[2])
                self.evaluate(leaves[3])
        elif node =='forR':
            iterator = self.env[leaves[0]]
            iterator['val'] = self.evaluate(leaves[1])
            stopVal = self.evaluate(leaves[2])
            while iterator['val'] <= stopVal:
                self.evaluate(leaves[3])
                iterator['val']+=1

        # FUNCTIONS
        elif node=='noneFunc':
            pass
        elif node=='funcList':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
        elif node=='func':
            self.defineFunc(leaves)
        elif node=='call':
            print('call', leaves)
        
        # PROGRAM
        elif node == 'prog':
            self.evaluate(leaves[0])
            self.evaluate(leaves[1])
    
        return 0

    
    def parseParameters(self, tree, Accumulator):
        node, leaves = self.readTree(tree)
        if node == 'nonePmt':
            return
        elif node == 'pmt':
            Accumulator.append(leaves)
        elif node == 'pmtList':
            self.parseParameters(leaves[0], Accumulator)
            self.parseParameters(leaves[1], Accumulator)
        
    
    def defineFunc(self, leaves):
        funcName = leaves[0] # bloo
        pmtList = []
        self.parseParameters(leaves[1], pmtList) # [['int', 'a'], ['int', 'b']]
        funcTree = leaves[2]
        self.functions[funcName] = {'parameters': pmtList, 'tree': funcTree}




    


if __name__ == '__main__':
    eval = Evaluator()
    s = 'stmt_list(dec(int, id(x)), stmt_list(assign(id(y), t_add(2, 5)), display(id(y))))'
    s1 = 'display(id(y))'
    s2 = 'forT( assign(id(x), 0), lt(id(x), 10), assign(id(x), t_add(id(x), 1)), stmt_list( display(id(x)), display(id(y)) ) )'
    s3 = 'id(x)'
    s4 = 'num(neg,6)'

    #print(eval.evaluate(s4))

    # acc = []
    # eval.parseParameters('pmtList(pmt(int, a), pmt(int, b))', acc)
    # print(acc)


    f1 = ['bloo', 'pmtList(pmt(int, a), pmt(int, b))', 'stmt_list(dec(int, c), stmt_list(assign(c, t_add(id(a), id(b))), return(id(c))))']
