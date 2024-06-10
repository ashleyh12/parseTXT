##import the libraries you want to use
import requests

#url of the file
url = "https://swift.gsfc.nasa.gov/archive/grb_table/tmp/grb_table_1718049017.txt"

##sending a https get request to the url above
response = requests.get(url)

##extract the data and write the info to another file for a more organized 
with open("grb_table_data.txt", "wb") as f:
        f.write(response.content)
#find the data within the file (grb name including the day it was detected, the time it was detected, and XRT RA coordinates, and maybe redshift values)


# with open('/Users/ashleyhaynes/Downloads/grb_table_1718041571.txt', 'r', encoding='latin-1') as f: ##opening the file and storing contents as 'f'
#         f.decode('utf-8')
