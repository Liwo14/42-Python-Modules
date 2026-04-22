# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 07:57:52 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 13:52:24 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    age = input("Enter plant age in days: ")
    if int(age) <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
