# Common Steps for All Teams
  1. [ ] Add the *automation-shared* submodule into *helsingor* folder.  Use release tag `2024.09.23.01`
     - See [automation-shared README](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/ff/changelog-auto-tag/README.md) for documentation (note the branch in the link!)

  2. [ ] Install the required Python dependencies by running
     ```bash
     py -m pip install -r requirements.txt
     ```
     from the root folder of the repo

  3. [ ] Create a `config.ini` file with three sections in the root of the repo:
     - (*config.ini* format inspiration can be found [here](https://github.com/Helsingor-Kommune-Automatisering/20008-kepo-rentetilskivning-af-indefrossede-feriepenge-ved-fratraedelse/blob/main/config.ini))

     - (Helper usage inspiration can be found [here](https://github.com/Helsingor-Kommune-Automatisering/20008-kepo-rentetilskivning-af-indefrossede-feriepenge-ved-fratraedelse/blob/032d1ce36230e2744878206c6f2ac45aeef9f800/tasks.py#L28) and [here](https://github.com/Helsingor-Kommune-Automatisering/20008-kepo-rentetilskivning-af-indefrossede-feriepenge-ved-fratraedelse/blob/032d1ce36230e2744878206c6f2ac45aeef9f800/tasks.py#L32))

     - A `Folders` section which contains an input and an output folder name

     - An `Inputs` section which contains three variables that point to the provided *employee\[1|2\].csv* and *departments.csv* files in the `files` folder.  Use variables from the `Folders` section

     - An `Outputs` section which contains a variable that points to a non-existent .csv file that we will use as output.  Use variables from the `Folders` section and include the current date in the filename

  4. [ ] Open `workshop.py`

  5. [ ] In the `init` method, use the [`confighelper` from automation-shared](https://github.com/Helsingor-Kommune-Automatisering/automation_shared/blob/bc2ffc3a89123e7d4464e31117cdad099ebdb08e/common/helpers.py#L551) to read and parse the .ini file

  6. [ ] Return to the *tasks.md* file in your team's folder
