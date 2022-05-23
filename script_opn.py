# necessary libraries
import pandas as pd
import glob
from pathlib import Path


# base path of files location
path = "/home/opm/Documentos-opm/OPN_COLOMBIA/ANALISYS/input_files"

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

#************************************************
# normaliza el nombre de los sitios por archivo 

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

# Removing duplicate values FAULT LTE
print( f'Shape before remove duplicates in LTE FAULT: {df_faults_lte_total.shape}' )

# Eliminar duplicados en faults lte
df_faults_lte_unique = df_faults_lte_total.drop_duplicates( 
                                                             subset=faults_lte_duplicate,
                                                             ignore_index=True 
                                                             )

print( f'Shape after remove duplicates LTE FAULT: {df_faults_lte_unique.shape}' )

# Eliminar duplicados en gsm total
print( f'Shape before remove duplicates GSM: {df_gsm_total.shape}' )
df_gsm_unique = df_gsm_total.drop_duplicates( 
                                               subset=gsm_monitoring_duplicate,
                                                             ignore_index=True 
                                                             )

print( f'Shape after remove duplicates GSM: {df_gsm_unique.shape}' )

# Eliminar duplicados en LTE total
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

# Eliminar duplicados en WCDMA total [pendind]
print( f'Shape before remove duplicates WCDMA: {df_wcdma_total.shape}' )
df_wcdma_unique = df_wcdma_total.drop_duplicates( 
                                               subset=wcdma_monitoring_duplicate,
                                                        ignore_index=True 
                                                              )

print( f'Shape after remove duplicates WCDMA: {df_wcdma_unique.shape}' )



# *************************************
# Filtrado de los archivos por sitios únicos
# Diccionario por clave: nombre del df y por valor el df
# correspondiente


print("\n")
print("******************************************")
print( "Filter by site..." )
print("******************************************")

# Unique sites per attribute per file
fault_lte_sites = list(df_faults_lte_unique[faults_lte_filter].unique())
gsm_sites = list( df_gsm_unique[gsm_filter].unique() )
lte_sites = list( df_lte_unique[lte_filter].unique() )
wbts_sites = list( df_wbts_unique[wbts_filter].unique() )
wcdma_sites = list( df_wcdma_unique[wcdma_filter].unique() )

# Dictionary FAULTS LTE
print("LTE FAULTS filter :")
d_f_lte = {}
for item in fault_lte_sites:
    d_f_lte[item] = df_faults_lte_unique[ 
                      df_faults_lte_unique[ faults_lte_filter ] ==  item 
                                  ]
    print( f'df_{item}: {d_f_lte[item].shape}' )

# Dictionary GSM
print("GSM filter:")
d_gsm = {}
for item in gsm_sites:
    d_gsm[item] = df_gsm_unique[ 
                      df_gsm_unique[ gsm_filter ] ==  item 
                                ]
    print( f'df_{item}: {d_gsm[item].shape}' )
    
# Dictionary LTE
print("LTE filter:")
d_lte = {}
for item in lte_sites:
    d_lte[item] = df_lte_unique[ 
                      df_lte_unique[ lte_filter ] ==  item 
                                ]
    print( f'df_{item}: {d_lte[item].shape}' )
    
# WBTS Dictionary 
print("WBTS filter:")
d_wbts = {}
for item in wbts_sites:
    d_wbts[item] = df_wbts_unique[ 
                      df_wbts_unique[ wbts_filter ] ==  item 
                                ]
    print( f'df_{item}: {d_wbts[item].shape}' )
    
# WCDMA Dictionary
print("WCDMA filter:")
d_wcdma = {}
for item in wcdma_sites:
    d_wcdma[item] = df_wcdma_unique[ 
                      df_wcdma_unique[ wcdma_filter ] ==  item 
                                ]
    print( f'df_{item}: {d_wcdma[item].shape}' )
    
# Exporting files filtered by site
print("\n")
print("******************************************")
print( "Exporting files filtered by site..." )
print("******************************************")

# Exporting LTE FAULTS files
print("Exporting LTE FAULTS files ... ")
for key, value in d_f_lte.items():
    file_path = Path( f'output_files/fallas_lte_{key}.csv' )
    file_path.parent.mkdir( parents=True, exist_ok=True )
    #print(f'{key}: {value.shape}')
    value.to_csv(file_path)
    
print("Exporting LTE FAULTS files OK!")

# Exporting GSM files
print("Exporting GSM files ... ")
for key, value in d_gsm.items():
    file_path = Path( f'output_files/gsm_{key}.csv' )
    file_path.parent.mkdir( parents=True, exist_ok=True )
    #print(f'{key}: {value.shape}')
    value.to_csv(file_path)

print("Exporting GSM files OK!")

# Exporting LTE files
print("Exporting LTE files... ")
for key, value in d_lte.items():
    file_path = Path( f'output_files/lte_{key}.csv' )
    file_path.parent.mkdir( parents=True, exist_ok=True )
    #print(f'{key}: {value.shape}')
    value.to_csv(file_path)
    
print("Exporting LTE files OK")


# Exporting WBTS files
print("Exporting WBTS files... ")
for key, value in d_wbts.items():
    file_path = Path( f'output_files/wbts_{key}.csv' )
    file_path.parent.mkdir( parents=True, exist_ok=True )
    #print(f'{key}: {value.shape}')
    value.to_csv(file_path)

print("Exporting WBTS files OK!")

# Exporting WCDMA files
print("Exporting WCDMA files... ")
for key, value in d_wcdma.items():
    file_path = Path( f'output_files/wcdma_{key}.csv' )
    file_path.parent.mkdir( parents=True, exist_ok=True )
    #print(f'{key}: {value.shape}')
    value.to_csv(file_path)
    
print("Exporting WCDMA files OK!")

