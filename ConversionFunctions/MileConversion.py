class ConvertSpeedMP:
    def mp_t_mp(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "MP":
            print(f"Converted Speed: {speed.__round__(accuracy)} mph")

    def mp_t_km(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "KM":
            feet_h = speed * 5280
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"Converted Speed: {outcome.__round__(accuracy)} kmh")

    def mp_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "KN":
            feet_h = speed * 5280
            outcome = feet_h / 6076
            print(f"Converted Speed: {outcome.__round__(accuracy)} knots")

    def mp_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "MA":
            feet_h = speed * 5280
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(f"Converted Speed: {outcome.__round__(accuracy)} mach")

    def mp_t_li(self, speed, unit, desired_unit, accuracy):
        if unit == "MP" and desired_unit == "LI":
            miles_m = speed / 60
            miles_s = miles_m / 60
            outcome = miles_s / 186000
            print(f"Converted Speed: {outcome.__round__(accuracy)} times the speed of light")



