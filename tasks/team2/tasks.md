# Task Assignments For Team 2


## Preparations
  1. [ ] Create a new branch for your project in the main repo

  2. [ ] Follow the instructions in the [common steps file](../common.md)

## Team Assignments
Work with the tasks below as time permits.  The main point is to work with the config helper in *automation-shared*.  Parsing and processing the .csv files is secondary.

  1. [ ] In the `read_input` method, open and read the *employees1.csv* and *employees2.csv* files.  Use the `configparser.ConfigParser` object returned from the [.ini helper](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/5bf0186702ed7ffaa292941c2aeb9f332859f545/common/helpers.py#L553) to find filenames.  Use Python's [CSV parser](https://docs.python.org/3/library/csv.html) to read the files

  2. [ ] In the `read_input` method, open and read the two input .csv files.  Use the `configparser.ConfigParser` object from the .ini helper to find filenames.  Use Python's [CSV parser](https://docs.python.org/3/library/csv.html) to read the files

  3. [ ] In the `process_input` method, add the following functionality:
     - [ ] Remove employees whos ID starts with a 9
     - [ ] Merge the two lists
     - [ ] Sort the merged list by last name, descending

  4. [ ] In the `write_output` method, add the following functionality:
     - [ ] Produce an output .csv file that contains the merged and sorted list

  5. [ ] Run the program and verify that it behaves correctly

  ### Bonus Points
  #### Working With *automation-shared* and Databases
  Working with a local SQLite database is often much more efficient than using e.g., Excel.  *automation-shared* has several functions that will simplify working with a database, including importing from and exporting to CSV and Excel.

  1. [ ] In the `init` function, open a SQLite database like so:
  ```python
    import sqlite3 as db

    database = db.connect("employees.db")
  ```

  2. [ ] Use the [`import_CSV`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L300) function to import the file `departments.csv` into a table named `employees`
  
  3. [ ] Use the [`update_record`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L448) function to change all records where *Department* is `Bookkeeping` to be `Accounts` instead
  
  4. [ ] Use the [`export_xlsx`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L247) function to export the data to an Excel spreadsheet

  5. [ ] Close the database:
  ```python
    database.close()
  ```

  #### Working With *automation-shared* and Databases II
  Mixing and matching data that has been imported into a database is fast and flexible.  Much more so than, for example, using Excel.

  Here, we will import two .csv files into tables and update one table with values from another.

  1. [ ] Open a database as above

  2. [ ] Use the [`import_CSV`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L300) function to import the file `shipments.csv` into a table named `shipments`

  3. [ ] Use the [`import_CSV`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L300) function to import the file `shipment_emails.csv` into a table named `contact`

  4. [ ] Use the [`copy_column_from_table`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L484) function to copy the `email` column from the `contact` table into the `shipments` table.  An empty `email` field already exists in the `shipments` table.  Match the email addresses to their sequence numbers (`seq` field)

  5. [ ] Use the [`export_xlsx`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L247) function to export the data to an Excel spreadsheet
  
  6. [ ] Close the database

