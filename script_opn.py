# necessary libraries
import pandas as pd
import numpy as np
import glob
from pathlib import Path


# base path of files location
path = "/home/opm/Documentos-opm/OPN_COLOMBIA/ANALISYS/input"

# List with the name of all excel files
xlsx_files_list = glob.glob( path + "/*.xlsx" )

# identifiers by technology
faults_lte = "Fallas_TX_LTE"
gsm_monitoring = "GSM_NPO_Monitoring_v4"
lte_monitoring = "LTE_FL16A_NPO_Monitoring_V4"
wbts_monitoring = "WBTS_WCDMA17_NPO_MONITORING"
wcdma_monitoring = "WCDMA17_NPO_Monitoring_V4"

#** Review each excel file according to technology **

# initialize counters
faults_lte_count = 0
gsm_monitoring_count = 0
lte_monitoring_count = 0
wbts_monitoring_count = 0
wcdma_monitoring_count = 0

# identifying files by technology
print("******************************************")
print( "Identifying files by technology ..." )
print("******************************************")


# file identification by technology
for xlsx_file in range( len( xlsx_files_list ) ):
    
    # file search
    if faults_lte in xlsx_files_list[ xlsx_file ]:
                
        # read file
        if faults_lte_count < 1:
            
            faults_lte_count += 1
            
            df_faults_lte_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_faults_lte_1 = df_faults_lte_1.drop( labels=0, axis=0 )
            # validation print
            print( f'Shape LTE FAULTS: {df_faults_lte_1.shape}, file: {faults_lte_count}' )
            
        else:
            df_faults_lte_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            faults_lte_count += 1
            
            df_faults_lte_2 = df_faults_lte_2.drop( labels=0, axis=0 )
            
            df_faults_lte_total = pd.concat( [ df_faults_lte_1, df_faults_lte_2 ],
                                            ignore_index=True )
            
            df_faults_lte_1 = df_faults_lte_total.copy()
            # validation print    
            print( f'Shape LTE FAULTS: {df_faults_lte_total.shape}, file: {faults_lte_count}' )
            
        
        
    ## search GSM monitoring***
    elif gsm_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if gsm_monitoring_count < 1:
            
            gsm_monitoring_count += 1
            
            df_gsm_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_gsm_1 = df_gsm_1.drop( labels=0, axis=0 )
            # validation print
            print( f'Shape GSM: {df_gsm_1.shape}, file: {gsm_monitoring_count}' )
            
            
        else:
            df_gsm_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_gsm_2 = df_gsm_2.drop( labels=0, axis=0 )
            
            df_gsm_total = pd.concat( [ df_gsm_1, df_gsm_2 ], ignore_index=True )
            
            df_gsm_1 = df_gsm_total.copy()
            # validation print    
            print( f'Shape GSM: {df_gsm_total.shape}, file: {gsm_monitoring_count}' )
            
                
            
    ## search LTE monitoring 
    elif lte_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if lte_monitoring_count < 1:
            
            lte_monitoring_count += 1
            
            df_lte_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_lte_1 = df_lte_1.drop( labels=0, axis=0 )
            # validation print
            print( f'Shape LTE: {df_lte_1.shape}, file: {lte_monitoring_count}' )
            
            
        else:
            df_lte_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            lte_monitoring_count += 1
            
            df_lte_2 = df_lte_2.drop( labels=0, axis=0 )
            
            df_lte_total = pd.concat( [ df_lte_1, df_lte_2 ], ignore_index=True )
            
            df_lte_1 = df_lte_total.copy()
            # validation print    
            print( f'Shape LTE: {df_lte_total.shape}, file: {lte_monitoring_count}' )
            
        
                
    ## search WBTS monitoring
    elif wbts_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if wbts_monitoring_count < 1:
            
            wbts_monitoring_count += 1
            
            df_wbts_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_wbts_1 = df_wbts_1.drop( labels=0, axis=0 )
            # validation print
            print( f'Shape WBTS: {df_wbts_1.shape}, file: {wbts_monitoring_count}' )
            
            
        else:
            df_wbts_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            wbts_monitoring_count += 1
            
            df_wbts_2 = df_wbts_2.drop( labels=0, axis=0 )
            
            df_wbts_total = pd.concat( [ df_wbts_1, df_wbts_2 ], ignore_index=True )
            
            df_wbts_1 = df_wbts_total.copy()
            # validation print    
            print( f'Shape WBTS: {df_wbts_total.shape}, file: {wbts_monitoring_count}' )
            

        
    ## search WCDA monitoring
    elif wcdma_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if wcdma_monitoring_count < 1:
            
            wcdma_monitoring_count += 1
            
            df_wcdma_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_wcdma_1 = df_wcdma_1.drop( labels=0, axis=0 )
            # validation print
            print( f'Shape WCDMA: {df_wcdma_1.shape}, file: {wcdma_monitoring_count}' )
            
            
        else:
            df_wcdma_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            wcdma_monitoring_count += 1
            
            df_wcdma_2 = df_wcdma_2.drop( labels=0, axis=0 )
            
            df_wcdma_total = pd.concat( [ df_wcdma_1, df_wcdma_2 ], ignore_index=True )
            
            df_wcdma_1 = df_wcdma_total.copy()
            # validation print    
            print( f'Shape WCDMA: {df_wcdma_total.shape}, file: {wcdma_monitoring_count}' )


    
    ## No valid files
    else:
        #print( "No valid files" )
        pass

