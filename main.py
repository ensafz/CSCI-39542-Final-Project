
"""
Name: Ensaf Haq Zafar
Email: ensaf.zafar30@login.cuny.edu
Resources: https://scikit-learn.org/stable/index.html, https://numpy.org/doc/stable/reference/index.html#reference, 
https://pandas.pydata.org/docs/user_guide/index.html#user-guide, https://docs.python.org/3/library/pickle.html
"""
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LassoCV, RidgeCV

"""
Parameters: csv_file: the name of a csv file, cols_to_use: list of columns to use

Description: Reads the data from the csv file and loads only the data from the specified columns into a dataftame. Drops tied matches. 
Replaces any outdated nation names with the updated version.

Return: df: a dataframe

"""
def import_data(csv_file, cols_to_use):
  df = pd.read_csv(csv_file, usecols=cols_to_use)
  # remove tied matches
  df = df.drop(df[df["home_score"] == df["away_score"]].index)
  nation_updates = {
    # historical to modern
    "West Germany": "Germany",
    "East Germany": "Germany",
    "Czechoslovakia": "Czechia",
    "Soviet Union": "Russia",
    "Yugoslavia": "Serbia",
    "FR Yugoslavia": "Serbia",
    "Zaire": "Congo DR",

    # matching naming from training dataset to testing naming conventions
    "Bosnia and Herzegovina": "Bosnia–Herz",
    "Czech Republic": "Czechia",
    "South Korea": "Korea Republic",
    "Ivory Coast": "Côte d'Ivoire",
    "Iran": "IR Iran",
    "Turkey": "Türkiye",
  }
  df["home_team"] = df["home_team"].replace(nation_updates)
  df["away_team"] = df["away_team"].replace(nation_updates)
  return df


def country_stats(raw_data_df):
  import pandas as pd

def build_training_set(df):
    # num wins
    df['home_win'] = df['home_score'] > df['away_score']
    df['away_win'] = df['away_score'] > df['home_score']
    
    # home goals
    home = df.groupby('home_team').agg(
        num_goals=('home_score', 'sum'),
        num_wins=('home_win', 'sum')
    )
    
    # away goals
    away = df.groupby('away_team').agg(
        num_goals=('away_score', 'sum'),
        num_wins=('away_win', 'sum')
    )
    
    # This filters for World Cup final matches and counts unique tournament years per country
    wc_matches = df[df['tournament'] == 'FIFA World Cup']
    combined_teams = pd.concat([
        wc_matches[['home_team', 'date']].rename(columns={'home_team': 'team'}),
        wc_matches[['away_team', 'date']].rename(columns={'away_team': 'team'})
    ])
    
    combined_teams['year'] = pd.to_datetime(combined_teams['date']).dt.year
    qualifications = combined_teams.groupby('team')['year'].nunique().rename('num_times_qualified')

    all_countries = list(set(df['home_team']).union(set(df['away_team'])))
    final_df = pd.DataFrame(index=all_countries).sort_index()
    
    final_df['num_goals'] = home['num_goals'].add(away['num_goals'], fill_value=0).astype(int)
    final_df['num_wins'] = home['num_wins'].add(away['num_wins'], fill_value=0).astype(int)
    final_df['num_times_qualified'] = final_df.index.map(qualifications).fillna(0).astype(int)
    
    return final_df.reset_index().rename(columns={'index': 'country'})

                                                                                                                                                                                                                                                                                        

  
"""
Parameters:

Description:

Return:

"""
def visualize_data(visual model, df, model):

"""
Parameters:

Description:

Return:

"""
def main():
  training_cols_to_use = ["year", "stage", "home_team", "away_team", "home_score", "away_score", "outcome"]
  training_data = import_data("wcmatches.csv", training_cols_to_use)
  testing_cols_to_use = ["round", "home_team", "away_team", "score", "home_score", "away_score"]
  testing_data = import_data("matches.csv", testing_cols_to_use)
  
  
