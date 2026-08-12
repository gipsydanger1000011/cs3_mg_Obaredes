def calculate_space_weight(earth_weight, destination):
    if destination == "mars":
       return earth_weight * 0.38
    elif destination == "jupiter":
       return earth_weight * 2.34
    elif destination == "moon":
       return earth_weight * 0.16
    else:
        print("Error: Unknown destination.")
        return 0

lunar_weight = calculate_space_weight(2077,"moon")
print(lunar_weight)