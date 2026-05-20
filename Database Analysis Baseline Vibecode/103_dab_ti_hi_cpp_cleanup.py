import pandas as pd
from category import data_cleanup_category

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
        
def dab_ipo_fx_patterns_dual_uniform(my_parameters, all_solutions):
    
    dab_ipo_parameter_multiple_layers                    = my_parameters["dab_ipo_parameter_multiple_layers"]
    dab_ipo_parameter_gap_from_outer_lengthwise          = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise           = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
    
    dab_ipo_parameter_gap_between_inners_lengthwise      = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    dab_ipo_parameter_gap_between_inners_widthwise       = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
    
    dab_ipo_parameter_outer_length                       = my_parameters["dab_ipo_parameter_outer_length"]
    dab_ipo_parameter_outer_width                        = my_parameters["dab_ipo_parameter_outer_width"]
    dab_ipo_parameter_outer_height                       = my_parameters["dab_ipo_parameter_outer_height"]
    dab_ipo_parameter_outer_weight                       = my_parameters["dab_ipo_parameter_outer_weight"]
    dab_ipo_parameter_outer_volume_utilisation           = my_parameters["dab_ipo_parameter_outer_volume_utilisation"]
    dab_ipo_parameter_max_inner_count                    = my_parameters["dab_ipo_parameter_max_inner_count"]
    dab_ipo_parameter_top_layer_full                     = my_parameters["dab_ipo_parameter_top_layer_full"]
    dab_ipo_parameter_inner_length                       = my_parameters["dab_ipo_parameter_inner_length"]
    dab_ipo_parameter_inner_width                        = my_parameters["dab_ipo_parameter_inner_width"]
    dab_ipo_parameter_inner_height                       = my_parameters["dab_ipo_parameter_inner_height"]
    dab_ipo_parameter_inner_weight                       = my_parameters["dab_ipo_parameter_inner_weight"]

    outer_length        								 = dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise*2
    outer_width         								 = dab_ipo_parameter_outer_width -dab_ipo_parameter_gap_from_outer_widthwise*2
    outer_height        								 = dab_ipo_parameter_outer_height
    outer_weight        								 = dab_ipo_parameter_outer_weight

    inner_length    									 = dab_ipo_parameter_inner_length
    inner_width     									 = dab_ipo_parameter_inner_width
    inner_height    									 = dab_ipo_parameter_inner_height
    inner_weight    									 = dab_ipo_parameter_inner_weight
    
    
    max_inner_count_weight      = math.floor((outer_weight + 0.0001) / inner_weight)
    max_inner_count             = min([dab_ipo_parameter_max_inner_count, max_inner_count_weight])

    max_inner_count_length  = math.floor((outer_length + dab_ipo_parameter_gap_between_inners_lengthwise + 0.0001) / (inner_length + dab_ipo_parameter_gap_between_inners_lengthwise))
    max_inner_count_width   = math.floor((outer_width + dab_ipo_parameter_gap_between_inners_widthwise + 0.0001) / (inner_width + dab_ipo_parameter_gap_between_inners_widthwise))
    
    my_new_max_inner_count1 = max_inner_count_length * max_inner_count_width
    my_new_max_inner_count1_length = max_inner_count_length

    if max_inner_count_length > 0 and max_inner_count_width > 0:

        max_inner_count_area_array = []

        for i in range(0, max_inner_count_length+1):
            remaining_length = dab_ipo_parameter_outer_length - (dab_ipo_parameter_inner_length + dab_ipo_parameter_gap_between_inners_lengthwise )*i
            
            
            current_inner_count = i * max_inner_count_width
            new_my_parameters = copy.deepcopy(my_parameters)
            new_my_parameters["dab_ipo_parameter_outer_length"] = remaining_length
            new_my_parameters["dab_ipo_parameter_inner_length"] = my_parameters["dab_ipo_parameter_inner_width"]
            new_my_parameters["dab_ipo_parameter_inner_width"] = my_parameters["dab_ipo_parameter_inner_length"]
            new_all_solutions = copy.deepcopy(all_solutions)
            new_all_solutions = dab_ipo_fx_patterns_uniform(new_my_parameters, new_all_solutions)
            remaining_uniform_count = new_all_solutions["ti_array"][len(new_all_solutions["ti_array"])-1]

            current_inner_count = current_inner_count + remaining_uniform_count
            max_inner_count_area_array.append(current_inner_count)
            
            if my_new_max_inner_count1 < current_inner_count:
                my_new_max_inner_count1 = current_inner_count
                my_new_max_inner_count1_length = i
            

        max_ti = max(max_inner_count_area_array)
        ti = max_ti
    else:
        ti = 0
        
        
    if ti == 0:
    
        max_inner_count_area_array = []
        new_my_parameters = copy.deepcopy(my_parameters)
        new_my_parameters["dab_ipo_parameter_inner_length"] = my_parameters["dab_ipo_parameter_inner_width"]
        new_my_parameters["dab_ipo_parameter_inner_width"] = my_parameters["dab_ipo_parameter_inner_length"]
        new_all_solutions = copy.deepcopy(all_solutions)
        new_all_solutions = dab_ipo_fx_patterns_uniform(new_my_parameters, new_all_solutions)
        remaining_uniform_count = new_all_solutions["ti_array"][len(new_all_solutions["ti_array"])-1]



        current_inner_count = remaining_uniform_count
        max_inner_count_area_array.append(current_inner_count)
        
        max_ti = max(max_inner_count_area_array)
        ti = max_ti
    
    
    plot_json = {}
    plot_json["min_x_array"] = [0, dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["min_y_array"] = [0, dab_ipo_parameter_gap_from_outer_widthwise]
    plot_json["max_x_array"] = [dab_ipo_parameter_outer_length, dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["max_y_array"] = [dab_ipo_parameter_outer_width, dab_ipo_parameter_outer_width - dab_ipo_parameter_gap_from_outer_widthwise]
    
    for i in range(0,my_new_max_inner_count1_length):
        for j in range(0,max_inner_count_width):
            plot_json["min_x_array"].append(dab_ipo_parameter_gap_from_outer_lengthwise + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_length)*i)
            plot_json["min_y_array"].append(dab_ipo_parameter_gap_from_outer_widthwise + (dab_ipo_parameter_gap_between_inners_widthwise + dab_ipo_parameter_inner_width)*j)
            plot_json["max_x_array"].append(dab_ipo_parameter_gap_from_outer_lengthwise + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_length)*i + dab_ipo_parameter_inner_length)
            plot_json["max_y_array"].append(dab_ipo_parameter_gap_from_outer_widthwise + (dab_ipo_parameter_gap_between_inners_widthwise + dab_ipo_parameter_inner_width)*j + dab_ipo_parameter_inner_width)
    
    remaining_length = (dab_ipo_parameter_outer_length - (dab_ipo_parameter_inner_length + dab_ipo_parameter_gap_between_inners_lengthwise )*my_new_max_inner_count1_length)- dab_ipo_parameter_gap_from_outer_lengthwise*2
    
    second_max_inner_count_length  = math.floor((remaining_length + dab_ipo_parameter_gap_between_inners_lengthwise + 0.0001) / (inner_width + dab_ipo_parameter_gap_between_inners_lengthwise))
    
    second_max_inner_count_width   = math.floor((outer_width + dab_ipo_parameter_gap_between_inners_widthwise + 0.0001) / (inner_length + dab_ipo_parameter_gap_between_inners_widthwise))
    
    start_x = dab_ipo_parameter_gap_from_outer_lengthwise + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_length)*my_new_max_inner_count1_length
    start_y = dab_ipo_parameter_gap_from_outer_widthwise
    
    
    for i in range(0,second_max_inner_count_length):
        for j in range(0,second_max_inner_count_width):
            plot_json["min_x_array"].append(start_x + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_width)*i)
            plot_json["min_y_array"].append(start_y + (dab_ipo_parameter_gap_between_inners_widthwise + dab_ipo_parameter_inner_length)*j)
            plot_json["max_x_array"].append(start_x + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_width)*i + dab_ipo_parameter_inner_width)
            plot_json["max_y_array"].append(start_y + (dab_ipo_parameter_gap_between_inners_widthwise + dab_ipo_parameter_inner_length)*j + dab_ipo_parameter_inner_length)
    
    
    
    
    
    
    
    all_solutions["plot_json_array"].append(json.dumps(plot_json))
    all_solutions["ti_array"].append(ti)
    
    
    return all_solutions

def dab_ipo_fx_patterns_uniform(my_parameters, all_solutions):
    
    dab_ipo_parameter_multiple_layers                    = my_parameters["dab_ipo_parameter_multiple_layers"]
    dab_ipo_parameter_gap_from_outer_lengthwise          = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise           = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
        
    dab_ipo_parameter_gap_between_inners_lengthwise      = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    dab_ipo_parameter_gap_between_inners_widthwise       = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]


    dab_ipo_parameter_outer_length                       = my_parameters["dab_ipo_parameter_outer_length"]
    dab_ipo_parameter_outer_width                        = my_parameters["dab_ipo_parameter_outer_width"]
    dab_ipo_parameter_outer_height                       = my_parameters["dab_ipo_parameter_outer_height"]
    dab_ipo_parameter_outer_weight                       = my_parameters["dab_ipo_parameter_outer_weight"]
    dab_ipo_parameter_outer_volume_utilisation            		= my_parameters["dab_ipo_parameter_outer_volume_utilisation"]
    dab_ipo_parameter_max_inner_count                    = my_parameters["dab_ipo_parameter_max_inner_count"]
    dab_ipo_parameter_top_layer_full                     = my_parameters["dab_ipo_parameter_top_layer_full"]
    dab_ipo_parameter_inner_length                       = my_parameters["dab_ipo_parameter_inner_length"]
    dab_ipo_parameter_inner_width                        = my_parameters["dab_ipo_parameter_inner_width"]
    dab_ipo_parameter_inner_height                       = my_parameters["dab_ipo_parameter_inner_height"]
    dab_ipo_parameter_inner_weight                       = my_parameters["dab_ipo_parameter_inner_weight"]

    outer_length        = dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise*2
    outer_width         = dab_ipo_parameter_outer_width -dab_ipo_parameter_gap_from_outer_widthwise*2
    outer_height        = dab_ipo_parameter_outer_height
    outer_weight        = dab_ipo_parameter_outer_weight

    inner_length    = dab_ipo_parameter_inner_length
    inner_width     = dab_ipo_parameter_inner_width
    inner_height    = dab_ipo_parameter_inner_height
    inner_weight    = dab_ipo_parameter_inner_weight
    
    
    max_inner_count_weight      = math.floor((outer_weight + 0.0001) / inner_weight)
    max_inner_count             = min([dab_ipo_parameter_max_inner_count, max_inner_count_weight])

    max_inner_count_length  = math.floor((outer_length + dab_ipo_parameter_gap_between_inners_lengthwise + 0.0001) / (inner_length + dab_ipo_parameter_gap_between_inners_lengthwise))
    max_inner_count_width   = math.floor((outer_width + dab_ipo_parameter_gap_between_inners_widthwise + 0.0001) / (inner_width + dab_ipo_parameter_gap_between_inners_widthwise))

    max_ti = max_inner_count_length * max_inner_count_width

    ti = max_ti
    
        
    plot_json = {}
    plot_json["min_x_array"] = [0, dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["min_y_array"] = [0, dab_ipo_parameter_gap_from_outer_widthwise]
    plot_json["max_x_array"] = [dab_ipo_parameter_outer_length, dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["max_y_array"] = [dab_ipo_parameter_outer_width, dab_ipo_parameter_outer_width - dab_ipo_parameter_gap_from_outer_widthwise]
    
    for i in range(0,max_inner_count_length):
        for j in range(0,max_inner_count_width):
            plot_json["min_x_array"].append(dab_ipo_parameter_gap_from_outer_lengthwise + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_length)*i)
            plot_json["min_y_array"].append(dab_ipo_parameter_gap_from_outer_widthwise + (dab_ipo_parameter_gap_between_inners_widthwise + dab_ipo_parameter_inner_width)*j)
            plot_json["max_x_array"].append(dab_ipo_parameter_gap_from_outer_lengthwise + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_length)*i + dab_ipo_parameter_inner_length)
            plot_json["max_y_array"].append(dab_ipo_parameter_gap_from_outer_widthwise + (dab_ipo_parameter_gap_between_inners_widthwise + dab_ipo_parameter_inner_width)*j + dab_ipo_parameter_inner_width)
    
    
    all_solutions["ti_array"].append(ti)
    all_solutions["plot_json_array"].append(json.dumps(plot_json))
    
    
    return all_solutions
def dab_ipo_fx_patterns_single_row(my_parameters, all_solutions):
    
    dab_ipo_parameter_multiple_layers                    = my_parameters["dab_ipo_parameter_multiple_layers"]
    
    dab_ipo_parameter_gap_from_outer_lengthwise          = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise           = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
        
    dab_ipo_parameter_gap_between_inners_lengthwise      = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    dab_ipo_parameter_gap_between_inners_widthwise       = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
    
    dab_ipo_parameter_outer_length                       = my_parameters["dab_ipo_parameter_outer_length"]
    dab_ipo_parameter_outer_width                        = my_parameters["dab_ipo_parameter_outer_width"]
    dab_ipo_parameter_outer_height                       = my_parameters["dab_ipo_parameter_outer_height"]
    dab_ipo_parameter_outer_weight                       = my_parameters["dab_ipo_parameter_outer_weight"]
    dab_ipo_parameter_outer_volume_utilisation            = my_parameters["dab_ipo_parameter_outer_volume_utilisation"]
    dab_ipo_parameter_max_inner_count                    = my_parameters["dab_ipo_parameter_max_inner_count"]
    dab_ipo_parameter_top_layer_full                     = my_parameters["dab_ipo_parameter_top_layer_full"]
    dab_ipo_parameter_inner_length                       = my_parameters["dab_ipo_parameter_inner_length"]
    dab_ipo_parameter_inner_width                        = my_parameters["dab_ipo_parameter_inner_width"]
    dab_ipo_parameter_inner_height                       = my_parameters["dab_ipo_parameter_inner_height"]
    dab_ipo_parameter_inner_weight                       = my_parameters["dab_ipo_parameter_inner_weight"]

    outer_length        = dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise*2
    outer_width         = dab_ipo_parameter_outer_width -dab_ipo_parameter_gap_from_outer_widthwise*2
    outer_height        = dab_ipo_parameter_outer_height
    outer_weight        = dab_ipo_parameter_outer_weight

    inner_length    = dab_ipo_parameter_inner_length
    inner_width     = dab_ipo_parameter_inner_width
    inner_height    = dab_ipo_parameter_inner_height
    inner_weight    = dab_ipo_parameter_inner_weight
    
    
    max_inner_count_weight      = math.floor((outer_weight + 0.0001) / inner_weight)
    max_inner_count             = min([dab_ipo_parameter_max_inner_count, max_inner_count_weight])


    max_inner_count_length  = math.floor((outer_length + dab_ipo_parameter_gap_between_inners_lengthwise + 0.0001) / (inner_length + dab_ipo_parameter_gap_between_inners_lengthwise))
    max_inner_count_width   = math.floor((outer_width + dab_ipo_parameter_gap_from_outer_widthwise + 0.0001) / (inner_width + dab_ipo_parameter_gap_from_outer_widthwise))
    
    max_inner_count_width = min([max_inner_count_width,1])
    max_ti = max_inner_count_length * max_inner_count_width
    
    ti = max_ti
    
    plot_json = {}
    plot_json["min_x_array"] = [0, dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["min_y_array"] = [0, dab_ipo_parameter_gap_from_outer_widthwise]
    plot_json["max_x_array"] = [dab_ipo_parameter_outer_length, dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["max_y_array"] = [dab_ipo_parameter_outer_width, dab_ipo_parameter_outer_width - dab_ipo_parameter_gap_from_outer_widthwise]
    
    for i in range(0,ti):
        plot_json["min_x_array"].append(dab_ipo_parameter_gap_from_outer_lengthwise + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_length)*i)
        plot_json["min_y_array"].append(dab_ipo_parameter_gap_from_outer_widthwise)
        plot_json["max_x_array"].append(dab_ipo_parameter_gap_from_outer_lengthwise + (dab_ipo_parameter_gap_between_inners_lengthwise + dab_ipo_parameter_inner_length)*i + dab_ipo_parameter_inner_length)
        plot_json["max_y_array"].append(dab_ipo_parameter_gap_from_outer_widthwise + dab_ipo_parameter_inner_width)
    
    all_solutions["ti_array"].append(ti)
    all_solutions["plot_json_array"].append(json.dumps(plot_json))
    
    return all_solutions

def dab_ipo_fx_patterns_single_case(my_parameters, all_solutions):

    dab_ipo_parameter_gap_from_outer_lengthwise          = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise           = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]

    dab_ipo_parameter_outer_length                       = my_parameters["dab_ipo_parameter_outer_length"]
    dab_ipo_parameter_outer_width                        = my_parameters["dab_ipo_parameter_outer_width"]
    dab_ipo_parameter_outer_height                       = my_parameters["dab_ipo_parameter_outer_height"]
    dab_ipo_parameter_outer_weight                       = my_parameters["dab_ipo_parameter_outer_weight"]

    dab_ipo_parameter_inner_length                       = my_parameters["dab_ipo_parameter_inner_length"]
    dab_ipo_parameter_inner_width                        = my_parameters["dab_ipo_parameter_inner_width"]
    dab_ipo_parameter_inner_height                       = my_parameters["dab_ipo_parameter_inner_height"]
    dab_ipo_parameter_inner_weight                       = my_parameters["dab_ipo_parameter_inner_weight"]

    fits = 1

    if (dab_ipo_parameter_inner_length) > (dab_ipo_parameter_outer_length - (2 * dab_ipo_parameter_gap_from_outer_lengthwise)):
        fits = 0
    if (dab_ipo_parameter_inner_width) > (dab_ipo_parameter_outer_width - (2 * dab_ipo_parameter_gap_from_outer_widthwise)):
        fits = 0
        
    if (dab_ipo_parameter_inner_height) > (dab_ipo_parameter_outer_height):
        fits = 0
        
    if (dab_ipo_parameter_inner_weight) > (dab_ipo_parameter_outer_weight):
        fits = 0
        
    
    ti = round(1.0)
    
    hi = round(1.0)
    inners_per_outer = round(1.0)
    
    if fits == 0:
        ti = 0
        
        hi = 0
        inners_per_outer = 0
    
    plot_json = {}
    plot_json["min_x_array"] = [0, dab_ipo_parameter_gap_from_outer_lengthwise, dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["min_y_array"] = [0, dab_ipo_parameter_gap_from_outer_widthwise, dab_ipo_parameter_gap_from_outer_widthwise]
    plot_json["max_x_array"] = [dab_ipo_parameter_outer_length, dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise, dab_ipo_parameter_inner_length]
    plot_json["max_y_array"] = [dab_ipo_parameter_outer_width, dab_ipo_parameter_outer_width - dab_ipo_parameter_gap_from_outer_widthwise, dab_ipo_parameter_inner_width]
    
    
    all_solutions["ti_array"].append(ti)
    all_solutions["plot_json_array"].append(json.dumps(plot_json))
    

    return all_solutions


def dab_ipo_fx_not_in_contour(pt_x, pt_y, c_minx, c_miny, c_maxx, c_maxy):
    not_in_contour = 1
    if (c_minx + 0.0001 < pt_x) and (pt_x < c_maxx - 0.0001) and (c_miny + 0.0001 < pt_y) and (pt_y < c_maxy - 0.0001):
        not_in_contour = 0
    return not_in_contour
def dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y):
    if (a1_x < b1_x ) and (b1_x < a2_x ) and (b1_y < a1_y ) and (a1_y < b2_y ):
        return 1
    else:
        return 0
