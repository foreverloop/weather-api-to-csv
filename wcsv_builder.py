#the csv will be built up over a number of days, appending the existing file
import requests,json,csv,ast,datetime
import pandas as pd

with open("endpoint.csv","r") as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        endpoint = row[0]
        
five_day_forecast = json.loads(requests.get(endpoint).text)

#header (decode headers on met office api site): pandas_frame_no,$,D,F,G,H,Pp,S,T,U,V,W,forecast_date
for forecast in five_day_forecast["SiteRep"]["DV"]["Location"]["Period"]:
    df = pd.DataFrame(forecast["Rep"])
    df2 = pd.DataFrame(forecast)
    final_df = pd.concat([df,df2["value"]],axis=1)
    final_df.to_csv("forca3hr.csv",mode='a',header=False)

#log to check to avoid duplicating data etc
time_gathered = "{0}".format(datetime.datetime.now())
with open("collection_log_wea.csv",'a') as f:
    f.write("\n" + time_gathered)