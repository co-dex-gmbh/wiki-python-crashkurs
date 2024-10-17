import unittest


def gameloop():
    spielbrett = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    aktiver_spieler = 'x'
    nächster_spieler = 'o'

    while not es_gibt_gewinner(spielbrett):
        print(als_quadrat(spielbrett))

        position = int(input(f"Spieler {aktiver_spieler}, wo willst du setzen? "))

        symbol_schreiben(spielbrett, position, aktiver_spieler)

        # Wechsle Spieler
        zwischenspeicher = aktiver_spieler
        aktiver_spieler = nächster_spieler
        nächster_spieler = zwischenspeicher

    print(als_quadrat(spielbrett))
    print(f"Herzlichen Glückwunsch!")


def als_quadrat(spielbrett):
    return f"{spielbrett[0]} | {spielbrett[1]} | {spielbrett[2]}\n{spielbrett[3]} | {spielbrett[4]} | {spielbrett[5]}\n{spielbrett[6]} | {spielbrett[7]} | {spielbrett[8]}"


def es_gibt_gewinner(spielbrett):
    return (spielbrett[0] == spielbrett[1] == spielbrett[2]
            or spielbrett[3] == spielbrett[4] == spielbrett[5]
            or spielbrett[6] == spielbrett[7] == spielbrett[8]
            or spielbrett[0] == spielbrett[3] == spielbrett[6]
            or spielbrett[1] == spielbrett[4] == spielbrett[7]
            or spielbrett[2] == spielbrett[5] == spielbrett[8]
            or spielbrett[0] == spielbrett[4] == spielbrett[8]
            or spielbrett[2] == spielbrett[4] == spielbrett[6])


def symbol_schreiben(spielbrett, position, symbol):
    spielbrett[position] = symbol


class TestAlsQuadrat(unittest.TestCase):
    def test_als_quadrat_0(self):
        spielbrett = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        erwartet = "0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8"
        self.assertEqual(als_quadrat(spielbrett), erwartet)

    def test_als_quadrat_1(self):
        spielbrett = ["x", "o", 2, "x", 4, 5, 6, 7, "o"]
        erwartet = "x | o | 2\nx | 4 | 5\n6 | 7 | o"
        self.assertEqual(als_quadrat(spielbrett), erwartet)


class TestEsGibtGewinner(unittest.TestCase):
    def test_es_gibt_gewinner_alles_leer(self):
        spielbrett = [0, 1, 2,
                      3, 4, 5,
                      6, 7, 8]
        self.assertEqual(False, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_erste_zug(self):
        spielbrett = [0, "x", 2,
                      3, 4, 5,
                      6, 7, 8]
        self.assertEqual(False, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_zweiter_zug(self):
        spielbrett = [0, "x", 2,
                      3, "o", 5,
                      6, 7, 8]
        self.assertEqual(False, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_dritter_zug(self):
        spielbrett = [0, "x", 2,
                      3, "o", 5,
                      6, "x", 8]
        self.assertEqual(False, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_zeile_0(self):
        spielbrett = ["x", "x", "x",
                      "o", "o", 5,
                      6, 7, 8]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_zeile_1(self):
        spielbrett = ["x", "x", "o",
                      "o", "o", "o",
                      6, 7, 8]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_zeile_2(self):
        spielbrett = [0, "x", "o",
                      "x", "o", "o",
                      "x", "x", "x"]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_spalte_0(self):
        spielbrett = ["x", 1, 2,
                      "x", 4, 5,
                      "x", 7, 8]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_spalte_1(self):
        spielbrett = [0, "o", 2,
                      3, "o", 5,
                      6, "o", 8]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_spalte_2(self):
        spielbrett = [0, 1, "x",
                      3, 4, "x",
                      6, 7, "x"]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_diagonale_links_nach_rechts(self):
        spielbrett = ["x", 1, 2,
                      3, "x", 5,
                      6, 7, "x"]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_diagonale_rechts_nach_links(self):
        spielbrett = [0, 1, "x",
                      3, "x", 5,
                      "x", 7, 8]
        self.assertEqual(True, es_gibt_gewinner(spielbrett))

    def test_es_gibt_gewinner_unentschieden(self):
        spielbrett = ["x", "o", "x",
                      "x", "x", "o",
                      "o", "x", "o"]
        self.assertEqual(False, es_gibt_gewinner(spielbrett))

class TestSymbolSchreiben(unittest.TestCase):
    def test_symbol_schreiben_0(self):
        spielbrett = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        symbol = "x"
        position = 4
        erwartet = [0, 1, 2, 3, "x", 5, 6, 7, 8]
        symbol_schreiben(spielbrett, position, symbol)
        self.assertEqual(spielbrett, erwartet)

    def test_symbol_schreiben_1(self):
        spielbrett = ["x", "o", 2, "x", 4, 5, 6, 7, "o"]
        symbol = "o"
        position = 2
        erwartet = ["x", "o", "o", "x", 4, 5, 6, 7, "o"]
        symbol_schreiben(spielbrett, position, symbol)
        self.assertEqual(spielbrett, erwartet)


if __name__ == '__main__':
    # unittest.main() # kommentar entfernen, um Methoden zu testen
    gameloop()
