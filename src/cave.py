class Cave:
    nada = ' '
    owall = 'Z' # outer wall made of hardened adamantium diamond

    def __init__(self, leveys, korkeus):
        my_name = type(self).__name__
        print(f"@init {my_name}")
        self.leveys = leveys
        self.korkeus = korkeus
        self.taulukko = [self.nada] * ( leveys * korkeus )

# test

if __name__ == "__main__":
    cave = Cave(10, 10)
    from renderer import Renderer
    renderer = Renderer()
    print(cave.taulukko)
    renderer.display(cave)
