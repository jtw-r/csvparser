import pandas as pd
import csv


#
# FUNCTION parse_columns ( csv_file, csv_column, csv_sep )

# REQUIRES
#   pandas
#
# ARGUMENTS     '*' are REQUIRED
#   *csv_file   | type: STRING  | CASE SENSITIVE | The .csv file you wish to reference
#   *csv_column | type: STRING  | CASE SENSITIVE | The column name you wish to pull data from
#                                                   within the .csv file
#    csv_sep    | type: CHAR    | CASE SENSITIVE | The delimiter that the specific .csv file
#                                                   uses. Will reference the get_delimiter()
#                                                   function if no value is specified
#
# RETURNS a list of the fields within
#
def parse_columns(csv_file="file.csv", csv_column="", csv_sep=""):
    if csv_sep == "":
        df = pd.read_csv(csv_file, sep=get_delimiter(csv_file))
    else:
        df = pd.read_csv(csv_file, sep=csv_sep)
    return df[csv_column].values


#
# FUNCTION get_delimiter ( csv_file )
#
# UTILITY FUNCTION
#
# REQUIRES
#   csv
#
# ARGUMENTS     '*' are REQUIRED
#   *csv_file   | type: STRING  | CASE SENSITIVE | The .csv file you wish to reference
#
# RETURNS the specific character set that is used to separate the .csv file
#
def get_delimiter(csv_file="file.csv"):
    sniffer = csv.Sniffer()
    sample_bytes = 32
    dialect = sniffer.sniff(open("file.csv").read(sample_bytes))

    return dialect.delimiter

