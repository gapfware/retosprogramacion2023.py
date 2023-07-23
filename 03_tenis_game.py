# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  *
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
#  */

def play_game(sequence: list):
    scores = ["Love", 15, 30, 40]
    p1_score = 0
    p2_score = 0

    for player in sequence:
        if player == 'P1':
            p1_score += 1
        elif player == 'P2':
            p2_score += 1

        if p1_score == 3 and p2_score == 3:
            print("Deuce")
        elif p1_score >= 4 or p2_score >= 4:
            result = p1_score - p2_score
            if result == 1:
                print("Ventaja P1")
            elif result == -1:
                print("Ventaja P2")
            elif result == 2:
                print("Ha ganado P1")
            else:
                print("Ha ganado P2")
        else:
            print(f"{scores[p1_score]} - {scores[p2_score]}")


def run():
    sequence = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P2', 'P2']
    play_game(sequence)


if __name__ == '__main__':
    run()
