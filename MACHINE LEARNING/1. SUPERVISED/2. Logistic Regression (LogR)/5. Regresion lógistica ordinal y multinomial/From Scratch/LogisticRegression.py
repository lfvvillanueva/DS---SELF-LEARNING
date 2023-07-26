# Importando la librería numpy para cálculos matriciales y otras operaciones matemáticas.
import numpy as np

# Función sigmoidal, que es la función de activación utilizada en regresión logística.
# Convierte cualquier número real en un valor entre 0 y 1.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Creando la clase LogisticRegression.
class LogisticRegression():
    # Constructor de la clase, se inicializan los hiperparámetros y las variables de instancia.
    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr             # Tasa de aprendizaje para el algoritmo de optimización.
        self.n_iters = n_iters   # Número de iteraciones para el algoritmo de optimización.
        self.weights = None     # Pesos del modelo, se inicializarán más tarde.
        self.bias = None        # Término de sesgo, también se inicializará más tarde.

    # Método para entrenar el modelo.
    def fit(self, X, y):
        # Obteniendo el número de muestras y características.
        n_samples, n_features = X.shape
        # Inicializando los pesos y el sesgo a cero.
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Bucle para iterar y optimizar los pesos usando el algoritmo del descenso del gradiente.
        for _ in range(self.n_iters):
            # Obteniendo las predicciones lineales del modelo.
            linear_pred = np.dot(X, self.weights) + self.bias
            # Aplicando la función sigmoidal para obtener probabilidades.
            predictions = sigmoid(linear_pred)

            # Calculando el gradiente de los pesos y el sesgo.
            dw = (1 / n_samples) * np.dot(X.T, (predictions - y))
            db = (1 / n_samples) * np.sum(predictions - y)

            # Actualizando los pesos y el sesgo en dirección opuesta al gradiente.
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    # Método para predecir las clases de nuevas muestras.
    def predict(self, X):
        # Obteniendo las predicciones lineales del modelo.
        linear_pred = np.dot(X, self.weights) + self.bias
        # Aplicando la función sigmoidal para obtener probabilidades.
        y_pred = sigmoid(linear_pred)
        # Clasificando las probabilidades en 0 o 1 basado en un umbral de 0.5.
        class_pred = [0 if y <= 0.5 else 1 for y in y_pred]
        return class_pred
    
#From: https://github.com/AssemblyAI-Examples/Machine-Learning-From-Scratch
#Video: 
