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
