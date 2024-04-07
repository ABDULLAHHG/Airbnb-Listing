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
    agg_meaning_list = ["Total Price" , "Avarage Price" , "Highest Price" , "Lowest Price"]
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

    fig.update_layout(height=1200, width=800, title_text=f"{df.index.name} VS " + " , ".join([col for col in df.columns]) )
    fig.show()


