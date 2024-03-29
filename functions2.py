# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:12:32 2024

@author: NobertTurihohabwe
"""
import streamlit as st
import pandas as pd
import numpy as np



def Kyaps(df):
    dfKYAPS=df
    try:
        deleted_columns=['id','NIN','Phone_number','name_of_borrower','email_of_borrower','highest_education_level','Date_of_birth','employment_status','created','Loan_term_value']
        dfKYAPS=dfKYAPS.drop(columns=deleted_columns)
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS['sector'] = dfKYAPS['Line_of_business'] +' '+ dfKYAPS['Loan_purpose']
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS = dfKYAPS.drop(columns=['Line_of_business','Loan_purpose'])
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS['Date_of_loan_issue'] = pd.to_datetime(dfKYAPS['Date_of_loan_issue'], format='mixed', errors='coerce')
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS['Date_of_repayments_commencement'] = pd.to_datetime(dfKYAPS['Date_of_repayments_commencement'],format='mixed', errors='coerce')
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS['Interest_rate'] = dfKYAPS['Interest_rate'].replace(22,0.22)
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS["Person_with_disabilities"] = dfKYAPS["Person_with_disabilities"].replace(0,"No")
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS["Loan_type"] = dfKYAPS["Loan_type"].str.replace(" Client",'')
    except Exception as e: 
        st.write(e)
    try:
        dfKYAPS["Age_Group"] = np.where(dfKYAPS["Age"] > 35, "Non Youth", "Youth")
    except Exception as e: 
        st.write(e)
    
    
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                  'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing','propriet'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize','agri',
                        'sugar cane production','diary production','fattening'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos','baby'],
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
    dfKYAPS['Sector'] = 'not_defined'

    try:
        # Iterate over each row in the DataFrame
        for index, row in dfKYAPS.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        dfKYAPS.at[index, 'Sector'] = sector
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e: 
        st.write(e)
    
    
    # Define your Districts and corresponding keywords
    district_keywords = {
            'Mbarara': ['mbarara', 'kinoni t/c', 'kitunguru', 'ruhunga','rubaya', 'bwizibwera', 'kakoba', 'rwebishekye', 
                        'rwanyamahembe', 'kakoba', 'rwentondo', 'rubingo','rukiro', 'kashari', 'rwentojo', 'nyarubungo','bukiro',
                        'katyazo', 'rutooma', 'ngango','kagongi', 'nkaaka', 'rugarama','katete','nyamitanga', 'mwizi','rwampara',
                        'omukagyera,','mirongo','Kashare', 'omukagyera','kamushoko', 'bubaare','kyantamba', 'rwanyampazi','kamukuzi',
                       'kashaka','kobwoba','igorora t/c','ntuura','kashenyi','nyabisirira','rubindi','byanamira','nchune','kariro',
                        'rwebikoona','mitoozo','bunenero','nyantungu'],
            'Kampala': ['kampala', 'ben kiwanuka', 'nateete', 'katwe','city centre','kawempe','kabalagala','nakulabye','nakawa',
                        'entebbe road','kalerwe','bulenga','kansanga','wandegeya', 'ntinda', 'acacia', 'bukoto', 'najjanankumbi','makindye','najja','kitintale','kibuli','kasubi'],
            'Kiruhura': ['kiruhura', 'kasaana', 'kinoni', 'rushere', 'kyabagyenyi','shwerenkye','kayonza', 'kikatsi',
                         'kihwa','kiguma','burunga','rwanyangwe','nyakashashara','ekikoni'],
            'Ibanda': ['ibanda', 'katongore','bihanga', 'rwetweka','mushunga','ishongororo', 'kikyenkye','nyakigando','nyarukiika',
                       'kagongo','bwengure','kabaare'],
            'Bushenyi': ['ishaka', 'bushen', 'kijumo','kabare','kakanju', 'nyamirembe','nkanga','nyabubare','bwekingo'],
            'Isingiro': ['isingiro', 'bushozi','Kabaare','ngarama','rwembogo','kabuyanda'],
            'Kazo': ['kazo', 'magondo', 'rwemikoma', 'kyabahura' 'Kyenshebashebe','ntambazi','kyabahura'],
            'Wakiso': ['wakiso', 'kyaliwajjala', 'nansana', 'entebbe', 'abayita', 'kireka', 'matuga','kyengera','kasangati','bweyogerere'],
            'Kibingo': ['buringo', 'masheruka','bwayegamba'],
            'Sheema': ['sheema','kabwohe', 'rwanama','mashojwa'],
            'Ntungamo': ['ntungamo','ntugam','kyaruhanga','rubaare','katomi'],
            'Rukiga': ['rukiga', 'nyakambu','rwenyangye','kamwezi'],
            'Kamwenge': ['kamwenge', 'kyabandara','bwizi t c','kamwen'],
            'Masaka': ['masaka','nyendo'],
            'Rukungiri': ['rukungiri','kihihi'],
            'Iganga': ['iganga'],
            'Amuria':['amuria'],
            'Buikwe': ['buikwe','lugazi'],
            'Bugiri': ['bugiri'],
            'Soroti': ['soroti'],
            'Kagadi':['kagadi'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Gulu': ['gulu'],
            'Kayunga': ['kayunga'],
            'Mbale': ['mbale','magale','nakaloke'],
            'Pader': ['pader'],
            'Kamuli': ['kamuli','namwendwa'],
            'Namayingo': ['namayingo'],
            'Koboko': ['koboko'],
            'Mityana': ['mityana'],
            'Hoima': ['hoima'],
            'Nakasongola': ['nakasongola'],
            'Kasese': ['kasese', 'bwera'],
            'Lira': ['lira','Namutumba'],
            'Mukono': ['mukono','seeta','kalagi'],
            'Kyenjojo': ['kyenjojo'],
            'Masindi': ['masindi'],
            'Buhweju': ['buhweju','kabegaramire'],
            'Butambala': ['butambala','kalamba'],
            'Rakai': ['rakai'],
            'Mpigi': ['mpigi','buwama'],
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
            'Mubende': ['mubende','kasambya'],
            'Kitagwenda': ['kitagwenda'],
            'Lwengo': ['lwengo','mbirizi'],
            'Mayuge': ['mayuge','musita'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Kole': ['kole'],
            'Fort Portal':['fort port','rwimi'],
            'Bulambuli': ['bulambuli'],
            'Luwero': ['luwero','wobulenzi'],
            'Tororo': ['tororo'],
            'Serere': ['serere'],
            'Bunyangabu': ['bunyangabu'],
            'Pallisa': ['pallisa'],
            'Manafwa': ['manafwa'],
            'Kalungu': ['kalungu','lukaya'],
            'Kyegegwa': ['kyegegwa'],
            'Kumi': ['kumi'],
            'Kakumiro': ['kakumiro','igayaza'],
            'Kitgum': ['kitgum'],
            'Kanungu': ['kanung'],
            'Kiboga': ['kiboga'],
            'Kapchorwa': ['kapchorwa'],
            'Kween':['kween'],
            'Kaliro': ['kaliro'],
            'Dokolo': ['dokolo'],
            'Apac': ['apac'],
            'Kabalore': ['nyamirima'],
            'Zombo': ['zombo', 'paidha'],
            'Nebbi': ['nebbi'],
            'Alebtong':['alebtong'],
            'Kibuku':['kibuku'],
            'Kyotera': ['kyotera','buwenge'],
            'Jinja': ['jinja'],
            'Kabarole': ['kabarole'],
            'Namutumba': ['namutumba'],
            'Luuka':['luuka'],
            'Kisoro':['kisoro','muhanga'],
            'Buvuma': ['buvuma']
        
        # Add more districts and their associated keywords as needed
    }
    
    # Create a new column 'district' and initialize with 'Other'
    dfKYAPS['District'] = 'Other'

    try:
    # Iterate over each row in the DataFrame
        for index, row in dfKYAPS.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        dfKYAPS.at[index, 'District'] = district
                        break  # Exit the loop once a sector is identified for the current row
    
    except Exception as e: 
        st.write(e)

    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','kisoro','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                       'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                       'kibingo','kabarole'],
            'Eastern': ['jinja','kween','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku','luuka'],
            'Central': ['kampala','luwero','kyotera','masaka','kayunga','mityana','sembabule','nakasongola','mukono','bukomansimbi',
                       'rakai','wakiso','mpigi','buikwe','gomba','lwengo','mayuge','butambala','lyantonde','mubende','kalungu',
                        'kiboga','butambala','buvuma'],
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong',
                         'amuria','namutumba']
    
        # Add more regions and their associated keywords as needed
    }
    
    # Create a new column 'region' and initialize with 'Other'
    dfKYAPS['Region'] = 'Other'

    try:
        # Iterate over each row in the DataFrame
        for index, row in dfKYAPS.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        dfKYAPS.at[index, 'Region'] = region
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e: 
        st.write(e)

    df=dfKYAPS
    return df



def ASA(df):
    dfASA=df
    try:
        deleted_columns=['id','NIN','Phone_number','name_of_borrower','email_of_borrower','highest_education_level','employment_status','created','Age','Loan_term_value']
        dfASA=dfASA.drop(columns=deleted_columns)
    except Exception as e:
        st.write(e)
    try:
        dfASA['sector'] = dfASA['Line_of_business'] +' '+ dfASA['Loan_purpose']
        dfASA = dfASA.drop(columns=['Line_of_business','Loan_purpose'])
    except Exception as e:
        st.write(e)
    try:
        dfASA['Date_of_birth'] = pd.to_datetime(dfASA['Date_of_birth'], format='mixed', errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        dfASA['Date_of_loan_issue'] = pd.to_datetime(dfASA['Date_of_loan_issue'], format='mixed', errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        dfASA['Age'] = dfASA['Date_of_loan_issue'].dt.year - dfASA['Date_of_birth'].dt.year
    except Exception as e:
        st.write(e)
    try:
        dfASA = dfASA.drop(columns=['Date_of_birth'])
    except Exception as e:
        st.write(e)
    try:
        dfASA['Date_of_repayments_commencement'] = pd.to_datetime(dfASA['Date_of_repayments_commencement'],format='mixed', errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        dfASA['Interest_rate'] = dfASA['Interest_rate'].replace(0.09,0.27)
    except Exception as e:
        st.write(e)
    try:
        dfASA['Length_of_time_running']=dfASA['Length_of_time_running'].str.lower()
    except Exception as e:
        st.write(e)
    try:
        dfASA['Length_of_time_running'] = dfASA['Length_of_time_running'].str.replace("16weeks", "")
        dfASA['Length_of_time_running'] = dfASA['Length_of_time_running'].str.replace("year", "")
        dfASA['Length_of_time_running'] = dfASA['Length_of_time_running'].str.replace("yr", "")
        dfASA['Length_of_time_running'] = dfASA['Length_of_time_running'].str.replace("s", "")
        dfASA['Length_of_time_running'] = dfASA['Length_of_time_running'].str.replace("&half", "")
        dfASA['Length_of_time_running'] = dfASA['Length_of_time_running'].str.replace("half", "")
    except Exception as e:
        st.write(e)
    try:
        dfASA['Length_of_time_running'] = pd.to_numeric(dfASA['Length_of_time_running'], errors='coerce')
    except Exception as e:
        st.write(e)
    try:
        dfASA["Previously_unemployed"] = (dfASA["Previously_unemployed"].str.lower()).str.replace("no","")
    except Exception as e:
        st.write(e)
    try:
        dfASA["Person_with_disabilities"] = dfASA["Person_with_disabilities"].str.capitalize()
    except Exception as e:
        st.write(e)
    try:
        dfASA["Age_Group"] = np.where(dfASA["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)
    
    
    
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                  'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize','agri',
                        'sugar cane production','diary production','fattening'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos','baby'],
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
    dfASA['Sector'] = 'not_defined'
    
    try:
    # Iterate over each row in the DataFrame
        for index, row in dfASA.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        dfASA.at[index, 'Sector'] = sector
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)
    
    
    # Define your Districts and corresponding keywords
    district_keywords = {
            'Mbarara': ['mbarara', 'kinoni t/c', 'kitunguru', 'ruhunga','rubaya', 'bwizibwera', 'kakoba', 'rwebishekye', 
                        'rwanyamahembe', 'kakoba', 'rwentondo', 'rubingo','rukiro', 'kashari', 'rwentojo', 'nyarubungo','bukiro',
                        'katyazo', 'rutooma', 'ngango','kagongi', 'nkaaka', 'rugarama','katete','nyamitanga', 'mwizi','rwampara',
                        'omukagyera,','mirongo','Kashare', 'omukagyera','kamushoko', 'bubaare','kyantamba', 'rwanyampazi','kamukuzi',
                       'kashaka','kobwoba','igorora t/c','ntuura','kashenyi','nyabisirira','rubindi','byanamira','nchune','kariro',
                        'rwebikoona','mitoozo','bunenero','nyantungu'],
            'Kampala': ['kampala', 'ben kiwanuka', 'nateete', 'katwe','city centre','kawempe','kabalagala','nakulabye','nakawa',
                        'entebbe road','kalerwe','bulenga','kansanga','wandegeya', 'ntinda', 'acacia', 'bukoto', 'najjanankumbi','makindye','najja','kitintale','kibuli','kasubi'],
            'Kiruhura': ['kiruhura', 'kasaana', 'kinoni', 'rushere', 'kyabagyenyi','shwerenkye','kayonza', 'kikatsi',
                         'kihwa','kiguma','burunga','rwanyangwe','nyakashashara','ekikoni'],
            'Ibanda': ['ibanda', 'katongore','bihanga', 'rwetweka','mushunga','ishongororo', 'kikyenkye','nyakigando','nyarukiika',
                       'kagongo','bwengure','kabaare'],
            'Bushenyi': ['ishaka', 'bushenyi', 'kijumo','kabare','kakanju', 'nyamirembe','nkanga','nyabubare','bwekingo'],
            'Isingiro': ['isingiro', 'bushozi','Kabaare','ngarama','rwembogo','kabuyanda','bushen'],
            'Kazo': ['kazo', 'magondo', 'rwemikoma', 'kyabahura' 'Kyenshebashebe','ntambazi','kyabahura'],
            'Wakiso': ['wakiso', 'kyaliwajjala', 'nansana', 'entebbe', 'abayita', 'kireka', 'matuga','kyengera','kasangati','bweyogerere'],
            'Kibingo': ['buringo', 'masheruka','bwayegamba'],
            'Sheema': ['sheema','kabwohe', 'rwanama','mashojwa'],
            'Ntungamo': ['ntungamo','ntugam','kyaruhanga','rubaare','katomi'],
            'Rukiga': ['rukiga', 'nyakambu','rwenyangye','kamwezi'],
            'Kamwenge': ['kamwenge', 'kyabandara','bwizi t c','kamwen'],
            'Masaka': ['masaka','nyendo'],
            'Rukungiri': ['rukungiri','kihihi'],
            'Iganga': ['iganga'],
            'Amuria':['amuria'],
            'Buikwe': ['buikwe','lugazi'],
            'Bugiri': ['bugiri'],
            'Soroti': ['soroti'],
            'Kagadi':['kagadi'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Gulu': ['gulu'],
            'Kayunga': ['kayunga'],
            'Mbale': ['mbale','magale','nakaloke'],
            'Pader': ['pader'],
            'Kamuli': ['kamuli','namwendwa'],
            'Namayingo': ['namayingo'],
            'Koboko': ['koboko'],
            'Mityana': ['mityana'],
            'Hoima': ['hoima'],
            'Nakasongola': ['nakasongola'],
            'Kasese': ['kasese', 'bwera'],
            'Lira': ['lira','Namutumba'],
            'Mukono': ['mukono','seeta','kalagi'],
            'Kyenjojo': ['kyenjojo'],
            'Masindi': ['masindi'],
            'Buhweju': ['buhweju','kabegaramire'],
            'Butambala': ['butambala','kalamba'],
            'Rakai': ['rakai'],
            'Mpigi': ['mpigi','buwama'],
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
            'Mubende': ['mubende','kasambya'],
            'Kitagwenda': ['kitagwenda'],
            'Lwengo': ['lwengo','mbirizi'],
            'Mayuge': ['mayuge','musita'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Kole': ['kole'],
            'Fort Portal':['fort port','rwimi'],
            'Bulambuli': ['bulambuli'],
            'Luwero': ['luwero','wobulenzi'],
            'Tororo': ['tororo'],
            'Serere': ['serere'],
            'Bunyangabu': ['bunyangabu'],
            'Pallisa': ['pallisa'],
            'Manafwa': ['manafwa'],
            'Kalungu': ['kalungu','lukaya'],
            'Kyegegwa': ['kyegegwa'],
            'Kumi': ['kumi'],
            'Kakumiro': ['kakumiro','igayaza'],
            'Kitgum': ['kitgum'],
            'Kanungu': ['kanung'],
            'Kiboga': ['kiboga'],
            'Kapchorwa': ['kapchorwa'],
            'Kween':['kween'],
            'Kaliro': ['kaliro'],
            'Dokolo': ['dokolo'],
            'Apac': ['apac'],
            'Kabalore': ['nyamirima'],
            'Zombo': ['zombo', 'paidha'],
            'Nebbi': ['nebbi'],
            'Alebtong':['alebtong'],
            'Kibuku':['kibuku'],
            'Kyotera': ['kyotera','buwenge'],
            'Jinja': ['jinja'],
            'Kabarole': ['kabarole'],
            'Namutumba': ['namutumba'],
            'Luuka':['luuka'],
            'Kisoro':['kisoro','muhanga'],
            'Buvuma': ['buvuma']
        
        # Add more districts and their associated keywords as needed
    }
    
    # Create a new column 'district' and initialize with 'Other'
    dfASA['District'] = 'Other'

    try:
        # Iterate over each row in the DataFrame
        for index, row in dfASA.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        dfASA.at[index, 'District'] = district
                        break  # Exit the loop once a sector is identified for the current row
    
    except Exception as e:
        st.write(e)
    
    
    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','kisoro','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                       'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                       'kibingo','kabarole'],
            'Eastern': ['jinja','kween','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku','luuka'],
            'Central': ['kampala','luwero','kyotera','masaka','kayunga','mityana','sembabule','nakasongola','mukono','bukomansimbi',
                       'rakai','wakiso','mpigi','buikwe','gomba','lwengo','mayuge','butambala','lyantonde','mubende','kalungu',
                        'kiboga','butambala','buvuma'],
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong',
                         'amuria','namutumba']
    
        # Add more regions and their associated keywords as needed
    }
    
    # Create a new column 'region' and initialize with 'Other'
    dfASA['Region'] = 'Other'

    try:
    # Iterate over each row in the DataFrame
        for index, row in dfASA.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        dfASA.at[index, 'Region'] = region
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)            
    df = dfASA
    return df





def pride(df):
    dfMonthly=df
    deleted_columns=['id','NIN','Phone_number','name_of_borrower','email_of_borrower','highest_education_level','employment_status','created','Age','Loan_term_value']
    try:
        dfMonthly=dfMonthly.drop(columns=deleted_columns)
    except Exception as e:
        st.write(e)
    try:
        dfMonthly['Loan_ID'] = dfMonthly['Loan_ID'].astype(str)
    except Exception as e:
        st.write(e)
    try:
        dfMonthly['Borrower_ID'] = dfMonthly['Borrower_ID'].astype(str)
    except Exception as e:
        st.write(e)
    try:
        dfMonthly['sector'] = dfMonthly['Line_of_business'] +' '+ dfMonthly['Loan_purpose']
    except Exception as e:
         st.write(e)
    try:    
        dfMonthly = dfMonthly.drop(columns=['Line_of_business','Loan_purpose'])
    except Exception as e:
        st.write(e)
    try:
        dfMonthly['Gender'] = dfMonthly['Gender'].replace('F','Female')
    except Exception as e:
         st.write(e)
    try:
         dfMonthly['Gender'] = dfMonthly['Gender'].replace('M','Male')
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Date_of_birth'] = pd.to_datetime(dfMonthly['Date_of_birth'])
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Date_of_loan_issue'] = pd.to_datetime(dfMonthly['Date_of_loan_issue'])
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Age'] = dfMonthly['Date_of_loan_issue'].dt.year - dfMonthly['Date_of_birth'].dt.year
    except Exception as e:
         st.write(e)
    try:
        dfMonthly = dfMonthly.drop(columns=['Date_of_birth'])
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Date_of_repayments_commencement'] = pd.to_datetime(dfMonthly['Date_of_repayments_commencement'])
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Tenure_of_loan'] = dfMonthly['Tenure_of_loan'] / 4.286
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Tenure_of_loan'] = dfMonthly['Tenure_of_loan'].astype(int)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Interest_rate'] = dfMonthly['Interest_rate'].replace(18,0.31)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Loan_type'] = dfMonthly['Loan_type'].replace('GROUP LOAN','Group')
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Expected_number_of_installments'] = dfMonthly['Expected_number_of_installments'].astype(int)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Expected_monthly_installment'] = dfMonthly['Expected_monthly_installment'].astype(int)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Number_of_employees'] = dfMonthly['Number_of_employees'].str.replace(" employees", "")
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Number_of_employees'] = dfMonthly['Number_of_employees'].str.replace(" employee", "")
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Number_of_employees'] = dfMonthly['Number_of_employees'].str.replace("2-4","3")
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Number_of_employees'] = dfMonthly['Number_of_employees'].str.replace("5-15","10")
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Number_of_employees'] = dfMonthly['Number_of_employees'].str.replace("16-30","23")
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Number_of_employees']=dfMonthly['Number_of_employees'].fillna(0)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Number_of_employees'] = pd.to_numeric(dfMonthly['Number_of_employees'])
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].str.replace(" years", "")
    
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].replace("1 - 3","2")
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].replace("4 - 5","4")
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].replace("6 - 10","8")
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].replace("Less than 1 year","1")
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].replace("More than 10 years","10")
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].replace("More than 10","10")
    except Exception as e:
         st.write(e)
         
    try:
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].replace("4.5","4")
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Length_of_time_running'] = dfMonthly['Length_of_time_running'].astype(int)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Loan_cycle_fund_specific'] = dfMonthly['Loan_cycle_fund_specific'].replace("N",0)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly['Loan_cycle_fund_specific'] = dfMonthly['Loan_cycle_fund_specific'].astype(int)
    except Exception as e:
         st.write(e)
    try:
        dfMonthly["Age_Group"] = np.where(dfMonthly["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
         st.write(e)
    
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
    dfMonthly['Sector'] = 'not_defined'

    try:
    # Iterate over each row in the DataFrame
        for index, row in dfMonthly.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'line_of_business' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        dfMonthly.at[index, 'Sector'] = sector
                        break  # Exit the loop once a sector is identified for the current row
                        
    except Exception as e:
         st.write(e)
    

    # Define your Districts and corresponding keywords
    district_keywords = {
            'Mbarara': ['mbarara', 'kinoni t/c', 'kitunguru', 'ruhunga','rubaya', 'bwizibwera', 'kakoba', 'rwebishekye', 
                        'rwanyamahembe', 'kakoba', 'rwentondo', 'rubingo','rukiro', 'kashari', 'rwentojo', 'nyarubungo','bukiro',
                        'katyazo', 'rutooma', 'ngango','kagongi', 'nkaaka', 'rugarama','katete','nyamitanga', 'mwizi','rwampara',
                        'omukagyera,','mirongo','Kashare', 'omukagyera','kamushoko', 'bubaare','kyantamba', 'rwanyampazi','kamukuzi',
                       'kashaka','kobwoba','igorora t/c','ntuura','kashenyi','nyabisirira','rubindi','byanamira','nchune','kariro',
                        'rwebikoona','mitoozo','bunenero','nyantungu'],
            'Kampala': ['kampala', 'ben kiwanuka', 'nateete', 'katwe','city centre','kawempe','kabalagala','nakulabye','nakawa',
                        'entebbe road','wandegeya', 'ntinda', 'acacia', 'bukoto'],
            'Kiruhura': ['kiruhura', 'kasaana', 'kinoni', 'rushere', 'kyabagyenyi','shwerenkye','kayonza', 'kikatsi',
                         'kihwa','kiguma','burunga','rwanyangwe','nyakashashara','ekikoni'],
            'Ibanda': ['ibanda', 'katongore','bihanga', 'rwetweka','mushunga','ishongororo', 'kikyenkye','nyakigando','nyarukiika',
                       'kagongo','bwengure','kabaare'],
            'Bushenyi': ['ishaka', 'bushenyi', 'kijumo','kabare','kakanju', 'nyamirembe','nkanga','nyabubare','bwekingo'],
            'Isingiro': ['isingiro', 'bushozi','Kabaare','ngarama','rwembogo','kabuyanda'],
            'Kazo': ['kazo', 'magondo', 'rwemikoma', 'kyabahura' 'Kyenshebashebe','ntambazi','kyabahura'],
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
            'Kyegegwa': ['kyegegwa'],
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
            'Buvuma': ['buvuma']
        
        # Add more districts and their associated keywords as needed
    }
    
    # Create a new column 'district' and initialize with 'Other'
    dfMonthly['District'] = 'Other'
    try:
    # Iterate over each row in the DataFrame
        for index, row in dfMonthly.iterrows():
            location = row['Location_of_borrower'].lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        dfMonthly.at[index, 'District'] = district
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
         st.write(e)
    
    
    
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
    dfMonthly['Region'] = 'Other'
    
    # Iterate over each row in the DataFrame

    try:
        for index, row in dfMonthly.iterrows():
            location = row['District'].lower()
            
            # Check for each district's keywords in the 'District' column
            for region, district in region_keywords.items():
                for keyword in district:
                    if keyword in location:
                        dfMonthly.at[index, 'Region'] = region
                        break  # Exit the loop once a sector is identified for the current row
    except Exception as e:
         st.write(e)
         
    df=dfMonthly
    return df





##Premier Credit Data Cleaning Code
def letshego(df):
    deleted_columns=['id','NIN','Phone_number','name_of_borrower','email_of_borrower','highest_education_level',
                     'employment_status','created','Age','Loan_term_value']
    try:
        df=df.drop(columns=deleted_columns)
    except Exception as e:
        st.write(e)
    try:
        df['Loan_ID'] = df['Loan_ID'].astype(str)
    except Exception as e:
        st.write(e)
    try:
        df['Borrower_ID'] = df['Borrower_ID'].astype(str)
    except Exception as e:
        st.write(e)
    try:
        df['sector'] = df['Line_of_business'] +' '+ df['Loan_purpose']
    except Exception as e:
        st.write(e)
    try:
        df= df.drop(columns=['Line_of_business','Loan_purpose'])
    except Exception as e:
        st.write(e)
    try:
        df['Gender'] = df['Gender'].replace('F','Female')
    except Exception as e:
        st.write(e)
    try:
        df['Gender'] = df['Gender'].replace('M','Male')
    except Exception as e:
        st.write(e)
    try:
        df['Date_of_birth'] = pd.to_datetime(df['Date_of_birth'])
    except Exception as e:
        st.write(e)
    try:
        df['Date_of_loan_issue'] = pd.to_datetime(df['Date_of_loan_issue'])
    except Exception as e:
        st.write(e)
    try:
        df['Age'] = df['Date_of_loan_issue'].dt.year - df['Date_of_birth'].dt.year
    except Exception as e:
        st.write(e)
    try:
        df = df.drop(columns=['Date_of_birth'])
    except Exception as e:
        st.write(e)
    try:
        df['Date_of_repayments_commencement'] = pd.to_datetime(df['Date_of_repayments_commencement'])
    except Exception as e:
        st.write(e)
    try:
        df['Interest_rate'] = df['Interest_rate'].replace(30,0.3)
    except Exception as e:
        st.write(e)
    try:
        df['Loan_type'] = df['Loan_type'].replace('New Loan','Individual')
    except Exception as e:
        st.write(e)
    try:
        df['Expected_number_of_installments'] = df['Expected_number_of_installments'].astype(int)
    except Exception as e:
        st.write(e)
    try:
        df['Expected_monthly_installment'] = df['Expected_monthly_installment'].astype(int)
    except Exception as e:
        st.write(e)
    try:
        df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)
    
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
    try:
        df['Sector'] = 'not_defined'
    except Exception as e:
        st.write(e)
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
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku'],
            'Central': ['kampala','luwero','kyotera','masaka','kayunga','mityana','sembabule','nakasongola','mukono','bukomansimbi',
                       'rakai','wakiso','mpigi','buikwe','gomba','lwengo','mayuge','butambala','lyantonde','mubende','kalungu',
                        'kiboga','butambala','buvuma'],
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong']
    
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