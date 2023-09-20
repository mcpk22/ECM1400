# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import numpy as np
import pandas as pd


#create an array for the pollutants
pollutant_list=["no","pm10","pm25"]

def check_type(values):
    '''
    Function recieves values in list 
    try if values in list is float(not non numerical)
    if yes return true
    if not return false
    
    Parameters:
        List:values
    Returns:
        true or false
    '''
    try:
        float(values)
        return True
    except:
        return False


def daily_average(data, monitoring_station, pollutant):
    """
    Function recieves data from csv file then calculate the daily average of each pollutant of each monitoring statiom

    Parameters:
        hour_1: the first hour of data
        hour_2: the second hour of data
        FirstCount:First item in data
        CountPerDay:Day count use to loop days
    Returns:
        daily average
    """
    #reading csv files
    
    if monitoring_station == "Marylebone Road":
        data = pd.read_csv("Pollution-London Marylebone Road.csv")
        specific_column = data[pollutant]  
    elif monitoring_station == "Harlington":
        data = pd.read_csv("Pollution-London Harlington.csv")
        specific_column = data[pollutant]    
    elif monitoring_station == "N Kensington":
        data = pd.read_csv("Pollution-London N Kensington.csv")
        specific_column = data[pollutant]


    hour_1=1
    hour_2=25
    #new list for returning daily average 
    Average_list = []
    #for loop finding daily average
    for days in range (365):
        array= specific_column[hour_1:hour_2]
        FirstCount=0
        CountPerDay=0
        for i in array:
            if i != "No data":
                #taking each value which is a float
                FirstCount = FirstCount + float(i)
                CountPerDay = CountPerDay +1
            else:
                continue
                #ignore "No data" values in the array 
        
            Daily_Average = FirstCount/CountPerDay
            #find daily average
            Daily_Average = round(Daily_Average,3)
        Average_list.append(Daily_Average) 
        hour_1 = hour_1+24
        hour_2 = hour_2+24
        days = days +1
    return Average_list
#test case #print (daily_average("","Marylebone Road", "pm25"))






def daily_median(data, monitoring_station, pollutant):
    """
    Function recieves data from csv file then calculate the daily median of each pollutant of each monitoring statiom

    Parameters:
        hour_1: the first hour of data
        hour_2: the second hour of data
        CountPerDay:Day count use to loop days
    Returns:
        daily median
    """
    
    #reading csv files
    if monitoring_station == "Marylebone Road":
        data = pd.read_csv("Pollution-London Marylebone Road.csv")
        specific_column = data[pollutant]  
    elif monitoring_station == "Harlington":
        data = pd.read_csv("Pollution-London Harlington.csv")
        specific_column = data[pollutant]    
    elif monitoring_station == "N Kensington":
        data = pd.read_csv("Pollution-London N Kensington.csv")
        specific_column = data[pollutant]

    hour_1=1
    hour_2=25
    #new list for returning median
    Median_list = []
    for days in range (365):
        array= specific_column[hour_1:hour_2]
        Sort_Array = []

        CountPerDay=0
        for i in array:
            if i != "No data":
                Sort_Array.append(i)
                CountPerDay = CountPerDay +1
            else:
                continue

        for i in range (1,len(Sort_Array)):
            test= Sort_Array[i]
            j =i-1
            while test < Sort_Array[j] and j >=0:
                Sort_Array[j+1] = Sort_Array[j]
                j=j-1
            Sort_Array[j+1]=test
        
        if CountPerDay%2 == 1:
            #length of datas in the array is even number
            Index = int(len(Sort_Array)/2)
            Median = Sort_Array[Index]
            Median_list.append(Median)
        else:
            #length of datas in the array is odd number
            Index_1 = int(len(Sort_Array)/2)
            Index_2 = int(len(Sort_Array)/2) -1
            if Index_2 > 1:
                Median = (float(Sort_Array[Index_1]) + float(Sort_Array[Index_2]))/2
                Median = round(Median,3)
                Median_list.append(Median)
               
        
        hour_1 = hour_1+24
        hour_2 = hour_2+24
        days = days +1
    return Median_list
#test case#print (daily_median("","Marylebone Road", "pm25"))




def hourly_average(data, monitoring_station, pollutant):
    """
    Function recieves data from csv file then calculate the hourly average of each pollutant of each monitoring statiom

    Parameters:
        hour_1: the first hour of data
        hour_2: the second hour of data
        FirstCount:First item in data
        CountPerDay:Day count use to loop days
    Returns:
        hourly average
    """
    
    #reading csv files
    if monitoring_station == "Marylebone Road":
        data = pd.read_csv("Pollution-London Marylebone Road.csv")
        specific_column = data[pollutant]  
    elif monitoring_station == "Harlington":
        data = pd.read_csv("Pollution-London Harlington.csv")
        specific_column = data[pollutant]    
    elif monitoring_station == "N Kensington":
        data = pd.read_csv("Pollution-London N Kensington.csv")
        specific_column = data[pollutant]
    
    hour_1 = 1
    hour_2 = 25
    #new list for returning the hourly average
    Hour_list = []
    for days in range (365):
        array = specific_column[hour_1:hour_2]
        FirstCount = 0
        CountPerDay = 0
        for i in array:
            if i != "No data":
                #taking each value which is a float
                FirstCount = FirstCount + float(i)
                CountPerDay = CountPerDay +1
            else:
                continue
            #ignoring "No data" values in array
            Hour_Average = FirstCount/CountPerDay
            #calculating hourly average
            Hour_Average = round(Hour_Average,3)
    
        hour_1 = hour_1 + 24
        hour_2 = hour_2 +24
        days = days + 1
        Hour_list.append(Hour_Average)
    return (Hour_list)

