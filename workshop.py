import csv
import io
import random
from helsingor.common.helpers import confighelpers

config = confighelpers.load_config('config.ini')

def init(input_file: str) -> io.TextIOWrapper:
    input_file =  open(input_file, mode="r")
    return input_file

def read_input(csv_file: io.TextIOWrapper) -> list:
    csv_data = csv.DictReader(csv_file, skipinitialspace=True)
    list_data = list(csv_data)
    return list_data

def process_input(data: list) -> list:
    return [row for row in data if row['Age'] >= 25]

def sort_by_age(data: list) -> list:
    def sort_func(item):
        return item['Age']
    
    return data.sort(key=sort_func)

def write_output(data: list) -> None:
    with open(config['Outputs']['EmployeesFilteredSorted'], mode='w') as out_file:
        csv_out = csv.DictWriter(out_file, fieldnames=data.fieldnames, lineterminator="\n")

        for row in data:
            csv_out.writerow(row)

def cleanup(file: io.TextIOWrapper) -> None:
    file.close()



# program execution:

employees1file = init(config['Inputs']['Employees1'])
employees2file = init(config['Inputs']['Employees2'])

employees1 = read_input(employees1file)
employees2 = read_input(employees2file)

merged_list = [*process_input(employees1), *process_input(employees2)]
sorted_list = sort_by_age(merged_list)

write_output(sorted_list)
cleanup(employees1file)
cleanup(employees2file)

