import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

class SolarCountryData:
    def __init__(self, filepath, country_name):
        self.country_name = country_name
        self.df = pd.read_csv(filepath)
        self.df["Country"] = country_name
    
    def get_metric(self, metric):
        return self.df[metric]
    
    def summary(self):
        return self.df[["GHI", "DNI", "DHI"]].describe()

class SolarComparison:
    def __init__(self, country_data_list):
        self.data_objects = country_data_list
        self.df_all = pd.concat([c.df for c in self.data_objects], ignore_index=True)

    def summary_table(self):
        return self.df_all.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])
    
    def plot_boxplot(self, metric):
        sns.boxplot(x="Country", y=metric, data=self.df_all)
        plt.title(f"{metric} Comparison")
        plt.show()

    def run_anova(self, metric):
        groups = [c.get_metric(metric) for c in self.data_objects]
        return f_oneway(*groups)
