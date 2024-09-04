import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def sigmoid(z):
    return 1/(np.exp(-z))

def relu(z):
    return np.maximum(0,z)

def sigmoid_derivative(z):
    s = sigmoid(z)
    return s * (1 - s)

def relu_derivative(z):
    return np.where(z > 0, 1, 0)

def forward_pass(X,weights,biases,activations,Y):
    pre_acts = [None,]
    acts = [X]
    for i in range(len(weights)):
        pre_act = acts[-1] @ weights[i].T + biases[i].T
        # print("Pre-Act",pre_act)
        pre_acts.append(pre_act)
        if activations[i]=='sigmoid':
            act = sigmoid(pre_act)
        elif activations[i]=='relu':
            act = relu(pre_act)
        elif activations[i]=='linear':
            act = pre_act
        # print("Act",act)
        acts.append(act)
    E = (acts[-1] - Y.reshape((X.shape[0],1)))
    return pre_acts,acts,E

def back_prop(X,pre_acts,acts,weights,biases,activations,E):
    w_grads = [np.zeros_like(w) for w in weights]
    b_grads = [np.zeros_like(b) for b in biases]
    L_grad_a_2 = E
    L_grad_z_2 = L_grad_a_2

    L_grad_w_2 = L_grad_z_2.T @ acts[1] / X.shape[0]
    L_grad_b_2 = np.sum(L_grad_z_2,axis=0,keepdims=True).T/X.shape[0]

    w_grads[1] = L_grad_w_2
    b_grads[1] = L_grad_b_2

    if activations[0] == 'sigmoid':
        L_grad_a_1 = (L_grad_z_2 @ weights[1]) * sigmoid_derivative(pre_acts[1])
    elif activations[0] == 'relu':
        L_grad_a_1 = (L_grad_z_2 @ weights[1]) * relu_derivative(pre_acts[1])
    elif activations[0] == 'linear':
        L_grad_a_1 = L_grad_z_2 @ weights[1]

    L_grad_z_1 = L_grad_a_1 

    L_grad_w_1 = L_grad_z_1.T @ acts[0] / X.shape[0]
    L_grad_b_1 = np.sum(L_grad_z_1, axis=0, keepdims=True).T / X.shape[0]

    w_grads[0] = L_grad_w_1
    b_grads[0] = L_grad_b_1

    return w_grads, b_grads

def back_prop(X, pre_acts, acts, weights, biases, activations, E):
    w_grads = [np.zeros_like(w) for w in weights]
    b_grads = [np.zeros_like(b) for b in biases]
    
    L_grad_a = E
    L_grad_z = L_grad_a 
    
    L_grad_w = L_grad_z.T @ acts[-2] / X.shape[0]
    L_grad_b = np.sum(L_grad_z, axis=0, keepdims=True).T / X.shape[0]
    
    w_grads[-1] = L_grad_w
    b_grads[-1] = L_grad_b

    for i in reversed(range(len(weights) - 1)):
        if activations[i] == 'sigmoid':
            L_grad_a = (L_grad_z @ weights[i + 1]) * sigmoid_derivative(pre_acts[i + 1])
        elif activations[i] == 'relu':
            L_grad_a = (L_grad_z @ weights[i + 1]) * relu_derivative(pre_acts[i + 1])
        elif activations[i] == 'linear':
            L_grad_a = L_grad_z @ weights[i + 1]

        L_grad_z = L_grad_a
        
        L_grad_w = L_grad_z.T @ acts[i] / X.shape[0]
        L_grad_b = np.sum(L_grad_z, axis=0, keepdims=True).T / X.shape[0]

        w_grads[i] = L_grad_w
        b_grads[i] = L_grad_b
    
    return w_grads, b_grads



alpha = 0.001
np.random.seed(40)
X = np.random.randint(0,15,(1000,2))
Y = np.sum(4*X + np.random.rand(),axis=1)
W1 = np.random.rand(8,2)*0.001
W2 = np.random.rand(1,8)*0.001

b1 = np.zeros(8).reshape((8,1))
b2 = np.zeros(1).reshape((1,1))
X_train,y_train,X_test,y_test = X[:500],Y[:500],X[500:],Y[500:]
weights = [W1,W2]
biases = [b1,b2]
pre_acts = []
acts = []
w_grads = []
b_grads = []
for _ in range(1000):
    pre_acts,acts,E = forward_pass(X_train,weights,biases,['relu','linear'],y_train)
    w_grads,b_grads = back_prop(X_train,pre_acts,acts,weights,biases,['relu','linear'],E)
    for i in range(len(weights)):
        weights[i] = weights[i] - alpha*w_grads[i]
        biases[i] = biases[i] - alpha*b_grads[i]
    
    if _%100 == 0:
        print("Train Error :",(1/1000)*np.sum(E**2))
        _,_,E = forward_pass(X_test,weights,biases,['relu','linear'],y_test)
        print("Test Error :",(1/1000)*np.sum(E**2))    
