from project.common import gym_dataclass


Customer = gym_dataclass({
    'name': str,
    'address': str,
    'email': str
}, 'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}')
