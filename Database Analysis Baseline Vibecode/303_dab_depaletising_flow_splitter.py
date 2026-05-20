import pandas as pd
from category import system_sizing_category

import numpy as np
import json
import math
import copy




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
my_variables_df = input_2.to_pandas()

df = df.reset_index(drop=True)
my_variables_df = my_variables_df.reset_index(drop=True)


sku_id_column_name								= self.sku_id_column
ti_column_name 									= self.ti_column_name
cpp_column_name 								= self.cpp_column_name
case_qty_column_name	 						= self.case_qty_column_name
cases_per_tray_column_name 						= self.inners_per_outer_column_name
pallet_consumption_method_column_name 			= self.pallet_consumption_method_column
replenishment_case_qty_column_name 				= self.single_replen_case_qty_column_name
incomplete_layer_handling						= self.incomplete_layer_handling
manual_stations_only							= self.manual_stations_only

delayering_operation_hours						= my_variables_df.at[0, 'delayering_operation_hours']
delayering_surge_factor							= my_variables_df.at[0, 'delayering_surge_factor']

columns_to_copy = []
columns_to_copy.append(sku_id_column_name)
columns_to_copy.append(ti_column_name)
columns_to_copy.append(cpp_column_name)
columns_to_copy.append(case_qty_column_name)
columns_to_copy.append(cases_per_tray_column_name)
columns_to_copy.append(pallet_consumption_method_column_name)
columns_to_copy.append(replenishment_case_qty_column_name)

new_df = df[columns_to_copy].copy()

original_name = sku_id_column_name
new_name = "dab_delayering_input_sku_id"
new_df.rename(columns={original_name: new_name}, inplace=True)
sku_id_column_name = new_name

original_name = ti_column_name
new_name = "dab_delayering_input_ti"
new_df.rename(columns={original_name: new_name}, inplace=True)
ti_column_name = new_name

original_name = cpp_column_name
new_name = "dab_delayering_input_cpp"
new_df.rename(columns={original_name: new_name}, inplace=True)
cpp_column_name = new_name

original_name = case_qty_column_name
new_name = "dab_delayering_input_case_qty"
new_df.rename(columns={original_name: new_name}, inplace=True)
case_qty_column_name = new_name

original_name = cases_per_tray_column_name
new_name = "dab_delayering_input_cases_per_tray"
new_df.rename(columns={original_name: new_name}, inplace=True)
cases_per_tray_column_name = new_name

original_name = pallet_consumption_method_column_name
new_name = "dab_delayering_input_consumption_method"
new_df.rename(columns={original_name: new_name}, inplace=True)
pallet_consumption_method_column_name = new_name

original_name = replenishment_case_qty_column_name
new_name = "dab_delayering_input_repenishment_case_qty"
new_df.rename(columns={original_name: new_name}, inplace=True)
replenishment_case_qty_column_name = new_name


df_copy = new_df

df_copy['dab_delayering_out_complete_layer_hi'] 					= 0
df_copy['dab_delayering_out_excess_cases'] 							= 0

df_copy['auto_station_single_replen_trays_generated']				= 0.0
df_copy['auto_station_single_replen_cases_in_trays']				= 0.0

df_copy['auto_station_single_replen_pallet_consumption']			= 0.0
df_copy['auto_station_single_replen_pallet_retrievals']				= 0.0
df_copy['auto_station_single_replen_pallet_residuals']				= 0.0
df_copy['auto_station_single_replen_layer_consumption']				= 0.0

df_copy['auto_station_replenishments_per_day']						= 0.0

df_copy['auto_station_daily_trays_generated']						= 0.0
df_copy['auto_station_daily_cases_in_trays_generated']				= 0.0
df_copy['auto_station_daily_pallet_consumption']					= 0.0
df_copy['auto_station_daily_pallet_retrievals']						= 0.0
df_copy['auto_station_daily_pallet_residuals']						= 0.0
df_copy['auto_station_daily_layer_consumption']						= 0.0

df_copy['surged_auto_station_daily_trays_generated'] 				= 0.0
df_copy['surged_auto_station_daily_cases_in_trays_generated'] 		= 0.0
df_copy['surged_auto_station_daily_pallet_consumption'] 			= 0.0
df_copy['surged_auto_station_daily_pallet_retrievals'] 				= 0.0
df_copy['surged_auto_station_daily_pallet_residuals'] 				= 0.0
df_copy['surged_auto_station_daily_layer_consumption'] 				= 0.0

df_copy['surged_auto_station_hourly_trays_generated'] 				= 0.0
df_copy['surged_auto_station_hourly_cases_in_trays_generated'] 		= 0.0
df_copy['surged_auto_station_hourly_pallet_consumption'] 			= 0.0
df_copy['surged_auto_station_hourly_pallet_retrievals'] 			= 0.0
df_copy['surged_auto_station_hourly_pallet_residuals'] 				= 0.0
df_copy['surged_auto_station_hourly_layer_consumption'] 			= 0.0


df_copy['top_layer_removal_single_replen_trays_generated']			= 0.0
df_copy['top_layer_removal_single_replen_cases_in_trays']			= 0.0

df_copy['top_layer_removal_single_replen_pallet_consumption']		= 0.0
df_copy['top_layer_removal_single_replen_pallet_retrievals']		= 0.0
df_copy['top_layer_removal_single_replen_pallet_residuals']			= 0.0
df_copy['top_layer_removal_single_replen_layer_consumption']		= 0.0

df_copy['top_layer_removal_replenishments_per_day']					= 0.0

df_copy['top_layer_removal_daily_trays_generated']					= 0.0
df_copy['top_layer_removal_daily_cases_in_trays_generated']			= 0.0
df_copy['top_layer_removal_daily_pallet_consumption']				= 0.0
df_copy['top_layer_removal_daily_pallet_retrievals']				= 0.0
df_copy['top_layer_removal_daily_pallet_residuals']					= 0.0
df_copy['top_layer_removal_daily_layer_consumption']				= 0.0

df_copy['surged_top_layer_removal_daily_trays_generated'] 					= 0.0
df_copy['surged_top_layer_removal_daily_cases_in_trays_generated'] 			= 0.0
df_copy['surged_top_layer_removal_daily_pallet_consumption'] 				= 0.0
df_copy['surged_top_layer_removal_daily_pallet_retrievals'] 				= 0.0
df_copy['surged_top_layer_removal_daily_pallet_residuals'] 					= 0.0
df_copy['surged_top_layer_removal_daily_layer_consumption'] 				= 0.0

df_copy['surged_top_layer_removal_hourly_trays_generated'] 					= 0.0
df_copy['surged_top_layer_removal_hourly_cases_in_trays_generated'] 		= 0.0
df_copy['surged_top_layer_removal_hourly_pallet_consumption'] 				= 0.0
df_copy['surged_top_layer_removal_hourly_pallet_retrievals'] 				= 0.0
df_copy['surged_top_layer_removal_hourly_pallet_residuals'] 				= 0.0
df_copy['surged_top_layer_removal_hourly_layer_consumption'] 				= 0.0

df_copy['manual_station_single_replen_trays_generated'] 			= 0.0
df_copy['manual_station_single_replen_cases_in_trays'] 				= 0.0

