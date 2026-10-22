import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.array([1.0, 2.0, 3.0 , 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
y = 2 * x + 1 * np.random.randn(len(x))

def gradient_descent(x, y, w, b, lr, epochs):
    losses = []
    for epoch in range(epochs):
        y_pred = x * w + b 
        error = y - y_pred
        loss = np.mean((error)**2)
        dw = -2 * np.mean(x* error)
        db = -2 * np.mean(error)
        w = w - lr * dw
        b = b - lr * db
        losses.append(loss)
        if epoch % 50 == 0:
            print(f"epoch: {epoch} | w: {w:.2f} | b: {b:.2f} | loss: {loss:.8f}")
    return w, b, losses


w, b, looses = gradient_descent(x,y, 0.0, 0.0, 0.01, 1000)

#plotting

plt.plot(looses)
plt.xlabel("epochs")
plt.ylabel("loss")
plt.title("Loss over time")
plt.show()














