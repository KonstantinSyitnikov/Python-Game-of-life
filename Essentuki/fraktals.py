import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(width, height, max_iter):
    x = np.linspace(-2.0, 1.0, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = c
    fractal = np.ones(c.shape)

    for i in range(max_iter):
        z = z**2 + c
        mask = (np.abs(z) > 2) & (fractal == 1)
        fractal[mask] = i
        z[mask] = 2

    return fractal / max_iter

width = 800
height = 600
max_iter = 100
fractal = mandelbrot(width, height, max_iter)

plt.imshow(fractal, cmap='magma', interpolation='nearest', extent=(-2, 1, -1.5, 1.5))
plt.show()