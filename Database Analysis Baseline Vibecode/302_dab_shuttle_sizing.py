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
my_variables_df = input_2.to_pandas()

df = df.reset_index(drop=True)
my_variables_df = my_variables_df.reset_index(drop=True)



case_qty_column_name 						= self.case_qty_column_name
case_qty_mean_column_name 					= self.case_qty_mean_column_name
cases_per_tray_column_name 					= self.inners_per_outer_column_name

tray_size_column_name 						= self.tray_size_column_name
replenishment_case_qty_column_name 			= self.single_replen_case_qty_column_name

max_aisle_rate 								= self.max_aisle_rate_tray_qty
tray_multiplicity_per_aisle					= self.tote_multiplicity

shuttle_depletion_hours 						= my_variables_df.at[0, 'shuttle_depletion_hours']
shuttle_replenishment_hours 					= my_variables_df.at[0, 'shuttle_replenishment_hours']
shuttle_surge_factor							= my_variables_df.at[0, 'shuttle_surge_factor']

df_copy = df.copy(deep=True)

input_row_count = len(df_copy)

df_pure = pd.DataFrame(df_copy.to_dict())
unique_input_row_count = df_pure.drop_duplicates().shape[0]

df_copy["orderlines_per_day"] = 0.0
df_copy["single_retrieval_tray_consumption"] = 0.0
df_copy["daily_tray_retrievals"] = 0.0
df_copy["daily_tray_consumption"] = 0.0
df_copy["daily_tray_residuals"] = 0.0

df_copy["daily_tray_replenishment"] = 0.0


for index, row in df_copy.iterrows():
    case_qty_value 												= row[case_qty_column_name]
    case_qty_mean_value 										= row[case_qty_mean_column_name]
    cases_per_tray_value 										= row[cases_per_tray_column_name]
    tray_size_value												= row[tray_size_column_name]
    replenishment_case_qty_value 								= row[replenishment_case_qty_column_name]
    
    df_copy.at[index, 'orderlines_per_day'] 					= case_qty_value / case_qty_mean_value
    df_copy.at[index, 'single_retrieval_tray_consumption'] 		= case_qty_mean_value / cases_per_tray_value
    
    if cases_per_tray_value == 1:
        df_copy.at[index, 'daily_tray_retrievals'] 			    = df_copy.at[index, 'orderlines_per_day'] * df_copy.at[index, 'single_retrieval_tray_consumption']
    else:
        df_copy.at[index, 'daily_tray_retrievals'] 				= df_copy.at[index, 'orderlines_per_day'] * math.ceil(df_copy.at[index, 'single_retrieval_tray_consumption'])
        
    df_copy.at[index, 'daily_tray_consumption'] 				= df_copy.at[index, 'orderlines_per_day'] * df_copy.at[index, 'single_retrieval_tray_consumption']
    df_copy.at[index, 'daily_tray_residuals'] 					= max(df_copy.at[index, 'daily_tray_retrievals'] - df_copy.at[index, 'daily_tray_consumption'],0)
    df_copy.at[index, 'daily_tray_replenishment'] 				= df_copy.at[index, 'daily_tray_consumption']
    
    df_copy.at[index, 'daily_case_consumption'] 				= df_copy.at[index, 'daily_tray_consumption'] * cases_per_tray_value
    df_copy.at[index, 'daily_case_replenishment'] 				= df_copy.at[index, 'daily_case_consumption']
    
    
    df_copy.at[index, 'daily_case_retrievals'] 					= df_copy.at[index, 'daily_tray_retrievals'] * cases_per_tray_value
    df_copy.at[index, 'daily_case_residuals'] 					= max(df_copy.at[index, 'daily_case_retrievals'] - df_copy.at[index, 'daily_case_consumption'],0)
    


total_daily_case_retrievals										= df_copy["daily_case_retrievals"].sum()
total_daily_case_consumption									= df_copy["daily_case_consumption"].sum()
total_daily_case_residuals										= df_copy["daily_case_residuals"].sum()
total_daily_case_replenishment									= df_copy["daily_case_replenishment"].sum()

total_daily_tray_retrievals										= df_copy["daily_tray_retrievals"].sum()
total_daily_tray_consumption									= df_copy["daily_tray_consumption"].sum()
total_daily_tray_residuals										= df_copy["daily_tray_residuals"].sum()
total_daily_tray_replenishment									= df_copy["daily_tray_replenishment"].sum()