df_copy['manual_station_single_replen_pallet_consumption'] 			= 0.0
df_copy['manual_station_single_replen_pallet_retrievals'] 			= 0.0
df_copy['manual_station_single_replen_pallet_residuals'] 			= 0.0
df_copy['manual_station_single_replen_layer_consumption'] 			= 0.0

df_copy['manual_station_replenishments_per_day'] 					= 0.0

df_copy['manual_station_daily_trays_generated'] 					= 0.0
df_copy['manual_station_daily_cases_in_trays_generated'] 			= 0.0
df_copy['manual_station_daily_pallet_consumption'] 					= 0.0
df_copy['manual_station_daily_pallet_retrievals'] 					= 0.0
df_copy['manual_station_daily_pallet_residuals'] 					= 0.0
df_copy['manual_station_daily_layer_consumption'] 					= 0.0

df_copy['surged_manual_station_daily_trays_generated'] 				= 0.0
df_copy['surged_manual_station_daily_cases_in_trays_generated'] 	= 0.0
df_copy['surged_manual_station_daily_pallet_consumption'] 			= 0.0
df_copy['surged_manual_station_daily_pallet_retrievals'] 			= 0.0
df_copy['surged_manual_station_daily_pallet_residuals'] 			= 0.0
df_copy['surged_manual_station_daily_layer_consumption'] 			= 0.0

df_copy['surged_manual_station_hourly_trays_generated'] 			= 0.0
df_copy['surged_manual_station_hourly_cases_in_trays_generated'] 	= 0.0
df_copy['surged_manual_station_hourly_pallet_consumption'] 			= 0.0
df_copy['surged_manual_station_hourly_pallet_retrievals'] 			= 0.0
df_copy['surged_manual_station_hourly_pallet_residuals'] 			= 0.0
df_copy['surged_manual_station_hourly_layer_consumption'] 			= 0.0


