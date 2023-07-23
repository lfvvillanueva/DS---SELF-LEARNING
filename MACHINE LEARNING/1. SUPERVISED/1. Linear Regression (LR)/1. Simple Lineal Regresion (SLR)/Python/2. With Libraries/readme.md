## Regresión Lineal Simple

### 1. Formulación del Modelo

La regresión lineal simple es uno de los métodos más básicos y comúnmente utilizados en estadísticas para modelar la relación entre dos variables cuantitativas. La idea es ajustar una línea recta a un conjunto de datos de tal manera que se minimize la distancia (generalmente medida como el cuadrado de la distancia) entre la línea y los puntos de datos.

#### Ecuación del Modelo:

$$ y = \beta_0 + \beta_1x + \epsilon $$
Donde:

- $y$: Variable dependiente
- $x$: Variable independiente
- $\beta_0$ y $\beta_1$: Coeficientes
- $\epsilon$: Error

#### Cálculos Uno a Uno:

$$ \beta_1 = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2} $$
$$ \beta_0 = \bar{y} - \beta_1\bar{x} $$

#### Cálculos Matriciales:

$$ \beta = (X^TX)^{-1}X^Ty $$

### 2. Funciones de Pérdida

La función de pérdida nos ayuda a medir cuán bien se ajusta nuestro modelo a los datos. En el contexto de la regresión lineal, generalmente empleamos el error cuadrático medio (MSE).

#### Error Cuadrático Medio (MSE):

$$ MSE = \frac{1}{n} \sum (y_i - \hat{y}\_i)^2 $$

#### Cálculos Uno a Uno:

Diferencia entre el valor observado y el valor predicho, cuadrado y promediado.

#### Cálculos Matriciales:

$$ MSE = \frac{1}{n} (y - X\beta)^T(y - X\beta) $$

### 4. Pruebas y Diagnóstico

#### Coeficiente de determinación (R^2)

El coeficiente $ R^2 $ mide la proporción de la variabilidad en $ y $ que puede ser explicada por $ x $. 
$$ R^2 = 1 - \frac{SS*{res}}{SS*{tot}} $$
Cálculos Matriciales:
$$ R^2 = 1 - \frac{(y - X\beta)^T(y - X\beta)}{(y - \bar{y})^T(y - \bar{y})} $$

#### Prueba F

La prueba F compara la varianza explicada por el modelo con la varianza residual.
$$ F = \frac{(SS*{tot} - SS*{res})/p}{SS\_{res}/(n-p-1)} $$

#### Prueba t para $ \beta_1 $

La prueba t evalúa si la pendiente de la línea de regresión es significativamente diferente de cero.
$$ t = \frac{\beta_1 - 0}{SE(\beta_1)} $$

### 5. Supuestos

- **Linearidad:** Relación entre $ x $ y $ y $ debe ser lineal.
- **Independencia:** Las observaciones deben ser independientes.
- **Homocedasticidad:** Varianza de errores constante.
- **Normalidad:** Errores distribuidos normalmente.

### 6. Violaciones y Soluciones

- **No linealidad:** Transformaciones o modelos no lineales.
- **Heterocedasticidad:** Modelos robustos o transformaciones.
- **No normalidad:** Transformaciones como logaritmos.

### 7. Aplicaciones Adecuadas y Limitaciones

**Aplicaciones Adecuadas:** Examinar relaciones lineales, estimar tendencias y hacer proyecciones.
**Limitaciones:** Relaciones lineales, sensibilidad a outliers y supuestos.

### 8. Resumen de las formas funcionales en las que se emplean logaritmos en las regresiones

Los logaritmos son herramientas matemáticas que transforman series de números de manera que las relaciones multiplicativas entre los números originales se conviertan en relaciones aditivas entre sus logaritmos. En el ámbito de la econometría y la estadística, las transformaciones logarítmicas se utilizan ampliamente en regresiones para linearizar relaciones, estabilizar varianzas y modelar multiplicatividades. A continuación, te presento un resumen detallado de las formas funcionales más comunes en las que se emplean logaritmos en las regresiones:

1. **Modelo Lineal-Logarítmico (semi-logarítmico)**

   - **Ecuación**: $$y = \beta_0 + \beta_1 \log(x) + \epsilon$$
   - **Interpretación**: Un incremento porcentual en $x$ se asocia con un cambio de $\beta_1$ unidades en $y$. Es decir, si $x$ aumenta en un 1%, $y$ cambia en $0.01 \times \beta_1$ unidades.
   - **Aplicaciones**: Comúnmente usado cuando se espera que los cambios porcentuales en la variable independiente $x$ tengan un impacto constante en la variable dependiente $y$.

