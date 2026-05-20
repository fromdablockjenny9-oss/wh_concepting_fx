import pandas as pd
from category import data_analysis_category

import numpy as np
import json
import math
import copy


# Copyright (c) 2026 fromdablockjenny9-oss @Github
# This project and its source code are the property of fromdablockjenny9-oss @Github
# Unauthorized copying, modification, or distribution is prohibited
# fromdablockjenny9@gmail.com

def fx_print_param_fx(d):
    for key, value in d.items():
        print(key + ' = ' + 'my_parameters["' + key + '"]')
        
def fx_join_single_column(dataframe1, dataframe2, sku_col_name_df_1, sku_col_name_df_2, column_to_join):
    dataframe1 = dataframe1.copy(deep=True)
    dataframe2 = dataframe2.copy(deep=True)
    
    
    suffix = ''
    new_column_name = column_to_join
    
    while new_column_name in dataframe1.columns:
        suffix = f'_{int(suffix[1:]) + 1 if suffix else 1}'
        new_column_name = column_to_join + suffix
    
    assigned_column_name = new_column_name
    
    dataframe2 = dataframe2.rename(columns={column_to_join: assigned_column_name})
    result = dataframe1.merge(dataframe2[[sku_col_name_df_2, assigned_column_name]], 
                      left_on=sku_col_name_df_1, 
                      right_on=sku_col_name_df_2, 
                      how="left")
                    
    result.drop(columns=[sku_col_name_df_2], inplace=True)
    
    return result, assigned_column_name 
    
def format_float_with_commas(number, decimal_places=0):
    floored_number = round(number, decimal_places)
    formatted_number = f"{floored_number:,.{decimal_places}f}"
    
    return formatted_number
    
def add_row_to_df(df = "", str_0 = "", str_1 = "",str_2 = "",str_3 = "",str_4 = "",str_5 = "",str_6 = "",str_7 = "",str_8 = "",str_9 = "",str_10 = "",str_11 = "",str_12 = "",str_13 = "",str_14 = "",str_15 = ""):
    if isinstance(df, pd.DataFrame):
        new_row = {
        df.columns[0]: str(str_0), 
        df.columns[1]: str(str_1), 
        df.columns[2]: str(str_2),
        df.columns[3]: str(str_3),
        df.columns[4]: str(str_4), 
        df.columns[5]: str(str_5),
        df.columns[6]: str(str_6),
        df.columns[7]: str(str_7),
        df.columns[8]: str(str_8),
        df.columns[9]: str(str_9),
        df.columns[10]: str(str_10),
        df.columns[11]: str(str_11),
        df.columns[12]: str(str_12),
        df.columns[13]: str(str_13),
        df.columns[14]: str(str_14),
        df.columns[15]: str(str_15)
        }
        df.loc[len(df)] = new_row
        return df

        
    else:
        
        
        if str_0 == "":
            str_0 = "0"
        if str_1 == "":
            str_1 = "1"
        if str_2 == "":
            str_2 = "2"
        if str_3 == "":
            str_3 = "3"
        if str_4 == "":
            str_4 = "4"
        if str_5 == "":
            str_5 = "5"
        if str_6 == "":
            str_6 = "6"
        if str_7 == "":
            str_7 = "7"
        if str_8 == "":
            str_8 = "8"
        if str_9 == "":
            str_9 = "9"
        if str_10 == "":
            str_10 = "10"
        if str_11 == "":
            str_11 = "11"
        if str_12 == "":
            str_12 = "12"
        if str_13 == "":
            str_13 = "13"
        if str_14 == "":
            str_14 = "14"
        if str_15 == "":
            str_15 = "15"
        
            
    
        column_names = [str_0, str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8, str_9, str_10, str_11, str_12, str_13, str_14, str_15]
        df = pd.DataFrame(columns=column_names)
        return df

