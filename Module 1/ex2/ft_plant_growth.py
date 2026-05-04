# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/30 08:43:34 by ccolnat         #+#    #+#               #
#  Updated: 2026/05/04 12:59:30 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# import random

R = '\033[31m'
Y = '\033[33m'
G = '\033[32m'
B = '\033[34m'
RESET = '\033[0m'


def soil_type_database(soil: int) -> str:
    """
    **Takes an int (1, 2, 3)**

    **Returns a type of soil in the form of :**
    - A string (Low, medium or high fertility soil)

    *Will default on medium fertility soil if input is outside range*
    """
    if soil == 1:
        return "low fertility soil   "
    elif soil == 3:
        return "high fertility soil  "
    else:
        return "medium fertility soil"


def vegetable_database(variety: int) -> tuple[str, float, float, int, int]:
    """
    **Takes an int (1 up to 18)**

    **Returns a turple for each vegetable variety in the form of :**
    - Name (str)
    - Mature height (float)
    - Base growth speed (float)
    - Cold resistance (int)
    - Heat resistane (int)

    *If input is outside range, will default on Dragon fruit.*
    """
    if variety == 1:
        return "Carrot      ", 25, 0.33, -10, 22
    elif variety == 2:
        return "Flax        ", 80, 0.84, -5, 30
    elif variety == 3:
        return "Onion       ", 40, 0.38, -1, 30
    elif variety == 4:
        return "Spelt       ", 11, 0.80, -5, 30
    elif variety == 5:
        return "Turnip      ", 35, 0.64, -5, 17
    elif variety == 6:
        return "Parsnip     ", 50, 0.45, -10,  22
    elif variety == 7:
        return "Rice        ", 11, 0.80, 8, 36
    elif variety == 8:
        return "Rye         ", 13, 0.90, -12, 17
    elif variety == 9:
        return "Soybean     ", 80, 0.80, -5, 30
    elif variety == 10:
        return "Amaranth    ", 12, 1.20, 6, 32
    elif variety == 11:
        return "Bell Pepper ", 75, 0.94, 8, 24
    elif variety == 12:
        return "Cassava     ", 22, 0.80, 4, 34
    elif variety == 13:
        return "Peanut      ", 40, 0.30, 10, 32
    elif variety == 14:
        return "Pineapple   ", 10, 0.20, 6, 38
    elif variety == 15:
        return "Sunflower   ", 22, 2.20, -5, 30
    elif variety == 16:
        return "Pumpkin     ", 45, 0.43, -5, 30
    elif variety == 17:
        return "Cabbage     ", 50, 0.55, -5, 25
    else:
        return "Dragon Fruit", 20, 0.80, 0, 28


class Plant:
    """
    **This is the blueprint for a Plant**
    """
    def __init__(
                self,
                soil_type: int
                ) -> None:

        self.soil_type: str = soil_type_database(soil_type)
        self.size: float = 0
        self.age: int = 0
        self.alive: bool = True
        self.moisture: float = 0.5
        self.growth_speed: float = 0


class Vegetable(Plant):
    """
    **This is the blueprint for a vegetable**
    """
    def __init__(
                self,
                soil_type: int,
                variety: int
                ) -> None:

        Plant.__init__(soil_type)
        self.name: str
        """
        **The name of the vegetable**
        """
        self.mature_size: float
        """
        **The size required to consider the vegetable mature**
        """
        self.base_growth: float
        """
        **Base growth speed**

        - Expressed in cm per day.

        - Growth speed can change depending on temp, soil and moisture.
        """
        self.heat_res: int
        """
        **Heat res**

        - Expressed in degrees celucius.

        - Plant can grow normally until temp reach that value.

        - For any degree above the res value plant lose 10% growth speed.

        - If temp reach 10 degrees above the res, plant dies.
        """
        self.cold_res: int
        """
        **Cold res**

        - Expressed in degrees celcius.

        - For any degree below 10, all plants lose 10% growth speed.

        - If temp reach that value, the plant dies.
        """

        (
            self.name,
            self.mature_size,
            self.base_growth,
            self.cold_res,
            self.heat_res
        ) = vegetable_database(variety)
        print(f"{self.name} was created succesfully ! ")

        if soil_type == "low fertility soil   ":
            self.base_growth = self.base_growth * 0.8
        elif soil_type == "high fertility soil  ":
            self.base_growth = self.base_growth * 1.2

    def show(self):
        """
        Method to show the attributes of the plant
        """
        if self.alive is True:
            print(f"| Name : {self.name} {self.age} days {self.size}cm.")
            print(f"{G} Is still alive !{RESET}")
        else:
            print(f"| Name : {self.name} {self.age} days {self.size}cm")
            print(f"{R} Is DEAD :c {RESET}")

    def grow(self):
        if self.size < self.mature_size:
            self.size += self.growth_speed
            if self.size > self.mature_size:
                self.size = self.mature_size
                print("Plant is fully grown !")

    def age(self, temp: float, rain: bool):
        """
        Method to simulate the passage of time
        """

        if temp > 5500:
            print("Hotter that the sun, kinda too much for plants isn´t it ?")
            return

        if temp < -273.15:
            print("Colder than the laws of physics, damn")
            return

        self.age += 1
        if rain is True:
            self.moisture += 0.25
            if self.moisture > 1:
                self.moisture = 1
        elif rain is False:
            self.moisture -= 0.1
            if self.moisture < 0:
                self.moisture = 0

        if self.alive is False:
            self.show
            return
        else:
            self.growth_speed = self.base_growth
            if temp > self.heat_res:
                if temp - self.heat_res >= 10:
                    self.alive = False
                    self.show
                    return
                else:
                    self.growth_speed *= (1 - ((temp - self.heat_res) / 10))

            if temp < self.cold_res:
                self.alive = False
                self.show
                return
            if temp == 9:
                self.growth_speed *= 0.9
            elif temp == 8:
                self.growth_speed *= 0.8
            elif temp == 7:
                self.growth_speed *= 0.7
            elif temp == 6:
                self.growth_speed *= 0.6
            elif temp == 5:
                self.growth_speed *= 0.5
            elif temp == 4:
                self.growth_speed *= 0.4
            elif temp == 3:
                self.growth_speed *= 0.3
            elif temp == 2:
                self.growth_speed *= 0.2
            elif temp == 1:
                self.growth_speed *= 0.1
            elif temp <= 0:
                self.growth_speed = 0

            self.grow
