##  OPEN THE FILE AND READ ITS CONTENTS


with open('/Users/ashleyhaynes/Downloads/grb_table_1718041571.txt', 'r', encoding='latin-1') as f: ##opening the file and storing contents as 'f'
    file_contents = f.readlines()  ##reading the file and storing the contents using file_contents
print(file_contents) ##printing the file contents 


##  RETRIEVE INFORMATION: grb name including the day it was detected, the time it was detected, and XRT RA coordinates, and maybe redshift values