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
 
if __name__ == '__main__':
    unittest.main()