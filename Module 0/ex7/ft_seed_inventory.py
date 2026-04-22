# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 09:32:48 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 11:19:33 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

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
