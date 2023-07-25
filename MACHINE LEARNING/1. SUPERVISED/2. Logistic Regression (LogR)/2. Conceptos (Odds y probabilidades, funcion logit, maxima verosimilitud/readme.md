## 2. Conceptos básicos

## Odds y Probabilidades: Entendiendo la Incertidumbre

Cuando hablamos de eventos aleatorios, como lanzar una moneda, tirar un dado o predecir el resultado de un partido de fútbol, nos enfrentamos a la incertidumbre. Para cuantificar esta incertidumbre, utilizamos conceptos matemáticos como las probabilidades y las odds.

### Probabilidades

Las probabilidades representan la posibilidad de que ocurra un evento específico. En términos matemáticos, si tenemos un evento con probabilidad $p$, su valor se encuentra en el intervalo $[0, 1]$. Un valor de probabilidad de 0 indica que el evento nunca ocurrirá, mientras que un valor de probabilidad de 1 significa que el evento siempre ocurrirá.

Por ejemplo, si lanzamos una moneda justa, la probabilidad de obtener cara ($C$) es de $p(C) = 0.5$, ya que hay una mitad de posibilidades de que la moneda caiga en cara.

### Odds

Las odds son una forma alternativa de expresar las probabilidades y se representan como el cociente entre la probabilidad de que ocurra un evento y la probabilidad de que no ocurra. Si llamamos a la probabilidad del evento $p$, entonces las odds ($O$) están dadas por la fórmula:

$$ O = \frac{p}{1-p} $$

Para entender mejor las odds, podemos considerar el ejemplo de la moneda nuevamente. Si la probabilidad de obtener cara ($p(C)$) es de 0.5, entonces las odds de obtener cara son:

$$ O(C) = \frac{0.5}{1-0.5} = 1 $$

Una odds de 1 significa que la probabilidad de que ocurra el evento es igual a la probabilidad de que no ocurra, lo que es coherente, ya que en una moneda justa, ambas caras son igualmente probables.

### Diferencias entre Probabilidades y Odds

La principal diferencia entre probabilidades y odds radica en cómo se expresan y cómo interpretamos sus valores:

1. **Rango de Valores**: Las probabilidades varían entre 0 y 1, mientras que las odds varían entre 0 e infinito. Una probabilidad de 0 representa una certeza de que el evento no ocurrirá, mientras que una probabilidad de 1 indica una certeza de que el evento sí ocurrirá. Por otro lado, las odds pueden ser mayores que 1 y nos dicen cuántas veces un evento es más probable que no ocurra.

2. **Interpretación**: Cuando hablamos de probabilidades, podemos entenderlas como la proporción de veces que esperaríamos que ocurra un evento si repitiéramos la situación muchas veces. Por ejemplo, si lanzamos un dado justo, la probabilidad de obtener un 6 es de 1/6, lo que significa que, en promedio, obtendríamos un 6 una vez cada seis lanzamientos.

   En cambio, las odds nos dicen cuántas veces el evento es más probable que no ocurra. Si las odds son 2, entonces el evento es dos veces más probable que no ocurra. Si las odds son 5, entonces el evento es cinco veces más probable que no ocurra.

En resumen, tanto las probabilidades como las odds nos proporcionan información sobre la incertidumbre asociada a un evento. Las probabilidades se encuentran en el rango [0, 1] y se interpretan como la probabilidad real del evento, mientras que las odds son una medida relativa y van desde 0 hasta el infinito, indicando cuántas veces es más probable que ocurra o no ocurra el evento.

---

### Función logit

La **función logit** es el logaritmo natural de las odds. Es utilizada en regresión logística para transformar una variable dependiente binaria en una escala que va de \(-\infty\) a \(+\infty\).

**Ecuación:**
\[ \log(\text{Odds}) = \log \left( \frac{p}{1-p} \right) \]

**Diferencias:**
- Mientras que las odds representan la relación entre la probabilidad de que ocurra y no ocurra un evento, la función logit transforma esas odds a una escala continua y sin límites. 

**Interpretación:** 
Si el valor de la función logit es 0, las odds son de 1, lo que implica que \( p = 0.5 \). Valores positivos de la función logit indican probabilidades mayores a 0.5, y valores negativos indican probabilidades menores a 0.5.

---

### Máxima verosimilitud

El **método de máxima verosimilitud (MLE, por sus siglas en inglés)** estima los parámetros de un modelo estadístico. En el contexto de la regresión logística, MLE busca encontrar los coeficientes que maximizan la verosimilitud de observar las respuestas dadas en el conjunto de datos, considerando los predictores.

**Ecuación:**
La función de verosimilitud \( L(\beta) \) para la regresión logística es:
\[ L(\beta) = \prod_{i=1}^{n} p_{i}^{y_i} (1-p_{i})^{(1-y_i)} \]

Donde:
- \( n \) es el número de observaciones.
- \( y_i \) es la respuesta de la i-ésima observación.
- \( p_i \) es la probabilidad predicha para la i-ésima observación.

**Diferencias:**
- Mientras que otros métodos, como el de mínimos cuadrados, buscan minimizar la diferencia entre las observaciones y sus predicciones, MLE busca maximizar la probabilidad de observar los datos dados.

**Interpretación:** 
El método de máxima verosimilitud nos proporciona los coeficientes que son "más probables" dados los datos que tenemos. Estos coeficientes maximizan la probabilidad de observar nuestras respuestas reales con las probabilidades predichas por el modelo.

---

**Comparación entre regresión logística y regresión lineal:**

La **regresión lineal** se utiliza cuando la variable de respuesta es continua y tiene una distribución aproximadamente normal. La **regresión logística**, por otro lado, se emplea cuando la variable de respuesta es binaria (o categórica ordinal/multinomial). Mientras que la regresión lineal tiene como objetivo predecir un valor continuo, la regresión logística busca predecir la probabilidad de que una observación pertenezca a una categoría específica. Es esencial elegir el tipo de regresión basado en la naturaleza y distribución de la variable de respuesta. 

