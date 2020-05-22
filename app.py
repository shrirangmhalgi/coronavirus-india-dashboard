from flask import Flask, render_template
app = Flask(__name__)

from scrapper.indian_scrapper import get_api_data
from eda.eda import covid_overview, covid_stacked_data_bar_chart, covid_line_graph, covid_statewise_active_cases_barplot, covid_statewise_confirmed_cases_barplot, covid_statewise_death_cases_barplot, covid_statewise_recovered_cases_barplot, covid_tablular_data, covid_statewise_active_cases_piechart, covid_statewise_confirmed_cases_piechart, covid_statewise_death_cases_piechart, covid_statewise_recovered_cases_piechart, get_top3_bottom3_list, get_top5_list

@app.route("/")
def index():
    data_dict = get_api_data()
    time_series_df = data_dict["time_series_df"]
    statewise_df = data_dict["statewise_df"]

    statewise_df.replace("Dadra and Nagar Haveli and Daman and Diu", "Dadra and Nagar Haveli", inplace=True)

    overview = covid_overview(statewise_df)
    stacked_data_bar_chart = covid_stacked_data_bar_chart(time_series_df)
    line_graph = covid_line_graph(time_series_df)
    tablular_data = covid_tablular_data(statewise_df[1:])

    statewise_active_cases_barplot = covid_statewise_active_cases_barplot(statewise_df)
    statewise_active_cases_barplot_t3b3_list = get_top3_bottom3_list(statewise_df, "Active Cases")

    statewise_confirmed_cases_barplot = covid_statewise_confirmed_cases_barplot(statewise_df)
    statewise_confirmed_cases_barplot_t3b3_list = get_top3_bottom3_list(statewise_df, "Confirmed Cases")

    statewise_death_cases_barplot = covid_statewise_death_cases_barplot(statewise_df)
    statewise_death_cases_barplot_t3b3_list = get_top3_bottom3_list(statewise_df, "Deaths")

    statewise_recovered_cases_barplot = covid_statewise_recovered_cases_barplot(statewise_df)
    statewise_recovered_cases_barplot_t3b3_list = get_top3_bottom3_list(statewise_df, "Recovered")
    
    # send list of top 5 states
    statewise_active_cases_piechart = covid_statewise_active_cases_piechart(statewise_df)
    statewise_active_cases_piechart_top5 = get_top5_list(statewise_df, "Active Cases")

    statewise_confirmed_cases_piechart = covid_statewise_confirmed_cases_piechart(statewise_df)
    statewise_confirmed_cases_piechart_top5 = get_top5_list(statewise_df, "Confirmed Cases")

    statewise_death_cases_piechart = covid_statewise_death_cases_piechart(statewise_df)
    statewise_death_cases_piechart_top5 = get_top5_list(statewise_df, "Deaths")

    statewise_recovered_cases_piechart = covid_statewise_recovered_cases_piechart(statewise_df)
    statewise_recovered_cases_piechart_top5 = get_top5_list(statewise_df, "Recovered")

    return render_template("index.html", 
                            overview=overview,
                            stacked_data_bar_chart=stacked_data_bar_chart,
                            line_graph=line_graph,
                            statewise_active_cases_barplot=statewise_active_cases_barplot,
                            statewise_confirmed_cases_barplot=statewise_confirmed_cases_barplot,
                            statewise_death_cases_barplot=statewise_death_cases_barplot,
                            statewise_recovered_cases_barplot=statewise_recovered_cases_barplot,
                            tablular_data=tablular_data,
                            statewise_active_cases_piechart=statewise_active_cases_piechart,
                            statewise_confirmed_cases_piechart=statewise_confirmed_cases_piechart,
                            statewise_death_cases_piechart=statewise_death_cases_piechart,
                            statewise_recovered_cases_piechart=statewise_recovered_cases_piechart,
                            statewise_active_cases_barplot_t3b3_list=statewise_active_cases_barplot_t3b3_list,
                            statewise_confirmed_cases_barplot_t3b3_list=statewise_confirmed_cases_barplot_t3b3_list,
                            statewise_death_cases_barplot_t3b3_list=statewise_death_cases_barplot_t3b3_list,
                            statewise_recovered_cases_barplot_t3b3_list=statewise_recovered_cases_barplot_t3b3_list,
                            statewise_active_cases_piechart_top5=statewise_active_cases_piechart_top5,
                            statewise_confirmed_cases_piechart_top5=statewise_confirmed_cases_piechart_top5,
                            statewise_death_cases_piechart_top5=statewise_death_cases_piechart_top5,
                            statewise_recovered_cases_piechart_top5=statewise_recovered_cases_piechart_top5)

if __name__ == "__main__":
    # app.jinja_env.cache = {}
    app.run(threaded=True)