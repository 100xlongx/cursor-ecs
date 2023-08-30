from esper import Processor
from components.aging import Aging

class AgeProcessor(Processor):
    def process(self):
        for ent, (component, ) in self.world.get_components(Aging):
            component.age += 1
            