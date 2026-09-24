L = {
"code": "es", "htmllang": "es", "name": "Español",
"date": "25 de septiembre de 2026",
"ui": {
    "home": "Inicio", "privacy": "Privacidad", "terms": "Términos", "delete": "Borrar datos",
    "menu": "Páginas", "language": "Idioma", "effective": "Fecha de entrada en vigor", "contact": "Contacto",
    "summary": "En resumen", "toc": "Contenido", "legal": "Legal",
    "by": "Un juego para móviles de Synverse",
    "tagline": "Política de privacidad, términos de uso y eliminación de datos de Watt Street.",
    "landing": "Watt Street es un juego idle tycoon sobre llevar la luz eléctrica a una ciudad al estilo de 1882. Este sitio reúne los documentos legales del juego.",
},
"privacy": {
"title": "Política de privacidad",
"blurb": "Qué datos usa el juego, para qué y cuáles son tus derechos.",
"intro": """<p>Esta Política de privacidad explica cómo <b>Synverse</b> (“nosotros”) trata la información cuando juegas a <b>%GAME%</b> (“el juego”, paquete <code>%PKG%</code>) en Android o iOS. Diseñamos el juego para funcionar con el mínimo de datos posible: no hay registro y nunca te pedimos tu nombre, correo electrónico ni número de teléfono.</p>""",
"summary": [
    "No necesitas cuenta ni inicio de sesión. El juego crea un ID de jugador (Player ID) anónimo y aleatorio mediante Unity Gaming Services.",
    "El progreso de tu ciudad se guarda en tu dispositivo y se copia en Unity Cloud Save con ese ID de jugador.",
    "No recopilamos tu nombre, correo, teléfono, contactos, fotos, ubicación precisa, cámara ni micrófono.",
    "Los anuncios, cuando existan, son vídeos con recompensa opcionales de Google AdMob. Google puede usar identificadores del dispositivo para publicidad, con tu consentimiento cuando la ley lo exija.",
    "Puedes pedirnos en cualquier momento que borremos tus datos en la nube: consulta <a href=\"%DELETE_LINK%\">Borrar tus datos</a>.",
],
"sections": [
("Responsable del tratamiento", """<p>El responsable del tratamiento es Synverse, editor de %GAME%. Puedes contactarnos en %EMAIL%.</p>"""),
("Información que trata el juego", """<h3>a) Datos guardados solo en tu dispositivo</h3>
<p>El juego conserva tu partida guardada (progreso de la ciudad, edificios, moneda del juego, marcas de tiempo para las ganancias sin conexión) y tus ajustes (música, efectos de sonido, vibración, idioma, progreso del tutorial y contadores de espera de anuncios) en el almacenamiento privado de la app en tu dispositivo. No tenemos acceso a estos datos. La vibración (háptica) la gestiona tu dispositivo localmente y no envía nada.</p>
<h3>b) ID de jugador anónimo (Unity Authentication)</h3>
<p>Cuando juegas en línea, el juego inicia sesión de forma anónima con Unity Authentication. Unity asigna un <b>ID de jugador</b> aleatorio y tokens de sesión. Este ID no está vinculado a tu nombre, correo ni teléfono. Los servicios de Unity también usan un identificador de instalación aleatorio y datos técnicos como tu dirección IP, tipo de dispositivo, sistema operativo y versión de la app para prestar el servicio.</p>
<h3>c) Copia en la nube (Unity Cloud Save)</h3>
<p>Una copia de tu partida (los mismos datos de progreso descritos arriba, más identificadores técnicos de revisión) se guarda en Unity Cloud Save con tu ID de jugador para poder restaurar tu ciudad. El juego sincroniza esta copia periódicamente mientras juegas.</p>
<h3>d) Contenido del juego (Unity Remote Config)</h3>
<p>El juego descarga su catálogo de misiones desde Unity Remote Config. Esta solicitud usa tu ID de jugador y los datos técnicos necesarios para entregar el contenido; no envía tu partida.</p>
<h3>e) Vinculación opcional de cuenta (si está disponible)</h3>
<p>Si el juego ofrece vincular tu progreso a una cuenta de Unity, el inicio de sesión se hace en la propia página de Unity. Nunca vemos ni guardamos tu contraseña; Unity solo comunica al juego un identificador de cuenta para poder restaurar tu partida en otro dispositivo.</p>
<h3>f) Anuncios (Google AdMob, si/cuando estén disponibles)</h3>
<p>El juego puede ofrecer <b>anuncios con recompensa opcionales</b>: un anuncio solo se reproduce cuando tocas para verlo a cambio de una recompensa en el juego. No hay anuncios obligatorios. Los anuncios los proporciona Google AdMob, que puede recopilar y tratar el identificador de publicidad de tu dispositivo (ID de publicidad de Android / IDFA de Apple), tu dirección IP, información del dispositivo y de la app y datos de interacción con anuncios para mostrar, medir y personalizar anuncios y prevenir el fraude. En Android 13 y posteriores, el juego declara el permiso <code>AD_ID</code> para que AdMob pueda leer el ID de publicidad; puedes restablecerlo o eliminarlo en los ajustes del dispositivo.</p>
<p>En el Espacio Económico Europeo, el Reino Unido y Suiza, el juego te pide consentimiento mediante la plataforma de mensajes para usuarios (UMP) de Google antes de mostrar anuncios personalizados; si lo rechazas, Google aún puede mostrar anuncios no personalizados. En iOS, el identificador de publicidad solo se usa si lo permites en el aviso de Transparencia de Seguimiento de Apps (ATT) de Apple. Más información: <a href="%G_PARTNER%">Cómo usa Google la información de sitios web o aplicaciones que utilizan sus servicios</a> y la <a href="%G_PRIV%">Política de privacidad de Google</a>.</p>
<h3>g) Compras dentro de la app (si/cuando estén disponibles)</h3>
<p>Si el juego ofrece compras, los pagos los procesan íntegramente Google Play o el App Store de Apple. Nunca recibimos los datos de tu tarjeta o cuenta bancaria. Solo recibimos una confirmación de compra (como el ID del producto y el ID del pedido o transacción) para entregarte lo que compraste.</p>
<h3>h) Cuando nos escribes</h3>
<p>Si nos envías un correo, recibimos tu dirección de correo y lo que incluyas en el mensaje, y lo usamos solo para responderte.</p>
<h3>i) Lo que no recopilamos</h3>
<p>No recopilamos tu nombre, correo (salvo que nos escribas), teléfono, contactos, fotos o archivos, ubicación precisa o aproximada mediante los servicios de ubicación del dispositivo, ni datos de cámara o micrófono. El juego no tiene chat ni funciones sociales. No usamos el servicio Unity Analytics ni servicios de informes de errores. El propio motor Unity puede enviar a Unity información técnica limitada (por ejemplo, modelo del dispositivo, sistema operativo y versión del motor), como se describe en la <a href="%U_PRIV%">política de privacidad de Unity</a>.</p>"""),
("Finalidades y bases legales", """<ul>
<li><b>Hacer funcionar el juego y conservar tu progreso</b> (partida local, copia en la nube, inicio de sesión anónimo, descarga de misiones): necesario para prestar el servicio que solicitas (art. 6.1.b RGPD).</li>
<li><b>Seguridad, prevención de abusos y estabilidad del servicio</b> (por ejemplo, límites de solicitudes y registros técnicos que conserva Unity): nuestro interés legítimo (art. 6.1.f RGPD).</li>
<li><b>Anuncios personalizados</b>: tu consentimiento cuando se requiera (art. 6.1.a RGPD), que puedes retirar en cualquier momento. Anuncios no personalizados y prevención del fraude publicitario: interés legítimo.</li>
<li><b>Responder a tus solicitudes y cumplir obligaciones legales</b>: obligación legal e interés legítimo (art. 6.1.c y f RGPD).</li>
</ul>
<p>No usamos tus datos para decisiones automatizadas con efectos jurídicos o similarmente significativos para ti.</p>"""),
("Con quién los compartimos", """<ul>
<li><b>Unity Technologies</b> (Authentication, Cloud Save, Remote Config) aloja el ID de jugador, la copia en la nube y el contenido del juego por nuestra cuenta como proveedor de servicios. Consulta la <a href="%U_PRIV%">política de privacidad de Unity</a>.</li>
<li><b>Google</b> (AdMob), si se ofrecen anuncios, como se describe arriba. Para los anuncios personalizados, Google actúa como responsable independiente de los datos que recopila. Consulta la <a href="%G_PRIV%">Política de privacidad de Google</a>.</li>
<li><b>Google Play / Apple</b>, para descargas, actualizaciones y posibles compras, según sus propias políticas de privacidad.</li>
<li><b>Autoridades</b>, solo si la ley lo exige.</li>
</ul>
<p>No vendemos tu información personal a cambio de dinero. Según algunas leyes estatales de EE. UU. (por ejemplo, California), permitir que AdMob muestre anuncios personalizados puede considerarse “compartir” datos para publicidad conductual entre contextos; puedes oponerte como se indica en la sección 7.</p>"""),
("Transferencias internacionales", """<p>Unity y Google pueden tratar datos en servidores fuera de tu país, incluido Estados Unidos. Estas transferencias se basan en garantías adecuadas, como las Cláusulas Contractuales Tipo de la Comisión Europea.</p>"""),
("Cuánto tiempo los conservamos", """<ul>
<li><b>Datos del dispositivo</b>: hasta que borres el juego o su almacenamiento.</li>
<li><b>Copia en la nube e ID de jugador</b>: mientras uses el juego. Los borramos cuando nos lo pidas (consulta <a href="%DELETE_LINK%">Borrar tus datos</a>), en un plazo de 30 días desde la verificación de la solicitud.</li>
<li><b>Correos de soporte</b>: hasta 12 meses después de resolver tu solicitud, salvo que la ley exija más tiempo.</li>
<li><b>Datos publicitarios</b>: los conserva Google según sus propias políticas.</li>
</ul>"""),
("Tus opciones y derechos", """<p>Según dónde vivas, tienes derecho a acceder a tus datos, rectificarlos, suprimirlos, limitar u oponerte a su tratamiento, recibirlos en un formato portable y retirar tu consentimiento en cualquier momento (RGPD). Los residentes de California y otros estados de EE. UU. pueden solicitar conocer, borrar y corregir su información personal y oponerse a su “venta” o “compartición”; no te discriminaremos por ejercer estos derechos. Los usuarios en Turquía tienen los derechos del artículo 11 de la ley KVKK.</p>
<p><b>Cómo ejercerlos:</b> escribe a %EMAIL% e incluye el ID de jugador que aparece en el juego en <i>Ajustes › Cuenta y nube</i>. Como no conocemos tu nombre ni tu correo, el ID de jugador es la forma de encontrar tus datos. Respondemos en un plazo de 30 días.</p>
<p><b>Anuncios:</b> cambia tu consentimiento publicitario en las opciones de privacidad del juego (se muestran en el EEE, el Reino Unido y Suiza), restablece o elimina tu ID de publicidad en los ajustes del dispositivo, o gestiona los anuncios en <a href="%G_ADS%">Mi Centro de Anuncios</a>. En iOS, puedes desactivar el seguimiento en Ajustes › Privacidad y seguridad › Rastreo.</p>
<p>También puedes presentar una reclamación ante tu autoridad de protección de datos (UE/EEE: <a href="%EDPB%">lista de autoridades</a>; en España, la AEPD).</p>"""),
("Borrar tus datos", """<p>Desinstalar el juego elimina todos los datos guardados en tu dispositivo. Para borrar tu copia en la nube y tu ID de jugador anónimo, sigue los pasos de <a href="%DELETE_LINK%">Borrar tus datos</a>.</p>"""),
("Menores", """<p>%GAME% está pensado para jugadores de 13 años o más y no está dirigido a menores de 13 años. No recopilamos a sabiendas información personal de menores de 13 años, de acuerdo con la ley estadounidense de protección de la privacidad infantil en línea (COPPA). Si eres padre, madre o tutor y crees que tu hijo menor de 13 años ha usado el juego, escríbenos a %EMAIL% y borraremos los datos relacionados. Donde la ley local fije una edad mayor para consentir el tratamiento de datos (hasta 16 años en algunos países de la UE; 14 en España), los jugadores por debajo de esa edad solo deben aceptar anuncios personalizados con permiso de sus padres.</p>"""),
("Seguridad", """<p>Los datos que se envían entre el juego y los servicios de Unity o Google se cifran en tránsito (HTTPS/TLS). Los datos de tu dispositivo se guardan en el almacenamiento privado de la app, protegido por el sistema operativo. Ningún sistema es totalmente seguro, pero limitamos lo que recopilamos para que haya poco que proteger.</p>"""),
("Cambios en esta política", """<p>Podemos actualizar esta política cuando cambie el juego (por ejemplo, al añadir anuncios o compras). Cambiaremos la fecha de entrada en vigor y, si los cambios son importantes, te avisaremos en el juego.</p>"""),
("Contacto", """<p>Synverse — %EMAIL%<br>Escribe “%GAME%” en el asunto.</p>"""),
],
},
"terms": {
"title": "Términos de uso",
"blurb": "Las reglas básicas para jugar.",
"intro": """<p>Estos Términos de uso (“Términos”) son un acuerdo entre tú y <b>Synverse</b> para el juego móvil <b>%GAME%</b>. Al descargar o jugar al juego aceptas estos Términos y nuestra <a href="%PRIVACY_LINK%">Política de privacidad</a>. Si no estás de acuerdo, no uses el juego.</p>""",
"sections": [
("Quién puede jugar", """<p>Debes tener al menos 13 años. Si eres menor de edad donde vives, necesitas el permiso de tu padre, madre o tutor.</p>"""),
("Tu licencia", """<p>Te concedemos una licencia personal, no exclusiva, intransferible y revocable para descargar y jugar al juego en tus dispositivos con fines no comerciales. El juego, su código, arte, música, textos y marcas pertenecen a Synverse o a sus licenciantes. No puedes copiar, vender, alquilar, modificar, aplicar ingeniería inversa ni redistribuir el juego, salvo cuando la ley lo permita expresamente.</p>"""),
("Objetos y moneda del juego", """<p>El dinero, los objetos, las mejoras y el progreso del juego no tienen valor real, no pueden cambiarse por dinero real y se te conceden bajo licencia, no se venden. Podemos equilibrarlos, cambiarlos o eliminarlos al actualizar el juego.</p>"""),
("Compras (si/cuando estén disponibles)", """<p>Si el juego ofrece compras, se realizan a través de Google Play o el App Store de Apple y se rigen por sus condiciones y políticas de reembolso. Tus derechos legales como consumidor no se ven afectados.</p>"""),
("Anuncios", """<p>El juego puede ofrecer anuncios con recompensa opcionales. El contenido publicitario lo proporcionan terceros (Google AdMob) y no somos responsables de los productos o sitios de terceros que aparezcan en los anuncios.</p>"""),
("Uso justo", """<p>No uses el juego con fines ilícitos, no ataques ni sobrecargues nuestros servicios ni los de nuestros proveedores, y no interfieras en el uso del servicio por otros jugadores.</p>"""),
("Copia en la nube y disponibilidad", """<p>La copia en la nube se ofrece por comodidad. Trabajamos para que sea fiable, pero no podemos garantizar que el juego o sus servicios en línea estén siempre disponibles, sin errores, ni que nunca se pierdan datos. Podemos actualizar, cambiar o suspender el juego o cualquier función.</p>"""),
("Exención y responsabilidad", """<p>El juego se ofrece “tal cual” y “según disponibilidad”. En la medida permitida por la ley, Synverse no responde de daños indirectos, pérdida de datos ni pérdida de objetos del juego. Nada de estos Términos limita la responsabilidad que la ley no permita limitar ni tus derechos imperativos como consumidor.</p>"""),
("Fin de estos Términos", """<p>Puedes dejar de usar el juego en cualquier momento desinstalándolo. Podemos suspender o cancelar tu acceso si incumples gravemente estos Términos.</p>"""),
("Dispositivos Apple", """<p>Si descargaste el juego del App Store de Apple, también se aplica el <a href="%APPLE_EULA%">Contrato de Licencia de Usuario Final estándar</a> de Apple. Apple no es responsable del juego ni de su soporte, y Apple y sus filiales son terceros beneficiarios de estos Términos.</p>"""),
("Ley aplicable y cambios", """<p>Estos Términos se rigen por las leyes de la República de Turquía. Si eres consumidor, conservas la protección de las leyes imperativas de tu país de residencia y puedes presentar reclamaciones allí. Podemos actualizar estos Términos; la fecha de entrada en vigor indica la versión vigente y seguir jugando implica aceptar la actualización.</p>"""),
("Contacto", """<p>Synverse — %EMAIL%</p>"""),
],
},
"delete": {
"title": "Borrar tus datos",
"blurb": "Cómo borrar tus datos en la nube de Watt Street y tu ID de jugador.",
"intro": """<p>Esta página explica cómo borrar los datos de <b>%STORE%</b> de <b>Synverse</b> (paquete <code>%PKG%</code>). El juego no tiene registro: usa un ID de jugador anónimo de Unity Gaming Services y una copia de tu ciudad en la nube.</p>""",
"sections": [
("Solicitar el borrado", """<ol>
<li>Abre el juego y toca <b>Ajustes</b> (icono de engranaje) › <b>Cuenta y nube</b>. Copia tu <b>ID de jugador</b>.</li>
<li>Escribe a %EMAIL% con el asunto <b>“%GAME% – borrado de datos”</b> e incluye tu ID de jugador.</li>
<li>Borramos tus datos en un plazo de 30 días y te lo confirmamos por correo.</li>
</ol>
<p>Si no puedes darnos un ID de jugador, puede que no encontremos tus datos, porque no conocemos tu nombre ni tu correo.</p>"""),
("Qué se borra", """<ul>
<li>Tu partida en la nube (progreso de la ciudad) guardada en Unity Cloud Save.</li>
<li>Tu ID de jugador anónimo y su registro de inicio de sesión en Unity Authentication.</li>
</ul>
<p>El borrado es permanente: tu progreso en la nube no se podrá recuperar.</p>"""),
("Qué puede conservarse", """<p>Conservamos tu correo y tu solicitud hasta 12 meses como constancia de que la atendimos, salvo que la ley exija más tiempo. Los registros técnicos de Unity se borran según los plazos de Unity. Los datos que Google recopila para publicidad los controla Google.</p>"""),
("Datos en tu dispositivo", """<p>Desinstala el juego o borra su almacenamiento en los ajustes del dispositivo para eliminar la partida y los ajustes guardados en tu teléfono. Esto no borra tu copia en la nube; solicítalo como se indica arriba.</p>"""),
("Datos publicitarios", """<p>Para restablecer o eliminar tu ID de publicidad, usa los ajustes del dispositivo (Android: Ajustes › Privacidad › Anuncios; iOS: Ajustes › Privacidad y seguridad › Rastreo). Puedes gestionar los datos publicitarios de Google en <a href="%G_ADS%">Mi Centro de Anuncios</a>.</p>"""),
],
},
}
