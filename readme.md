# Fintelligentia Code Challenge

## Enunciado del problema

```
CHALLENGE CODE FINTELLIGENTIA:

Objetivo:

Conectarse al ambiente de test de MATba/Rofex a traves de WebSocket, recibir market data de los assets detallados y cotizar precios según la siguiente lógica.

Utilizar la libreria PyRofex para conectarse al mkt, la misma tiene la opción de escuchar MD por WS pero solo enviar ordenes por Rest. Hacer las modificaciones necesarias para que el ruteo de ordenes también sea por WS.
Escuchar la MD de las acciones GGAL e YPD.
Calcular los precios teóricos de los futuros de Galicia e YPF con vencimiento JUNIO 2024 siguiendo una lógica de Carry trade con TNA.
Cotizar bid y ask de ambos activos segun la lógica anterior.

Compartir el proyecto en Github al usuario levilucchini@gmail.com
```

## Solución

Para ejecutar el código, primero hay que instalar las dependencias:

```sh
pip install -r requirements.txt
```

Luego configurar las credenciales de MATba/Rofex. Se puede hacer en un archivo `.env` como se ve en el archivo `.env.example`, o sino mediante variables de entorno.

Luego, se puede ejecutar el código con:

```sh
python main.py
```

### Conexión al ambiente de test de MATba/Rofex a través de WebSocket

Hecho en el archivo `main.py`.

### Crear ruteo de órdenes por WS

Leyendo en detalle el código de la librería `pyRofex` encontré que la clase `WebSocketClient` tiene un método llamado [`send_order`](https://github.com/matbarofex/pyRofex/blob/bb03a096e3d9f830486f7ce619c6c70e0889e8fe/src/pyRofex/clients/websocket_rfx.py#L292) que envía una orden por el mismo canal de websocket que utiliza para el resto de las operaciones. La orden tiene el formato de [`SEND_ORDER`](https://github.com/matbarofex/pyRofex/blob/bb03a096e3d9f830486f7ce619c6c70e0889e8fe/src/pyRofex/components/messages.py#L17), el cual es el mismo formato documentado en la [API de Primary](https://apihub.primary.com.ar/assets/docs/Primary-API.pdf) oficial de MATba/Rofex.

La funcionalidad está expuesta a través de [`send_order_via_websocket`](https://github.com/matbarofex/pyRofex/blob/bb03a096e3d9f830486f7ce619c6c70e0889e8fe/src/pyRofex/service.py#L810), y en mis tests parece funcionar correctamente para el envío de órdenes por websocket.

Por lo tanto, no es necesario hacer ninguna modificación a la librería `pyRofex` para poder enviar órdenes por websocket. Además, la funcionalidad existe desde [agosto del 2022](https://github.com/matbarofex/pyRofex/commit/b981c42b2f531d2032f2d474e80b6f81b61d95f5) y hay [un ejemplo](https://github.com/matbarofex/pyRofex/blob/master/samples/6_websocket_order_routing.py), por lo cual infiero que este enunciado era una trampa para ver si el postulante se tomaba el tiempo de averiguar e investigar.

### Escuchar la MD de las acciones GGAL e YPD

Hecho en el archivo `main.py`.

### Calcular los precios teóricos de los futuros de Galicia e YPF con vencimiento JUNIO 2024 siguiendo una lógica de Carry trade con TNA

TODO

### Cotizar bid y ask de ambos activos según la lógica anterior

TODO

## Notas

No llegué a concretar la parte algorítmica de este desafío. El poco tiempo que le pude dedicar lo invertí todo en explorar el problema y la librería `pyRofex`. Actualmente (sábado a la noche víspera de día del padre) estoy escribiendo este README para documentar mis pensamientos y el camino que seguiría si tuviera más tiempo.

Investigué un poco sobre carry trade y TNA:

- entiendo que TNA es la tasa nominal anual
- entiendo que carry trade es una estrategia de inversión que consiste en tomar prestado en una moneda con una tasa de interés baja y prestar en una moneda con una tasa de interés alta
- me queda la duda de a qué se refiere el "precio del futuro", ya que entiendo que el futuro no tiene un precio sino los precios de bid y ask y sus respectivas cantidades. Supongo que se refiere a calcular el precio de un futuro en base a la tasa de interés y el precio spot.

En cuanto a la implementación, creo que la mejor forma de hacerlo sería:

- obtener los precios spot (bid y ask) de GGAL y YPF
- obtener la tasa de interés de la TNA
  - no sé si se puede obtener de la API de MATba/Rofex, aparece la columna en https://mtr.primary.ventures/futuros/financieros pero está vacía
- crear una función `futuro_predictor` que pueda predecir el precio de un futuro en base a la tasa de interés y el precio spot llamada
  - agregaría tests unitarios para corroborar el comportamiento de la función
  - entiendo que la función es stateless, por lo cual no necesitaría un objeto para encapsularla. En algún momento pensé que el algoritmo de carry trade podría necesitar múltiples datos de bid y ask para calcular el precio futuro, y en ese caso lo hubiera encapsulado en una clase.
