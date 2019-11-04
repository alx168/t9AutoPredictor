from node import Node
class Trie:
    def __init__(self):
        self.root = Node(None)
        self.map = {
            '2':2, 'a' : 2, 'b' : 2, 'c' : 2,
            '3':3, 'd' : 3, 'e' : 3, 'f' : 3,
            '4':4, 'g' : 4, 'h' : 4, 'i' : 4,
            '5':5, 'j' : 5, 'k' : 5, 'l' : 5,
            '6':6, 'm' : 6, 'n' : 6, 'o' : 6,
            '7':7, 'p' : 7, 'q' : 7, 'r' : 7, 's' : 7,
            '8':8, 't' : 8, 'u' : 8, 'v' : 8,
            '9':9, 'w' : 9, 'x' : 9, 'y' : 9, 'z' : 9,
            '#' : 10
                }
    def findAll(self, target):
        target = target.lower()
        node = self.root
        for index, c in enumerate(target):
            node = node.children[self.map[c]]
            if node == None:
                return []
            if index == len(target) - 1:
                return self.getAllWords(node)

    def getAllWords(self, node):
        l = []
        stack = []
        visited = set()
        stack.append(node)
        while len(stack) > 0:
            node = stack.pop()
            visited.add(node)
            if node.word is not None:
                l.append(node.word)
            for n in node.children.keys():
                if node.children[n] != None and node.children[n] not in visited:
                    stack.append(node.children[n])
        return l

    def insert(self, word):
        if word is not None:
            word = word.lower()
        node = self.root
        for index, c in enumerate(word):
            if node.children[self.map[c]] == None:
                node.children[self.map[c]] = Node(None)
            if index == len(word) - 1:
                '''
                #can make code much faster and use less memory by using a list to store the words where they would usually be stored in the pound symbol, so 
                #cat is inserted and then bat but bat would be stored at b(2) a(2) t(8)'s list 
                #to use this version, uncomment out the line below and make node class's children[10] be an empty list
                node.children[self.map['#']].append(word)
                '''
                # this code is for the more memory wasting and slower version as specified in the assignment .pdf
                while node.word != None:
                    if node.children[self.map['#']] == None:
                        node.children[self.map['#']] = Node(None)
                        node = node.children[self.map['#']]
                        node.word = word
                        return
                    node = node.children[self.map['#']]
                node.word = word
                return
            node = node.children[self.map[c]]  
            
    def printTrie(self):
        l = self.getAllWords(self.root)
        print(l)
        print("number of words: " + str(len(l)))

    def addWords(self, textFile):
        file1 = open(textFile, "r") 
        for line in file1:
            self.insert(line.strip())     
        file1.close()
    
