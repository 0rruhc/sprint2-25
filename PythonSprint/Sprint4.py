# Author: Abiodun Magret Oyedele, Lana Starkes and Jeff Woolridge.
# Date(s): Feb 10, 2025 - Feb 10, 2025
# Description: Program to calculate equipment maintenance schedule and financial information.

# Import libraries
import datetime

# Constants
USEFUL_LIFE_MONTHS = 180  # 15 years = 180 months
SALVAGE_PERCENTAGE = 0.10  # 10% of the purchase cost

# Input and validation for equipment cost
while True:
    try:
        equipCost = float(input("Enter the equipment cost: $"))
        if equipCost <= 0:
            print("Cost must be a positive value.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number for the equipment cost.")

# Input and validation for purchase date
while True:
    purchaseDate_str = input("Enter the equipment purchase date (DD/MM/YYYY): ")
    try:
        purchaseDate = datetime.datetime.strptime(purchaseDate_str, "%d/%m/%Y")
        if purchaseDate > datetime.datetime.now():
            print("The purchase date cannot be in the future. Please enter a valid date.")
        else:
            break
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")

# Calculate maintenance schedule dates
cleaningDate = purchaseDate + datetime.timedelta(days=10)  # Cleaning in 10 days
fluidCheckDate = purchaseDate + datetime.timedelta(weeks=3)  # Tube and fluid check in 3 weeks
majorInspection = purchaseDate + datetime.timedelta(weeks=26)  # Major inspection in 6 months (26 weeks)

# Calculate amortization
salvageValue = equipCost * SALVAGE_PERCENTAGE  # Salvage value (10% of cost)
amortization = (equipCost - salvageValue) / USEFUL_LIFE_MONTHS  # Monthly amortization

# Format the dates in DD, MON, YYYY format
cleaningDate_str = cleaningDate.strftime("%d %B, %Y")
fluidCheckDate_str = fluidCheckDate.strftime("%d %B, %Y")
majorInspection_str = majorInspection.strftime("%d %B, %Y")
purchaseDate_str = purchaseDate.strftime("%d %B, %Y")

# Output
print("\n\n")
print("XYZ Company - Equipment Maintenance Schedule")
print()
print("-------------------------------------------------------")
print()
print("Equipment Purchase Information:")
print()
print(f"Equipment Cost:                      ${equipCost:,.2f}")
print(f"Purchase Date:                       {purchaseDate_str}")
print()
print("-------------------------------------------------------")
print()
print("Maintenance Schedule:")
print()
print(f"Cleaning (10 days):                  {cleaningDate_str}")
print(f"Tube and Fluid Check (3 weeks):      {fluidCheckDate_str}")
print(f"Major Inspection (6 months):         {majorInspection_str}")
print()
print("-------------------------------------------------------")
print()
print("Financial Information:")
print()
print(f"Salvage Value (10% of cost):         ${salvageValue:,.2f}")
print(f"Monthly Amortization:                ${amortization:,.2f}")
print()
print("-------------------------------------------------------")