def dab_ipo_fx_check_space(start_pt_x, start_pt_y, my_cl_parameters):

    outer_min_x = my_cl_parameters["my_space"][1][0]
    outer_min_y = my_cl_parameters["my_space"][1][1]
    outer_max_x = my_cl_parameters["my_space"][1][2]
    outer_max_y = my_cl_parameters["my_space"][1][3]

    inner_min_x = start_pt_x
    inner_min_y = start_pt_y
    inner_max_x = inner_min_x + my_cl_parameters["inner_length"]
    inner_max_y = inner_min_y + my_cl_parameters["inner_width"]

    fits = 1

    if inner_max_x > outer_max_x + 0.0001:
        fits = 0

    if inner_max_y > outer_max_y + 0.0001:
        fits = 0

    if inner_min_x < outer_min_x - 0.0001:
        fits = 0

    if inner_min_y < outer_min_y - 0.0001:
        fits = 0
    
    gapped_inner_min_x = inner_min_x - my_cl_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    gapped_inner_min_y = inner_min_y - my_cl_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
    gapped_inner_max_x = inner_max_x + my_cl_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    gapped_inner_max_y = inner_max_y + my_cl_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]

    for i in range(2,len(my_cl_parameters["my_space"])):
        
        btc_min_x = my_cl_parameters["my_space"][i][0]
        btc_min_y = my_cl_parameters["my_space"][i][1]
        btc_max_x = my_cl_parameters["my_space"][i][2]
        btc_max_y = my_cl_parameters["my_space"][i][3]
        
        if dab_ipo_fx_not_in_contour(btc_min_x, btc_min_y, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        if dab_ipo_fx_not_in_contour(btc_max_x, btc_min_y, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        if dab_ipo_fx_not_in_contour(btc_max_x, btc_max_y, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        if dab_ipo_fx_not_in_contour(btc_min_x, btc_max_y, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        
        if dab_ipo_fx_not_in_contour((btc_min_x + btc_max_x)/2, (btc_min_y + btc_max_y)/2, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        
        if dab_ipo_fx_not_in_contour((btc_min_x + btc_max_x) / 2, btc_min_y, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        if dab_ipo_fx_not_in_contour((btc_min_x + btc_max_x) / 2, btc_max_y, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        if dab_ipo_fx_not_in_contour(btc_min_x, (btc_min_y + btc_max_y) / 2, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        if dab_ipo_fx_not_in_contour(btc_max_x, (btc_min_y + btc_max_y) / 2, gapped_inner_min_x, gapped_inner_min_y, gapped_inner_max_x, gapped_inner_max_y) == 0:
            fits = 0
        
        btc_gapped_inner_min_x = btc_min_x - my_cl_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
        btc_gapped_inner_min_y = btc_min_y - my_cl_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
        btc_gapped_inner_max_x = btc_max_x + my_cl_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
        btc_gapped_inner_max_y = btc_max_y + my_cl_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
        
        a1_x = inner_min_x
        a1_y = inner_min_y
        a2_x = inner_max_x
        a2_y = inner_min_y
        b1_x = btc_min_x
        b1_y = btc_min_y
        b2_x = btc_min_x
        b2_y = btc_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
        
        a1_x = inner_min_x
        a1_y = inner_min_y
        a2_x = inner_max_x
        a2_y = inner_min_y
        b1_x = btc_max_x
        b1_y = btc_min_y
        b2_x = btc_max_x
        b2_y = btc_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
        
        a1_x = inner_min_x
        a1_y = inner_max_y
        a2_x = inner_max_x
        a2_y = inner_max_y
        b1_x = btc_min_x
        b1_y = btc_min_y
        b2_x = btc_min_x
        b2_y = btc_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
        
        a1_x = inner_min_x
        a1_y = inner_max_y
        a2_x = inner_max_x
        a2_y = inner_max_y
        b1_x = btc_max_x
        b1_y = btc_min_y
        b2_x = btc_max_x
        b2_y = btc_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
            
            
            
            
        #--------------------------------------------------------------------------------------------
            
            
            
        a1_x = btc_min_x
        a1_y = btc_min_y
        a2_x = btc_max_x
        a2_y = btc_min_y
        b1_x = inner_min_x
        b1_y = inner_min_y
        b2_x = inner_min_x
        b2_y = inner_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
        
        a1_x = btc_min_x
        a1_y = btc_min_y
        a2_x = btc_max_x
        a2_y = btc_min_y
        b1_x = inner_max_x
        b1_y = inner_min_y
        b2_x = inner_max_x
        b2_y = inner_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
        
        a1_x = btc_min_x
        a1_y = btc_max_y
        a2_x = btc_max_x
        a2_y = btc_max_y
        b1_x = inner_min_x
        b1_y = inner_min_y
        b2_x = inner_min_x
        b2_y = inner_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
        
        a1_x = btc_min_x
        a1_y = btc_max_y
        a2_x = btc_max_x
        a2_y = btc_max_y
        b1_x = inner_max_x
        b1_y = inner_min_y
        b2_x = inner_max_x
        b2_y = inner_max_y
        if dab_ipo_fx_perpendicular_lines_intersect(a1_x, a1_y, a2_x, a2_y, b1_x, b1_y, b2_x, b2_y) == 1:
            fits = 0
            
    return fits

def dab_ipo_fx_fill_up_space(start_pt_x, start_pt_y, my_cl_parameters):
    new_json_data = copy.deepcopy(my_cl_parameters)
    new_json_data["my_space"] = np.append(my_cl_parameters["my_space"], np.array([[start_pt_x,start_pt_y,start_pt_x + my_cl_parameters["inner_length"],start_pt_y + my_cl_parameters["inner_width"]]]), axis = 0)
    new_json_data["current_inner_count"] = my_cl_parameters["current_inner_count"] + 1

    return new_json_data

def dab_ipo_fx_empty_up_space(inner_index, my_cl_parameters):
    new_json_data = copy.deepcopy(my_cl_parameters)
    new_json_data["my_space"] = np.delete(my_cl_parameters["my_space"], inner_index, axis=0)
    new_json_data["current_inner_count"] = my_cl_parameters["current_inner_count"] - 1

    return new_json_data

def dab_ipo_fx_find_max_inner_count(my_cl_parameters):
    if my_cl_parameters["current_inner_count"] >= my_cl_parameters["max_allowed_inner_count"]:
        return my_cl_parameters
        
    this_dab_ipo_fx_inners_added = 0
    new_json_data = copy.deepcopy(my_cl_parameters)

    old_inner_counter = my_cl_parameters["current_inner_count"]

    if old_inner_counter == 0:
        start_pt_x = my_cl_parameters["my_space"][1][0]
        start_pt_y = my_cl_parameters["my_space"][1][1]
        fits = dab_ipo_fx_check_space(start_pt_x, start_pt_y, new_json_data)

        if fits == 1:
            new_json_data = dab_ipo_fx_fill_up_space(start_pt_x, start_pt_y, new_json_data)
            this_dab_ipo_fx_inners_added = this_dab_ipo_fx_inners_added + 1

    if new_json_data["current_inner_count"] >= new_json_data["max_allowed_inner_count"]:
        return new_json_data

    if len(new_json_data["my_space"]) > 2:
        
        im_done = 0
        inners_prior_loop = new_json_data["current_inner_count"]
        
        
        while im_done == 0:
            pts_array = np.empty((0, 2), float)
            for i in range(2,len(new_json_data["my_space"])):
                minx = new_json_data["my_space"][i][0]
                miny = new_json_data["my_space"][i][1]
                maxx = new_json_data["my_space"][i][2]
                maxy = new_json_data["my_space"][i][3]
                
                dab_ipo_parameter_gap_between_inners_lengthwise = new_json_data["dab_ipo_parameter_gap_between_inners_lengthwise"]
                dab_ipo_parameter_gap_between_inners_widthwise = new_json_data["dab_ipo_parameter_gap_between_inners_widthwise"]
                
                
                
                
                
                

                lw_delta = new_json_data["inner_width"] - new_json_data["inner_length"]
                if lw_delta < 0:
                    lw_delta = lw_delta * (-1)

                pts_array = np.append(pts_array, np.array([[maxx + dab_ipo_parameter_gap_between_inners_lengthwise,miny]]), axis = 0)
                pts_array = np.append(pts_array, np.array([[maxx + dab_ipo_parameter_gap_between_inners_lengthwise,miny - lw_delta]]), axis = 0)
                pts_array = np.append(pts_array, np.array([[minx,maxy + dab_ipo_parameter_gap_between_inners_widthwise]]), axis = 0)
            
            pts_array = pts_array[np.lexsort((pts_array[:, 1], pts_array[:, 0]))]
            

            for i in range(0, len(pts_array)):
                start_pt_x = pts_array[i][0]
                start_pt_y = pts_array[i][1]

                fits = dab_ipo_fx_check_space(start_pt_x, start_pt_y, new_json_data)

                if fits == 1:
                    new_json_data = dab_ipo_fx_fill_up_space(start_pt_x, start_pt_y, new_json_data)
                    this_dab_ipo_fx_inners_added = this_dab_ipo_fx_inners_added + 1
                    break
            
            if new_json_data["current_inner_count"] == inners_prior_loop:
                im_done = 1
            else:
                inners_prior_loop = new_json_data["current_inner_count"]
                
            if new_json_data["current_inner_count"] >= new_json_data["max_allowed_inner_count"]:
                return new_json_data

    if new_json_data["current_inner_count"] >= new_json_data["max_allowed_inner_count"]:
        return new_json_data

    if (old_inner_counter != new_json_data["current_inner_count"]) and (old_inner_counter+1 < new_json_data["current_inner_count"]):
        
        if this_dab_ipo_fx_inners_added > 0:
            new_json_data_2 = copy.deepcopy(new_json_data)
            inner_length = new_json_data_2["inner_length"]
            inner_width = new_json_data_2["inner_width"]
            new_json_data_2["inner_length"] = inner_width
            new_json_data_2["inner_width"] = inner_length
            

            for i in range(0,this_dab_ipo_fx_inners_added):
                
                new_json_data_3 = dab_ipo_fx_find_max_inner_count(new_json_data_2)

                if new_json_data_3["current_inner_count"] > new_json_data["current_inner_count"]:
                    new_json_data = new_json_data_3


                if new_json_data["current_inner_count"] >= new_json_data["max_allowed_inner_count"]:
                    return new_json_data

                inner_index = len(new_json_data_2["my_space"]) - 1
                new_json_data_2 = dab_ipo_fx_empty_up_space(inner_index, new_json_data_2)
        
    else:
        a = 0


    
    

    return new_json_data
def dab_ipo_fx_pattern_complex_ti(my_parameters):
    
    max_recursion_depth = min(my_parameters["dab_ipo_parameter_max_recursion_depth"], my_parameters["dab_ipo_parameter_max_inner_count"])
    
    
    dab_ipo_parameter_gap_from_outer_lengthwise          = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise           = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
        
    dab_ipo_parameter_gap_between_inners_lengthwise      = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    dab_ipo_parameter_gap_between_inners_widthwise       = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]

    outer_length = my_parameters["dab_ipo_parameter_outer_length"]
    outer_width = my_parameters["dab_ipo_parameter_outer_width"]
    
    inner_length = my_parameters["dab_ipo_parameter_inner_length"]
    inner_width = my_parameters["dab_ipo_parameter_inner_width"]
    
    my_cl_parameters = {}
    my_cl_parameters["inner_length"] = inner_length
    my_cl_parameters["inner_width"] = inner_width
    my_cl_parameters["outer_length"] = outer_length
    my_cl_parameters["outer_width"] = outer_width
    
    my_cl_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"] = dab_ipo_parameter_gap_from_outer_lengthwise
    my_cl_parameters["dab_ipo_parameter_gap_from_outer_widthwise"] = dab_ipo_parameter_gap_from_outer_widthwise
    my_cl_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"] = dab_ipo_parameter_gap_between_inners_lengthwise
    my_cl_parameters["dab_ipo_parameter_gap_between_inners_widthwise"] = dab_ipo_parameter_gap_between_inners_widthwise
    
    my_cl_parameters["my_space"] = np.empty((0, 4), float)
    my_cl_parameters["current_inner_count"] = 0

    outer_area_reduced = ((outer_length - dab_ipo_parameter_gap_from_outer_lengthwise  * 2 + dab_ipo_parameter_gap_between_inners_lengthwise)*(outer_width - dab_ipo_parameter_gap_from_outer_widthwise * 2 + dab_ipo_parameter_gap_between_inners_widthwise))
    inner_area_increased = ((inner_length + dab_ipo_parameter_gap_between_inners_lengthwise)*(inner_width + dab_ipo_parameter_gap_between_inners_widthwise))
    max_inners_by_area = math.floor(outer_area_reduced / inner_area_increased)
    
    my_cl_parameters["max_allowed_inner_count"] = min(max_inners_by_area, max_recursion_depth)

    my_cl_parameters["my_space"] = np.append(my_cl_parameters["my_space"], np.array([[0,0,outer_length,outer_width]]), axis = 0)
    my_cl_parameters["my_space"] = np.append(my_cl_parameters["my_space"], np.array([[dab_ipo_parameter_gap_from_outer_lengthwise,dab_ipo_parameter_gap_from_outer_widthwise,outer_length-dab_ipo_parameter_gap_from_outer_lengthwise,outer_width-dab_ipo_parameter_gap_from_outer_widthwise]]), axis = 0)

    new_cl_parameters = dab_ipo_fx_find_max_inner_count(my_cl_parameters)

    if (inner_length != inner_width) and (new_cl_parameters["current_inner_count"] < new_cl_parameters["max_allowed_inner_count"]):
        new_json_data_2 = copy.deepcopy(my_cl_parameters)
        new_json_data_2["inner_length"] = inner_width
        new_json_data_2["inner_width"] = inner_length
        
        new_cl_parameters_2 = dab_ipo_fx_find_max_inner_count(new_json_data_2)

        if new_cl_parameters["current_inner_count"] < new_cl_parameters_2["current_inner_count"]:
            new_cl_parameters = new_cl_parameters_2


    if (inner_length != inner_width) and (new_cl_parameters["current_inner_count"] < new_cl_parameters["max_allowed_inner_count"]):
        new_json_data_2 = copy.deepcopy(my_cl_parameters)
        new_json_data_2["inner_length"] = inner_length
        new_json_data_2["inner_width"] = inner_width
        new_json_data_2["outer_length"] = outer_width
        new_json_data_2["outer_width"] = outer_length

        new_cl_parameters_2 = dab_ipo_fx_find_max_inner_count(new_json_data_2)

        if new_cl_parameters["current_inner_count"] < new_cl_parameters_2["current_inner_count"]:
            new_cl_parameters = new_cl_parameters_2


    if (inner_length != inner_width) and (new_cl_parameters["current_inner_count"] < new_cl_parameters["max_allowed_inner_count"]):
        new_json_data_2 = copy.deepcopy(my_cl_parameters)
        new_json_data_2["inner_length"] = inner_width
        new_json_data_2["inner_width"] = inner_length
        new_json_data_2["outer_length"] = outer_width
        new_json_data_2["outer_width"] = outer_length

        new_cl_parameters_2 = dab_ipo_fx_find_max_inner_count(new_json_data_2)

        if new_cl_parameters["current_inner_count"] < new_cl_parameters_2["current_inner_count"]:
            new_cl_parameters = new_cl_parameters_2

    
    ti = new_cl_parameters["current_inner_count"]
    
    plot_json = {}
    plot_json["min_x_array"] = [0, dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["min_y_array"] = [0, dab_ipo_parameter_gap_from_outer_widthwise]
    plot_json["max_x_array"] = [outer_length, outer_length - dab_ipo_parameter_gap_from_outer_lengthwise]
    plot_json["max_y_array"] = [outer_width, outer_width - dab_ipo_parameter_gap_from_outer_widthwise]
    
    for i in range(2,len(new_cl_parameters["my_space"])):
        plot_json["min_x_array"].append(new_cl_parameters["my_space"][i][0])
        plot_json["min_y_array"].append(new_cl_parameters["my_space"][i][1])
        plot_json["max_x_array"].append(new_cl_parameters["my_space"][i][2])
        plot_json["max_y_array"].append(new_cl_parameters["my_space"][i][3])
        
    
    return ti, plot_json
def dab_ipo_fx_patterns_complex(my_parameters, all_solutions):
    
    dab_ipo_parameter_multiple_layers                    = my_parameters["dab_ipo_parameter_multiple_layers"]
    
    dab_ipo_parameter_gap_from_outer_lengthwise          = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise           = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
        
    dab_ipo_parameter_gap_between_inners_lengthwise      = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    dab_ipo_parameter_gap_between_inners_widthwise       = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
    
    dab_ipo_parameter_outer_length                       = my_parameters["dab_ipo_parameter_outer_length"]
    dab_ipo_parameter_outer_width                        = my_parameters["dab_ipo_parameter_outer_width"]
    dab_ipo_parameter_outer_height                       = my_parameters["dab_ipo_parameter_outer_height"]
    dab_ipo_parameter_outer_weight                       = my_parameters["dab_ipo_parameter_outer_weight"]
    dab_ipo_parameter_outer_volume_utilisation            		= my_parameters["dab_ipo_parameter_outer_volume_utilisation"]
    dab_ipo_parameter_max_inner_count                    = my_parameters["dab_ipo_parameter_max_inner_count"]
    dab_ipo_parameter_top_layer_full                     = my_parameters["dab_ipo_parameter_top_layer_full"]
    dab_ipo_parameter_inner_length                       = my_parameters["dab_ipo_parameter_inner_length"]
    dab_ipo_parameter_inner_width                        = my_parameters["dab_ipo_parameter_inner_width"]
    dab_ipo_parameter_inner_height                       = my_parameters["dab_ipo_parameter_inner_height"]
    dab_ipo_parameter_inner_weight                       = my_parameters["dab_ipo_parameter_inner_weight"]

    outer_length        = dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise*2
    outer_width         = dab_ipo_parameter_outer_width -dab_ipo_parameter_gap_from_outer_widthwise*2
    outer_height        = dab_ipo_parameter_outer_height
    outer_weight        = dab_ipo_parameter_outer_weight

    inner_length    = dab_ipo_parameter_inner_length
    inner_width     = dab_ipo_parameter_inner_width
    inner_height    = dab_ipo_parameter_inner_height
    inner_weight    = dab_ipo_parameter_inner_weight
    
    
    max_inner_count_weight      = math.floor((outer_weight + 0.0001) / inner_weight)
    max_inner_count             = min([dab_ipo_parameter_max_inner_count, max_inner_count_weight])
    
    ti, plot_json = dab_ipo_fx_pattern_complex_ti(my_parameters)
    
    max_ti = ti
    
    all_solutions["ti_array"].append(ti)
    all_solutions["plot_json_array"].append(json.dumps(plot_json))
    
    return all_solutions
    
def dab_ipo_fx_IPO_Main(my_parameters):

    dab_ipo_parameter_patterns_single_case_l_to_l = my_parameters["dab_ipo_parameter_patterns_single_case_l_to_l"]
    dab_ipo_parameter_patterns_single_case_w_to_l = my_parameters["dab_ipo_parameter_patterns_single_case_w_to_l"]
    dab_ipo_parameter_patterns_single_row_l_to_l = my_parameters["dab_ipo_parameter_patterns_single_row_l_to_l"]
    dab_ipo_parameter_patterns_single_row_w_to_l = my_parameters["dab_ipo_parameter_patterns_single_row_w_to_l"]
    dab_ipo_parameter_patterns_single_row_l_to_w = my_parameters["dab_ipo_parameter_patterns_single_row_l_to_w"]
    dab_ipo_parameter_patterns_single_row_w_to_w = my_parameters["dab_ipo_parameter_patterns_single_row_w_to_w"]
    dab_ipo_parameter_patterns_uniform_l_to_l = my_parameters["dab_ipo_parameter_patterns_uniform_l_to_l"]
    dab_ipo_parameter_patterns_uniform_w_to_l = my_parameters["dab_ipo_parameter_patterns_uniform_w_to_l"]
    dab_ipo_parameter_patterns_dual_uniform_l_loading = my_parameters["dab_ipo_parameter_patterns_dual_uniform_l_loading"]
    dab_ipo_parameter_patterns_dual_uniform_w_loading = my_parameters["dab_ipo_parameter_patterns_dual_uniform_w_loading"]
    dab_ipo_parameter_patterns_complex = my_parameters["dab_ipo_parameter_patterns_complex"]
    dab_ipo_parameter_max_recursion_depth = my_parameters["dab_ipo_parameter_max_recursion_depth"]
    
    dab_ipo_parameter_multiple_layers = my_parameters["dab_ipo_parameter_multiple_layers"]
    dab_ipo_parameter_top_layer_full = my_parameters["dab_ipo_parameter_top_layer_full"]
    
    dab_ipo_parameter_outer_volume_utilisation = my_parameters["dab_ipo_parameter_outer_volume_utilisation"]
    dab_ipo_parameter_max_inner_count = my_parameters["dab_ipo_parameter_max_inner_count"]
    
    dab_ipo_parameter_gap_from_outer_lengthwise          = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise           = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
    
    dab_ipo_parameter_gap_between_inners_lengthwise      = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
    dab_ipo_parameter_gap_between_inners_widthwise       = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
    
    dab_ipo_parameter_output_ti = my_parameters["dab_ipo_parameter_output_ti"]
    dab_ipo_parameter_output_hi = my_parameters["dab_ipo_parameter_output_hi"]
    dab_ipo_parameter_output_selected_pattern_name = my_parameters["dab_ipo_parameter_output_selected_pattern_name"]
    dab_ipo_parameter_output_inners_per_outer = my_parameters["dab_ipo_parameter_output_inners_per_outer"]
    dab_ipo_parameter_output_plot_info = my_parameters["dab_ipo_parameter_output_plot_info"]
    
    dab_ipo_parameter_outer_length = my_parameters["dab_ipo_parameter_outer_length"]
    dab_ipo_parameter_outer_width = my_parameters["dab_ipo_parameter_outer_width"]
    dab_ipo_parameter_outer_height = my_parameters["dab_ipo_parameter_outer_height"]
    dab_ipo_parameter_outer_weight = my_parameters["dab_ipo_parameter_outer_weight"]
    

    
    
    dab_ipo_parameter_inner_length = my_parameters["dab_ipo_parameter_inner_length"]
    dab_ipo_parameter_inner_width = my_parameters["dab_ipo_parameter_inner_width"]
    dab_ipo_parameter_inner_height = my_parameters["dab_ipo_parameter_inner_height"]
    dab_ipo_parameter_inner_weight = my_parameters["dab_ipo_parameter_inner_weight"]
    
    
    outer_length = dab_ipo_parameter_outer_length 
    outer_width = dab_ipo_parameter_outer_width 
    
    inner_length = dab_ipo_parameter_inner_length 
    inner_width = dab_ipo_parameter_inner_width 
    
    
    
    case_plot_orientation_switch = 0
    case_plot_orientation_switch = case_plot_orientation_switch + dab_ipo_parameter_patterns_single_case_l_to_l
    case_plot_orientation_switch = case_plot_orientation_switch + dab_ipo_parameter_patterns_single_row_l_to_l
    case_plot_orientation_switch = case_plot_orientation_switch + dab_ipo_parameter_patterns_single_row_w_to_w
    case_plot_orientation_switch = case_plot_orientation_switch + dab_ipo_parameter_patterns_uniform_l_to_l
    case_plot_orientation_switch = case_plot_orientation_switch + dab_ipo_parameter_patterns_dual_uniform_l_loading
    case_plot_orientation_switch = case_plot_orientation_switch + dab_ipo_parameter_patterns_dual_uniform_w_loading
    case_plot_orientation_switch = case_plot_orientation_switch + dab_ipo_parameter_patterns_complex
    
    if case_plot_orientation_switch > 0:
        plot_json = {}
        plot_json["min_x_array"] = [0, dab_ipo_parameter_gap_from_outer_lengthwise, dab_ipo_parameter_gap_from_outer_lengthwise]
        plot_json["min_y_array"] = [0, dab_ipo_parameter_gap_from_outer_widthwise, dab_ipo_parameter_gap_from_outer_widthwise]
        plot_json["max_x_array"] = [outer_length, outer_length - dab_ipo_parameter_gap_from_outer_lengthwise, dab_ipo_parameter_gap_from_outer_lengthwise + inner_length]
        plot_json["max_y_array"] = [outer_width, outer_width - dab_ipo_parameter_gap_from_outer_widthwise, dab_ipo_parameter_gap_from_outer_widthwise + inner_width]
            
        plot_info = json.dumps(plot_json)
    else:
        plot_json = {}
        plot_json["min_x_array"] = [0, dab_ipo_parameter_gap_from_outer_lengthwise, dab_ipo_parameter_gap_from_outer_lengthwise]
        plot_json["min_y_array"] = [0, dab_ipo_parameter_gap_from_outer_widthwise, dab_ipo_parameter_gap_from_outer_widthwise]
        plot_json["max_x_array"] = [outer_length, outer_length - dab_ipo_parameter_gap_from_outer_lengthwise, dab_ipo_parameter_gap_from_outer_lengthwise + inner_width]
        plot_json["max_y_array"] = [outer_width, outer_width - dab_ipo_parameter_gap_from_outer_widthwise, dab_ipo_parameter_gap_from_outer_widthwise + inner_length]
            
        plot_info = json.dumps(plot_json)

    all_solutions = {}
    all_solutions["ti_array"] = []
    all_solutions["hi_array"] = []
    all_solutions["dab_ipo_parameter_array"] = []
    all_solutions["pattern_name_array"] = []
    all_solutions["plot_json_array"] = []

    if dab_ipo_parameter_patterns_single_case_l_to_l == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        all_solutions = dab_ipo_fx_patterns_single_case(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("single_case_l_to_l")
        
    if dab_ipo_parameter_patterns_single_case_w_to_l == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        new_my_parameters["dab_ipo_parameter_inner_length"] = my_parameters["dab_ipo_parameter_inner_width"]
        new_my_parameters["dab_ipo_parameter_inner_width"] = my_parameters["dab_ipo_parameter_inner_length"]
        all_solutions = dab_ipo_fx_patterns_single_case(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("single_case_w_to_l")
        
        

    if dab_ipo_parameter_patterns_single_row_l_to_l == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        all_solutions = dab_ipo_fx_patterns_single_row(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("single_row_l_to_l")

    if dab_ipo_parameter_patterns_single_row_w_to_l == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        new_my_parameters["dab_ipo_parameter_inner_length"] = my_parameters["dab_ipo_parameter_inner_width"]
        new_my_parameters["dab_ipo_parameter_inner_width"] = my_parameters["dab_ipo_parameter_inner_length"]
        all_solutions = dab_ipo_fx_patterns_single_row(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("single_row_w_to_l")

    if dab_ipo_parameter_patterns_single_row_l_to_w == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        new_my_parameters["dab_ipo_parameter_outer_length"] = my_parameters["dab_ipo_parameter_outer_width"]
        new_my_parameters["dab_ipo_parameter_outer_width"] = my_parameters["dab_ipo_parameter_outer_length"]
        new_my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"] = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
        new_my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"] = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
        new_my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"] = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
        new_my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"] = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
        all_solutions = dab_ipo_fx_patterns_single_row(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("single_row_l_to_w")

    if dab_ipo_parameter_patterns_single_row_w_to_w == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        new_my_parameters["dab_ipo_parameter_inner_length"] = my_parameters["dab_ipo_parameter_inner_width"]
        new_my_parameters["dab_ipo_parameter_inner_width"] = my_parameters["dab_ipo_parameter_inner_length"]
        new_my_parameters["dab_ipo_parameter_outer_length"] = my_parameters["dab_ipo_parameter_outer_width"]
        new_my_parameters["dab_ipo_parameter_outer_width"] = my_parameters["dab_ipo_parameter_outer_length"]
        new_my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"] = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
        new_my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"] = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
        new_my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"] = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
        new_my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"] = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
        all_solutions = dab_ipo_fx_patterns_single_row(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("single_row_w_to_w")
    
    if dab_ipo_parameter_patterns_uniform_l_to_l == 1:
        all_solutions = dab_ipo_fx_patterns_uniform(my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("uniform_l_to_l")

    if dab_ipo_parameter_patterns_uniform_w_to_l == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        new_my_parameters["dab_ipo_parameter_inner_length"] = my_parameters["dab_ipo_parameter_inner_width"]
        new_my_parameters["dab_ipo_parameter_inner_width"] = my_parameters["dab_ipo_parameter_inner_length"]
        all_solutions = dab_ipo_fx_patterns_uniform(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("uniform_w_to_l")


    if dab_ipo_parameter_patterns_dual_uniform_l_loading == 1:
        all_solutions = dab_ipo_fx_patterns_dual_uniform(my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("dual_uniform_l_loading")

    if dab_ipo_parameter_patterns_dual_uniform_w_loading == 1:
        new_my_parameters = copy.deepcopy(my_parameters)
        new_my_parameters["dab_ipo_parameter_outer_length"] = my_parameters["dab_ipo_parameter_outer_width"]
        new_my_parameters["dab_ipo_parameter_outer_width"] = my_parameters["dab_ipo_parameter_outer_length"]
        new_my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"] = my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"]
        new_my_parameters["dab_ipo_parameter_gap_from_outer_widthwise"] = my_parameters["dab_ipo_parameter_gap_from_outer_lengthwise"]
        new_my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"] = my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"]
        new_my_parameters["dab_ipo_parameter_gap_between_inners_widthwise"] = my_parameters["dab_ipo_parameter_gap_between_inners_lengthwise"]
        all_solutions = dab_ipo_fx_patterns_dual_uniform(new_my_parameters, all_solutions)
        all_solutions["pattern_name_array"].append("dual_uniform_w_loading")
    
    if dab_ipo_parameter_patterns_complex == 1:
    
        max_ti = 0
        my_i = -1
        for i in range(0,len(all_solutions["ti_array"])):
            if max_ti < all_solutions["ti_array"][i]:
                max_ti = all_solutions["ti_array"][i]
                my_i = i
                
        outer_length = my_parameters["dab_ipo_parameter_outer_length"]
        outer_width = my_parameters["dab_ipo_parameter_outer_width"]
        
        inner_length = my_parameters["dab_ipo_parameter_inner_length"]
        inner_width = my_parameters["dab_ipo_parameter_inner_width"]

        outer_area_reduced = ((outer_length - dab_ipo_parameter_gap_from_outer_lengthwise  * 2 + dab_ipo_parameter_gap_between_inners_lengthwise)*(outer_width - dab_ipo_parameter_gap_from_outer_widthwise * 2 + dab_ipo_parameter_gap_between_inners_widthwise))
        inner_area_increased = ((inner_length + dab_ipo_parameter_gap_between_inners_lengthwise)*(inner_width + dab_ipo_parameter_gap_between_inners_widthwise))
        max_inners_by_area = math.floor(outer_area_reduced / inner_area_increased)
        
        outer_length        = dab_ipo_parameter_outer_length - dab_ipo_parameter_gap_from_outer_lengthwise*2
        outer_width         = dab_ipo_parameter_outer_width -dab_ipo_parameter_gap_from_outer_widthwise*2
        outer_height        = dab_ipo_parameter_outer_height
        outer_weight        = dab_ipo_parameter_outer_weight

        inner_length    = dab_ipo_parameter_inner_length
        inner_width     = dab_ipo_parameter_inner_width
        inner_height    = dab_ipo_parameter_inner_height
        inner_weight    = dab_ipo_parameter_inner_weight
        
        
        max_inner_count_weight      = math.floor((outer_weight + 0.0001) / inner_weight)
        max_inner_count             = min([dab_ipo_parameter_max_inner_count, max_inner_count_weight])
        
        max_inner_count				= min([max_inner_count, max_inners_by_area])
        
        
        if max_inner_count > max_ti and max_ti < dab_ipo_parameter_max_recursion_depth:
        
            all_solutions = dab_ipo_fx_patterns_complex(my_parameters, all_solutions)
            all_solutions["pattern_name_array"].append("complex")
        
        
        
    max_ti = 0
    my_i = -1
    for i in range(0,len(all_solutions["ti_array"])):
        if max_ti < all_solutions["ti_array"][i]:
            max_ti = all_solutions["ti_array"][i]
            my_i = i
        
        
        
    all_flags = {}	
    all_flags["ipo_limited_by__multiple_layers_disabled__to"] = "NA"
    all_flags["ipo_limited_by__weight__to"] = "NA"
    all_flags["ipo_limited_by__volume_restriction__to"] = "NA"
    all_flags["ipo_limited_by__max_inner_count__to"] = "NA"
    all_flags["ipo_limited_by__full_layers_only__to"] = "NA"
    
    
    if my_i > -1:
    
        ti_max = all_solutions["ti_array"][my_i]
        pattern_name = all_solutions["pattern_name_array"][my_i]
        plot_info = all_solutions["plot_json_array"][my_i]
        
        
        if dab_ipo_parameter_multiple_layers == 0:
            all_flags["ipo_limited_by__multiple_layers_disabled__to"] = str(int(ti_max))
        else:
            all_flags["ipo_limited_by__multiple_layers_disabled__to"] = "NA"
            
        all_flags["ipo_limited_by__weight__to"] = "NA"
        all_flags["ipo_limited_by__volume_restriction__to"] = "NA"
        all_flags["ipo_limited_by__max_inner_count__to"] = "NA"
        all_flags["ipo_limited_by__full_layers_only__to"] = "NA"
        
        hi_max = math.floor((dab_ipo_parameter_outer_height + 0.0001) / dab_ipo_parameter_inner_height)
        hi = hi_max
        if dab_ipo_parameter_multiple_layers == 0:
            hi = min(1, hi)
        
        inner_per_outer_max = ti_max * hi
        
        if dab_ipo_parameter_outer_volume_utilisation > 1:
            dab_ipo_parameter_outer_volume_utilisation = float(1)
        
        outer_max_volume_incl_utilisation = float((dab_ipo_parameter_outer_length * dab_ipo_parameter_outer_width  * dab_ipo_parameter_outer_height) * dab_ipo_parameter_outer_volume_utilisation)
        inner_volume = float(dab_ipo_parameter_inner_length  * dab_ipo_parameter_inner_width * dab_ipo_parameter_inner_height)
        inner_per_outer_volume_utilisation_max = math.floor((outer_max_volume_incl_utilisation + 0.0001) / inner_volume)
        
        inner_per_outer_weight = math.floor((dab_ipo_parameter_outer_weight  + 0.0001) / dab_ipo_parameter_inner_weight )
        
        
        all_flags["ipo_limited_by__weight__to"] = str(int(inner_per_outer_weight))
        all_flags["ipo_limited_by__volume_restriction__to"] = str(int(inner_per_outer_volume_utilisation_max))
        all_flags["ipo_limited_by__max_inner_count__to"] = str(int(dab_ipo_parameter_max_inner_count))
        
        
        
        inners_per_outer = min([inner_per_outer_max, inner_per_outer_volume_utilisation_max, dab_ipo_parameter_max_inner_count, inner_per_outer_weight])
        
        
        if inners_per_outer < ti_max:
            hi = 1
            ti = inners_per_outer
        else:
            ti = ti_max
            max_hi_from_count_incomple_top_layer =  math.ceil((inners_per_outer)/round(ti))
            max_hi_from_count_comple_top_layer =    math.floor((inners_per_outer+0.0001)/round(ti))
            
            if dab_ipo_parameter_top_layer_full == 0:
                hi = min([hi, max_hi_from_count_incomple_top_layer])
            else:
                hi = min([hi, max_hi_from_count_comple_top_layer])
                inners_per_outer = ti * hi
                all_flags["ipo_limited_by__full_layers_only__to"] = str(int(inners_per_outer))
       
    else:
        ti_max = 0
        hi_max = 0
        ti = 0
        hi = 0
        inners_per_outer = 0
        pattern_name = "NA"
        

    if ti*hi*inners_per_outer == 0:
        ti = 0
        hi = 0
        inners_per_outer = 0
        pattern_name = "NA"
    
    return ti, hi, ti_max, hi_max, inners_per_outer, pattern_name, plot_info, all_flags
    
    
def dab_inners_per_outer(data_df, parameter_df):

    data_df = data_df.copy(deep=True)
    parameter_df = parameter_df.copy(deep=True)

    dab_ipo_parameter_sku_id_column_name 			= parameter_df.at[0, 'dab_ipo_parameter_sku_id_column_name']
    dab_ipo_parameter_inner_length_column_name 	= parameter_df.at[0, 'dab_ipo_parameter_inner_length_column_name']
    dab_ipo_parameter_inner_width_column_name 	= parameter_df.at[0, 'dab_ipo_parameter_inner_width_column_name']
    dab_ipo_parameter_inner_height_column_name 	= parameter_df.at[0, 'dab_ipo_parameter_inner_height_column_name']
    dab_ipo_parameter_inner_weight_column_name 	= parameter_df.at[0, 'dab_ipo_parameter_inner_weight_column_name']


    my_parameters = {}
    for col in parameter_df.columns:
        my_parameters[col] = parameter_df[col].values[0]
    output_df = pd.DataFrame()
    
    output_df['ipo_output_sku_id'] = None
    
    output_df['ipo_output_ti'] = None
    output_df['ipo_output_hi'] = None
    output_df['ipo_output_inners_per_outer'] = None
    
    output_df['ipo_output_max_ti'] = None
    output_df['ipo_output_max_hi'] = None
    
    output_df['ipo_output_pattern_name'] = None
    output_df['ipo_output_plot_info'] = None
    output_df['ipo_limited_by__multiple_layers_disabled__to'] = None
    output_df['ipo_limited_by__weight__to'] = None
    output_df['ipo_limited_by__volume_restriction__to'] = None
    output_df['ipo_limited_by__max_inner_count__to'] = None
    output_df['ipo_limited_by__full_layers_only__to'] = None
    
    expected_orientation = 0
    if my_parameters["dab_ipo_parameter_outer_length"] < my_parameters["dab_ipo_parameter_outer_width"]:
        expected_orientation = 1

    for index, row in data_df.iterrows():
        
        my_parameters2 = copy.deepcopy(my_parameters)
        
        my_parameters2["dab_ipo_parameter_sku_id"] 			= data_df.at[index, dab_ipo_parameter_sku_id_column_name]
        my_parameters2["dab_ipo_parameter_inner_length"] 	= data_df.at[index, dab_ipo_parameter_inner_length_column_name]
        my_parameters2["dab_ipo_parameter_inner_width"] 	= data_df.at[index, dab_ipo_parameter_inner_width_column_name]
        my_parameters2["dab_ipo_parameter_inner_height"] 	= data_df.at[index, dab_ipo_parameter_inner_height_column_name]
        my_parameters2["dab_ipo_parameter_inner_weight"] 	= data_df.at[index, dab_ipo_parameter_inner_weight_column_name]

        ti = 0
        hi = 0
        inners_per_outer = 0
        ti_max = 0
        hi_max = 0
        pattern_name = ""
        plot_info = ""
        all_flags = {}
        
        ti, hi, ti_max, hi_max, inners_per_outer, pattern_name, plot_info, all_flags  = dab_ipo_fx_IPO_Main(my_parameters2)
        
        ti = int(ti)
        hi = int(hi)
        inners_per_outer = int(inners_per_outer)
        ti_max = int(ti_max)
        hi_max = int(hi_max)
        pattern_name = str(pattern_name)
        plot_info = str(plot_info)
        
        plot_json = json.loads(plot_info)
        
        my_orientation = 0
        if plot_json["max_x_array"][0] < plot_json["max_y_array"][0]:
            my_orientation = 1
        
        if expected_orientation != my_orientation:
            g = 0
            for g in range(len(plot_json["min_x_array"])):
                
                plot_json["min_y_array"][g] = plot_json["min_y_array"][g] * (-1)
                plot_json["max_y_array"][g] = plot_json["max_y_array"][g] * (-1)
                
                x = plot_json["min_x_array"][g]
                y = plot_json["min_y_array"][g]
                plot_json["min_x_array"][g] = -y
                plot_json["min_y_array"][g] = x
                
                x = plot_json["max_x_array"][g]
                y = plot_json["max_y_array"][g]
                plot_json["max_x_array"][g] = -y
                plot_json["max_y_array"][g] = x
            
        plot_json["sku_id"] = my_parameters2["dab_ipo_parameter_sku_id"]
        plot_json["ti_max"] = ti_max
        plot_json["hi_max"] = hi_max
        plot_json["inners_per_outer"] = inners_per_outer
        plot_json["pattern_name"] = pattern_name
        
        plot_json['ipo_limited_by__multiple_layers_disabled__to'] 	= str(all_flags["ipo_limited_by__multiple_layers_disabled__to"])
        plot_json['ipo_limited_by__weight__to'] 					= str(all_flags["ipo_limited_by__weight__to"])
        plot_json['ipo_limited_by__volume_restriction__to'] 		= str(all_flags["ipo_limited_by__volume_restriction__to"])
        plot_json['ipo_limited_by__max_inner_count__to'] 			= str(all_flags["ipo_limited_by__max_inner_count__to"])
        plot_json['ipo_limited_by__full_layers_only__to'] 			= str(all_flags["ipo_limited_by__full_layers_only__to"])
        
        outer_height = my_parameters2["dab_ipo_parameter_outer_height"] 
        inner_height = my_parameters2["dab_ipo_parameter_inner_height"]
        
        plot_json["height_array"] = [outer_height, outer_height]
        for i in range(2, len(plot_json["min_x_array"])):
            plot_json["height_array"].append(inner_height)
        
        
        
        plot_info = json.dumps(plot_json)
        
           
        output_df.at[index, 'ipo_output_sku_id'] 									= data_df.at[index, dab_ipo_parameter_sku_id_column_name]
        output_df.at[index, 'ipo_output_max_ti'] 									= ti_max
        output_df.at[index, 'ipo_output_max_hi'] 									= hi_max
        output_df.at[index, 'ipo_output_ti'] 										= ti
        output_df.at[index, 'ipo_output_hi'] 										= hi
        output_df.at[index, 'ipo_output_inners_per_outer'] 							= inners_per_outer
        output_df.at[index, 'ipo_output_pattern_name'] 								= pattern_name
        output_df.at[index, 'ipo_output_plot_info'] 								= plot_info
        output_df.at[index, 'ipo_limited_by__multiple_layers_disabled__to'] 		= str(all_flags["ipo_limited_by__multiple_layers_disabled__to"])
        output_df.at[index, 'ipo_limited_by__weight__to'] 							= str(all_flags["ipo_limited_by__weight__to"])
        output_df.at[index, 'ipo_limited_by__volume_restriction__to'] 				= str(all_flags["ipo_limited_by__volume_restriction__to"])
        output_df.at[index, 'ipo_limited_by__max_inner_count__to'] 					= str(all_flags["ipo_limited_by__max_inner_count__to"])
        output_df.at[index, 'ipo_limited_by__full_layers_only__to'] 				= str(all_flags["ipo_limited_by__full_layers_only__to"])
        
        
    return output_df
    

def dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_0, plot_df_0_i, summable_value):
    col0 = col_name
    col1 = "Patterns"
    col2 = in_table_name
    col3 = ""
    col4 = ""
    
    
    if col_name == "Inner cannot fit into outer":
        col3 = ""
        col4 = format_float_with_commas( (output_df['ipo_output_pattern_name'] == output_col_value).sum())
        summable_value = summable_value + ( (output_df['ipo_output_pattern_name'] == output_col_value).sum())
    else:
        col3 = format_float_with_commas( my_variables_df.at[0, col_name] )
        col4 = format_float_with_commas( (output_df['ipo_output_pattern_name'] == output_col_value).sum())
        summable_value = summable_value + ( (output_df['ipo_output_pattern_name'] == output_col_value).sum())
    
            
    plot_df_0_i = plot_df_0_i + 1
    plot_df_0.at[plot_df_0_i, "0"] = col0
    plot_df_0.at[plot_df_0_i, "1"] = col1
    plot_df_0.at[plot_df_0_i, "2"] = col2
    plot_df_0.at[plot_df_0_i, "3"] = col3
    plot_df_0.at[plot_df_0_i, "4"] = col4
    
    return plot_df_0, plot_df_0_i, summable_value
def dab_ipo_statistics_fx_detect_restricted_by_the_limit(col_name, in_table_name, output_column_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_0, plot_df_0_i, summable_value):
    col0 = col_name
    col1 = "Restrictions"
    col2 = in_table_name
    col3 = ""
    col4 = ""
    
    
    ipo_column_name = "ipo_output_inners_per_outer"
    
    unique_values_in_column = output_df[output_column_name].unique().shape[0]
    restriction_active = 1
    first_entry = output_df[output_column_name].iloc[0]
    if unique_values_in_column == 1 and first_entry == "NA":
        restriction_active = 0
        col3 = "NA"
        
    output_df[ipo_column_name] = output_df[ipo_column_name].astype(str)
    output_df[output_column_name] = output_df[output_column_name].str.replace(',', '')
    
    if restriction_active == 1:
        
        col3 = format_float_with_commas( my_variables_df.at[0, col_name], 4)
        
        col4 = format_float_with_commas(output_df[output_df[output_column_name] == output_df[ipo_column_name]].shape[0])
        summable_value = summable_value + (output_df[output_df[output_column_name] == output_df[ipo_column_name]].shape[0])
    
    plot_df_0_i = plot_df_0_i + 1
    plot_df_0.at[plot_df_0_i, "0"] = col0
    plot_df_0.at[plot_df_0_i, "1"] = col1
    plot_df_0.at[plot_df_0_i, "2"] = col2
    plot_df_0.at[plot_df_0_i, "3"] = col3
    plot_df_0.at[plot_df_0_i, "4"] = col4
    
    return plot_df_0, plot_df_0_i, summable_value
    
    
def dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_0, plot_df_0_i, rounding_precision):
    col0 = col_name
    col1 = col1_name
    col2 = in_table_name
    col3 = ""
    col4 = ""
    
    col3 = format_float_with_commas( my_variables_df.at[0, col_name] ,rounding_precision)
        
    
            
            
    plot_df_0_i = plot_df_0_i + 1
    plot_df_0.at[plot_df_0_i, "0"] = col0
    plot_df_0.at[plot_df_0_i, "1"] = col1
    plot_df_0.at[plot_df_0_i, "2"] = col2
    plot_df_0.at[plot_df_0_i, "3"] = col3
    plot_df_0.at[plot_df_0_i, "4"] = col4
    
    return plot_df_0, plot_df_0_i


def dab_inners_per_outer_statistics(input_df, my_variables_df, output_df):

    input_df = input_df.copy(deep=True)
    my_variables_df = my_variables_df.copy(deep=True)
    output_df = output_df.copy(deep=True)
    
    
    my_column_detection = "Assign Column Below"


    plot_df_0 = pd.DataFrame()
    plot_df_0["0"] = None
    plot_df_0["1"] = None
    plot_df_0["2"] = None
    plot_df_0["3"] = None
    plot_df_0["4"] = None



    plot_df_0_i = -1

    plot_df_0_i = plot_df_0_i + 1
    plot_df_0.at[plot_df_0_i, "1"] = "Total Input Rows:"
    plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(len(input_df), 0)

    unique_rows_count = input_df.drop_duplicates().shape[0]

    plot_df_0_i = plot_df_0_i + 1
    plot_df_0.at[plot_df_0_i, "1"] = "Unique Input Rows:"
    plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(unique_rows_count, 0)

    plot_df_0_i = plot_df_0_i + 1
    plot_df_0.at[plot_df_0_i, "1"] = "Total Output Rows:"
    plot_df_0.at[plot_df_0_i, "2"] = format_float_with_commas(len(output_df), 0)


    plot_df_1 = pd.DataFrame()
    plot_df_1["0"] = None
    plot_df_1["1"] = None
    plot_df_1["2"] = None
    plot_df_1["3"] = None
    plot_df_1["4"] = None
    plot_df_1_i = -1

    summable_value = 0

    col_name = "dab_ipo_parameter_patterns_single_case_l_to_l"
    output_col_value = "single_case_l_to_l"
    in_table_name = "Single Case L to L"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    col_name = "dab_ipo_parameter_patterns_single_case_w_to_l"
    output_col_value = "single_case_w_to_l"
    in_table_name = "Single Case W to L"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    plot_df_1_i = plot_df_1_i + 1
    plot_df_1.at[plot_df_1_i, "0"] = ""

    col_name = "dab_ipo_parameter_patterns_single_row_l_to_l"
    output_col_value = "single_row_l_to_l"
    in_table_name = "Slingle Row L to L"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    col_name = "dab_ipo_parameter_patterns_single_row_w_to_l"
    output_col_value = "single_row_w_to_l"
    in_table_name = "Slingle Row W to L"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    col_name = "dab_ipo_parameter_patterns_single_row_l_to_w"
    output_col_value = "single_row_l_to_w"
    in_table_name = "Slingle Row L to W"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    col_name = "dab_ipo_parameter_patterns_single_row_w_to_w"
    output_col_value = "single_row_w_to_w"
    in_table_name = "Slingle Row W to W"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    plot_df_1_i = plot_df_1_i + 1
    plot_df_1.at[plot_df_1_i, "0"] = ""

    col_name = "dab_ipo_parameter_patterns_uniform_l_to_l"
    output_col_value = "uniform_l_to_l"
    in_table_name = "Uniform L to L"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    col_name = "dab_ipo_parameter_patterns_uniform_w_to_l"
    output_col_value = "uniform_w_to_l"
    in_table_name = "Uniform W to L"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    plot_df_1_i = plot_df_1_i + 1
    plot_df_1.at[plot_df_1_i, "0"] = ""

    col_name = "dab_ipo_parameter_patterns_dual_uniform_l_loading"
    output_col_value = "dual_uniform_l_loading"
    in_table_name = "Dual Uniform L Loading"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    col_name = "dab_ipo_parameter_patterns_dual_uniform_w_loading"
    output_col_value = "dual_uniform_w_loading"
    in_table_name = "Dual Uniform W Loading"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    plot_df_1_i = plot_df_1_i + 1
    plot_df_1.at[plot_df_1_i, "0"] = ""

    col_name = "dab_ipo_parameter_patterns_complex"
    output_col_value = "complex"
    in_table_name = "Complex"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)

    col_name = "dab_ipo_parameter_max_recursion_depth"
    col1_name = "Patterns Parameter"
    in_table_name = "Recursion Depth"
    plot_df_1, plot_df_1_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_1, plot_df_1_i, 0)

    plot_df_1_i = plot_df_1_i + 1
    plot_df_1.at[plot_df_1_i, "0"] = ""
    
    col_name = "Inner cannot fit into outer"
    output_col_value = "NA"
    in_table_name = "NA"
    plot_df_1, plot_df_1_i, summable_value = dab_ipo_statistics_fx_detect_settings_patters(col_name, output_col_value, in_table_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_1, plot_df_1_i, summable_value)
    
    plot_df_1_i = plot_df_1_i + 1
    plot_df_1.at[plot_df_1_i, "0"] = ""
    
    plot_df_1_i = plot_df_1_i + 1
    plot_df_1.at[plot_df_1_i, "3"] = "Total Count:"
    plot_df_1.at[plot_df_1_i, "4"] = format_float_with_commas(summable_value)

    plot_df_2 = pd.DataFrame()
    plot_df_2["0"] = None
    plot_df_2["1"] = None
    plot_df_2["2"] = None
    plot_df_2["3"] = None
    plot_df_2["4"] = None
    plot_df_2_i = -1

    summable_value = 0

    col_name = "dab_ipo_parameter_multiple_layers"
    in_table_name = "Multiple Layers Allowed"
    output_column_name = "ipo_limited_by__multiple_layers_disabled__to"
    plot_df_2, plot_df_2_i, summable_value = dab_ipo_statistics_fx_detect_restricted_by_the_limit(col_name, in_table_name, output_column_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_2, plot_df_2_i, summable_value)

    col_name = "dab_ipo_parameter_outer_weight"
    in_table_name = "Max Outer Weight"
    output_column_name = "ipo_limited_by__weight__to"
    plot_df_2, plot_df_2_i, summable_value = dab_ipo_statistics_fx_detect_restricted_by_the_limit(col_name, in_table_name, output_column_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_2, plot_df_2_i, summable_value)

    col_name = "dab_ipo_parameter_outer_volume_utilisation"
    in_table_name = "Limit Volume utilisation"
    output_column_name = "ipo_limited_by__volume_restriction__to"
    plot_df_2, plot_df_2_i, summable_value = dab_ipo_statistics_fx_detect_restricted_by_the_limit(col_name, in_table_name, output_column_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_2, plot_df_2_i, summable_value)

    col_name = "dab_ipo_parameter_max_inner_count"
    in_table_name = "Max Inner Count"
    output_column_name = "ipo_limited_by__max_inner_count__to"
    plot_df_2, plot_df_2_i, summable_value = dab_ipo_statistics_fx_detect_restricted_by_the_limit(col_name, in_table_name, output_column_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_2, plot_df_2_i, summable_value)

    col_name = "dab_ipo_parameter_top_layer_full"
    in_table_name = "Top layer Full"
    output_column_name = "ipo_limited_by__full_layers_only__to"
    plot_df_2, plot_df_2_i, summable_value = dab_ipo_statistics_fx_detect_restricted_by_the_limit(col_name, in_table_name, output_column_name, input_df, my_variables_df, output_df, my_column_detection, plot_df_2, plot_df_2_i, summable_value)

    plot_df_2_i = plot_df_2_i + 1
    plot_df_2.at[plot_df_2_i, "3"] = "Total Count:"
    plot_df_2.at[plot_df_2_i, "4"] = format_float_with_commas(summable_value)

    plot_df_3 = pd.DataFrame()
    plot_df_3["0"] = None
    plot_df_3["1"] = None
    plot_df_3["2"] = None
    plot_df_3["3"] = None
    plot_df_3["4"] = None
    plot_df_3_i = -1

    col_name = "dab_ipo_parameter_outer_length"
    col1_name = "Outer Dimensions"
    in_table_name = "Length"
    plot_df_3, plot_df_3_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_3, plot_df_3_i, 4)

    col_name = "dab_ipo_parameter_outer_width"
    col1_name = "Outer Dimensions"
    in_table_name = "Width"
    plot_df_3, plot_df_3_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_3, plot_df_3_i, 4)

    col_name = "dab_ipo_parameter_outer_height"
    col1_name = "Outer Dimensions"
    in_table_name = "Height"
    plot_df_3, plot_df_3_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_3, plot_df_3_i, 4)

    plot_df_3_i = plot_df_3_i + 1
    plot_df_3.at[plot_df_3_i, "0"] = ""

    col_name = "dab_ipo_parameter_gap_from_outer_lengthwise"
    col1_name = "Gaps"
    in_table_name = "Gap From Outer Lengthwise"
    plot_df_3, plot_df_3_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_3, plot_df_3_i, 4)

    col_name = "dab_ipo_parameter_gap_from_outer_widthwise"
    col1_name = "Gaps"
    in_table_name = "Gap From Outer Widthwise"
    plot_df_3, plot_df_3_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_3, plot_df_3_i, 4)
    
    plot_df_3_i = plot_df_3_i + 1
    plot_df_3.at[plot_df_3_i, "0"] = ""
    
    col_name = "dab_ipo_parameter_gap_between_inners_lengthwise"
    col1_name = "Gaps"
    in_table_name = "Gap Between Inners Lengthwise"
    plot_df_3, plot_df_3_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_3, plot_df_3_i, 4)

    col_name = "dab_ipo_parameter_gap_between_inners_widthwise"
    col1_name = "Gaps"
    in_table_name = "Gap Between Inners Widthwise"
    plot_df_3, plot_df_3_i = dab_ipo_statistics_fx_detect_settings_generic(col_name, col1_name, in_table_name, input_df, my_variables_df, my_column_detection, plot_df_3, plot_df_3_i, 4)


    plot_df_0 = plot_df_0.fillna('')
    plot_df_1 = plot_df_1.fillna('')
    plot_df_2 = plot_df_2.fillna('')
    plot_df_3 = plot_df_3.fillna('')


    plot_df_0 = plot_df_0.rename(columns={'0': '0', '1': 'Name', '2': 'Count', '3': '3', '4': '4'})
    plot_df_1 = plot_df_1.rename(columns={'0': 'Variable Name', '1': 'Variable Type', '2': 'Name', '3': 'Setting', '4': 'Output Row Count'})
    plot_df_2 = plot_df_2.rename(columns={'0': 'Variable Name', '1': 'Variable Type', '2': 'Name', '3': 'Setting', '4': 'Output Row Count'})
    plot_df_3 = plot_df_3.rename(columns={'0': 'Variable Name', '1': 'Variable Type', '2': 'Name', '3': 'Setting', '4': 'Output Row Count'})

    return plot_df_0, plot_df_1, plot_df_2, plot_df_3



def dab_ti_hi_validation(data_df, parameter_df, ipo_value_df):
    
    
    data_df = data_df.copy(deep=True)
    parameter_df = parameter_df.copy(deep=True)
    ipo_value_df = ipo_value_df.copy(deep=True)
    
    output_df = pd.DataFrame()
    
    dab_ti_hi_val_parameter_max_outer_length 					= parameter_df.at[0, "dab_ti_hi_val_parameter_max_outer_length"]
    dab_ti_hi_val_parameter_max_outer_width 					= parameter_df.at[0, "dab_ti_hi_val_parameter_max_outer_width"]
    
    dab_ti_hi_val_parameter_min_outer_area 						= parameter_df.at[0, "dab_ti_hi_val_parameter_min_outer_area"]
    dab_ti_hi_val_parameter_max_outer_area 						= parameter_df.at[0, "dab_ti_hi_val_parameter_max_outer_area"]
    dab_ti_hi_val_parameter_min_outer_height 					= parameter_df.at[0, "dab_ti_hi_val_parameter_min_outer_height"]
    dab_ti_hi_val_parameter_max_outer_height 					= parameter_df.at[0, "dab_ti_hi_val_parameter_max_outer_height"]
    dab_ti_hi_val_parameter_min_outer_weight 					= parameter_df.at[0, "dab_ti_hi_val_parameter_min_outer_weight"]
    dab_ti_hi_val_parameter_max_outer_weight 					= parameter_df.at[0, "dab_ti_hi_val_parameter_max_outer_weight"]

    dab_ipo_parameter_patterns_single_case_l_to_l 				= parameter_df.at[0, "dab_ipo_parameter_patterns_single_case_l_to_l"]
    dab_ipo_parameter_patterns_single_case_w_to_l 				= parameter_df.at[0, "dab_ipo_parameter_patterns_single_case_w_to_l"]
    dab_ipo_parameter_patterns_single_row_l_to_l 				= parameter_df.at[0, "dab_ipo_parameter_patterns_single_row_l_to_l"]
    dab_ipo_parameter_patterns_single_row_w_to_l 				= parameter_df.at[0, "dab_ipo_parameter_patterns_single_row_w_to_l"]
    dab_ipo_parameter_patterns_single_row_l_to_w 				= parameter_df.at[0, "dab_ipo_parameter_patterns_single_row_l_to_w"]
    dab_ipo_parameter_patterns_single_row_w_to_w 				= parameter_df.at[0, "dab_ipo_parameter_patterns_single_row_w_to_w"]
    dab_ipo_parameter_patterns_uniform_l_to_l 					= parameter_df.at[0, "dab_ipo_parameter_patterns_uniform_l_to_l"]
    dab_ipo_parameter_patterns_uniform_w_to_l 					= parameter_df.at[0, "dab_ipo_parameter_patterns_uniform_w_to_l"]
    dab_ipo_parameter_patterns_dual_uniform_l_loading 			= parameter_df.at[0, "dab_ipo_parameter_patterns_dual_uniform_l_loading"]
    dab_ipo_parameter_patterns_dual_uniform_w_loading 			= parameter_df.at[0, "dab_ipo_parameter_patterns_dual_uniform_w_loading"]
    dab_ipo_parameter_patterns_complex 							= parameter_df.at[0, "dab_ipo_parameter_patterns_complex"]
    dab_ipo_parameter_max_recursion_depth 						= parameter_df.at[0, "dab_ipo_parameter_max_recursion_depth"]

    dab_ipo_parameter_multiple_layers 							= parameter_df.at[0, "dab_ipo_parameter_multiple_layers"]

    dab_ipo_parameter_outer_volume_utilisation 					= parameter_df.at[0, "dab_ipo_parameter_outer_volume_utilisation"]
    dab_ipo_parameter_max_inner_count 							= parameter_df.at[0, "dab_ipo_parameter_max_inner_count"]
    dab_ipo_parameter_top_layer_full 							= parameter_df.at[0, "dab_ipo_parameter_top_layer_full"]

    dab_ipo_parameter_outer_length 								= parameter_df.at[0, "dab_ipo_parameter_outer_length"]
    dab_ipo_parameter_outer_width 								= parameter_df.at[0, "dab_ipo_parameter_outer_width"]
    dab_ipo_parameter_outer_height 								= parameter_df.at[0, "dab_ipo_parameter_outer_height"]
    dab_ipo_parameter_outer_weight 								= parameter_df.at[0, "dab_ipo_parameter_outer_weight"]

    dab_ipo_parameter_gap_from_outer_lengthwise 				= parameter_df.at[0, "dab_ipo_parameter_gap_from_outer_lengthwise"]
    dab_ipo_parameter_gap_from_outer_widthwise 					= parameter_df.at[0, "dab_ipo_parameter_gap_from_outer_widthwise"]
    dab_ipo_parameter_gap_between_inners_lengthwise 			= parameter_df.at[0, "dab_ipo_parameter_gap_between_inners_lengthwise"]
    dab_ipo_parameter_gap_between_inners_widthwise 				= parameter_df.at[0, "dab_ipo_parameter_gap_between_inners_widthwise"]
    dab_ipo_parameter_output_ti 								= parameter_df.at[0, "dab_ipo_parameter_output_ti"]
    dab_ipo_parameter_output_hi 								= parameter_df.at[0, "dab_ipo_parameter_output_hi"]
    dab_ipo_parameter_output_inners_per_outer 					= parameter_df.at[0, "dab_ipo_parameter_output_inners_per_outer"]
    dab_ipo_parameter_output_selected_pattern_name 				= parameter_df.at[0, "dab_ipo_parameter_output_selected_pattern_name"]
    dab_ipo_parameter_output_plot_info 							= parameter_df.at[0, "dab_ipo_parameter_output_plot_info"]
    dab_ipo_parameter_output_max_ti 							= parameter_df.at[0, "dab_ipo_parameter_output_max_ti"]
    dab_ipo_parameter_output_max_hi 							= parameter_df.at[0, "dab_ipo_parameter_output_max_hi"]
    dab_ipo_parameter_output_flag_info 							= parameter_df.at[0, "dab_ipo_parameter_output_flag_info"]
    
    dab_ipo_parameter_sku_id_column_name 						= parameter_df.at[0, "dab_ipo_parameter_sku_id_column_name"]

    dab_ti_hi_val_parameter_length_column_name 					= parameter_df.at[0, "dab_ti_hi_val_parameter_length_column_name"]
    dab_ti_hi_val_parameter_width_column_name 					= parameter_df.at[0, "dab_ti_hi_val_parameter_width_column_name"]
    dab_ti_hi_val_parameter_height_column_name 					= parameter_df.at[0, "dab_ti_hi_val_parameter_height_column_name"]
    dab_ti_hi_val_parameter_weight_column_name 					= parameter_df.at[0, "dab_ti_hi_val_parameter_weight_column_name"]
    dab_ti_hi_val_parameter_ti_column_name 						= parameter_df.at[0, "dab_ti_hi_val_parameter_ti_column_name"]
    dab_ti_hi_val_parameter_hi_column_name 						= parameter_df.at[0, "dab_ti_hi_val_parameter_hi_column_name"]
    dab_ti_hi_val_parameter_ipo_column_name 					= parameter_df.at[0, "dab_ti_hi_val_parameter_ipo_column_name"]
    dab_ti_hi_val_parameter_incomplete_layers_allowed 			= parameter_df.at[0, "dab_ti_hi_val_parameter_incomplete_layers_allowed"]
    dab_ti_hi_val_parameter_parameter_accuracy_order 			= parameter_df.at[0, "dab_ti_hi_val_parameter_parameter_accuracy_order"]
    dab_ti_hi_val_parameter_output_flags 						= parameter_df.at[0, "dab_ti_hi_val_parameter_output_flags"]
    
    row_count = len(data_df)
    
    min_outer_volume = dab_ti_hi_val_parameter_min_outer_area * dab_ti_hi_val_parameter_min_outer_height
    max_outer_volume = dab_ti_hi_val_parameter_max_outer_area * dab_ti_hi_val_parameter_max_outer_height
    
    output_df["dab_tihi_cleanup_output_SKU_ID"] = ""
    
    output_df["dab_tihi_cleanup_output_ti"] = 0
    output_df["dab_tihi_cleanup_output_hi"] = 0
    output_df["dab_tihi_cleanup_output_ipo"] = 0
    
    output_df["FX_FLAG_ORIGINAL_VALUE_ti"] = 0
    output_df["FX_FLAG_ORIGINAL_VALUE_hi"] = 0
    output_df["FX_FLAG_ORIGINAL_VALUE_ipo"] = 0
    
    stats_ti_zero_failed = 0
    stats_ti_zero_passed = 0
    
    stats_hi_zero_failed = 0
    stats_hi_zero_passed = 0
    
    stats_cpp_zero_failed = 0
    stats_cpp_zero_passed = 0
    
    stats_cfop_passed = 0
    stats_cfop_failed = 0
    
    stats_layer_check_eligible_skus = 0
    stats_layer_check_not_eligible_skus = 0

    stats_lats_passed = 0
    stats_lats_failed = 0

    stats_latl_passed = 0
    stats_latl_failed = 0

    stats_lwtl_passed = 0
    stats_lwtl_failed = 0
    
    stats_layer_check_overall_passed = 0
    stats_layer_check_overall_failed = 0
    
    stats_hi_check_eligible_skus = 0
    stats_hi_check_not_eligible_skus = 0
    
    stats_phtl_passed = 0
    stats_phtl_failed = 0
    
    stats_phth_passed = 0
    stats_phth_failed = 0
    
    stats_hi_check_overall_passed = 0
    stats_hi_check_overall_failed = 0
    
    stats_ipo_check_eligible_skus = 0
    stats_ipo_check_not_eligible_skus = 0
    
    stats_pwtl_passed = 0
    stats_pwtl_failed = 0
    
    stats_pwtla_passed = 0
    stats_pwtla_failed = 0
    
    stats_pvtl_passed = 0
    stats_pvtl_failed = 0
    
    stats_pvth_passed = 0
    stats_pvth_failed = 0
    
    stats_ipo_check_overall_passed = 0
    stats_ipo_check_overall_failed = 0
    
    stats_tc_eligible = 0
    stats_tc_passed = 0
    stats_tc_failed_removing_ti = 0
    stats_tc_failed_removing_hi = 0
    stats_tc_failed_removing_cpp = 0
    
    stats_spr_eligible = 0
    stats_spr_success_ti = 0
    stats_spr_success_hi = 0
    stats_spr_success_ipo = 0
    stats_spr_failed_removing_ti = 0
    stats_spr_failed_removing_hi = 0
    stats_spr_failed_removing_cpp = 0
    
    stats_dpr_eligible = 0
    stats_dpr_success = 0
    stats_dpr_failed = 0
    
    stats_tpr_eligible = 0
    stats_tpr_success = 0
    
    stats_tripple_zero = 0
    
    stats_overall_modified_sku = 0
    stats_overall_modified_ti = 0
    stats_overall_modified_hi = 0
    stats_overall_modified_cpp = 0
    
    for index, row in data_df.iterrows():
    
        
        if ipo_value_df.at[index, "ipo_output_sku_id"] != data_df.at[index, dab_ipo_parameter_sku_id_column_name]:
            
            output_df = pd.DataFrame()
            statistics_df = pd.DataFrame()
            statistics_df.at[0, "Error"] = "Internal Error - SKU Name mismatch"
            output_df.at[0, "Error"] = "Internal Error - SKU Name mismatch"
            return output_df, statistics_df
        
        length_value 	= data_df.at[index, dab_ti_hi_val_parameter_length_column_name]
        width_value 	= data_df.at[index, dab_ti_hi_val_parameter_width_column_name]
        height_value 	= data_df.at[index, dab_ti_hi_val_parameter_height_column_name]
        weight_value 	= data_df.at[index, dab_ti_hi_val_parameter_weight_column_name]
        
        case_volume = length_value * width_value * height_value
        
        ti_value 		= data_df.at[index, dab_ti_hi_val_parameter_ti_column_name]
        hi_value 		= data_df.at[index, dab_ti_hi_val_parameter_hi_column_name]
        ipo_value 		= data_df.at[index, dab_ti_hi_val_parameter_ipo_column_name]
        
        
        layer_area = length_value * width_value * ti_value
        layer_weight = weight_value * ti_value
        outer_height = height_value * hi_value
        
        
        
        
        
        
        
        output_df.at[index, "dab_tihi_cleanup_output_SKU_ID"] 						= data_df.at[index, dab_ipo_parameter_sku_id_column_name]
        
        output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_ti"] 			= ti_value
        output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_hi"] 			= hi_value
        output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_ipo"] 			= ipo_value
        
        output_df.at[index, "FX_FLAG_ti_is_zero"] 							= 0
        output_df.at[index, "FX_FLAG_hi_is_zero"] 							= 0
        output_df.at[index, "FX_FLAG_cpp_is_zero"] 							= 0
        
        output_df.at[index, "FX_FLAG_case_too_large_for_pallet"] 			= 0
        
        output_df.at[index, "FX_FLAG_layer_area_too_small"] 				= 0
        output_df.at[index, "FX_FLAG_layer_area_too_large"] 				= 0
        
        output_df.at[index, "FX_FLAG_layer_weight_too_large"] 				= 0
        
        output_df.at[index, "FX_FLAG_pallet_height_too_low"] 				= 0
        output_df.at[index, "FX_FLAG_pallet_height_too_high"] 				= 0
        
        output_df.at[index, "FX_FLAG_pallet_weight_too_low"] 				= 0
        output_df.at[index, "FX_FLAG_pallet_weight_too_high"] 				= 0
        
        output_df.at[index, "FX_FLAG_pallet_volume_too_low"] 				= 0
        output_df.at[index, "FX_FLAG_pallet_volume_too_high"] 				= 0
        
        output_df.at[index, "FX_FLAG_eligible_for_tripple_coherence_test"]	= 0
        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] 		= ""
        
        output_df.at[index, "FX_FLAG_RECALC_missing_single_parameter_recalc_mspr"] 	= 0
        output_df.at[index, "FX_FLAG_RECALC_mspr_status"] 								= ""
        
        output_df.at[index, "FX_FLAG_RECALC_missing_two_parameters_recalc_mtpr"] 		= 0
        output_df.at[index, "FX_FLAG_RECALC_mtpr_status"] 								= ""
        
        output_df.at[index, "FX_FLAG_RECALC_Function_Error_2_values_remain"] = 0
        
        
        output_df.at[index, "FX_FLAG_RECALC_missing_all_parameters_recalc"] = 0
        
        
        if ti_value <= 0:
            output_df.at[index, "FX_FLAG_ti_is_zero"] = 1
            ti_value = 0
            stats_ti_zero_failed = stats_ti_zero_failed + 1
        else:
            stats_ti_zero_passed = stats_ti_zero_passed + 1
            
        if hi_value <= 0:
            hi_value = 0
            output_df.at[index, "FX_FLAG_hi_is_zero"] = 1
            stats_hi_zero_failed = stats_hi_zero_failed + 1
        else:
            stats_hi_zero_passed = stats_hi_zero_passed + 1
            
        if ipo_value <= 0:
            ipo_value = 0
            output_df.at[index, "FX_FLAG_cpp_is_zero"] = 1
            stats_cpp_zero_failed = stats_cpp_zero_failed + 1
        else:
            stats_cpp_zero_passed = stats_cpp_zero_passed + 1
        
        
        if ((min(length_value, width_value) > min(dab_ti_hi_val_parameter_max_outer_length, dab_ti_hi_val_parameter_max_outer_width)) or (max(length_value, width_value) > max(dab_ti_hi_val_parameter_max_outer_length, dab_ti_hi_val_parameter_max_outer_width))): 
            output_df.at[index, "FX_FLAG_case_too_large_for_pallet"] = 1
            stats_cfop_failed = stats_cfop_failed + 1
            ti_value = 0
        else:
            stats_cfop_passed = stats_cfop_passed + 1
        
        if (ti_value != 0):
            stats_layer_check_eligible_skus = stats_layer_check_eligible_skus + 1
        
            if (layer_area < dab_ti_hi_val_parameter_min_outer_area):
                output_df.at[index, "FX_FLAG_layer_area_too_small"] = 1
                stats_lats_failed = stats_lats_failed + 1
            else:
                stats_lats_passed = stats_lats_passed + 1
                
            if (dab_ti_hi_val_parameter_max_outer_area < layer_area):
                output_df.at[index, "FX_FLAG_layer_area_too_large"] = 1
                stats_latl_failed = stats_latl_failed + 1
            else:
                stats_latl_passed = stats_latl_passed + 1
                
            if (layer_weight > dab_ti_hi_val_parameter_max_outer_weight):
                output_df.at[index, "FX_FLAG_layer_weight_too_large"] = 1
                stats_lwtl_failed = stats_lwtl_failed + 1
            else:
                stats_lwtl_passed = stats_lwtl_passed + 1
        else:
            stats_layer_check_not_eligible_skus = stats_layer_check_not_eligible_skus + 1
        
        sum_of_flags = 0
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_layer_area_too_small"]
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_layer_area_too_large"]
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_layer_weight_too_large"]
        
        
        if sum_of_flags > 0:
            ti_value = 0
            stats_layer_check_overall_failed = stats_layer_check_overall_failed + 1
        else:
            if (ti_value != 0):
                stats_layer_check_overall_passed = stats_layer_check_overall_passed + 1
        
        if (hi_value != 0):
            stats_hi_check_eligible_skus = stats_hi_check_eligible_skus + 1
            if (outer_height < dab_ti_hi_val_parameter_min_outer_height):
                output_df.at[index, "FX_FLAG_pallet_height_too_low"] = 1
                stats_phtl_failed = stats_phtl_failed + 1
            else:
                stats_phtl_passed = stats_phtl_passed + 1
                
            if (dab_ti_hi_val_parameter_max_outer_height < outer_height):
                output_df.at[index, "FX_FLAG_pallet_height_too_high"] = 1
                stats_phth_failed = stats_phth_failed + 1
            else:
                stats_phth_passed = stats_phth_passed + 1
        else:
            stats_hi_check_not_eligible_skus = stats_hi_check_not_eligible_skus + 1
            
        sum_of_flags = 0
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_pallet_height_too_low"]
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_pallet_height_too_high"]
        
        if sum_of_flags > 0:
            hi_value = 0
            stats_hi_check_overall_failed = stats_hi_check_overall_failed + 1
        else:
            if (hi_value != 0):
                stats_hi_check_overall_passed = stats_hi_check_overall_passed + 1
        
        if (ipo_value != 0):
            stats_ipo_check_eligible_skus = stats_ipo_check_eligible_skus + 1
            if ((ipo_value * weight_value) < dab_ti_hi_val_parameter_min_outer_weight):
                output_df.at[index, "FX_FLAG_pallet_weight_too_low"] = 1
                stats_pwtl_failed = stats_pwtl_failed + 1
            else:
                stats_pwtl_passed = stats_pwtl_passed + 1
                
            if (dab_ti_hi_val_parameter_max_outer_weight < (ipo_value * weight_value)):
                output_df.at[index, "FX_FLAG_pallet_weight_too_high"] = 1
                stats_pwtla_failed = stats_pwtla_failed + 1
            else:
                stats_pwtla_passed = stats_pwtla_passed + 1
                
            
            if ((ipo_value * case_volume) < min_outer_volume):
                output_df.at[index, "FX_FLAG_pallet_volume_too_low"] = 1
                stats_pvtl_failed = stats_pvtl_failed + 1
            else:
                stats_pvtl_passed = stats_pvtl_passed + 1
                
            if (max_outer_volume < (ipo_value * case_volume)):
                output_df.at[index, "FX_FLAG_pallet_volume_too_high"] = 1
                stats_pvth_failed = stats_pvth_failed + 1
            else:
                stats_pvth_passed = stats_pvth_passed + 1
        else:
            stats_ipo_check_not_eligible_skus = stats_ipo_check_not_eligible_skus + 1
        
        sum_of_flags = 0
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_pallet_weight_too_low"]
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_pallet_weight_too_high"]
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_pallet_volume_too_low"]
        sum_of_flags = sum_of_flags + output_df.at[index, "FX_FLAG_pallet_volume_too_high"]
        
        if sum_of_flags > 0:
            ipo_value = 0
            stats_ipo_check_overall_failed = stats_ipo_check_overall_failed + 1
        else:
            if (ipo_value != 0):
                stats_ipo_check_overall_passed = stats_ipo_check_overall_passed + 1
        
        
        if ti_value > 0 and hi_value > 0 and ipo_value > 0:
            stats_tc_eligible = stats_tc_eligible + 1
            output_df.at[index, "FX_FLAG_eligible_for_tripple_coherence_test"] = 1
            
            cpp_high = ti_value * hi_value
            cpp_low = ti_value * (hi_value-1) + 1 
            
            if dab_ti_hi_val_parameter_incomplete_layers_allowed == "Yes":

                if (ipo_value < cpp_low) or (cpp_high < ipo_value):
                    
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                        hi_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing HI"
                        stats_tc_failed_removing_hi = stats_tc_failed_removing_hi + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                        ipo_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing CPP"
                        stats_tc_failed_removing_cpp = stats_tc_failed_removing_cpp + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                        hi_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing HI"
                        stats_tc_failed_removing_hi = stats_tc_failed_removing_hi + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                        ti_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing TI"
                        stats_tc_failed_removing_ti = stats_tc_failed_removing_ti + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                        ipo_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing CPP"
                        stats_tc_failed_removing_cpp = stats_tc_failed_removing_cpp + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                        ti_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing TI"
                        stats_tc_failed_removing_ti = stats_tc_failed_removing_ti + 1
                else:
                    output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Passed!"
                    stats_tc_passed = stats_tc_passed + 1
                        
            else:
                if cpp_high != ipo_value:
                
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                        hi_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing HI"
                        stats_tc_failed_removing_hi = stats_tc_failed_removing_hi + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                        ipo_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing CPP"
                        stats_tc_failed_removing_cpp = stats_tc_failed_removing_cpp + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                        hi_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing HI"
                        stats_tc_failed_removing_hi = stats_tc_failed_removing_hi + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                        ti_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing TI"
                        stats_tc_failed_removing_ti = stats_tc_failed_removing_ti + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                        ipo_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing CPP"
                        stats_tc_failed_removing_cpp = stats_tc_failed_removing_cpp + 1
                    if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                        ti_value = 0
                        output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Fail: Removing TI"
                        stats_tc_failed_removing_ti = stats_tc_failed_removing_ti + 1
                else:
                    output_df.at[index, "FX_FLAG_tripple_coherence_test_status"] = "Passed!"
                    stats_tc_passed = stats_tc_passed + 1
        
        
        number_of_remaining_values = 0
        if ti_value > 0:
            number_of_remaining_values = number_of_remaining_values + 1
            
        if hi_value > 0:
            number_of_remaining_values = number_of_remaining_values + 1
            
        if ipo_value > 0:
            number_of_remaining_values = number_of_remaining_values + 1
        
        if number_of_remaining_values == 2:
            stats_spr_eligible = stats_spr_eligible + 1
            if (ti_value > 0) and (hi_value > 0):
                output_df.at[index, "FX_FLAG_RECALC_missing_single_parameter_recalc_mspr"] = 1
                
                
                cpp_high = ti_value * hi_value
                cpp_low = ti_value * (hi_value-1) + 1 
                cpp_weight = math.floor(dab_ti_hi_val_parameter_max_outer_weight / weight_value)
                cpp_volume = math.floor(max_outer_volume / case_volume)
                cpp_restriction = min(cpp_weight, cpp_volume)
            
            
            
                if dab_ti_hi_val_parameter_incomplete_layers_allowed == "Yes":
                    if cpp_high <= cpp_restriction:
                        ipo_value = cpp_high
                        output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Success: Recalculated CPP"
                        stats_spr_success_ipo = stats_spr_success_ipo + 1
                    else:
                        if cpp_low <= cpp_restriction:
                            ipo_value = cpp_restriction
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Success: Recalculated CPP"
                            stats_spr_success_ipo = stats_spr_success_ipo + 1
                        else:
                            
                            ipo_value = 0
                            
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                hi_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                hi_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                hi_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                                stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                                ti_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                                stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                                ti_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                                stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                                ti_value = 0
                            
                else:
                    
                    if cpp_high <= cpp_restriction:
                        ipo_value = cpp_high
                        output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Success: Recalculated CPP"
                        stats_spr_success_ipo = stats_spr_success_ipo + 1
                    else:
                        
                        ipo_value = 0
                        
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
            
            
            if (ti_value > 0) and (ipo_value > 0) and (output_df.at[index, "FX_FLAG_RECALC_mspr_status"] == ""):
                output_df.at[index, "FX_FLAG_RECALC_missing_single_parameter_recalc_mspr"] = 1
                
                hi_max = math.ceil(ipo_value / ti_value)
                hi_min = math.floor(ipo_value / ti_value)
                
                
                if dab_ti_hi_val_parameter_incomplete_layers_allowed == "Yes":
                    outer_height = hi_max * hi_value
                    if ((outer_height >= dab_ti_hi_val_parameter_min_outer_height) or (dab_ti_hi_val_parameter_max_outer_height >= outer_height)):
                        hi_value = hi_max
                        output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Success: Recalculated HI"
                        stats_spr_success_hi = stats_spr_success_hi + 1
                    else:
                        hi_value = 0
                        
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                    
                    
                else:
                    outer_height = hi_max * hi_value
                    if hi_max == hi_min and ((outer_height >= dab_ti_hi_val_parameter_min_outer_height) or (dab_ti_hi_val_parameter_max_outer_height >= outer_height)):
                        hi_value = hi_max
                    else:
                        hi_value = 0
                        
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing TI"
                            stats_spr_failed_removing_ti = stats_spr_failed_removing_ti + 1
                            ti_value = 0
                    
                    
                    
                    
            
            if (ipo_value > 0) and (hi_value > 0) and (output_df.at[index, "FX_FLAG_RECALC_mspr_status"] == ""):
                output_df.at[index, "FX_FLAG_RECALC_missing_single_parameter_recalc_mspr"] = 1
                ti_estimate_low = math.floor(ipo_value / hi_value)
                ti_estimate_high = math.ceil(ipo_value / hi_value)
                
                if ti_estimate_low == ti_estimate_high:
                    ti_value_to_check = ti_estimate_low
                    
                    layer_area = ti_value_to_check * length_value * width_value
                    layer_weight = weight_value * ti_value_to_check
                    
                    
                    if ipo_value_df.at[index, "ipo_output_max_ti"] == 0:
                        ti_value_to_check = 0
                        
                    if (layer_area < dab_ti_hi_val_parameter_min_outer_area) or (dab_ti_hi_val_parameter_max_outer_area < layer_area):
                        ti_value_to_check = 0
                        
                    if layer_weight > dab_ti_hi_val_parameter_max_outer_weight:
                        ti_value_to_check = 0
                        
                    if ti_value_to_check == 0:
                        ti_value = 0
                        
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                    else:
                        output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Success: Recalculated TI"
                        stats_spr_success_ti = stats_spr_success_ti + 1
                        ti_value = ti_value_to_check
                    
                else:
                    
                    if dab_ti_hi_val_parameter_incomplete_layers_allowed == "Yes":
                        
                        bottom_layer_ti = ti_estimate_high
                        
                        full_bottom_layer_cases = (hi_value - 1) * bottom_layer_ti
                        top_layer_cases = ipo_value - full_bottom_layer_cases
                        
                        if top_layer_cases < 1:
                            ti_value = 0
                        
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                hi_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                                stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                                ipo_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                hi_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                hi_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                                stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                                ipo_value = 0
                                
                            if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                                stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                                ipo_value = 0
                        else:
                            
                            
                            layer_area = full_bottom_layer_cases * length_value * width_value
                            layer_weight = weight_value * full_bottom_layer_cases
                            
                            if ipo_value_df.at[index, "ipo_output_max_ti"] == 0:
                                full_bottom_layer_cases = 0
                                
                            if (layer_area < dab_ti_hi_val_parameter_min_outer_area) or (dab_ti_hi_val_parameter_max_outer_area < layer_area):
                                full_bottom_layer_cases = 0
                                
                            if layer_weight > dab_ti_hi_val_parameter_max_outer_weight:
                                full_bottom_layer_cases = 0
                            ti_value = full_bottom_layer_cases
                            
                            if ti_value == 0:
                                if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                                    output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                    stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                    hi_value = 0
                                    
                                if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                                    output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                                    stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                                    ipo_value = 0
                                    
                                if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                                    output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                    stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                    hi_value = 0
                                    
                                if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                                    output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                                    stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                                    hi_value = 0
                                    
                                if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                                    output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                                    stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                                    ipo_value = 0
                                    
                                if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                                    output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                                    stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                                    ipo_value = 0
                            else:
                                output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Success: Recalculated TI"
                                stats_spr_success_ti = stats_spr_success_ti + 1
                    else:
                        ti_value = 0
                        
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > CPP > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "TI > HI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > TI > HI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "CPP > HI > TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing HI"
                            stats_spr_failed_removing_hi = stats_spr_failed_removing_hi + 1
                            hi_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > TI > CPP":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
                            
                        if dab_ti_hi_val_parameter_parameter_accuracy_order == "HI > CPP> TI":
                            output_df.at[index, "FX_FLAG_RECALC_mspr_status"] = "Fail: Removing CPP"
                            stats_spr_failed_removing_cpp = stats_spr_failed_removing_cpp + 1
                            ipo_value = 0
            
            
        number_of_remaining_values = 0
        if ti_value > 0:
            number_of_remaining_values = number_of_remaining_values + 1
            
        if hi_value > 0:
            number_of_remaining_values = number_of_remaining_values + 1
            
        if ipo_value > 0:
            number_of_remaining_values = number_of_remaining_values + 1
        
        if number_of_remaining_values == 1:
            stats_dpr_eligible = stats_dpr_eligible + 1
            if ti_value > 0:
                output_df.at[index, "FX_FLAG_RECALC_missing_two_parameters_recalc_mtpr"] 		= 1
                
                
                cpp_restriction_1 = math.floor(dab_ipo_parameter_outer_height /  height_value) * ti_value
                cpp_restriction_2 = math.floor(dab_ipo_parameter_outer_weight / weight_value)
                ipo_value = min(cpp_restriction_1, cpp_restriction_2, dab_ipo_parameter_max_inner_count)
                
                if dab_ipo_parameter_top_layer_full == 1:
                    if ipo_value > 0:
                        hi_value = math.floor(ipo_value / ti_value)
                        ipo_value = ti_value * hi_value
                        output_df.at[index, "FX_FLAG_RECALC_mtpr_status"] = "Success!"
                        stats_dpr_success = stats_dpr_success + 1
                    else:
                        ti_value = 0
                        hi_value = 0
                        ipo_value = 0
                        stats_dpr_failed = stats_dpr_failed + 1
                        number_of_remaining_values = 0
                     
                else:
                    if ipo_value > 0:
                        hi_value = math.ceil(ipo_value / ti_value)
                        output_df.at[index, "FX_FLAG_RECALC_mtpr_status"] = "Success!"
                        stats_dpr_success = stats_dpr_success + 1
                    else:
                        ti_value = 0
                        hi_value = 0
                        ipo_value = 0
                        stats_dpr_failed = stats_dpr_failed + 1
                        number_of_remaining_values = 0
                
            else:	
                if hi_value > 0:
                    output_df.at[index, "FX_FLAG_RECALC_missing_two_parameters_recalc_mtpr"] 		= 1
                   
                    ti_value = ipo_value_df.at[index, "ipo_output_ti"]
                    cpp_restriction_1 = math.floor(min((dab_ipo_parameter_outer_height /  height_value), hi_value)) * ti_value
                    cpp_restriction_2 = math.floor(dab_ipo_parameter_outer_weight / weight_value)
                    
                    cpp_restriction_3 = (dab_ipo_parameter_outer_length * dab_ipo_parameter_outer_width * dab_ipo_parameter_outer_height * dab_ipo_parameter_outer_volume_utilisation) / (length_value * width_value * height_value) #Not applicable, as Ti may have overhangs, and that is fine
                    
                    ipo_value = min(cpp_restriction_1, cpp_restriction_2, cpp_restriction_3, dab_ipo_parameter_max_inner_count)
                    
                    if dab_ipo_parameter_top_layer_full == 1:
                        if ipo_value > 0:
                            hi_value = math.floor(ipo_value / ti_value)
                            ipo_value = ti_value * hi_value
                            output_df.at[index, "FX_FLAG_RECALC_mtpr_status"] = "Success!"
                            stats_dpr_success = stats_dpr_success + 1
                        else:
                            ti_value = 0
                            hi_value = 0
                            ipo_value = 0
                            stats_dpr_failed = stats_dpr_failed + 1
                            number_of_remaining_values = 0
                    else:
                        if ipo_value > 0:
                            hi_value = math.ceil(ipo_value / ti_value)
                            output_df.at[index, "FX_FLAG_RECALC_mtpr_status"] = "Success!"
                            stats_dpr_success = stats_dpr_success + 1
                        else:
                            ti_value = 0
                            hi_value = 0
                            ipo_value = 0
                            stats_dpr_failed = stats_dpr_failed + 1
                            number_of_remaining_values = 0
                else:
                    if ipo_value > 0:
                        output_df.at[index, "FX_FLAG_RECALC_missing_two_parameters_recalc_mtpr"] 		= 1
                        
                        ti_value = ipo_value_df.at[index, "ipo_output_ti"]
                        cpp_restriction_1 = math.floor(dab_ipo_parameter_outer_height /  height_value) * ti_value
                        cpp_restriction_2 = math.floor(dab_ipo_parameter_outer_weight / weight_value)
                        
                        cpp_restriction_3 = (dab_ipo_parameter_outer_length * dab_ipo_parameter_outer_width * dab_ipo_parameter_outer_height * dab_ipo_parameter_outer_volume_utilisation) / (length_value * width_value * height_value) #Not applicable, as Ti may have overhangs, and that is fine
                        ipo_value = min(cpp_restriction_1, cpp_restriction_2, cpp_restriction_3, dab_ipo_parameter_max_inner_count, ipo_value)
                        if dab_ipo_parameter_top_layer_full == 1:
                            if ipo_value > 0:
                                hi_value = math.floor(ipo_value / ti_value)
                                ipo_value = ti_value * hi_value
                                output_df.at[index, "FX_FLAG_RECALC_mtpr_status"] = "Success!"
                                stats_dpr_success = stats_dpr_success + 1
                            else:
                                ti_value = 0
                                hi_value = 0
                                ipo_value = 0
                                stats_dpr_failed = stats_dpr_failed + 1
                                number_of_remaining_values = 0
                        else:
                            if ipo_value > 0:
                                hi_value = math.ceil(ipo_value / ti_value)
                                output_df.at[index, "FX_FLAG_RECALC_mtpr_status"] = "Success!"
                                stats_dpr_success = stats_dpr_success + 1
                            else:
                                ti_value = 0
                                hi_value = 0
                                ipo_value = 0
                                stats_dpr_failed = stats_dpr_failed + 1
                                number_of_remaining_values = 0
                            
        
        if number_of_remaining_values == 2:
            
            output_df.at[index, "FX_FLAG_RECALC_Function_Error_2_values_remain"] = 1
            
            ti_value = 0
            hi_value = 0
            ipo_value = 0
            number_of_remaining_values = 0
            
        if number_of_remaining_values == 3:
            
            output_df.at[index, "FX_FLAG_RECALC_Function_Error_2_values_remain"] = 0
        
        if number_of_remaining_values == 0:
            stats_tpr_eligible = stats_tpr_eligible + 1
            
            ti_value = ipo_value_df.at[index, "ipo_output_ti"]
            hi_value = ipo_value_df.at[index, "ipo_output_hi"]
            ipo_value = ipo_value_df.at[index, "ipo_output_inners_per_outer"]
            
            if (ti_value > 0) and (hi_value > 0) and (ipo_value > 0):
                stats_tpr_success = stats_tpr_success + 1
                output_df.at[index, "FX_FLAG_RECALC_missing_all_parameters_recalc"] = 1
            else:
                ti_value = 0
                hi_value = 0
                ipo_value = 0
        
        if (ti_value == 0) or (hi_value == 0) or (ipo_value == 0):
            ti_value = 0
            hi_value = 0
            ipo_value = 0
            stats_tripple_zero = stats_tripple_zero + 1
        
        
        output_df.at[index, "dab_tihi_cleanup_output_ti"] 		= ti_value
        output_df.at[index, "dab_tihi_cleanup_output_hi"] 		= hi_value
        output_df.at[index, "dab_tihi_cleanup_output_ipo"] 		= ipo_value
        
        if ti_value != output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_ti"]:
            stats_overall_modified_ti = stats_overall_modified_ti + 1
            
        if hi_value != output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_hi"]:
            stats_overall_modified_hi = stats_overall_modified_hi + 1
            
        if ipo_value != output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_ipo"]:
            stats_overall_modified_cpp = stats_overall_modified_cpp + 1
    
        if (ti_value != output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_ti"]) or (hi_value != output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_hi"]) or (ipo_value != output_df.at[index, "FX_FLAG_ORIGINAL_VALUE_ipo"]):
            stats_overall_modified_sku = stats_overall_modified_sku + 1
    
    
    
    statistics_df = add_row_to_df() 
    
    statistics_df = add_row_to_df(statistics_df, "Received Data")
    statistics_df = add_row_to_df(statistics_df, "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@")
    statistics_df = add_row_to_df(statistics_df, "Name", 										"Value")
    statistics_df = add_row_to_df(statistics_df, "Total Rows", 									format_float_with_commas(row_count))
    statistics_df = add_row_to_df(statistics_df, "Unique SKU IDs", 								format_float_with_commas(data_df[dab_ipo_parameter_sku_id_column_name].nunique()))
    statistics_df = add_row_to_df(statistics_df)
    
    
    statistics_df = add_row_to_df(statistics_df, "TI HI CPP Validation Criteria")
    statistics_df = add_row_to_df(statistics_df, "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@")
    statistics_df = add_row_to_df(statistics_df, "Name", 										"Value")
    statistics_df = add_row_to_df(statistics_df, "max_outer_length", 							format_float_with_commas(dab_ti_hi_val_parameter_max_outer_length,4))
    statistics_df = add_row_to_df(statistics_df, "max_outer_width", 							format_float_with_commas(dab_ti_hi_val_parameter_max_outer_width,4))
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "min_outer_area", 								format_float_with_commas(dab_ti_hi_val_parameter_min_outer_area,4))
    statistics_df = add_row_to_df(statistics_df, "max_outer_area", 								format_float_with_commas(dab_ti_hi_val_parameter_max_outer_area,4))
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "min_outer_height", 							format_float_with_commas(dab_ti_hi_val_parameter_min_outer_height,4))
    statistics_df = add_row_to_df(statistics_df, "max_outer_height", 							format_float_with_commas(dab_ti_hi_val_parameter_max_outer_height,4))
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "min_outer_weight", 							format_float_with_commas(dab_ti_hi_val_parameter_min_outer_weight,4))
    statistics_df = add_row_to_df(statistics_df, "max_outer_weight", 							format_float_with_commas(dab_ti_hi_val_parameter_max_outer_weight,4))
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "incomplete_layers_allowed", 					dab_ti_hi_val_parameter_incomplete_layers_allowed)
    statistics_df = add_row_to_df(statistics_df, "parameter_accuracy_order", 					dab_ti_hi_val_parameter_parameter_accuracy_order)
    statistics_df = add_row_to_df(statistics_df)
    
    
    statistics_df = add_row_to_df(statistics_df, "TI HI CPP Recalculation Criteria")
    statistics_df = add_row_to_df(statistics_df, "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@")
    statistics_df = add_row_to_df(statistics_df, "TI Patterns")
    statistics_df = add_row_to_df(statistics_df, "Name", 										"Value")
    statistics_df = add_row_to_df(statistics_df, "single_case_l_to_l", 							dab_ipo_parameter_patterns_single_case_l_to_l)
    statistics_df = add_row_to_df(statistics_df, "single_case_w_to_l", 							dab_ipo_parameter_patterns_single_case_w_to_l)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "single_row_l_to_l", 							dab_ipo_parameter_patterns_single_row_l_to_l)
    statistics_df = add_row_to_df(statistics_df, "single_row_w_to_l", 							dab_ipo_parameter_patterns_single_row_w_to_l)
    statistics_df = add_row_to_df(statistics_df, "single_row_l_to_w", 							dab_ipo_parameter_patterns_single_row_l_to_w)
    statistics_df = add_row_to_df(statistics_df, "single_row_w_to_w", 							dab_ipo_parameter_patterns_single_row_w_to_w)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "uniform_l_to_l", 								dab_ipo_parameter_patterns_uniform_l_to_l)
    statistics_df = add_row_to_df(statistics_df, "uniform_w_to_l", 								dab_ipo_parameter_patterns_uniform_w_to_l)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "dual_uniform_l_loading", 						dab_ipo_parameter_patterns_dual_uniform_l_loading)
    statistics_df = add_row_to_df(statistics_df, "dual_uniform_w_loading", 						dab_ipo_parameter_patterns_dual_uniform_w_loading)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "complex", 									dab_ipo_parameter_patterns_complex)
    statistics_df = add_row_to_df(statistics_df, "max_recursion_depth", 						dab_ipo_parameter_max_recursion_depth)
    statistics_df = add_row_to_df(statistics_df)
    
    statistics_df = add_row_to_df(statistics_df, "Restrictions")
    statistics_df = add_row_to_df(statistics_df, "Name", 										"Value")
    statistics_df = add_row_to_df(statistics_df, "multiple_layers", 							dab_ipo_parameter_multiple_layers)
    statistics_df = add_row_to_df(statistics_df, "outer_weight", 								format_float_with_commas(dab_ipo_parameter_outer_weight,2))
    statistics_df = add_row_to_df(statistics_df, "outer_volume_utilisation", 					format_float_with_commas(dab_ipo_parameter_outer_volume_utilisation,2))
    statistics_df = add_row_to_df(statistics_df, "max_inner_count", 							format_float_with_commas(dab_ipo_parameter_max_inner_count,2))
    statistics_df = add_row_to_df(statistics_df, "top_layer_full", 								dab_ipo_parameter_top_layer_full)
    statistics_df = add_row_to_df(statistics_df)
    
    statistics_df = add_row_to_df(statistics_df, "Other Settings")
    statistics_df = add_row_to_df(statistics_df, "Name",  										"Value")
    statistics_df = add_row_to_df(statistics_df, "outer_length", 								format_float_with_commas(dab_ipo_parameter_outer_length,4))
    statistics_df = add_row_to_df(statistics_df, "outer_width", 								format_float_with_commas(dab_ipo_parameter_outer_width,4))
    statistics_df = add_row_to_df(statistics_df, "outer_height", 								format_float_with_commas(dab_ipo_parameter_outer_height,4))
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "gap_from_outer_lengthwise", 					format_float_with_commas(dab_ipo_parameter_gap_from_outer_lengthwise,4))
    statistics_df = add_row_to_df(statistics_df, "gap_from_outer_widthwise", 					format_float_with_commas(dab_ipo_parameter_gap_from_outer_widthwise,4))
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "gap_between_inners_lengthwise", 				format_float_with_commas(dab_ipo_parameter_gap_between_inners_lengthwise,4))
    statistics_df = add_row_to_df(statistics_df, "gap_between_inners_widthwise", 				format_float_with_commas(dab_ipo_parameter_gap_between_inners_widthwise,4))
    statistics_df = add_row_to_df(statistics_df)
    
    statistics_df = add_row_to_df(statistics_df, "Function Statistics")
    statistics_df = add_row_to_df(statistics_df, "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@")
    statistics_df = add_row_to_df(statistics_df, "Isolated Parameter Tests")
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Test", 								"Passed", 							"Failed", 								"Total")
    statistics_df = add_row_to_df(statistics_df, "TI > 0", 								stats_ti_zero_passed, 				stats_ti_zero_failed, 					stats_ti_zero_passed + stats_ti_zero_failed)
    statistics_df = add_row_to_df(statistics_df, "HI > 0", 								stats_hi_zero_passed, 				stats_hi_zero_failed, 					stats_hi_zero_passed + stats_hi_zero_failed)
    statistics_df = add_row_to_df(statistics_df, "CPP > 0", 							stats_cpp_zero_passed, 				stats_cpp_zero_failed, 					stats_cpp_zero_passed + stats_cpp_zero_failed)
    statistics_df = add_row_to_df(statistics_df, "Case fits on a pallet", 				stats_cfop_passed, 					stats_cfop_failed, 						stats_cfop_passed + stats_cfop_failed)
    statistics_df = add_row_to_df(statistics_df)
    
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Test", 								"Passed", 							"Failed", 								"Total")
    statistics_df = add_row_to_df(statistics_df, "SKUs eligible for TI tests", 			stats_layer_check_eligible_skus, 	stats_layer_check_not_eligible_skus, 	stats_layer_check_eligible_skus + stats_layer_check_not_eligible_skus)
    statistics_df = add_row_to_df(statistics_df, "Layer area too small", 				stats_lats_passed, 					stats_lats_failed, 						stats_lats_passed + stats_lats_failed)
    statistics_df = add_row_to_df(statistics_df, "Layer area too large", 				stats_latl_passed, 					stats_latl_failed, 						stats_latl_passed + stats_latl_failed)
    statistics_df = add_row_to_df(statistics_df, "Layer weight too large", 				stats_lwtl_passed, 					stats_lwtl_failed, 						stats_lwtl_passed + stats_lwtl_failed)
    statistics_df = add_row_to_df(statistics_df, "Overall TI Tests", 					stats_layer_check_overall_passed, 	stats_layer_check_overall_failed, 		stats_layer_check_overall_passed + stats_layer_check_overall_failed)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Test", 								"Passed", 							"Failed", 								"Total")
    statistics_df = add_row_to_df(statistics_df, "SKUs eligible for HI tests", 			stats_hi_check_eligible_skus, 		stats_hi_check_not_eligible_skus, 		stats_hi_check_eligible_skus + stats_hi_check_not_eligible_skus)
    statistics_df = add_row_to_df(statistics_df, "Pallet height too low", 				stats_phtl_passed, 					stats_phtl_failed, 						stats_phtl_passed + stats_phtl_failed)
    statistics_df = add_row_to_df(statistics_df, "Pallet height too high", 				stats_phth_passed, 					stats_phth_failed, 						stats_phth_passed + stats_phth_failed)
    statistics_df = add_row_to_df(statistics_df, "Overall HI Tests", 					stats_hi_check_overall_passed, 		stats_hi_check_overall_failed, 			stats_hi_check_overall_passed + stats_hi_check_overall_failed)
    
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Test", 								"Passed", 							"Failed", 								"Total")
    statistics_df = add_row_to_df(statistics_df, "SKUs eligible for CPP tests", 		stats_ipo_check_eligible_skus,		stats_ipo_check_not_eligible_skus, 		stats_ipo_check_eligible_skus + stats_ipo_check_not_eligible_skus)
    statistics_df = add_row_to_df(statistics_df, "Pallet weight too low", 				stats_pwtl_passed, 					stats_pwtl_failed, 						stats_pwtl_passed + stats_pwtl_failed)
    statistics_df = add_row_to_df(statistics_df, "Pallet weight too large", 			stats_pwtla_passed, 				stats_pwtla_failed, 					stats_pwtla_passed + stats_pwtla_failed)
    statistics_df = add_row_to_df(statistics_df, "Pallet volume too low", 				stats_pvtl_passed, 					stats_pvtl_failed, 						stats_pvtl_passed + stats_pvtl_failed)
    statistics_df = add_row_to_df(statistics_df, "Pallet volume too high", 				stats_pvth_passed, 					stats_pvth_failed, 						stats_pvth_passed + stats_pvth_failed)
    statistics_df = add_row_to_df(statistics_df, "Overall CPP Tests", 					stats_ipo_check_overall_passed, 	stats_ipo_check_overall_failed, 		stats_ipo_check_overall_passed + stats_ipo_check_overall_failed)
    
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Tripple Coherence Test")
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Name", "Value")
    statistics_df = add_row_to_df(statistics_df, "Eligible SKUs", 								stats_tc_eligible)
    statistics_df = add_row_to_df(statistics_df, "Passed", 										stats_tc_passed)
    statistics_df = add_row_to_df(statistics_df, "parameter_accuracy_order", 					dab_ti_hi_val_parameter_parameter_accuracy_order)
    statistics_df = add_row_to_df(statistics_df, "Failed: Removing TI", 						stats_tc_failed_removing_ti)
    statistics_df = add_row_to_df(statistics_df, "Failed: Removing HI", 						stats_tc_failed_removing_hi)
    statistics_df = add_row_to_df(statistics_df, "Failed: Removing CPP", 						stats_tc_failed_removing_cpp)
    
    
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Single Parameter Recalculation")
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Name", "Value")
    statistics_df = add_row_to_df(statistics_df, "Eligible SKUs", stats_spr_eligible)
    statistics_df = add_row_to_df(statistics_df, "Successfully Recalculated TI", stats_spr_success_ti)
    statistics_df = add_row_to_df(statistics_df, "Successfully Recalculated HI", stats_spr_success_hi)
    statistics_df = add_row_to_df(statistics_df, "Successfully Recalculated CPP", stats_spr_success_ipo)
    statistics_df = add_row_to_df(statistics_df, "parameter_accuracy_order", 					dab_ti_hi_val_parameter_parameter_accuracy_order)
    statistics_df = add_row_to_df(statistics_df, "Failed: Removing TI", stats_spr_failed_removing_ti)
    statistics_df = add_row_to_df(statistics_df, "Failed: Removing HI", stats_spr_failed_removing_hi)
    statistics_df = add_row_to_df(statistics_df, "Failed: Removing CPP", stats_spr_failed_removing_cpp)
    
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Dual Parameter Recalculation")
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Name", "Value")
    statistics_df = add_row_to_df(statistics_df, "Eligible SKUs", stats_dpr_eligible)
    statistics_df = add_row_to_df(statistics_df, "Successfully Recalculated", stats_dpr_success)
    statistics_df = add_row_to_df(statistics_df, "Failed", stats_dpr_failed)
    
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Tripple Parameter Recalculation")
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Name", "Value")
    statistics_df = add_row_to_df(statistics_df, "Eligible SKUs", stats_tpr_eligible)
    statistics_df = add_row_to_df(statistics_df, "Successfully Recalculated", stats_tpr_success)
    statistics_df = add_row_to_df(statistics_df)
    
    
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, "Total Rows", format_float_with_commas(row_count))
    statistics_df = add_row_to_df(statistics_df, "Overall Modified SKUs", stats_overall_modified_sku)
    statistics_df = add_row_to_df(statistics_df, "Overall Modified ti", stats_overall_modified_ti)
    statistics_df = add_row_to_df(statistics_df, "Overall Modified hi", stats_overall_modified_hi)
    statistics_df = add_row_to_df(statistics_df, "Overall Modified cpp", stats_overall_modified_cpp)
    statistics_df = add_row_to_df(statistics_df, "All values set to 0", stats_tripple_zero)
    statistics_df = add_row_to_df(statistics_df)
    
    
    
    
    statistics_df = statistics_df.loc[:, (statistics_df != "").any()]


    return output_df, statistics_df


