from datetime import datetime
from dataclasses import dataclass


@dataclass
class Garden:
    id: int
    name: str


@dataclass
class Sensor:
    id: int
    name: str
    type: str
    connection: str
    status: bool


@dataclass
class Project:
    id: int
    name: str
    created_at = datetime.utcnow
    gardens: list
    sensors: list

    @property
    def created_date(self):
        return str(self.created_at)


sensors_history = []


def write_sensor_value(sensor_id, value,):
    sensors_history.append([str(datetime.utcnow()), sensor_id, value])
    return sensors_history[-1]


grd1 = Garden(1, 'Tomato')
sens1 = Sensor(1, 'Pump', 'rule', 'arduino', True)
pr1 = Project(1, 'First project', [1], [1])
