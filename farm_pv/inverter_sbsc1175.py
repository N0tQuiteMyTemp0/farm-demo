from random import randrange
from farm_pv.inverter_base import Inverter


class InverterSbsc1175(Inverter):
    @property
    def model_signature(self):
        return "Sbsc1175_Model_"

    def read_instant_power(self):
        # random value beteen 0-10 kW
        self._instant_power = randrange(10)

    def read_energy_per_day(self):
        self.energy_per_day += 2*self._instant_power

    def read_temperature(self):
        # random value beteen 0-70 Celcius degrees
        self.temperature = randrange(70)
