import numpy as np
from scipy import optimize

#X=np.array([[3,5],[5,1],[10,2]])
#y=np.array([[0.75],[0.82],[0.93]])
#NN=Neural_Network()
#T= trainer(NN)
#T.train(X,y)
#yHat=NN.forward(X)
#numgrad = computeNumericGradient(NN,X,y)
#grad = NN.computeGradients(X,y)
#norm(grad-numgrad)/norm(grad+numgrad)

class Neural_Network(object):
    def __init__(self):
        #Define Params
        self.inputLayerSize=2
        self.outputLayerSize=1
        self.hiddenLayerSize=3

        #weight params
        self.w1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.w2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

    def forward(self, X):
        #propogate inputs through network
        self.z2 = np.dot(X, self.w1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.w2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        #apply sigmoid function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))

    def sigmoidPrime(self, z):
        #derivative of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)

    def cost(self, X, y):
        #return np.power((y - yHat),2) - my attempt
        self.yHat = self.forward(X)
        J = 0.5*sum((y-self.yHat)**2)
        return J
        

    def costPrime(self, X, y):
        self.yHat = self.forward(X)
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)
        delta2 = np.dot(delta3, self.w2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)
        return dJdW1, dJdW2

    def getParams(self):
        params = np.concatenate((self.w1.ravel(), self.w2.ravel()))
        return params

    def setParams(self,params):
        w1_start = 0
        w1_end = self.hiddenLayerSize*self.inputLayerSize
        self.w1 = np.reshape(params[w1_start:w1_end], (self.inputLayerSize, self.hiddenLayerSize))
        w2_end = w1_end + (self.hiddenLayerSize * self.outputLayerSize)
        self.w2 = np.reshape(params[w1_end:w2_end], (self.hiddenLayerSize, self.outputLayerSize))

    def computeGradients(self, X, y):
        dJdW1, dJdW2 = self.costPrime(X,y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))

def computeNumericGradient(N, X, y):
    paramsInit = N.getParams()
    numgrad = np.zeros(paramsInit.shape)
    perturb = np.zeros(paramsInit.shape)
    e = 1e-4

    for p in range(len(paramsInit)):
        #set perturb vector
        perturb[p] = e
        N.setParams(paramsInit + perturb)
        loss2 = N.cost(X,y)

        N.setParams(paramsInit - perturb)
        loss1 = N.cost(X,y)

        #Compute Numerical Gradient
        numgrad[p] = (loss2-loss1) / (2*e)

        #return the value we changed back to zero
        perturb[p] = 0
    #return params to original value
    N.setParams(paramsInit)
    return numgrad



class trainer(object):
    def __init__(self, N):
        #Make local reference to NN
        self.N=N

    def costWrap(self, params, X, y):
        self.N.setParams(params)
        cost = self.N.cost(X,y)
        grad = self.N.computeGradients(X,y)
        return cost, grad

    def callbackF(self, params):
        self.N.setParams(params)
        self.J.append(self.N.cost(self.X,self.y))
        
    def train(self, X, y):
        self.X = X
        self.y = y
        self.J = []
        params0 = self.N.getParams()
        options = {'maxiter' : 200, 'disp' : True}
        _res = optimize.minimize(self.costWrap, params0, jac=True, method='BFGS',
                                 args = (X,y), options = options, callback=self.callbackF)
        self.N.setParams(_res.x)
        self.optimizationResults = _res










        

        
