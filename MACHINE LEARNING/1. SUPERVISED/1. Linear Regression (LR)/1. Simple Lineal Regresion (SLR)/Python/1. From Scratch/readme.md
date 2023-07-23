## Regresión Lineal Simple

### 1. Formulación del Modelo

La regresión lineal simple es uno de los métodos más básicos y comúnmente utilizados en estadísticas para modelar la relación entre dos variables cuantitativas. La idea es ajustar una línea recta a un conjunto de datos de tal manera que se minimize la distancia (generalmente medida como el cuadrado de la distancia) entre la línea y los puntos de datos.

#### Ecuación del Modelo:
$$ y = \beta_0 + \beta_1x + \epsilon $$
Donde:
- $ y $: Variable dependiente
- $ x $: Variable independiente
- $ \beta_0 $ y $ \beta_1 $: Coeficientes
- $ \epsilon $: Error

#### Cálculos Uno a Uno:
$$ \beta_1 = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2} $$
$$ \beta_0 = \bar{y} - \beta_1\bar{x} $$

#### Cálculos Matriciales:
$$ \beta = (X^TX)^{-1}X^Ty $$

### 2. Funciones de Pérdida

La función de pérdida nos ayuda a medir cuán bien se ajusta nuestro modelo a los datos. En el contexto de la regresión lineal, generalmente empleamos el error cuadrático medio (MSE).

#### Error Cuadrático Medio (MSE):
$$ MSE = \frac{1}{n} \sum (y_i - \hat{y}_i)^2 $$

#### Cálculos Uno a Uno:
Diferencia entre el valor observado y el valor predicho, cuadrado y promediado.

#### Cálculos Matriciales:
$$ MSE = \frac{1}{n} (y - X\beta)^T(y - X\beta) $$

### 4. Pruebas y Diagnóstico

#### Coeficiente de determinación (R^2)
El coeficiente $ R^2 $ mide la proporción de la variabilidad en $ y $ que puede ser explicada por $ x $. 
$$ R^2 = 1 - \frac{SS_{res}}{SS_{tot}} $$
Cálculos Matriciales:
$$ R^2 = 1 - \frac{(y - X\beta)^T(y - X\beta)}{(y - \bar{y})^T(y - \bar{y})} $$

#### Prueba F
La prueba F compara la varianza explicada por el modelo con la varianza residual. 
$$ F = \frac{(SS_{tot} - SS_{res})/p}{SS_{res}/(n-p-1)} $$

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

### Conclusión

La regresión lineal simple es una herramienta fundamental en estadística y análisis de datos. Es esencial entender sus supuestos y limitaciones para interpretar adecuadamente sus resultados.
