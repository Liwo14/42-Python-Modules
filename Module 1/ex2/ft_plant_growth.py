# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/30 08:43:34 by ccolnat         #+#    #+#               #
#  Updated: 2026/05/06 07:54:12 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

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
        return "Carrot", 25, 0.33, -10, 22
    elif variety == 2:
        return "Flax", 80, 0.84, -5, 30
    elif variety == 3:
        return "Onion", 40, 0.38, -1, 30
    elif variety == 4:
        return "Spelt", 11, 0.80, -5, 30
    elif variety == 5:
        return "Turnip", 35, 0.64, -5, 17
    elif variety == 6:
        return "Parsnip", 50, 0.45, -10,  22
    elif variety == 7:
        return "Rice", 11, 0.80, 8, 36
    elif variety == 8:
        return "Rye", 13, 0.90, -12, 17
    elif variety == 9:
        return "Soybean", 80, 0.80, -5, 30
    elif variety == 10:
        return "Amaranth", 12, 1.20, 6, 32
    elif variety == 11:
        return "Bell Pepper", 75, 0.94, 8, 24
    elif variety == 12:
        return "Cassava", 22, 0.80, 4, 34
    elif variety == 13:
        return "Peanut", 40, 0.30, 10, 32
    elif variety == 14:
        return "Pineapple", 10, 0.20, 6, 38
    elif variety == 15:
        return "Sunflower", 22, 2.20, -5, 30
    elif variety == 16:
        return "Pumpkin", 45, 0.43, -5, 30
    elif variety == 17:
        return "Cabbage", 50, 0.55, -5, 25
    else:
        return "Dragon Fruit", 20, 0.80, 0, 28


class Plant:
    """
    **This is the blueprint for a Plant**
    - Need a soil type:
        - Int 1 for low fertility soil
        - Int 2 for medium fertility soil
        - Int 3 for high fertility soil

    *(will default on medium if any other value is provided)*
    """
    def __init__(
        self,
        soil_type: int
    ) -> None:

        self.soil_type: str = soil_type_database(soil_type)
        """
        **The soil type**
        - Affect the base growth speed

        *(can be low, medium or high fertility soil)*
        """
        self.size: float = 1
        """
        **The size of the vegetable**

        *(Expressed in cm)*
        """
        self.plant_age: int = 0
        """
        **The age of the plant**
        - Plants stop aging if dead or fully grown

        *(Expressed in days)*


        """
        self.alive: bool = True
        """
        **State of the plant**

        *(Alive or Dead)*
        """
        self.moisture: int = 50
        """
        **Humidity level of the soil**

        *(affect grow speed)*
        """
        self.growth_speed: float = 0
        """
        **Real growth speed**
        - Affected by temperature and moisture

        *Extreme temperatures can kill plants*
        """
        self.temp: float = 20
        """
        **Temperature of the day**

        *(expressed in °C)*
        """
        self.old_temp: float = 20
        """
        **Temperature of the previous day**

        *(expressed in °C)*
        """

    def raining(self, rain: bool):
        """
        **Method to change the wether**
        - If True, will increase the humidity of 42%
        - If False, will decrease the humidity of 8%
        """
        if rain:
            self.moisture += 42
            if self.moisture > 100:
                self.moisture = 100
        elif not rain:
            self.moisture -= 8
            if self.moisture < 0:
                self.moisture = 0


