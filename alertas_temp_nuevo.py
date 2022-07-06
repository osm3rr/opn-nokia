# necessary libraries
import pandas as pd
import numpy as np
import glob
from pathlib import Path
import shutil
import os
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

# base path of files location

## dev mode ###
# "w" for windows
# "l" for linux
os_dev = "w"

if os_dev == "l":
    
    path = "/home/opm/Documentos-opm/OPN_COLOMBIA/ANALYSIS/"
    # List with the name of all excel files
    xlsx_files_list = glob.glob( path + "input" + "/*.xlsx" )

elif os_dev == 'w':
    
    path = "C:\PythonScripts"
    # List with the name of all excel files
    xlsx_files_list = glob.glob( path + "\input" + "\*.xlsx" )




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
print('\n')
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
print('\n')
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

print('\n')
print( "***************************************************" )
print( "4G parameter correspondence (FAULTS LTE): done!!! " )
print("****************************************************")


# **fix attribute names read in lte**
print('\n')
print("*****************************************************************")
print( "check the attributes for early warning reporting 4G (LTE)..." )
print("*****************************************************************")

# control flag for tests in this notebodone
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

print( "*****************************************" )
print( "4G parameter correspondence (LTE): done!!! " )
print("*******************************************")


# **fix attribute names read in WBTS and WCDMA**
print('\n')
print("*****************************************************************")
print( "check the attributes for early warning reporting 3G (WBTS, WCDMA)..." )
print("*****************************************************************")

print('\n')
print( "***************************************************" )
print( "3G parameter correspondence (WBTS, WCDMA): done!!! " )
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

print('\n')
print( "***************************************************" )
print( "2G parameter correspondence (GSM): done!!! " )
print("****************************************************")

#************************************************
# normalize the name of the sites per file
#************************************************
# def norm_name(site:str) -> str:
#     """normaliza los nombres de los sitios, 
#     colocando los nombres en minúscula y sustituyendo los caracteres
#     '.', ':', ' ' y '-' por '_'

#     Args:
#         site (str): nombre del sitio original

#     Returns:
#         site (str): nombre del sitio normalizado    
#     """
    
#     site = site.lower()
#     signs = [' ', '.', ':', '-']
#     for c in range( len( site ) ):
#         if site[c] in signs:
#             site = site.replace(site[c] , '_')
        
#     return site

# # Normalization of site names
# print("\n")
# print("******************************************")
# print( "Normalization of site names..." )
# print("******************************************")

# Attributes to filter by technology
faults_lte_filter = 'LNBTS name'
gsm_filter = 'BCF name'
lte_filter = 'LNBTS name'
wbts_filter = 'WBTS name'
wcdma_filter = 'WBTS name'

# # Normalization of site names 
# df_faults_lte_total[ faults_lte_filter ] = df_faults_lte_total[
#     faults_lte_filter ].apply( norm_name );

# df_gsm_total[ gsm_filter ] = df_gsm_total[ 
#                                             gsm_filter ].apply( norm_name );

# df_lte_total[ lte_filter ] = df_lte_total[ 
#                                             lte_filter ].apply( norm_name );

# df_wbts_total[ wbts_filter ] = df_wbts_total[
#     wbts_filter ].apply( norm_name );

# df_wcdma_total[ wcdma_filter ] = df_wcdma_total[
#     wcdma_filter ].apply( norm_name );

# print( "Normalization of site names done!" )

#************************************************
# Remove duplicate values
#************************************************
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


# ************************************************
# File filtering by unique sites
# ************************************************

print("\n")
print("******************************************")
print( "Filter by site..." )
print("******************************************")

print("\n")
print("******************************************")
print( "reading the filters file by site..." )
print("******************************************")

# file path for filter by unique sites
if os_dev == "l":
    filter_file = 'input/listado_de_sitios_at.txt'

elif os_dev == "w":
    filter_file = 'input\listado_de_sitios_at.txt'

