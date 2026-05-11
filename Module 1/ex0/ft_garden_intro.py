# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/23 10:57:26 by ccolnat         #+#    #+#               #
#  Updated: 2026/05/11 09:27:20 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

R = '\033[31m'
Y = '\033[33m'
G = '\033[32m'
B = '\033[34m'
RESET = '\033[0m'


def ft_garden_intro():
    name: str = "Rye"
    base_multiplier: float = 1.12
    age: int = 14
    moisture: int = 42
    multiplier: float = 0
    soil: str = "Low"
    if soil == "Low":
        multiplier += 1
    elif soil == "Medium":
        multiplier += 2
    elif soil == "High":
        multiplier += 3
    if moisture <= 25:
        multiplier += 1
    elif moisture <= 75:
        multiplier += 2
    else:
        multiplier += 3
    temp: int = 21
    growth_speed: float = base_multiplier * multiplier
    height: float = growth_speed * age
    print(f"{B}")
    print(" ______________________________________")
    print("|                                      |")
    print("|         Welcome in My Garden         |")
    print("|______________________________________|")
    print(f"{RESET}")
    print(f" - Plant type is: {name}")
    print(f" - Plant height is: {height:.1f}cm")
    print(f" - Planted: {age} days ago")
    print(f"{B}")
    print(" ______________________________________")
    print("|                                      |")
    print("|               Growth Data            |")
    print("|______________________________________|")
    print(f"{RESET}")
    print(f" - Soil type is: {R}{soil} fertility soil{RESET} ")
    print(f" - Moisture is: {Y}{moisture}%{RESET}")
    print(f" - Temperature is {G}{temp}°C{RESET}")
    print(f" - Plant growth speed is {growth_speed:.1f}cm per day!")
    print(f"{B}")
    print(" ______________________________________")
    print("|                                      |")
    print("|      May the Plants Be with you!     |")
    print("|______________________________________|")
    print(f"{RESET}")
    print(f"{R}[End of Prog]{RESET}")


if __name__ == "__main__":
    ft_garden_intro()


# !/usr/bin/env python3
