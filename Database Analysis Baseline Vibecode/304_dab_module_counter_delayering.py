import pandas as pd
from category import system_sizing_category

import numpy as np
import json
import math
import copy
import ast




# Copyright (c) 2026 fromdablockjenny9-oss @Github
# This project and its source code are the property of fromdablockjenny9-oss @Github
# Unauthorized copying, modification, or distribution is prohibited
# fromdablockjenny9@gmail.com

def ensure_multiple(num_1, num_2):
    if num_1 % num_2 == 0:
        return num_1
    else:
        return math.ceil(num_1 / num_2) * num_2
def is_multiple(number_1, number_2):
    if number_2 == 0:
        return "Error: Division by zero"
    return 1 if number_1 % number_2 == 0 else 0
def format_float_with_commas(number, decimal_places=0):
    floored_number = round(number, decimal_places)
    formatted_number = f"{floored_number:,.{decimal_places}f}"
    
    return formatted_number

df = input_1.to_pandas()
df = df.reset_index(drop=True)

total_surged_hourly_trays_generated							= df['surged_hourly_trays_generated'].sum()
total_surged_hourly_cases_in_trays_generated				= df['surged_hourly_cases_in_trays_generated'].sum()
total_surged_hourly_pallet_consumption						= df['surged_hourly_pallet_consumption'].sum()
total_surged_hourly_pallet_retrievals						= df['surged_hourly_pallet_retrievals'].sum()
total_surged_hourly_pallet_residuals						= df['surged_hourly_pallet_residuals'].sum()
total_surged_hourly_layer_consumption						= df['surged_hourly_layer_consumption'].sum()

module_name 			= self.module_name
report_group 			= self.report_group
expected_flows			= self.expected_flows


unique_flow_values = df['flow_name'].unique()

bottleneck_1_string 	= self.bottleneck_1_string
bottleneck_2_string 	= self.bottleneck_2_string
bottleneck_3_string 	= self.bottleneck_3_string
bottleneck_4_string 	= self.bottleneck_4_string
bottleneck_5_string 	= self.bottleneck_5_string
bottleneck_6_string 	= self.bottleneck_6_string
bottleneck_7_string 	= self.bottleneck_7_string
bottleneck_8_string 	= self.bottleneck_8_string
bottleneck_9_string 	= self.bottleneck_9_string
bottleneck_10_string 	= self.bottleneck_10_string

bottlenecks_array = []

bottlenecks_array.append(ast.literal_eval(bottleneck_1_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_2_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_3_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_4_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_5_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_6_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_7_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_8_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_9_string))
bottlenecks_array.append(ast.literal_eval(bottleneck_10_string))

df_out = pd.DataFrame()

df_out["0"] = ""
df_out["report_group"] = ""
df_out["input_or_output"] = ""
df_out["marker"] = ""

df_out["heading"] = ""
df_out["value"] = ""

i = -1
i = i+1
df_out.at[i, "0"] 					= "-----------------------"
df_out.at[i, "report_group"] 		= "-----------------------"
df_out.at[i, 'input_or_output'] 	= "-----------------------"
df_out.at[i, 'marker'] 				= "-----------------------"
df_out.at[i, 'heading'] 			= "-----------------------"
df_out.at[i, 'value'] 				= "-----------------------"

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= report_group
df_out.at[i, 'input_or_output'] 	= "input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "module_name"
df_out.at[i, 'value'] 				= module_name

for value in unique_flow_values:
    count = len(df.loc[df['flow_name'] == value])
    
    if value in expected_flows:
        i = i+1
        df_out.at[i, "0"] 					= ""
        df_out.at[i, "report_group"] 		= report_group
        df_out.at[i, 'input_or_output'] 	= "input"
        df_out.at[i, 'marker'] 				= "----->"
        df_out.at[i, 'heading'] 			= "flow_name"
        df_out.at[i, 'value'] 				= str(value) + "; count: " + str(count)
        
        
    else:
        i = i+1
        df_out.at[i, "0"] 					= ""
        df_out.at[i, "report_group"] 		= report_group
        df_out.at[i, 'input_or_output'] 	= "input"
        df_out.at[i, 'marker'] 				= "!!!!!!!!!!!!!!!!!!!!! Check Flow Name!"
        df_out.at[i, 'heading'] 			= "flow_name"
        df_out.at[i, 'value'] 				= str(value) + "; count: " + str(count)
        
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= report_group
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "-----------------------"
df_out.at[i, 'value'] 				= "-----------------------"

minimum_X_needed = []
df_copy = df.copy(deep=True)


