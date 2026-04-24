# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/24 08:56:08 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/24 13:17:09 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    """
    This is the blueprint for a Plant
    """
    def __init__(self, type, age, multi, soil_water, soil_temp, soil_type):
        """
        Initialization of the plant:
        type: str, age: int, multiplier: float
        """
        self.type: str = type
        self.age: int = age
        self.multi: float = multi
        self.soil_water: int = soil_water
        self.soil_temp: float = soil_temp
        self.soil_type: str = soil_type

    def __init_3__(self, multiplier: float):
        """
        Initialization of the multiplier
        """
        self.multiplier = multiplier

    def show(self):
        """
        Method to shows the attributes of the plant
        """
        print(self.type)
        print(self.age)
        print(self.multi)
        print(self.soil_water)
        print(self.soil_temp)
        print(self.soil_type)


if __name__ == "__main__":
    plant1 = Plant("Rye", 14, 1.12, 42, 21, "Low")
    print("Hello")
    Plant.show(plant1)
#    ft_garden_data()
