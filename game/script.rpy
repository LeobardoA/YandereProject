# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define mami = Character("Mami Nanami", color="#F5C10E")
define config.default_text_cps = 1 #0-100 is accepted


# El juego comienza aquí.

label start:

    play music "electric love.mp3" fadeout 1.0

    scene bg_sunset

    show mami idle:
        zoom 0.6
        xalign 0.5
        yalign 1.0

    mami "Vaya..."

    mami "Asi que ahora el tipo este esta haciendo un juego tipo Doki Doki de mi huh?, Gracias Isabel."

    mami "Hey..."

    python:
        import ctypes
        import re
        import socket
        # Define algunas constantes necesarias
        SPI_SETDESKWALLPAPER = 20
        RUTA_IMAGEN  = str(renpy.open_file("images/bg_sunset.png"))
        ruta_archivo = re.search(r"'(.*?)'", RUTA_IMAGEN).group(1)
        ruta_archivo = ruta_archivo.replace('\\\\', '/')
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, ruta_archivo, 3)
        nombre_equipo = socket.gethostname()
        print(nombre_equipo)



    mami "Sabias que hay cambios en tu equipo?"
    # Finaliza el juego:

    return
