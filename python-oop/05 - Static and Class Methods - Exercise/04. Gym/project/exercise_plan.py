from project.common import gym_dataclass


@classmethod
def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
    return cls(trainer_id, equipment_id, hours*60)


ExercisePlan = gym_dataclass({
    'trainer_id': int,
    'equipment_id': int,
    'duration': int,
}, 'Plan <{self.id}> with duration {self.duration} minutes'
)

ExercisePlan.from_hours = from_hours
