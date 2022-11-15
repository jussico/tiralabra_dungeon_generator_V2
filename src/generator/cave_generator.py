
from generator.cave import Cave

nada = Cave.nada
owall = Cave.owall

class CaveGenerator:
    def __init__(self):
        my_name = type(self).__name__
        print(f"@init {my_name}")
    
    def create_empty_cave(self, leveys, korkeus):
        print(f"leveys: {leveys} korkeus: {korkeus}")
        cave = Cave(leveys, korkeus)
        taulukko = cave.taulukko
        # top and bottom wall
        for x in range(leveys):
            pass
            taulukko[x] = owall
            # print(f"korkeus: {korkeus} x: {x}") 
            # print(f"ongelma: {korkeus * (leveys - 1) + x}")
            taulukko[(korkeus -1) * leveys + x] = owall
        # left and right wall
        for y in range(korkeus):
            pass
            taulukko[y * leveys] = owall
            taulukko[y * leveys + leveys - 1] = owall
        return cave

# tests

if __name__ == "__main__":
    gen = CaveGenerator()
    from renderer import Renderer
    renderer = Renderer()
    # cave = gen.create_empty_cave(20, 10)
    # print(cave.taulukko)
    # renderer.display(cave)

    # renderer.display(gen.create_empty_cave(5, 40))
    # renderer.display(gen.create_empty_cave(40, 5))
    renderer.display(gen.create_empty_cave(80, 40))
