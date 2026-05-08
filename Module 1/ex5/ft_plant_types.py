# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/06 11:57:07 by ccolnat         #+#    #+#               #
#  Updated: 2026/05/08 12:57:52 by ccolnat         ###   ########.fr        #
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


def vegetable_database(variety: int) -> tuple[
        str,
        float,
        float,
        int,
        int,
        float]:
    """
    **Takes an int (1 up to 18)**

    **Returns a turple for each vegetable variety in the form of :**
    - Name (str)
    - Mature height (float)
    - Base growth speed (float)
    - Cold resistance (int)
    - Heat resistane (int)
    - Max Nutritional Value

    *If input is outside range, will default on Dragon fruit.*
    """
    if variety == 1:
        return "Carrot", 25, 0.33, -10, 22, 100
    elif variety == 2:
        return "Flax", 80, 0.84, -5, 30, 30
    elif variety == 3:
        return "Onion", 40, 0.38, -1, 30, 100
    elif variety == 4:
        return "Spelt", 110, 0.80, -5, 30, 60
    elif variety == 5:
        return "Turnip", 35, 0.64, -5, 17, 100
    elif variety == 6:
        return "Parsnip", 50, 0.45, -10, 22, 100
    elif variety == 7:
        return "Rice", 110, 0.80, 8, 36, 60
    elif variety == 8:
        return "Rye", 135, 0.90, -12, 17, 60
    elif variety == 9:
        return "Soybean", 80, 0.80, -5, 30, 150
    elif variety == 10:
        return "Amaranth", 125, 1.20, 6, 32, 60
    elif variety == 11:
        return "Bell Pepper", 75, 0.94, 8, 24, 50
    elif variety == 12:
        return "Cassava", 225, 0.80, 4, 34, 100
    elif variety == 13:
        return "Peanut", 40, 0.30, 10, 32, 160
    elif variety == 14:
        return "Pineapple", 105, 0.20, 6, 38, 320
    elif variety == 15:
        return "Sunflower", 225, 2.20, -5, 30, 60
    elif variety == 16:
        return "Pumpkin", 45, 0.43, -5, 30, 480
    elif variety == 17:
        return "Cabbage", 50, 0.55, -5, 25, 300
    else:
        return "Dragon Fruit", 200, 0.80, 0, 28, 280


def tree_database(variety: int) -> tuple[str, float, float, float, float]:
    """
    **Takes an int (1 up to 12)**

    **Returns a turple for each tree variety in the form of :**
    - Name (str)
    - Max height (float)
    - Base height growth speed (float)
    - Base diameter growth speed (float)
    - Base shade growth per day (float)

    *If input is outside range, will default on Walnut.*
    """
    if variety == 1:
        return "Acacia", 3000, 0.25, 0.003, 0.15
    elif variety == 2:
        return "Cypress", 4000, 0.15, 0.004, 0.08
    elif variety == 3:
        return "Birch", 3000, 0.20, 0.003, 0.10
    elif variety == 4:
        return "Ebony", 3000, 0.05, 0.001, 0.02
    elif variety == 5:
        return "Kapok", 7300, 0.40, 0.010, 0.35
    elif variety == 6:
        return "Larch", 5000, 0.15, 0.003, 0.05
    elif variety == 7:
        return "Maple", 4500, 0.15, 0.003, 0.15
    elif variety == 8:
        return "Oak", 4000, 0.10, 0.005, 0.25
    elif variety == 9:
        return "Pine", 8000, 0.18, 0.003, 0.06
    elif variety == 10:
        return "Purpleheart", 5000, 0.12, 0.003, 0.12
    elif variety == 11:
        return "Redwood", 11600, 0.25, 0.010, 0.15
    else:
        return "Walnut", 4000, 0.15, 0.004, 0.20


