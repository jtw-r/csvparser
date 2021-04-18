import pandas as pd
import csv


#
# FUNCTION parse_columns ( csv_file, csv_column, csv_sep )

# REQUIRES
#   pandas
#
# ARGUMENTS     '*' are REQUIRED
#   *csv_file   | type: STRING  | CASE SENSITIVE | The .csv file you wish to reference
#    csv_sep    | type: CHAR    | CASE SENSITIVE | The delimiter that the specific .csv file
#                                                   uses. Will reference the get_delimiter()
#                                                   function if no value is specified
#
# RETURNS a list of the fields within
#
def parse(csv_file="file.csv", csv_sep=""):
    """

    :param csv_file:
    :param csv_sep:
    :return:
    """
    if csv_sep == "":
        df = pd.read_csv(csv_file, sep=get_delimiter(csv_file))
    else:
        df = pd.read_csv(csv_file, sep=csv_sep)
    return df


def get_column(csv_struct: list, csv_column: str):
    return csv_struct[csv_column].values


def get_columns(csv_struct: list, csv_columns: list):
    aggregate = []
    for _index in csv_columns:
        _data = csv_struct[_index]
        aggregate.append(_data)

    return aggregate


#
# Remove duplicate fields
#
def condense(csv_struct: list):
    _zipped = {}
    if len(csv_struct) == 2:
        _zipped = dict(zip(csv_struct[0], csv_struct[1]))
    return _zipped


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
    dialect = sniffer.sniff(open(csv_file).read(sample_bytes))

    return dialect.delimiter
