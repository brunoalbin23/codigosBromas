# Codigos bromas
En este repositorio vamos a ver varios códigos sencillos para ejecutar y hacerle unas pequeñas bromas a nuestros amigos.
### 1 - Bucle de ventanas
Loop de ventanas de bloc de notas infinitos, 

Ejecución - Copiar o clonar el archivo "codigoVentana", abrir, guardar como ".bat" y cambiarle el nombre, la "victima" debe clickear el archivo.

>[!CAUTION]
>Para detenrlo, ctrl + c con la consola abierta como ventana principal, desde el administrador cerrar la consola o directamente reiniciar el pc.

### 2 - Respuesta Si o SI
Ventana con pregunta que se responde con si o no, si intenamos dar click sobre el "no" se moverá, haciendo que este sea imposible de clickear, "obligando" a la persona a dar en el boton de Si.

Ejecución - (Se necesita tener pyhton instalado) Clonar PreguntasSioSi y ejecutar para mas interesante, se puede hacer un ejecutable con los siguientes comandos en la consola:

```pip install pyinstaller```

```pyinstaller --onefile --windowed PreguntaSioSI.py```

Esto creará un ejecutable, obviamente se puede cambiar tanto la pregunta como el mensaje al responder "si", tambien recomiendo cambiar el nombre del archivo para que no sea obvio.