def flower_database(variety: int) -> tuple[str, str, float, float, int]:
    """
    **Takes an int (1 up to 10)**

    **Returns a turple for each flower variety in the form of :**
    - Name (str)
    - Color (str)
    - Max height (float)
    - Base height growth speed (float)
    - Blooming temperature (int)

    *If input is outside range, will default on while Edleweiss.*
    """
    if variety == 1:
        return "Heather", "Purple", 60, 0.15, 14
    if variety == 2:
        return "Heather", "Pink", 60, 0.15, 14
    elif variety == 3:
        return "Lupine", "Blue", 120, 1.00, 16
    elif variety == 4:
        return "Lupine", "Purple", 120, 1.00, 16
    elif variety == 5:
        return "Lupine", "Pink", 120, 1.00, 16
    elif variety == 6:
        return "Foxglove", "Purple", 150, 1.20, 19
    elif variety == 7:
        return "Foxglove", "Pink", 150, 1.20, 19
    elif variety == 8:
        return "Foxglove", "White", 150, 1.20, 19
    elif variety == 9:
        return "Goldenrod", "Yellow", 100, 0.80, 22
    else:
        return "Edleweiss", "White", 20, 0.20, 10


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

        self._name: str
        """
        **The name of the vegetable**
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
        self._soil_type: str = soil_type_database(soil_type)
        """
        **The soil type**
        - Affect the base growth speed

        *(can be low, medium or high fertility soil)*
        """
        self._size: float
        """
        **The size of the vegetable**

        *(Expressed in cm)*
        """
        self._max_size: float
        """
        **The size required to consider the vegetable mature**

        *(Expressed in cm)*
        """
        self._base_growth: float
        """
        **Base growth speed**

        - Expressed in cm per day.

        - Base growth speed only change depending on the soil type.
        """
        self._growth_speed: float
        """
        **Real growth speed**
        - Affected by temperature and moisture

        *Extreme temperatures can kill plants*
        """
        self._moisture: int = 50
        """
        **Humidity level of the soil**

        *(affect grow speed)*
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

        if self._soil_type == "low fertility soil   ":
            self._base_growth *= 0.8
        elif self._soil_type == "high fertility soil  ":
            self._base_growth *= 1.2

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
            print(f"{R}Age too big{RESET}")
            print(f"{Y}Age unchanged ({self._plant_age}) days")
            return
        elif age < 0:
            print(f"{Y}Warning: value of new age is negative{RESET}")
            print(f"{Y}Age set to 0 instead {RESET}")
            self._plant_age = 0
        else:
            self._plant_age = age

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
        if height >= 100:
            print(f"{R}Error, value too high")
            print(f"{Y}Height unchanged: ({self._size} cm){RESET}")
            return
        elif height < 0:
            print(f"{Y}Warning, negative value,", end=" ")
            print(f"setting height to minimum instead{RESET}")

            self._size = 1
            return
        else:
            self._size = height

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

    def update_plant(self) -> None:
        """
        **Method to update the growth speed of the plant**
        - Do nothing if the plant is fully grown or dead
        - Apply buffs of malus for humidity level
        """
        if not self._alive:
            return
        if self._size == self._max_size:
            return
        self._growth_speed = self._base_growth

        if 0 <= self._moisture < 25:
            self._growth_speed *= 0.5
        elif 25 <= self._moisture < 50:
            self._growth_speed *= 0.8
        elif 50 <= self._moisture < 75:
            self._growth_speed *= 1.2
        elif 75 <= self._moisture <= 100:
            self._growth_speed *= 1.5

        print(f"{Y}{self._name} was updated succesfully ! {RESET}")


