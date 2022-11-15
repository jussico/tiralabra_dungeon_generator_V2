from generator.cave_generator import CaveGenerator
from generator.renderer import Renderer

def main():
    gen = CaveGenerator()
    renderer = Renderer()
    # cave = gen.create_empty_cave(20, 10)
    # print(cave.taulukko)
    # renderer.display(cave)

    # renderer.display(gen.create_empty_cave(5, 40))
    # renderer.display(gen.create_empty_cave(40, 5))
    renderer.display(gen.create_empty_cave(80, 40))

if __name__ == "__main__":
    main()