# reading file
reader = open( filter_file, 'r' )
data = reader.read()

# nota: incorporar la lógica para que detecte el caso en el
# que se coloca una coma al final del último sitio
#sites_to_search = data.replace("\n", '').split(',')
sites_to_search = data.split( "\n" )
reader.close()

#print( 'sitios a buscar:', sites_to_search )

# sites by filter
print("\n")
print("******************************************")
print( "reading the filters file by site done!!!" )
print("******************************************")

# site search by technology
print("\n")
print("******************************************")
print( "site search by technology..." )
print("******************************************")

# Unique sites per attribute per file
lte_failures_sites = list(df_faults_lte_unique[faults_lte_filter].unique())
gsm_sites = list( df_gsm_unique[gsm_filter].unique() )
lte_sites = list( df_lte_unique[lte_filter].unique() )
wbts_sites = list( df_wbts_unique[wbts_filter].unique() )
wcdma_sites = list( df_wcdma_unique[wcdma_filter].unique() )

print("\n")
print("******************************************")
print( "search for sites in LTE FAILURES..." )
print("******************************************")

found_sites_lte_failures = []
#total_items_searched = len( sites_to_search )
#found_items_counter_lte_failures = 0
for item in sites_to_search:
    if item in lte_failures_sites:
        #found_items_counter_lte_failures += 1
        found_sites_lte_failures.append( item )

print( f'Found sites in LTE FAILURES: {found_sites_lte_failures}' )

print("\n")
print("******************************************")
print( "search for sites in GSM..." )
print("******************************************")

found_sites_gsm = []
#total_items_searched = len( sites_to_search )
#found_items_counter = 0
for item in sites_to_search:
    if item in gsm_sites:
        #found_items_counter += 1
        found_sites_gsm.append( item )

print( f'Found sites in GSM: {found_sites_gsm}' )

print("\n")
print("******************************************")
print( "search for sites in LTE..." )
print("******************************************")

found_sites_lte = []
#total_items_searched = len( sites_to_search )
#found_items_counter = 0
for item in sites_to_search:
    if item in lte_sites:
        #found_items_counter += 1
        found_sites_lte.append( item )

print( f'Found sites in LTE: {found_sites_lte}' )

print("\n")
print("******************************************")
print( "search for sites in WBTS..." )
print("******************************************")

found_sites_wbts = []
#total_items_searched = len( sites_to_search )
#found_items_counter = 0
for item in sites_to_search:
    if item in wbts_sites:
        #found_items_counter += 1
        found_sites_wbts.append( item )

print( f'Found sites in WBTS: {found_sites_wbts}' )

print("\n")
print("******************************************")
print( "search for sites in WCDMA..." )
print("******************************************")

found_sites_wcdma = []
#total_items_searched = len( sites_to_search )
#found_items_counter = 0
for item in sites_to_search:
    if item in wcdma_sites:
        #found_items_counter += 1
        found_sites_wcdma.append( item )

print( f'Found sites in WCDMA: {found_sites_wcdma}' )

print("\n")
print("******************************************")
print( "site search by technology done!!!" )
print("******************************************")

# Copy template by technology and save as many times as sites found

# ***** Save the files in specifics templates by technology************
print("\n")
print("******************************************")
print( "Saving files by technology..." )
print("******************************************")

# Cleaning the folder output
print("\n")
print("******************************************")
print( "removing existing files..." )
print("******************************************")
dest_path = r"output/"
for file in os.listdir( dest_path ):
    existing_file = dest_path + file
    os.remove( existing_file )

print("******************************************")
print( "existing files removed successfuly!" )
print("******************************************")


print("\n")
print("******************************************")
print( " Creating files per site 2G ..." )
print("******************************************")

# templates path
if os_dev == "l":
    src_path_2g = r"plantilla/Alertas Tempranas_2G.xlsx"
elif os_dev == "w":
    src_path_2g = r"plantilla\Alertas Tempranas_2G.xlsx"

