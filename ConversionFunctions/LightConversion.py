class ConvertSpeedLI:
    def li_t_li(self, speed, unit, desired_unit, accuracy):
        if unit == "LI" and desired_unit == "LI":
            print(f"Converted Speed: {speed.__round__(accuracy)} times the speed of light")

    def li_t_mp(self, speed, unit, desired_unit, accuracy):
        if unit == "LI" and desired_unit == "MP":
            miles_s = speed * 186000
            miles_m = miles_s * 60
            outcome = miles_m * 60
            print(f"Converted Speed: {outcome.__round__(accuracy)}mph")

    def li_t_km(self, speed, unit, desired_unit, accuracy):
        if unit == "LI" and desired_unit == "KM":
            miles_s = speed * 186000
            miles_m = miles_s * 60
            miles_h = miles_m * 60
            feet_h = miles_h * 5280
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"Converted Speed: {outcome.__round__(accuracy)}kmh")

    def li_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "LI" and desired_unit == "KN":
            miles_s = speed * 186000
            miles_m = miles_s * 60
            miles_h = miles_m * 60
            feet_h = miles_h * 5280
            outcome = feet_h / 6076
            print(f"Converted Speed: {outcome.__round__(accuracy)} knots")

    def li_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "LI" and desired_unit == "MA":
            miles_s = speed * 186000
            miles_m = miles_s * 60
            miles_h = miles_m * 60
            feet_h = miles_h * 5280
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(f"Converted Speed: {outcome.__round__(accuracy)} mach (at sea level)")