#***************************************************
# check the attributes for early warning reporting
#**************************************************

# check the attributes for early warning reporting 4G
print("******************************************")
print( "check the attributes for early warning reporting 4G (FAULTS LTE)..." )
print("******************************************")

# attributes available in lte faults
attribte_list_faults_lte = df_faults_lte_total.columns.to_list()

# existence of the "LNBTS type" attribute
if "LNBTS type" not in attribte_list_faults_lte:
    
    # determine total rows
    rows_faults_lte = df_faults_lte_total.shape
    
    # list with total NAN values
    lnbts_type_faults_lte = [ np.NaN for value in range( rows_faults_lte[0] ) ]
    
    # insert in the df the number of empty values
    df_faults_lte_total.insert(
                                loc = 2, 
                                column = "LNBTS type", 
                                value = lnbts_type_faults_lte
                               )

# if the file exists, no action is taken
else:
    pass

# Change of name of the attributes according to the template
df_faults_lte_total = df_faults_lte_total.rename( columns = 
                                                    { 
                                                    "avgRTT_15Min" : "avgRTT_15Min (M51132C0)", 
                                                    "maxRTT_15Min" : "maxRTT_15Min (M51132C1)"
                                                    }
                                                )

print( "***************************************************" )
print( "4G parameter correspondence (FAULTS LTE): ok!!! " )
print("****************************************************")
print('\n')

# **fix attribute names read in lte**
print("*****************************************************************")
print( "check the attributes for early warning reporting 4G (LTE)..." )
print("*****************************************************************")

# control flag for tests in this notebook
rename_count_lte = 0

# attributes available in lte
attribte_list_lte = df_lte_total.columns.to_list()

# existence of the "LNBTS type" attribute
if "LNBTS type" not in attribte_list_lte:
    
    # determine total rows
    rows_lte = df_lte_total.shape
    
    # list with total NAN values
    lnbts_type_lte = [ np.NaN for value in range( rows_lte[0] ) ]
    
    # insert in the df the number of empty values
    df_lte_total.insert(
                                loc = 2, 
                                column = "LNBTS type", 
                                value = lnbts_type_lte
                               )
# if the file exists, no action is taken
else:
    pass

# Change of name of the attributes according to the template

if rename_count_lte < 1:
    
    rename_count_lte += 1
    
    df_lte_total = df_lte_total.rename( columns = { 
                                                "AVG_RTWP_RX_ANT_1 (M8005C306)" : "AVG_RTWP_RX_ANT_1", 
                                                "AVG_RTWP_RX_ANT_2 (M8005C307)" : "AVG_RTWP_RX_ANT_2", 
                                                "AVG_RTWP_RX_ANT_3 (M8005C308)" : "AVG_RTWP_RX_ANT_3", 
                                                "AVG_RTWP_RX_ANT_4 (M8005C309)" : "AVG_RTWP_RX_ANT_4"
                                                }
                                    )
