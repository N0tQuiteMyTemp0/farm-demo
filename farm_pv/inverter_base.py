from abc import (
    ABC,
    abstractmethod,
)


class Inverter(ABC):
    def __init__(self) -> None:
        self._id = None
        self._instant_power = 0  # value in kW
        self._temperature = 0
        self._energy_per_day = 0

    def update_all_parameters(self):
        """method should retrieve the current values from all device parameters

        Important!
        Keep in mind, whenever you introduce new parameters, the code below
        should be updated as well.
        """
        self.read_instant_power()
        self.read_energy_per_day()
        self.read_temperature()

    #
    #   ABSTRACT METHODS THAT MUST BE IMPLEMENTED BY ALL DEVICES
    #
    @property
    @abstractmethod
    def model_signature(self):
        pass

    @abstractmethod
    def read_instant_power(self):
        pass

    @abstractmethod
    def read_energy_per_day(self):
        pass

    @abstractmethod
    def read_temperature(self):
        pass

    #
    # PARAMETERS (SETTERS AND GETTERS)
    #

    @property
    def instant_power(self):
        return self._instant_power

    # @instant_power.setter
    # def instant_power(self, val):
    #     self._instant_power = val

    @property
    def energy_per_day(self):
        return self._energy_per_day

    @energy_per_day.setter
    def energy_per_day(self, val):
        self._energy_per_day = val

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, val):
        self._temperature = val

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = self.model_signature + val
