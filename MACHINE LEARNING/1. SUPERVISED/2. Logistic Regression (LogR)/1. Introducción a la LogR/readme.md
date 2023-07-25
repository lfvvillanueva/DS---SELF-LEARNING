# 1. Introducción a la regresión logística

La regresión logística es una técnica estadística que se utiliza para predecir la probabilidad de que una variable categórica tome un valor determinado, basándose en una o más variables predictoras. Aunque comparte similitudes con la regresión lineal, su enfoque principal y las técnicas matemáticas subyacentes son distintas.

## Diferencias con la regresión lineal

### Regresión Lineal

La **regresión lineal** es una técnica que busca modelar la relación entre una variable dependiente continua y una o más variables independientes. Su objetivo es encontrar la mejor línea recta (en el caso bidimensional) que se ajuste a los datos.

**Ecuación de la regresión lineal:**
$$Y = \beta_0 + \beta_1X_1 + ... + \beta_pX_p + \epsilon \$$

Donde:
- $Y$ es la variable dependiente continua.
- $X_i$  son las variables predictoras.
- $\beta_i$  son los coeficientes.
- $\epsilon$  es el error aleatorio.

Esta técnica asume que la relación entre las variables es lineal y que los residuales (errores) tienen una distribución normal. Se utiliza principalmente cuando el objetivo es predecir un valor continuo.

### Regresión Logística

Por otro lado, la **regresión logística** se utiliza cuando la variable dependiente es categórica, en particular, cuando es binaria (por ejemplo, sí/no, 1/0, verdadero/falso). En lugar de predecir un valor continuo, busca predecir la probabilidad logarítmica de que una observación pertenezca a una de las categorías.

**Ecuación de la regresión logística:**
$$\log\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1X_1 + ... + \beta_pX_p$$

Donde:
- $p$ es la probabilidad de que la variable dependiente sea 1 (o éxito).
- $\log$ es el logaritmo natural.
- $X_i$ y $\beta_i$ tienen las mismas definiciones que en la regresión lineal.

El lado izquierdo, $\log\left(\frac{p}{1-p}\right)$, se conoce como logit. La regresión logística transforma su salida usando la función logit para mapear cualquier valor entre 0 y 1, lo que la hace adecuada para predecir probabilidades.

**Interpretación:**
En regresión logística, un coeficiente positivo para una variable predictora sugiere que, manteniendo constantes las demás variables, un incremento en esa predictora aumentará la probabilidad logarítmica de que la respuesta sea un "éxito" (o categoría 1), y viceversa.

### ¿Cuándo usar cuál?

- **Regresión lineal:** Utilice esta técnica cuando su objetivo sea predecir o explicar una variable dependiente **continua** basada en una o más variables independientes.

- **Regresión logística:** Utilice esta técnica cuando quiera predecir la **probabilidad** de que una observación pertenezca a una categoría específica basándose en una o más variables independientes.