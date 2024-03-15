# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:12:32 2024

@author: NobertTurihohabwe
"""
import streamlit as st
import pandas as pd
import numpy as np



##Butuuro Sacco Data Cleaning Code
def Butuuro(df):
    try:
        df["sector"] = df['Line_of_business'] + " " + df['Loan_purpose']
        df["Loan_ID"] = df["Loan_ID"].astype(str)
        df["Borrower_ID"] = df["Borrower_ID"].astype(str)
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_birth"] = pd.to_datetime(df["Date_of_birth"],format='mixed')
    #df['Date_of_loan_issue'] = (df['Date_of_loan_issue'].str.replace(' 00:00:00','')).str.replace(' ','')
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_loan_issue"] = pd.to_datetime(df["Date_of_loan_issue"], format='mixed')#, dayfirst=False)
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_repayments_commencement"] = pd.to_datetime(df["Date_of_repayments_commencement"],format='mixed')
    except Exception as e:
        st.write(e)
    try:
        df["Expected_monthly_installment"] = df["Expected_monthly_installment"].round(0).astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df["Age"] = (((df["Date_of_loan_issue"] - df["Date_of_birth"]).dt.days)//365.25).astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df = df.drop(columns =['id','name_of_borrower', 'email_of_borrower', 'highest_education_level','Line_of_business', 'Loan_purpose',
                                        'employment_status', 'Loan_term_value','created','NIN', 'Phone_number',"Date_of_birth"])
    except Exception as e:
        st.write(e)
    try:
        df['Interest_rate'] = df['Interest_rate']*12/100
        df["Loan_type"] = df["Loan_type"].str.replace(" Client", "")
        #Add Age Group
        df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)
    #Add Sector
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                    'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing',
                                            'super market','buusiness'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'restaurant', 'baker', 'cook'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ["rent",'construct', 'estate','house renovation','house completion'],
        'Transport': ['transport', 'boda', 'motorcycle'],
        'Mining': ['mining', 'mineral','quarry'],
        # Add more sectors and their associated keywords as needed
    }

        # Create a new column 'sector' and initialize with 'Other'
    df['Sector'] = 'not_defined'
    try:
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        df.at[index, 'Sector'] = sector
                        break  # Exit the loop once a district is identified for the current row

    except Exception as e:
        st.write(e)




    #Add Districts
    # Define your Districts and corresponding keywords
    district_keywords = {
            'Kiruhura': ['kiruhura', 'kasaana', 'kinoni', 'rushere', 'kyabagyenyi','shwerenkye','kayonza', 'kikatsi',
                            'kihwa','kiguma','burunga','rwanyangwe','nyakashashara','ekikoni'],
            'Ibanda': ['ibanda', 'katongore','bihanga', 'rwetweka','mushunga','ishongororo', 'kikyenkye','nyakigando','nyarukiika',
                        'kagongo','bwengure','kabaare'],
            'Bushenyi': ['ishaka', 'bushenyi', 'kijumo','kabare','kakanju', 'nyamirembe','nkanga','nyabubare','bwekingo'],
            'Isingiro': ['isingiro', 'bushozi','Kabaare','ngarama','rwembogo','kabuyanda'],
            'Kazo': ['kazo', 'magondo', 'rwemikoma', 'kyabahura' 'Kyenshebashebe','ntambazi','kyabahura'],
            'Kibingo': ['buringo', 'masheruka','bwayegamba'],
            'Sheema': ['sheema','kabwohe', 'rwanama','mashojwa'],
            'Ntungamo': ['ntungamo','kyaruhanga','rubaare','katomi'],
            'Rukiga': ['rukiga', 'nyakambu','rwenyangye','kamwezi'],
            'Kagadi':['kagadi'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Rubirizi': ['rubirizi','kichwamba'],
            'Lyantonde': ['lyantonde'],
            'Mubende': ['mubende'],
            'Kitagwenda': ['kitagwenda'],
            'Lwengo': ['lwengo'],
            'Mayuge': ['mayuge'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Kole': ['kole'],
            'Fort Portal':['fort portal'],
            'Kanungu': ['kanungu'],
            'Mitooma': ['mitooma']
        
        # Add more districts and their associated keywords as needed
    }

        # Create a new column 'district' and initialize with 'Other'
    df['District'] = 'Other'
    try:
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        df.at[index, 'District'] = district
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)
    
    #Add Regions
    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                        'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                        'kibingo','kabarole'],
    
        # Add more regions and their associated keywords as needed
    }
    
    # Create a new column 'region' and initialize with 'Other'
    df['Region'] = 'Other'
    
    try:
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        df.at[index, 'Region'] = region
                        break  # Exit the loop once a Region is identified for the current row
    except Exception as e:
        st.write(e)
        ##End Butuuro Sacco
    return df





#Data Cleaning Code for Lyamujungu SACCO
def Lyamujungu(df):
    df["sector"] = df['Line_of_business'] + ' ' + df['Loan_purpose']
    try:
        df = df.drop(columns =['id','name_of_borrower', 'email_of_borrower', 'highest_education_level','employment_status',
                                'Date_of_birth','Loan_term_value','created','NIN', 'Phone_number','Line_of_business','Loan_purpose'])
    except Exception as e:
        st.write(e)
    try:
        df['Number_of_youth_employees'] = pd.to_numeric(df['Number_of_youth_employees'] ,errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df['Number_of_employees_that_are_refugees'] = pd.to_numeric(df['Number_of_employees_that_are_refugees'] ,errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df['Number_of_female_employees'] = pd.to_numeric(df['Number_of_female_employees'] ,errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df['Previously_unemployed'] = pd.to_numeric(df['Previously_unemployed'] ,errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df['Number_of_employees_with_disabilities'] = pd.to_numeric(df['Number_of_employees_with_disabilities'] ,errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df['Interest_rate'] = df['Interest_rate']/100
    except Exception as e:
        st.write(e)
            
    df['Loan_product_name'] = df['Loan_product_name'].str.replace("1-1-2-20 ","")

    try:
        df["Date_of_loan_issue"] = pd.to_datetime(df["Date_of_loan_issue"])
    except Exception as e:
        st.write(e)
    try:
        df["Length_of_time_running"] = pd.to_datetime(df["Length_of_time_running"], errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df["Length_of_time_running"] = df["Date_of_loan_issue"] - df["Length_of_time_running"]
    except Exception as e:
        st.write(e)
    try:
        df["Length_of_time_running"] = (df["Length_of_time_running"].dt.days//365).astype("Int64")
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_repayments_commencement"] = pd.to_datetime(df["Date_of_repayments_commencement"], errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df['Tenure_of_loan'] = (df['Tenure_of_loan']/30).astype(int)
    except Exception as e:
        st.write(e)
    df['Rural_urban'] = df['Rural_urban'].replace("0","")

    try:
        df['Number_of_employees'] = (pd.to_numeric(df['Number_of_employees'], errors='coerce')).astype("Int64")
    except Exception as e:
        st.write(e)
    try:
        df['Loan_amount'] = pd.to_numeric(df['Loan_amount'].str.replace(",","")).astype(int)
    except Exception as e:
        st.write(e)
    try:
        df['Expected_monthly_installment'] = pd.to_numeric(df['Expected_monthly_installment'].str.replace(",","")).astype(int)
    except Exception as e:
        st.write(e)
    df['Person_with_disabilities'] = df['Person_with_disabilities'].str.replace('false','No')

    try:
        df["Annual_revenue_of_borrower"] = pd.to_numeric(df["Annual_revenue_of_borrower"], errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        df["Annual_revenue_of_borrower"] = df["Annual_revenue_of_borrower"].astype("Int64")
    except Exception as e:
        st.write(e)
    try:
        df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)
    #AddSectors
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                    'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing',
                                            'super market'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'restaurant', 'baker', 'cook'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ["rent",'construct', 'estate','house renovation','house completion'],
        'Transport': ['transport', 'boda', 'motorcycle'],
        'Mining': ['mining', 'mineral','quarry'],
        # Add more sectors and their associated keywords as needed
    }

    # Create a new column 'sector' and initialize with 'Other'
    df['Sector'] = 'not_defined'
    try:
    # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        df.at[index, 'Sector'] = sector
                        break  # Exit the loop once a sector is identified for the current row

    except Exception as e:
        st.write(e)


    #Add Districts
    # Define your Districts and corresponding keywords
    district_keywords = {
            'Kiruhura': ['kiruhura', 'kasaana', 'kinoni', 'rushere', 'kyabagyenyi','shwerenkye','kayonza', 'kikatsi',
                            'kihwa','kiguma','burunga','rwanyangwe','nyakashashara','ekikoni'],
            'Ibanda': ['ibanda', 'katongore','bihanga', 'rwetweka','mushunga','ishongororo', 'kikyenkye','nyakigando','nyarukiika',
                        'kagongo','bwengure','kabaare'],
            'Bushenyi': ['ishaka', 'bushenyi', 'kijumo','kabare','kakanju', 'nyamirembe','nkanga','nyabubare','bwekingo'],
            'Isingiro': ['isingiro', 'bushozi','Kabaare','ngarama','rwembogo','kabuyanda'],
            'Kazo': ['kazo', 'magondo', 'rwemikoma', 'kyabahura' 'Kyenshebashebe','ntambazi','kyabahura'],
            'Kibingo': ['buringo', 'masheruka','bwayegamba'],
            'Sheema': ['sheema','kabwohe', 'rwanama','mashojwa'],
            'Ntungamo': ['ntungamo','kyaruhanga','rubaare','katomi'],
            'Rukiga': ['rukiga', 'nyakambu','rwenyangye','kamwezi'],
            'Kagadi':['kagadi'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Rubirizi': ['rubirizi','kichwamba'],
            'Lyantonde': ['lyantonde'],
            'Mubende': ['mubende'],
            'Kitagwenda': ['kitagwenda'],
            'Lwengo': ['lwengo'],
            'Mayuge': ['mayuge'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Kole': ['kole'],
            'Fort Portal':['fort portal'],
            'Kanungu': ['kanungu'],
            'Rubanda': ['rubanda']
        
        # Add more districts and their associated keywords as needed
    }

    # Create a new column 'district' and initialize with 'Other'
    df['District'] = 'Other'

    try:
    # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each district's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        df.at[index, 'District'] = district
                        break  # Exit the loop once a district is identified for the current row
    except Exception as e:
        st.write(e)

    #Add Regions:
    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                        'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                        'kibingo','kabarole','rubanda'],

        # Add more regions and their associated keywords as needed
    }

    # Create a new column 'region' and initialize with 'Other'
    df['Region'] = 'Other'
    try:
    # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        df.at[index, 'Region'] = region
                        break  # Exit the loop once a Region is identified for the current row
    except Exception as e:
        st.write(e)
    return df  
#End of Lyamujungu code







#Data Cleaning Code for Flow Uganda
def Flow(df):
#to the Flow_Data DataFrame and drop the Original Columns
    df["sector"] = df['Line_of_business'] + " " + df['Loan_purpose']

    try:
        df = df.drop(columns =['id','name_of_borrower', 'email_of_borrower', 'highest_education_level','Line_of_business', 'Loan_purpose',
                                'employment_status', 'Loan_term_value','created','NIN', 'Phone_number', "Date_of_birth"])
    except Exception as e:
        st.write(e)
    try:
    #Convert Duration to Total Years
        df['Length_of_time_running'] = df['Length_of_time_running'].fillna(' ')
        def convert_to_years(duration):
            parts = duration.split()
            if len(parts) == 4:
                total_years = int(parts[0]) + int(parts[2])//12
            elif len(parts) == 2 and parts[1] == 'months':
                total_years = int(parts[0])//12
            else:
                total_years = 0
            return total_years
    except Exception as e:
        st.write(e)
    try:
    # Apply the function to the 'duration' column
        df['Length_of_time_running'] = df['Length_of_time_running'].apply(convert_to_years)
    #Change Data Type
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_loan_issue"] = pd.to_datetime(df["Date_of_loan_issue"])
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_repayments_commencement"] = pd.to_datetime(df["Date_of_repayments_commencement"])
    except Exception as e:
        st.write(e)
    try:
        df['Gender'] = df['Gender'].str.title()
    except Exception as e:
        st.write(e)
    try:
        df['Tenure_of_loan'] = (df['Tenure_of_loan']/30).round(2)
    except Exception as e:
        st.write(e)
    try:
        df['Interest_rate'] = (df['Interest_rate']/df['Loan_amount'])*12/df['Tenure_of_loan']
    except Exception as e:
        st.write(e)
    try:
        df['Loan_type'] = df['Loan_type'].replace('SME','')
    except Exception as e:
        st.write(e)
    try:
        df['Age'] = df['Age'].astype(int)
    except Exception as e:
        st.write(e)
    try:
        df["Person_with_disabilities"] = df["Person_with_disabilities"].str.title()
    except Exception as e:
        st.write(e)
    try:
    #Add Age Group Column 
        df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)

    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                    'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing',
                                            'super market'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'restaurant', 'baker', 'cook'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ["rent",'construct', 'estate','house renovation','house completion'],
        'Transport': ['transport', 'boda', 'motorcycle'],
        'Mining': ['mining', 'mineral','quarry'],
        # Add more sectors and their associated keywords as needed
    }
    
    # Create a new column 'sector' and initialize with 'Other'
    df['Sector'] = 'not_defined'
    try:
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        df.at[index, 'Sector'] = sector
                        break  # Exit the loop once a sector is identified for the current row

    except Exception as e:
        st.write(e)
    
    
    # Define your Districts and corresponding keywords
    district_keywords = {
            "Moyo": ["moyo"],
            'Buikwe': ['buikwe','lugazi'],
            'Bugiri': ['bugiri'],
            'Soroti': ['soroti'],
            'Kagadi':['kagadi'],
            'Gulu': ['gulu'],
            'Kayunga': ['kayunga'],
            'Mbale': ['mbale'],
            'Pader': ['pader'],
            'Kamuli': ['kamuli'],
            'Namayingo': ['namayingo'],
            'Koboko': ['koboko'],
            'Mityana': ['mityana'],
            'Hoima': ['hoima'],
            'Nakasongola': ['nakasongola'],
            'Lira': ['lira'],
            'Butambala': ['butambala','kalamba'],
            'Rakai': ['rakai'],
            'Mpigi': ['mpigi'],
            'Sembabule': ['sembabule', 'sembambule'],
            'Arua': ['arua'],
            'Gomba': ['gomba'],
            'Bundibugyo': ['bundibugyo'],
            'Kiryandongo': ['kiryandongo', 'bweyale'],
            'Oyam': ['oyam'],
            'Bukwo': ['bukwo','bukwa'],
            'Lwengo': ['lwengo'],
            'Mayuge': ['mayuge'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Bulambuli': ['bulambuli'],
            'Luwero': ['luwero'],
            'Tororo': ['tororo'],
            'Serere': ['serere'],
            'Bunyangabu': ['bunyangabu'],
            'Pallisa': ['pallisa'],
            'Manafwa': ['manafwa'],
            'Kalungu': ['kalungu'],
            'Kyegegwa': ['kyegegwa','kyeggegwa'],
            'Kumi': ['kumi'],
            'Kakumiro': ['kakumiro'],
            'Kitgum': ['kitgum'],
            'Kanungu': ['kanungu'],
            'Kiboga': ['kiboga'],
            'Kapchorwa': ['kapchorwa'],
            'Kaliro': ['kaliro'],
            'Dokolo': ['dokolo'],
            'Apac': ['apac'],
            'Kabalore': ['nyamirima'],
            'Zombo': ['zombo'],
            'Nebbi': ['nebbi'],
            'Alebtong':['alebtong'],
            'Kibuku':['kibuku'],
            'Kyotera': ['kyotera','buwenge'],
            'Jinja': ['jinja'],
            'Kabarole': ['kabarole'],
            'Buvuma': ['buvuma'],
            "Yumbe": ["yumbe"],
            "Obongi": ["obongi"],
            "Adjumani": ["adjumani"],
            "Amuru": ["amuru"],
            "Katakwi": ["katakwii"],
            "Amuria": ["amuria"],
            "Bududa": ["bududa"],
            'Bukedea': ["bukedea"],
            "Nakaseke": ["nakaseke"],
            "Omoro": ["omoro"],
            "Kyankwanzi": ["kyankwanzi"],
            "Kasanda": ["kasanda"],
            'Kaberamaido': ['kaberamaido'],
            'Luuka': ['luuka'],
            'Butaleja': ['butaleja'],
            'Amolatar': ['amolatar'],
            'Iganga': ['iganga'],
            'Buyende': ['buyende'],
            'Ngora': ['ngora'],
            'Busia': ['busia']

        # Add more districts and their associated keywords as needed
    }
    
    # Create a new column 'district' and initialize with 'Other'
    df['District'] = 'Other'
    try:
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        df.at[index, 'District'] = district
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)


    region_keywords = {
    
            'Eastern': ['jinja','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku','katakwi',"amuria",
                        "bududa",'bukedea','luuka', 'kaberamaido','butaleja','iganga','ngora','buikwe','mayuge','buyende'],
    
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong',
                        'yumbe',"obongi","moyo", 'adjumani','omoro','amuru','amolatar']
    
        # Add more regions and their associated keywords as needed
    }
    
    # Create a new column 'region' and initialize with 'Other'
    df['Region'] = 'Other'
    try:
    # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        df.at[index, 'Region'] = region
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)
    return df
#End of Data Clleaning code for Flow







#Data Cleaning Code for Vision Fund
def VF(df):
    df["sector"] = df['Line_of_business'] + " " + df['Loan_purpose']
    try:
        df = df.drop(columns = ['Line_of_business', 'Loan_purpose'])
    except Exception as e:
        st.write(e)
    try:
        df = df.drop(columns =['id','name_of_borrower', 'email_of_borrower', 'highest_education_level',
                                'employment_status', 'Loan_term_value','created','NIN', 'Phone_number',"Date_of_birth"])
    except Exception as e:
        st.write(e)

    try:
        df["Borrower_ID"] = df["Borrower_ID"].astype(str)
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_loan_issue"] = pd.to_datetime(df["Date_of_loan_issue"])
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_repayments_commencement"] = pd.to_datetime(df["Date_of_repayments_commencement"])
    except Exception as e:
        st.write(e)
    try:
        df['Interest_rate'] = df['Interest_rate']*12/100
    except Exception as e:
        st.write(e)
    try:
        df["Gender"] = df["Gender"].str.title()
    except Exception as e:
        st.write(e)
    try:
        df["Person_with_disabilities"] = df["Person_with_disabilities"].str.title()
    except Exception as e:
        st.write(e)
    try:
        df["Rural_urban"] = df["Rural_urban"].str.title()
    except Exception as e:
        st.write(e)
    try:
        df["Length_of_time_running"] = df["Length_of_time_running"]//12
    except Exception as e:
        st.write(e)
        
    try:
    #Add Age Group Column 
        df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)
    
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                    'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing',
                                            'super market'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'restaurant', 'baker', 'cook'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ["rent",'construct', 'estate','house renovation','house completion'],
        'Transport': ['transport', 'boda', 'motorcycle'],
        'Mining': ['mining', 'mineral','quarry'],
        # Add more sectors and their associated keywords as needed
    }
    
    # Create a new column 'sector' and initialize with 'Other'
    df['Sector'] = 'not_defined'
    try:
    # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        df.at[index, 'Sector'] = sector
                        break  # Exit the loop once a sector is identified for the current row
    
    except Exception as e:
        st.write(e)


    # Define your Districts and corresponding keywords
    district_keywords = {
            "Moyo": ["moyo"],
            'Mbarara': ['mbarara'],
            'Kampala': ['kampala'],
            'Kiruhura': ['kiruhura'],
            'Ibanda': ['ibanda'],
            'Bushenyi': ['ishaka', 'bushenyi'],
            'Isingiro': ['isingiro'],
            'Kazo': ['kazo'],
            'Wakiso': ['wakiso', 'kyaliwajjala', 'nansana', 'entebbe', 'abayita', 'kireka'],
            'Kibingo': ['buringo', 'masheruka','bwayegamba'],
            'Sheema': ['sheema','kabwohe', 'rwanama','mashojwa'],
            'Ntungamo': ['ntungamo','kyaruhanga','rubaare','katomi'],
            'Rukiga': ['rukiga', 'nyakambu','rwenyangye','kamwezi'],
            'Kamwenge': ['kamwenge', 'kyabandara','bwizi t c'],
            'Masaka': ['masaka'],
            'Rukungiri': ['rukungiri'],
            'Iganga': ['iganga'],
            'Buikwe': ['buikwe','lugazi'],
            'Bugiri': ['bugiri'],
            'Soroti': ['soroti'],
            'Kagadi':['kagadi'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Gulu': ['gulu'],
            'Kayunga': ['kayunga'],
            'Mbale': ['mbale'],
            'Pader': ['pader'],
            'Kamuli': ['kamuli'],
            'Namayingo': ['namayingo'],
            'Koboko': ['koboko'],
            'Mityana': ['mityana'],
            'Hoima': ['hoima'],
            'Nakasongola': ['nakasongola'],
            'Kasese': ['kasese', 'bwera'],
            'Lira': ['lira'],
            'Mukono': ['mukono'],
            'Kyenjojo': ['kyenjojo'],
            'Masindi': ['masindi'],
            'Buhweju': ['buhweju','kabegaramire'],
            'Butambala': ['butambala','kalamba'],
            'Rakai': ['rakai'],
            'Mpigi': ['mpigi'],
            'Sembabule': ['sembabule', 'sembambule'],
            'Arua': ['arua'],
            'Rubanda': ['rubanda'],
            'Gomba': ['gomba'],
            'Bundibugyo': ['bundibugyo'],
            'Kiryandongo': ['kiryandongo', 'bweyale'],
            'Oyam': ['oyam'],
            'Mitooma': ['mitooma'],
            'Rubirizi': ['rubirizi','kichwamba'],
            'Lyantonde': ['lyantonde'],
            'Bukwo': ['bukwo','bukwa'],
            'Busia': ['busia'],
            'Mubende': ['mubende'],
            'Kitagwenda': ['kitagwenda'],
            'Lwengo': ['lwengo'],
            'Mayuge': ['mayuge'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Kole': ['kole'],
            'Fort Portal':['fort portal'],
            'Bulambuli': ['bulambuli'],
            'Luwero': ['luwero'],
            'Tororo': ['tororo'],
            'Serere': ['serere'],
            'Bunyangabu': ['bunyangabu'],
            'Pallisa': ['pallisa'],
            'Manafwa': ['manafwa'],
            'Kalungu': ['kalungu'],
            'Kyegegwa': ['kyegegwa','kyeggegwa'],
            'Kumi': ['kumi'],
            'Kakumiro': ['kakumiro'],
            'Kitgum': ['kitgum'],
            'Kanungu': ['kanungu'],
            'Kiboga': ['kiboga'],
            'Kapchorwa': ['kapchorwa'],
            'Kaliro': ['kaliro'],
            'Dokolo': ['dokolo'],
            'Apac': ['apac'],
            'Kabalore': ['nyamirima'],
            'Zombo': ['zombo'],
            'Nebbi': ['nebbi'],
            'Alebtong':['alebtong'],
            'Kibuku':['kibuku'],
            'Kyotera': ['kyotera','buwenge'],
            'Jinja': ['jinja'],
            'Kabarole': ['kabarole'],
            'Buvuma': ['buvuma'],
            "Yumbe": ["yumbe"],
            "Obongi": ["obongi"],
            "Adjumani": ["adjumani"],
            "Amuru": ["amuru"],
            "Katakwi": ["katakwii"],
            "Amuria": ["amuria"],
            "Bududa": ["bududa"],
            'Bukedea': ["bukedea"],
            "Nakaseke": ["nakaseke"],
            "Omoro": ["omoro"],
            "Kyankwanzi": ["kyankwanzi"],
            "Kasanda": ["kasanda"],
            'Luuka': ['luuka'],
            'Kaberamaido':['kaberimaido'],
            'Ngora': ['ngora']
            
            
        # Add more districts and their associated keywords as needed
    }
    
    # Create a new column 'district' and initialize with 'Other'
    df['District'] = 'Other'
    try:
    # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        df.at[index, 'District'] = district
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)

    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                        'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                        'kibingo','kabarole'],
            'Eastern': ['jinja','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku','katakwi',"amuria",
                        "bududa",'bukedea','luuka','kaberamaido','ngora'],
            'Central': ['kampala','luwero','kyotera','masaka','kayunga','mityana','sembabule','nakasongola','mukono','bukomansimbi',
                        'rakai','wakiso','mpigi','buikwe','gomba','lwengo','mayuge','butambala','lyantonde','mubende','kalungu',
                        'kiboga','butambala','buvuma','nakaseke','kyankwanzi','kasanda'],
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong',
                        'yumbe',"obongi","moyo", 'adjumani','omoro','amuru']
    
        # Add more regions and their associated keywords as needed
    }
    
    # Create a new column 'region' and initialize with 'Other'
    df['Region'] = 'Other'
    try:
    # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        df.at[index, 'Region'] = region
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)
    return df
#End of Vision Fund Code






#Data Cleaning Code for Other
def Other(df):
    try:
        df["sector"] = df['Line_of_business'] + " " + df['Loan_purpose']
    except Exception as e:
        st.write(e)

    try:
        df = df.drop(columns =['id','name_of_borrower', 'email_of_borrower', 'highest_education_level',
                               'employment_status', 'Loan_term_value','created','NIN', 'Phone_number'])
    except Exception as e:
        st.write(e)
    if df["Date_of_birth"].iloc[0] =='':
        df = df.drop(columns =["Date_of_birth"])
    try:
        df["Borrower_ID"] = df["Borrower_ID"].astype(str)
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_loan_issue"] = pd.to_datetime(df["Date_of_loan_issue"])
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_repayments_commencement"] = pd.to_datetime(df["Date_of_repayments_commencement"])
    except Exception as e:
        st.write(e)
    try:
        df['Interest_rate'] = df['Interest_rate']*100
    except Exception as e:
        st.write(e)
    try:
        df["Gender"] = df["Gender"].str.title()
    except Exception as e:
        st.write(e)
    try:
        df["Person_with_disabilities"] = df["Person_with_disabilities"].str.title()
    except Exception as e:
        st.write(e)
    try:
        df["Rural_urban"] = df["Rural_urban"].str.title()
    except Exception as e:
        st.write(e)
    try:
        df["Length_of_time_running"] = df["Length_of_time_running"]
    except Exception as e:
        st.write(e)
    try:
        df = df.drop(columns = ['Line_of_business', 'Loan_purpose'])
    except Exception as e:
        st.write(e)
    try:
    #Add Age Group Column 
        if df["Age"].iloc[0] == '':
            df["Age_Group"]='Calculate Age'
        else:                        
            df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)    

    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                    'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing',
                                            'super market'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'restaurant', 'baker', 'cook'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ["rent",'construct', 'estate','house renovation','house completion'],
        'Transport': ['transport', 'boda', 'motorcycle'],
        'Mining': ['mining', 'mineral','quarry'],
        # Add more sectors and their associated keywords as needed
    }

    try:
        # Create a new column 'sector' and initialize with 'Other'
        df['Sector'] = 'not_defined'
        
        # Iterate over each row in the DataFrame
        df['sector'] = df['sector'].fillna('Other')
        for index, row in df.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        df.at[index, 'Sector'] = sector
                        break  # Exit the loop once a sector is identified for the current row

    except Exception as e:
        st.write(e)

    # Define your Districts and corresponding keywords
    district_keywords = {
            "Moyo": ["moyo"],
            'Mbarara': ['mbarara'],
            'Kampala': ['kampala'],
            'Kiruhura': ['kiruhura'],
            'Ibanda': ['ibanda'],
            'Bushenyi': ['ishaka', 'bushenyi'],
            'Isingiro': ['isingiro'],
            'Kazo': ['kazo'],
            'Wakiso': ['wakiso', 'kyaliwajjala', 'nansana', 'entebbe', 'abayita', 'kireka'],
            'Kibingo': ['buringo', 'masheruka','bwayegamba'],
            'Sheema': ['sheema','kabwohe', 'rwanama','mashojwa'],
            'Ntungamo': ['ntungamo','kyaruhanga','rubaare','katomi'],
            'Rukiga': ['rukiga', 'nyakambu','rwenyangye','kamwezi'],
            'Kamwenge': ['kamwenge', 'kyabandara','bwizi t c'],
            'Masaka': ['masaka'],
            'Rukungiri': ['rukungiri'],
            'Iganga': ['iganga'],
            'Buikwe': ['buikwe','lugazi'],
            'Bugiri': ['bugiri'],
            'Soroti': ['soroti'],
            'Kagadi':['kagadi'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Gulu': ['gulu'],
            'Kayunga': ['kayunga'],
            'Mbale': ['mbale'],
            'Pader': ['pader'],
            'Kamuli': ['kamuli'],
            'Namayingo': ['namayingo'],
            'Koboko': ['koboko'],
            'Mityana': ['mityana'],
            'Hoima': ['hoima'],
            'Nakasongola': ['nakasongola'],
            'Kasese': ['kasese', 'bwera'],
            'Lira': ['lira'],
            'Mukono': ['mukono'],
            'Kyenjojo': ['kyenjojo'],
            'Masindi': ['masindi'],
            'Buhweju': ['buhweju','kabegaramire'],
            'Butambala': ['butambala','kalamba'],
            'Rakai': ['rakai'],
            'Mpigi': ['mpigi'],
            'Sembabule': ['sembabule', 'sembambule'],
            'Arua': ['arua'],
            'Rubanda': ['rubanda'],
            'Gomba': ['gomba'],
            'Bundibugyo': ['bundibugyo'],
            'Kiryandongo': ['kiryandongo', 'bweyale'],
            'Oyam': ['oyam'],
            'Mitooma': ['mitooma'],
            'Rubirizi': ['rubirizi','kichwamba'],
            'Lyantonde': ['lyantonde'],
            'Bukwo': ['bukwo','bukwa'],
            'Busia': ['busia'],
            'Mubende': ['mubende'],
            'Kitagwenda': ['kitagwenda'],
            'Lwengo': ['lwengo'],
            'Mayuge': ['mayuge'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Kole': ['kole'],
            'Fort Portal':['fort portal'],
            'Bulambuli': ['bulambuli'],
            'Luwero': ['luwero'],
            'Tororo': ['tororo'],
            'Serere': ['serere'],
            'Bunyangabu': ['bunyangabu'],
            'Pallisa': ['pallisa'],
            'Manafwa': ['manafwa'],
            'Kalungu': ['kalungu'],
            'Kyegegwa': ['kyegegwa','kyeggegwa'],
            'Kumi': ['kumi'],
            'Kakumiro': ['kakumiro'],
            'Kitgum': ['kitgum'],
            'Kanungu': ['kanungu'],
            'Kiboga': ['kiboga'],
            'Kapchorwa': ['kapchorwa'],
            'Kaliro': ['kaliro'],
            'Dokolo': ['dokolo'],
            'Apac': ['apac'],
            'Kabalore': ['nyamirima'],
            'Zombo': ['zombo'],
            'Nebbi': ['nebbi'],
            'Alebtong':['alebtong'],
            'Kibuku':['kibuku'],
            'Kyotera': ['kyotera','buwenge'],
            'Jinja': ['jinja'],
            'Kabarole': ['kabarole'],
            'Buvuma': ['buvuma'],
            "Yumbe": ["yumbe"],
            "Obongi": ["obongi"],
            "Adjumani": ["adjumani"],
            "Amuru": ["amuru"],
            "Katakwi": ["katakwii"],
            "Amuria": ["amuria"],
            "Bududa": ["bududa"],
            'Bukedea': ["bukedea"],
            "Nakaseke": ["nakaseke"],
            "Omoro": ["omoro"],
            "Kyankwanzi": ["kyankwanzi"],
            "Kasanda": ["kasanda"],
            'Luuka': ['luuka'],
            'Kaberamaido':['kaberimaido']
            
        # Add more districts and their associated keywords as needed
    }

    # Create a new column 'district' and initialize with 'Other'
    try:
        df['District'] = 'Other'
        
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        df.at[index, 'District'] = district
                        break  # Exit the loop once a sector is identified for the current row
        
    except Exception as e:
        st.write(e)

    try:
        region_keywords = {
                'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                            'masindi','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                            'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                            'kibingo','kabarole'],
                'Eastern': ['jinja','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                            'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku','katakwi',"amuria",
                            "bududa",'bukedea','luuka','kaberamaido'],
                'Central': ['kampala','luwero','kyotera','masaka','kayunga','mityana','sembabule','nakasongola','mukono','bukomansimbi',
                            'rakai','wakiso','mpigi','buikwe','gomba','lwengo','mayuge','butambala','lyantonde','mubende','kalungu',
                            'kiboga','butambala','buvuma','nakaseke','kyankwanzi','kasanda'],
                'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong',
                            'yumbe',"obongi","moyo", 'adjumani','omoro','amuru']
        
            # Add more regions and their associated keywords as needed
        }
        
        # Create a new column 'region' and initialize with 'Other'
        df['Region'] = 'Other'
        
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        df.at[index, 'Region'] = region
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)  
    return df
