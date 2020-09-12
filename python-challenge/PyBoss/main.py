# import employee_data.csv
import os
import csv

# set path for the file
csvpath = os.path.join("Resources", "employee_data.csv")

# dictionary for the US states with abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# set the new names to hold its elements
Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []

# open current csv file
with open(csvpath) as csvfile:
    # create a variable to hold the information in the csv file
    csvreader = csv.reader(csvfile, delimiter=",")
    #remove the header line when counting
    csv_header = next(csvreader)
    # test if the file has been loaded up correctly
    print(csvreader)
    
    for row in csvreader:
        # employee ID unchanged
        Emp_ID.append(row[0])
        
        # split employee's names into two parts
        name = row[1]
        Full_name = name.split(" ")
        First_Name.append(Full_name[0])
        Last_Name.append(Full_name[1])

        # fix the employee's DOB to MM/DD/YYYY
        DOB_current = row[2]
        split_DOB = DOB_current.split("-")
        MM = split_DOB[1]
        DD = split_DOB[2]
        YYYY = split_DOB[0]
        DOB_new = MM + "/" + DD + "/" + YYYY
        DOB.append(str(DOB_new))

        # Cover the first 5 digits in SSN
        SSN_current = row[3]
        split_SSN = SSN_current.split("-")
        SSN_new = "***-**-" + split_SSN[2]
        SSN.append(SSN_new)

        # Two-letter abbreviations for States
        state_current = row[4]
        state_new = us_state_abbrev[state_current]
        State.append(state_new)

 # use zip function to bring all the updated information together
    updated_data = zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State)

 # output into a new file
output_file = os.path.join("Output", "output.csv")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])  
    writer.writerows(updated_data) 