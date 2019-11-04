class Node:
    def __init__(self, word):
        self.word = None
        if word is not None:
            self.word = word.lower()
        self.children = {
                2 : None, 3: None, 4: None, 5: None,
                6 : None, 7: None, 8: None, 9: None,
                10 : None 
                }
