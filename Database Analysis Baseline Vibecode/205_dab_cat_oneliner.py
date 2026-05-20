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



        
data_df = input_1.to_pandas()


data_df = data_df.reset_index(drop=True)




config_coumn_name = self.column_one_zero_test
cases_as_cases_name = self.column_cases_as_cases
cases_per_tray_name = self.column_cases_per_tray
tray_size_name = self.column_tray_size




data_df_2 = data_df.copy(deep=True)
tray_equivalents_name = "dab_bs_name_noone_will_ever_use_tray_equivalents"

data_df_2[tray_equivalents_name] = None

total_sku_that_passed = 0
total_cases_that_passed = 0
total_tray_equivalents = 0.0

for index, row in data_df_2.iterrows():
    if data_df_2.at[index, config_coumn_name] > 0 and data_df_2.at[index, cases_per_tray_name] > 0:
        data_df_2.at[index, tray_equivalents_name] = data_df_2.at[index, cases_as_cases_name] / data_df_2.at[index, cases_per_tray_name]
        total_sku_that_passed 		= total_sku_that_passed + 1
        total_cases_that_passed 	= total_cases_that_passed + data_df_2.at[index, cases_as_cases_name]
        if data_df_2.at[index, tray_size_name] == "Large":
            total_tray_equivalents 		= total_tray_equivalents + data_df_2.at[index, tray_equivalents_name]
        else:
            if data_df_2.at[index, tray_size_name] == "Small":
                total_tray_equivalents 		= total_tray_equivalents + data_df_2.at[index, tray_equivalents_name]/2
    else:
        data_df_2.at[index, tray_equivalents_name] = 0


oneliner_df = add_row_to_df("", 					"Configuration", 		        "Passed Rows", 											"Total Rows", 										"%", 																				 		"Passed Cases As Cases",								"Total Cases As Cases", 													"%_", 																											"Large Tray equivalents", 								"Weighted AVG Cases Per Tray/Tote")
oneliner_df = add_row_to_df(oneliner_df, 			self.param_config_name, 		format_float_with_commas(total_sku_that_passed),		format_float_with_commas(len(data_df_2)), 	 		format_float_with_commas( (total_sku_that_passed / len(data_df_2))*100,2 ) + " %",	 		format_float_with_commas(total_cases_that_passed),		format_float_with_commas(data_df_2[cases_as_cases_name].sum()), 			format_float_with_commas( (total_cases_that_passed / data_df_2[cases_as_cases_name].sum())*100,2 ) + " %", 		format_float_with_commas(total_tray_equivalents), 		format_float_with_commas(total_cases_that_passed / total_tray_equivalents,4))
oneliner_df = oneliner_df.loc[:, (oneliner_df != "").any()]





return oneliner_df



