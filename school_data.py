# school_data.py
# Nick Nikolov
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 3 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

#schools codes are unique identifiers, each school only has one code
school_codes = [1224, 1679, 9626, 9806, 9813, 9815, 9816, 9823, 9825, 9826, 9829, 9830, 9836, 9847, 9850, 9856, 9857, 9858, 9860, 9865]
school_names = ["Centennial High School", "Robert Thirsk School", "Louise Dean School", "Queen Elizabeth High School", "Forest Lawn High School", "Crescent Heights High School", "Western Canada High School", "Central Memorial High School", "James Fowler High School", "Ernest Manning High School", "William Aberhart High School", "National Sport School", "Henry Wise Wood High School", "Bowness High School", "Lord Beaverbrook High School", "Jack James High School", "Sir Winston Churchill High School", "Dr. E. P. Scarlett High School", "John G Diefenbaker High School", "Lester B. Pearson High School"]

#reshape all the year arrays 
year_2013 = year_2013.reshape(20, 3)
year_2014 = year_2014.reshape(20, 3)
year_2015 = year_2015.reshape(20, 3)
year_2016 = year_2016.reshape(20, 3)
year_2017 = year_2017.reshape(20, 3)
year_2018 = year_2018.reshape(20, 3)
year_2019 = year_2019.reshape(20, 3)
year_2020 = year_2020.reshape(20, 3)
year_2021 = year_2021.reshape(20, 3)
year_2022 = year_2022.reshape(20, 3)
#create a dictionary to reference the school code to the school name
code_to_name = {}
for school_code, school_name in zip(school_codes, school_names):
    code_to_name[school_code] = school_name