# destination path
dest_path = r"output/"

shutil.copy( src_path_2g, dest_path )

# rename the file
for file_name in os.listdir(dest_path):
    if "2G" in file_name:
        for file in range( len( found_sites_gsm )):
            
            old_name_2g = dest_path + file_name
            new_name_dest_2g = dest_path + found_sites_gsm[file]+'_' + file_name
            
            os.rename( old_name_2g, new_name_dest_2g )
            shutil.copy( src_path_2g, dest_path )
            
        os.remove( old_name_2g )
    else:
        pass
print("\n")
print("********************************************************")
print( "files per site 2G created successfully!!!..." )
print("********************************************************")


print("\n")
print("******************************************")
print( " Creating files per site 3G ..." )
print("******************************************")

# templates path
if os_dev == "l":
    src_path_3g = r"plantilla/Alertas Tempranas_3G.xlsx"
elif os_dev == "w":
    src_path_3g = r"plantilla\Alertas Tempranas_3G.xlsx"

# destination path
dest_path = r"output/"

shutil.copy( src_path_3g, dest_path )

# rename the file
for file_name in os.listdir(dest_path):
    if "3G" in file_name:
        for file in range( len( found_sites_wbts )):
            
            old_name_3g = dest_path + file_name
            new_name_dest_3g = dest_path + found_sites_wbts[file]+'_' + file_name
            
            os.rename( old_name_3g, new_name_dest_3g )
            shutil.copy( src_path_3g, dest_path )
            
        os.remove( old_name_3g )
    else:
        pass
print("\n")
print("********************************************************")
print( "files per site 3G created successfully!!!..." )
print("********************************************************")

# savig LTE FAULTS
print("\n")
print("******************************************")
print( " Creating files per site 4G..." )
print("******************************************")

# templates path
if os_dev == "l":
    src_path_4g = r"plantilla/Alertas Tempranas_4G.xlsx"
elif os_dev == "w":
    src_path_4g = r"plantilla\Alertas Tempranas_4G.xlsx"



# destination path
dest_path = r"output/"

shutil.copy( src_path_4g, dest_path )

# rename the file
for file_name in os.listdir(dest_path):
    if "4G" in file_name:
        for file in range( len( found_sites_lte_failures )):
            
            old_name_4g = dest_path + file_name
            new_name_dest_4g = dest_path + found_sites_lte_failures[file] + '_' + file_name
            
            os.rename( old_name_4g, new_name_dest_4g )
            shutil.copy( src_path_4g, dest_path )
            
        os.remove( old_name_4g )
    else:
        pass
print("\n")
print("********************************************************")
print( "files per site 4G created successfully!!! ..." )
print("********************************************************")

#############################################################
#**** create technology-consolidated files in input folder***
#############################################################
print("\n")
print("********************************************************")
print( "create technology-consolidated files in input folder..." )
print("********************************************************")

# destination path input folder
dest_path_input = r"input/"

# templates path
src_path_plantilla = r"plantilla/"
for consolidated_file in os.listdir(src_path_plantilla):
    src_path = src_path_plantilla + consolidated_file
    
    if consolidated_file in os.listdir( dest_path_input ):
        os.remove( dest_path_input + consolidated_file )
        shutil.copy( src_path, dest_path_input )    
    
    else:
        
        shutil.copy( src_path, dest_path_input )
print("********************************************************")
print( "create technology-consolidated files in input folder done!!" )
print("********************************************************")

#############################################################
#**** filter the data according to the indicated sites*****
#############################################################

# Saves the filtered data in a dictionary. 
# By key of the dictionary is the site and by value the data

# LTE FAILURES Dictionary 
print("\n")
print("********************************************************")
print("LTE FAULTS filter...")
print("********************************************************")
dic_lte_faults = {}
for item in found_sites_lte_failures:
    dic_lte_faults[item] = df_faults_lte_unique[ 
                        df_faults_lte_unique[ faults_lte_filter ] ==  item 
                                               ]
    print( f'{item}: {dic_lte_faults[item].shape}' )

