class Table:

    def __init__(self, table_name, labels, symbol):
        self.name = table_name
        self.labels = labels
        self.symbol = symbol
        self.max_lengths = []
        self.data = []

        for label in labels:
            self.max_lengths.append(len(label))

    

    def print(self):
        for i in range(len(self.labels)):
            print(self.labels[i] + "  " + " "*(self.max_lengths[i]-len(self.labels[i])), end="")
            self.__symbol__(1)
        print("\n")
        self.__symbol__((sum(self.max_lengths)) + (4 * len(self.labels)) + 2)
        print("\n")
        
        for entry in self.data:
            for i in range(len(entry)):
                print(entry[i] +"  "+" "*(self.max_lengths[i]-len(entry[i])), end="")
                self.__symbol__(1)
            print("\n")

    def addEntry(self, x):
        self.data.append(x)

        for i in range(len(x)):
            if(len(x[i]) > self.max_lengths[i]):
                self.max_lengths[i] = len(x[i])

    def addEntries(self, x):
        for entry in x:
            self.addEntry(entry)
        

    def __symbol__(self, num):
        print(self.symbol * num + "  ", end="")


    
