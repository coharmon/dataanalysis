import unittest
import pandas as pd
from formdata import FormData


class GetAllChinaData(unittest.TestCase):

    def test_InitialChinaData(self):

        form_data = FormData()
        get_basic_data = form_data.GetBasicData('Global_Development_Indicators_2000_2020.xlsx', 'China')
        # Check if the data for China is present
        print(get_basic_data) 
        # Check if the data for China is present
        self.assertTrue('China' in get_basic_data['country_name'].values, "China data is not present in the dataset")

    def test_ChinaLowUnemployment(self):

        form_data = FormData()
        get_basic_data = form_data.GetBasicData('Global_Development_Indicators_2000_2020.xlsx', 'China')
        # Check if the unemployment rate is less than 4.3% 
        china_low_unemployment = get_basic_data.loc[get_basic_data['unemployment_rate'] < 4.3]
        china_low_unemployment = china_low_unemployment[['year', 'unemployment_rate']]
        print(china_low_unemployment)

    def test_ChinaMinUnemployment(self):
        
        form_data = FormData()
        get_basic_data = form_data.GetBasicData('Global_Development_Indicators_2000_2020.xlsx', 'China') 
        sorted_data = get_basic_data.sort_values(by='unemployment_rate', ascending=True)
        print("Year with the lowest unemployment rate was :", sorted_data[['year']].head(1))
        print("The unemployment rate in that year was :", sorted_data[['unemployment_rate']].head(1))
        # Check if the unemployment rate is sorted in descending order      
        self.assertTrue(sorted_data['unemployment_rate'].is_monotonic_increasing, "Unemployment rate is not sorted in descending order")
    
    def test_ChinaMaxUnemployment(self):  
        form_data = FormData()
        get_basic_data = form_data.GetBasicData('Global_Development_Indicators_2000_2020.xlsx', 'China') 
        sorted_data = get_basic_data.sort_values(by='unemployment_rate', ascending=True)
        print("Year with the highest unemployment rate was :", sorted_data[['year']].tail(1))
        print("The unemployment rate in that year was :", sorted_data[['unemployment_rate']].tail(1))
        # Check if the unemployment rate is sorted in descending order      
        self.assertTrue(sorted_data['unemployment_rate'].is_monotonic_increasing, "Unemployment rate is not sorted in ascending order")  

if __name__ == '__main__':
    unittest.main()