# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 08:18:30 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 13:57:33 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_recursive():
    def recursive(i, days):
        if i <= days:
            print(f"Day {i}")
            recursive(i + 1, days)
    i = 1
    harvest_day = input("Days until harvest: ")
    recursive(i, int(harvest_day))
    print("Harvest time!")
