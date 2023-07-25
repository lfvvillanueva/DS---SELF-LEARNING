# Decision Trees (DT)

## Introducción

Los Árboles de Decisión son una herramienta poderosa y popular para clasificación y regresión. Dividen el espacio de características en regiones. Para tomar una decisión sobre una observación, se revisa en qué región del espacio cae y se asigna la salida de dicha región.

## Conceptos básicos

### Nodo

Un nodo representa una característica o atributo en el conjunto de datos que se utiliza para dividir los datos en subconjuntos más pequeños. Los árboles de decisión constan de:
- **Nodo raíz**: El nodo que divide primero el conjunto de datos.
- **Nodos de decisión**: Nodos que llevan a otros nodos.
- **Nodos hoja**: Nodos que representan una decisión/clasificación.

### División

Es el proceso de dividir un nodo en dos o más sub-nodos.

### Poda

La eliminación de subnodos de un nodo. Puede ayudar a reducir la complejidad del árbol y evitar el sobreajuste.

## Medidas de selección de nodos

El algoritmo selecciona la característica de división basada en una medida. Las medidas más populares son:

### Ganancia de información

$$
\text{Ganancia}(S, A) = \text{Entropía}(S) - \sum_{v \in \text{Valores}(A)} \left( \frac{|S_v|}{|S|} \times \text{Entropía}(S_v) \right)
$$

Donde:
- $S$ es el conjunto actual de ejemplos.
- $A$ es el atributo o característica.
- $\text{Valores}(A)$ son todos los posibles valores de $A$.
- $S_v$ son los ejemplos de $S$ donde $A$ tiene el valor $v$.

Entropía:

$$
\text{Entropía}(S) = -p_+ \log_2(p_+) - p_- \log_2(p_-)
$$

Donde $p_+$ y $p_-$ son las proporciones de ejemplos positivos y negativos en $S$, respectivamente.

### Índice Gini

$$
\text{Gini}(S) = 1 - \sum_{i=1}^{c} p_i^2
$$

Donde $p_i$ es la proporción de ejemplos que pertenecen a la clase $i$ y $c$ es el número total de clases.

### Reducción de Varianza (para árboles de regresión)

$$
\text{Varianza}(S) = \frac{1}{|S|} \sum_{i \in S} (x_i - \bar{x})^2
$$

Donde $x_i$ es el valor de la i-ésima observación y $\bar{x}$ es la media de las observaciones.

## Construcción

Los árboles de decisión se construyen de manera recursiva:
1. Comienza con el conjunto completo de ejemplos.
2. Si todos los ejemplos tienen la misma clasificación, retorna un nodo hoja con esa clasificación.
3. Si no, selecciona la mejor característica para dividir los datos.
4. Divide el conjunto en subconjuntos basados en la característica seleccionada.
5. Repite el proceso para cada subconjunto.

## Ventajas y desventajas

**Ventajas**:
- Fáciles de entender y visualizar.
- Pueden manejar datos no lineales.
- Requieren menos preprocesamiento de datos (p. ej., normalización).

**Desventajas**:
- Sensibles a ruido.
- Pueden sobreajustar fácilmente.

## Ejemplo en Python

Vamos a usar el famoso conjunto de datos `Iris` y la biblioteca `scikit-learn`.

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar datos
iris = load_iris()
X = iris.data
y = iris.target

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un árbol de decisión
clf = DecisionTreeClassifier(criterion='entropy')  # Usamos entropía, pero puedes cambiar a 'gini'
clf.fit(X_train, y_train)

# Predecir y calcular precisión
y_pred = clf.predict(X_test)
print(accuracy_score(y_test, y_pred))
```

Este es un ejemplo básico. En la práctica, es posible que desees ajustar más hiperparámetros, usar validación cruzada, y visualizar el árbol con herramientas como `Graphviz`.