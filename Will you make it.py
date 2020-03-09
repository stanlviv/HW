def zero_fuel(distance_to_pump, mpg, fuel_left):
    result = mpg*fuel_left
    if result >= distance_to_pump:
        return True
    elif result < distance_to_pump:
        return False