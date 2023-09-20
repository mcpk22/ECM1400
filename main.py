# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

from reporting import*
from monitoring import*
from matplotlib import pyplot as mat_plot
import os


def main_menu():
    """Main Menu: asking the user to input a letter to access to the modules"""
    
    print("R - Pollution Reporting \nI - Mobility Intelligence \nM - Real-Time Montoring \nA - About \nQ - quit\n")
    reply = input("Choose an option \neg.type A for About: ")
    
    #By entering a letter (capital or small letter) access module
    if reply[0] == "R" or reply[0] =="r":
        reporting_menu()
    elif reply[0] == "I" or reply[0]== "i":
        intelligence_menu()
    elif reply[0] == "M" or reply[0]== "m":
        monitoring_menu()
    elif reply[0] == "A" or reply[0]== "a":
        about()
    elif reply[0] == "Q" or reply[0]== "q":
        quit()

def reporting_menu():
    """users to choose what data they want from which monitoring station"""
    #reading csv files

    data = open("project\project\data\Pollution-London Harlington.csv").readlines()
    data = open ("project\project\data\Pollution-London Marylebone Road.csv").readlines()
    data = open("project\project\data\Pollution-London N Kensington.csv").readlines()
    monitoring_station=["Marylebone Road","Harlington","N Kensington"]
    pollutant = ["no","pm10","pm25"]

    #choosing monitoring station
    print("M - Marylebone Road \nH - Harlington \nN - N Kensington")
    respond= input("Which station you to check? ")
    if respond[0]=="M" or respond[0]=="m":
        print("You chose Marylebone Road Station")
        monitoring_station="Marylebone Road"
    if respond[0]=="H" or respond[0]=="h":
        print("You chose Harlington Station")
        monitoring_station="Harlington"
    if respond[0]=="N" or respond[0]=="n":
        print("You chose N Kensington station")
        monitoring_station="N Kensington"

    #choosing which pollutant the user want to check
    print("N - Nitric Oxide \n1 - pm10 \n2 - pm2.5")
    ans = input("Which pollutant data you want to check? ")
    if ans[0]=="N" or ans[0]=="n":
        print("You chose Nitric Oxide")
        pollutant = "no"
    elif ans[0] =="1":
        print("You chose pm10")
        pollutant="pm10"
    elif ans[0]=="2":
        print("You chose pm25")
        pollutant="pm25"
    
    #printing the required data
    print("D - Daily Average \nN - Daily Median \nH - Hourly Average \nM - Monthly AVerage \nP - Peak Hour \nC - Counted Missing Data \nF - Filled Missing Data")
    reply = input("Which data do you want to get? ")
    new_value=[]
    date=[]
    if reply[0] == "D" or reply[0] == "d":
        print(daily_average(data, monitoring_station, pollutant))
    elif reply[0] == "N" or reply[0] == "n":
        print(daily_median(data, monitoring_station, pollutant))
    elif reply[0] == "H" or reply[0] == "h":
        print(hourly_average(data, monitoring_station, pollutant))
    elif reply[0] == "M" or reply[0] == "m":
        print(monthly_average(data, monitoring_station, pollutant))
    elif reply[0] == "P" or reply[0] == "p":
        date=input("Enter a date (YYYY-MM-DD):")
        print(peak_hour_date(data, date, monitoring_station,pollutant))
    elif reply[0] == "C" or reply[0] == "c":
        print(count_missing_data(data,  monitoring_station,pollutant))
    elif reply[0] == "F" or reply[0] == "f":
        new_value=input("Enter a new value: ")
        print(fill_missing_data(data, new_value,  monitoring_station,pollutant))
    print("\n")
    main_menu()
    #going back to the main menu




def monitoring_menu():
    """users to choose what kind of data they want to get"""
    
    print("D - Daily Average \nP - peak_hour \nS - Sum data \nM - Mean data")
    reply= input("Which data do you want to get? ")
    #printing required data
    if reply[0] == "D" or reply[0] == "d":
        print(Daily_average(site_code='MY1',species_code='NO',start_date=None,end_date=None))
    elif reply[0] == "P" or reply[0] == "p":
        print(peak_hour(site_code='MY1',species_code='NO',start_date=None,end_date=None))
    elif reply[0] == "S" or reply[0] == "s":
        print(sum_data(site_code='MY1',species_code='NO',start_date=None,end_date=None))
    elif reply[0] == "M" or reply[0] == "m":
        print(mean_data(site_code='MY1',species_code='NO',start_date=None,end_date=None))
    print("\n")
    main_menu()
    #going back to the main menu




def intelligence_menu():
    """users to choose what kind of data they want to get from this module"""
    
    print("R - open red pixel file \nC - open cyan pixel file \nT - text file ")
    reply= input("Which data do you want to get? ")
    #printing required data
    if reply[0] == "R" or reply[0] == "r":
        rgb_img = mat_plot.imread('map-red-pixels.jpg')
        mat_plot.imshow(rgb_img)
        mat_plot.show()
        #opening the red pixel image
    elif reply[0] == "C" or reply[0] == "c":
        rgb_img = mat_plot.imread('map-cyan-pixels.jpg')
        mat_plot.imshow(rgb_img)
        mat_plot.show()
        #opening the cyan pixel image
    elif reply[0] == "T" or reply[0] == "t":
       os.system("cc-output-2a.txt")
       #opening the text file
    main_menu()
    #going back to the main menu




def about():
    """Telling the user about the author"""
    
    #Having the Module Code, Candidate number
    ModuleCode = "ECM1400"
    CandidateNumber = "238086"
    print("module code:", ModuleCode)
    print("Candidate number:", CandidateNumber, "\n")
    #printing and showing Module Code, Candidate number to user
    main_menu()
    #going back to the main menu




def quit():
    """Function to exit the menu"""
    print("thanks,bye bye")
    exit()




if __name__ == '__main__':
    main_menu()