import plotly
import plotly.figure_factory as ff 
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

def covid_overview(statewise_df):
    index_position = statewise_df[statewise_df['State Name'].str.lower() == 'total'].index.values.astype(int)[0]
    
    index_data = statewise_df.iloc[index_position]
    return {
        "Confirmed Cases" : index_data[3],
        "Active Cases" : index_data[2],
        "Deaths" : index_data[4],
        "Recovered" : index_data[5]
    }

def covid_stacked_data_bar_chart(time_series_df):
    pio.templates.default = "xgridoff"
    dates = list(time_series_df["Date"])
    fig = go.Figure(data=[
        go.Bar(name='Deaths', x=dates, y=time_series_df["Total Deceased"]),
        go.Bar(name='Recoveries', x=dates, y=time_series_df["Total Recovered"]),
        go.Bar(name='Active Cases', x=dates, y=time_series_df["Total Confirmed"])
    ])
    fig.update_layout(barmode='stack',
                      xaxis_title="Date",
                      yaxis_title="Count")
    return plotly.offline.plot(fig, output_type='div')

def covid_line_graph(time_series_df):
    pio.templates.default = "xgridoff"
    dates = list(time_series_df["Date"])
    fig = go.Figure(data=[
        go.Scatter(name='Deaths', x=dates, y=time_series_df["Daily Deceased"]),
        go.Scatter(name='Recoveries', x=dates, y=time_series_df["Daily Recovered"]),
        go.Scatter(name='Active Cases', x=dates, y=time_series_df["Daily Confirmed"])
    ])
    fig.update_layout(xaxis_title="Date",
                      yaxis_title="Count")
    return plotly.offline.plot(fig, output_type='div')


def covid_statewise_active_cases_barplot(statewise_df):
    pio.templates.default = "ggplot2"
    statewise_df = statewise_df[1:]
    statewise_df.sort_values('Active Cases', inplace=True, ascending=False)

    fig = go.Figure(data=[
        go.Bar(name='Active Cases', x=statewise_df['State Name'], y=statewise_df["Active Cases"])
    ])
    fig.update_layout(xaxis_title="State Name",
                      yaxis_title="Count")
    return plotly.offline.plot(fig, output_type='div')
    

def covid_statewise_confirmed_cases_barplot(statewise_df):
    pio.templates.default = "plotly"
    statewise_df = statewise_df[1:]
    statewise_df.sort_values('Confirmed Cases', inplace=True, ascending=False)

    fig = go.Figure(data=[
        go.Bar(name='Confirmed Cases', x=statewise_df['State Name'], y=statewise_df["Confirmed Cases"])
    ])
    fig.update_layout(xaxis_title="State Name",
                      yaxis_title="Count")
    return plotly.offline.plot(fig, output_type='div')

def covid_statewise_death_cases_barplot(statewise_df):
    pio.templates.default = "ggplot2"
    statewise_df = statewise_df[1:]
    statewise_df.sort_values('Deaths', inplace=True, ascending=False)

    fig = go.Figure(data=[
        go.Bar(name='Deaths', x=statewise_df['State Name'], y=statewise_df["Deaths"])
    ])
    fig.update_layout(xaxis_title="State Name",
                      yaxis_title="Count")
    return plotly.offline.plot(fig, output_type='div')

def covid_statewise_recovered_cases_barplot(statewise_df):
    pio.templates.default = "plotly"
    statewise_df = statewise_df[1:]
    statewise_df.sort_values('Recovered', inplace=True, ascending=False)

    fig = go.Figure(data=[
        go.Bar(name='Recovered', x=statewise_df['State Name'], y=statewise_df["Recovered"])
    ])
    fig.update_layout(xaxis_title="State Name",
                      yaxis_title="Count")
    return plotly.offline.plot(fig, output_type='div')

def covid_tablular_data(statewise_df):
    table = ff.create_table(statewise_df)
    return plotly.offline.plot(table, output_type='div')

