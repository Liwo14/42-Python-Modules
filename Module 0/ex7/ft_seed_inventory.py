# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 09:32:48 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 11:06:53 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    else:
        if unit == "grams":
            print(f"{seed_type} seeds: {quantity} grams total")
        else:
            if unit == "area":
                print(f"{seed_type} seeds: covers {quantity} square meters")
            else:
                print("Unknown unit type")


ft_seed_inventory(sys.argv[1], int(sys.argv[2]), sys.argv[3])
