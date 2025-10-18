# SDEV245_Final_Project

This Python script uses the argparse module to trigger another function, scanner(choice).

The scanner(choice) function houses five text files, all mimicking security based strings such as API Keys & Access IDs. 

The user is required to pick an integer between 1-5, which will then select the file for them. 

Each line is read within each file.

Five varying regex expressions are used to compare their parameters to each line within the chosen file. 

One the match is found, the output given to the user is the file name, the line the data was on, & the string itself. 

Lastly, a log file is created with a warning message that access was breached on the files.