data_df = input_1.to_pandas()
parameter_df = input_2.to_pandas()

data_df = data_df.reset_index(drop=True)
parameter_df = parameter_df.reset_index(drop=True)





parameter_df.at[0, 'dab_ipo_parameter_sku_id_column_name']                          = self.column_param_sku_id

parameter_df.at[0, 'dab_ti_hi_val_parameter_length_column_name']                    = self.column_param_length
parameter_df.at[0, 'dab_ti_hi_val_parameter_width_column_name']                     = self.column_param_width
parameter_df.at[0, 'dab_ti_hi_val_parameter_height_column_name']                    = self.column_param_height
parameter_df.at[0, 'dab_ti_hi_val_parameter_weight_column_name']                    = self.column_param_weight


parameter_df.at[0, 'dab_ti_hi_val_parameter_ti_column_name']                        = self.column_param_ti
parameter_df.at[0, 'dab_ti_hi_val_parameter_hi_column_name']                        = self.column_param_hi
parameter_df.at[0, 'dab_ti_hi_val_parameter_ipo_column_name']                       = self.column_param_cpp
parameter_df.at[0, 'dab_ti_hi_val_parameter_incomplete_layers_allowed']             = self.selection_incomplete_layers
parameter_df.at[0, 'dab_ti_hi_val_parameter_parameter_accuracy_order']              = self.selection_parameter_accuracy_order
parameter_df.at[0, 'dab_ti_hi_val_parameter_output_flags']                          = self.selection_output_flags





