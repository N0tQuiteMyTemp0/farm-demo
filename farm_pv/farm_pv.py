
from farm_pv.inverter_base import Inverter


class FarmPV:
    """list of all installed devices"""
    inverters = []

    def read(self) -> None:
        """generate raport for the farm"""
        print(self.__DISPLAY_HEADER)

        inverter: Inverter
        for inverter in FarmPV.inverters:
            inverter.update_all_parameters()
            self.__display_parameters(inverter)
        print()

    def add_inverter(self, inverter) -> None:
        """add a next inverter to the farm (Inverter type required)"""
        if not isinstance(inverter, Inverter):
            raise TypeError("Error. Inverter type object required.")

        inverter.id = self.__assign_device_id()
        FarmPV.inverters.append(inverter)

    #
    # private stuff
    #
    __nextId = 1

    def __assign_device_id(self) -> str:
        """trivial id generator (static field value incremented by 1)"""
        current_free_id = FarmPV.__nextId
        FarmPV.__nextId += 1
        return str(current_free_id)

    def __display_parameters(self, inverter: Inverter) -> None:
        text = (
            f'{inverter.id:>32}\t{inverter.instant_power:>3}\t'
            f'{inverter.energy_per_day:>7}\t{inverter.temperature:>11}'
        )
        print(text)

    __DISPLAY_HEADER = \
        'MODEL_INVERTERA_NUMER_PORZADKOWY\tMOC\tENERGIA\tTEMPERATURA'