total_hourly_tray_retrievals									= total_daily_tray_retrievals 				/ shuttle_depletion_hours
total_hourly_tray_consumption									= total_daily_tray_consumption 				/ shuttle_depletion_hours
total_hourly_tray_residuals										= total_daily_tray_residuals 				/ shuttle_depletion_hours
total_hourly_tray_replenishment									= total_daily_tray_replenishment 			/ shuttle_replenishment_hours

total_hourly_shuttle_out 											= total_hourly_tray_retrievals
total_hourly_shuttle_in 											= total_hourly_tray_residuals + total_hourly_tray_replenishment


# Surged:
surged_total_daily_tray_retrievals								= total_daily_tray_retrievals				* shuttle_surge_factor
surged_total_daily_tray_consumption								= total_daily_tray_consumption				* shuttle_surge_factor
surged_total_daily_tray_residuals 								= total_daily_tray_residuals				* shuttle_surge_factor
surged_total_daily_tray_replenishment							= total_daily_tray_replenishment			* shuttle_surge_factor

surged_total_hourly_tray_retrievals								= total_hourly_tray_retrievals				* shuttle_surge_factor
surged_total_hourly_tray_consumption							= total_hourly_tray_consumption				* shuttle_surge_factor
surged_total_hourly_tray_residuals								= total_hourly_tray_residuals				* shuttle_surge_factor
surged_total_hourly_tray_replenishment							= total_hourly_tray_replenishment			* shuttle_surge_factor

surged_total_hourly_shuttle_out										= total_hourly_shuttle_out 						* shuttle_surge_factor
surged_total_hourly_shuttle_in										= total_hourly_shuttle_in 						* shuttle_surge_factor

surged_min_aisles_out 											= math.ceil(surged_total_hourly_shuttle_out 	/ max_aisle_rate)
surged_min_aisles_in 											= math.ceil(surged_total_hourly_shuttle_in 		/ max_aisle_rate)

min_asiles 														= max(surged_min_aisles_out, surged_min_aisles_in)

multiplicity_tray_count 										= math.ceil(min_asiles * tray_multiplicity_per_aisle)

df_copy["multiplicity_tray_count"] = multiplicity_tray_count

df_copy["cases_in_multiplicity_trays"] = 0
df_copy["additional_storage_trays"] = 0
df_copy["total_stored_trays"] = 0
df_copy["large_location_equivalents"] = 0.0
df_copy["total_stored_cases"] = 0

large_tray_sum = 0
small_tray_sum = 0


for index, row in df_copy.iterrows():
    
    
    case_qty_value 							= row[case_qty_column_name]
    case_qty_mean_value 					= row[case_qty_mean_column_name]
    cases_per_tray_value 					= row[cases_per_tray_column_name]
    tray_size_value							= row[tray_size_column_name]
    replenishment_case_qty_value 			= row[replenishment_case_qty_column_name]
    
    in_shuttle_case_qty_value = replenishment_case_qty_value / 2 
    
    
    df_copy.at[index, 'cases_in_multiplicity_trays'] 		= multiplicity_tray_count * max(math.floor(cases_per_tray_value/2),1)
    df_copy.at[index, 'additional_storage_trays'] 			= max(in_shuttle_case_qty_value - df_copy.at[index, 'cases_in_multiplicity_trays'], 0)
    df_copy.at[index, "total_stored_trays"] 							= multiplicity_tray_count + df_copy.at[index, 'additional_storage_trays']
    
    if tray_size_value == "Small":
        df_copy.at[index, "large_location_equivalents"] 			= df_copy.at[index, "total_stored_trays"] / 2
        small_tray_sum 												= small_tray_sum + df_copy.at[index, "total_stored_trays"]
    else:
        df_copy.at[index, "large_location_equivalents"] 			= df_copy.at[index, "total_stored_trays"]
        large_tray_sum 												= large_tray_sum + df_copy.at[index, "total_stored_trays"]
    
    df_copy.at[index, "total_stored_cases"] 						= df_copy.at[index, 'cases_in_multiplicity_trays'] + df_copy.at[index, 'additional_storage_trays'] * cases_per_tray_value
    
surged_inbound_elevator_rate_requirement 		= surged_total_hourly_shuttle_in / min_asiles
surged_outbount_elevator_rate_requirement 		= surged_total_hourly_shuttle_out / min_asiles

total_stored_cases_sum 					= df_copy["total_stored_cases"].sum()

total_stored_trays_sum 					= df_copy["total_stored_trays"].sum()

procent_of_small_trays 					= small_tray_sum / (small_tray_sum + large_tray_sum)
mean_cases_per_tray 					= total_stored_trays_sum / total_stored_cases_sum