else:
    pass

# the list of column names is updated
attribte_list_lte = df_lte_total.columns.to_list()


# Check the existence of the attributes, if they do not exist they are added
if 'AVG_RTWP_RX_ANT_1 (M8005C306)' not in attribte_list_lte:
    
   df_lte_total[ 'AVG_RTWP_RX_ANT_1 (M8005C306)' ] = df_lte_total[ 'AVG_RTWP_RX_ANT_1' ] / 10

else:
    pass

if 'AVG_RTWP_RX_ANT_2 (M8005C307)' not in attribte_list_lte:
    
    df_lte_total[ 'AVG_RTWP_RX_ANT_2 (M8005C307)' ] = df_lte_total[ 'AVG_RTWP_RX_ANT_2' ] / 10
    
else:
    pass


if 'AVG_RTWP_RX_ANT_3 (M8005C308)' not in attribte_list_lte:
    
    df_lte_total[ 'AVG_RTWP_RX_ANT_3 (M8005C308)' ] = df_lte_total[ 'AVG_RTWP_RX_ANT_3' ] / 10
    
else:
    pass

if 'AVG_RTWP_RX_ANT_4 (M8005C309)' not in attribte_list_lte:
    
    df_lte_total[ 'AVG_RTWP_RX_ANT_4 (M8005C309)' ] = df_lte_total[ 'AVG_RTWP_RX_ANT_4' ] / 10
    
else:
    pass


if 'Sector' not in attribte_list_lte:
    # "Sector": Last two characters of the 'LNCEL name' attribute
    df_lte_total[ 'Sector' ] = df_lte_total[ 'LNCEL name' ].apply( lambda x: x[ -2: ] )
else:
    pass

# the list of column names is updated
attribte_list_lte = df_lte_total.columns.to_list()

print( "*******************************" )
print( "4G parameter correspondence (LTE): ok!!! " )
print("******************************************")
print('\n')

# **fix attribute names read in WBTS and WCDMA**
print("*****************************************************************")
print( "check the attributes for early warning reporting 3G (WBTS, WCDMA)..." )
print("*****************************************************************")

print( "***************************************************" )
print( "3G parameter correspondence (WBTS, WCDMA): ok!!! " )
print("****************************************************")
print('\n')

print("*****************************************************************")
print( "check the attributes for early warning reporting 2G (GSM)..." )
print("*****************************************************************")

# attributes available in gsm
attribte_list_gsm = df_gsm_total.columns.to_list()

# verify existence of the attribute "Zlinea"
if "Zlinea" not in attribte_list_gsm:
    
    # determine total rows
    rows_gsm = df_gsm_total.shape
    
    # list with total NAN values
    zlinea_gsm = [ np.NaN for value in range( rows_gsm[0] ) ]
    
    # insert in the df the number of empty values
    df_gsm_total[ "Zlinea" ] = zlinea_gsm
    
# if the file exists, no action is taken
else:
    pass

print( "***************************************************" )
print( "2G parameter correspondence (GSM): ok!!! " )
print("****************************************************")
print('\n')

#************************************************
# normalize the name of the sites per file
#************************************************
def norm_name(site:str) -> str:
    """normaliza los nombres de los sitios, 
    colocando los nombres en minúscula y sustituyendo los caracteres
    '.', ':', ' ' y '-' por '_'

    Args:
        site (str): nombre del sitio original

    Returns:
        site (str): nombre del sitio normalizado    
    """
    
    site = site.lower()
    signs = [' ', '.', ':', '-']
    for c in range( len( site ) ):
        if site[c] in signs:
            site = site.replace(site[c] , '_')
        
    return site

# Normalization of site names
print("\n")
print("******************************************")
print( "Normalization of site names..." )
print("******************************************")

# Attributes to filter by technology
faults_lte_filter = 'LNBTS name'
gsm_filter = 'BCF name'
lte_filter = 'LNBTS name'
wbts_filter = 'WBTS name'
wcdma_filter = 'WBTS name'

# Normalization of site names 
df_faults_lte_total[ faults_lte_filter ] = df_faults_lte_total[
    faults_lte_filter ].apply( norm_name );