print("********************************************************")
print("LTE FAULTS filter done!!!")
print("********************************************************")

# GSM Dictionary 
print("\n")
print("********************************************************")
print("GSM filter...")
print("********************************************************")
dic_gsm = {}
for item in found_sites_gsm:
    dic_gsm[item] = df_gsm_unique[ 
                    df_gsm_unique[ gsm_filter ] ==  item 
                                 ]
    print( f'{item}: {dic_gsm[item].shape}' )

print("********************************************************")
print("GSM filter done!!!")
print("********************************************************")
    
# # LTE Dictionary 
print("\n")
print("********************************************************")
print("LTE filter...")
print("********************************************************")
dic_lte = {}
for item in found_sites_lte:
    dic_lte[item] = df_lte_unique[ 
                    df_lte_unique[ lte_filter ] ==  item 
                                 ]
    print( f'{item}: {dic_lte[item].shape}' )

print("********************************************************")
print("LTE filter done!!!")
print("********************************************************")
    
    
# WBTS Dictionary 
print("\n")
print("********************************************************")
print("WBTS filter...")
print("********************************************************")
dic_wbts = {}
for item in found_sites_wbts:
    dic_wbts[item] = df_wbts_unique[ 
                     df_wbts_unique[ wbts_filter ] ==  item 
                                    ]
    print( f'{item}: {dic_wbts[item].shape}' )

print("********************************************************")
print("WBTS filter done!!!")
print("********************************************************")
    
# WCDMA Dictionary
print("\n")
print("********************************************************")
print("WCDMA filter:")
print("********************************************************")
dic_wcdma = {}
for item in found_sites_wcdma:
    dic_wcdma[item] = df_wcdma_unique[ 
                      df_wcdma_unique[ wcdma_filter ] ==  item 
                                    ]
    print( f'{item}: {dic_wcdma[item].shape}' )

print("********************************************************")
print("WCDMA filter done!!!")
print("********************************************************")

#############################################################
#**** data injection in filterd files*****
#############################################################

print("\n")
print("********************************************************")
print("4G data injection...")
print("********************************************************")

########## Data injection FAULTS LTE #########
# loop through existing files
for file_name in os.listdir(dest_path):
    if "4G" in file_name:
        # file filtered path
        path_file_4g = dest_path + file_name
        # 
        for site in dic_lte_faults:
            if site in path_file_4g:
                # data injection
                with pd.ExcelWriter( 
                                    path_file_4g,
                                    mode='a', 
                                    engine='openpyxl', 
                                    if_sheet_exists='overlay' ) as writer:
                    
                    # reading the dimensions of the existing file
                    reader_faults_lte = pd.read_excel( path_file_4g, sheet_name='Data2' )
                    start_row_faults_lte = len( reader_faults_lte ) + 1
                    
                    # fill the specific df in an existing sheet
                    dic_lte_faults[ site ].to_excel( 
                                                writer, 
                                                sheet_name = 'Data2', 
                                                index = False,
                                                header = None,
                                                startrow = start_row_faults_lte
                                                )
                      
            else:
                pass
                
    else:
        pass
    
########## Data injection LTE #########
# loop through existing files
for file_name in os.listdir(dest_path):
    if "4G" in file_name:
        # file filtered path
        path_file_4g = dest_path + file_name
        # 
        for site in dic_lte:
            if site in path_file_4g:
                # data injection
                with pd.ExcelWriter( 
                                    path_file_4g,
                                    mode='a', 
                                    engine='openpyxl', 
                                    if_sheet_exists='overlay' ) as writer:
                    
                    # reading the dimensions of the existing file
                    reader_lte = pd.read_excel( path_file_4g, sheet_name='Data' )
                    start_row_lte = len( reader_lte ) + 1
                    
                    # fill the specific df in an existing sheet
                    dic_lte[ site ].to_excel( 
                                                writer, 
                                                sheet_name = 'Data', 
                                                index = False,
                                                header = None,
                                                startrow = start_row_lte
                                                )
                      
            else:
                pass
                
    else:
        pass

