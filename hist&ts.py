#Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import os


# List of lists

listOfFileNames = []
listDataFramesForHist = []
listDataFramesForTimeSeries = []



for files in os.walk("./set-a"):
    for filename in files:
        listOfFileNames.append(filename)



# For Histograms
for filename in listOfFileNames:
    d = pd.read_csv("./set-a/" + filename)
    d.Time = d.Time.map(lambda x: "00:"+x)
    listDataFramesForTimeSeries.append(d)   
    d = d.drop(columns=['Time'])
    e = d.groupby(['Parameter']).agg({'Value':'mean'})
    listDataFramesForHist.append(e.T)
    
 
# Concatenate all dataframes in list into single dataframe
DfForHistogram = pd.concat(listDataFramesForHist)


# Plot histograms of each column
DfForHistogram.hist(figsize=(20,20), color= 'red')


                





                            
                    # FOR TIMESERIES

ts = listDataFramesForTimeSeries[4]
ts.Time = pd.to_datetime(ts.Time,format= '%H:%M:%S').dt.time # converting into Time type
groups = ts.groupby('Parameter')

Temp_test = groups.get_group('Temp')
Temp_test.info()


Temp_test.set_index(Temp_test.Time, inplace=True)
Temp_test = Temp_test.drop(columns=['Time'])



Temp_test.plot(figsize=(10,5), linewidth=1, fontsize=17, color= 'red')
plt.xlabel('Time', fontsize=17);plt.ylabel('Temp',fontsize=17)




