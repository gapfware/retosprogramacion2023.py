# /*
#  * Crea un programa que simule el comportamiento del sombrero selccionador del
#  * universo mágico de Harry Potter. (Me aburre harry potter, lo hare de redes sociales)
#  * De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
#  * Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
#  * En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#  * coloque al usuario en una de las 4 principales redes sociales:
#  * (Facebook, Tiktok, Twitter y Instagram)
#  * Ten en cuenta los rasgos de cada red social para hacer las preguntas
#  * y crear el algoritmo seleccionador:
#  */

def select_social_media():
    ig = 0
    tw = 0
    tt = 0
    fb = 0
    questions = [
        "Para que usas redes sociales:\n1. Comunicarte\n2. Enterarte de la vida de los demas\n3. Entretenimiento\n4. Informarte",
        "Que tan delicado eres con el contenido que consumes?\n1. MUY DELICADO\n2. Delicado\n3. Moderado\n4. Cero delicado",
        "Pasas mucho tiempo en redes sociales\n1. No casi\n2. Bastante\n3. Adicto a las redes sociales\n4. Algo",
        "Te gusta publicar lo que haces por redes sociales?\n1. Lo hago con frecuencia\n2. Si, publico todo\n3. De vez en cuando\n4. Ocasionalmente",
        "Que tan hater eres?\n1. No tanto\n2. Hater\n3. Cero\n4. MUY HATER"
    ]

    for question in questions:
        print(question)
        answer = int(input(""))
        while answer < 1 or answer > 4:
            answer = int(input("Seleccione una opcion correcta.\n"))

        if answer == 1:
            fb += 1
        if answer == 2:
            ig += 1
        if answer == 3:
            tt += 1
        if answer == 4:
            tw += 1

    if fb > ig and fb > tt and fb > tw:
        return "Facebook"
    elif ig > fb and ig > tt and ig > tw:
        return "Instagram"
    elif tt > fb and tt > ig and tt > tw:
        return "TikTok"
    elif tw > fb and tw > ig and tw > tt:
        return "Twitter"
    else:
        return "Todas o... Ninguna "


def run():
    print(
        f"Tu red social ideal según tus respuestas es: {select_social_media()}"
    )


if __name__ == '__main__':
    run()