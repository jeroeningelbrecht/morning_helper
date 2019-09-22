# morning_helper
* a clock to make it more visual how much time they still have
* an indication what the weather will be so they know what to wear that day

## First step: create the environment

* conda env create -f environment.yml
* conda activate morning_help


### CondaValueError: prefix already exists: [path to conda environments]/morning_help
* conda env remove -n morning_help


## Run app.py
This file takes care of the rest.
As a result, you should see:
* an analog clock
* current temperature
* minimum predicted temperature for today
* maximum predicted temperature for today