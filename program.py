from trie import Trie 

def main():
    t = Trie()
    t.addWords('dict.txt')
    print("words currently in trie: ")
    t.printTrie()
    userInput = input("Enter a sequence to autopredict:\n")
    while userInput != 'quit':
        if userInput == None or userInput == '':
            print('empty string detected')
        else:
            l = t.findAll(userInput)
            if l == []:
                print("couldn't find sequence")
            else:
                l.sort()
                print(l)
        userInput = input("Enter a sequence to autopredict:\n")
main()
