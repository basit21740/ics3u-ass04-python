#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: NOv 2021
# This program tells if the package is acceptable or not

import math


def main():
    # this function tells if the package is acceptable or not
    
    # input
    try:
        length = int(input("Enter length of the package (mm): "))
        width = int(input("Enter width of the package (mm): "))
        weight = int(input("Enter weight of the package: "))
        height = int(input("Enter height of the package: "))
   
        # process
        volume = length * width * height
        if volume >= 10000:
           print("This package is not acceptable because it doesn't meets the requirement of weight = 27kg and volume = 10,000mm")
        elif weight >= 27:
           print("This package is not acceptable because doesn't meets the requirement of weight = 27kg and volume = 10,000mm³")
        else:
           print("This package is acceptable")
    except ValueError:
            print("Invalid Input")
    
    print("\nDone.")
if __name__ == "__main__":
    main()
