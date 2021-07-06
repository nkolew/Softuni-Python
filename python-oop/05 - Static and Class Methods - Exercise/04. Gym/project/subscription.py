from project.common import gym_dataclass


Subscription = gym_dataclass({
    'date': str,
    'customer_id': int,
    'trainer_id': int,
    'exercise_id': int,
}, 'Subscription <{self.id}> on {self.date}')
