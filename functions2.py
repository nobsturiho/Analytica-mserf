# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:12:32 2024

@author: NobertTurihohabwe
"""
import streamlit as st
import pandas as pd
import numpy as np


##Premier Credit Data Cleaning Code
def letshego(df):
    deleted_columns=['id','NIN','Phone_number','name_of_borrower','email_of_borrower','highest_education_level','employment_status','created','Age','Loan_term_value']
    df=df.drop(columns=deleted_columns)
    df['Loan_ID'] = df['Loan_ID'].astype(str)
    df['Borrower_ID'] = df['Borrower_ID'].astype(str)
    df['Sector'] = df['Line_of_business'] +' '+ df['Loan_purpose']
    df= df.drop(columns=['Line_of_business','Loan_purpose'])
    df['Gender'] = df['Gender'].replace('F','Female')
    df['Gender'] = df['Gender'].replace('M','Male')
    df['Date_of_birth'] = pd.to_datetime(df['Date_of_birth'])
    df['Date_of_loan_issue'] = pd.to_datetime(df['Date_of_loan_issue'])
    df['Age'] = df['Date_of_loan_issue'].dt.year - df['Date_of_birth'].dt.year
    df = df.drop(columns=['Date_of_birth'])
    df['Date_of_repayments_commencement'] = pd.to_datetime(df['Date_of_repayments_commencement'])
    df['Interest_rate'] = df['Interest_rate'].replace(30,0.3)
    df['Loan_type'] = df['Loan_type'].replace('New Loan','Individual')
    df['Expected_number_of_installments'] = df['Expected_number_of_installments'].astype(int)
    df['Expected_monthly_installment'] = df['Expected_monthly_installment'].astype(int)
    df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    
    
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                  'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing'],
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
    df['sector'] = 'not_defined'
    
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        line_of_business = row['Sector'].lower()
        
        # Check for each sector's keywords in the 'line_of_business' column
        for sector, keywords in sector_keywords.items():
            for keyword in keywords:
                if keyword in line_of_business:
                    df.at[index, 'sector'] = sector
                    break  # Exit the loop once a sector is identified for the current row
    
    
    df.drop(columns="Sector", inplace=True)
    df.rename(columns={'sector': 'Sector'}, inplace=True)
    
    
    # Define your Districts and corresponding keywords
    district_keywords = {
            'Mbarara': ['mbarara', 'kinoni t/c', 'kitunguru', 'ruhunga','rubaya', 'bwizibwera', 'kakoba', 'rwebishekye', 
                        'rwanyamahembe', 'kakoba', 'rwentondo', 'rubingo','rukiro', 'kashari', 'rwentojo', 'nyarubungo','bukiro',
                        'katyazo', 'rutooma', 'ngango','kagongi', 'nkaaka', 'rugarama','katete','nyamitanga', 'mwizi','rwampara',
                        'omukagyera,','mirongo','Kashare', 'omukagyera','kamushoko', 'bubaare','kyantamba', 'rwanyampazi','kamukuzi',
                       'kashaka','kobwoba','igorora t/c','ntuura','kashenyi','nyabisirira','rubindi','byanamira','nchune','kariro',
                        'rwebikoona','mitoozo','bunenero','nyantungu'],
            'Kampala': ['kampala', 'ben kiwanuka', 'nateete', 'katwe','city centre','kawempe','kabalagala','nakulabye','nakawa','masajja',
                        'entebbe road','wandegeya', 'ntinda', 'acacia', 'bukoto','luku','nsambya','bulenga','bunono','central','haji'],
            'Kiruhura': ['kiruhura', 'kasaana', 'kinoni', 'rushere', 'kyabagyenyi','shwerenkye','kayonza', 'kikatsi',
                         'kihwa','kiguma','burunga','rwanyangwe','nyakashashara','ekikoni'],
            'Ibanda': ['ibanda', 'katongore','bihanga', 'rwetweka','mushunga','ishongororo', 'kikyenkye','nyakigando','nyarukiika',
                       'kagongo','bwengure','kabaare'],
            'Bushenyi': ['ishaka', 'bushenyi', 'kijumo','kabare','kakanju', 'nyamirembe','nkanga','nyabubare','bwekingo'],
            'Isingiro': ['isingiro', 'bushozi','Kabaare','ngarama','rwembogo','kabuyanda'],
            'Kazo': ['kazo', 'magondo', 'rwemikoma', 'kyabahura' 'Kyenshebashebe','ntambazi','kyabahura'],
            'Wakiso': ['wakiso', 'kyaliwajjala', 'nansana', 'entebbe', 'abayita', 'kireka','nakawuka','bweyog','kisaasi','bwaise'],
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
            'Gulu': ['gulu','vangua','agwee','te-dam','obiya','pawato','kaswa'],
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
            'Mukono': ['mukono','kyampi'],
            'Kyenjojo': ['kyenjojo'],
            'Masindi': ['masindi'],
            'Buhweju': ['buhweju','kabegaramire'],
            'Butambala': ['butambala','kalamba'],
            'Rakai': ['rakai'],
            'Mpigi': ['mpigi'],
            'Sembabule': ['sembabule', 'sembambule'],
            'Arua': ['arua','nabikh'],
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
            'Mubende': ['mubende','kyakatebe'],
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
            'Luwero': ['luwero','kasana','kizito','kakooko'],
            'Tororo': ['tororo'],
            'Serere': ['serere'],
            'Bunyangabu': ['bunyangabu'],
            'Pallisa': ['pallisa'],
            'Manafwa': ['manafwa'],
            'Kalungu': ['kalungu'],
            'Kyegegwa': ['kyegegwa'],
            'Kumi': ['kumi'],
            'Kakumiro': ['kakumiro'],
            'Kitgum': ['kitgum','bwonag'],
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
            'Buvuma': ['buvuma']
        
        # Add more districts and their associated keywords as needed
    }
    
    # Create a new column 'district' and initialize with 'Other'
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
    
    
    
    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                       'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                       'kibingo','kabarole'],
            'Eastern': ['jinja','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku'],
            'Central': ['kampala','luwero','kyotera','masaka','kayunga','mityana','sembabule','nakasongola','mukono','bukomansimbi',
                       'rakai','wakiso','mpigi','buikwe','gomba','lwengo','mayuge','butambala','lyantonde','mubende','kalungu',
                        'kiboga','butambala','buvuma'],
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong']
    
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
    return df