import pandas as pd

def HowManyMedalsByCountry(df: pd.DataFrame, country: str) -> dict:
    my_dict = {}
    df_bis = [df['Team'] == country]


if __name__ == '__main__':
    import sys
    #sys.path.append('/Users/cc/Documents/Learn2020/42/42PythonBootcamp/day04/ex00')
    sys.path.append('../ex00')
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')