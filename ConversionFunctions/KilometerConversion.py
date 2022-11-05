class ConvertSpeedKM:
    def km_t_km(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "KM":
            print(f"Converted Speed: {speed.__round__(accuracy)} kmh")

    def km_t_mp(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "MP":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 5280
            print(f"Converted Speed: {outcome.__round__(accuracy)} mph")

    def km_t_kn(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "KN":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            outcome = feet_h / 6076
            print(f"Converted Speed: {outcome.__round__(accuracy)} knots")

    def km_t_ma(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "MA":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            knots_h = feet_h / 6076
            outcome = knots_h / 661.7
            print(f"Converted Speed: {outcome.__round__(accuracy)} mach (at sea level)")

    def km_t_li(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "LI":
            meters_h = speed * 1000
            feet_h = meters_h * 3.280839895013
            miles_h = feet_h / 5280
            miles_m = miles_h / 60
            miles_s = miles_m / 60
            outcome = miles_s / 186000
            print(f"Converted Speed: {outcome.__round__(accuracy)} times the speed of light")