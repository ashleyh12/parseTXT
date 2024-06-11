##import the libraries you want to use
import requests

#url of the file
url = "https://swift.gsfc.nasa.gov/archive/grb_table/tmp/grb_table_1718049017.txt"

##sending a https get request to the url above
response = requests.get(url)

##extract the data and write the info to another file for a more organized view 
with open("grb_table_data.txt", "wb") as f:
        f.write(response.content)

##read the data from the new file created
with open("grb_table_data.txt", "r", encoding='latin-1') as f:
    for line in f: ##looping through the table (rows and columns)
        columns = line.split() ##columns
        grbName = columns[0]
        time = columns[1]
        xrtRA = columns[13]
        redshiftVal = columns[30] ## check this later!!!
        print("GRB Name: " + str(grbName) + " | " + " Time: " + str(time) + " | " + "Redshift: ")
 


#find the data within the file (grb name including the day it was detected, the time it was detected, and XRT RA coordinates, and maybe redshift values)