class School:
    """A Class used to create a school object

        Attributes:
        current_school_name (String): used to keep track of the current school name that the user inputs
        current_school_code (int): used to keep track of the current school code that the user inputs
        enrollment (numpy array): Combines the student enrollment across all schools for the past 10 years, in grades 10 - 12
    """
    current_school_name = 0
    current_school_code = 0

    #create full array of all enrollment data for all schools
    enrollment = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])

    def print_array_info(self):
        """ function print_array_info is a class function 
        used to print the dimensions and shape of the overall enrollment array
        The overall enrollment array is constructed of total enrollment for each school for each grade
        
        Args: None
        return: void
        """
        shape = self.enrollment.shape #array shape
        dimensions = self.enrollment.ndim # array dimensions

        print(f"""Shape of full data array: {shape}""")
        print(f"""Dinensions of full data array: {dimensions}""")


    def print_specific_data(self): 
        """ function print_specific_data is a class function used to print the data for one school
            functionality:
            Does not accept input outside of the class
            prints the mean enrollment for each grade individually
            prints the lowest enrollment for a single grade
            prints the highest enrollment for a single grade
            prints the total enrollment accross all grades for each year
            prints the total enrollment across all grades for the past 10 years
            prints the mean total enrolllment over the past 10 years
                - if enrollment has exceeded 500, it will print the median across all years where the enrollment exceeded 500

            All NaN values are treated as zero 
            Args: None
            return: void
        """

        school_index = school_codes.index(self.current_school_code) #references the school code to the index in the code array 
        
        grade_10 = self.enrollment[:, school_index, 0] #all of grade 10 enrollment for current school
        grade_11 = self.enrollment[:, school_index, 1] #all of grade 11 enrollment for current school
        grade_12 = self.enrollment[:, school_index, 2] #all of grade 12 enrollment for current school
        max_school_grade = np.nanmax(self.enrollment[:, school_index, :]) #checks all grades, and returns the highest enrollment
        min_school_grade = np.nanmin(self.enrollment[:, school_index, :]) #checks all grades, and returns the lowest enrollment
        print(f"""Shcool Name: {self.current_school_name}, School Code: {self.current_school_code}""")
        print(f"""Mean enrollment for Grade 10: {int(np.nanmean(grade_10))}""")
        print(f"""Mean enrollment for Grade 11: {int(np.nanmean(grade_11))}""")
        print(f"""Mean enrollment for Grade 12: {int(np.nanmean(grade_12))}""")

        print(f"""Highest enrollment for a single grade: {int(max_school_grade)}""")
        print(f"""Lowest enrollment for a single grade: {int(min_school_grade)}""")
        
        #loop over all years, and outputs the total enrollment for the current school, in all grades
        for i in range(len(self.enrollment[:, 1])):
            current_year = 2013+i #keep track of current year to output
            current_year_enrollment = np.nansum(self.enrollment[i, school_index, :]) #sum over the current year, all grades, current school. creates a subarray
            print(f"""Total enrollment for {current_year}: {int(current_year_enrollment)}""") 
        
        total_enrollment = np.nansum(self.enrollment[:, school_index, :]) #sum of total enrollment for current shcool, all years, all grades
        print(f"""Total enrollment over 10 years: {int(total_enrollment)}""")
        print(f"""Mean Total enrollment over 10 years: {int(total_enrollment // 10)}""")

        """ 
        Uses a boolean mask to find all enrollments over 500, for a given school across all grades

        If there are none over 500, print that there are none
        if there are enrollments over 500, find the median for all enrollments over 500
        """
        current_school_enrollment = self.enrollment[:, school_index, :] # creates subarray of all enrollment for a single school
        if not np.any(current_school_enrollment > 500): #creates boolean array, if there are no true values, then no enrollments are over 500
            print("No enrollments over 500.")
        else: #if there is at least one enrollment over 500 - find the mean
            mean_over_500 = np.nanmedian(current_school_enrollment[current_school_enrollment > 500])
            print(f"""For all enrollments over 500, the median value was: {int(mean_over_500)}""")

    def print_general_data(self):
        """ function print_general_data is a class function used to print the data for all schools.

        does not take input outside of the class
        prints the mean enrollment in 2013 for all schools
        prints the mean enrollment in 2022 for all schools
        prints the total graduating class in 2022 for all schools
        prints the lowest enrollment in a single grade, across all schools and all grades
        prints the highest enrollment in a single grade, across all schools and all grades

        All NaN values will be treated as zero
        Args: None
        return: void
        """
        mean_2013 = np.nanmean(self.enrollment[0, :, :])
        mean_2022 = np.nanmean(self.enrollment[9, :, :])
        total_2022 = np.nansum(self.enrollment[9, :, 2])
        max_grade = np.nanmax(self.enrollment)
        min_grade=np.nanmin(self.enrollment)
        print(f"""Mean enrollment in 2013: {int(mean_2013)}""")
        print(f"""Mean enrollment in 2022: {int(mean_2022)}""")
        print(f"""Total graduating class in 2022: {int(total_2022)}""")
        print(f"""Highest enrollment for a single grade: {int(max_grade)}""")
        print(f"""Lowest enrollment for a single grade: {int(min_grade)}""")

def main():
    """
    - Defines an instance of School class
    - Loop to prompt user for school code or school name input
    - prints specific data for the school input
        - checks the input and throws a  ValueError if incorrect school code or school name is input
    - prints general data for all schools in Calgary
    
    
    """
    print("ENSF 592 School Enrollment Statistics")
    #define instance of a School class
    school = School()

    # Print Stage 1 requirements here
    #prints all info about the data array created
    school.print_array_info()

    # Prompt for user input, they either enter school name or school code
    while(True):
        current_school_input = input("Please enter the high school name or school code: ")
        try:
            if int(current_school_input) not in school_codes: #first check if code was entered
                raise ValueError
            else: #if code is valid, then set the current school code to the input, and break the loop
                school.current_school_name = code_to_name[int(current_school_input)]
                school.current_school_code = int(current_school_input)
                print(school.current_school_name)
                break
        except:  #if it wasn't a code input, check if the name was input
            try:
                if str(current_school_input) not in school_names:
                    raise ValueError #raise error if incorrect school name was listed
                else:
                    school.current_school_name = str(current_school_input)
                    current_school_input = [k for k, v in code_to_name.items() if v == str(current_school_input)]
                    school.current_school_code = current_school_input[0]
                    print(current_school_input[0])
                    break
            except: ValueError()
            print("You must enter a valid school name or code.") #raises an error, but loop continues to prompt for a valid entry

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    school.print_specific_data()

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    school.print_general_data()

if __name__ == '__main__':
    main()