for index, row in df_copy.iterrows():

    ti_column_value 												= row[ti_column_name]
    cpp_column_value 												= row[cpp_column_name]
    case_qty_column_value 											= row[case_qty_column_name]
    cases_per_tray_column_value 									= row[cases_per_tray_column_name]
    pallet_consumption_method_column_value 							= row[pallet_consumption_method_column_name]
    replenishment_case_qty_column_value 							= row[replenishment_case_qty_column_name]

    df_copy.at[index, 'dab_delayering_out_complete_layer_hi'] 									= 0
    df_copy.at[index, 'dab_delayering_out_excess_cases'] 										= 0
    
    df_copy.at[index, 'auto_station_single_replen_trays_generated']			= 0.0
    df_copy.at[index, 'auto_station_single_replen_cases_in_trays']			= 0.0

    df_copy.at[index, 'auto_station_single_replen_pallet_consumption']		= 0.0
    df_copy.at[index, 'auto_station_single_replen_pallet_retrievals']		= 0.0
    df_copy.at[index, 'auto_station_single_replen_pallet_residuals']		= 0.0
    df_copy.at[index, 'auto_station_single_replen_layer_consumption']		= 0.0

    df_copy.at[index, 'auto_station_replenishments_per_day']				= 0.0

    df_copy.at[index, 'auto_station_daily_trays_generated']					= 0.0
    df_copy.at[index, 'auto_station_daily_cases_in_trays_generated']		= 0.0
    df_copy.at[index, 'auto_station_daily_pallet_consumption']				= 0.0
    df_copy.at[index, 'auto_station_daily_pallet_retrievals']				= 0.0
    df_copy.at[index, 'auto_station_daily_pallet_residuals']				= 0.0
    df_copy.at[index, 'auto_station_daily_layer_consumption']				= 0.0
    
    df_copy.at[index, 'surged_auto_station_daily_trays_generated'] 				= 0.0
    df_copy.at[index, 'surged_auto_station_daily_cases_in_trays_generated'] 	= 0.0
    df_copy.at[index, 'surged_auto_station_daily_pallet_consumption'] 			= 0.0
    df_copy.at[index, 'surged_auto_station_daily_pallet_retrievals'] 			= 0.0
    df_copy.at[index, 'surged_auto_station_daily_pallet_residuals'] 			= 0.0
    df_copy.at[index, 'surged_auto_station_daily_layer_consumption'] 			= 0.0

    df_copy.at[index, 'surged_auto_station_hourly_trays_generated'] 			= 0.0
    df_copy.at[index, 'surged_auto_station_hourly_cases_in_trays_generated'] 	= 0.0
    df_copy.at[index, 'surged_auto_station_hourly_pallet_consumption'] 			= 0.0
    df_copy.at[index, 'surged_auto_station_hourly_pallet_retrievals'] 			= 0.0
    df_copy.at[index, 'surged_auto_station_hourly_pallet_residuals'] 			= 0.0
    df_copy.at[index, 'surged_auto_station_hourly_layer_consumption'] 			= 0.0
    

    df_copy.at[index, 'top_layer_removal_single_replen_trays_generated']	= 0.0
    df_copy.at[index, 'top_layer_removal_single_replen_cases_in_trays']		= 0.0

    df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption']	= 0.0
    df_copy.at[index, 'top_layer_removal_single_replen_pallet_retrievals']	= 0.0
    df_copy.at[index, 'top_layer_removal_single_replen_pallet_residuals']	= 0.0
    df_copy.at[index, 'top_layer_removal_single_replen_layer_consumption']	= 0.0

    df_copy.at[index, 'top_layer_removal_replenishments_per_day']			= 0.0

    df_copy.at[index, 'top_layer_removal_daily_trays_generated']			= 0.0
    df_copy.at[index, 'top_layer_removal_daily_cases_in_trays_generated']	= 0.0
    df_copy.at[index, 'top_layer_removal_daily_pallet_consumption']			= 0.0
    df_copy.at[index, 'top_layer_removal_daily_pallet_retrievals']			= 0.0
    df_copy.at[index, 'top_layer_removal_daily_pallet_residuals']			= 0.0
    df_copy.at[index, 'top_layer_removal_daily_layer_consumption']			= 0.0
    
    df_copy.at[index, 'surged_top_layer_removal_daily_trays_generated'] 				= 0.0
    df_copy.at[index, 'surged_top_layer_removal_daily_cases_in_trays_generated'] 		= 0.0
    df_copy.at[index, 'surged_top_layer_removal_daily_pallet_consumption'] 				= 0.0
    df_copy.at[index, 'surged_top_layer_removal_daily_pallet_retrievals'] 				= 0.0
    df_copy.at[index, 'surged_top_layer_removal_daily_pallet_residuals'] 				= 0.0
    df_copy.at[index, 'surged_top_layer_removal_daily_layer_consumption'] 				= 0.0

    df_copy.at[index, 'surged_top_layer_removal_hourly_trays_generated'] 				= 0.0
    df_copy.at[index, 'surged_top_layer_removal_hourly_cases_in_trays_generated'] 		= 0.0
    df_copy.at[index, 'surged_top_layer_removal_hourly_pallet_consumption'] 			= 0.0
    df_copy.at[index, 'surged_top_layer_removal_hourly_pallet_retrievals'] 				= 0.0
    df_copy.at[index, 'surged_top_layer_removal_hourly_pallet_residuals'] 				= 0.0
    df_copy.at[index, 'surged_top_layer_removal_hourly_layer_consumption'] 				= 0.0

    df_copy.at[index, 'manual_station_single_replen_trays_generated'] 		= 0.0
    df_copy.at[index, 'manual_station_single_replen_cases_in_trays'] 		= 0.0

    df_copy.at[index, 'manual_station_single_replen_pallet_consumption'] 	= 0.0
    df_copy.at[index, 'manual_station_single_replen_pallet_retrievals'] 	= 0.0
    df_copy.at[index, 'manual_station_single_replen_pallet_residuals'] 		= 0.0
    df_copy.at[index, 'manual_station_single_replen_layer_consumption'] 	= 0.0

    df_copy.at[index, 'manual_station_replenishments_per_day'] 				= 0.0

    df_copy.at[index, 'manual_station_daily_trays_generated'] 				= 0.0
    df_copy.at[index, 'manual_station_daily_cases_in_trays_generated'] 		= 0.0
    df_copy.at[index, 'manual_station_daily_pallet_consumption'] 			= 0.0
    df_copy.at[index, 'manual_station_daily_pallet_retrievals'] 			= 0.0
    df_copy.at[index, 'manual_station_daily_pallet_residuals'] 				= 0.0
    df_copy.at[index, 'manual_station_daily_layer_consumption'] 			= 0.0
    
    df_copy.at[index, 'surged_manual_station_daily_trays_generated'] 				= 0.0
    df_copy.at[index, 'surged_manual_station_daily_cases_in_trays_generated'] 		= 0.0
    df_copy.at[index, 'surged_manual_station_daily_pallet_consumption'] 			= 0.0
    df_copy.at[index, 'surged_manual_station_daily_pallet_retrievals'] 				= 0.0
    df_copy.at[index, 'surged_manual_station_daily_pallet_residuals'] 				= 0.0
    df_copy.at[index, 'surged_manual_station_daily_layer_consumption'] 				= 0.0

    df_copy.at[index, 'surged_manual_station_hourly_trays_generated'] 				= 0.0
    df_copy.at[index, 'surged_manual_station_hourly_cases_in_trays_generated'] 		= 0.0
    df_copy.at[index, 'surged_manual_station_hourly_pallet_consumption'] 			= 0.0
    df_copy.at[index, 'surged_manual_station_hourly_pallet_retrievals'] 			= 0.0
    df_copy.at[index, 'surged_manual_station_hourly_pallet_residuals'] 				= 0.0
    df_copy.at[index, 'surged_manual_station_hourly_layer_consumption'] 			= 0.0
    
    df_copy.at[index, 'dab_delayering_out_complete_layer_hi'] 		= math.floor(cpp_column_value / ti_column_value)
    df_copy.at[index, 'dab_delayering_out_excess_cases'] 			= cpp_column_value - (ti_column_value * df_copy.at[index, 'dab_delayering_out_complete_layer_hi'])
    
    
    if manual_stations_only == "False" and (pallet_consumption_method_column_value == "in_layer_qty" or pallet_consumption_method_column_value == "in_pallet_qty") and incomplete_layer_handling == "be sent to top layer removal station, then to Auto":
        
        
        if df_copy.at[index, 'dab_delayering_out_complete_layer_hi'] != 0: 
            
            df_copy.at[index, 'auto_station_single_replen_trays_generated'] 			= math.ceil((replenishment_case_qty_column_value - df_copy.at[index, 'dab_delayering_out_excess_cases']) / cases_per_tray_column_value)
            df_copy.at[index, 'auto_station_single_replen_cases_in_trays']				= cases_per_tray_column_value * df_copy.at[index, 'auto_station_single_replen_trays_generated']
            
            df_copy.at[index, 'auto_station_single_replen_pallet_consumption'] 			= (replenishment_case_qty_column_value - df_copy.at[index, 'dab_delayering_out_excess_cases']) / (ti_column_value * df_copy.at[index, 'dab_delayering_out_complete_layer_hi'])
            df_copy.at[index, 'auto_station_single_replen_pallet_retrievals'] 			= math.ceil(df_copy.at[index, 'auto_station_single_replen_pallet_consumption'])
            df_copy.at[index, 'auto_station_single_replen_pallet_residuals'] 			= df_copy.at[index, 'auto_station_single_replen_pallet_retrievals'] - df_copy.at[index, 'auto_station_single_replen_pallet_consumption']
            df_copy.at[index, 'auto_station_single_replen_layer_consumption'] 			= (replenishment_case_qty_column_value - df_copy.at[index, 'dab_delayering_out_excess_cases']) / (ti_column_value)
            
            df_copy.at[index, 'auto_station_replenishments_per_day'] 					= case_qty_column_value / (replenishment_case_qty_column_value - df_copy.at[index, 'dab_delayering_out_excess_cases'])
        
            df_copy.at[index, 'auto_station_daily_trays_generated']						= df_copy.at[index, 'auto_station_single_replen_trays_generated']							* df_copy.at[index, 'auto_station_replenishments_per_day']
            df_copy.at[index, 'auto_station_daily_cases_in_trays_generated']			= df_copy.at[index, 'auto_station_single_replen_cases_in_trays']							* df_copy.at[index, 'auto_station_replenishments_per_day']
            df_copy.at[index, 'auto_station_daily_pallet_consumption'] 					= df_copy.at[index, 'auto_station_single_replen_pallet_consumption']						* df_copy.at[index, 'auto_station_replenishments_per_day']
            df_copy.at[index, 'auto_station_daily_pallet_retrievals'] 					= df_copy.at[index, 'auto_station_single_replen_pallet_retrievals']							* df_copy.at[index, 'auto_station_replenishments_per_day']
            df_copy.at[index, 'auto_station_daily_pallet_residuals'] 					= df_copy.at[index, 'auto_station_single_replen_pallet_residuals']							* df_copy.at[index, 'auto_station_replenishments_per_day']
            df_copy.at[index, 'auto_station_daily_layer_consumption'] 					= df_copy.at[index, 'auto_station_single_replen_layer_consumption']							* df_copy.at[index, 'auto_station_replenishments_per_day']
            
            df_copy.at[index, 'surged_auto_station_daily_trays_generated'] 				= df_copy.at[index, 'auto_station_daily_trays_generated'] 									* delayering_surge_factor
            df_copy.at[index, 'surged_auto_station_daily_cases_in_trays_generated'] 	= df_copy.at[index, 'auto_station_daily_cases_in_trays_generated'] 							* delayering_surge_factor
            df_copy.at[index, 'surged_auto_station_daily_pallet_consumption'] 			= df_copy.at[index, 'auto_station_daily_pallet_consumption'] 								* delayering_surge_factor
            df_copy.at[index, 'surged_auto_station_daily_pallet_retrievals'] 			= df_copy.at[index, 'auto_station_daily_pallet_retrievals'] 								* delayering_surge_factor
            df_copy.at[index, 'surged_auto_station_daily_pallet_residuals'] 			= df_copy.at[index, 'auto_station_daily_pallet_residuals'] 									* delayering_surge_factor
            df_copy.at[index, 'surged_auto_station_daily_layer_consumption'] 			= df_copy.at[index, 'auto_station_daily_layer_consumption'] 								* delayering_surge_factor

            df_copy.at[index, 'surged_auto_station_hourly_trays_generated'] 			= df_copy.at[index, 'surged_auto_station_daily_trays_generated'] 							/ delayering_operation_hours
            df_copy.at[index, 'surged_auto_station_hourly_cases_in_trays_generated']	= df_copy.at[index, 'surged_auto_station_daily_cases_in_trays_generated'] 					/ delayering_operation_hours
            df_copy.at[index, 'surged_auto_station_hourly_pallet_consumption']			= df_copy.at[index, 'surged_auto_station_daily_pallet_consumption'] 						/ delayering_operation_hours
            df_copy.at[index, 'surged_auto_station_hourly_pallet_retrievals']			= df_copy.at[index, 'surged_auto_station_daily_pallet_retrievals'] 							/ delayering_operation_hours
            df_copy.at[index, 'surged_auto_station_hourly_pallet_residuals']			= df_copy.at[index, 'surged_auto_station_daily_pallet_residuals'] 							/ delayering_operation_hours
            df_copy.at[index, 'surged_auto_station_hourly_layer_consumption']			= df_copy.at[index, 'surged_auto_station_daily_layer_consumption'] 							/ delayering_operation_hours
            



            
        if  df_copy.at[index, 'dab_delayering_out_excess_cases'] > 0:
            df_copy.at[index, 'top_layer_removal_single_replen_trays_generated'] 			= math.ceil((df_copy.at[index, 'dab_delayering_out_excess_cases']) / cases_per_tray_column_value)
            df_copy.at[index, 'top_layer_removal_single_replen_cases_in_trays']				= cases_per_tray_column_value * df_copy.at[index, 'top_layer_removal_single_replen_trays_generated']
            
            if df_copy.at[index, 'dab_delayering_out_complete_layer_hi'] != 0:
                df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption'] 		= 0.0 
                df_copy.at[index, 'top_layer_removal_single_replen_pallet_retrievals'] 			= df_copy.at[index, 'auto_station_single_replen_pallet_retrievals'] 
                df_copy.at[index, 'top_layer_removal_single_replen_pallet_residuals'] 			= df_copy.at[index, 'auto_station_single_replen_pallet_retrievals']
                df_copy.at[index, 'top_layer_removal_single_replen_layer_consumption'] 			= df_copy.at[index, 'auto_station_single_replen_pallet_retrievals'] 
                
                df_copy.at[index, 'top_layer_removal_replenishments_per_day'] 					= df_copy.at[index, 'auto_station_replenishments_per_day']
            else:
                df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption'] 		= math.ceil((replenishment_case_qty_column_value) / df_copy.at[index, 'dab_delayering_out_excess_cases']) 
                df_copy.at[index, 'top_layer_removal_single_replen_pallet_retrievals'] 			= df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption'] 	
                df_copy.at[index, 'top_layer_removal_single_replen_pallet_residuals'] 			= df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption']	
                df_copy.at[index, 'top_layer_removal_single_replen_layer_consumption'] 			= df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption']	
                
                df_copy.at[index, 'top_layer_removal_replenishments_per_day']					= df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption']	
                
                
        
            df_copy.at[index, 'top_layer_removal_daily_trays_generated']						= df_copy.at[index, 'top_layer_removal_single_replen_trays_generated']							* df_copy.at[index, 'top_layer_removal_replenishments_per_day']
            df_copy.at[index, 'top_layer_removal_daily_cases_in_trays_generated']				= df_copy.at[index, 'top_layer_removal_single_replen_cases_in_trays']							* df_copy.at[index, 'top_layer_removal_replenishments_per_day']
            df_copy.at[index, 'top_layer_removal_daily_pallet_consumption'] 					= df_copy.at[index, 'top_layer_removal_single_replen_pallet_consumption']						* df_copy.at[index, 'top_layer_removal_replenishments_per_day']
            df_copy.at[index, 'top_layer_removal_daily_pallet_retrievals'] 						= df_copy.at[index, 'top_layer_removal_single_replen_pallet_retrievals']						* df_copy.at[index, 'top_layer_removal_replenishments_per_day']
            df_copy.at[index, 'top_layer_removal_daily_pallet_residuals'] 						= df_copy.at[index, 'top_layer_removal_single_replen_pallet_residuals']							* df_copy.at[index, 'top_layer_removal_replenishments_per_day']
            df_copy.at[index, 'top_layer_removal_daily_layer_consumption'] 						= df_copy.at[index, 'top_layer_removal_single_replen_layer_consumption']						* df_copy.at[index, 'top_layer_removal_replenishments_per_day']
            
            df_copy.at[index, 'surged_top_layer_removal_daily_trays_generated'] 					= df_copy.at[index, 'top_layer_removal_daily_trays_generated'] 										* delayering_surge_factor
            df_copy.at[index, 'surged_top_layer_removal_daily_cases_in_trays_generated'] 			= df_copy.at[index, 'top_layer_removal_daily_cases_in_trays_generated'] 							* delayering_surge_factor
            df_copy.at[index, 'surged_top_layer_removal_daily_pallet_consumption'] 					= df_copy.at[index, 'top_layer_removal_daily_pallet_consumption'] 									* delayering_surge_factor
            df_copy.at[index, 'surged_top_layer_removal_daily_pallet_retrievals'] 					= df_copy.at[index, 'top_layer_removal_daily_pallet_retrievals'] 									* delayering_surge_factor
            df_copy.at[index, 'surged_top_layer_removal_daily_pallet_residuals'] 					= df_copy.at[index, 'top_layer_removal_daily_pallet_residuals'] 									* delayering_surge_factor
            df_copy.at[index, 'surged_top_layer_removal_daily_layer_consumption'] 					= df_copy.at[index, 'top_layer_removal_daily_layer_consumption'] 									* delayering_surge_factor

            df_copy.at[index, 'surged_top_layer_removal_hourly_trays_generated'] 					= df_copy.at[index, 'surged_top_layer_removal_daily_trays_generated'] 								/ delayering_operation_hours
            df_copy.at[index, 'surged_top_layer_removal_hourly_cases_in_trays_generated']			= df_copy.at[index, 'surged_top_layer_removal_daily_cases_in_trays_generated'] 						/ delayering_operation_hours
            df_copy.at[index, 'surged_top_layer_removal_hourly_pallet_consumption']					= df_copy.at[index, 'surged_top_layer_removal_daily_pallet_consumption'] 							/ delayering_operation_hours
            df_copy.at[index, 'surged_top_layer_removal_hourly_pallet_retrievals']					= df_copy.at[index, 'surged_top_layer_removal_daily_pallet_retrievals'] 							/ delayering_operation_hours
            df_copy.at[index, 'surged_top_layer_removal_hourly_pallet_residuals']					= df_copy.at[index, 'surged_top_layer_removal_daily_pallet_residuals'] 								/ delayering_operation_hours
            df_copy.at[index, 'surged_top_layer_removal_hourly_layer_consumption']					= df_copy.at[index, 'surged_top_layer_removal_daily_layer_consumption'] 							/ delayering_operation_hours
                
    if manual_stations_only == "True" or pallet_consumption_method_column_value == "in_case_qty" or (incomplete_layer_handling == "be pushed to Manual station for delayering" and df_copy.at[index, 'dab_delayering_out_excess_cases'] > 0):
        
        
        df_copy.at[index, 'manual_station_single_replen_trays_generated'] 			= math.ceil(replenishment_case_qty_column_value / cases_per_tray_column_value)
        df_copy.at[index, 'manual_station_single_replen_cases_in_trays']				= cases_per_tray_column_value * df_copy.at[index, 'manual_station_single_replen_trays_generated']
        
        df_copy.at[index, 'manual_station_single_replen_pallet_consumption'] 		= replenishment_case_qty_column_value / (ti_column_value * df_copy.at[index, 'dab_delayering_out_complete_layer_hi'] + df_copy.at[index, 'dab_delayering_out_excess_cases'])
        df_copy.at[index, 'manual_station_single_replen_pallet_retrievals'] 		= math.ceil(df_copy.at[index, 'manual_station_single_replen_pallet_consumption'])
        df_copy.at[index, 'manual_station_single_replen_pallet_residuals'] 			= df_copy.at[index, 'manual_station_single_replen_pallet_retrievals'] - df_copy.at[index, 'manual_station_single_replen_pallet_consumption']
        df_copy.at[index, 'manual_station_single_replen_layer_consumption'] 		= math.ceil(replenishment_case_qty_column_value / (ti_column_value))
        
        df_copy.at[index, 'manual_station_replenishments_per_day'] 					= case_qty_column_value / replenishment_case_qty_column_value
    
        df_copy.at[index, 'manual_station_daily_trays_generated']					= df_copy.at[index, 'manual_station_single_replen_trays_generated']							* df_copy.at[index, 'manual_station_replenishments_per_day']
        df_copy.at[index, 'manual_station_daily_cases_in_trays_generated']			= df_copy.at[index, 'manual_station_single_replen_cases_in_trays']							* df_copy.at[index, 'manual_station_replenishments_per_day']
        df_copy.at[index, 'manual_station_daily_pallet_consumption'] 				= df_copy.at[index, 'manual_station_single_replen_pallet_consumption']						* df_copy.at[index, 'manual_station_replenishments_per_day']
        df_copy.at[index, 'manual_station_daily_pallet_retrievals'] 				= df_copy.at[index, 'manual_station_single_replen_pallet_retrievals']						* df_copy.at[index, 'manual_station_replenishments_per_day']
        df_copy.at[index, 'manual_station_daily_pallet_residuals'] 					= df_copy.at[index, 'manual_station_single_replen_pallet_residuals']						* df_copy.at[index, 'manual_station_replenishments_per_day']
        df_copy.at[index, 'manual_station_daily_layer_consumption'] 				= df_copy.at[index, 'manual_station_single_replen_layer_consumption']						* df_copy.at[index, 'manual_station_replenishments_per_day']
        
        df_copy.at[index, 'surged_manual_station_daily_trays_generated'] 			= df_copy.at[index, 'manual_station_daily_trays_generated'] 								* delayering_surge_factor
        df_copy.at[index, 'surged_manual_station_daily_cases_in_trays_generated'] 	= df_copy.at[index, 'manual_station_daily_cases_in_trays_generated'] 						* delayering_surge_factor
        df_copy.at[index, 'surged_manual_station_daily_pallet_consumption'] 		= df_copy.at[index, 'manual_station_daily_pallet_consumption'] 								* delayering_surge_factor
        df_copy.at[index, 'surged_manual_station_daily_pallet_retrievals'] 			= df_copy.at[index, 'manual_station_daily_pallet_retrievals'] 								* delayering_surge_factor
        df_copy.at[index, 'surged_manual_station_daily_pallet_residuals'] 			= df_copy.at[index, 'manual_station_daily_pallet_residuals'] 								* delayering_surge_factor
        df_copy.at[index, 'surged_manual_station_daily_layer_consumption'] 			= df_copy.at[index, 'manual_station_daily_layer_consumption'] 								* delayering_surge_factor

        df_copy.at[index, 'surged_manual_station_hourly_trays_generated'] 			= df_copy.at[index, 'surged_manual_station_daily_trays_generated'] 							/ delayering_operation_hours
        df_copy.at[index, 'surged_manual_station_hourly_cases_in_trays_generated']	= df_copy.at[index, 'surged_manual_station_daily_cases_in_trays_generated'] 				/ delayering_operation_hours
        df_copy.at[index, 'surged_manual_station_hourly_pallet_consumption']		= df_copy.at[index, 'surged_manual_station_daily_pallet_consumption'] 						/ delayering_operation_hours
        df_copy.at[index, 'surged_manual_station_hourly_pallet_retrievals']			= df_copy.at[index, 'surged_manual_station_daily_pallet_retrievals'] 						/ delayering_operation_hours
        df_copy.at[index, 'surged_manual_station_hourly_pallet_residuals']			= df_copy.at[index, 'surged_manual_station_daily_pallet_residuals'] 						/ delayering_operation_hours
        df_copy.at[index, 'surged_manual_station_hourly_layer_consumption']			= df_copy.at[index, 'surged_manual_station_daily_layer_consumption'] 						/ delayering_operation_hours
    
