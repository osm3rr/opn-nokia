# Function for processing data to graph
# return a df with data for 1 parameter

def data_to_graph_1(file_name: str, parameter: str ): 
    """
    Description: Generates a df from the parameter to analyze and 
    the name of the file filtered by technology and site.
    
    Inputs:
    file_name -> file name by site and technology 
    parameter -> attribute to analyse
    """
    # variables
    filter_by = "Sector"
    source = "Data"
    # source: "Data" 17 attributes
    
    dest_path = r"/home/opm/Documentos-opm/OPN_COLOMBIA/ANALYSIS/output/"
    #file_name = "BOG.Atavanza_Alertas Tempranas_4G.xlsx"
    
    path_file = dest_path + file_name


    # read the specific tab
    df_in = pd.read_excel( io=path_file, sheet_name= source )

    # attributes for the graph
    df_graph_1 = df_in[ [ 'Period start time', parameter, filter_by ] ]

    # rename the attribute 
    df_graph_1 = df_graph_1.rename( { "Period start time": "Etiquetas de fila"}, axis='columns')

    # change the format
    df_graph_1['Etiquetas de fila'] = df_graph_1['Etiquetas de fila'].dt.strftime( '%d/%m/%Y  %H:%M' )

    # uniques values for the attribute column
    column_list = list( df_graph_1[ filter_by ].unique() )

    # insert the first attribute
    column_list.insert( 0, "Etiquetas de fila" )

    # Dictionary for data package
    dict_graph1 = {}

    # the first value of dictionary
    dict_graph1[ column_list[0] ] = df_graph_1[ column_list[0] ] 

    # build a dictionary with 
    for item in range(1, len( column_list ) ):
        dict_graph1[ column_list[item] ] = df_graph_1[ df_graph_1[ filter_by ] == column_list[item] ][parameter]

    df_1 = pd.DataFrame( dict_graph1 )

    dict_st2 = {}
    for item in range(1, len( column_list ) ):
        dict_st2[ column_list[item] ] = df_1[ (df_1[ column_list[item] ] > 0)][[column_list[0], column_list[item]]]

    # create a consolidate df
    count = 1
    while ( count < len( dict_st2 ) ):
        global df_f
        
        if count == 1:
            df_f = dict_st2[column_list[count]].join(
                dict_st2[column_list[count + 1]].set_index( column_list[0] ),
                on=column_list[0] )

            count += 1
                    
        else:
            df_f = df_f.join( dict_st2[column_list[count + 1]].set_index( column_list[0] ),
                on=column_list[0] )

            count += 1
            
    # add the mean at the end
    df_f["Total general"] = df_f.iloc[ : , 1: ].mean( axis=1 )

    return df_f


# Function 2 for data injection in the specific file_name

def data_to_graph_2( file_name ):

    # parameters in 4G vs "Sector"
    pm_to_graph_data = [    
                        "Cell Avail excl BLU", "RACH Stp Completion SR",
                        "Total E-UTRAN RRC conn stp SR", "Data RB stp SR", 
                        "E-UTRAN E-RAB stp SR", "Intra eNB HO SR total", 
                        "Inter eNB E-UTRAN tot HO SR X2", "E-UTRAN Inter-Freq HO SR", 
                        "Avg PDCP cell thp UL", "Avg PDCP cell thp DL", 
                        "PDCP SDU Volume, DL", "PDCP SDU Volume, UL", 
                        "Average CQI", "AVG_RTWP_RX_ANT_1 (M8005C306)", 
                        "Avg UE distance", "VoLTE total traffic", 
                        "Avg active users per cell"
                        ]


    # source: "Data2"
    #pm_to_graph_data2 = ["SCTP X2 succ trans R", "SCTP S1 succ trans R"]

    # save in a dict the data for graph
    dict_graph = {}
    #file_name = "BOG.Atavanza_Alertas Tempranas_4G.xlsx"

    #path_file = dest_path + file_name

    for pm in range(len(pm_to_graph_data)):
        dict_to_graph[ pm_to_graph_data[pm] ] = data_to_graph_1(file_name, pm_to_graph_data[pm] )
        
    #////  data injection in the specific file_name ////
    
    # file filtered path
    dest_path_input = r"/home/opm/Documentos-opm/OPN_COLOMBIA/ANALYSIS/output/"
    path_file_4g = dest_path_input + file_name
    
    # sheet names
    sheet_names_4g = [ 'Cell Avail excl BLU', 'RACH',
                     'RRC', 'Radio Bearer', 'ERAB',
                     'Intra HO', 'Inter HO', 'Inter-Freq HO',
                     'Avg PDCP cell thp UL', 'Avg PDCP cell thp DL',
                     'PDCP SDU Volume, DL', 'PDCP SDU Volume, UL',
                     'Average CQI', 'AVG_RTWP', 'Avg UE distance',
                     'VoLTE total traffic', 'Avg active users per cell']
    
    # iterate each attribute in the dictionary
    for sheet_name in sheet_names_4g:
        
        # data injection
        with pd.ExcelWriter( 
                            path_file_4g,
                            mode='a', 
                            engine='openpyxl', 
                            if_sheet_exists='overlay' ) as writer:
            
            # reading the dimensions of the existing file
            reader_site = pd.read_excel( path_file_4g, sheet_name= sheet_name )
            start_row_site = len( reader_site ) + 1
                    
            # fill the specific df in an existing sheet
            dict_to_graph[ attribute ].to_excel( 
                                            writer, 
                                            sheet_name = sheet_name, 
                                            index = False,
                                            header = None,
                                            startrow = start_row_site
                                            )      
    
    #return dict_to_graph
# main script

# define operative system
os_ = "l"
    
if os_ == "w":
    dest_path = r"C:\PythonScripts\output"
    file_name = "\BOG.Atavanza_Alertas Tempranas_4G.xlsx"
    path_file = dest_path + file_name
        
elif os_ == "l":
    dest_path = r"/home/opm/Documentos-opm/OPN_COLOMBIA/ANALYSIS/output/"

# processing data for each file in the path file
for file_name in os.listdir(dest_path):
    if "4G" in file_name:
        path_file = dest_path + file_name
        print( file_name )

#data_to_graph_2( "BOG.Atavanza_Alertas Tempranas_4G.xlsx" )
        
    