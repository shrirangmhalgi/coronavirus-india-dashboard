import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json

def get_scraped_data():
    base_url = "https://www.mohfw.gov.in/"

    response = requests.get(base_url)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find_all("table")[0]
    trs = table.find_all("tr")

    srNo = []
    state = []
    confirmed = []
    cured = []
    death = []

    for tr in trs:
        tds = tr.find_all("td")

        try:
            srNo.append(int(tds[0].text.strip()))
            state.append(tds[1].text.strip())
            confirmed.append(int(tds[2].text.strip()))
            cured.append(int(tds[3].text.strip()))
            death.append(int(tds[4].text.strip()))
        except :
            pass
    
    zipped = zip(srNo,
                 state,
                 confirmed,
                 cured,
                 death)

    df = pd.DataFrame(list(zipped), columns=["Sr No",
                                             "State",
                                             "Confirmed Cases",
                                             "Cured",
                                             "Deaths"])
    
    return df

def get_api_data():
    base_url = "https://api.covid19india.org/data.json"
    response = requests.get(base_url)
    api_data = json.loads(response.text)
    
    # ------------------------------------TIME-SERIES-DATA-FRAME-------------------------------
    # lists for time_series_data
    date_list = []
    daily_confirmed_list = []
    daily_deceased_list = []
    daily_recovered_list = []
    total_confirmed_list = []
    total_deceased_list = []
    total_recovered_list = []

    time_series = api_data["cases_time_series"]
    for t in time_series:
        date_list.append(t["date"])
        daily_confirmed_list.append(int(t["dailyconfirmed"]))
        daily_deceased_list.append(int(t["dailydeceased"]))
        daily_recovered_list.append(int(t["dailyrecovered"]))
        total_confirmed_list.append(int(t["totalconfirmed"]))
        total_deceased_list.append(int(t["totaldeceased"]))
        total_recovered_list.append(int(t["totalrecovered"]))
        
    time_series_zipped = zip(date_list, 
                             daily_confirmed_list, 
                             daily_deceased_list, 
                             daily_recovered_list, 
                             total_confirmed_list, 
                             total_deceased_list, 
                             total_recovered_list)

    time_series_df = pd.DataFrame(list(time_series_zipped), columns=["Date",
                                             "Daily Confirmed",
                                             "Daily Deceased",
                                             "Daily Recovered",
                                             "Total Confirmed",
                                             "Total Deceased",
                                             "Total Recovered"])

    # ------------------------------------STATEWISE-DATA-FRAME-------------------------------    
    # lists for statewise data
    state_name_list = []
    state_code_list = []
    active_cases_list = []
    confirmed_cases_list = []
    deaths_list = []
    recovered_list = []

    statewise_data = api_data["statewise"]

    for s in statewise_data:
        state_name_list.append(s["state"])
        state_code_list.append(s["statecode"])
        active_cases_list.append(int(s["active"]))
        confirmed_cases_list.append(int(s["confirmed"]))
        deaths_list.append(int(s["deaths"]))
        recovered_list.append(int(s["recovered"]))

    statewise_zipped = zip(state_name_list, 
                           state_code_list,
                           active_cases_list,
                           confirmed_cases_list,
                           deaths_list,
                           recovered_list)

    statewise_df = pd.DataFrame(list(statewise_zipped), columns=["State Name",
                                                                 "State Code",
                                                                 "Active Cases",
                                                                 "Confirmed Cases",
                                                                 "Deaths",
                                                                 "Recovered"])


    # ------------------------------------TESTED-DATA-FRAME-------------------------------    
    # lists for tested data
#     timestamp_list = []
#     total_samples_tested_list = []
#     total_positive_cases_list = []
#     total_individuals_tested_list = []
#     tests_per_million_list = []
#     tests_per_confirmed_cases = []
#     tests_positivity_rate = []
#     individuals_tests_per_confirmed_case = []

#     tested_data = api_data["tested"]

#     for t in tested_data:
#         timestamp_list.append(t["updatetimestamp"].strip())
#         total_samples_tested_list.append(t["totalsamplestested"].strip())
#         total_positive_cases_list.append(t["totalpositivecases"].strip())
#         total_individuals_tested_list.append(t["totalindividualstested"].strip())
#         tests_per_million_list.append(t["testspermillion"].strip())
#         tests_per_confirmed_cases.append(t["testsperconfirmedcase"].strip())
#         tests_positivity_rate.append(t["testpositivityrate"][:-1].strip())
#         individuals_tests_per_confirmed_case.append(t["individualstestedperconfirmedcase"].strip())

#     tested_zipped = zip(timestamp_list,
#                         total_samples_tested_list,
#                         total_positive_cases_list,
#                         total_individuals_tested_list,
#                         tests_per_million_list,
#                         tests_per_confirmed_cases,
#                         tests_positivity_rate,
#                         individuals_tests_per_confirmed_case)

#     tested_df = pd.DataFrame(list(tested_zipped), columns=["Timestamp",
#                                                            "Total Samples Tested",
#                                                            "Total Positive Cases",
#                                                            "Total Individuals Tested", 
#                                                            "Tests Per Million",
#                                                            "Tests Per Confirmed Cases",
#                                                            "Tests Positivity Rate",
#                                                            "Individuals Tests Per Confirmed Case"])

#     # tested_df.to_csv("tested_data.csv", index=False)
#     # statewise_df.to_csv("statewise_data.csv", index=False)
#     # time_series_df.to_csv("time_series.csv", index=False)

    return {
        # "tested_df" : tested_df,
        "statewise_df" : statewise_df,
        "time_series_df" : time_series_df
    }

# # Complex do it later...
# # def state_districtwise_data():
# #     base_url = "https://api.covid19india.org/state_district_wise.json"

# #     response = requests.get(base_url)
# #     api_data = json.loads(response.text)

# #     print(api_data["Maharashtra"])
