# Web de la Asociación Baolar

Web estática: 10 páginas HTML, una hoja de estilo (`css/estilo.css`) y un pequeño script (`js/menu.js`). Vive en GitHub y Cloudflare la publica gratis en asociacionbaolar.org. Cada cambio que se guarda en GitHub aparece en la web en uno o dos minutos.

## Actualización anual (leer esto primero)

1. Entra en github.com con la cuenta de Baolar y abre el repositorio `asociacionbaolar`.
2. Pulsa en la página que quieras cambiar (por ejemplo `educacion.html`) y luego en el lápiz ("Edit this file").
3. Cambia el texto. Los textos están tal cual, entre etiquetas como `<p>…</p>`. No borres las etiquetas, solo lo que hay entre ellas.
4. Pulsa "Commit changes…" y otra vez "Commit changes". En un par de minutos estará publicado.
5. Para una foto nueva: entra en la carpeta `img/`, pulsa "Add file" → "Upload files" y arrástrala. Luego, en la página, cambia el nombre del archivo dentro de `src="img/…"`.
6. Si algo sale mal: en el repositorio, pestaña "Commits", se ve cada cambio y se puede deshacer (botón "Revert").

Datos que conviene revisar cada año: becas (curso y localidad), proyectos en marcha y su estado, y que el IBAN y el correo siguen siendo los mismos.

Cuentas que hay que conservar: GitHub, Cloudflare (web y dominio) y Formspree (formulario). Las tres con asociacionbaolar@gmail.com.

## Puesta en marcha (solo la primera vez)

### 1. Salvar las fotos de Wix

Las fotos todavía se cargan desde Wix. Antes de darlo de baja:

1. Abre una terminal en esta carpeta (en Mac: escribe `cd `, arrastra la carpeta a Terminal y pulsa Intro).
2. Ejecuta `python3 descargar_imagenes.py` (en Windows: `py descargar_imagenes.py`).
3. Comprueba que se ha creado la carpeta `img/` y que, al abrir `index.html`, se ven las fotos.

El cartel del proyecto de los baños de Kaylo ya está en `docs/`.

### 2. Formulario de contacto (hecho)

El formulario ya está conectado a Formspree (cuenta de asociacionbaolar@gmail.com, formulario «Contacto web Baolar», código `xqpejpjq`). Los mensajes llegan a asociacionbaolar@gmail.com. Plan gratuito: 50 mensajes al mes.

### 3. Subir la web a GitHub

1. Crea una cuenta gratuita en github.com con asociacionbaolar@gmail.com.
2. Pulsa "New repository", llámalo `asociacionbaolar`, márcalo como "Public" y créalo.
3. En el repositorio vacío, pulsa "uploading an existing file" y arrastra **el contenido** de la carpeta baolar-web (las páginas y las carpetas `css`, `js`, `img`, `docs`), no la carpeta en sí.
4. Pulsa "Commit changes".

### 4. Publicar con Cloudflare Pages

1. Crea una cuenta gratuita en dash.cloudflare.com.
2. Workers y Pages → Crear → Pages → "Conectar a Git". Autoriza GitHub y elige el repositorio `asociacionbaolar`.
3. En la configuración de compilación no hay que poner nada: deja el comando vacío y el directorio de salida como `/`. Pulsa "Guardar e implementar".
4. En un par de minutos la web estará en `asociacionbaolar.pages.dev`. Revísala en ordenador y móvil y prueba el formulario.

El archivo `_redirects` hace que los enlaces antiguos de Wix (por ejemplo `/s-projects-side-by-side`) lleven a la página nueva.

### 5. El dominio asociacionbaolar.org

Si está comprado en Wix:

1. En Cloudflare, "Añadir un dominio" → `asociacionbaolar.org` → plan gratuito. Cloudflare dará dos servidores de nombres.
2. En Wix → Dominios, cambia los servidores de nombres por los de Cloudflare. Desde ese momento el dominio deja de mostrar la web de Wix.
3. En Cloudflare Pages → el proyecto → Dominios personalizados, añade `asociacionbaolar.org` y `www.asociacionbaolar.org`.
4. Para dejar de pagar a Wix: en Wix → Dominios → "Transferir fuera de Wix" (desactiva antes el registro privado). Llega un código de autorización al correo del titular. En Cloudflare → Registro de dominios → Transferir, pega el código. Incluye un año de renovación (unos 10 € para un .org) y tarda hasta 7 días.

No se puede transferir un dominio comprado, o con los datos del titular cambiados, en los últimos 60 días.

### 6. Cerrar Wix

Cuando la transferencia esté completada y la web nueva funcione en el dominio, cancela el plan premium de Wix. No borres el sitio de Wix enseguida: déjalo sin plan un par de meses como copia de seguridad.

## Pagos

- Dominio asociacionbaolar.org: pagado en Wix hasta el 12 de noviembre de 2027 (21,78 €). En septiembre de 2027 se transfiere a Cloudflare, que cobra unos 10 € al año.
- La asociación no tiene tarjeta: lo paga Silvia Torrijos con la suya y la asociación se lo reembolsa desde la cuenta de Triodos. La factura debe ir a nombre de la Asociación Baolar con su CIF.
- GitHub, Cloudflare Pages y Formspree son gratuitos.

## Notas

Las tipografías (Amatic SC, Caveat y Zilla Slab, parecidas a las de Wix) se cargan desde Google Fonts, lo que envía la IP de quien visita a Google. Si se quiere evitar, se pueden descargar (por ejemplo desde google-webfonts-helper) y servir desde la carpeta.

La página `privacidad.html` es un texto básico orientativo. Conviene que alguien de la junta lo revise.

El repositorio es público: cualquiera puede ver el código de la web, pero solo la cuenta de Baolar puede cambiarlo. No guardes ahí documentos internos ni datos personales.
