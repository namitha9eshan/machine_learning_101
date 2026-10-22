#Batch Gradient descent 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.array([1.0, 2.0, 3.0 , 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
y = 2*x + 1 * np.random.randn(len(x))

def gradient_descent(x,y,w, b, lr, epochs = 1000):
    losses = []
    for epoch in range(epochs):
        y_pred = w * x + b 
        error = y - y_pred
        loss = np.mean((error)**2)
        losses.append(loss)
        wd = -2 * np.mean(x* error)
        wb = -2 * np.mean(error)
        w = w - lr * wd
        b = b - lr * wb
        if epoch % 50 == 0:
            print(f"epoch: {epoch} | w: {w:.2f} | b: {b:.2f} |  loss: {loss:.8f}")
    return w, b , losses 

w, b, loss = gradient_descent(x,y, 0.0, 0.0, 0.01, 1000)

plt.plot(loss)
plt.xlabel("epochs")
plt.ylabel('Loss')
plt.title("loss over time")
plt.show()

