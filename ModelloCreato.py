class Model()
     def fit(self, data):
     raise NotImplementedError('Metodo non implementato')
     def predict(self, data):
     raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model)
    def predict(self, data):
        lenght = len(data)
        somma_incr = None
        for i in a range (1, lenght):
            somma_incr = somma_incr + (data[i]-data[i-1])
        media_incr = somma_incr/lenght

        prediction = media_incr + data[lenght-1]  

        return prediction 