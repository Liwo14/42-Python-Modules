# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/30 08:43:34 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/30 14:52:56 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random

R = '\033[31m'
Y = '\033[33m'
G = '\033[32m'
B = '\033[34m'
RESET = '\033[0m'


def soil_type_database(nb: int) -> str:
    pass


def vegetable_database(nb: int) -> str:
    if sariety == 1:
        name = "Carrot      "
        max_size = 25
        max_age = 75
        daily_growth = self.max_size / self.max_age
        cold_resistance =
        heat_resistance =
        moisture =
        soil_type =
        size = 0
        age = 0
    elif variety == 2:
        name = "Flax        "
        max_size = 80
        max_age = 95
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif variety == 3:
        name = "Onion       "
        max_size = 40
        max_age = 10
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif variety == 4:
        name = "Spelt       "
        max_size = 110
        max_age = 135
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif variety == 5:
        name = "Turnip      "
        max_size = 35
        max_age = 55
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif variety == 6:
        name = "Parsnip     "
        max_size = 50
        max_age = 110
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif variety == 7:
        name = "Rice        "
        max_size = 110
        max_age = 130
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif variety == 8:
        name = "Rye         "
        max_size = 135
        max_age = 140
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 9:
        name = "Soybean     "
        max_size = 80
        max_age = 100
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 10:
        name = "Amaranth    "
        max_size = 125
        max_age = 100
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 11:
        name = "Bell Pepper "
        max_size = 75
        max_age = 80
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 12:
        name = "Cassava     "
        max_size = 225
        max_age = 270
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 13:
        name = "Peanut      "
        max_size = 40
        max_age = 135
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 14:
        name = "Pineapple   "
        max_size = 105
        max_age = 450
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 15:
        name = "Sunflower   "
        max_size = 225
        max_age = 100
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 16:
        name = "Pumpkin     "
        max_size = 45
        max_age = 105
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 17:
        name = "Cabbage     "
        max_size = 50
        max_age = 90
        daily_growth = self.max_size / self.max_age
        size = 0
        age = 0
    elif.variety == 18:
        .name = "Dragon Fruit"
        .max_size = 200
        .max_age = 240
        .daily_growth = self.max_size / self.max_age
        .size = 0
        .age = 0
    pass


class Plant:
    """
    This is the blueprint for a Plant
    """
    def __init__(
                self,
                soil_type: int
                ) -> None:

        self.soil_type: str = soil_type_database(soil_type)
        self.size: int = 0
        self.age: int = 0
        self.alive: bool = True
        self.stuned: bool = False
        self.moisture: float = 0.75


class Vegetable(Plant):
    """
    This is the blueprint for a vegetable
    """
    def __init__(
                self,
                soil_type: int,
                variety: int
                ) -> None:

        Plant.__init__(soil_type)
        self.name: str
        self.ripen_day: str
        self.growth_base_speed: float
        self.heat_resistance: int
        self.cold_resistance: int

        (
            self.ripen_day,
            self.growth_base_speed,
            self.name,
            self.heat_resistance,
            self.cold_resistance
        ) = vegetable_database(variety)
        