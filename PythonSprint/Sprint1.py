# Description: A program that process salesperson travel claims when they return
# from a business trip at NL Chocolate Company.
# Author: Abiodun Magret Oyedele, Lana Starkes and Jeff Woolridge.
# Date(s): Feb 10, 2025 - Feb 10, 2025
 
 
# Define required libraries.
import datetime 


# Define program constants.
CUR_DATE = datetime.datetime.now()
DAILY_RATE = 85
MILLEAGE_O_RATE = 0.17
MILEAGE_R_RATE = 65
BONUS_3_DAYS = 100
BONUS_KM_O = 0.04
BONUS_CLAIMTYPE_E = 45
BONUS_START_DATE_RANGE = 50
HST_RATE = 0.15
TOTAL_KM = 0

# Main program starts here.
while True:

    # Gather user inputs.
    while True:
        empNum = (input("Enter employee number (XXXXX) or '0' to exit: "))

        if empNum == "0":
            print("Exiting program. Goodbye!")
            exit()

        if (empNum == ""):
            print()
            print("   Data Entry Error - Employee number must be entered")
            print()
        elif len(empNum) != 5:
            print()
            print("   Data Entry Error - Five characters must be entered for employee number")
            print()
        else:
            break

    # A set of allowable character can be validated against the firstName input.
    while True:
        firstName = input("Enter employee firstName: ").title()

        if (firstName == ""):
            print()
            print("   Data Entry Error - Employee first name must be entered")
            print()
        else:
            break

    # A set of allowable character can be validated against the lastName input.
    while True:
        lastName = input("Enter employee lastName: ").title()

        if (lastName == ""):
            print()
            print("   Data Entry Error - Employee last name must be entered")
            print()
        else:
            break

    location = input("Enter trip location: ")

    while True:
        startStr = input("Enter start date (YYYY-MM-DD): ")

        if (startStr == ""):
            print()
            print("   Data Entry Error - The trip start date must be entered")
            print()
            continue
        try:
            startDate = datetime.datetime.strptime(startStr, "%Y-%m-%d") 
            break  
        except:
            print()
            print("    Data Entry Error - Start date is not the correct format (YYYY-MM-DD)")
            print()

    while True:
        endStr = input("Enter end date (YYYY-MM-DD): ").strip()

        if (endStr == ""):
            print()
            print("   Data Entry Error - The trip end date must be entered")
            print()
            continue
        try:
            endDate = datetime.datetime.strptime(endStr, "%Y-%m-%d") 

            endMaxDate = startDate + datetime.timedelta(days=7)

            if endDate < startDate:
                print()
                print("    Data Entry Error - end date must be after the start date")
                print()
                continue

            if endDate > endMaxDate:
                print()
                print("    Data Entry Error - end date cannot be more than 7 days from start date")
                print()
                continue

            break 

        except:
            print()
            print("    Data Entry Error - end date is not the correct format (YYYY-MM-DD)")
            print()

    while True:
        carUsed = input("Enter car used (O for Own Car or R for Rented Car): ").upper()

        if (carUsed == ""):
            print()
            print("    Data Entry Error - The car used must be entered")
            print()
            continue
        elif (carUsed != "O" and carUsed != "R"):
            print()
            print("    Data Entry Error - Car used should either be O or R")
            print()
            continue
        else:
            break

    if (carUsed == "O"):
        while True:
            TOTAL_KM = int(input("Enter total Kilometers travelled (####): "))

            try:
                TOTAL_KM = int(TOTAL_KM)
                if (TOTAL_KM > 2000):
                    print()
                    print("    Data Entry Error - The total kilometers travelled cannot exceed 2000kilometers")
                    print()
                else:
                    break
            except:
                print()
                print("    Data Entry Error - The total kilometers travelled must be a number")
                print()

    while True:
        claimType = input("Enter the claim type (S or E): ").upper()

        if (claimType != "E" and claimType != "S"):
            print()
            print("    Data Entry Error - Claim type must be either 'S' for Standard or 'E' for Executive")
            print()
        else:
            break

    # Perform required calculations.

    totalDays = (endDate - startDate).days
    diemAmount = DAILY_RATE * totalDays

    if (carUsed == "O"):
        milleageAmount = MILLEAGE_O_RATE * TOTAL_KM
    elif (carUsed == "R"):
        milleageAmount = MILEAGE_R_RATE * totalDays

    # Calculates bonus based on certain criterias
    bonus = 0
    start_date_range = datetime.datetime(startDate.year, 12, 15)
    end_date_range = datetime.datetime(startDate.year, 12, 22)

    if (totalDays > 3):
        bonus = bonus + BONUS_3_DAYS

    if (TOTAL_KM > 1000 and carUsed == "O"):
        bonus = bonus + (BONUS_KM_O * TOTAL_KM)

    if (claimType == "E"):
        bonus = bonus + (BONUS_CLAIMTYPE_E * totalDays)

    if startDate >= start_date_range and startDate <= end_date_range:
        bonus = bonus + BONUS_START_DATE_RANGE * totalDays

    claimAmount = diemAmount + milleageAmount + bonus

    HST = HST_RATE * claimAmount

    claimTotal = claimAmount + HST

    # Display results
    print()
    print(f"             NL Chocolate Company")
    print("_" * 48)

    print()
    print(f" Employee Number: {empNum:>30s}")
    print(f" Employee First Name: {firstName:>26s}")
    print(f" Employee Last Name: {lastName:>27s}")
    print(f" Trip location: {location:>32s}")
    print(f" Start Date: {startDate.strftime('%Y-%m-%d'):>35s}")
    print(f" End Date: {endDate.strftime('%Y-%m-%d'):>37s}")

    if (carUsed == "O"):
        carUsedValue = "Own Car"
    elif (carUsed == "R"):
        carUsedValue = "Rented Car"
    print(f" Car Used: {carUsedValue:>37s}")
    
    if (carUsed == "O"):
        print(f" Total Kilometers travelled: {TOTAL_KM:>19d}")

    if (claimType == "S"):
        claimTypeResult = "Standard"
    elif (claimType == "E"):
        claimTypeResult = "Executive"
    print(f" Claim type: {claimTypeResult:>35s}")

    print()
    print(f" Number of days: {totalDays:>31d}")
    print(f" Per diem amount: {diemAmount:>30.2f}")
    print(f" Mileage amount: {milleageAmount:31.2f}")
    print(f" Bonus: {bonus:>40.2f}")
    print(f" Claim amount: {claimAmount:>33.2f}")
    print(f" HST: {HST:>42.2f}")
    print(f" Claim Total: {claimTotal:>34.2f}")
    print("_" * 48)
    print()

    # Any housekeeping duties at the end of the program.
    again = input(f"Do you want to enter another claim? (Y to continue): ").upper()
    if again != "Y":
        print(f" Goodbye!!!")
        break