auto_station_df 			= df_copy[df_copy['auto_station_single_replen_trays_generated'] != 0].copy(deep=True)
top_layer_removal_df 		= df_copy[df_copy['top_layer_removal_single_replen_trays_generated'] != 0].copy(deep=True)
manual_station_df 			= df_copy[df_copy['manual_station_single_replen_trays_generated'] != 0].copy(deep=True)

auto_station_row_count 										= len(auto_station_df)
auto_station_daily_trays_generated							= auto_station_df["auto_station_daily_trays_generated"].sum()
auto_station_daily_cases_in_trays_generated					= auto_station_df["auto_station_daily_cases_in_trays_generated"].sum()
auto_station_daily_pallet_consumption						= auto_station_df["auto_station_daily_pallet_consumption"].sum()
auto_station_daily_pallet_retrievals						= auto_station_df["auto_station_daily_pallet_retrievals"].sum()
auto_station_daily_pallet_residuals							= auto_station_df["auto_station_daily_pallet_residuals"].sum()
auto_station_daily_layer_consumption						= auto_station_df["auto_station_daily_layer_consumption"].sum()

surged_auto_station_daily_trays_generated 					= auto_station_df["surged_auto_station_daily_trays_generated"].sum()
surged_auto_station_daily_cases_in_trays_generated 			= auto_station_df["surged_auto_station_daily_cases_in_trays_generated"].sum()
surged_auto_station_daily_pallet_consumption 				= auto_station_df["surged_auto_station_daily_pallet_consumption"].sum()
surged_auto_station_daily_pallet_retrievals 				= auto_station_df["surged_auto_station_daily_pallet_retrievals"].sum()
surged_auto_station_daily_pallet_residuals 					= auto_station_df["surged_auto_station_daily_pallet_residuals"].sum()
surged_auto_station_daily_layer_consumption 				= auto_station_df["surged_auto_station_daily_layer_consumption"].sum()

