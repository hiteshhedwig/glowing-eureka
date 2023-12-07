# Naming convention for logged images

## Data storing structure
### Key variables 
    - date-time
    - purpose - day, night, trial
    - vehicle source - (any passenger car, cargo vehicle, opensource)
    - camera lens - focal length or type of camera


- collect daily data from vehicle
- make sure - to create data log in excel or automated
- store them in disk 
	- folder naming convention should be (YYMMDD-purpose-vehicle-cameralens)
	- file naming convention (YYMMDDhhmmss-purpose-vehicle-cameralens_{randomstring}.png)
	for example - 
		YYMMDD-purpose-vehicle-cameralens/
			YYMMDD-purpose-vehicle-cameralens_{randomstring}.png
			YYMMDD-purpose-vehicle-cameralens_{randomstring}.png
	- create a python file which intakes new recorded data and converts filename to above convention.
	- store the data in certain format