import parse as p


# Call the parse() function and specify 1) the file location/name, 2) the column name you wish to
#   pull data from. It will return a list that you can print out or iterate through.
data = p.parse_columns("file.csv", "Company")
print(data)
