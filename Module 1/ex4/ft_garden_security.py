# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/06 07:29:33 by ccolnat         #+#    #+#               #
#  Updated: 2026/05/06 11:52:51 by ccolnat         ###   ########.fr        #
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
    elif soil == 2:
        return "medium fertility soil"
    elif soil == 3:
        return "high fertility soil  "
    else:
        print(f"{Y}Invalid value, setting to default value{RESET}")
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
        return "Spelt", 110, 0.80, -5, 30
    elif variety == 5:
        return "Turnip", 35, 0.64, -5, 17
    elif variety == 6:
        return "Parsnip", 50, 0.45, -10,  22
    elif variety == 7:
        return "Rice", 110, 0.80, 8, 36
    elif variety == 8:
        return "Rye", 135, 0.90, -12, 17
    elif variety == 9:
        return "Soybean", 80, 0.80, -5, 30
    elif variety == 10:
        return "Amaranth", 125, 1.20, 6, 32
    elif variety == 11:
        return "Bell Pepper", 75, 0.94, 8, 24
    elif variety == 12:
        return "Cassava", 225, 0.80, 4, 34
    elif variety == 13:
        return "Peanut", 40, 0.30, 10, 32
    elif variety == 14:
        return "Pineapple", 105, 0.20, 6, 38
    elif variety == 15:
        return "Sunflower", 225, 2.20, -5, 30
    elif variety == 16:
        return "Pumpkin", 45, 0.43, -5, 30
    elif variety == 17:
        return "Cabbage", 50, 0.55, -5, 25
    else:
        return "Dragon Fruit", 200, 0.80, 0, 28


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

        self._soil_type: str = soil_type_database(soil_type)
        """
        **The soil type**
        - Affect the base growth speed

        *(can be low, medium or high fertility soil)*
        """
        self._size: float = 1
        """
        **The size of the vegetable**

        *(Expressed in cm)*
        """
        self._plant_age: int = 0
        """
        **The age of the plant**
        - Plants stop aging if dead or fully grown

        *(Expressed in days)*


        """
        self._alive: bool = True
        """
        **State of the plant**

        *(Alive or Dead)*
        """
        self._moisture: int = 50
        """
        **Humidity level of the soil**

        *(affect grow speed)*
        """
        self._growth_speed: float = 0
        """
        **Real growth speed**
        - Affected by temperature and moisture

        *Extreme temperatures can kill plants*
        """
        self._temp: float = 20
        """
        **Temperature of the day**

        *(expressed in °C)*
        """
        self._old_temp: float = 20
        """
        **Temperature of the previous day**

        *(expressed in °C)*
        """

    def raining(self, rain: bool) -> None:
        """
        **Method to change the wether**
        - If True, will increase the humidity of 42%
        - If False, will decrease the humidity of 8%
        """
        if rain:
            self._moisture += 42
            if self._moisture > 100:
                self._moisture = 100
        elif not rain:
            self._moisture -= 8
            if self._moisture < 0:
                self._moisture = 0

    @property
    def get_temp(self) -> float:
        """
        Allows outside code to READ the temp safely.
        """
        return self._temp

    @property
    def get_soil(self) -> str:
        """
        Allows outside code to READ the soil type safely.
        """
        return self._soil_type

    @get_soil.setter
    def set_soil(self, type: int) -> None:
        """
        Validates the input before updating the soil.
        """
        self._soil_type: str = soil_type_database(type)


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
        self._name: str
        """
        **The name of the vegetable**
        """
        self._max_size: float
        """
        **The size required to consider the vegetable mature**
        """
        self._base_growth: float
        """
        **Base growth speed**

        - Expressed in cm per day.

        - Base growth speed only change depending on the soil type.
        """
        self._heat_res: int
        """
        **Heat res**

        - Expressed in degrees celucius.

        - Plant can grow normally until temp reach that value.

        - For any degree above the res value plant lose 10% growth speed.

        - If temp reach 10 degrees above the res, plant dies.
        """
        self._cold_res: int
        """
        **Cold res**

        - Expressed in degrees celcius.

        - For any degree below 10, all plants lose 10% growth speed.

        - If temp reach that value, the plant dies.
        """

        (
            self._name,
            self._max_size,
            self._base_growth,
            self._cold_res,
            self._heat_res
        ) = vegetable_database(variety)
        print(f"{Y}{self._name} was created succesfully ! {RESET}")

        Vegetable.update_plant(self)

    @property
    def get_height(self) -> float:
        """
        Allows outside code to READ the size safely.
        """
        return self._size

    @get_height.setter
    def set_height(self, height: float) -> None:
        """
        Validates the input before updating the height.
        """
        if height > self._max_size:
            print(f"{R}Error, value higher than the maximum height")
            print(f"{Y}Height unchanged: ({self._size} cm){RESET}")
            return
        elif height < 0:
            print(f"{Y}Warning, negative value,", end=" ")
            print(f"setting height to minimum instead{RESET}")

            self._size = 1
            return
        else:
            self._size = height

    @property
    def get_age(self) -> int:
        """
        Allows outside code to READ the age safely.
        """
        return self._plant_age

    @get_age.setter
    def set_age(self, age: int) -> None:
        """
        Validates the input before updating age.
        """
        if age > 360:
            raise (ValueError)
        elif age < 0:
            self._plant_age = 0
        else:
            self._plant_age = age

    def age(self) -> None:
        """
        **Method to age the plant**

        *Wont age the plant if it's dead or fully grown*
        """
        if self._alive and self._size != self._max_size:
            self._plant_age += 1

    def show(self) -> None:
        """
        **Method to show the daily change of the plant**
        """
        if self._size == self._max_size:
            return
        if not self._alive:
            return
        else:
            print(" _______________________________")
            print(f"|Day: {self._plant_age:2} | {self._name:12} is ", end="")
            print(f"{G}Alive{RESET}|")

        print("|________|______________________|_____________________", end="")
        print("____________________")
        if self._growth_speed >= self._base_growth:
            print(f"|Size: {self._size:6.2f} cm | Growth: ", end="")
            print(f"{G}{self._growth_speed:.2f}{RESET} cm/day |", end="")
        else:
            print(f"|Size: {self._size:6.2f} cm | Growth: ", end="")
            print(f"{R}{self._growth_speed:.2f}{RESET} cm/day |", end="")

        if self._old_temp < self._temp:
            print(f" Temp is: {Y}⬈ ", end="")
        elif self._old_temp == self._temp:
            print(" Temp is: ⭢ ", end="")
        elif self._old_temp > self._temp:
            print(f" Temp is: {B}⬊ ", end="")
        print(f"{self._temp:2}{RESET}°C |", end=" ")

        if 0 <= self._moisture < 25:
            print(f"Humidity: {R}{self._moisture:3}{RESET}% |")
        elif 25 <= self._moisture < 50:
            print(f"Humidity: {Y}{self._moisture:3}{RESET}% |")
        elif 50 <= self._moisture < 75:
            print(f"Humidity: {B}{self._moisture:3}{RESET}% |")
        elif 75 <= self._moisture <= 100:
            print(f"Humidity: {G}{self._moisture:3}{RESET}% |")
        print("|________________|_____________________|______________", end="")
        print("___|________________|")

    def show_detailed(self) -> None:
        """
        **Method to show all the summary of the plant growth**
        """
        print("--------------------------------------------------------------")
        if not self._alive:
            print(f"{self._name} {R}died{RESET} on day ", end="")
            print(f"{self._plant_age} at {R}", end="")
            print(f"{(self._size / self._max_size * 100):.2f}", end="")
            print(f"{RESET} % maturity ({self._size:.2f} cm)")
            return
        print(f"State : {G}Alive{RESET}")
        print(f"Variety : {B}{self._name}{RESET}")

        if self._soil_type == "low fertility soil   ":
            print(f"Planted in : {Y}{self._soil_type}{RESET}")
        elif self._soil_type == "high fertility soil  ":
            print(f"Planted in : {G}{self._soil_type}{RESET}")
        else:
            print(f"Planted in : {B}{self._soil_type}{RESET}")
        print(f"Age : {self._plant_age} days")
        print(f"Size : {self._size:.2f} cm")
        if self._size == self._max_size:
            print(f"Maturity: {G}{(self._size / self._max_size * 100):.2f}%")
            print(f"{RESET}")
        else:
            print(f"Maturity: {Y}{(self._size / self._max_size * 100):.2f}%")
            print(f"{RESET}")

        print(f"Base growth speed : {self._base_growth:.2f}cm per day")
        print(f"Current growth speed : {self._growth_speed:.2f}cm per day")
        print(f"Cold res down to: {self._cold_res}°C")
        print(f"Heat res up to: {self._heat_res}°C")

    def grow(self) -> None:
        """
        **Method to grow the plant**
        - Prints a message when fully grown

        *Wont grow the plant if it's fully grown already*
        """
        if self._size == self._max_size:
            return
        if self._size < self._max_size:
            self._size += self._growth_speed
            if self._size > self._max_size:
                self._size = self._max_size
                print(f"{G}{self._name} is fully grown after", end="")
                print(f" {self._plant_age} days !{RESET}")

    def change_temp(self, temp: float) -> None:
        """
        **Method to change the temperature**
        """
        if 5500 > temp >= 60:
            print(f"{R}Invalid temp: ({temp}°C), too high{RESET}", end=" ")
            print("Damn, climate change goes hard today")
            print(f"{Y}Temperature unchanged ({self._temp}°C){RESET}")
            return
        elif temp >= 5500:
            print(f"{R}Invalid temp:{RESET}", end=" ")
            print("Hotter that the sun, kinda too hot for plants", end=" ")
            print("isn't it?")
            print(f"{Y}Temperature unchanged ({self._temp}°C){RESET}")
            return

        elif -273.15 <= temp <= -60:
            print(f"{R}Invalid temp: ({temp}°C), too low{RESET}", end=" ")
            print("You may need to turn the heater On")
            print(f"{Y}Temperature unchanged ({self._temp}°C){RESET}")
        elif temp < -273.15:
            print(f"{R}Invalid temp:{RESET}", end=" ")
            print("Colder than the laws of physics, damn")
            print(f"{Y}Temperature unchanged ({self._temp}°C){RESET}")
            return

        else:
            self._old_temp = self._temp
            self._temp = temp

    def update_plant(self) -> None:
        """
        **Method to update the growth speed of the plant**
        - Do nothing if the plant is fully grown or dead
        - Apply buffs of malus for humidity level
        - Apply buffs of malus for temperature

        *Also kill the plant if temeratures are above or below plant
        resistances*
        """
        if not self._alive:
            return
        if self._size == self._max_size:
            return
        print(f"{Y}{self._name} was updated succesfully ! {RESET}")
        self._growth_speed = self._base_growth

        if 0 <= self._moisture < 25:
            self._growth_speed *= 0.5
        elif 25 <= self._moisture < 50:
            self._growth_speed *= 0.8
        elif 50 <= self._moisture < 75:
            self._growth_speed *= 1.2
        elif 75 <= self._moisture <= 100:
            self._growth_speed *= 1.5

        if self._temp > self._heat_res:
            if self._temp - self._heat_res >= 10:
                self._alive = False
                self._growth_speed = 0
                print(f"{R}{self._name} has grown {self._size:.2f} cm", end="")
                print("and died from the heat after {self._plant_age} days")
                print(f"{RESET}")
                return
            else:
                self._growth_speed *= (1 - (self._temp - self._heat_res) / 10)

        if self._temp < self._cold_res:
            self._alive = False
            self._growth_speed = 0
            print(f"{R}{self._name} has grown {self._size:.2f} cm", end="")
            print("and died from the cold after {self._plant_age} days{RESET}")
            return
        if self._temp < 0:
            self._growth_speed = 0
        if 0 <= self._temp <= 9:
            self._growth_speed *= self._temp / 10


