from keras.layers import Dense,Activation,LeakyReLU
from keras.models import Sequential

class DNN:
    def __init__(self,classes): # Classes will be Provided on the Run time... i.e 5
        print('\n Training Started .... \n')
        self.model=Sequential()
        self.classes=classes
        
    def create(self):
        
        self.model.add(Dense(128,input_dim=128))
        self.model.add(LeakyReLU(alpha=0.1))
        
        self.model.add(Dense(64))
        self.model.add(LeakyReLU(alpha=0.1))
        
        self.model.add(Dense(32))
        self.model.add(LeakyReLU(alpha=0.1))
        
        self.model.add(Dense(16))
        self.model.add(LeakyReLU(alpha=0.1))
        
        self.model.add(Dense(self.classes))
        
        self.model.add(Activation('softmax'))
        

        return self.model
