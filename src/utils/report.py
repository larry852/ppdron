import time

TARGET_ESSID = None
TARGET_KEY = None
TARGET_CHANNEL = None
TARGET_PRIVACY = None
TARGET_ATTACK = None
recomendations = [
'Uso de contraseñas robustas, se debe evitar claves que puedan ser adivinadas por un atacante fácilmente, la implementación de una política de claves seguras y cambio de estas periódicamente es necesario para este punto de acceso.',
'Establecimiento de cifrado WPA/WPA2 - PSK: Es lo más robusto que hay hoy en día, aunque no es ni mucho menos infalible, ya que existen formas de atacar un red con WPA/WPA2-PSK, pero es lo más que podemos tener en cuanto a cifrado de red en entornos domésticos.',
'Cambio de la clave por defecto. El punto de acceso objetivo contiene una configuración por defecto. Un atacante utiliza la implementación de los algoritmos que usaron los fabricantes para establecer claves por defecto.',
'Ocultar el SSID: Al ocultar el SSID del punto de acceso, se evita que emita los beacon frames con el nombre de la red. Limitando la difusión del punto de acceso a personas ajenas a la red.',
'Cambiar periódicamente del SSID y clave: al realizar este proceso periódicamente se evita que la configuración de acceso al punto de acceso termine almacenada en bases de datos públicas y cualquier persona logre ingresar a la red.',
'Desactivación del WPS (WiFi Protected Setup): Esta característica permite que un equipo se conecte a la WiFi utilizando un código temporal que simplifica todo el proceso de "enrollment" de un nuevo equipo. Por desgracia las implementaciones de muchos routers no detectan los ataques de fuerza bruta y en unos minutos un atacante lograria ingresar a la red WiFi. ',
'Filtración por direcciones MAC de conexión: No es una medida definitiva, pero dificulta el trabajo del atacante, además ayuda a identificar y localizar a los atacantes.',
'Implementación de WPA/WPA2 - Enterprise: Esta tipo de configuración de red está pensada para diseños empresariales, que agrega un nivel de seguridad adicional.',
'Deshabilitar el punto de acceso cuando no esté en uso.',
'Actualiza el firmware del punto de acceso: Se debe actualizar el software del software del router o punto de acceso.',
'Cambio de la contraseña de administración del punto de acceso: Las credenciales por defecto representan un problema en estos dispositivos.',
'Configuración del Firewall del sistema operativo: Este procedimiento es útil con el uso de VPN, el firewall del router no ofrece ninguna protección mediante este tipo de conexión, así que es fundamental configurar el del sistema operativo activo y restringir todos los protocolos de entrada a los equipos pertenecientes de la red.', 
'Supervisión constante de logs del router o punto de acceso Wi-Fi: Permite tener un historial sobre las direcciones MAC y las direcciones IP de conexión a la red. Si se ha configurado filtrado de MAC, y algún atacante logra entrar en la red, entonces en los logs quedarán registrados varios equipos con la misma dirección IP sobre la misma dirección MAC. Esto permite la generación de alertas.',
'Uso de escaneo pasivo de conexiones: El uso de herramientas para el escaneo de red, permite la identificación de los equipo en la red y control de dispositivos en la red.'
]

cdnBootstrap = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">'

def initLog():
	file = open("log.html", "w")
	file.write(cdnBootstrap)
	file.write('<title> Log PPDRON </title>')
	file.write('<div class="center-block"><h1> <strong>Log </strong> <small> PPDRON</small></h1></div>')
	file.close()

def initReport():
	file = open("report.html", "w")
	file.write(cdnBootstrap)
	file.write('<title> Reporte PPDRON </title>')
	file.write('<div class="center-block"><h1> <strong>Reporte </strong> <small> PPDRON</small></h1></div>')
	file.close()

def generateReport():
	file = open("report.html", "a")
	file.write('<table class="table table-hover">')
	file.write('<tr><th>AP Objetivo</th><th>Canal</th><th>Encriptación</th><th>Ataque</th><th>Clave</th></tr>')
	file.write('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>'.format(TARGET_ESSID, TARGET_CHANNEL, TARGET_PRIVACY, TARGET_ATTACK, TARGET_KEY))
	file.write('</table>')
	file.write('<br>')
	file.write('<table class="table table-hover">')
	file.write('<tr><th>Recomendaciones</th></tr>')
	for x in recomendations:
		file.write('<tr><td><li>{0}</li></td></tr>'.format(x))
	file.write('</table>')
	file.close()

def saveLog(data):
	file = open("log.html", "a")
	file.write('<h3>' + time.strftime("%H:%M:%S") + ' [ ' + data + ' ] </h3>')
	file.close()
	


