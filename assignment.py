# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:23:27 2023
@author: Ushas 

This code plots 3 different visualisations that is line plot, stacked barplot 
and pie plot using 2 different data sets.
"""

#Import required packages
import matplotlib.pyplot as plt
import pandas as pd

#Read the file into "rate"
rate = pd.read_excel("Mortality_rate.xlsx")
print(rate)

#Function to plot line plot
def line_plot(line):
    """
    This line_plot function plots line graph of child mortality rate under 
    5 years old (per 1,000 live births) of 4 countries between 1995 to 2020.
    
    Parameters
    ----------
    line : This parameter passes the values of selected 4 countries' child 
    mortality rate with respect to the years.

    Returns
    -------
    None.

    """
    
    
    plt.figure()
    plt.plot(line["year"], line["South Africa"], label="South Africa")
    plt.plot(line["year"], line["Nigeria"], label="Nigeria")
    plt.plot(line["year"], line["United Kingdom"], label="United Kingdom")
    plt.plot(line["year"], line["India"], label="India")

    #Settng Title and Labels
    plt.title("Mortality Rate Over Years")
    plt.xlabel("Year")
    plt.ylabel("Mortality rate")
    
    #removing white space from Left & right side of the graph
    plt.xlim(1995, 2020)
    plt.legend()
    plt.savefig("lineplot.png")
    plt.show()
 
#Calling function to creat line plot
line_plot(rate)

 
#Function to plot bar plot  
def bar_plot(bar):
    """
    From 1995 through 2020, this bar_plot function creates a stacked bar graph
    showing child mortality rates under 5 years old (per 1,000 live births) 
    in three countries.
    
    Parameters
    ----------
    bar : This parameter passes the values of the selected four countries' 
    child mortality rates in relation to the years.

    Returns
    -------
    None.

    """
    
    plt.figure()
    plt.bar(bar["year"], bar["United States"], label="United States",
            alpha=0.5 )
    plt.bar(bar["year"], bar["Canada"], label="Canada")
    plt.bar(bar["year"], bar["Australia"], label="Australia",  alpha=0.6)
    
    #Settng Title and Labels
    plt.legend()
    plt.xlabel("Year")
    plt.ylabel("Mortality rate")
    plt.title("Mortality Rate Over Years")
    plt.savefig("barplot.png")
    plt.show()

#Calling function to creat bar plot    
bar_plot(rate)   

#Read the file into "international"
international = pd.read_excel("international_mobility_ratio.xlsx")
print(international)

#Function to plot pie plot
def pie_plot(pie):
    """
    This pie_plot function represnts inbound & outbound International students 
    mobility ratio between 5 countries in the year 2018.

    Parameters
    ----------
    pie : This parameter passes the values of the selected 5 countries' 
    International Mobility Ratio.

    Returns
    -------
    None.

    """
    #ploting pie plots as two subplots
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1)
    plt.pie(international["Outbound mobility ratio"], 
            labels=international["country"], autopct="%1.f%%" )
    plt.title("Outbound International Mobility Ratio")


    plt.subplot(2, 2, 2)
    plt.pie(international["Inbound mobility rate"],
            labels=international["country"], autopct="%1.f%%" )
    
    #Settng Title and Labels
    plt.title("Inbound International Mobility Ratio")
    plt.savefig("pieplot.png")
    plt.show()

#Calling function to creat pie plot    
pie_plot(international)

    
    
    
