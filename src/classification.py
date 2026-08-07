from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

mini_dataset = fetch_openml(name='mnist_784', as_frame=False)
some_digit = mini_dataset.data[112].reshape(28, 28)
plt.imshow(some_digit, cmap='gray')
plt.title('Some Digit from MNIST')
plt.show()