class Vegetable(Plant):
    """
    **This is the blueprint for a vegetable**
    - Need a soil type:
        - Int 1 for low fertility soil
        - Int 2 for medium fertility soil
        - Int 3 for high fertility soil
        *(will default on medium if any other value is provided)*
    - Need the vegetable variety
        - Int 1 up to 18
        *(will default on 18 (Dragon Fruit) if any other value is provided)*


    """
    def __init__(
        self,
        soil_type: int,
        variety: int
    ) -> None:

        Plant.__init__(self, soil_type)
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

        - Base growth speed only change depending on the soil type.
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
        print(f"{Y}{self.name} was created succesfully ! {RESET}")

        if self.soil_type == "low fertility soil   ":
            self.base_growth = self.base_growth * 0.8
        elif self.soil_type == "high fertility soil  ":
            self.base_growth = self.base_growth * 1.2

    def age(self):
        """
        **Method to age the plant**

        *Wont age the plant if it's dead or fully grown*
        """
        if self.alive and self.size != self.mature_size:
            self.plant_age += 1

    def show(self):
        """
        **Method to show the daily change of the plant**
        """
        if self.size == self.mature_size:
            return
        if not self.alive:
            return
        else:
            print(" _______________________________")
            print(f"|Day: {self.plant_age:2} | {self.name:12} is ", end="")
            print(f"{G}Alive{RESET}|")

        print("|________|______________________|_____________________", end="")
        print("____________________")
        if self.growth_speed >= self.base_growth:
            print(f"|Size: {self.size:6.2f} cm | Growth: ", end="")
            print(f"{G}{self.growth_speed:.2f}{RESET} cm/day |", end="")
        else:
            print(f"|Size: {self.size:6.2f} cm | Growth: ", end="")
            print(f"{R}{self.growth_speed:.2f}{RESET} cm/day |", end="")

        if self.old_temp < self.temp:
            print(f" Temp is: {Y}⬈ ", end="")
        elif self.old_temp == self.temp:
            print(" Temp is: ⭢ ", end="")
        elif self.old_temp > self.temp:
            print(f" Temp is: {B}⬊ ", end="")
        print(f"{self.temp:2}{RESET}°C |", end=" ")

        if 0 <= self.moisture < 25:
            print(f"Humidity: {R}{self.moisture:3}{RESET}% |")
        elif 25 <= self.moisture < 50:
            print(f"Humidity: {Y}{self.moisture:3}{RESET}% |")
        elif 50 <= self.moisture < 75:
            print(f"Humidity: {B}{self.moisture:3}{RESET}% |")
        elif 75 <= self.moisture <= 100:
            print(f"Humidity: {G}{self.moisture:3}{RESET}% |")
        print("|________________|_____________________|______________", end="")
        print("___|________________|")

    def show_detailed(self):
        """
        **Method to show all the summary of the plant growth**
        """
        print("--------------------------------------------------------------")
        if not self.alive:
            print(f"{self.name} {R}died{RESET} on day ", end="")
            print(f"{self.plant_age} at {R}", end="")
            print(f"{(self.size / self.mature_size * 100):.2f}", end="")
            print(f"{RESET} % maturity ({self.size:.2f} cm)")
            return
        print(f"State : {G}Alive{RESET}")
        print(f"Variety : {B}{self.name}{RESET}")

        if self.soil_type == "low fertility soil   ":
            print(f"Planted in : {Y}{self.soil_type}{RESET}")
        elif self.soil_type == "high fertility soil  ":
            print(f"Planted in : {G}{self.soil_type}{RESET}")
        else:
            print(f"Planted in : {B}{self.soil_type}{RESET}")
        print(f"Age : {self.plant_age} days")
        print(f"Size : {self.size:.2f} cm")
        if self.size == self.mature_size:
            print(f"Maturity : {G}{(self.size / self.mature_size * 100):.2f}%")
            print(f"{RESET}")
        else:
            print(f"Maturity : {Y}{(self.size / self.mature_size * 100):.2f}%")
            print(f"{RESET}")

        print(f"Base growth speed : {self.base_growth:.2f}cm per day")
        print(f"Current growth speed : {self.growth_speed:.2f}cm per day")
        print(f"Cold res down to: {self.cold_res}°C")
        print(f"Heat res up to: {self.heat_res}°C")

    def grow(self):
        """
        **Method to grow the plant**
        - Prints a message when fully grown

        *Wont grow the plant if it's fully grown already*
        """
        if self.size == self.mature_size:
            return
        if self.size < self.mature_size:
            self.size += self.growth_speed
            if self.size > self.mature_size:
                self.size = self.mature_size
                print(f"{G}{self.name} is fully grown after", end="")
                print(f" {self.plant_age} days !{RESET}")

    def change_temp(self, temp: float):
        """
        **Method to change the temperature**
        """
        if 5500 > temp >= 60:
            print("Damn, climate change goes hard today")
            print(f"{R}Invalid temp, too high{RESET}")
            return
        elif temp >= 5500:
            print("Hotter that the sun, kinda too much for plants isn't it ?")
            print(f"{R}Invalid temp, too high{RESET}")
            return

        if -273.15 <= temp <= -100:
            print("You may need to turn the heater On")
            print(f"{R}Invalid temp, too low{RESET}")
        elif temp < -273.15:
            print("Colder than the laws of physics, damn")
            print(f"{R}Invalid temp, too low{RESET}")
            return

        self.old_temp = self.temp
        self.temp = temp

    def update_plant(self):
        """
        **Method to update the growth speed of the plant**
        - Do nothing if the plant is fully grown or dead
        - Apply buffs of malus for humidity level
        - Apply buffs of malus for temperature

        *Also kill the plant if temeratures are above or below plant
        resistances*
        """
        if not self.alive:
            return
        if self.size == self.mature_size:
            return
        print(f"{Y}{self.name} was updated succesfully ! {RESET}")
        self.growth_speed = self.base_growth

        if 0 <= self.moisture < 25:
            self.growth_speed *= 0.5
        elif 25 <= self.moisture < 50:
            self.growth_speed *= 0.8
        elif 50 <= self.moisture < 75:
            self.growth_speed *= 1.2
        elif 75 <= self.moisture <= 100:
            self.growth_speed *= 1.5

        if self.temp > self.heat_res:
            if self.temp - self.heat_res >= 10:
                self.alive = False
                self.growth_speed = 0
                print(f"{R}{self.name} has grown {self.size:.2f} cm", end="")
                print("and died from the heat after {self.plant_age} days")
                print(f"{RESET}")
                return
            else:
                self.growth_speed *= (1 - ((self.temp - self.heat_res) / 10))

        if self.temp < self.cold_res:
            self.alive = False
            self.growth_speed = 0
            print(f"{R}{self.name} has grown {self.size:.2f} cm", end="")
            print("and died from the cold after {self.plant_age} days{RESET}")
            return
        if self.temp < 0:
            self.growth_speed = 0
        if 0 <= self.temp <= 9:
            self.growth_speed *= self.temp / 10


