class Tokenizer:

    def __init__(self) -> None:
        self.keywords = set(['shuru', 'khatam', 'int', 'str', 'bool', 'True', 'False', 'for-loop', 'in', 'range', 'if', 'else', 'display', 'func'])
        self.comparators = set(['+=', '-=', '*=', '/=', '>=', '==', '<='])
        self.operators = set(['+', '-', '*', '/', '%', '<', '>', '='])
        self.delimiters = set([';', '(', ')', '{', '}', ',', '?', ':'])
        

    def tokenizerV2(self,text):
        #print('TEXT:', text)
        text=text.strip()
        tokens = []

        
        if not len(text):
            return []
        
        # KEYWORD
        if text in self.keywords:
            return [text]

        # for-loop
        if text.startswith('for-loop'):
            return ['for-loop'] + self.tokenizerV2(text[len('for-loop'):])
        
        # string
        if text[0]=='"':
            i=1
            while(i<len(text)):
                if text[i] == '"':
                    tokens.append(text[0]) # "
                    tokens.append(text[1:i]) # string
                    tokens.append(text[i]) # "
                    return tokens + self.tokenizerV2(text[i+1:])  
                i+=1

        # comment
        if text.startswith('$$'):
            i=2
            while i<len(text):
                if text[i]=='$' and text[i-1]=='$':
                    return self.tokenizerV2(text[i+1:])
                i+=1

        
        # syntactic sugar and comparators 
        if text[:2] in self.comparators:
            tokens.append(text[:2])
            return tokens + self.tokenizerV2(text[2:])  


        # operators
        if text[0] in self.operators or text[0] in self.delimiters:
            tokens.append(text[:1])
            return tokens + self.tokenizerV2(text[1:])  

        # everything else
        i=0
        while(i<len(text)):
            if text[i] in self.delimiters or text[i] in self.operators:
                tokens.append(text[:i])
                return tokens + self.tokenizerV2(text[i:])
            elif text[i] == ' ':
                tokens.append(text[:i])
                return tokens + self.tokenizerV2(text[i+1:])
            i+=1
        
        return [text]



    def tokenizeProgram(self, program):
        tokens = []
        for line in program.split('\n'):
            tokens += self.tokenizerV2(line)
        return tokens

        
    
if __name__ == "__main__":

    Tk = Tokenizer()

    tokens = []
    sample2 = 'for-loop(i in range(2,4)) { z = z+ 2; } '
    sample3 = 'x == 10 ?              display zzz : x = 10;'
    sample4 = ' $$this is a commmmment $$ if (x==5) { display "no else is okay" ; }   '


    print(Tk.tokenizeProgram(sample4))

    # for line in sample4.split('\n'):
    #     #for word in line.split(' '):
    #     print('WORD: ', line )
    #     print('TOKENS: ', Tk.tokenizerV2(line))
    #     print('**************************')
    #     tokens += Tk.tokenizerV2(line)
    # #print(tokens)
    # print(tokenizerV2('"hello world"'))
    # print(tokenizerV2('""'))
    # print(tokenizerV2('i=i+1;)'))
    # print(tokenizerV2('for-loop(i'))
    # print(tokenizerV2('asdf123+=2;'))