#print(hourly_average("","Marylebone Road", "pm25"))


def monthly_average(data, monitoring_station, pollutant):
    """
    Function recieves data from csv file then calculate the monthly average of each pollutant of each monitoring statiom

    Parameters:
        pollutant: pollutant data recorded in the csv file
    Returns:
        monthly average
    """
    
    #reading csv files
 
    data= open("project\project\data\Pollution-London Harlington.csv").readlines()
    data= open("project\project\data\Pollution-London Marylebone Road.csv").readlines()
    data= open("project\project\data\Pollution-London N Kensington.csv").readlines()

    #pollutant in columns
    if pollutant == "pm25":
            pollutant = 4
    elif pollutant == "pm10":
            pollutant = 3
    elif pollutant == "no":
            pollutant = 2

    #creating a list highlighting each month in data
    month = ["2021-01", "2021-02","2021-03","2021-04","2021-05","2021-06","2021-07","2021-08"
            ,"2021-09","2021-10", "2021-11", "2021-12"]

    #list for after striping spaces and commas
    month_list = []
    for line in data:
        line=line.strip()
        line=line.split(",")
        month_list.append(line)
   

    
    new_list=[]
    for value in month:
        temp_list=[]
        for list in month_list:
            if list[0][0:7]==value:
                temp_list.append(list[pollutant])
        new_list.append(temp_list)
    

    #new list for returning monthly average         
    month_average=[]
    for months in new_list:
        months_sum = 0
        count=0
        for values in months:
            if values != "No data":
                months_sum= months_sum+ float(values)
                count+=1
        average_ans=months_sum/count
        average_ans=round(average_ans,3)
        month_average.append(average_ans)
    return month_average

print(monthly_average("","Harlington", "no"))


def peak_hour_date(data, date, monitoring_station,pollutant):
    """
    Function recieves data from csv file then calculate the highest value read in a day of each pollutant of each monitoring statiom

    Parameters:
        pollutant: pollutant data recorded in the csv file
    Returns:
        peak hour date
    """

    #reading csv files
    data=open("project\project\data\Pollution-London Harlington.csv").readlines()
    data=open("project\project\data\Pollution-London Marylebone Road.csv").readlines()
    data=open("project\project\data\Pollution-London N Kensington.csv").readlines()
    
    #pollutant in columns
    if pollutant == "pm25":
        pollutant = 4
    if pollutant =="pm10":
        pollutant = 3
    if pollutant == "no":
        pollutant = 2

    peak_list=[]
    for line in data:
        line=line.strip()
        line=line.split(",")
        temp= line[0]
        

        if date == line[0]:
            peak_list.append(line[pollutant])

    peak=0
    for num in peak_list:
        if float(num)>peak:
            peak=float(num)
    return peak

#print(peak_hour_date("","2021-02-01","Harlington","pm25"))




def count_missing_data(data,  monitoring_station,pollutant):
    """
    Function recieves data from csv file then calculate the missing data of each pollutant of each monitoring statiom

    Parameters:
        missing data: find how many data is missing
    Returns:
        how many missing data
    """
    
    #reading csv files
    if monitoring_station == "Marylebone Road":
        data = pd.read_csv("Pollution-London Marylebone Road.csv")
        specific_column = data[pollutant]  
    elif monitoring_station == "Harlington":
        data = pd.read_csv("Pollution-London Harlington.csv")
        specific_column = data[pollutant]    
    elif monitoring_station == "N Kensington":
        data = pd.read_csv("Pollution-London N Kensington.csv")
        specific_column = data[pollutant]

    #assuming no data is missing
    missing_data=0
    for i in range (8760):
        if specific_column[i]=="No data":
            #every "No data" missing data +1
            missing_data +=1
        else:
            continue
    return missing_data

#print("There are", count_missing_data("", "Marylebone Road", "pm25"), "missing data")    

def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """
    Function recieves data from csv file then fill every missing data with a new value of each pollutant of each monitoring statiom

    Parameters:
        new_value: The value that filled "No data"
    Returns:
        filled data
    """
    
    #reading csv files
    if monitoring_station == "Marylebone Road":
        data = pd.read_csv("Pollution-London Marylebone Road.csv")
        specific_column = data[pollutant]  
    elif monitoring_station == "Harlington":
        data = pd.read_csv("Pollution-London Harlington.csv")
        specific_column = data[pollutant]    
    elif monitoring_station == "N Kensington":
        data = pd.read_csv("Pollution-London N Kensington.csv")
        specific_column = data[pollutant]
    for i in range(8760):
        if specific_column[i]=="No data":
            #if "No data" replace it by a new_value
            new_file=specific_column.replace("No data",new_value)
        else:
            continue
    print(new_file)

#fill_missing_data("", "1000", "Marylebone Road", "pm25")

