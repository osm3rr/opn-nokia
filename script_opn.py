# necessary libraries
import pandas as pd
import glob


# ruta base de la ubicación de los files
path = "/home/opm/Documentos-opm/OPN_COLOMBIA/ANALISYS/input_files"

# Lista con el nombre de todos los archivos excel
xlsx_files_list = glob.glob( path + "/*.xlsx" )

# identifiers by technology
faults_lte = "Fallas_TX_LTE"
gsm_monitoring = "GSM_NPO_Monitoring_v4"
lte_monitoring = "LTE_FL16A_NPO_Monitoring_V4"
wbts_monitoring = "WBTS_WCDMA17_NPO_MONITORING"
wcdma_monitoring = "WCDMA17_NPO_Monitoring_V4"

# Revisar cada archivo excel según tecnologia

# initialize counters
faults_lte_count = 0
gsm_monitoring_count = 0
lte_monitoring_count = 0
wbts_monitoring_count = 0
wcdma_monitoring_count = 0

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
            # print( f'shape df_faults_lte_1: {df_faults_lte_1.shape}, file: {faults_lte_count}' )
            
        else:
            df_faults_lte_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            faults_lte_count += 1
            
            df_faults_lte_2 = df_faults_lte_2.drop( labels=0, axis=0 )
            
            df_faults_lte_total = pd.concat( [ df_faults_lte_1, df_faults_lte_2 ],
                                            ignore_index=True )
            
            df_faults_lte_1 = df_faults_lte_total.copy()
            # validation print    
            #print( f'shape df_faults_lte_total: {df_lte_total.shape}' )
            # print( f'shape df_faults_lte_total: {df_lte_total.shape}, file: {faults_lte_count}' )
            
        
        
    ## search GSM monitoring***
    elif gsm_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if gsm_monitoring_count < 1:
            
            gsm_monitoring_count += 1
            
            df_gsm_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_gsm_1 = df_gsm_1.drop( labels=0, axis=0 )
            # validation print
            # print( f'shape df_gsm_1: {df_gsm_1.shape}, file: {gsm_monitoring_count}' )
            
            
        else:
            df_gsm_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_gsm_2 = df_gsm_2.drop( labels=0, axis=0 )
            
            df_gsm_total = pd.concat( [ df_gsm_1, df_gsm_2 ], ignore_index=True )
            
            df_gsm_1 = df_gsm_total.copy()
            # validation print    
            # print( f'shape df_gsm_total: {df_gsm_total.shape}, file: {gsm_monitoring_count}' )
            
                
            
    ## search LTE monitoring 
    elif lte_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if lte_monitoring_count < 1:
            
            lte_monitoring_count += 1
            
            df_lte_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_lte_1 = df_lte_1.drop( labels=0, axis=0 )
            # validation print
            # print( f'shape df_lte_1: {df_lte_1.shape}, file: {lte_monitoring_count}' )
            
            
        else:
            df_lte_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            lte_monitoring_count += 1
            
            df_lte_2 = df_lte_2.drop( labels=0, axis=0 )
            
            df_lte_total = pd.concat( [ df_lte_1, df_lte_2 ], ignore_index=True )
            
            df_lte_1 = df_lte_total.copy()
            # validation print    
            # print( f'shape df_lte_total: {df_lte_total.shape}, file: {lte_monitoring_count}' )
            
        
                
    ## search WBTS monitoring
    elif wbts_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if wbts_monitoring_count < 1:
            
            wbts_monitoring_count += 1
            
            df_wbts_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_wbts_1 = df_wbts_1.drop( labels=0, axis=0 )
            # validation print
            #print( f'shape df_wbts_1: {df_wbts_1.shape}, file: {wbts_monitoring_count}' )
            
            
        else:
            df_wbts_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            wbts_monitoring_count += 1
            
            df_wbts_2 = df_wbts_2.drop( labels=0, axis=0 )
            
            df_wbts_total = pd.concat( [ df_wbts_1, df_wbts_2 ], ignore_index=True )
            
            df_wbts_1 = df_wbts_total.copy()
            # validation print    
            # print( f'shape df_wbts_total: {df_wbts_total.shape}, file: {wbts_monitoring_count}' )
            

        
    ## search WCDA monitoring
    elif wcdma_monitoring in xlsx_files_list[ xlsx_file ]:
        
        # read file
        if wcdma_monitoring_count < 1:
            
            wcdma_monitoring_count += 1
            
            df_wcdma_1 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            df_wcdma_1 = df_wcdma_1.drop( labels=0, axis=0 )
            # validation print
            #print( f'shape df_wcdma_1: {df_wcdma_1.shape}, file: {wcdma_monitoring_count}' )
            
            
        else:
            df_wcdma_2 = pd.read_excel( io=xlsx_files_list[ xlsx_file ] )
            
            wcdma_monitoring_count += 1
            
            df_wcdma_2 = df_wcdma_2.drop( labels=0, axis=0 )
            
            df_wcdma_total = pd.concat( [ df_wcdma_1, df_wcdma_2 ], ignore_index=True )
            
            df_wcdma_1 = df_wcdma_total.copy()
            # validation print    
            #print( f'shape df_wcdma_total: {df_wcdma_total.shape}, file: {wcdma_monitoring_count}' )


    
    ## No valid files
    else:
        #print( "No valid files" )
        pass
    