if __name__ == "__main__":
    import random
    temp: int
    is_raining: int
    temp = random.randint(15, 30)
    print(f"{Y}--------------------{RESET}")
    print(f"{Y}--Starting testing--{RESET}")
    print(f"{Y}--------------------{RESET}")

    plant_01 = Vegetable(1, 1)
    plant_02 = Vegetable(1, 2)
    plant_03 = Vegetable(1, 3)
    plant_04 = Vegetable(1, 4)
    print(f"{Y}--------------------{RESET}")

    test = plant_01.get_soil
    print(f"plant_01 : {test}")
    test = plant_02.get_soil
    print(f"plant_02 : {test}")
    test = plant_03.get_soil
    print(f"plant_03 : {test}")
    test = plant_04.get_soil
    print(f"plant_04 : {test}")
    print(f"{Y}-------------------------{RESET}")
    test = plant_01.get_temp
    print(f"plant_01 : {test}°C")
    test = plant_02.get_temp
    print(f"plant_02 : {test}°C")
    test = plant_03.get_temp
    print(f"plant_03 : {test}°C")
    test = plant_04.get_temp
    print(f"plant_04 : {test}°C")
    print(f"{Y}-------------------------{RESET}")
    test = plant_01.get_height
    print(f"plant_01 : {test} cm")
    test = plant_02.get_height
    print(f"plant_02 : {test} cm")
    test = plant_03.get_height
    print(f"plant_03 : {test} cm")
    test = plant_04.get_height
    print(f"plant_04 : {test} cm")

    print(f"{Y}-------------------------{RESET}")
    print(f"{Y}---Upgrading soil type---{RESET}")
    print(f"{Y}-------------------------{RESET}")

    plant_01.set_soil = 3
    test = plant_01.get_soil
    print(f"plant_01 : {test}")
    plant_02.set_soil = 3
    test = plant_02.get_soil
    print(f"plant_02 : {test}")
    plant_03.set_soil = (42000000)
    test = plant_03.get_soil
    print(f"plant_03 : {test}")
    plant_04.set_soil = (-100000)
    test = plant_04.get_soil
    print(f"plant_04 : {test}")

    print(f"{Y}-------------------------{RESET}")
    print(f"{Y}------Changing temp------{RESET}")
    print(f"{Y}-------------------------{RESET}")

    Vegetable.change_temp(plant_01, -60)
    Vegetable.change_temp(plant_02, 72)
    Vegetable.change_temp(plant_03, -2000000)
    Vegetable.change_temp(plant_04, 42000000)

    print(f"{Y}-------------------------{RESET}")
    print(f"{Y}-----Re-Changing temp----{RESET}")
    print(f"{Y}-------------------------{RESET}")

    Vegetable.change_temp(plant_01, -14)
    Vegetable.change_temp(plant_02, 14)
    Vegetable.change_temp(plant_03, 42)
    Vegetable.change_temp(plant_04, -42)

    test = plant_01.get_temp
    print(f"plant_01 : {test}°C")
    test = plant_02.get_temp
    print(f"plant_02 :  {test}°C")
    test = plant_03.get_temp
    print(f"plant_03 :  {test}°C")
    test = plant_04.get_temp
    print(f"plant_04 : {test}°C")

    print(f"{Y}-------------------------{RESET}")
    print(f"{Y}-----Changing height-----{RESET}")
    print(f"{Y}-------------------------{RESET}")

    plant_01.set_height = 3
    test = plant_01.get_height
    print(f"plant_01 : {test} cm")
    plant_02.set_height = 42
    test = plant_02.get_height
    print(f"plant_02 : {test} cm")
    plant_03.set_height = 31
    test = plant_03.get_height
    print(f"plant_03 : {test} cm")
    plant_04.set_height = 97
    test = plant_04.get_height
    print(f"plant_04 : {test} cm")

    print(f"{Y}-------------------------{RESET}")
    print(f"{Y}----Re-Changing height---{RESET}")
    print(f"{Y}-------------------------{RESET}")

    plant_01.set_height = 25
    test = plant_01.get_height
    print(f"plant_01 : {test} cm")
    plant_02.set_height = 72
    test = plant_02.get_height
    print(f"plant_02 : {test} cm")
    plant_03.set_height = (42000000)
    test = plant_03.get_height
    print(f"plant_03 : {test} cm")
    plant_04.set_height = (-100000)
    test = plant_04.get_height
    print(f"plant_04 : {test} cm")
