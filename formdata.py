import pandas as pd

class FormData():

    def GetBasicData(self, filename, country_name):
        df = pd.read_excel(filename, nrows=8760)
        df.fillna(0, inplace=True)

        get_basic_data = df[['year', 'country_name', 'gdp_usd', 'population', 'unemployment_rate']]
        get_basic_data = get_basic_data[get_basic_data['country_name'] == country_name]
        return get_basic_data
    
    def GetEnergyData(self, filename):
        df = pd.read_excel(filename, nrows=8760)
        df.fillna(0, inplace=True)

        get_energy_data = df[['year', 'country_name', 'energy_use_per_capita', 'co2_emissions_kt', 'renewable_energy_pct']]
        return get_energy_data
    
    def GetSchoolData(self, filename):
        df = pd.read_excel(filename, nrows=8760)
        df.fillna(0, inplace=True)

        get_school_data = df[['year', 'country_name', 'life_expectancy', 'child_mortality_rate', 'school_enrollment_secondary']]
        return get_school_data