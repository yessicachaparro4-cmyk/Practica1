## Parte 3. Operaciones

```javascript
let suma = numero1 + numero2;
let resta = numero1 - numero2;
let multiplicacion = numero1 * numero2;
let division = numero1 / numero2;
```

## Parte 4. Pruebas

| Prueba | Número 1 | Número 2 | Suma | Resta | Multiplicación | División |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 2 | 12 | 8 | 20 | 5 |
| 2 | 7 | 3 | 10 | 4 | 21 | 2.3333333333333335 |
| 3 | 5.5 | 2 | 7.5 | 3.5 | 11 | 2.75 |

## Registro de un error

**Error:** Al principio la suma podía unir los valores como texto en lugar de sumarlos.

**Solución:** Usé `Number()` alrededor de cada `prompt()` para convertir las entradas a números.

## Reflexión final

### ¿Qué parte del laboratorio fue más sencilla?

Realizar las operaciones de suma, resta, multiplicación y división.

### ¿Qué diferencia observaste entre 25 y "25"?

25 es un número, mientras que "25" es texto porque está entre comillas.

### ¿Por qué fue necesario utilizar Number()?

Porque `prompt()` recibe la información como texto y `Number()` la convierte en número para poder realizar correctamente las operaciones matemáticas.

### ¿Qué cambio agregarías a tu calculadora?

Agregaría una validación para evitar dividir entre cero y mostrar un mensaje de error.

## Archivo principal

El programa se encuentra en el archivo `calculadora.js`.

## Evidencia

Se incluye una captura de la consola mostrando una prueba de la calculadora en funcionamiento.

## Archivos del proyecto

```text
README.md
calculadora.js
evidencia-calculadora.png
```
