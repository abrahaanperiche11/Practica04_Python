from pyfiglet import Figlet
import random

def main():
    # Obtendremos los tipos de letras
    fuentes_disponibles = Figlet().getFonts()

    # pedimos al usuario ingrear la fuente
    fuente_seleccionada = input("Ingrese el nombre de la fuente: ")
    if fuente_seleccionada=='':
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Se seleccionó aleatoriamente la fuente: {fuente_seleccionada}")

    # Solicitar al usuario el texto
    texto_imprimir = input("Ingrese el texto a imprimir: ")

    # Configurar la fuente seleccionada
    figlet = Figlet(font=fuente_seleccionada)

    # Imprimir el texto usando la fuente seleccionada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()