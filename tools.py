import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

# # We will try to create our tools here 
# Drop Outliers 
def drop_Outliers(col : str) -> pd.Series():
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1 
    lower_lim = Q1 - 1.5 * IQR
    upper_lim = Q3 + 1.5 * IQR
    outliers_15_low = (df[col] < lower_lim)
    outliers_15_up = (df[col] > upper_lim)
    
    #  result len 
    # len(df[col]) - (len(df[col][outliers_15_low]) + len(df[col][outliers_15_up]))
    
    #  the Outliers
    # df[col][(outliers_15_low | outliers_15_up)]

    #  the col without the outliers 
    return df[col][~(outliers_15_low | outliers_15_up)]

# Statistics summary Mean , Max , Min , Sum
def column_summary_statistics(df : pd.DataFrame() , groupby_column : str , target_column : str) -> pd.DataFrame():

    agg_list = ["sum" , "mean" , "max" , "min"]
    agg_meaning_list = ["Total Price" , "Average Price" , "Highest Price" , "Lowest Price"]
    df = df.groupby(groupby_column)[target_column].agg(agg_list)
    df.columns = df.columns = agg_meaning_list
    return df

# plot the Statistics Summary 
def plot_column_summary_statistics(df : pd.DataFrame()) -> None :
    fig = make_subplots(rows=2, cols=2 , subplot_titles = [col.title() for col in df.columns])

    for i , column in enumerate(df.columns):
        row = (i)//2 + 1
        col = (i)%2 + 1

        fig.add_trace(
        go.Bar(x = df.index , y = df[column],
        showlegend=False,
        name=column.title(),

        opacity=0.75
    ),
        row=row, col=col

    )
    fig.update_layout(plot_bgcolor = "white",
                 font = dict(color = "#909497", size = 18),
                 title = dict(text = f"{df.index.name.title()} VS " + " , ".join([col for col in df.columns]), font = dict(size = 26)),
                 margin = dict(t = 100, r = 80, b = 80, l = 120),
                 hovermode="closest",
                 height = 1200,
                 width = 1000)

    fig.show()


def Muti_hist_plot(df):
    selected_columns = [col for col in df if df[col].dtype in ["int64" , "float64"]]
    rows = cols = int(len(selected_columns) ** 0.5)
    
    fig = make_subplots(rows=rows, cols=cols , subplot_titles = [col.title() for col in selected_columns])
    
    for i , column in enumerate(selected_columns):
        row = (i)//rows + 1
        col = (i)%cols + 1
        
        fig.add_trace(
        go.Histogram(x = df[column] ,
        # histnorm='percent',
        showlegend=False,
        name=column.title(),
        
        xbins=dict(
    #         start=-3.0,
    #         end=4,
    #         size=0.5
        ),
        # marker_color='#330C73',
        opacity=0.75
    ),
        row=row, col=col
        
    )
    
    
    
        fig.update_layout(plot_bgcolor = "white",
                 font = dict(color = "#909497", size = 18),
                 title = dict(text = "all numerical columns".title(), font = dict(size = 26)),
                 margin = dict(t = 100, r = 80, b = 80, l = 120),
                 hovermode="closest",
                 height = 1000,
                 width = 900)
        
    fig.show() 