surged_auto_station_hourly_trays_generated 					= auto_station_df["surged_auto_station_hourly_trays_generated"].sum()
surged_auto_station_hourly_cases_in_trays_generated 		= auto_station_df["surged_auto_station_hourly_cases_in_trays_generated"].sum()
surged_auto_station_hourly_pallet_consumption 				= auto_station_df["surged_auto_station_hourly_pallet_consumption"].sum()
surged_auto_station_hourly_pallet_retrievals 				= auto_station_df["surged_auto_station_hourly_pallet_retrievals"].sum()
surged_auto_station_hourly_pallet_residuals 				= auto_station_df["surged_auto_station_hourly_pallet_residuals"].sum()
surged_auto_station_hourly_layer_consumption 				= auto_station_df["surged_auto_station_hourly_layer_consumption"].sum()

top_layer_station_row_count 								= len(top_layer_removal_df)
top_layer_removal_daily_trays_generated						= top_layer_removal_df["top_layer_removal_daily_trays_generated"].sum()
top_layer_removal_daily_cases_in_trays_generated			= top_layer_removal_df["top_layer_removal_daily_cases_in_trays_generated"].sum()
top_layer_removal_daily_pallet_consumption					= top_layer_removal_df["top_layer_removal_daily_pallet_consumption"].sum()
top_layer_removal_daily_pallet_retrievals					= top_layer_removal_df["top_layer_removal_daily_pallet_retrievals"].sum()
top_layer_removal_daily_pallet_residuals					= top_layer_removal_df["top_layer_removal_daily_pallet_residuals"].sum()
top_layer_removal_daily_layer_consumption					= top_layer_removal_df["top_layer_removal_daily_layer_consumption"].sum()

