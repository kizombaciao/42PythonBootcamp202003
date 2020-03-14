import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:
    def histogram(self, df: pd.DataFrame, features: list):
        df[features].hist()
        #df['City'].hist()
        plt.show()



if __name__ == "__main__":
    import sys
    sys.path.append('/Users/cc/Documents/Learn2020/42/42PythonBootcamp/day04/ex00')
    from FileLoader import FileLoader
    loader = FileLoader()
    data = loader.load('../resources/athlete_events.csv')

    g1 = MyPlotLib()
    g1.histogram(data, 'City')        