df_gsm_total[ gsm_filter ] = df_gsm_total[ 
                                            gsm_filter ].apply( norm_name );

df_lte_total[ lte_filter ] = df_lte_total[ 
                                            lte_filter ].apply( norm_name );

df_wbts_total[ wbts_filter ] = df_wbts_total[
    wbts_filter ].apply( norm_name );

df_wcdma_total[ wcdma_filter ] = df_wcdma_total[
    wcdma_filter ].apply( norm_name );

print( "Normalization of site names OK!" )

#************************************************
# Remove duplicate values

print("\n")
print("******************************************")
print( "Removing duplicate values..." )
print("******************************************")

# Attributes to remove duplicate values
faults_lte_duplicate = [ 'Period start time', 'LNBTS name', 'ATT_INTER_ENB_HO (M8014C6)' ]
gsm_monitoring_duplicate = [ 'Period start time', 'BSC name', 'BTS name' ]
lte_monitoring_duplicate = [ 'Period start time', 'LNCEL name' ]
wbts_monitoring_duplicate = [ 'Period start time', 'WBTS name', 'WBTS ID' ]
wcdma_monitoring_duplicate = [ 'Period start time', 'WCEL name', 'WCEL ID' ]

# Removing duplicate values LTE FAULT
print( f'Shape before remove duplicates in LTE FAULT: {df_faults_lte_total.shape}' )

# Removing duplicate values LTE FAULT
df_faults_lte_unique = df_faults_lte_total.drop_duplicates( 
                                                             subset=faults_lte_duplicate,
                                                             ignore_index=True 
                                                             )

print( f'Shape after remove duplicates LTE FAULT: {df_faults_lte_unique.shape}' )

# remove duplicates in GSM total
print( f'Shape before remove duplicates GSM: {df_gsm_total.shape}' )
df_gsm_unique = df_gsm_total.drop_duplicates( 
                                            subset=gsm_monitoring_duplicate,
                                            ignore_index=True 
                                            )

print( f'Shape after remove duplicates GSM: {df_gsm_unique.shape}' )

# Remove Duplicates in Full LTE
print( f'Shape before remove duplicates LTE: {df_lte_total.shape}' )
df_lte_unique = df_lte_total.drop_duplicates( 
                                            subset=lte_monitoring_duplicate,
                                            ignore_index=True 
                                            )

print( f'Shape after remove duplicates LTE: {df_lte_unique.shape}' )

# Eliminar duplicados en WBTS total [pendind]
print( f'Shape before remove duplicates WBTS: {df_wbts_total.shape}' )
df_wbts_unique = df_wbts_total.drop_duplicates( 
                                               subset=wbts_monitoring_duplicate,
                                               ignore_index=True 
                                            )

print( f'Shape after remove duplicates WBTS: {df_wbts_unique.shape}' )

# Remove Duplicates in WCDMA Total
print( f'Shape before remove duplicates WCDMA: {df_wcdma_total.shape}' )
df_wcdma_unique = df_wcdma_total.drop_duplicates( 
                                                subset=wcdma_monitoring_duplicate,
                                                ignore_index=True 
                                                )

print( f'Shape after remove duplicates WCDMA: {df_wcdma_unique.shape}' )



# ***** Save the files in specifics templates by technology************
print("\n")
print("******************************************")
print( "Saving files by technology..." )
print("******************************************")

# algorithm
# 1. define path by technology
# 2. tune the with statement by technology

print("******************************************")
print( "Saving data LTE FAULTS 4G..." )
print("******************************************")


# saving 4G files
path_4g_lte_faults = 'output/Alertas Tempranas_4G.xlsx'

with pd.ExcelWriter( path_4g_lte_faults,
                    mode='a', 
                    engine='openpyxl', 
                    if_sheet_exists='overlay' ) as writer:
    
    # vacía el df específico en una hoja existente
    df_faults_lte_unique.to_excel( writer, 
                  sheet_name='Data2', 
                  startrow=1, 
                  index= False,
                  header=None
                  )

print("******************************************")
print( "Saving data LTE FAULTS 4G ok!!!" )
print("******************************************")






# *************************************
# Filtrado de los archivos por sitios únicos
# Diccionario por clave: nombre del df y por valor el df
# correspondiente

