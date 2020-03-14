import pandas as pd

class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def when(self, location) -> list:
        return list(self.df[self.df['City'] == location]['Year'].drop_duplicates())

    def where(self, date):
        return list(self.df[self.df['Year'] == date]['City'].drop_duplicates())

if __name__ == '__main__':
    import sys
    sys.path.append('/Users/cc/Documents/Learn2020/42/42PythonBootcamp/day04/ex00')
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))