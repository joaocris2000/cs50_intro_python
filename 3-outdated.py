#transform from mm-dd-yyyy or m d, y in yyyy-mm-dd
month_list={   "January": 1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,      #Lib with months of the year
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12 }

while True:
    try:
        date=input("Whats the date?")
        month, day, year=date.split("/")
        month=int(month)
        day=int(day)
        if 1<=month<=12 and 1<=day<=31:
            break
                                            
    except ValueError: 
        try: 
            month_day, year=date.split(", ")
            month, day= month_day.split(" ")
            day=int(day)
            month=month_list[month]
            if 1<=day<=31:
                break
        except ValueError:
            False
                              
        
print(f"{year}-{month:02}-{day:02}")