# print("\n")
# print("******************************************")
# print( "Filter by site..." )
# print("******************************************")

# # Unique sites per attribute per file
# fault_lte_sites = list(df_faults_lte_unique[faults_lte_filter].unique())
# gsm_sites = list( df_gsm_unique[gsm_filter].unique() )
# lte_sites = list( df_lte_unique[lte_filter].unique() )
# wbts_sites = list( df_wbts_unique[wbts_filter].unique() )
# wcdma_sites = list( df_wcdma_unique[wcdma_filter].unique() )

# # LTE FAULTS Dictionary 
# print("LTE FAULTS filter :")
# dic_lte_faults = {}
# for item in fault_lte_sites:
#     dic_lte_faults[item] = df_faults_lte_unique[ 
#                       df_faults_lte_unique[ faults_lte_filter ] ==  item 
#                                   ]
#     print( f'{item}: {dic_lte_faults[item].shape}' )

# # GSM Dictionary 
# print("GSM filter:")
# dic_gsm = {}
# for item in gsm_sites:
#     dic_gsm[item] = df_gsm_unique[ 
#                       df_gsm_unique[ gsm_filter ] ==  item 
#                                 ]
#     print( f'{item}: {dic_gsm[item].shape}' )
    
# # LTE Dictionary 
# print("LTE filter:")
# dic_lte = {}
# for item in lte_sites:
#     dic_lte[item] = df_lte_unique[ 
#                       df_lte_unique[ lte_filter ] ==  item 
#                                 ]
#     print( f'{item}: {dic_lte[item].shape}' )
    
# # WBTS Dictionary 
# print("WBTS filter:")
# dic_wbts = {}
# for item in wbts_sites:
#     dic_wbts[item] = df_wbts_unique[ 
#                       df_wbts_unique[ wbts_filter ] ==  item 
#                                 ]
#     print( f'{item}: {dic_wbts[item].shape}' )
    
# # WCDMA Dictionary
# print("WCDMA filter:")
# dic_wcdma = {}
# for item in wcdma_sites:
#     dic_wcdma[item] = df_wcdma_unique[ 
#                       df_wcdma_unique[ wcdma_filter ] ==  item 
#                                 ]
#     print( f'{item}: {dic_wcdma[item].shape}' )
    
# # Exporting files filtered by site
# print("\n")
# print("******************************************")
# print( "Exporting files filtered by site..." )
# print("******************************************")

# output_folder = 'output'

# # Exporting LTE FAULTS files
# print("Exporting LTE FAULTS files ... ")
# for key, value in dic_lte_faults.items():
#     file_path = Path( f'{output_folder}/{key}_fallas_lte_Alertas Tempranas_4G.csv' )
#     file_path.parent.mkdir( parents=True, exist_ok=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)
    
# print("Exporting LTE FAULTS files OK!")

# # Exporting GSM files
# print("Exporting GSM files ... ")
# for key, value in dic_gsm.items():
#     file_path = Path( f'{output_folder}/{key}_Alertas Tempranas_2G.csv' )
#     file_path.parent.mkdir( parents=True, exist_ok=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)

# print("Exporting GSM files OK!")

# # Exporting LTE files
# print("Exporting LTE files... ")
# for key, value in dic_lte.items():
#     file_path = Path( f'{output_folder}/{key}_lte_Alertas Tempranas_4G.csv' )
#     file_path.parent.mkdir( parents=True, exist_ok=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)
    
# print("Exporting LTE files OK")

# # Exporting WBTS files
# print("Exporting WBTS files... ")
# for key, value in dic_wbts.items():
#     file_path = Path( f'{output_folder}/{key}_wbts_Alertas Tempranas_3G.csv' )
#     file_path.parent.mkdir( parents=True, exist_ok=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)

# print("Exporting WBTS files OK!")

# # Exporting WCDMA files
# print("Exporting WCDMA files... ")
# for key, value in dic_wcdma.items():
#     file_path = Path( f'{output_folder}/{key}_wcdma_Alertas Tempranas_3G.csv' )
#     file_path.parent.mkdir( parents=True, exist_ok=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)
    
# print("Exporting WCDMA files OK!")