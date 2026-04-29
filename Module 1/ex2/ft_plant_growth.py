# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/29 10:03:58 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/29 11:51:45 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

R = '\033[31m'
Y = '\033[33m'
G = '\033[32m'
B = '\033[34m'
RESET = '\033[0m'


class Plant:
    """
    This is the blueprint for a Plant
    """
    def __init__(self, variety: int, soil_type: int, category: int):
        """
        - First Arg ***variety*** is type (int) from 1 to 17 for the variety of plant.
            * If outside of range will default on 18 (dragon fruit)
        - Second arg ***soil_type*** is type (int) from 1 to 3.
            * If outside of range will default on 2 (Medium Fertility)
        - Third arg ***category*** is type (int)  (vegetable, tree, flower...)
        """
        if variety < 1 or variety > 17:
            self.variety = 18
            """
            Number between 1 and 18, determine the plant type.
            """
        else:
            self.variety = variety

        if soil_type < 1 or soil_type > 3:
            self.soil_type = 2
            """
            1 = Low fertility (80% growth)
            2 = Medium fertility (100% growth)
            3 = Hight fertility (120% growth)
            """
        else:
            self.soil_type = soil_type

        if category < 1 or category > 3:
            self.category = 1

        class Vegetable:
            """
            bal
            """
            def __init__(self, variety: int, soil_type: int):
                 """
                 bla
                 """
                
                if self.variety == 1:
                    self.name = "Carrot      "
                    self.max_size = 25
                    self.max_age = 75
                    self.daily_growth = self.max_size / self.max_age
                    self.cold_resistance =
                    self.heat_resistance =
                    self.moisture =
                    self.soil_type =
                    self.size = 0
                    self.age = 0
                elif self.variety == 2:
                    self.name = "Flax        "
                    self.max_size = 80
                    self.max_age = 95
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 3:
                    self.name = "Onion       "
                    self.max_size = 40
                    self.max_age = 10
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 4:
                    self.name = "Spelt       "
                    self.max_size = 110
                    self.max_age = 135
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 5:
                    self.name = "Turnip      "
                    self.max_size = 35
                    self.max_age = 55
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 6:
                    self.name = "Parsnip     "
                    self.max_size = 50
                    self.max_age = 110
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 7:
                    self.name = "Rice        "
                    self.max_size = 110
                    self.max_age = 130
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 8:
                    self.name = "Rye         "
                    self.max_size = 135
                    self.max_age = 140
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 9:
                    self.name = "Soybean     "
                    self.max_size = 80
                    self.max_age = 100
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 10:
                    self.name = "Amaranth    "
                    self.max_size = 125
                    self.max_age = 100
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 11:
                    self.name = "Bell Pepper "
                    self.max_size = 75
                    self.max_age = 80
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 12:
                    self.name = "Cassava     "
                    self.max_size = 225
                    self.max_age = 270
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 13:
                    self.name = "Peanut      "
                    self.max_size = 40
                    self.max_age = 135
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 14:
                    self.name = "Pineapple   "
                    self.max_size = 105
                    self.max_age = 450
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 15:
                    self.name = "Sunflower   "
                    self.max_size = 225
                    self.max_age = 100
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 16:
                    self.name = "Pumpkin     "
                    self.max_size = 45
                    self.max_age = 105
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 17:
                    self.name = "Cabbage     "
                    self.max_size = 50
                    self.max_age = 90
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0
                elif self.variety == 18:
                    self.name = "Dragon Fruit"
                    self.max_size = 200
                    self.max_age = 240
                    self.daily_growth = self.max_size / self.max_age
                    self.size = 0
                    self.age = 0

    def growth(self, temperature: float):
        """ 
        
        """

    def show(self):
        """
        Method to shows the attributes of the plant
        """
        print(f"| Name : {self.name} | {self.age} days | {self.size}cm |")
        print("|---------------------+----------+-------|")
        
