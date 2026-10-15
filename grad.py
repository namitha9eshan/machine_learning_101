#Gradient Descent : batch gradient descent
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0])
y = np.array([0, 0, 0, 1, 0, 1, 1, 1])

def gradient_descent(x, y, w, b, lr, epochs = 1000):
    for i in range(iter):
        y_pred = x * w + b     
        cost = np.mean((y-y_pred)**2)
        wd = -2* np.mean(x * (y-y_pred))
        bd = -2* np.mean(y-y_pred)
        w = w - lr*wd
        b = b - lr*bd
        print(f"w : {w: .2f},  b : {b: .2f}, epochs : {i} , loss : {cost} ")


gradient_descent(x,y,0,0,0.001,1500)





