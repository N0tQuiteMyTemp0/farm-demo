from farm_pv.farm_pv import FarmPV
from farm_pv.inverter_hdk125x5 import InverterHdk125x5
from farm_pv.inverter_sbsc1175 import InverterSbsc1175

if __name__ == '__main__':
    farm_pv = FarmPV()
    try:
        farm_pv.add_inverter(InverterHdk125x5())
        farm_pv.add_inverter(InverterSbsc1175())
        farm_pv.add_inverter(InverterHdk125x5())
        farm_pv.add_inverter(InverterSbsc1175())
        farm_pv.add_inverter(InverterHdk125x5())
        farm_pv.add_inverter(InverterHdk125x5())
    except TypeError as tex:
        print("Error's occurred during add_inverter() method call.")
        print("Have you passed wrong obejct type?")
        print(tex)

    for i in range(5):
        farm_pv.read()