parameter_df.at[0, 'dab_ipo_parameter_inner_length_column_name']					= parameter_df.at[0, 'dab_ti_hi_val_parameter_length_column_name']
parameter_df.at[0, 'dab_ipo_parameter_inner_width_column_name']						= parameter_df.at[0, 'dab_ti_hi_val_parameter_width_column_name']
parameter_df.at[0, 'dab_ipo_parameter_inner_height_column_name']					= parameter_df.at[0, 'dab_ti_hi_val_parameter_height_column_name']
parameter_df.at[0, 'dab_ipo_parameter_inner_weight_column_name']					= parameter_df.at[0, 'dab_ti_hi_val_parameter_weight_column_name']


ipo_value_df = dab_inners_per_outer(data_df, parameter_df)
plot_df_0, plot_df_1, plot_df_2, plot_df_3 = dab_inners_per_outer_statistics(data_df, parameter_df, ipo_value_df)







validation_output_df, validation_function_summary_df = dab_ti_hi_validation(data_df, parameter_df, ipo_value_df)


output_df = data_df.copy(deep=True)
sku_col_name_df_1 = parameter_df.at[0, 'dab_ipo_parameter_sku_id_column_name']
sku_col_name_df_2 = "dab_tihi_cleanup_output_SKU_ID"



