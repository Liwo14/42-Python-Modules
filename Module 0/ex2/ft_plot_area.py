# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: ccolnat <ccolnat@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 06:49:02 by ccolnat         #+#    #+#               #
#  Updated: 2026/04/22 11:18:25 by ccolnat         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plot_area():
    width = input("Enter width: ")
    length = input("Enter length: ")
    area = int(width) * int(length)
    print("Plot area: ", area)
