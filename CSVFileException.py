class CSVFile():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        ListaDueElementi = []
        ListaDiListe = []
        file = open(self.name, 'r')
        for line in file:
            elements = line.split(',')
            if elements[0] != 'Date':
                data = elements[0]
                value = elements[1]
                ListaDueElementi = [data, value]
                ListaDiListe.append(ListaDueElementi)
        return ListaDiListe

var1 = CSVFile('sales')
var2 = var1.get_data()
print(var2)