j = -1
for item in bottlenecks_array:
    my_name 								= item[0]
    my_utilisation 							= item[1]
    seconds_per_pallet_retrieval 			= item[2]
    seconds_per_pallet_consumption 			= item[3]
    seconds_per_pallet_residuals 			= item[4]
    seconds_per_layer_consumption 			= item[5]
    seconds_per_case_generated 				= item[6]
    seconds_per_trays_or_totes_generated 	= item[7]
    
    total_seconds_per_pallet_retrieval 				= seconds_per_pallet_retrieval					* total_surged_hourly_pallet_retrievals
    total_seconds_per_pallet_consumption 			= seconds_per_pallet_consumption				* total_surged_hourly_pallet_consumption
    total_seconds_per_pallet_residuals 				= seconds_per_pallet_residuals					* total_surged_hourly_pallet_residuals
    total_seconds_per_layer_consumption 			= seconds_per_layer_consumption					* total_surged_hourly_layer_consumption
    total_seconds_per_case_generated 				= seconds_per_case_generated					* total_surged_hourly_cases_in_trays_generated
    total_seconds_per_trays_or_totes_generated 		= seconds_per_trays_or_totes_generated			* total_surged_hourly_trays_generated
    
    total_time = total_seconds_per_pallet_retrieval + total_seconds_per_pallet_consumption + total_seconds_per_pallet_residuals + total_seconds_per_layer_consumption + total_seconds_per_case_generated + total_seconds_per_trays_or_totes_generated
    
    if total_time > 0 and my_utilisation > 0:
        j = j + 1
        minimum_X_needed.append((total_time/my_utilisation) / 3600)
        
        i = i+1
        df_out.at[i, "0"] 					= ""
        df_out.at[i, "report_group"] 		= report_group
        df_out.at[i, 'input_or_output'] 	= "output"
        df_out.at[i, 'marker'] 				= ""
        df_out.at[i, 'heading'] 			= "Bottleneck"
        df_out.at[i, 'value'] 				= my_name
        
        i = i+1
        df_out.at[i, "0"] 					= ""
        df_out.at[i, "report_group"] 		= report_group
        df_out.at[i, 'input_or_output'] 	= "output"
        df_out.at[i, 'marker'] 				= ""
        df_out.at[i, 'heading'] 			= "minimum needed"
        df_out.at[i, 'value'] 				= str(format_float_with_commas(minimum_X_needed[j],2))
        
        i = i+1
        df_out.at[i, "0"] 					= ""
        df_out.at[i, "report_group"] 		= report_group
        df_out.at[i, 'input_or_output'] 	= ""
        df_out.at[i, 'marker'] 				= ""
        df_out.at[i, 'heading'] 			= ""
        df_out.at[i, 'value'] 				= ""


if len(minimum_X_needed) == 0:
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= "!!!!!!!"
    df_out.at[i, 'heading'] 			= "ZERO VALUES"
    df_out.at[i, 'value'] 				= "CHECK FLOW AND SETUP"
else:
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= "----->"
    df_out.at[i, 'heading'] 			= module_name + " Modules Needed"
    df_out.at[i, 'value'] 				= str(format_float_with_commas((max(minimum_X_needed)),2))
    
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= ""
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= ""
    df_out.at[i, 'value'] 				= ""
    
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= "Flows Per Module:"
    df_out.at[i, 'value'] 				= ""
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= "surged_hourly_pallet_retrievals"
    df_out.at[i, 'value'] 				= str(format_float_with_commas((total_surged_hourly_pallet_retrievals / max(minimum_X_needed)),2))
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= "surged_hourly_pallet_consumption"
    df_out.at[i, 'value'] 				= str(format_float_with_commas((total_surged_hourly_pallet_consumption / max(minimum_X_needed)),2))
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= "surged_hourly_pallet_residuals"
    df_out.at[i, 'value'] 				= str(format_float_with_commas((total_surged_hourly_pallet_residuals / max(minimum_X_needed)),2))
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= "surged_hourly_layer_consumption"
    df_out.at[i, 'value'] 				= str(format_float_with_commas((total_surged_hourly_layer_consumption / max(minimum_X_needed)),2))
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= "surged_hourly_cases_in_trays_generated"
    df_out.at[i, 'value'] 				= str(format_float_with_commas((total_surged_hourly_cases_in_trays_generated / max(minimum_X_needed)),2))
    i = i+1
    df_out.at[i, "0"] 					= ""
    df_out.at[i, "report_group"] 		= report_group
    df_out.at[i, 'input_or_output'] 	= "output"
    df_out.at[i, 'marker'] 				= ""
    df_out.at[i, 'heading'] 			= "surged_hourly_trays_generated"
    df_out.at[i, 'value'] 				= str(format_float_with_commas((total_surged_hourly_trays_generated / max(minimum_X_needed)),2))
    
return df_out

