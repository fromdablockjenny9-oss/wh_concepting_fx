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
def format_float_with_commas(number, decimal_places=0):
    floored_number = round(number, decimal_places)
    formatted_number = f"{floored_number:,.{decimal_places}f}"
    
    return formatted_number

df = input_1.to_pandas()

df = df.reset_index(drop=True)

ti_column_name 								= self.ti_column_name
cpp_column_name 							= self.cpp_column_name
case_qty_column_name 						= self.case_qty_column_name
case_qty_mean_column_name 					= self.case_qty_mean_column_name
case_qty_std_dev_column_name 				= self.case_qty_std_dev_column_name

inners_per_outer_column_name 				= self.inners_per_outer_column_name

max_doi_to_replenish_in_pallet_qty 			= self.max_doi_to_replenish_in_pallet_qty
max_doi_to_replenish_in_layer_qty 			= self.max_doi_to_replenish_in_layer_qty
doi_target_for_layers						= self.doi_target_for_layers
max_doi_to_replenish_in_case_qty			= self.max_doi_to_replenish_in_case_qty

roundup_to_full_pallet_qty_threshold 		= self.roundup_to_full_pallet_qty_threshold
roundup_to_full_layer_qty_threshold 		= self.roundup_to_full_layer_qty_threshold

disable_individual_case_replenishment 		= self.disable_individual_case_replenishment
disable_layer_replenishment 				= self.disable_layer_replenishment

roundup_to_full_tray_qty 					= self.roundup_to_full_tray_qty

df_copy = df.copy(deep=True)
df_copy['cases_as_trays'] = df_copy[case_qty_column_name] / df_copy[inners_per_outer_column_name]


plot_df_0 = pd.DataFrame()
plot_df_0["0"] = None
plot_df_0["1"] = None
plot_df_0["2"] = None
plot_df_0["3"] = None
plot_df_0["4"] = None
plot_df_0["5"] = None

plot_df_0_i = -1

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = "Total Input Rows:"
plot_df_0.at[plot_df_0_i, "1"] = format_float_with_commas(len(df_copy), 0)

my_total_cases = df_copy[case_qty_column_name].sum()
plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(my_total_cases, 2)

plot_df_0.at[plot_df_0_i, "3"] = "100.00%"

my_total_cases_as_trays = df_copy["cases_as_trays"].sum()
plot_df_0.at[plot_df_0_i, "4"] = format_float_with_commas(my_total_cases_as_trays, 2)
plot_df_0.at[plot_df_0_i, "5"] = "100.00%"




df_pure = pd.DataFrame(df_copy.to_dict())
unique_rows_count = df_pure.drop_duplicates().shape[0]

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = "Unique Input Rows:"
plot_df_0.at[plot_df_0_i, "1"] = format_float_with_commas(unique_rows_count, 0)

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = ""

df['pallet_consumption_method'] = ""
df['case_replenishment_qty'] = 0

for index, row in df.iterrows():
    
    ti_value 								= row[ti_column_name]
    cpp_column_value 						= row[cpp_column_name]
    case_qty_value 							= row[case_qty_column_name]
    case_qty_mean_value 					= row[case_qty_mean_column_name]
    case_qty_std_dev_value 					= row[case_qty_std_dev_column_name]
    inners_per_outer_value 					= row[inners_per_outer_column_name]
    
    cpp = cpp_column_value
    
    days_to_consume_pallet = cpp / case_qty_value
    days_to_consume_layer = ti_value / case_qty_value
    days_to_consume_case = 1/case_qty_value
    
    my_replen_method = ""
    my_replen_qty = 0
    
    min_replen_qty_array = []
    min_replen_qty_array.append(0)
    min_replen_qty_array.append((case_qty_mean_value + case_qty_std_dev_value)*2) 
    
    if days_to_consume_pallet <= max_doi_to_replenish_in_pallet_qty:
        my_replen_method = "in_pallet_qty"
        min_replen_qty_array.append(cpp) 
    elif days_to_consume_layer <= max_doi_to_replenish_in_layer_qty:
        my_replen_method = "in_layer_qty"
        min_replen_qty_array.append(ti_value) 
        min_replen_qty_array.append(math.ceil((doi_target_for_layers/days_to_consume_layer) * ti_value))
    else:
        my_replen_method = "in_case_qty"
        min_replen_qty_array.append(math.ceil(max_doi_to_replenish_in_case_qty/days_to_consume_case)) 
    
    
    my_replen_qty = max(min_replen_qty_array)
    
    if my_replen_qty > cpp * roundup_to_full_pallet_qty_threshold and my_replen_method != "in_pallet_qty":
        my_replen_method = "in_pallet_qty"
        my_replen_qty = ensure_multiple(my_replen_qty, cpp)
    
    if my_replen_qty > ti_value * roundup_to_full_layer_qty_threshold and my_replen_method == "in_case_qty":
        my_replen_method = "in_layer_qty"
        my_replen_qty = ensure_multiple(my_replen_qty, ti_value)

    if disable_individual_case_replenishment == "Yes" and  my_replen_method == "in_case_qty":
        my_replen_method = "in_layer_qty"
        my_replen_qty = ensure_multiple(my_replen_qty, ti_value)
        
    if disable_layer_replenishment == "Yes" and  my_replen_method == "in_layer_qty":
        my_replen_method = "in_pallet_qty"
        my_replen_qty = ensure_multiple(my_replen_qty, cpp)
        
    if roundup_to_full_tray_qty == "Yes" and  my_replen_method == "in_case_qty":
        my_replen_qty = ensure_multiple(my_replen_qty, inners_per_outer_value)

    if my_replen_method == "in_pallet_qty":
        my_replen_qty = ensure_multiple(my_replen_qty, cpp)
        
    elif my_replen_method == "in_layer_qty":
        my_replen_qty = ensure_multiple(my_replen_qty, ti_value)
        
    else:
        my_replen_qty = ensure_multiple(my_replen_qty, 1)

    df.at[index, 'pallet_consumption_method'] 		= my_replen_method
    df.at[index, 'case_replenishment_qty'] 	= my_replen_qty