print("********************************************************")
print("4G data injection, done!")
print("********************************************************")

print("\n")
print("********************************************************")
print("3G data injection...")
print("********************************************************")
########## Data injection WCDMA #########
# loop through existing files
for file_name in os.listdir(dest_path):
    if "3G" in file_name:
        # file filtered path
        path_file_3g = dest_path + file_name
        # 
        for site in dic_wcdma:
            if site in path_file_3g:
                # data injection
                with pd.ExcelWriter( 
                                    path_file_3g,
                                    mode='a', 
                                    engine='openpyxl', 
                                    if_sheet_exists='overlay' ) as writer:
                    
                    # reading the dimensions of the existing file
                    reader_wcdma = pd.read_excel( path_file_3g, sheet_name='Data' )
                    start_row_wcdma = len( reader_wcdma ) + 1
                    
                    # fill the specific df in an existing sheet
                    dic_wcdma[ site ].to_excel( 
                                                writer, 
                                                sheet_name = 'Data',
                                                index = False,
                                                header = None,
                                                startrow = start_row_wcdma
                                                )
                      
            else:
                pass
                
    else:
        pass

########## Data injection WBTS #########
# loop through existing files
for file_name in os.listdir(dest_path):
    if "3G" in file_name:
        # file filtered path
        path_file_3g = dest_path + file_name
        # 
        for site in dic_wbts:
            if site in path_file_3g:
                # data injection
                with pd.ExcelWriter( 
                                    path_file_3g,
                                    mode='a', 
                                    engine='openpyxl', 
                                    if_sheet_exists='overlay' ) as writer:
                    
                    # reading the dimensions of the existing file
                    reader_wbts = pd.read_excel( path_file_3g, sheet_name='Data2' )
                    start_row_wbts = len( reader_wbts ) + 1
                    
                    # fill the specific df in an existing sheet
                    dic_wbts[ site ].to_excel( 
                                                writer, 
                                                sheet_name = 'Data2', 
                                                index = False,
                                                header = None,
                                                startrow = start_row_wbts
                                                )
                      
            else:
                pass
                
    else:
        pass

print("********************************************************")
print("3G data injection, done!")
print("********************************************************")

print("\n")
print("********************************************************")
print("2G data injection...")
print("********************************************************")
########## Data injection GSM #########
# loop through existing files
for file_name in os.listdir(dest_path):
    if "2G" in file_name:
        # file filtered path
        path_file_2g = dest_path + file_name
        # 
        for site in dic_gsm:
            if site in path_file_2g:
                # data injection
                with pd.ExcelWriter( 
                                    path_file_2g,
                                    mode='a', 
                                    engine='openpyxl', 
                                    if_sheet_exists='overlay' ) as writer:
                    
                    # reading the dimensions of the existing file
                    reader_gsm = pd.read_excel( path_file_2g, sheet_name='Data' )
                    start_row_gsm = len( reader_gsm ) + 1
                    
                    # fill the specific df in an existing sheet
                    dic_gsm[ site ].to_excel( 
                                                writer, 
                                                sheet_name = 'Data',
                                                index = False,
                                                header = None,
                                                startrow = start_row_gsm
                                                )
                      
            else:
                pass
                
    else:
        pass
    
print("********************************************************")
print("2G data injection, done!")
print("********************************************************")

#############################################################
#**** data injection in consolidated files*****
#############################################################

print("\n")
print("********************************************************")
print("2G data injection consolidated file...")
print("********************************************************")
########## Data injection GSM consolidated file #########

