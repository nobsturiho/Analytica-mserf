# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 15:36:11 2023

@author: Nobert Turihohabwe
"""
#pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
import functions as fx
   

#Develop DashBoard
st.header('Project Analytica (MSE Recovery Fund)')


#Add Sidebar to DashBoard
add_sidebar = st.sidebar.selectbox('Category',('Data_Cleaning','About The Fund','Impact Measurement','PFI Comparison'))

if add_sidebar == 'About The Fund':
    st.write('The Micro and Small Enterprises (MSE) Recovery Fund is a 5-year, USD 20MN (approximately UGX 70 Bn)',
             'initiative under the Mastercard Foundation Young Africa Works program, established in partnership with',
             ' Financial Sector Deepening (FSD) Uganda to offset the shocks of the COVID-19 pandemic on the economy of',
             ' Uganda through investments in Micro and Small Enterprises, via Tier III and Tier IV financial institutions.')




#Develop Impact Measurement DashBoard
if add_sidebar == 'Impact Measurement':
    st.subheader('Impact Measurement: To be completed')

    
    

#Develop PFI Comparison DashBoard
if add_sidebar == 'PFI Comparison':
    st.write('PFI Comparison: To be Completed')



#Develop Data Cleaning DashBoard
if add_sidebar == 'Data_Cleaning':
    st.subheader('Import file to clean')
    
    #Add file uploader widget
    uploaded_file = st.file_uploader("Choose an excel file", type="xlsx")
    
    if uploaded_file is not None:
        # Read the file file into a DataFrame
        df = pd.read_excel(uploaded_file)
        lender = df['lender'].iloc[0]
    
        # Display the DataFrame
        st.subheader("Preview of the raw data:")
        st.write("The shape is: ",df.shape)
        st.write("The lender is :",lender)
        st.write(df.head())
        
        
        #Add Data Cleaning Button
        if st.button("Click to Clean Data"):
            
            #Clean the data

            #Data Cleaning for Mushanga SACCO 
            if df['lender'].iloc[0] == 'Mushanga SACCO':
                df = fx.Mushanga(df)
            #Data Cleaning for Butuuro SACCO                   
            elif df['lender'].iloc[0] == 'Butuuro SACCO':
               df = fx.Butuuro(df)
            #Data Cleaning for Premier Credit 
            elif df['lender'].iloc[0] == 'Premier Credit':
               df = fx.Premier(df)
                
            #Data Cleaning for Finca
            elif df['lender'].iloc[0] == 'FINCA Uganda':
               df = fx.Finca(df)
                
            #Data Cleaning for Lyamujungu SACCO
            elif df['lender'].iloc[0] == 'Lyamujungu SACCO':
               df = fx.Lyamujungu(df)
                                
            #Data Cleaning Code for Flow Uganda                   
            elif df['lender'].iloc[0] == 'Flow Uganda':
               df = fx.Flow(df)

            #Data Cleaning Code for Vision Fund                   
            elif df['lender'].iloc[0] == 'Vision Fund':
               df = fx.VF(df)

                
            #Data Cleaning Code for Other PFI                  
            else:
               df = fx.Other(df)
                



            #Print the cleaned dataframe
            st.subheader('Preview the Clean Data')
            st.write('The shape is: ',df.shape)
            st.write(df.head())
            
            
            #Export Clean File
            st.subheader('Export Clean File')
            
            # Create an expandable section for additional export options
            with st.expander("Export Clean Data"):
                
                lender = df['lender'].iloc[0]
                import calendar
                month = calendar.month_name[int(df['month'].iloc[0])]
                #Add button to Download Data
                st.download_button(
                    label="Click to Download Clean File",
                    data=df.to_csv(index=False),  # Convert DataFrame to Excel data
                    file_name= f"{lender}_{month}_Clean_Data.csv",  # Set file name
                )
                
                
                
            
            #Add Portfolio Monitoring Fields
            st.subheader('Portfolio Monitoring')
            st.write('Impact Measurement')
            
            #Add Columns
            col1, col2, col3 = st.columns(3)
            with col1:
                Loans = df['Loan_ID'].count()
                st.metric('Number of Loans', Loans,0)
            with col2:
                Amount = format(df['Loan_amount'].sum(), ',')
                st.metric('Loan Amount (UGX)', Amount, 0)
            with col3:
                Ticket = format(round(df['Loan_amount'].mean(),0), ',')
                st.metric('Avg Tickets (UGX)', Ticket, 0)
            with col1:
                Interest = round((df['Interest_rate'].mean())*100,1)
                st.metric('Average Interest (%)', Interest, 0)
            with col2:
                Gender = pd.DataFrame(df.groupby(by ='Gender').count()['year']).rename(columns = {'year':'Number'})
                Women = (Gender.iloc[0,0]/(Gender['Number'].sum())*100).round(1)
                st.metric('Pct Women (%)', Women, 0)
            with col3:
                Age_Group = pd.DataFrame(df.groupby(by ='Age_Group').count()['year']).rename(columns = {'year':'Number'})
                Youths = (Age_Group.iloc[-1,0]/(Age_Group['Number'].sum())*100).round(1)
                st.metric('Pct Youths (%)', Youths, 0)
                
            st.subheader('Loan Type')
            Loan_type = pd.DataFrame(df['Loan_type'].unique()).rename(columns = {0:'Loan Type'})
            st.write(Loan_type)
            
            st.subheader('Number of Women Borrowers')
            try:
                Gender_df = pd.DataFrame(df.groupby('Gender')['Loan_amount'].count())
                Gender_df = Gender_df.rename(columns = {"Loan_amount":"Number"})
                Gender_df["Percent (%)"] = (Gender_df["Number"]*100/sum(Gender_df["Number"])).round(2)
                st.write(Gender_df)
            except Exception:
                st.write("Error")
                
            st.subheader('Number of Youth Borrowers')
            try:
                Age_Group_df = pd.DataFrame(df.groupby('Age_Group')['Loan_amount'].count())
                Age_Group_df = Age_Group_df.rename(columns = {"Loan_amount":"Number"})
                Age_Group_df["Percent (%)"] = (Age_Group_df["Number"]*100/sum(Age_Group_df["Number"])).round(2)
                st.write(Age_Group_df)
            except Exception:
                st.write("Error")
                
            st.subheader('Economic Sectors Served')
            try:
                Sector_df = pd.DataFrame(df.groupby('Sector')['Loan_amount'].count())
                Sector_df = Sector_df.rename(columns = {"Loan_amount":"Number"})
                Sector_df["Percent (%)"] = (Sector_df["Number"]*100/sum(Sector_df["Number"])).round(2)
                st.write(Sector_df)
            except Exception:
                st.write("Error")
            
            st.subheader('Average Revenue of Borrowers')
            try:
                Annual_Revenue = format(round(df['Annual_revenue_of_borrower'].mean(), 0), ',')
                st.metric('Average Revenue (UGX)',Annual_Revenue)
            except Exception:
                st.write("Error")
            
            st.subheader('Average Number of Employees')
            try:
                employees = round(df['Number_of_employees'].mean(), 0)
                st.metric('Average number of employees:', employees)
            except Exception:
                st.write("Error")
