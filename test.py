# #import the libraries you want to use
# import requests
# import numpy as np

# # #METHOD 1

# # url of the file
# url = "https://swift.gsfc.nasa.gov/archive/grb_table/tmp/grb_table_1718196496.txt"

# #sending a https get request to the url above
# response = requests.get(url)


# ##extract the data and write the info to another file 
# with open("grb_table_data.txt", "wb") as f:
#         f.write(response.content)

# #read the data from the new file created
# with open("grb_table_data.txt", "r", encoding='latin-1') as f:
#     for line in f: ##looping through the table (rows and columns)
#         columns = line.split() ##columns
#         grbName = columns[0]
#         time = columns[1]
#         xrtRA = columns[14]
#         # redshiftVal = columns[30] ## check this later!!!
#         print(f"GRB Name: {grbName} | Time: {time} | XRT RA: {xrtRA} | Redshift: ")



#METHOD 2 (with numpy.genfromtext())

#import the libraries you want to use
import requests
import numpy as np

# url of the file
url = "https://swift.gsfc.nasa.gov/archive/grb_table/tmp/grb_table_1718196496.txt"

#sending a https get request to the url above
response = requests.get(url)


##extract the data and write the info to another file 
with open("grb_table_data.txt", "wb") as f:
        f.write(response.content)

# data = np.genfromtxt("grb_table_data.txt", dtype=str, encoding='latin-1')

#read the data from the new file created
with open("grb_table_data.txt", "r", encoding='latin-1') as f:
    for line in f:
        columns = line.split() ##columns
        grbName = columns[0]
        time = columns[1]
        xrtRA = columns[14]
        print(f"GRB Name: {grbName} | Time: {time} | XRT RA: {xrtRA} | Redshift: ")