from project.common import gym_dataclass


Equipment = gym_dataclass({
    'name': str,
}, 'Equipment <{self.id}> {self.name}'
)

