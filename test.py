#automating the BAT ra and BAT dec

# #import the libraries you want to use
# import requests
# import numpy as np
# from astropy.time import Time, TimeDelta
# from astropy.io import fits

# # url of the file
# url = "https://swift.gsfc.nasa.gov/archive/grb_table/tmp/grb_table_1718893650.txt"

# #sending a https get request to the url above
# response = requests.get(url)


# ##extract the data and write the info to another file 
# with open("grb_table_data.txt", "wb") as f:
#         f.write(response.content)

# #read the data from the new file created
# with open("grb_table_data.txt", "r", encoding='latin-1') as f:
#     for line in f:
#         columns = line.split() ##columns
#         grbName = columns[0]
#         time = columns[1]
#         BATra = columns[3]
#         BATdec = columns[4]
#         print(f"GRB Name: {grbName} | BAT RA: {BATra} | BAT DEC: {BATdec}")


## CONVERTING THE GRB NAME TO A MONTH-YEAR-DAY FORMAT
from astropy.time import Time

def grb_date(grb_name):
    year = "20" + grb_name[3:5]  #converting the grb name to years
    month = grb_name[5:7] ##converting the name to months via indexing
    day = grb_name[7:9]  ##converting it to days 

    date_format = f"{year}-{month}-{day}" ##setting up the string format
    time = Time(date_format) ##converting the date string into an Astropy Time object 
    return time

grb_name = "GRB220601B"
grb_time = grb_date(grb_name) ##storing the result of time format from above function
last_day = grb_time + 7 ##adding a week to the above time 
print(f"{str(grb_time)} .. {str(last_day)}")