if parameter_df.at[0, 'dab_ti_hi_val_parameter_output_flags'] == "No":
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "dab_tihi_cleanup_output_ti")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "dab_tihi_cleanup_output_hi")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "dab_tihi_cleanup_output_ipo")
else:
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "dab_tihi_cleanup_output_ti")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "dab_tihi_cleanup_output_hi")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "dab_tihi_cleanup_output_ipo")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_ORIGINAL_VALUE_ti")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_ORIGINAL_VALUE_hi")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_ORIGINAL_VALUE_ipo")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_ti_is_zero")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_hi_is_zero")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_cpp_is_zero")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_case_too_large_for_pallet")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_layer_area_too_small")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_layer_area_too_large")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_layer_weight_too_large")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_pallet_height_too_low")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_pallet_height_too_high")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_pallet_weight_too_low")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_pallet_weight_too_high")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_pallet_volume_too_low")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_pallet_volume_too_high")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_eligible_for_tripple_coherence_test")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_tripple_coherence_test_status")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_RECALC_missing_single_parameter_recalc_mspr")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_RECALC_mspr_status")
    
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_RECALC_missing_two_parameters_recalc_mtpr")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_RECALC_mtpr_status")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_RECALC_Function_Error_2_values_remain")
    output_df, assigned_column_name = fx_join_single_column(output_df, validation_output_df, sku_col_name_df_1, sku_col_name_df_2, "FX_FLAG_RECALC_missing_all_parameters_recalc")

return output_df, validation_function_summary_df
