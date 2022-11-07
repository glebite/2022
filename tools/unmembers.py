""" unmembers.py

Get a list of UN Members/Missions

Generates a big list.
"""
import requests
import pandas as pd
import json


class UnMembers:
    """
    """
    def __init__(self, url):
        """initializer for UnMembers

        Parameters:
        url (str): URL pointing to the bluebook data
        
        Returns:
        n/a
        """
        self.response = requests.get(url)
        print(type(self.response))
        self.data = str(self.response.content, 'utf-8')
        self.data = json.loads(self.data)

    def create_table(self):
        """
        """
        df = pd.json_normalize(self.data['countries'])
        self.sorted_df = df.sort_values('MC_EntityBB', axis=0)
        self.sorted_df = self.sorted_df[self.sorted_df['MC_Category'].isin(['1', '2'])]

    def dump_to_csv(self, file_name):
        """
        """
        self.sorted_df.to_csv(file_name, sep=',', header=True)

    def just_dump_country_email(self):
        """
        """
        self.create_table()
        print(self.sorted_df[['MC_Entity', 'MC_eMail', 'MC_UNCorrespondenceLanguage']].to_string())
        

    def raw_dump(self):
        """
        """
        for country in self.data['countries']:
            print(country)
            

def main():
    x = UnMembers('https://bluebook.unmeetings.org/data.json')
    x.create_table()
    x.just_dump_country_email()
    x.dump_to_csv('country_email.csv')

if __name__=="__main__":
    main()