2. **Modelo Logarítmico-Lineal**

   - **Ecuación**: $$\log(y) = \beta_0 + \beta_1 x + \epsilon$$
   - **Interpretación**: Un incremento de una unidad en $x$ se relaciona con un cambio porcentual de $\beta_1$ en $y$.
   - **Aplicaciones**: Útil cuando un incremento unitario en $x$ se espera que tenga un efecto porcentual constante en $y$.

3. **Modelo Logarítmico-Logarítmico (log-log)**

   - **Ecuación**: $$\log(y) = \beta_0 + \beta_1 \log(x) + \epsilon$$
   - **Interpretación**: Un incremento porcentual en $x$ se asocia con un cambio porcentual de $\beta_1$ en $y$. Es decir, si $x$ aumenta en un 1%, $y$ cambia en un $\beta_1 \%$.
   - **Aplicaciones**: Este modelo es ampliamente utilizado para estimar elasticidades, por ejemplo, en economía cuando se busca medir la reacción porcentual de una variable frente a cambios porcentuales en otra (como la elasticidad precio-demanda).

4. **Beneficios de las transformaciones logarítmicas**:

   - **Linearización de relaciones**: Las transformaciones logarítmicas pueden ayudar a convertir relaciones no lineales en relaciones aproximadamente lineales, lo que facilita el análisis usando regresión lineal.
   - **Estabilización de varianzas**: En muchos casos, la varianza de la variable dependiente puede aumentar o disminuir con el nivel de la misma. Transformar la variable dependiente con un logaritmo puede estabilizar esta varianza.
   - **Interpretaciones multiplicativas o porcentuales**: Como se mencionó anteriormente, los modelos log-transformados permiten interpretaciones en términos de cambios porcentuales, lo que puede ser más intuitivo y útil en ciertas aplicaciones, especialmente en economía.

5. **Consideraciones**:
   - **Dominio**: Es importante recordar que el logaritmo de un número negativo o cero no está definido. Por lo tanto, antes de aplicar transformaciones logarítmicas, es esencial asegurarse de que todas las observaciones de la variable a transformar sean estrictamente positivas.
   - **Elección de la base**: El logaritmo natural (base $e$) es el más común en econometría, pero otros logaritmos, como el logaritmo base 10, también pueden usarse. La elección de la base afectará el valor numérico de los coeficientes, pero no la interpretación general de los resultados.

En resumen, las transformaciones logarítmicas en regresiones ofrecen una herramienta valiosa para modelar y analizar relaciones entre variables, especialmente cuando se buscan interpretaciones porcentuales o cuando la relación original no es lineal.

| Modelo                          | Ecuación                       | Interpretación                                                                                           | Aplicaciones                                                                                 |
|---------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Lineal-Logarítmico (semi-logarítmico) | $y = \beta_0 + \beta_1 \log(x) + \epsilon$ | Un incremento porcentual en $x$ se asocia con un cambio de $\beta_1$ unidades en $y$. Es decir, si $x$ aumenta en un 1%, $y$ cambia en $0.01 \times \beta_1$ unidades. | Comúnmente usado cuando se espera que los cambios porcentuales en la variable independiente $x$ tengan un impacto constante en la variable dependiente $y$. |
| Logarítmico-Lineal               | $\log(y) = \beta_0 + \beta_1 x + \epsilon$ | Un incremento de una unidad en $x$ se relaciona con un cambio porcentual de $\beta_1$ en $y$.       | Útil cuando un incremento unitario en $x$ se espera que tenga un efecto porcentual constante en $y$.   |
| Logarítmico-Logarítmico (log-log)   | $\log(y) = \beta_0 + \beta_1 \log(x) + \epsilon$ | Un incremento porcentual en $x$ se asocia con un cambio porcentual de $\beta_1$ en $y$. Es decir, si $x$ aumenta en un 1%, $y$ cambia en un $\beta_1 \%$       | Ampliamente utilizado para estimar elasticidades, especialmente en economía.                |


### Conclusión

La regresión lineal simple es una herramienta fundamental en estadística y análisis de datos. Es esencial entender sus supuestos y limitaciones para interpretar adecuadamente sus resultados.
