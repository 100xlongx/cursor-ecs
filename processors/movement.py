from esper import Processor
from components.velocity import Velocity
from components.position import Position

class MovementProcessor(Processor):
    def process(self):
        for ent, (vel, pos) in self.world.get_components(Velocity, Position):
            pos.x += vel.x
            pos.y += vel.y