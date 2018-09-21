class Table:

    def __init__(self, table_name, labels, symbol):
        self.name = table_name
        self.labels = labels
        self.symbol = symbol
        self.max_lengths = []

        for label in labels:
            self.max_lengths.append(len(label))

    

    def print(self):
        print(self.name)

    
