class ConvertSpeedKN:
    def kn_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "KN":
            print(f"Here is the converted speed: {speed.__round__(accuracy)} knots")

    def kn_t_mp(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "MP":
            feet_h = speed * 6076
            outcome = feet_h / 5280
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} mph")

    def kn_t_km(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "KM":
            feet_h = speed * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} kmh")

    def kn_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "MA":
            outcome = speed / 661.7
            print(f"Here is the converted speed: {outcome.__round__(accuracy)} mach (at sea level)")

    def kn_t_li(self, speed, unit, desired_unit, accuracy):
        if unit == "KN" and desired_unit == "LI":
            feet_h = speed * 6070
            miles_h = feet_h / 5280
            miles_m = miles_h / 60
            miles_s = miles_m / 60
            outcome = miles_s / 186000
            print(f"Converted Speed: {outcome.__round__(accuracy)} times the speed of light")