replen_sum_of_rows = 0
replen_sum_of_cases = 0
replen_sum_of_trays = 0

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = "Replenishment:"

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = "In Case QTY:"
new_df = df[df['pallet_consumption_method'] == 'in_case_qty']
df_copy = new_df.copy(deep=True)
df_copy['cases_as_trays'] = df_copy[case_qty_column_name] / df_copy[inners_per_outer_column_name]
local_cases_as_trays = df_copy["cases_as_trays"].sum()
plot_df_0.at[plot_df_0_i, "1"] = format_float_with_commas(len(df_copy), 0)
plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(df_copy[case_qty_column_name].sum(), 2)
plot_df_0.at[plot_df_0_i, "3"] = format_float_with_commas((df_copy[case_qty_column_name].sum() / my_total_cases)*100,2) + "%"
plot_df_0.at[plot_df_0_i, "4"] = format_float_with_commas(local_cases_as_trays, 2)
plot_df_0.at[plot_df_0_i, "5"] = format_float_with_commas((local_cases_as_trays / my_total_cases_as_trays)*100,2) + "%"
replen_sum_of_rows = replen_sum_of_rows + len(df_copy)
replen_sum_of_cases = replen_sum_of_cases + df_copy[case_qty_column_name].sum()
replen_sum_of_trays = replen_sum_of_trays + local_cases_as_trays

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = "In Layer QTY:"
new_df = df[df['pallet_consumption_method'] == 'in_layer_qty']
df_copy = new_df.copy(deep=True)
df_copy['cases_as_trays'] = df_copy[case_qty_column_name] / df_copy[inners_per_outer_column_name]
local_cases_as_trays = df_copy["cases_as_trays"].sum()
plot_df_0.at[plot_df_0_i, "1"] = format_float_with_commas(len(df_copy), 0)
plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(df_copy[case_qty_column_name].sum(), 2)
plot_df_0.at[plot_df_0_i, "3"] = format_float_with_commas((df_copy[case_qty_column_name].sum() / my_total_cases)*100,2) + "%"
plot_df_0.at[plot_df_0_i, "4"] = format_float_with_commas(local_cases_as_trays, 2)
plot_df_0.at[plot_df_0_i, "5"] = format_float_with_commas((local_cases_as_trays / my_total_cases_as_trays)*100,2) + "%"
replen_sum_of_rows = replen_sum_of_rows + len(df_copy)
replen_sum_of_cases = replen_sum_of_cases + df_copy[case_qty_column_name].sum()
replen_sum_of_trays = replen_sum_of_trays + local_cases_as_trays

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = "In Pallet QTY:"
new_df = df[df['pallet_consumption_method'] == 'in_pallet_qty']
df_copy = new_df.copy(deep=True)
df_copy['cases_as_trays'] = df_copy[case_qty_column_name] / df_copy[inners_per_outer_column_name]
local_cases_as_trays = df_copy["cases_as_trays"].sum()
plot_df_0.at[plot_df_0_i, "1"] = format_float_with_commas(len(df_copy), 0)
plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(df_copy[case_qty_column_name].sum(), 2)
plot_df_0.at[plot_df_0_i, "3"] = format_float_with_commas((df_copy[case_qty_column_name].sum() / my_total_cases)*100,2) + "%"
plot_df_0.at[plot_df_0_i, "4"] = format_float_with_commas(local_cases_as_trays, 2)
plot_df_0.at[plot_df_0_i, "5"] = format_float_with_commas((local_cases_as_trays / my_total_cases_as_trays)*100,2) + "%"
replen_sum_of_rows = replen_sum_of_rows + len(df_copy)
replen_sum_of_cases = replen_sum_of_cases + df_copy[case_qty_column_name].sum()
replen_sum_of_trays = replen_sum_of_trays + local_cases_as_trays

plot_df_0_i = plot_df_0_i + 1
plot_df_0.at[plot_df_0_i, "0"] = "Sum:"
plot_df_0.at[plot_df_0_i, "1"] = format_float_with_commas(replen_sum_of_rows, 0)

plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(replen_sum_of_cases, 2)
plot_df_0.at[plot_df_0_i, "3"] = format_float_with_commas((replen_sum_of_cases / my_total_cases)*100,2) + "%"

plot_df_0.at[plot_df_0_i, "4"] = format_float_with_commas(replen_sum_of_trays, 2)
plot_df_0.at[plot_df_0_i, "5"] = format_float_with_commas((replen_sum_of_trays / my_total_cases_as_trays)*100,2) + "%"

plot_df_0 = plot_df_0.fillna('')
plot_df_0 = plot_df_0.rename(columns={'0': 'Name', '1': 'Rows', '2': 'Cases As Cases', '3': '%_', '4': 'Converted to Trays/Totes', '5': '%__'})

return df, plot_df_0