# loop through existing files
for file_name in os.listdir(dest_path_input):
    if "2G" in file_name:
        # file filtered path
        path_file_2g_cf = dest_path_input + file_name
        # 
        for site in dic_gsm:
            #if site in path_file_2g_cf:
                # data injection
            with pd.ExcelWriter( 
                                path_file_2g_cf,
                                mode='a', 
                                engine='openpyxl', 
                                if_sheet_exists='overlay' ) as writer:
                
                    
                # reading the dimensions of the existing file
                reader_gsm = pd.read_excel( path_file_2g_cf, sheet_name='Data' )
                start_row_gsm = len( reader_gsm ) + 1
                    
                # fill the specific df in an existing sheet
                dic_gsm[ site ].to_excel( 
                                            writer, 
                                            sheet_name = 'Data',
                                            index = False,
                                            header = None,
                                            startrow = start_row_gsm
                                            )
                      
            #else:
            #    pass
                
    else:
        pass
    
print("********************************************************")
print("2G data injection consolidated file: done!!!")
print("********************************************************")

print("\n")
print("********************************************************")
print("3G data injection consolidated file...")
print("********************************************************")
########## Data injection WCDMA #########
# loop through existing files
for file_name in os.listdir(dest_path_input):
    if "3G" in file_name:
        # file filtered path
        path_file_3g_cf = dest_path_input + file_name
        # 
        for site in dic_wcdma:
        #if site in path_file_3g:
            # data injection
            with pd.ExcelWriter( 
                                path_file_3g_cf,
                                mode='a', 
                                engine='openpyxl', 
                                if_sheet_exists='overlay' ) as writer:
                    
                # reading the dimensions of the existing file
                reader_wcdma = pd.read_excel( path_file_3g_cf, sheet_name='Data' )
                start_row_wcdma = len( reader_wcdma ) + 1
                    
                # fill the specific df in an existing sheet
                dic_wcdma[ site ].to_excel( 
                                            writer, 
                                            sheet_name = 'Data',
                                            index = False,
                                            header = None,
                                            startrow = start_row_wcdma
                                            )
                      
            # else:
            #     pass
                
    else:
        pass

########## Data injection WBTS #########
# loop through existing files
for file_name in os.listdir(dest_path_input):
    if "3G" in file_name:
        # file filtered path
        path_file_3g_cf = dest_path_input + file_name
        # 
        for site in dic_wbts:
            #if site in path_file_3g:
            # data injection
            with pd.ExcelWriter( 
                                path_file_3g_cf,
                                mode='a', 
                                engine='openpyxl', 
                                if_sheet_exists='overlay' ) as writer:
                    
                # reading the dimensions of the existing file
                reader_wbts = pd.read_excel( path_file_3g_cf, sheet_name='Data2' )
                start_row_wbts = len( reader_wbts ) + 1
                    
                # fill the specific df in an existing sheet
                dic_wbts[ site ].to_excel( 
                                            writer, 
                                            sheet_name = 'Data2', 
                                            index = False,
                                            header = None,
                                            startrow = start_row_wbts
                                            )
                      
            # else:
            #     pass
                
    else:
        pass

print("********************************************************")
print("3G data injection consolidated file: done!!!")
print("********************************************************")

#/////////////// WORK IN PROGRESS/////////////////

print("\n")
print("********************************************************")
print("4G data injection consolidated file...")
print("********************************************************")

########## Data injection FAULTS LTE #########
# loop through existing files
for file_name in os.listdir(dest_path_input):
    if "4G" in file_name:
        # file filtered path
        path_file_4g_cf = dest_path_input + file_name
        # 
        for site in dic_lte_faults:
            #if site in path_file_4g:
                # data injection
            with pd.ExcelWriter( 
                                path_file_4g_cf,
                                mode='a', 
                                engine='openpyxl', 
                                if_sheet_exists='overlay' ) as writer:
                                    
                # reading the dimensions of the existing file
                reader_faults_lte = pd.read_excel( path_file_4g_cf, sheet_name='Data2' )
                start_row_faults_lte = len( reader_faults_lte ) + 1
                    
                # fill the specific df in an existing sheet
                dic_lte_faults[ site ].to_excel( 
                                            writer, 
                                            sheet_name = 'Data2', 
                                            index = False,
                                            header = None,
                                            startrow = start_row_faults_lte
                                            )      
            # else:
            #     pass
                
    else:
        pass
    
