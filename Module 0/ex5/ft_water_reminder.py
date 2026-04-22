# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 08:10:12 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 11:18:43 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    last_sip = input("Days since last watering: ")
    if int(last_sip) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
