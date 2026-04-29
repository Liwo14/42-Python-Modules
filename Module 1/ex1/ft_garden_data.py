# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/24 08:56:08 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/29 10:04:30 by ccolnat         ###   ########.fr        #
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
    def __init__(self, type: int):
        """
        Take 1 Arg for the type of plant, should be an int between 1 and 17
        (If outside of range will default on dragon fruit)
        """
        self.type = type
        if type < 1 or type > 17:
            self.name = "Dragon Fruit"
            self.size = "200"
            self.age = "240"
        elif type == 1:
            self.name = "Carrot      "
            self.size = "25 "
            self.age = "75 "
        elif type == 2:
            self.name = "Flax        "
            self.size = "80 "
            self.age = "95 "
        elif type == 3:
            self.name = "Onion       "
            self.size = "40 "
            self.age = "105"
        elif type == 4:
            self.name = "Spelt       "
            self.size = "110"
            self.age = "135"
        elif type == 5:
            self.name = "Turnip      "
            self.size = "35 "
            self.age = "55 "
        elif type == 6:
            self.name = "Parsnip     "
            self.size = "50 "
            self.age = "110"
        elif type == 7:
            self.name = "Rice        "
            self.size = "110"
            self.age = "130"
        elif type == 8:
            self.name = "Rye         "
            self.size = "135"
            self.age = "140"
        elif type == 9:
            self.name = "Soybean     "
            self.size = "80 "
            self.age = "100"
        elif type == 10:
            self.name = "Amaranth    "
            self.size = "125"
            self.age = "100"
        elif type == 11:
            self.name = "Bell Pepper "
            self.size = "75 "
            self.age = "80 "
        elif type == 12:
            self.name = "Cassava     "
            self.size = "225"
            self.age = "270"
        elif type == 13:
            self.name = "Peanut      "
            self.size = "40 "
            self.age = "135"
        elif type == 14:
            self.name = "Pineapple   "
            self.size = "105"
            self.age = "450"
        elif type == 15:
            self.name = "Sunflower   "
            self.size = "225"
            self.age = "100"
        elif type == 16:
            self.name = "Pumpkin     "
            self.size = "45 "
            self.age = "105"
        elif type == 17:
            self.name = "Cabbage     "
            self.size = "50 "
            self.age = "90 "

    def show(self):
        """
        Method to shows the attributes of the plant
        """
        print(f"| Name : {self.name} | {self.age} days | {self.size}cm |")
        print("|---------------------+----------+-------|")


if __name__ == "__main__":

    print(f"{B}")
    print(" ________________________________________")
    print("|                                        |")
    print("|              Plant list :              |")
    print("|________________________________________|")
    i: int = 1
    while i != 19:
        plant = Plant(i)
        Plant.show(plant)
        i += 1
    print("|_____________________|__________|_______|")
    print(f"{RESET}")
