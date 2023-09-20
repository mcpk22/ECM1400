# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#
import pandas as pd
import requests
import datetime

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    

    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url).json()
    data_frame= pd.DataFrame(res)
    data_frame= data_frame.iloc[2]
    result= data_frame.item()
    
    values=[]
    for element in result:
        if element ["@Value"] != "":
            values.append(element ["@Value"])
    print (values)


#print(get_live_data_from_api())

def Daily_average(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    This Function is to retrieve data from API and then calculate the daily average of the datas collected
    
    """
    
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url).json()
    data_frame= pd.DataFrame(res)
    data_frame= data_frame.iloc[2]
    result= data_frame.item()
    
    #create list to store float numbers 
    values=[]
    for element in result:
        if element ["@Value"] != "":
            values.append(element ["@Value"])
    
    #FirstCount:First item in data
    #CountPerDay:Day count use to loop days
    FirstCount=0
    CountPerDay=0
    for i in values:
        FirstCount= FirstCount+1
        CountPerDay= CountPerDay +float(i)
    if FirstCount != 0:
        average=CountPerDay/FirstCount
        #calculate the daily average
        print("The average is ",average)
    else:
        return None

#print (Daily_average())  
        

def peak_hour(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    This Function is to retrieve data from API and then calculate the peak hour data of the datas collected
    """
    # Your code goes here
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url).json()
    data_frame= pd.DataFrame(res)
    data_frame= data_frame.iloc[2]
    result= data_frame.item()
    
    #create list to store float numbers 
    values=[]
    for element in result:
        if element ["@Value"] != "":
            values.append(element ["@Value"])
    

    peak = 0
    for num in values:
        if float(num) > peak:
            peak = float(num)
            print("The peak data is ",peak)
        else:
            return None


#print(peak_hour())


def sum_data(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    This Function is to retrieve data from API and then calculate the sum of the datas collected
    """
   
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url).json()
    data_frame= pd.DataFrame(res)
    data_frame= data_frame.iloc[2]
    result= data_frame.item()
    
    #create list to store float numbers 
    values=[]
    for element in result:
        if element ["@Value"] != "":
            values.append(element ["@Value"])
    
    
    count=0
    for i in values:
        count=count+float(i)
    print("The sum is ",count)
    

#print(sum_data())


def mean_data(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """Your documentation goes here"""
    # Your code goes here
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url).json()
    data_frame= pd.DataFrame(res)
    data_frame= data_frame.iloc[2]
    result= data_frame.item()
    
    values=[]
    for element in result:
        if element ["@Value"] != "":
            values.append(element ["@Value"])
    
    
#print(mean_data())

