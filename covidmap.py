import pycountry
import plotly.express as px
import pandas as pd
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df1 = pd.read_csv(URL_DATASET)
print(df1.head(3))
print(df1.tail(3))
df1["Date"] = pd.to_datetime(df1["Date"])

#Taking all the confirmed cases on date 3/07/2020
df1=df1[df1["Date"]=='2020-07-03']
df1.reset_index(drop=True, inplace=True)
df = df1.sort_values(by=['Date'], ascending=False) #sort data by date
country=list(df['Country'])
totalcases=list(df['Confirmed'])
list1 = [[country[i],totalcases[i]] for i in range(len(country))] 
map_1 = Map(init_opts=opts.InitOpts(width="1000px", height="460px")) 
map_1.add("Total Confirmed Cases", 
 list1, 
 maptype='world',
 is_map_symbol_show=False) 
map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) 
map_1.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1100000,is_piecewise=True,pieces=[
 {"min": 500000},
 {"min": 200000,"max": 499999},
 {"min": 100000,"max": 199999},
 {"min": 50000, "max": 99999},
 {"min": 10000, "max": 49999},
 {"max": 9999},]),
 legend_opts=opts.LegendOpts(is_show=False))
map_1.render()



        