large_location_equivalents_sum 			= df_copy["large_location_equivalents"].sum()

large_location_equivalents_per_aisle 	= large_location_equivalents_sum / min_asiles

trays_per_aisle 						= total_stored_trays_sum / min_asiles

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
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "Inputs:"
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "shuttle_replenishment_hours"
df_out.at[i, 'value'] 				= str(format_float_with_commas(shuttle_replenishment_hours,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "shuttle_depletion_hours"
df_out.at[i, 'value'] 				= str(format_float_with_commas(shuttle_depletion_hours,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "max_aisle_rate"
df_out.at[i, 'value'] 				= str(format_float_with_commas(max_aisle_rate,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "tray_multiplicity_per_aisle"
df_out.at[i, 'value'] 				= str(format_float_with_commas(tray_multiplicity_per_aisle,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Input"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "shuttle_surge_factor"
df_out.at[i, 'value'] 				= str(format_float_with_commas(shuttle_surge_factor,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "Outputs (Rate):"
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_tray_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_tray_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_tray_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_tray_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_tray_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_tray_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_tray_replenishment"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_tray_replenishment,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_case_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_case_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_case_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_case_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_case_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_case_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_daily_case_replenishment"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_daily_case_replenishment,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_hourly_tray_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_hourly_tray_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_hourly_tray_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_hourly_tray_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_hourly_tray_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_hourly_tray_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_hourly_tray_replenishment"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_hourly_tray_replenishment,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_hourly_shuttle_in"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_hourly_shuttle_in,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_hourly_shuttle_out"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_hourly_shuttle_out,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_total_daily_tray_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_daily_tray_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_total_daily_tray_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_daily_tray_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_total_daily_tray_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_daily_tray_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "surged_total_daily_tray_replenishment"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_daily_tray_replenishment,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_total_hourly_tray_retrievals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_hourly_tray_retrievals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_total_hourly_tray_residuals"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_hourly_tray_residuals,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_total_hourly_tray_consumption"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_hourly_tray_consumption,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_total_hourly_tray_replenishment"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_hourly_tray_replenishment,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_total_hourly_shuttle_in"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_hourly_shuttle_in,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_total_hourly_shuttle_out"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_total_hourly_shuttle_out,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "min_asiles"
df_out.at[i, 'value'] 				= str(format_float_with_commas(min_asiles,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_inbound_elevator_rate_requirement"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_inbound_elevator_rate_requirement,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "surged_outbount_elevator_rate_requirement"
df_out.at[i, 'value'] 				= str(format_float_with_commas(surged_outbount_elevator_rate_requirement,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "Outputs (Storage):"
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "total_stored_cases_sum"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_stored_cases_sum,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "large_tray_sum"
df_out.at[i, 'value'] 				= str(format_float_with_commas(large_tray_sum,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "small_tray_sum"
df_out.at[i, 'value'] 				= str(format_float_with_commas(small_tray_sum,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "total_stored_trays_sum"
df_out.at[i, 'value'] 				= str(format_float_with_commas(total_stored_trays_sum,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "procent_of_small_trays"
df_out.at[i, 'value'] 				= str(format_float_with_commas(procent_of_small_trays,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "mean_cases_per_tray"
df_out.at[i, 'value'] 				= str(format_float_with_commas(mean_cases_per_tray,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "large_location_equivalents_sum"
df_out.at[i, 'value'] 				= str(format_float_with_commas(large_location_equivalents_sum,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= "----->"
df_out.at[i, 'heading'] 			= "large_location_equivalents_per_aisle"
df_out.at[i, 'value'] 				= str(format_float_with_commas(large_location_equivalents_per_aisle,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Output"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "trays_per_aisle"
df_out.at[i, 'value'] 				= str(format_float_with_commas(trays_per_aisle,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Sense-Check"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "input_row_count"
df_out.at[i, 'value'] 				= str(format_float_with_commas(input_row_count,2))
i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= "Sense-Check"
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= "unique_input_row_count"
df_out.at[i, 'value'] 				= str(format_float_with_commas(unique_input_row_count,2))

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""

i = i+1
df_out.at[i, "0"] 					= ""
df_out.at[i, "report_group"] 		= "Shuttle Sizing"
df_out.at[i, 'input_or_output'] 	= ""
df_out.at[i, 'marker'] 				= ""
df_out.at[i, 'heading'] 			= ""
df_out.at[i, 'value'] 				= ""
        
return df_out, df_copy
