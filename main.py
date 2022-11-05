from ConversionFunctions import MileConversion
from ConversionFunctions import KilometerConversion
from ConversionFunctions import KnotConversion
from ConversionFunctions import MachConversion
from ConversionFunctions import LightConversion
CMP = MileConversion.ConvertSpeedMP()
CKM = KilometerConversion.ConvertSpeedKM()
CKN = KnotConversion.ConvertSpeedKN()
CMA = MachConversion.ConvertSpeedMA()
CLI = LightConversion.ConvertSpeedLI()

# Line Break
lb = "\n"

while True:
#Speed Input
    while True:
        try:
            speed = float(input("Speed? "))
            break
        except ValueError:
            print("Numerical Values Only Please!", lb)

#Unit Input
    while True:
        unit_input = input("What unit of speed was that in? (Mph), (Km/h), (Knots), (Mach), or the Speed of (Light)? ")
        unit = unit_input[0:2].upper()
        if unit in ("MP", "KM", "KN", "MA", "LI"):
            break
        print("Please input Mph, Km/h, Knots, Mach, or Light!", lb)
        continue

#Desired Unit Input
    while True:
        desired_unit_input = input("What would you like to convert to? (Mph), (Km/h), (Knots), (Mach), or the Speed of (Light)? ")
        desired_unit = desired_unit_input[0:2].upper()
        if desired_unit in ("MP", "KM", "KN", "MA", "LI"):
            break
        print("Please input Mph, Kmh, Knots, Mach, or Light!", lb)
        continue

#Accuracy Input
    while True:
        round_input = input("Would you like to round? ")
        round = round_input[0].upper()
        if round in "Y":
            while True:
                try:
                    accuracy = int(input("How many decimal points would you like to round to? "))
                    break
                except ValueError:
                    print("Please input integers (whole numbers) only!", lb)
            break
        if round in "N":
            accuracy = 100
            break
        else:
            print("Answer with yes or no please!", lb)
            continue

#Conversion Functions
    CMP.mp_t_mp(speed, unit, desired_unit, accuracy)
    CMP.mp_t_kn(speed, unit, desired_unit, accuracy)
    CMP.mp_t_km(speed, unit, desired_unit, accuracy)
    CMP.mp_t_ma(speed, unit, desired_unit, accuracy)
    CMP.mp_t_li(speed, unit, desired_unit, accuracy)

    CKM.km_t_km(speed, unit, desired_unit, accuracy)
    CKM.km_t_mp(speed, unit, desired_unit, accuracy)
    CKM.km_t_kn(speed, unit, desired_unit, accuracy)
    CKM.km_t_ma(speed, unit, desired_unit, accuracy)
    CKM.km_t_li(speed, unit, desired_unit, accuracy)

    CKN.kn_t_kn(speed, unit, desired_unit, accuracy)
    CKN.kn_t_mp(speed, unit, desired_unit, accuracy)
    CKN.kn_t_km(speed, unit, desired_unit, accuracy)
    CKN.kn_t_ma(speed, unit, desired_unit, accuracy)
    CKN.kn_t_li(speed, unit, desired_unit, accuracy)

    CMA.ma_t_ma(speed, unit, desired_unit, accuracy)
    CMA.ma_t_mp(speed, unit, desired_unit, accuracy)
    CMA.ma_t_km(speed, unit, desired_unit, accuracy)
    CMA.ma_t_kn(speed, unit, desired_unit, accuracy)
    CMA.ma_t_li(speed, unit, desired_unit, accuracy)

    CLI.li_t_li(speed, unit, desired_unit, accuracy)
    CLI.li_t_mp(speed, unit, desired_unit, accuracy)
    CLI.li_t_km(speed, unit, desired_unit, accuracy)
    CLI.li_t_kn(speed, unit, desired_unit, accuracy)
    CLI.li_t_ma(speed, unit, desired_unit, accuracy)

#Program Loop Input
    while True:
        answer = str(input("Run again? Yes/No: "))
        repeat = answer[0].upper()
        if repeat in ("Y", "N"):
            break
        print("Answer with yes or no please!", lb)
    if repeat == "Y":
        continue
    else:
        print("Goodbye! Thank you for using this program!")
        break

