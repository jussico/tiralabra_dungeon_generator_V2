import blessed 
from blessed.colorspace import RGB_256TABLE
import random

def logita(jotain):
    with open('logia.txt', 'a') as logia:
        print(jotain, file=logia)
    logia.close()

def render(term, taulukko, korkeus, leveys):
    # logita("@render")
    result = term.home + term.normal
    for x in range(leveys+2): result = result + '◼'
    result = result + '\n'
    for y in range(korkeus):
        result = result + '◼'
        for x in range(leveys):
            merkki = taulukko[(x+1)*(y+1)-1]
            if merkki == 'x':
                result = result + term.orangered(merkki)
            else:
                result = result + str(merkki)
        result = result + '◼'
        result = result + '\n'
    for x in range(leveys+2): result = result + '◼'
    result = result + '\n'

    result += term.clear_eos + '\n'

    # term.normal
    # term.center()
    # term.number_of_colors
    # blessed.color.COLOR_DISTANCE_ALGORITHMS
    # https://github.com/jquast/blessed/blob/master/docs/colors.rst

    return result

def main():
    logita("@main")

    term = blessed.Terminal()
    logita(f"24 bit colors support?: {term.number_of_colors == 1 << 24}")

    logita("@main2")
    with term.cbreak(), term.hidden_cursor(), term.fullscreen():
        logita("@with")
        korkeus = 40
        leveys = 80
        taulukko = [0] * korkeus * leveys
        oliot = [0] * korkeus * leveys # TODO: oma tietorakenne kaikille erikseen, tähän esityskerros
        for y in range(korkeus):
            for x in range(leveys):
                taulukko[x*y] = ((x+1)*(y+1)) % 10

        taulukko[100] = 'x'
        taulukko[101] = 'x'
        taulukko[102] = 'x'
        taulukko[103] = 'x'

        likainen = True
        while True:
            # logita("@while forever loop")
            if likainen:
                outp = render(term, taulukko, korkeus, leveys)
                print(outp, end='', flush=True)

            # muokkaa maa ilmaa
            satu_x = random.randint(0,leveys-1)
            satu_y = random.randint(0,korkeus-1)
            merkki = taulukko[(satu_x+1)*(satu_y+1)-1]
            if merkki != 'x':
                taulukko[(satu_x+1)*(satu_y+1)-1] = (merkki + 1) % 10

            likainen = True
            
if __name__ == '__main__':
    main()
