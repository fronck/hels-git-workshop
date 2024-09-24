# Task Assignments For Team 3

  - [ ] Add the *automation-shared* submodule into *helsingor* folder.  Use release tag `2024.09.23.01`
    - See [automation-shared README](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/ff/changelog-auto-tag/README.md) for documentation (note the branch in the link!)
  - [ ] Create a new branch for your project
  - [ ] Create a `config.ini` file with three sections:
      - `Folders` which contains an input and an output folder name
      - `Inputs` which contains two variables that point to the provided .csv files in `files1`.  Use variables from the `Folders` section
      - `Outputs` which contains a variable that points to a non-existent .csv file that we will use as output.  Use variables from the `Folders` section and include the current date in the filename
      - Inspiration can be found [here](https://github.com/Helsingor-Kommune-Automatisering/20008-kepo-rentetilskivning-af-indefrossede-feriepenge-ved-fratraedelse/blob/ff/feedback-adjustments/config.ini)

  - [ ] Open `workshop.py`

  - [ ] In the `init` method, use the [`confighelper` from automation-shared](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L551) to read and parse the .ini file

  - [ ] In the `read_input` method, open and read the two input .csv files.  Use the `configparser.ConfigParser` object from the .ini helper to find filenames.  Use Python's [CSV parser](https://docs.python.org/3/library/csv.html) to read the files

  - [ ] In the `process_input` method, add the following functionality:
    - [ ] Remove duplicate entries (employees IDs present in both lists)
    - [ ] Merge the two lists
    - [ ] Sort the merged list by ID, ascending

  - [ ] In the `write_output` method, add the following functionality:
    - [ ] Produce an output .csv file that contains the merged and sorted list

  - [ ] Run the program and verify that it behaves correctly

  ### Bonus Points I
  #### Working With *automation-shared* and Databases I
  Worling with a local SQLite database is often much more efficient than using e.g., Excel.  *automation-shared* has several functions that will simplify working with a database, including importing from and exporting to CSV and Excel.
   - [ ] In the `init` function, open a SQLite database like so:
  ```python
    import sqlite3 as db

    database = db.connect("employees.db")
  ```
  - [ ] Use the [`import_CSV`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L300) function to import the file `employees3.csv` into a table named `employees`
  - [ ] Use the [`update_record`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L448) function to change all records where *Department* is `Bookkeeping` to be `Accounts` instead
  - [ ] Use the [`export_xlsx`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L247) function to export the data to an Excel spreadsheet
  - [ ] Close the database:
  ```python
    database.close()
  ```

  #### Working With *automation-shared* and Databases II
  Mixing and matching data that has been imported into a database is fast and flexible.  Much more so than, for example, using Excel.

  Here, we will import two .csv files into tables and update one table with values from another.

  - [ ] Open a database as above
  - [ ] Use the [`import_CSV`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L300) function to import the file `shipments.csv` into a table named `shipments`
  - [ ] Use the [`import_CSV`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L300) function to import the file `shipment_emails.csv` into a table named `contact`
  - [ ] Use the [`copy_column_from_table`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L484) function to copy the `email` column from the `contact` table into the `shipments` table.  An empty `email` field already exists in the `shipments` table.  Match the email addresses to their sequence numbers (`seq` field)
  - [ ] Use the [`export_xlsx`](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L247) function to export the data to an Excel spreadsheet
  - [ ] Close the database

