#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


# In[2]:


class climate_change:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def read_world_bank_data(self):
        countries = pd.read_csv(self.file_path, index_col = 'date')
        years = countries.T.rename_axis(None, axis = 1)
        return years, countries

    def plot_bar(self):
        '''
        This function accepts the path to data, creates dataframe with years as columns and
        selects data after every 5 years and transposes years to columns and plots them
        '''
        _, df1 = self.read_world_bank_data()
        np.random.seed(45) # Get the same random samples below
        df1 = df1[::5].T.sample(13) # Every 5 year data        
        df1.plot(kind = 'bar', figsize = (7,4))
        plt.title(f"{self.file_path[:-4]}")
        plt.xlabel('Country Name')
        plt.legend(bbox_to_anchor = [1, 1])
        plt.show()
        
    def plot_line(self):
        '''
        This function produces line plots
        '''
        df, _ = self.read_world_bank_data()
        np.random.seed(45) # Get same random sample below
        df = df.sample(13).T
        df.plot(kind ='line', linestyle = '--')
        plt.title(f'{self.file_path[:-4]}')
        plt.xlabel('Year')
        plt.legend(bbox_to_anchor = [1,0.8])
        plt.show()
        
    def display_describe(self):
        '''
        This function displays the data after each ten year period, focusing on the 
        dataframe with years as column
        '''
        df, _ = self.read_world_bank_data()
        np.random.seed(45)
        return df.sample(13).T.describe().T
    
    # Static method is defined below, accepts arguments not class instances
    @staticmethod
    def plot_heatmap(files, cmap):
        country = input("Enter the name of the country (e.g China): ")  # Ask for the country to display its correlations 
        i = 0
        names = [] # Initialize empty list
        for file in files:
            names.append(file[:-4]) # Save the column names to list
            countries = pd.read_csv(file, index_col = 'date')
            country_df = countries[country]
            if i == 0:
                df = country_df
                i += 1
            else:
                df = pd.concat([df, country_df], axis = 1)
        df.columns = names # Set the column names        
        corr_df = df.dropna().corr() # Correlation        
        
        plt.figure(figsize = (8,8))
        plt.imshow(corr_df, cmap = cmap) # Plot correlation heatmap
        plt.colorbar()
        for i in range(corr_df.shape[0]):
            for j in range(corr_df.shape[0]):
                plt.annotate(f"{corr_df.iloc[i,j]:.2f}", (i, j)) # Annotate
        plt.xticks(range(corr_df.shape[0]), corr_df.columns, rotation = 90)
        plt.yticks(range(corr_df.shape[0]), corr_df.columns)
        plt.title(f"{country}")
        plt.show()


# In[3]:


# Get the file names from directory
csv_files = [path for path in os.listdir() if '.csv' in path]

# Mortality Rate Bar Plot
mortality = climate_change('Mortality rate, under-5 (per 1,000 live births).csv')
print("Mortality Bar Plot")
mortality.plot_bar()

# Investigating Correlation in > Input = Korea, Rep.
print("\nCorrelation Heatmap Korea, Rep.")
mortality.plot_heatmap(csv_files[:-1], "viridis")

# Line Plot of 13 random countries
print("Line Plot for 13 countries")
mortality.plot_line()

# Investigating Correlation in > Input = Tanzania
print("\nCorrelation Heatmap Tanzania")
mortality.plot_heatmap(csv_files[:-1], "plasma")

###############################
# Agricultural Land Bar plot
print("\nAgricultural Land Bar Plot")
agri = climate_change("Agricultural land (sq. km).csv")
agri.plot_bar()

# Line Plot of 13 random countries
print("Line Plot for 13 countries")
agri.plot_line()

# Investigating Correlation in > Input = Montenegro
print("\nCorrelation Heatmap Montenegro")
agri.plot_heatmap(csv_files[:-1], "inferno")


# In[4]:


# Descriptive statistics
agri = climate_change("Agricultural land (sq. km).csv")

# Display data in 10 year gaps
print("Agricultural land Data after Every 10 years")
agri.display_describe()


# In[ ]:




