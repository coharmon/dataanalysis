import unittest
import pandas as pd
from formdata import FormData


class SortIncomeBrackets(unittest.TestCase):

    def test_get_low_income_countries(self):

        df = pd.read_excel('Global_Development_Indicators_2000_2020.xlsx', nrows=8760)
        df.fillna(0, inplace=True)

        get_basic_data = df[['year', 'country_name', 'gdp_usd', 'population', 'unemployment_rate']]
        get_low_income_countries = get_basic_data[get_basic_data['gdp_usd'] < 578209113776.615]
        print(get_low_income_countries)
    
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