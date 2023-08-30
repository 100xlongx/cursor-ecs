from esper import World

from components import Position, Velocity, Aging
from processors import MovementProcessor, AgeProcessor

def main() -> None:
    world = World()

    movement_processor = MovementProcessor()
    aging_processor = AgeProcessor()

    world.add_processor(movement_processor)
    world.add_processor(aging_processor)

    player = world.create_entity()

    world.add_component(player, Velocity(0, 1))
    world.add_component(player, Position(3, 3))
    world.add_component(player, Aging(1))

    print(world.component_for_entity(player, Aging))

    world.process()

    print(world.component_for_entity(player, Aging))

    
if __name__ == "__main__":
    main()