surged_top_layer_removal_daily_trays_generated 				= top_layer_removal_df["surged_top_layer_removal_daily_trays_generated"].sum()
surged_top_layer_removal_daily_cases_in_trays_generated 	= top_layer_removal_df["surged_top_layer_removal_daily_cases_in_trays_generated"].sum()
surged_top_layer_removal_daily_pallet_consumption 			= top_layer_removal_df["surged_top_layer_removal_daily_pallet_consumption"].sum()
surged_top_layer_removal_daily_pallet_retrievals 			= top_layer_removal_df["surged_top_layer_removal_daily_pallet_retrievals"].sum()
surged_top_layer_removal_daily_pallet_residuals 			= top_layer_removal_df["surged_top_layer_removal_daily_pallet_residuals"].sum()
surged_top_layer_removal_daily_layer_consumption 			= top_layer_removal_df["surged_top_layer_removal_daily_layer_consumption"].sum()

surged_top_layer_removal_hourly_trays_generated 			= top_layer_removal_df["surged_top_layer_removal_hourly_trays_generated"].sum()
surged_top_layer_removal_hourly_cases_in_trays_generated 	= top_layer_removal_df["surged_top_layer_removal_hourly_cases_in_trays_generated"].sum()
surged_top_layer_removal_hourly_pallet_consumption 			= top_layer_removal_df["surged_top_layer_removal_hourly_pallet_consumption"].sum()
surged_top_layer_removal_hourly_pallet_retrievals 			= top_layer_removal_df["surged_top_layer_removal_hourly_pallet_retrievals"].sum()
surged_top_layer_removal_hourly_pallet_residuals 			= top_layer_removal_df["surged_top_layer_removal_hourly_pallet_residuals"].sum()
surged_top_layer_removal_hourly_layer_consumption 			= top_layer_removal_df["surged_top_layer_removal_hourly_layer_consumption"].sum()

manual_station_row_count 									= len(manual_station_df)
manual_station_daily_trays_generated						= manual_station_df["manual_station_daily_trays_generated"].sum()
manual_station_daily_cases_in_trays_generated				= manual_station_df["manual_station_daily_cases_in_trays_generated"].sum()
manual_station_daily_pallet_consumption						= manual_station_df["manual_station_daily_pallet_consumption"].sum()
manual_station_daily_pallet_retrievals						= manual_station_df["manual_station_daily_pallet_retrievals"].sum()
manual_station_daily_pallet_residuals						= manual_station_df["manual_station_daily_pallet_residuals"].sum()
manual_station_daily_layer_consumption						= manual_station_df["manual_station_daily_layer_consumption"].sum()

surged_manual_station_daily_trays_generated 				= manual_station_df["surged_manual_station_daily_trays_generated"].sum()
surged_manual_station_daily_cases_in_trays_generated 		= manual_station_df["surged_manual_station_daily_cases_in_trays_generated"].sum()
surged_manual_station_daily_pallet_consumption 				= manual_station_df["surged_manual_station_daily_pallet_consumption"].sum()
surged_manual_station_daily_pallet_retrievals 				= manual_station_df["surged_manual_station_daily_pallet_retrievals"].sum()
surged_manual_station_daily_pallet_residuals 				= manual_station_df["surged_manual_station_daily_pallet_residuals"].sum()
surged_manual_station_daily_layer_consumption 				= manual_station_df["surged_manual_station_daily_layer_consumption"].sum()

surged_manual_station_hourly_trays_generated 				= manual_station_df["surged_manual_station_hourly_trays_generated"].sum()
surged_manual_station_hourly_cases_in_trays_generated 		= manual_station_df["surged_manual_station_hourly_cases_in_trays_generated"].sum()
surged_manual_station_hourly_pallet_consumption 			= manual_station_df["surged_manual_station_hourly_pallet_consumption"].sum()
surged_manual_station_hourly_pallet_retrievals 				= manual_station_df["surged_manual_station_hourly_pallet_retrievals"].sum()
surged_manual_station_hourly_pallet_residuals 				= manual_station_df["surged_manual_station_hourly_pallet_residuals"].sum()
surged_manual_station_hourly_layer_consumption 				= manual_station_df["surged_manual_station_hourly_layer_consumption"].sum()

original_name = "auto_station_single_replen_trays_generated"
new_name = "single_replen_trays_generated"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_single_replen_cases_in_trays"
new_name = "single_replen_cases_in_trays"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_single_replen_pallet_consumption"
new_name = "single_replen_pallet_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_single_replen_pallet_retrievals"
new_name = "single_replen_pallet_retrievals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_single_replen_pallet_residuals"
new_name = "single_replen_pallet_residuals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_single_replen_layer_consumption"
new_name = "single_replen_layer_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_replenishments_per_day"
new_name = "replenishments_per_day"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_daily_trays_generated"
new_name = "daily_trays_generated"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_daily_cases_in_trays_generated"
new_name = "daily_cases_in_trays_generated"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_daily_pallet_consumption"
new_name = "daily_pallet_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_daily_pallet_retrievals"
new_name = "daily_pallet_retrievals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_daily_pallet_residuals"
new_name = "daily_pallet_residuals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "auto_station_daily_layer_consumption"
new_name = "daily_layer_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_daily_trays_generated"
new_name = "surged_daily_trays_generated"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_daily_cases_in_trays_generated"
new_name = "surged_daily_cases_in_trays_generated"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_daily_pallet_consumption"
new_name = "surged_daily_pallet_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_daily_pallet_retrievals"
new_name = "surged_daily_pallet_retrievals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_daily_pallet_residuals"
new_name = "surged_daily_pallet_residuals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_daily_layer_consumption"
new_name = "surged_daily_layer_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_hourly_trays_generated"
new_name = "surged_hourly_trays_generated"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_hourly_cases_in_trays_generated"
new_name = "surged_hourly_cases_in_trays_generated"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_hourly_pallet_consumption"
new_name = "surged_hourly_pallet_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_hourly_pallet_retrievals"
new_name = "surged_hourly_pallet_retrievals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_hourly_pallet_residuals"
new_name = "surged_hourly_pallet_residuals"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_auto_station_hourly_layer_consumption"
new_name = "surged_hourly_layer_consumption"
auto_station_df.rename(columns={original_name: new_name}, inplace=True)