class Tree(Plant):
    """
    **This is the blueprint for a tree**
    - Need a soil type:
        - Int 1 for low fertility soil
        - Int 2 for medium fertility soil
        - Int 3 for high fertility soil
        *(will default on medium if any other value is provided)*
    - Need the tree variety
        - Int 1 up to 12
        *(will default on 12 (Walnut) if any other value is provided)*
    """
    def __init__(
        self,
        soil_type: int,
        variety: int
    ) -> None:

        self._diam: float

        self._base_diam_growth: float
        """
        **Base diamerter growth speed**

        - Expressed in cm per day.

        - Base growth speed only change depending on the soil type.
        """
        self._shade_base
        """
        **Basde shade of a tree**
        """
        self._shade: float
        """
        **Value of the shade area of the tree**
        - expressed in cm²

        *(Height * Diameter) + (Diameter + Base shade) * Age*
        """

        super().__init__(soil_type)

        if self._soil_type == "low fertility soil   ":
            self._base_diam_growth *= 0.8
        elif self._soil_type == "high fertility soil  ":
            self._base_diam_growth *= 1.2

        (
            self._name,
            self._max_size,
            self._base_growth,
            self._base_diam_growth,
            self._shade_base
        ) = tree_database(variety)
        print(f"{Y}{self._name} was created succesfully ! {RESET}")

        Tree.update_tree(self)

    def update_tree(self) -> None:
        """
        **Method to update the growth speed of the tree**
        - Do the usual update by super() calling update_Plant method
        - Additionally update trunk growth speed and shade area
        """

        self._shade = ((self._size * self._diam) +
                       ((self._diam * self._shade_base) * self._plant_age))

        if 0 <= self._moisture < 25:
            self._base_diam_growth *= 0.9
        elif 25 <= self._moisture < 50:
            self._base_diam_growth *= 1.1
        elif 50 <= self._moisture < 75:
            self._base_diam_growth *= 1.2
        elif 75 <= self._moisture <= 100:
            self._base_diam_growth *= 1.3
        super().update_plant

    def grow_tree(self) -> None:
        """
        Grow the tree
        """
        super().grow
        if self._size == self._max_size:
            return
        if self._size < self._max_size:
            self._diam += self._base_diam_growth


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
        self._nutrition_value: float = 0
        """
        **Nutritional Value of the vegetable**

        - Represent the current nutrional value of the vegetable
        """
        self._max_nutrition_value: float
        """
        **Nutritional Value of the vegetable**

        - Represent the nutrional value of the vegetable when fully grown
        """

        super().__init__(soil_type)

        (
            self._name,
            self._max_size,
            self._base_growth,
            self._cold_res,
            self._heat_res,
            self._max_nutrition_value
        ) = vegetable_database(variety)
        print(f"{Y}{self._name} was created succesfully ! {RESET}")

        Vegetable.update_vegetable(self)

    def update_vegetable(self) -> None:
        """
        **Method to update the growth speed of the vegetable**
        - Do the usual update by super() calling update_Plant method
        - Additionally apply buffs of malus for temperature
        - Update the nutritional value in relation to growth percentage

        *If plant is dead, nutritional value is halved*
        *Also kill the vegetable if temeratures are above or below resistances*
        """

        super().update_plant

        self._nutrition_value = (self._max_nutrition_value *
                                 (self._size / self._max_size))

        if self._temp > self._heat_res:
            if self._temp - self._heat_res >= 10:
                self._alive = False
                self._growth_speed = 0
                print(f"{R}{self._name} has grown {self._size:.2f} cm", end="")
                print(f"and died of the heat after {self._plant_age} days")
                print(f"{RESET}")
                return
            else:
                self._growth_speed *= (1 - (self._temp - self._heat_res) / 10)

        if self._temp < self._cold_res:
            self._alive = False
            self._growth_speed = 0
            print(f"{R}{self._name} has grown {self._size:.2f} cm", end="")
            print(f"and died of the cold after {self._plant_age} days{RESET}")
            return
        if self._temp < 0:
            self._growth_speed = 0
        if 0 <= self._temp <= 9:
            self._growth_speed *= self._temp / 10

        if not self._alive:
            self._nutrition_value = (self._max_nutrition_value *
                                     (self._size / self._max_size))
            self._nutrition_value *= 0.5


if __name__ == "__main__":
    pass
