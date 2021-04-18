import parse as p


# Call the parse() function and specify 1) the file location/name, 2) the column name you wish to
#   pull data from. It will return a list that you can print out or iterate through.
data = p.parse("file.csv")
print(data)
print("---")

data_column = p.get_column(data, "Company")
print(data_column)
print("---")

data_multi_columns = p.get_columns(data, ["Company", "Email"])
print(data_multi_columns)
print("---")

data_condensed = p.condense(data_multi_columns)
print(data_condensed)