def covid_statewise_active_cases_piechart(statewise_df):
    pio.templates.default = "ggplot2"
    statewise_df.sort_values('Active Cases', inplace=True, ascending=False)
    top_5_df = pd.DataFrame(list(zip(statewise_df['State Name'][1:6], statewise_df['Active Cases'][1:6])))
    other_df = pd.DataFrame(list(zip(["Others"], [statewise_df['Active Cases'][6:].sum()])))
    result = pd.concat([top_5_df, other_df])
    fig = go.Figure(data=[
        go.Pie(labels=result[0], values=result[1], textinfo="label+percent", pull=[0.1, 0, 0, 0, 0], rotation=45)
    ])
    return plotly.offline.plot(fig, output_type='div')

def covid_statewise_confirmed_cases_piechart(statewise_df):
    pio.templates.default = "plotly_white"
    statewise_df.sort_values('Confirmed Cases', inplace=True, ascending=False)
    top_5_df = pd.DataFrame(list(zip(statewise_df['State Name'][1:6], statewise_df['Confirmed Cases'][1:6])))
    other_df = pd.DataFrame(list(zip(["Others"], [statewise_df['Confirmed Cases'][6:].sum()])))
    result = pd.concat([top_5_df, other_df])
    fig = go.Figure(data=[
        go.Pie(labels=result[0], values=result[1], textinfo="label+percent", pull=[0.1, 0, 0, 0, 0], rotation=45)
    ])
    return plotly.offline.plot(fig, output_type='div')

def covid_statewise_death_cases_piechart(statewise_df):
    pio.templates.default = "ggplot2"
    statewise_df.sort_values('Deaths', inplace=True, ascending=False)
    top_5_df = pd.DataFrame(list(zip(statewise_df['State Name'][1:6], statewise_df['Deaths'][1:6])))
    other_df = pd.DataFrame(list(zip(["Others"], [statewise_df['Deaths'][6:].sum()])))
    result = pd.concat([top_5_df, other_df])
    fig = go.Figure(data=[
        go.Pie(labels=result[0], values=result[1], textinfo="label+percent", pull=[0.1, 0, 0, 0, 0], rotation=45)
    ])
    return plotly.offline.plot(fig, output_type='div')

def covid_statewise_recovered_cases_piechart(statewise_df):
    pio.templates.default = "plotly_white"
    statewise_df.sort_values('Recovered', inplace=True, ascending=False)
    top_5_df = pd.DataFrame(list(zip(statewise_df['State Name'][1:6], statewise_df['Recovered'][1:6])))
    other_df = pd.DataFrame(list(zip(["Others"], [statewise_df['Recovered'][6:].sum()])))
    result = pd.concat([top_5_df, other_df])
    fig = go.Figure(data=[
        go.Pie(labels=result[0], values=result[1], textinfo="label+percent", pull=[0.1, 0, 0, 0, 0], rotation=150)
    ])
    return plotly.offline.plot(fig, output_type='div')

def get_top3_bottom3_list(statewise_df, parameter):
    statewise_df.sort_values(parameter, inplace=True, ascending=False)
    result_list = []

    tu = tuple(statewise_df["State Name"])

    # extracting top 3 data
    counter = 1
    while counter <= 3:
        result_list.append(tu[counter])
        counter += 1

    # extracting bottom 3 data
    counter = 0
    index = -1
    for i in range(0, len(tu)):
        index = len(tu) - 1 - i

        if tu[index] != 'State Unassigned':
            result_list.append(tu[index])
            counter += 1
            if counter == 3:
                break
        else:
            continue

    return result_list

def get_top5_list(statewise_df, parameter):
    statewise_df.sort_values(parameter, inplace=True, ascending=False)
    result_list = []

    tu = tuple(statewise_df["State Name"])

    # extracting top 3 data
    counter = 1
    while counter <= 5:
        result_list.append(tu[counter])
        counter += 1

    return result_list