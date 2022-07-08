class View:
    def __init__(self):
        pass

    def inputSignal(self):
        return input("바꾸고 싶은 문자열을 입력하세요! ")


class ViewModel:
    def __init__(self, view, model):
        self.view = view
        self.model = model
    
    def changeData(self):
        changed_String = self.view.inputSignal()
        self.model.dataIn(changed_String)
        
        model_String = self.model.dataOut()
        self.printString(model_String)

    def printString(self, string):
        print("String: {string}".format(string=string))


class Model:
    def __init__(self):
        self.data = "Test String"
    
    def dataOut(self):
        return self.data

    def dataIn(self, data):
        self.data = data


if __name__=='__main__':
    testView = View()
    testModel = Model()
    testViewModel = ViewModel(testView, testModel)
    while(True):
        testViewModel.changeData()