auto_station_df['flow_name'] = "auto_station"

original_name = "top_layer_removal_single_replen_trays_generated"
new_name = "single_replen_trays_generated"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_single_replen_cases_in_trays"
new_name = "single_replen_cases_in_trays"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_single_replen_pallet_consumption"
new_name = "single_replen_pallet_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_single_replen_pallet_retrievals"
new_name = "single_replen_pallet_retrievals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_single_replen_pallet_residuals"
new_name = "single_replen_pallet_residuals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_single_replen_layer_consumption"
new_name = "single_replen_layer_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_replenishments_per_day"
new_name = "replenishments_per_day"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_daily_trays_generated"
new_name = "daily_trays_generated"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_daily_cases_in_trays_generated"
new_name = "daily_cases_in_trays_generated"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_daily_pallet_consumption"
new_name = "daily_pallet_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_daily_pallet_retrievals"
new_name = "daily_pallet_retrievals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_daily_pallet_residuals"
new_name = "daily_pallet_residuals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "top_layer_removal_daily_layer_consumption"
new_name = "daily_layer_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_daily_trays_generated"
new_name = "surged_daily_trays_generated"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_daily_cases_in_trays_generated"
new_name = "surged_daily_cases_in_trays_generated"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_daily_pallet_consumption"
new_name = "surged_daily_pallet_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_daily_pallet_retrievals"
new_name = "surged_daily_pallet_retrievals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_daily_pallet_residuals"
new_name = "surged_daily_pallet_residuals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_daily_layer_consumption"
new_name = "surged_daily_layer_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_hourly_trays_generated"
new_name = "surged_hourly_trays_generated"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_hourly_cases_in_trays_generated"
new_name = "surged_hourly_cases_in_trays_generated"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_hourly_pallet_consumption"
new_name = "surged_hourly_pallet_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_hourly_pallet_retrievals"
new_name = "surged_hourly_pallet_retrievals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_hourly_pallet_residuals"
new_name = "surged_hourly_pallet_residuals"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_top_layer_removal_hourly_layer_consumption"
new_name = "surged_hourly_layer_consumption"
top_layer_removal_df.rename(columns={original_name: new_name}, inplace=True)

top_layer_removal_df['flow_name'] = "top_layer_removal"

original_name = "manual_station_single_replen_trays_generated"
new_name = "single_replen_trays_generated"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_single_replen_cases_in_trays"
new_name = "single_replen_cases_in_trays"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_single_replen_pallet_consumption"
new_name = "single_replen_pallet_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_single_replen_pallet_retrievals"
new_name = "single_replen_pallet_retrievals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_single_replen_pallet_residuals"
new_name = "single_replen_pallet_residuals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_single_replen_layer_consumption"
new_name = "single_replen_layer_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_replenishments_per_day"
new_name = "replenishments_per_day"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_daily_trays_generated"
new_name = "daily_trays_generated"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_daily_cases_in_trays_generated"
new_name = "daily_cases_in_trays_generated"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_daily_pallet_consumption"
new_name = "daily_pallet_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_daily_pallet_retrievals"
new_name = "daily_pallet_retrievals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_daily_pallet_residuals"
new_name = "daily_pallet_residuals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "manual_station_daily_layer_consumption"
new_name = "daily_layer_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_daily_trays_generated"
new_name = "surged_daily_trays_generated"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_daily_cases_in_trays_generated"
new_name = "surged_daily_cases_in_trays_generated"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_daily_pallet_consumption"
new_name = "surged_daily_pallet_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_daily_pallet_retrievals"
new_name = "surged_daily_pallet_retrievals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_daily_pallet_residuals"
new_name = "surged_daily_pallet_residuals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_daily_layer_consumption"
new_name = "surged_daily_layer_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_hourly_trays_generated"
new_name = "surged_hourly_trays_generated"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_hourly_cases_in_trays_generated"
new_name = "surged_hourly_cases_in_trays_generated"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_hourly_pallet_consumption"
new_name = "surged_hourly_pallet_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_hourly_pallet_retrievals"
new_name = "surged_hourly_pallet_retrievals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_hourly_pallet_residuals"
new_name = "surged_hourly_pallet_residuals"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

original_name = "surged_manual_station_hourly_layer_consumption"
new_name = "surged_hourly_layer_consumption"
manual_station_df.rename(columns={original_name: new_name}, inplace=True)

manual_station_df['flow_name'] = "manual_station"

drop_column_list_auto = []

drop_column_list_auto.append("auto_station_single_replen_trays_generated")
drop_column_list_auto.append("auto_station_single_replen_cases_in_trays")

drop_column_list_auto.append("auto_station_single_replen_pallet_consumption")
drop_column_list_auto.append("auto_station_single_replen_pallet_retrievals")
drop_column_list_auto.append("auto_station_single_replen_pallet_residuals")
drop_column_list_auto.append("auto_station_single_replen_layer_consumption")

drop_column_list_auto.append("auto_station_replenishments_per_day")

drop_column_list_auto.append("auto_station_daily_trays_generated")
drop_column_list_auto.append("auto_station_daily_cases_in_trays_generated")
drop_column_list_auto.append("auto_station_daily_pallet_consumption")
drop_column_list_auto.append("auto_station_daily_pallet_retrievals")
drop_column_list_auto.append("auto_station_daily_pallet_residuals")
drop_column_list_auto.append("auto_station_daily_layer_consumption")

drop_column_list_auto.append("surged_auto_station_daily_trays_generated")
drop_column_list_auto.append("surged_auto_station_daily_cases_in_trays_generated")
drop_column_list_auto.append("surged_auto_station_daily_pallet_consumption")
drop_column_list_auto.append("surged_auto_station_daily_pallet_retrievals")
drop_column_list_auto.append("surged_auto_station_daily_pallet_residuals")
drop_column_list_auto.append("surged_auto_station_daily_layer_consumption")

drop_column_list_auto.append("surged_auto_station_hourly_trays_generated")
drop_column_list_auto.append("surged_auto_station_hourly_cases_in_trays_generated")
drop_column_list_auto.append("surged_auto_station_hourly_pallet_consumption")
drop_column_list_auto.append("surged_auto_station_hourly_pallet_retrievals")
drop_column_list_auto.append("surged_auto_station_hourly_pallet_residuals")
drop_column_list_auto.append("surged_auto_station_hourly_layer_consumption")

drop_column_list_top = []
drop_column_list_top.append("top_layer_removal_single_replen_trays_generated")
drop_column_list_top.append("top_layer_removal_single_replen_cases_in_trays")

drop_column_list_top.append("top_layer_removal_single_replen_pallet_consumption")
drop_column_list_top.append("top_layer_removal_single_replen_pallet_retrievals")
drop_column_list_top.append("top_layer_removal_single_replen_pallet_residuals")
drop_column_list_top.append("top_layer_removal_single_replen_layer_consumption")

drop_column_list_top.append("top_layer_removal_replenishments_per_day")
drop_column_list_top.append("top_layer_removal_daily_trays_generated")
drop_column_list_top.append("top_layer_removal_daily_cases_in_trays_generated")
drop_column_list_top.append("top_layer_removal_daily_pallet_consumption")
drop_column_list_top.append("top_layer_removal_daily_pallet_retrievals")
drop_column_list_top.append("top_layer_removal_daily_pallet_residuals")
drop_column_list_top.append("top_layer_removal_daily_layer_consumption")

