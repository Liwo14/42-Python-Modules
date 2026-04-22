# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 08:18:33 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 11:18:46 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
    i = 1
    harvest_day = input("Days until harvest: ")
    while i != int(harvest_day):
        print(f"Day {i}")
        i += 1
    print(f"Day {i}")
    print("Harvest time!")