# Remove duplicate values

# Atributos para eliminar valores duplicados
faults_lte_duplicate = [ 'Period start time', 'LNBTS name', 'ATT_INTER_ENB_HO (M8014C6)' ]
gsm_monitoring_duplicate = [ 'Period start time', 'BSC name', 'BTS name' ]
lte_monitoring_duplicate = [ 'Period start time', 'LNCEL name' ]
wbts_monitoring_duplicate = [ 'Period start time', 'WBTS name', 'WBTS ID' ]
wcdma_monitoring_duplicate = [ 'Period start time', 'WCEL name', 'WCEL ID' ]

# Removiendo valores duplicados

print( f'shape before delete duplicate FAULT LTE: {df_faults_lte_total.shape}' )

# Eliminar duplicados en faults lte
df_faults_lte_filtered = df_faults_lte_total.drop_duplicates( 
                                                             subset=faults_lte_duplicate,
                                                             ignore_index=True 
                                                             )

print( f'shape after delete duplicate FAULT LTE: {df_faults_lte_filtered.shape}' )

# Eliminar duplicados en gsm total
print( f'shape before delete duplicate GSM: {df_gsm_total.shape}' )
df_gsm_filtered = df_gsm_total.drop_duplicates( 
                                               subset=gsm_monitoring_duplicate,
                                                             ignore_index=True 
                                                             )

print( f'shape after delete duplicate GSM: {df_gsm_filtered.shape}' )

# Eliminar duplicados en LTE total
print( f'shape before delete duplicate LTE: {df_lte_total.shape}' )
df_lte_filtered = df_lte_total.drop_duplicates( 
                                               subset=lte_monitoring_duplicate,
                                                        ignore_index=True 
                                                              )

print( f'shape after delete duplicate LTE: {df_lte_filtered.shape}' )

# Eliminar duplicados en WBTS total [pendind]
print( f'shape before delete duplicate WBTS: {df_wbts_total.shape}' )
df_wbts_filtered = df_wbts_total.drop_duplicates( 
                                               subset=wbts_monitoring_duplicate,
                                                        ignore_index=True 
                                                              )

print( f'shape after delete duplicate WBTS: {df_wbts_filtered.shape}' )

# Eliminar duplicados en WCDMA total [pendind]
print( f'shape before delete duplicate WCDMA: {df_wcdma_total.shape}' )
df_wcdma_filtered = df_wcdma_total.drop_duplicates( 
                                               subset=wcdma_monitoring_duplicate,
                                                        ignore_index=True 
                                                              )

print( f'shape after delete duplicate WCDMA: {df_wcdma_filtered.shape}' )