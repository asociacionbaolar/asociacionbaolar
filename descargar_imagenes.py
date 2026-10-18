# -*- coding: utf-8 -*-
"""
Descarga a la carpeta img/ todas las fotos (y el PDF del proyecto) que la web
todavía carga desde Wix, y cambia los enlaces de las páginas para que apunten
a las copias locales.

Hay que ejecutarlo UNA vez, ANTES de dar de baja la web de Wix:
    python3 descargar_imagenes.py      (en Mac o Linux)
    py descargar_imagenes.py           (en Windows)

Solo usa Python, sin instalar nada más. Se puede repetir sin problema.
"""
import os, re, sys, urllib.request

CARPETA = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(CARPETA, "img")
PATRON = re.compile(r'https://(?:static\.wixstatic\.com/media/[^"\s)]+|www\.asociacionbaolar\.org/_files/[^"\s)]+)')

def nombre_local(url):
    if "/_files/" in url:
        return "proyecto-" + url.rsplit("/", 1)[-1]
    archivo = url.split("/media/")[1].split("/")[0]          # p. ej. dadc18_xxx~mv2.jpg
    tam = re.search(r"/w_(\d+)", url)
    base, ext = os.path.splitext(archivo.replace("~", "-"))
    return f"{base}-{tam.group(1) if tam else 'orig'}{ext}"

def main():
    os.makedirs(DESTINO, exist_ok=True)
    # Los archivos que empiezan por "._" son copias ocultas que el Mac crea en discos externos: se ignoran
    paginas = [f for f in os.listdir(CARPETA) if f.endswith(".html") and not f.startswith("._")]
    urls = set()
    for p in paginas:
        with open(os.path.join(CARPETA, p), encoding="utf-8") as f:
            urls.update(PATRON.findall(f.read()))
    print(f"{len(urls)} archivos que descargar")
    fallos = []
    mapa = {}
    for i, url in enumerate(sorted(urls), 1):
        local = nombre_local(url)
        ruta = os.path.join(DESTINO, local)
        mapa[url] = "img/" + local
        if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as r, open(ruta, "wb") as out:
                out.write(r.read())
            print(f"  [{i}/{len(urls)}] {local}")
        except Exception as e:
            fallos.append((url, e))
            mapa.pop(url)
            print(f"  [{i}/{len(urls)}] FALLO {url}: {e}")
    for p in paginas:
        ruta = os.path.join(CARPETA, p)
        with open(ruta, encoding="utf-8") as f:
            txt = f.read()
        for url, local in mapa.items():
            txt = txt.replace(url, local)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(txt)
    if fallos:
        print(f"\n{len(fallos)} archivos no se han podido bajar. Vuelve a ejecutar el script más tarde.")
        sys.exit(1)
    print("\nListo: todas las imágenes están en img/ y las páginas ya no dependen de Wix.")

if __name__ == "__main__":
    main()