if __name__ == "__main__":
    import random
    temp: int
    is_raining: int
    temp = random.randint(15, 30)
    print(f"{Y}--------------------{RESET}")
    print(f"{Y}Starting simulation{RESET}")
    print(f"{Y}--------------------{RESET}")

    print(f"{Y}Starting temp: {temp}°C{RESET}")
    print(f"{Y}--------------------{RESET}")
    plant_1 = Vegetable(random.randint(1, 3), random.randint(1, 18))
    plant_2 = Vegetable(random.randint(1, 3), random.randint(1, 18))
    plant_3 = Vegetable(random.randint(1, 3), random.randint(1, 18))
    plant_4 = Vegetable(random.randint(1, 3), random.randint(1, 18))
    print(f"{Y}--------------------{RESET}")

    Vegetable.update_plant(plant_1)
    Vegetable.update_plant(plant_2)
    Vegetable.update_plant(plant_3)
    Vegetable.update_plant(plant_4)
    print(f"{Y}--------------------{RESET}")

    Vegetable.show_detailed(plant_1)
    Vegetable.show_detailed(plant_2)
    Vegetable.show_detailed(plant_3)
    Vegetable.show_detailed(plant_4)

    nb_of_days: int = 0
    while (nb_of_days < 7):
        temp += random.randint(-2, 2)
        is_raining = random.randint(0, 4)

        Vegetable.change_temp(plant_1, temp)
        Vegetable.change_temp(plant_2, temp)
        Vegetable.change_temp(plant_3, temp)
        Vegetable.change_temp(plant_4, temp)

        if is_raining == 0:
            print(f"{B}It's raining today !{RESET}")
            Vegetable.raining(plant_1, True)
            Vegetable.raining(plant_2, True)
            Vegetable.raining(plant_3, True)
            Vegetable.raining(plant_4, True)
        else:
            Vegetable.raining(plant_1, False)
            Vegetable.raining(plant_2, False)
            Vegetable.raining(plant_3, False)
            Vegetable.raining(plant_4, False)

        Vegetable.grow(plant_1)
        Vegetable.grow(plant_2)
        Vegetable.grow(plant_3)
        Vegetable.grow(plant_4)

        Vegetable.age(plant_1)
        Vegetable.age(plant_2)
        Vegetable.age(plant_3)
        Vegetable.age(plant_4)

        Vegetable.show(plant_1)
        Vegetable.show(plant_2)
        Vegetable.show(plant_3)
        Vegetable.show(plant_4)

        Vegetable.update_plant(plant_1)
        Vegetable.update_plant(plant_2)
        Vegetable.update_plant(plant_3)
        Vegetable.update_plant(plant_4)
        nb_of_days += 1

    print("--------------------------Summary-----------------------------")
    Vegetable.show_detailed(plant_1)
    Vegetable.show_detailed(plant_2)
    Vegetable.show_detailed(plant_3)
    Vegetable.show_detailed(plant_4)
    print("------------------------------------------------------------------")
