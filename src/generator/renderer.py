import blessed 
from blessed.colorspace import RGB_256TABLE
import random
from util import *

# https://blessed.readthedocs.io/_/downloads/en/latest/pdf/
# steelblue4 yms. 

class Renderer:
    def __init__(self):
        my_name = type(self).__name__
        print(f"@init {my_name}")
        self.term = blessed.Terminal()

    def display(self, cave):
        self.display_table(cave.taulukko, cave.leveys, cave.korkeus)

    def display_table(self, taulukko, leveys, korkeus):
        printable = self.render(taulukko, leveys, korkeus)
        print(self.term.home + self.term.on_black + self.term.clear) # clear the screen
        print(printable, end='', flush=True)

    def render(self, taulukko, leveys, korkeus, border = False):
        logita("@render")
        result = self.term.home + self.term.normal
        if border:
            for x in range(leveys+2): result = result + '◼'
        result = result + '\n'
        for y in range(korkeus):
            if border:  result = result + '◼'
            # logita(f"leveys on: {leveys}")
            for x in range(leveys):
                # logita(f"indeksi: {y * leveys + x}")
                merkki = taulukko[y * leveys + x]
                if merkki == 'x':
                    result = result + self.term.orangered(merkki)
                if merkki == 'Z':
                    result = result + self.term.steelblue4('█')
                else:
                    # logita(f"merkki: {str(merkki)}")
                    result = result + str(merkki)
            if border:  result = result + '◼'
            result = result + '\n'
        if border:
            for x in range(leveys+2): result = result + '◼'
        result = result + '\n'

        result = result + self.term.clear_eos + '\n'

        # term.normal
        # term.center()
        # term.number_of_colors
        # blessed.color.COLOR_DISTANCE_ALGORITHMS
        # https://github.com/jquast/blessed/blob/master/docs/colors.rst

        return result

# tests

# def main():
#     logita("@main")
#     renderer = Renderer()

#     term = blessed.Terminal()
#     logita(f"24 bit colors support?: {term.number_of_colors == 1 << 24}")

#     logita("@main2")
#     with term.cbreak(), term.hidden_cursor(), term.fullscreen():
#         logita("@with")
#         korkeus = 40
#         leveys = 80
#         taulukko = [0] * korkeus * leveys
#         oliot = [0] * korkeus * leveys # TODO: oma tietorakenne kaikille erikseen, tähän esityskerros
#         for y in range(korkeus):
#             for x in range(leveys):
#                 taulukko[x*y] = ((x+1)*(y+1)) % 10

#         taulukko[100] = 'x'
#         taulukko[101] = 'x'
#         taulukko[102] = 'x'
#         taulukko[103] = 'x'

#         likainen = True
#         while True:
#             # logita("@while forever loop")
#             if likainen:
#                 outp = renderer.render(taulukko, leveys, korkeus)
#                 print(outp, end='', flush=True)

#             # muokkaa maa ilmaa
#             satu_x = random.randint(0,leveys-1)
#             satu_y = random.randint(0,korkeus-1)
#             merkki = taulukko[(satu_x+1)*(satu_y+1)-1]
#             if merkki != 'x':
#                 taulukko[(satu_x+1)*(satu_y+1)-1] = (merkki + 1) % 10

#             likainen = True
            
# if __name__ == "__main__":
#     main()
#     # c = Renderer()
