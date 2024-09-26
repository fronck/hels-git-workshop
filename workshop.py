import csv
import io
import random

def init() -> io.TextIOWrapper:
    input_file =  open("tasks/team2/files/employees2.csv", mode="r")
    return input_file



def read_input(csv_file: io.TextIOWrapper) -> list:
    csv_data = csv.DictReader(csv_file, skipinitialspace=True)
    list_data = list(csv_data)
    return list_data



def process_input(data: list) -> list:
    for row in data:
        # re-assign IDs
        row["ID"] = int(random.uniform(1000, 5000))

    return data



def write_output(data: list) -> None:
    with open("garbled_employees.csv", mode='w') as out_file:
        csv_out = csv.DictWriter(out_file, fieldnames=data.fieldnames, lineterminator="\n")

        for row in data:
            csv_out.writerow(row)

        

def cleanup(file: io.TextIOWrapper) -> None:
    file.close()



# program execution:

csv_file = init()
reader = read_input(csv_file)
new_data = process_input(reader)
write_output(new_data)
cleanup(csv_file)

