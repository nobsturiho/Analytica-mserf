# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:12:32 2024

@author: NobertTurihohabwe
"""
import streamlit as st
import pandas as pd
import numpy as np


##Premier Credit Data Cleaning Code
def Premier(df):
    try:
        dropped_columns = (['id', 'name_of_borrower', 'email_of_borrower', 'highest_education_level', 
                        'employment_status', 'created', 'Loan_term_value', 'NIN', 'Phone_number'])
        df.drop(columns = dropped_columns, inplace = True)
    except Exception as e:
        st.write(e)
    try:    
        df["sector"] = df['Line_of_business'] + ' ' + df['Loan_purpose']
    except Exception as e:
        st.write(e)
    try:    
        df.drop(columns = ['Line_of_business', 'Loan_purpose'], inplace = True)
    except Exception as e:
        st.write(e)
    try:    
        df["Date_of_loan_issue"] = pd.to_datetime(df["Date_of_loan_issue"])
    except Exception as e:
        st.write(e)
    try:    
        df["Date_of_birth"] = pd.to_datetime(df["Date_of_birth"])
    except Exception as e:
        st.write(e)
    try:    
        df["Date_of_repayments_commencement"] = pd.to_datetime(df["Date_of_repayments_commencement"])
    except Exception as e:
        st.write(e)
    try:    
        df["Age"] = ((df["Date_of_loan_issue"] - df["Date_of_birth"]).dt.days // 365).astype(int)
    except Exception as e:
        st.write(e)
    try:    
        df.drop(columns = ['Date_of_birth'], inplace = True)
    except Exception as e:
        st.write(e)
    try:    
        df['Interest_rate'] = df['Interest_rate']/100
    except Exception as e:
        st.write(e)
    try:    
        df['Expected_monthly_installment'] = df['Expected_monthly_installment'].round(0).astype('int64')
    except Exception as e:
        st.write(e)
    try:    
        df['Number_of_employees_with_disabilities'] = df['Number_of_employees_with_disabilities'].round(0).astype('Int64').head()
    except Exception as e:
        st.write(e)
    try:    
        df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)
    
    
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                  'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock','other other'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'buying stock','textiles,apparel and leather clothing','textile',
                                            'event','garage','forward','personal development'],
        'Agriculture': ['agri', 'agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening','irish','legume','tea'],
        'Technology': ['technology', 'software', 'hardware','lighting', 'it solutions', 'internet'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'restaurant', 'baker', 'cook','bar','disco','beverage'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel','tour'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['videography','petrol','saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ['land','rent','construct', 'estate','house renovation','house completion','carpentry', 'house improveme',
                                   'housing deve'],
        'Transport': ['transport', 'boda', 'motorcycle'],
        'Mining': ['mining', 'mineral','quarry'],
        # Add more sectors and their associated keywords as needed
    }
    
    # Create a new column 'sector' and initialize with 'Other'
    try:
        df['Sector'] = 'not_defined'
        
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'sector' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        df.at[index, 'Sector'] = sector
                        break  
    
    # Exit the loop once a sector is identified for the current row
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
                        'entebbe road','mkoa','wandegeya', 'ntinda', 'acacia', 'bukoto','luweero','-0.298696', 'lugala', 'kalisizo', '+0.212189,+32.615876'],
            'Kiruhura': ['kiruhura', 'kasaana', 'kinoni', 'rushere', 'kyabagyenyi','shwerenkye','kayonza', 'kikatsi',
                         'kihwa','kiguma','burunga','rwanyangwe','nyakashashara','ekikoni'],
            'Ibanda': ['ibanda', 'katongore','bihanga', 'rwetweka','mushunga','ishongororo', 'kikyenkye','nyakigando','nyarukiika',
                       'kagongo','bwengure','kabaare'],
            'Bushenyi': ['ishaka', 'bushenyi', 'kijumo','kabare','kakanju', 'nyamirembe','nkanga','nyabubare','bwekingo'],
            'Isingiro': ['isingiro', 'bushozi','Kabaare','ngarama','rwembogo','kabuyanda'],
            'Kazo': ['kazo', 'magondo', 'rwemikoma', 'kyabahura' 'Kyenshebashebe','ntambazi','kyabahura'],
            'Wakiso': ['lweza','lyamutundwe', 'bwebaja','kawanda','wakiso', 'kyaliwajjala', 'nansana', 'entebbe', 'abayita', 'kireka','kyengera','kasangati','matugga','buloba',
                      'gobero','magigye','entebbe', 'gayaza', 'najjera', '0.199356', '0.475201', 'seeta', 'mpala', 'bulenga', '0.169786, 32.53353', 'buddo', 'bombo', 'kiwenda', 'buyala', 'abaita', 'na'],
            'Kibingo': ['buringo', 'masheruka','bwayegamba'],
            'Sheema': ['sheema','kabwohe', 'rwanama','mashojwa'],
            'Ntungamo': ['ntungamo','kyaruhanga','rubaare','katomi'],
            'Rukiga': ['rukiga', 'nyakambu','rwenyangye','kamwezi'],
            'Kamwenge': ['kamwenge', 'kyabandara','bwizi t c'],
            'Masaka': ['masaka', 'sunga'],
            'Rukungiri': ['rukungiri'],
            'Iganga': ['iganga', 'bulubandi'],
            'Buikwe': ['buikwe','lugazi','njeru', 'mbiko'],
            'Bugiri': ['bugiri'],
            'Soroti': ['soroti', 'opiyai'],
            'Kagadi':['kagadi'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Gulu': ['gulu'],
            'Kayunga': ['kayunga', 'ntenjeru'],
            'Mbale': ['mbale', 'budadiri', 'busiu'],
            'Pader': ['pader'],
            'Kamuli': ['kamuli'],
            'Namayingo': ['namayingo'],
            'Koboko': ['koboko'],
            'Mityana': ['mityana', 'busunju', '0.498320'],
            'Hoima': ['hoima','kigorobya'],
            'Nakasongola': ['nakasongola'],
            'Lira': ['lira'],
            'Mukono': ['mukono', 'kigunga', 'goma'],
            'Kyenjojo': ['kyenjojo'],
            'Masindi': ['masindi'],
            'Buhweju': ['buhweju','kabegaramire'],
            'Butambala': ['butambala','kalamba'],
            'Rakai': ['rakai'],
            'Mpigi': ['mpigi', 'bujuuko', 'katende', 'kayabwe'],
            'Sembabule': ['sembabule', 'sembambule'],
            'Arua': ['arua'],
            'Rubanda': ['rubanda'],
            'Gomba': ['gomba'],
            'Bundibugyo': ['bundibugyo'],
            'Kiryandongo': ['kiryandongo', 'bweyale', 'kigumba'],
            'Oyam': ['oyam'],
            'Mitooma': ['mitooma'],
            'Rubirizi': ['rubirizi','kichwamba'],
            'Lyantonde': ['lyantonde'],
            'Bukwo': ['bukwo','bukwa'],
            'Busia': ['busia'],
            'Mubende': ['mubende', 'kyawooga'],
            'Kitagwenda': ['kitagwenda'],
            'Lwengo': ['lwengo'],
            'Mayuge': ['mayuge'],
            'Sironko': ['sironko'],
            'Kibaale': ['kibale', 'kibaale','kiryanjagi'],
            'Bukomansimbi': ['bukomansimbi'],
            'Budaka': ['budaka'],
            'Kole': ['kole'],
            'Fort Portal':['fort portal'],
            'Bulambuli': ['bulambuli'],
            'Luwero': ['luwero', 'kakoge'],
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
            'Kiboga': ['kiboga', 'kikooba'],
            'Kapchorwa': ['kapchorwa'],
            'Kaliro': ['kaliro'],
            'Dokolo': ['dokolo'],
            'Apac': ['apac'],
            'Kabalore': ['nyamirima'],
            'Zombo': ['zombo'],
            'Nebbi': ['nebbi'],
            'Alebtong':['alebtong'],
            'Kibuku':['kibuku'],
            'Kyotera': ['kyotera','buwenge', 'mutukula'],
            'Jinja': ['jinja'],
            'Kabarole': ['kabarole', 'rwimi', 'kyatambara', 'buhesesi', 'kogere'],
            'Buvuma': ['buvuma'],
            'Tororo': ['malaba','tororo'],
            'Kasese': ['kinyabisiki','kasese','bwera'],
            'Agago': ['kalongo', 'agago']
        
        # Add more districts and their associated keywords as needed
    }
    
    try:
        # Create a new column 'district' and initialize with 'Other'
        df['District'] = 'Other'
        
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            location = str(row['Location_of_borrower']).lower()
            
            # Check for each sector's keywords in the 'location' column
            for district, keywords in district_keywords.items():
                for keyword in keywords:
                    if keyword in location:
                        df.at[index, 'District'] = district
                        break  
                        # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e) 
    
    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                       'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                       'kibingo','kabarole', 'kyankwanzi'],
            'Eastern': ['jinja','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku'],
            'Central': ['kampala','luwero','kyotera','masaka','kayunga','mityana','sembabule','nakasongola','mukono','bukomansimbi',
                       'rakai','wakiso','mpigi','buikwe','gomba','lwengo','mayuge','butambala','lyantonde','mubende','kalungu',
                        'kiboga','butambala','buvuma'],
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong', 'agago']
    
        # Add more regions and their associated keywords as needed
    }
    
    try:
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
                        break  
        # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e) 
    return df




##Mushanga Sacco Data Cleaning Code
def Mushanga(df):
    dropped_columns = (['id', 'NIN', 'Phone_number', 'name_of_borrower', 'email_of_borrower', 'highest_education_level', 
                        'employment_status', 'created', 'Loan_term_value'])
    try:
        df.drop(columns = dropped_columns, inplace = True)
    except Exception as e:
        st.write(e)
    try:
        df["sector"] = df['Line_of_business'] + df['Loan_purpose']
        df.drop(columns = ['Line_of_business', 'Loan_purpose'], inplace = True)
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_loan_issue"] = pd.to_datetime(df["Date_of_loan_issue"])
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_birth"] = pd.to_datetime(df["Date_of_birth"])
    except Exception as e:
        st.write(e)
    try:
        df["Date_of_repayments_commencement"] = pd.to_datetime(df["Date_of_repayments_commencement"])
    except Exception as e:
        st.write(e)
    try:
        df["Age"] = ((df["Date_of_loan_issue"] - df["Date_of_birth"]).dt.days // 365).astype(int)
    except Exception as e:
        st.write(e)
    try:
        df.drop(columns = ['Date_of_birth'], inplace = True)
    except Exception as e:
        st.write(e)
    try:
        df["Tenure_of_loan"] = round(df["Tenure_of_loan"] / 30, 0)
    except Exception as e:
        st.write(e)
    try:
        df["Tenure_of_loan"] = df["Tenure_of_loan"].astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df['Interest_rate'] = df['Interest_rate']/100
    except Exception as e:
        st.write(e)
    try:
        temp_data = df['Expected_number_of_installments'].copy()
    except Exception as e:
        st.write(e)
    try:
        df['Expected_number_of_installments'] = df['Expected_monthly_installment']
    except Exception as e:
        st.write(e)
    try:
        df['Expected_monthly_installment'] = temp_data
    except Exception as e:
        st.write(e)
    try:
        df['Expected_monthly_installment'] = df['Expected_monthly_installment'].round(0).astype('int64')
    except Exception as e:
        st.write(e)
    try:
        df['Length_of_time_running'] = pd.to_datetime(df['Length_of_time_running'])
    except Exception as e:
        st.write(e)
    try:
        df['Length_of_time_running'] = ((df['Date_of_loan_issue'] - df['Length_of_time_running']).dt.days // 365).astype(int)
    except Exception as e:
        st.write(e)
    try:
        df['Number_of_employees_with_disabilities'] = df['Number_of_employees_with_disabilities'].round(0).astype('Int64').head()
    except Exception as e:
        st.write(e)
    try:
        df['Person_with_disabilities'] = df['Person_with_disabilities'].str.replace('false', 'No')
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
        'Enterprise/Business Development': ["trade",'merchandise','bisuness','commercial', 'small scale','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop','buying stock','textiles,apparel and leather clothing'],
        'Agriculture': ['agri', 'agricult','crops', 'production  ', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening', 'agribusiness'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'grocery', 'restaurant', 'baker', 'cook'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel', 'bar'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ['plot','rent','construct', 'estate','house renovation','house completion'],
        'Transport': ['transport', 'boda', 'motorcycle'],
        'Mining': ['mining', 'mineral','quarry'],
        # Add more sectors and their associated keywords as needed
    }


    try:
        # Create a new column 'sector' and initialize with 'Other'
        df['Sector'] = 'not_defined'
    
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            line_of_business = row['sector'].lower()
            
            # Check for each sector's keywords in the 'sector' column
            for sector, keywords in sector_keywords.items():
                for keyword in keywords:
                    if keyword in line_of_business:
                        df.at[index, 'Sector'] = sector
                        break  
                #   break  # Exit the outer loop if a sector is identified
    
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
            'Kamwenge': ['kamwenge', 'kyabandara','bwizi t c'],
            'Rukungiri': ['rukungiri'],
            'Kabale': ['kabale', 'nyakashebeya'],
            'Kasese': ['kasese', 'bwera'],
            'Kyenjojo': ['kyenjojo'],
            'Buhweju': ['buhweju','kabegaramire'],
            'Rubanda': ['rubanda'],
            'Bundibugyo': ['bundibugyo'],
            'Mitooma': ['mitooma'],
            'Rubirizi': ['rubirizi','kichwamba'],
            'Lyantonde': ['lyantonde'],
            'Fort Portal':['fort portal'],
            'Kanungu': ['kanungu'],
            'Kiboga': ['kiboga'],
            'Kabarole': ['nyamirima', 'kabarole'],
            'Alebtong':['alebtong'],
            'Kibuku':['kibuku'],
            'Kyankwanzi':['kyankwanzi']
        
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
                        break  
                        # Exit the loop once a sector is identified for the current row
    except Exception as e:
        st.write(e)


    region_keywords = {
            'Western': ['mbarara','fort portal','kagadi','kabale','rukungiri','ibanda','bushenyi','hoima','kyenjojo','kasese',
                        'masindi','sheema','isingiro','buhweju','kibaale','kitagwenda','kamwenge','rubanda','ntungamo','kiruhura',
                    'bundibugyo','kiryandongo','rubirizi','bunyangabu','rukiga','kyegegwa','kanungu','kazo','mitooma','kabalore',
                    'kibingo','kabarole', 'kyankwanzi'],
            'Eastern': ['jinja','iganga','bugiri','soroti','mbale','kamuli','namayingo','sironko','budaka','busia','bukwo',
                        'bulambuli','tororo','serere','pallisa','manafwa','kumi','kapchorwa','kaliro','kibuku'],

        # Add more regions and their associated keywords as needed
    }

    try:
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
                        break  
    except Exception as e:
        st.write(e)                    
    return df
#End of Mushanga code





#Data Cleaning Code for Finca
def Finca(df):
    #combine line of business and loan purpose to create sector
    try:
        df['sector']= df['Line_of_business'] + " "+ df['Loan_purpose']
    except Exception as e:
        st.write(e)
    try:
        df=df.drop(columns=['id','name_of_borrower','email_of_borrower','highest_education_level','employment_status',
        'created','Date_of_birth','Loan_term_value','Line_of_business','Loan_purpose','NIN', 'Phone_number'])
    except Exception as e:
        st.write(e)
    #align date columns
    try:
        if type(df['Date_of_loan_issue'][0]) == np.int64:
            df['Date_of_loan_issue'] = (pd.to_datetime('1900')+pd.to_timedelta((df['Date_of_loan_issue']-2),unit='D'))
        else:
            df['Date_of_loan_issue']=pd.to_datetime(df['Date_of_loan_issue'])
    except Exception as e:
        st.write(e)
    try:
        if type(df['Date_of_repayments_commencement'][0]) == np.int64:
            df['Date_of_repayments_commencement'] = (pd.to_datetime('1900')+pd.to_timedelta((df['Date_of_repayments_commencement']-2),unit='D'))
        else:
            df['Date_of_repayments_commencement']=pd.to_datetime(df['Date_of_repayments_commencement'])
    except Exception as e:
        st.write(e)
    #remove units in tenure of loans
    try:
        df['Tenure_of_loan']= df['Tenure_of_loan'].str.replace(' Month(s)','',regex=False)
    except Exception as e:
        st.write(e)
    try:
        df['Tenure_of_loan'] = df['Tenure_of_loan'].str.replace(' Months','',regex=False)
    except Exception as e:
        st.write(e)
    try:
        df['Tenure_of_loan'] = pd.to_numeric(df['Tenure_of_loan'], errors= 'coerce')
    except Exception as e:
        st.write(e)   
    
    
    
    #remove 'loans' in loan type
    df['Loan_type']= df['Loan_type'].str.replace(' loan','',regex=False)
    
    #change M to male and F to female
    df['Gender']= df['Gender'].str.replace('F','Female',regex=False)
    df['Gender']= df['Gender'].str.replace('M','Male',regex=False)
    try:
    #change interest rate to % without units
        if type(df['Interest_rate'][0]) == str:
            df['Interest_rate']= (df['Interest_rate'].str.replace('%','',regex=False).astype(float))/100
        else:
            df['Interest_rate']=pd.to_numeric(df['Interest_rate'], errors='coerce')/100
    except Exception as e:
        st.write(e)
    #change Expected_number_of_installments, Number_of_employees, Annual_revenue_of_borrower, Length_of_time_running, Person_with_disabilities, Number_of_employees_that_are_refugees, Number_of_female_employees, Previously_unemployed, Number_of_employees_with_disabilities to integers
    try:
        df['Expected_number_of_installments']= df['Expected_number_of_installments'].str.replace(' Month(s)','',regex=False)
    except Exception as e:
        st.write(e)
    try:
        df['Expected_number_of_installments'] = df['Expected_number_of_installments'].str.replace(' Months','',regex=False)
    except Exception as e:
        st.write(e)
    try:
        df['Expected_number_of_installments'] = pd.to_numeric(df['Expected_number_of_installments'], errors='coerce')
    except Exception as e:
        st.write(e)   
        
    try:
        df['Number_of_employees']= df['Number_of_employees'].round(0).astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df['Annual_revenue_of_borrower']= df['Annual_revenue_of_borrower'].astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df['Length_of_time_running']= df['Length_of_time_running'].astype('Int64')
    except Exception as e:
        st.write(e)
    #try:
        #df['Person_with_disabilities']= df['Person_with_disabilities'].astype('str')
    #except Exception as e:
        #st.write(e)
    try:
        df['Number_of_employees_that_are_refugees']= df['Number_of_employees_that_are_refugees'].round(0).astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df['Number_of_female_employees']= df['Number_of_female_employees'].astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df['Previously_unemployed']= df['Previously_unemployed'].astype('Int64')
    except Exception as e:
        st.write(e)
    try:
        df['Number_of_employees_with_disabilities']= df['Number_of_employees_with_disabilities'].astype('Int64')
    except Exception as e:
        st.write(e)
    #change Loan_ID and Borrower_ID to string
    try:
        df['Loan_ID']= df['Loan_ID'].astype('str')
    except Exception as e:
        st.write(e)
    try:
        df['Borrower_ID']= df['Borrower_ID'].astype('str')
    except Exception as e:
        st.write(e)
    try:
    # Create age group column
        df["Age_Group"] = np.where(df["Age"] > 35, "Non Youth", "Youth")
    except Exception as e:
        st.write(e)
    
    
    # Create a dictionary of sectors and their key words
    sector_keywords = {
        'Other': ['other','purchase of assets', 'marketing', 'restructuring of facility','memebership organisations','auto richshaw',
                    'portfolio', 'Portfolio Concentration', 'other activities', 'other services buying stock','other other'],
        'Enterprise/Business Development': ["trade",'merchandise','fertilizer & insecticide','stall','cottage industry',
                                            'trading','retail','boutique','wholesale','hawk','business','working capital', 'sell',
                                            'shop', 'agribusiness','buying stock','textiles,apparel and leather clothing','textile'],
        'Agriculture': ['agricult','crops', 'productionmaize','production rice', 'agro products','animal', 'farm', 'rearing', 
                        'vegetable', 'fish','poultry','coffee','beef','cattle','banana','livestock','agro input','maize',
                        'sugar cane production','diary production','fattening','irish','legume','production'],
        'Technology': ['technology', 'software', 'hardware'],
        'Finance / Financial Services': ['financ', 'banking', 'investment', 'mobile money', 'loan'],
        'Health': ['health', 'medical', 'pharmac', 'diagnos'],
        'Food & Beverage': ['bakery','maize processing','confection', 'fast food', 'restaurant', 'baker', 'cook','bar','disco','beverage'],
        'Manufacturing': ['manufactur','factory'],
        'Education & Skills': ['educat','school','tuition','train'],
        'Refugees & Displaced Populations': ['refugee'],
        'Tourism & Hospitality': ['hotel','tour'],
        'Innovation': ['handicraft', 'furniture','bamboo'],
        'Services': ['airtime','welding','saloon','laundry','mechanic', 'tailor', 'beauty', 'print', 'weaving'],
        'Energy': ["coal", 'oil mill','energy'],
        'Digital Economy': ["fax", 'digital economy'],
        'Construction & Estates': ["rent",'construct', 'estate','house renovation','house completion','carpentry', 'house improveme'],
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
            'Buvuma': ['buvuma'],
            'Notavailable': ['notavailable']
        
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
            'Northern': ['gulu','pader','koboko','lira','arua','oyam','kole','zombo','nebbi','kitgum','dokolo','apac','alebtong'],
            'Other': ['notavailable']
    
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
#End of Finca's Code