########## Data injection LTE #########
# loop through existing files
for file_name in os.listdir(dest_path_input):
    if "4G" in file_name:
        # file filtered path
        path_file_4g_cf = dest_path_input + file_name
        # 
        for site in dic_lte:
            #if site in path_file_4g:
                # data injection
            with pd.ExcelWriter( 
                                path_file_4g_cf,
                                mode='a', 
                                engine='openpyxl', 
                                if_sheet_exists='overlay' ) as writer:
                                    
                # reading the dimensions of the existing file
                reader_lte = pd.read_excel( path_file_4g_cf, sheet_name='Data' )
                start_row_lte = len( reader_lte ) + 1
                    
                # fill the specific df in an existing sheet
                dic_lte[ site ].to_excel( 
                                        writer, 
                                        sheet_name = 'Data', 
                                        index = False,
                                        header = None,
                                        startrow = start_row_lte
                                        )
                      
            # else:
            #     pass
                
    else:
        pass

print("********************************************************")
print("4G data injection consolidated file: Done!!!")
print("********************************************************")


# Saving 4G files
# path_4g = 'output/Alertas Tempranas_4G.xlsx'

# with pd.ExcelWriter( 
#                     path_4g,
#                     mode='a', 
#                     engine='openpyxl', 
#                     if_sheet_exists='overlay' ) as writer:
    
#     # reading the dimensions of the existing file
#     reader_faults_lte = pd.read_excel( path_4g, sheet_name='Data2' )
#     start_row_faults_lte = len( reader_faults_lte ) + 1
    
#     # fill the specific df in an existing sheet
#     df_faults_lte_unique.to_excel( 
#                                 writer, 
#                                 sheet_name = 'Data2', 
#                                 index = False,
#                                 header = None,
#                                 startrow = start_row_faults_lte
#                                 )
# print("\n")
# print("******************************************")
# print( "Saving data LTE FAULTS 4G done!!!" )
# print("******************************************")

# # savig LTE FAULTS
# print("\n")
# print("******************************************")
# print( "Saving data LTE 4G (Data)..." )
# print("******************************************")

# # saving 4G files
# path_4g = 'output/Alertas Tempranas_4G.xlsx'

# with pd.ExcelWriter( 
#                     path_4g,
#                     mode='a', 
#                     engine='openpyxl', 
#                     if_sheet_exists='overlay' ) as writer:
    
#     # reading the dimensions of the existing file
#     reader_lte = pd.read_excel( path_4g, sheet_name='Data' )
#     start_row_lte = len( reader_lte ) + 1
    
#     # fill the specific df in an existing sheet
#     df_lte_unique.to_excel( 
#                             writer, 
#                             sheet_name='Data', 
#                             index = False,
#                             header = None,
#                             startrow = start_row_lte
#                             )
# print("\n")
# print("******************************************")
# print( "Saving data LTE 4G done!!!" )
# print("******************************************")

# # savig 3G files
# print("\n")
# print("******************************************")
# print( "Saving data WCDMA 3G (Data)..." )
# print("******************************************")

# # saving 3G files
# path_3g = 'output/Alertas Tempranas_3G.xlsx'

# with pd.ExcelWriter( 
#                     path_3g,
#                     mode='a', 
#                     engine='openpyxl', 
#                     if_sheet_exists='overlay' ) as writer:
    
#     # reading the dimensions of the existing file
#     reader_wcdma = pd.read_excel( path_3g, sheet_name='Data' )
#     start_row_wcdma = len( reader_wcdma ) + 1
    
