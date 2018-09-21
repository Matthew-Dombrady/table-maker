class Table:

    def __init__(self, table_name, labels, symbol):
        self.name = table_name
        self.labels = labels
        self.symbol = symbol
        self.max_lengths = []

        for label in labels:
            self.max_lengths.append(len(label))

    

    def print(self):
        for label in self.labels:
            print(label + "  ", end="")
            self.__symbol__(1)
        print("\n")
        self.__symbol__((sum(self.max_lengths)) + (4 * len(self.labels)))
        

    def __symbol__(self, num):
        print(self.symbol * num + "  ", end="")

    
