print("WELCOME TO TIP CALCULATOR!")
bill=int(input("what was the total bill ? $ "))
tip=int(input("How much tip would you like to give? 10%,12%,20%?"))
split=int(input("How many people to split the bill?"))
tip_cal=tip/100
bill_ttl=bill+(bill*tip_cal)
ttl_split=bill_ttl/split
round(ttl_split,2)
print(f"Each person should pay: ${ttl_split}" )