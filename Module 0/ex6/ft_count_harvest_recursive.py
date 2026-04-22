# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 08:18:30 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 11:18:51 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_recursive():
    def recursive(i, days):
        if days >= i:
            print(f"Day {days}")
            recursive(i, days - 1)
    i = 1
    harvest_day = input("Days until harvest: ")
    recursive(i, int(harvest_day))
    print("Harvest time!")
