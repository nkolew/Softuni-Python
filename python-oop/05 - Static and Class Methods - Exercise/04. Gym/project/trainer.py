from project.common import gym_dataclass


Trainer = gym_dataclass({
    'name':str,
}, 'Trainer <{self.id}> {self.name}')