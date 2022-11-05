# This repo contains many scripts to convert different speed measurement units like: mph, kph

## KMH definition
KMH or KPH or km/h is an abbreviation for “kilometer per hour”. It is a unit of speed that is used to express the number of kilometers travelled in one hour

## MPH definition
MPH or mi/h is an abbreviation for “miles per hour”. It is the United States Customary and British Imperial unit of speed that is used to express the number of miles travelled in one hour.

## Knot definition
The knot is a unit of speed; one knot equals one nautical mile per hour, exactly 1.852 km/h.

Conversion of [kph to mph](https://www.calculatorful.com/kmh-to-mph) can easily be carried out with the help of the following formula:
```
Mph = Kph / 1.609344
```
As 1 MPH equals 1.609344 km/h, therefore we will divide the specific value of km/h by 1.609344 to get output in mph.

Sample function
```
def km_t_mp(self, speed, unit, desired_unit, accuracy):
        if unit == "KM" and desired_unit == "MP":
            outcome = speed / 1.609344
            print(f"Converted Speed: {outcome.__round__(accuracy)} mph")
```


