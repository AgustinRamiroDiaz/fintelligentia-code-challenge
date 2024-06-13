# Primeros pensamientos

- voy a tener que conectarme por websocket
- tendré que darme maña para hacer el ruteo de ordenes por websocket, probablemente accediendo a alguna primitiva de la librería PyRofex. Sino puedo hacerlo, tendré que hacerlo más "manualmente" con algún otro paquete de Python que permita la conexión por websocket (sería más trabajo porque debería crear el protocolo de comunicación https://apihub.primary.com.ar/assets/docs/Primary-API.pdf)
- el escuchar las acciones debería fácil una vez que tengo la conexión
- estimar los precios futuros con carry trade y TNA no debería ser complicado, creo que Pandas me va a ayudar mucho con esto
- no especifica input y output. Voy a optar por una CLI que reciba parámetros de configuración y que después imprima todo por consola. En una app productiva agregaríamos healthchecks, logs estructurados, etc.