drop_column_list_top.append("surged_top_layer_removal_daily_trays_generated")
drop_column_list_top.append("surged_top_layer_removal_daily_cases_in_trays_generated")
drop_column_list_top.append("surged_top_layer_removal_daily_pallet_consumption")
drop_column_list_top.append("surged_top_layer_removal_daily_pallet_retrievals")
drop_column_list_top.append("surged_top_layer_removal_daily_pallet_residuals")
drop_column_list_top.append("surged_top_layer_removal_daily_layer_consumption")

drop_column_list_top.append("surged_top_layer_removal_hourly_trays_generated")
drop_column_list_top.append("surged_top_layer_removal_hourly_cases_in_trays_generated")
drop_column_list_top.append("surged_top_layer_removal_hourly_pallet_consumption")
drop_column_list_top.append("surged_top_layer_removal_hourly_pallet_retrievals")
drop_column_list_top.append("surged_top_layer_removal_hourly_pallet_residuals")
drop_column_list_top.append("surged_top_layer_removal_hourly_layer_consumption")

drop_column_list_manual = []
drop_column_list_manual.append("manual_station_single_replen_trays_generated")
drop_column_list_manual.append("manual_station_single_replen_cases_in_trays")

drop_column_list_manual.append("manual_station_single_replen_pallet_consumption")
drop_column_list_manual.append("manual_station_single_replen_pallet_retrievals")
drop_column_list_manual.append("manual_station_single_replen_pallet_residuals")
drop_column_list_manual.append("manual_station_single_replen_layer_consumption")

drop_column_list_manual.append("manual_station_replenishments_per_day")

drop_column_list_manual.append("manual_station_daily_trays_generated")
drop_column_list_manual.append("manual_station_daily_cases_in_trays_generated")
drop_column_list_manual.append("manual_station_daily_pallet_consumption")
drop_column_list_manual.append("manual_station_daily_pallet_retrievals")
drop_column_list_manual.append("manual_station_daily_pallet_residuals")
drop_column_list_manual.append("manual_station_daily_layer_consumption")

drop_column_list_manual.append("surged_manual_station_daily_trays_generated")
drop_column_list_manual.append("surged_manual_station_daily_cases_in_trays_generated")
drop_column_list_manual.append("surged_manual_station_daily_pallet_consumption")
drop_column_list_manual.append("surged_manual_station_daily_pallet_retrievals")
drop_column_list_manual.append("surged_manual_station_daily_pallet_residuals")
drop_column_list_manual.append("surged_manual_station_daily_layer_consumption")

drop_column_list_manual.append("surged_manual_station_hourly_trays_generated")
drop_column_list_manual.append("surged_manual_station_hourly_cases_in_trays_generated")
drop_column_list_manual.append("surged_manual_station_hourly_pallet_consumption")
drop_column_list_manual.append("surged_manual_station_hourly_pallet_retrievals")
drop_column_list_manual.append("surged_manual_station_hourly_pallet_residuals")
drop_column_list_manual.append("surged_manual_station_hourly_layer_consumption")

drop_column_list = drop_column_list_manual + drop_column_list_top
auto_station_df.drop(columns=drop_column_list, inplace=True)

drop_column_list = drop_column_list_manual + drop_column_list_auto
top_layer_removal_df.drop(columns=drop_column_list, inplace=True)

drop_column_list = drop_column_list_top + drop_column_list_auto
manual_station_df.drop(columns=drop_column_list, inplace=True)

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
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "Inputs:"
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "incomplete_layer_handling"
df_out.at[i, 'value'] 				= incomplete_layer_handling
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "manual_stations_only"
df_out.at[i, 'value'] 				= manual_stations_only
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "delayering_operation_hours"
df_out.at[i, 'value'] 				= str(format_float_with_commas(delayering_operation_hours,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "delayering_surge_factor"
df_out.at[i, 'value'] 				= str(format_float_with_commas(delayering_surge_factor,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "Outputs (Rate):"
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "auto_station_row_count"
df_out.at[i, 'value'] 				= str(format_float_with_commas(auto_station_row_count,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "auto_station_daily_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(auto_station_daily_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "auto_station_daily_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(auto_station_daily_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "auto_station_daily_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(auto_station_daily_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "auto_station_daily_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(auto_station_daily_pallet_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "auto_station_daily_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(auto_station_daily_pallet_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "auto_station_daily_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(auto_station_daily_layer_consumption,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_auto_station_daily_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_daily_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_auto_station_daily_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_daily_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_auto_station_daily_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_daily_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_auto_station_daily_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_daily_pallet_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_auto_station_daily_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_daily_pallet_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_auto_station_daily_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_daily_layer_consumption,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_auto_station_hourly_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_hourly_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_auto_station_hourly_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_hourly_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_auto_station_hourly_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_hourly_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_auto_station_hourly_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_hourly_pallet_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_auto_station_hourly_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_hourly_pallet_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_auto_station_hourly_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_auto_station_hourly_layer_consumption,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "top_layer_station_row_count"
df_out.at[i, 'value'] 				= str(format_float_with_commas(top_layer_station_row_count,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "top_layer_removal_daily_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(top_layer_removal_daily_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "top_layer_removal_daily_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(top_layer_removal_daily_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "top_layer_removal_daily_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(top_layer_removal_daily_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "top_layer_removal_daily_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(top_layer_removal_daily_pallet_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "top_layer_removal_daily_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(top_layer_removal_daily_pallet_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "top_layer_removal_daily_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(top_layer_removal_daily_layer_consumption,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_daily_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_daily_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_daily_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_daily_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_daily_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_daily_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_daily_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_daily_pallet_retrievals))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_daily_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_daily_pallet_residuals))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_daily_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_daily_layer_consumption))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_hourly_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_hourly_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_hourly_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_hourly_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_hourly_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_hourly_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_hourly_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_hourly_pallet_retrievals))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_hourly_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_hourly_pallet_residuals))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_top_layer_removal_hourly_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_top_layer_removal_hourly_layer_consumption))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "manual_station_row_count"
df_out.at[i, 'value'] 				= str(format_float_with_commas(manual_station_row_count,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "manual_station_daily_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(manual_station_daily_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "manual_station_daily_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(manual_station_daily_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "manual_station_daily_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(manual_station_daily_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "manual_station_daily_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(manual_station_daily_pallet_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "manual_station_daily_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(manual_station_daily_pallet_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "manual_station_daily_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(manual_station_daily_layer_consumption,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_manual_station_daily_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_daily_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_manual_station_daily_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_daily_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_manual_station_daily_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_daily_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_manual_station_daily_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_daily_pallet_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_manual_station_daily_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_daily_pallet_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_manual_station_daily_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_daily_layer_consumption,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_manual_station_hourly_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_hourly_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_manual_station_hourly_cases_in_trays_generated"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_hourly_cases_in_trays_generated,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_manual_station_hourly_pallet_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_hourly_pallet_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_manual_station_hourly_pallet_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_hourly_pallet_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_manual_station_hourly_pallet_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_hourly_pallet_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_manual_station_hourly_layer_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_manual_station_hourly_layer_consumption,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Depalletising Flows"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

return df_out, auto_station_df, top_layer_removal_df, manual_station_df, df_copy
