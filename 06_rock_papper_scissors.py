#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

def rock_paper_scissor_lizard_spock(game: list):
    p1_points = 0
    p2_points = 0

    rules = {"🗿": ["✂️", "🦎"],
             "📄": ["🗿", "🖖"],
             "✂️": ["📄", "🦎"],
             "🦎": ["🖖", "📄"],
             "🖖": ["🗿", "✂️"]}

    for play in game:
        p1_selection = play[0]
        p2_selection = play[1]
        if p1_selection != p2_selection:
            if p1_selection in rules[p2_selection]:
                p1_points += 1
            else:
                p2_points += 1
    return 'Tie' if p1_points == p2_points else "P1 win." if p1_points > p2_points else "P2 Win."


def run():
    print(rock_paper_scissor_lizard_spock([("🗿", "🗿")]))
    print(rock_paper_scissor_lizard_spock([("🗿", "✂️")]))
    print(rock_paper_scissor_lizard_spock([("✂️", "🗿")]))
    print(rock_paper_scissor_lizard_spock(
        [("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿"), ("🗿", "🗿")]))
    print(rock_paper_scissor_lizard_spock([("🖖", "🗿"), ("✂️", "📄"), ("🗿", "🗿"), ("🦎", "🖖")]))


if __name__ == '__main__':
    run()