#     # fill with the specific df in an existing sheet
#     df_wcdma_unique.to_excel( 
#                             writer, 
#                             sheet_name='Data', 
#                             index = False,
#                             header = None,
#                             startrow = start_row_wcdma
#                             )
# print("\n")
# print("******************************************")
# print( "Saving data WCDMA 3G done!!!" )
# print("******************************************")

# print("\n")
# print("******************************************")
# print( "Saving data WBTS 3G (Data2)..." )
# print("******************************************")

# # saving 3G files
# path_3g = 'output/Alertas Tempranas_3G.xlsx'

# with pd.ExcelWriter( 
#                     path_3g,
#                     mode='a', 
#                     engine='openpyxl', 
#                     if_sheet_exists='overlay' ) as writer:
    
#     # reading the dimensions of the existing file
#     reader_wbts = pd.read_excel( path_3g, sheet_name='Data2' )
#     start_row_wbts = len( reader_wbts ) + 1
    
#     # fill with the specific df in an existing sheet
#     df_wbts_unique.to_excel( 
#                             writer, 
#                             sheet_name='Data2', 
#                             index = False,
#                             header = None,
#                             startrow = start_row_wbts
#                             )
# print("\n")
# print("******************************************")
# print( "Saving data WBTS 3G done!!!" )
# print("******************************************")

# # saving 2G files
# print("\n")
# print("******************************************")
# print( "Saving data GSM 2G (Data)..." )
# print("******************************************")

# # saving 2G files
# path_2g = 'output/Alertas Tempranas_2G.xlsx'

# with pd.ExcelWriter( 
#                     path_2g,
#                     mode='a', 
#                     engine='openpyxl', 
#                     if_sheet_exists='overlay' ) as writer:
    
#     # reading the dimensions of the existing file
#     reader_gsm = pd.read_excel( path_2g, sheet_name='Data' )
#     start_row_gsm = len( reader_gsm ) + 1

#     # fill with the specific df in an existing sheet
#     df_gsm_unique.to_excel( 
#                             writer, 
#                             sheet_name='Data', 
#                             index = False,
#                             header = None,
#                             startrow = start_row_gsm
#                             )
# print("\n")
# print("******************************************")
# print( "Saving data GSM 2G done!!!" )
# print("******************************************")


#############################################################
#**** filter the data according to the indicated sites*****
#############################################################

# Saves the filtered data in a dictionary. 
# By key of the dictionary is the site and by value the data

# LTE FAILURES Dictionary 
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
#     file_path.parent.mkdir( parents=True, exist_done=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)
    
# print("Exporting LTE FAULTS files done!")

# # Exporting GSM files
# print("Exporting GSM files ... ")
# for key, value in dic_gsm.items():
#     file_path = Path( f'{output_folder}/{key}_Alertas Tempranas_2G.csv' )
#     file_path.parent.mkdir( parents=True, exist_done=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)

# print("Exporting GSM files done!")

# # Exporting LTE files
# print("Exporting LTE files... ")
# for key, value in dic_lte.items():
#     file_path = Path( f'{output_folder}/{key}_lte_Alertas Tempranas_4G.csv' )
#     file_path.parent.mkdir( parents=True, exist_done=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)
    
# print("Exporting LTE files done")

# # Exporting WBTS files
# print("Exporting WBTS files... ")
# for key, value in dic_wbts.items():
#     file_path = Path( f'{output_folder}/{key}_wbts_Alertas Tempranas_3G.csv' )
#     file_path.parent.mkdir( parents=True, exist_done=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)

# print("Exporting WBTS files done!")

# # Exporting WCDMA files
# print("Exporting WCDMA files... ")
# for key, value in dic_wcdma.items():
#     file_path = Path( f'{output_folder}/{key}_wcdma_Alertas Tempranas_3G.csv' )
#     file_path.parent.mkdir( parents=True, exist_done=True )
#     #print(f'{key}: {value.shape}')
#     value.to_csv(file_path)
    
# print("Exporting WCDMA files done!")