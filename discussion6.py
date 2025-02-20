import csv
import unittest
import os


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    flight_dict = {}

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open
    
    # METHOD 1
    # with open(full_path, 'r') as csvfile:
    #     csvReader = csv.reader(csvfile)

    #     # store header in a list
    #     header = next(csvReader)

    #     for row in csvReader:
    #         for i in range(1, len(header)):
    #             if header[i] not in flight_dict:
    #                 # Add the year as a key in the dict if it does not exist yet
    #                 flight_dict[header[i]] = {}
    #             # flight_dict[year][month] = value
    #             flight_dict[header[i]][row[0]] = row[i]


    # METHOD 2
    flight_list = []

    with open(full_path, 'r') as csvfile:
        csvReader = csv.reader(csvfile)

        # store header in a list
        header = next(csvReader)

        for row in csvReader:
            flight_list.append(row)

    # Add the year as a key in the dict
    for i in range(1, len(flight_list[0])):
        flight_dict[flight_list[0][i]] = {}
        
    
    for row in flight_list :
        for i in range(1, len(row)):
            # flight_dict[year][month] = value
            flight_dict[flight_list[0][i]][row[0]] = row[i]
            

    return flight_dict

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''
    pass

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    pass

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    print("----------------------------------------------------------------------")
    flight_dict = load_csv('daily_visitors.csv')
    print("Output of load_csv:", flight_dict, "\n")
    print("Output of get_annual_max:", get_annual_max(flight_dict), "\n")
    print("Output of get_month_avg:", get_month_avg(flight_dict), "\n")
    print("----------------------------------------------------------------------")
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