def dab_single_case_tests(data_df, parameter_df, column_df):

    data_df = data_df.copy(deep=True)
    parameter_df = parameter_df.copy(deep=True)
    column_df = column_df.copy(deep=True)
    
    dab_ipo_parameter_sku_id_column_name 		= column_df.at[0, 'dab_ipo_parameter_sku_id_column_name']
    dab_ipo_parameter_cac_qty_column_name 	    = column_df.at[0, 'dab_ipo_parameter_cac_qty_column_name']
    dab_ipo_parameter_inner_length_column_name 	= column_df.at[0, 'dab_ipo_parameter_inner_length_column_name']
    dab_ipo_parameter_inner_width_column_name 	= column_df.at[0, 'dab_ipo_parameter_inner_width_column_name']
    dab_ipo_parameter_inner_height_column_name 	= column_df.at[0, 'dab_ipo_parameter_inner_height_column_name']
    dab_ipo_parameter_inner_weight_column_name 	= column_df.at[0, 'dab_ipo_parameter_inner_weight_column_name']
    
    
    
    my_parameters = {}
    for col in parameter_df.columns:
        my_parameters[col] = parameter_df[col].values[0]
    
    output_df = pd.DataFrame()
    output_df['sct_output_sku_id'] = None
    output_df['sct_output_cac_qty'] = None
    
    output_df['sct_tests_passed'] = None
    
    output_df['sct_density (kg/m^3)'] = None
    output_df['sct_weight_pressure (N/m^2)'] = None
    output_df['sct_height_to_width'] = None
    output_df['sct_length_to_width'] = None
    
    output_df['sct_flag_min_length'] = None
    output_df['sct_flag_max_length'] = None
    
    output_df['sct_flag_min_width'] = None
    output_df['sct_flag_max_width'] = None
    
    output_df['sct_flag_min_height'] = None
    output_df['sct_flag_max_height'] = None
    
    output_df['sct_flag_min_weight'] = None
    output_df['sct_flag_max_weight'] = None
    
    output_df['sct_flag_min_density'] = None
    output_df['sct_flag_max_density'] = None
    
    output_df['sct_flag_min_weight_pressure'] = None
    output_df['sct_flag_max_weight_pressure'] = None
    
    output_df['sct_flag_min_height_to_width'] = None
    output_df['sct_flag_max_height_to_width'] = None
    
    output_df['sct_flag_min_length_to_width'] = None
    output_df['sct_flag_max_length_to_width'] = None
    
    
    
    for index, row in data_df.iterrows():
        
        
        my_parameters2 = copy.deepcopy(my_parameters)
        
        
       
        my_parameters2["dab_ipo_parameter_sku_id"] 					= data_df.at[index, dab_ipo_parameter_sku_id_column_name]
        
        my_parameters2["dab_ipo_parameter_inner_length"] 			= data_df.at[index, dab_ipo_parameter_inner_length_column_name]
        my_parameters2["dab_ipo_parameter_inner_width"] 			= data_df.at[index, dab_ipo_parameter_inner_width_column_name]
        my_parameters2["dab_ipo_parameter_inner_height"] 			= data_df.at[index, dab_ipo_parameter_inner_height_column_name]
        my_parameters2["dab_ipo_parameter_inner_weight"] 			= data_df.at[index, dab_ipo_parameter_inner_weight_column_name]
        
        
        output_df.at[index, 'sct_output_sku_id'] = my_parameters2["dab_ipo_parameter_sku_id"]
        output_df.at[index, 'sct_output_cac_qty'] = data_df.at[index, dab_ipo_parameter_cac_qty_column_name]
        
        test_result = 1
        
        if my_parameters2["dab_ipo_parameter_inner_length"] < my_parameters2["dab_sct_parameter_min_length"]:
            test_result = 0
            output_df.at[index, 'sct_flag_min_length'] = 1
        if my_parameters2["dab_ipo_parameter_inner_length"] > my_parameters2["dab_sct_parameter_max_length"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_length'] = 1
            
        if my_parameters2["dab_ipo_parameter_inner_width"] < my_parameters2["dab_sct_parameter_min_width"]:
            test_result = 0
            output_df.at[index, 'sct_flag_min_width'] = 1
        if my_parameters2["dab_ipo_parameter_inner_width"] > my_parameters2["dab_sct_parameter_max_width"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_width'] = 1
        
        if my_parameters2["dab_ipo_parameter_inner_height"] < my_parameters2["dab_sct_parameter_min_height"]:
            test_result = 0
            output_df.at[index, 'sct_flag_min_height'] = 1
        if my_parameters2["dab_ipo_parameter_inner_height"] > my_parameters2["dab_sct_parameter_max_height"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_height'] = 1
        
        if my_parameters2["dab_ipo_parameter_inner_weight"] < my_parameters2["dab_sct_parameter_min_weight"]:
            test_result = 0
            output_df.at[index, 'sct_flag_min_weight'] = 1
        if my_parameters2["dab_ipo_parameter_inner_weight"] > my_parameters2["dab_sct_parameter_max_weight"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_weight'] = 1
            
        
        
        g = 9.807 # m/s^2
        
        density = (my_parameters2["dab_ipo_parameter_inner_weight"]) / (my_parameters2["dab_ipo_parameter_inner_length"] * my_parameters2["dab_ipo_parameter_inner_width"] * my_parameters2["dab_ipo_parameter_inner_height"])
        weight_pressure = (my_parameters2["dab_ipo_parameter_inner_weight"] * g) / (my_parameters2["dab_ipo_parameter_inner_length"] * my_parameters2["dab_ipo_parameter_inner_width"])
        height_to_width = my_parameters2["dab_ipo_parameter_inner_height"] / my_parameters2["dab_ipo_parameter_inner_width"]
        length_to_width	= my_parameters2["dab_ipo_parameter_inner_length"] / my_parameters2["dab_ipo_parameter_inner_width"]
        
        
        
        output_df.at[index, 'sct_density (kg/m^3)'] = density
        output_df.at[index, 'sct_weight_pressure (N/m^2)'] = weight_pressure
        output_df.at[index, 'sct_height_to_width'] = height_to_width
        output_df.at[index, 'sct_length_to_width'] = length_to_width
        
        
        if density < my_parameters2["dab_sct_parameter_min_density"]:
            test_result = 0
            output_df.at[index, 'sct_flag_min_density'] = 1
            
        if density > my_parameters2["dab_sct_parameter_max_density"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_density'] = 1
            
            
        if weight_pressure < my_parameters2["dab_sct_parameter_min_weight_pressure"]:
            test_result = 0
            output_df.at[index, 'sct_flag_min_weight_pressure'] = 1
            
        if weight_pressure > my_parameters2["dab_sct_parameter_max_weight_pressure"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_weight_pressure'] = 1
            
            
        if height_to_width < my_parameters2["dab_sct_parameter_min_height_to_width"]:
            test_result = 0
            output_df.at[index, 'sct_flag_min_height_to_width'] = 1
            
        if height_to_width > my_parameters2["dab_sct_parameter_max_height_to_width"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_height_to_width'] = 1

            
        if length_to_width < my_parameters2["dab_sct_parameter_min_length_to_width"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_length_to_width'] = 1
            
        if length_to_width > my_parameters2["dab_sct_parameter_max_length_to_width"]:
            test_result = 0
            output_df.at[index, 'sct_flag_max_length_to_width'] = 1
            
            
        output_df.at[index, 'sct_tests_passed'] = test_result
    
    
    
    output_df.fillna(0, inplace=True)
    statistics_df = add_row_to_df("", "-", 																																	"SKU", 																	"SKU %", 																													"Quantity",  																												"Quantity %")
    statistics_df = add_row_to_df(statistics_df, "Total Rows", 																												len(output_df), 														format_float_with_commas((len(output_df)/len(output_df))*100, 2) + "%", 													format_float_with_commas(output_df["sct_output_cac_qty"].sum()), 															format_float_with_commas((1)*100, 2) + "%") 

    statistics_df = add_row_to_df(statistics_df, "Test passed", 																											output_df["sct_tests_passed"].sum(), 									format_float_with_commas(((output_df["sct_tests_passed"] == 1).sum()/len(output_df))*100, 2) + "%",							format_float_with_commas(output_df.loc[output_df["sct_tests_passed"] == 1, "sct_output_cac_qty"].sum()), 					format_float_with_commas((     output_df.loc[output_df["sct_tests_passed"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "Test failed", 																											(output_df["sct_tests_passed"] == 0).sum(), 							format_float_with_commas(((output_df["sct_tests_passed"] == 0).sum()/len(output_df))*100, 2) + "%", 						format_float_with_commas(output_df.loc[output_df["sct_tests_passed"] == 0, "sct_output_cac_qty"].sum()), 					format_float_with_commas((     output_df.loc[output_df["sct_tests_passed"] == 0, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Length < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_length"],3) + " m", 							output_df["sct_flag_min_length"].sum(), 				format_float_with_commas(((output_df["sct_flag_min_length"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_min_length"] == 1, "sct_output_cac_qty"].sum()), 				format_float_with_commas((     output_df.loc[output_df["sct_flag_min_length"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "Length > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_length"],3) + " m", 							output_df["sct_flag_max_length"].sum(), 				format_float_with_commas(((output_df["sct_flag_max_length"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_max_length"] == 1, "sct_output_cac_qty"].sum()), 				format_float_with_commas((     output_df.loc[output_df["sct_flag_max_length"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")

    statistics_df = add_row_to_df(statistics_df, "Width < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_width"],3) + " m", 								output_df["sct_flag_min_width"].sum(), 					format_float_with_commas(((output_df["sct_flag_min_width"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_min_width"] == 1, "sct_output_cac_qty"].sum()), 					format_float_with_commas((     output_df.loc[output_df["sct_flag_min_width"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "Width > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_width"],3) + " m", 								output_df["sct_flag_max_width"].sum(), 					format_float_with_commas(((output_df["sct_flag_max_width"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_max_width"] == 1, "sct_output_cac_qty"].sum()), 					format_float_with_commas((     output_df.loc[output_df["sct_flag_max_width"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")

    statistics_df = add_row_to_df(statistics_df, "Height < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_height"],3) + " m", 							output_df["sct_flag_min_height"].sum(), 				format_float_with_commas(((output_df["sct_flag_min_height"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_min_height"] == 1, "sct_output_cac_qty"].sum()), 				format_float_with_commas((     output_df.loc[output_df["sct_flag_min_height"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "Height > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_height"],3) + " m", 							output_df["sct_flag_max_height"].sum(), 				format_float_with_commas(((output_df["sct_flag_max_height"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_max_height"] == 1, "sct_output_cac_qty"].sum()), 				format_float_with_commas((     output_df.loc[output_df["sct_flag_max_height"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")

    statistics_df = add_row_to_df(statistics_df, "Weight < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_weight"],3) + " kg", 							output_df["sct_flag_min_weight"].sum(), 				format_float_with_commas(((output_df["sct_flag_min_weight"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_min_weight"] == 1, "sct_output_cac_qty"].sum()), 				format_float_with_commas((     output_df.loc[output_df["sct_flag_min_weight"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "Weight > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_weight"],3) + " kg", 							output_df["sct_flag_max_weight"].sum(), 				format_float_with_commas(((output_df["sct_flag_max_weight"] == 1).sum()/len(output_df))*100, 2) + "%",						format_float_with_commas(output_df.loc[output_df["sct_flag_max_weight"] == 1, "sct_output_cac_qty"].sum()), 				format_float_with_commas((     output_df.loc[output_df["sct_flag_max_weight"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")

    
    statistics_df = add_row_to_df(statistics_df, "Density < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_density"],1) + " N/m^2", 		output_df["sct_flag_min_density"].sum(), 		format_float_with_commas(((output_df["sct_flag_min_density"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_min_density"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_min_density"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "Density > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_density"],1) + " N/m^2", 		output_df["sct_flag_max_density"].sum(), 		format_float_with_commas(((output_df["sct_flag_max_density"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_max_density"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_max_density"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    
    statistics_df = add_row_to_df(statistics_df, "Weight Pressure < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_weight_pressure"],1) + " N/m^2", 		output_df["sct_flag_min_weight_pressure"].sum(), 		format_float_with_commas(((output_df["sct_flag_min_weight_pressure"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_min_weight_pressure"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_min_weight_pressure"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "Weight Pressure > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_weight_pressure"],1) + " N/m^2", 		output_df["sct_flag_max_weight_pressure"].sum(), 		format_float_with_commas(((output_df["sct_flag_max_weight_pressure"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_max_weight_pressure"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_max_weight_pressure"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    
    statistics_df = add_row_to_df(statistics_df, "H/W ratio < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_height_to_width"],2), 						output_df["sct_flag_min_height_to_width"].sum(), 		format_float_with_commas(((output_df["sct_flag_min_height_to_width"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_min_height_to_width"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_min_height_to_width"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "H/W ratio > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_height_to_width"],2), 						output_df["sct_flag_max_height_to_width"].sum(), 		format_float_with_commas(((output_df["sct_flag_max_height_to_width"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_max_height_to_width"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_max_height_to_width"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    
    statistics_df = add_row_to_df(statistics_df, "L/W ratio < " + format_float_with_commas(my_parameters["dab_sct_parameter_min_length_to_width"],2), 						output_df["sct_flag_min_length_to_width"].sum(), 		format_float_with_commas(((output_df["sct_flag_min_length_to_width"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_min_length_to_width"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_min_length_to_width"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    statistics_df = add_row_to_df(statistics_df, "L/W ratio > " + format_float_with_commas(my_parameters["dab_sct_parameter_max_length_to_width"],2), 						output_df["sct_flag_max_length_to_width"].sum(), 		format_float_with_commas(((output_df["sct_flag_max_length_to_width"] == 1).sum()/len(output_df))*100, 2) + "%",				format_float_with_commas(output_df.loc[output_df["sct_flag_max_length_to_width"] == 1, "sct_output_cac_qty"].sum()), 		format_float_with_commas((     output_df.loc[output_df["sct_flag_max_length_to_width"] == 1, "sct_output_cac_qty"].sum()      / output_df["sct_output_cac_qty"].sum())*100, 2) + "%")
    
    
    statistics_df = statistics_df.loc[:, (statistics_df != "").any()]
    
    
    return output_df, statistics_df

data_df = input_1.to_pandas()
parameter_df = input_2.to_pandas()


data_df = data_df.reset_index(drop=True)
parameter_df = parameter_df.reset_index(drop=True)



column_df = pd.DataFrame()
column_df.at[0, 'dab_ipo_parameter_sku_id_column_name']                 = self.column_param_sku_id
column_df.at[0, 'dab_ipo_parameter_cac_qty_column_name']                = self.column_param_quantity
column_df.at[0, 'dab_ipo_parameter_inner_length_column_name']           = self.column_param_length
column_df.at[0, 'dab_ipo_parameter_inner_width_column_name']            = self.column_param_width
column_df.at[0, 'dab_ipo_parameter_inner_height_column_name']           = self.column_param_height
column_df.at[0, 'dab_ipo_parameter_inner_weight_column_name']           = self.column_param_weight

parameter_df.at[0, 'dab_sct_name'] = "dab_case_automation_test (1 means passed)"





sct_value_df, sct_statistics_df = dab_single_case_tests(data_df, parameter_df, column_df)


joint_value_df = sct_value_df


output_df = data_df.copy(deep=True)

sku_col_name_df_1 = column_df.at[0, 'dab_ipo_parameter_sku_id_column_name']
sku_col_name_df_2 = "sct_output_sku_id"

joint_value_df = joint_value_df.rename(columns={"sct_tests_passed": parameter_df.at[0, 'dab_sct_name'] + ""})
output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, parameter_df.at[0, 'dab_sct_name'] + "")

if self.selection_output_flags == "Yes":

    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_weight_pressure (N/m^2)")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_height_to_width")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_length_to_width")

    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_length")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_length")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_width")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_width")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_height")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_height")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_weight")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_weight")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_density")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_density")

    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_weight_pressure")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_weight_pressure")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_height_to_width")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_height_to_width")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_min_length_to_width")
    output_df, assigned_column_name = fx_join_single_column(output_df, joint_value_df, sku_col_name_df_1, sku_col_name_df_2, "sct_flag_max_length_to_width")
    
return output_df, sct_statistics_df
