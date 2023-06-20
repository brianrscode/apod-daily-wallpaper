import apod
from os import getcwd
from datetime import datetime
import ctypes


def main():
    """
    Establece el fondo de escritorio actual de Windows
    con la Imagen del Día de la Astronomía de la NASA (APOD).

    Retorna:
    Ninguno
    """

    SPI_SETDESKWALLPAPER = 20

    explorer = apod.ApodExplorer()  # Crea una instancia de ApodExplorer
    # Hace una petición HTTP para obtener los datos de la imagen del día
    http_status = explorer.make_http_request(*datetime.now().timetuple()[:3])
    # Crea una instancia de ApodImageDownloader para descargar la imagen
    downloader = apod.ApodImageDownloader(explorer.check_for_images())
    # Descarga y guarda la imagen en el directorio actual
    downloader.save_image(getcwd(), "fondo.png")
    # Establece la imagen descargada como fondo de escritorio
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, getcwd() + "\\fondo.png", 0)


if __name__ == "__main__":
    main()
