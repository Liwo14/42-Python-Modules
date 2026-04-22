# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 07:57:57 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 11:18:33 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_harvest_total():
    i = 1
    total = 0
    while i <= 3:
        harvest = input(f"Day {i} harvest: ")
        total = int(harvest) + total
        i += 1
    print("Total harvest: ", total)
