class ConvertSpeedMA:
    def ma_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == "MA":
            print(f"Converted Speed: {speed.__round__(accuracy)} mach (at sea level)")

    def ma_t_mp(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == "MP":
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            outcome = feet_h / 5280
            print(f"Converted Speed: {outcome.__round__(accuracy)} mph")

    def ma_t_km(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == "KM":
            knots_h = speed * 661.7
            feet_h = knots_h * 6076
            meters_h = feet_h * 0.3048
            outcome = meters_h / 1000
            print(f"Converted Speed: {outcome.__round__(accuracy)} kmh")

    def ma_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == "KN":
            outcome = speed * 661.7
            print(f"Converted Speed: {outcome.__round__(accuracy)} knots")

    def ma_t_li(self, speed, unit, desired_unit, accuracy):
        if unit == "MA" and desired_unit == "LI":
            knots_h = speed / 661.7
            feet_h = knots_h * 6076
            miles_h = feet_h / 5280
            miles_m = miles_h / 60
            miles_s = miles_m / 60
            outcome = miles_s / 186000
            print(f"Converted Speed: {outcome.__round__(accuracy)} times the speed of light")