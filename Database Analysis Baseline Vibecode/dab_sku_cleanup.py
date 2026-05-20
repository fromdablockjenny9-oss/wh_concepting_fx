
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
    
    def fx_column_name(dataframe1, column_to_join):
        dataframe1 = dataframe1.copy(deep=True)
        suffix = ''
        new_column_name = column_to_join
        while new_column_name in dataframe1.columns:
            suffix = f'_{int(suffix[1:]) + 1 if suffix else 1}'
            new_column_name = column_to_join + suffix
        assigned_column_name = new_column_name
        return assigned_column_name 

        
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



    df = input_1.to_pandas()
    my_variables_df = input_2.to_pandas()

    df = df.reset_index(drop=True)
    my_variables_df = my_variables_df.reset_index(drop=True)

    row_count = len(df)

    length_column_name									= self.column_param_length
    width_column_name 									= self.column_param_width
    height_column_name 									= self.column_param_height
    weight_column_name	 								= self.column_param_weight

    average_type	 						            = self.selection_avg_type
    quantity_column_name	 							= self.column_param_quantity
    output_flags	 									= self.selection_output_flags

    minimum_length			= my_variables_df.at[0, 'minimum_length']
    maximum_length			= my_variables_df.at[0, 'maximum_length']

    minimum_width			= my_variables_df.at[0, 'minimum_width']
    maximum_width			= my_variables_df.at[0, 'maximum_width']

    minimum_height			= my_variables_df.at[0, 'minimum_height']
    maximum_height			= my_variables_df.at[0, 'maximum_height']

    minimum_weight			= my_variables_df.at[0, 'minimum_weight']
    maximum_weight			= my_variables_df.at[0, 'maximum_weight']

    minimum_density			= my_variables_df.at[0, 'minimum_density']
    maximum_density			= my_variables_df.at[0, 'maximum_density']

    stats_good_dim_rows = 0
    stats_good_weight_rows = 0
    stats_corrected_dim_rows = 0
    stats_corrected_weight_rows = 0

    dab_length_name 	= fx_column_name(df, "DAB_Length")
    dab_width_name 		= fx_column_name(df, "DAB_Width")
    dab_height_name 	= fx_column_name(df, "DAB_Height")
    dab_weight_name 	= fx_column_name(df, "DAB_Weight")

    df[dab_length_name] = df[length_column_name].copy()
    df[dab_width_name] = df[width_column_name].copy()
    df[dab_height_name] = df[height_column_name].copy()
    df[dab_weight_name] = df[weight_column_name].copy()

    length_column_name 		= dab_length_name
    width_column_name 		= dab_width_name
    height_column_name 		= dab_height_name
    weight_column_name 		= dab_weight_name

    if output_flags == "No":
        flag_df = pd.DataFrame()
    else:
        flag_df = df

    dab_flag_min_length_col = fx_column_name(flag_df, "DAB_FLAG_min_length")
    dab_flag_max_length_col = fx_column_name(flag_df, "DAB_FLAG_max_length")

    dab_flag_min_width_col = fx_column_name(flag_df, "DAB_FLAG_min_width")
    dab_flag_max_width_col = fx_column_name(flag_df, "DAB_FLAG_max_width")

    dab_flag_min_height_col = fx_column_name(flag_df, "DAB_FLAG_min_height")
    dab_flag_max_height_col = fx_column_name(flag_df, "DAB_FLAG_max_height")

    dab_flag_min_weight_col = fx_column_name(flag_df, "DAB_FLAG_min_weight")
    dab_flag_max_weight_col = fx_column_name(flag_df, "DAB_FLAG_max_weight")

    dab_flag_min_density_col = fx_column_name(flag_df, "DAB_FLAG_min_density")
    dab_flag_max_density_col = fx_column_name(flag_df, "DAB_FLAG_max_density")

    dab_flag_bad_dims_col = fx_column_name(flag_df, "DAB_FLAG_bad_dims")

    if average_type == "Average":
        dab_calc_length_to_width_ratio_col 					= fx_column_name(flag_df, "DAB_CALC_length_to_width_ratio")
        dab_calc_length_to_height_ratio_col 				= fx_column_name(flag_df, "DAB_CALC_length_to_height_ratio")
        dab_calc_length_col 								= fx_column_name(flag_df, "DAB_CALC_length")
        dab_calc_density_col 								= fx_column_name(flag_df, "DAB_CALC_density")
    else:
        dab_calc_weighted_length_to_width_ratio_col 		= fx_column_name(flag_df, "DAB_CALC_weighted_length_to_width_ratio")
        dab_calc_weighted_length_to_height_ratio_col 		= fx_column_name(flag_df, "DAB_CALC_weighted_length_to_height_ratio")
        dab_calc_weighted_length_col 						= fx_column_name(flag_df, "DAB_CALC_weighted_length")
        dab_calc_weighted_density_col 						= fx_column_name(flag_df, "DAB_CALC_weighted_density")


    dab_flag_bad_weight_col = fx_column_name(flag_df, "DAB_FLAG_bad_weight")



    flag_df[dab_flag_min_length_col] = 0
    flag_df[dab_flag_max_length_col] = 0

    flag_df[dab_flag_min_width_col] = 0
    flag_df[dab_flag_max_width_col] = 0

    flag_df[dab_flag_min_height_col] = 0
    flag_df[dab_flag_max_height_col] = 0

    flag_df[dab_flag_min_weight_col] = 0
    flag_df[dab_flag_max_weight_col] = 0

    flag_df[dab_flag_min_density_col] = 0
    flag_df[dab_flag_max_density_col] = 0

    flag_df[dab_flag_bad_dims_col] = 0


    if average_type == "Average":
        flag_df[dab_calc_length_to_width_ratio_col] = 0.0
        flag_df[dab_calc_length_to_height_ratio_col] = 0.0
        flag_df[dab_calc_length_col] = 0.0
        flag_df[dab_calc_density_col] = 0.0
    else:
        flag_df[dab_calc_weighted_length_to_width_ratio_col] = 0.0
        flag_df[dab_calc_weighted_length_to_height_ratio_col] = 0.0
        flag_df[dab_calc_weighted_length_col] = 0.0
        flag_df[dab_calc_weighted_density_col] = 0.0

    flag_df[dab_flag_bad_weight_col] = 0

    good_dims_count = 0
    good_weight_count = 0

    for index, row in df.iterrows():
        length_value 												= row[length_column_name]
        width_value 												= row[width_column_name]
        height_value 												= row[height_column_name]
        
        
        
        flag_df.at[index, dab_flag_min_length_col] = 0
        flag_df.at[index, dab_flag_max_length_col] = 0
        
        flag_df.at[index, dab_flag_min_width_col] = 0
        flag_df.at[index, dab_flag_max_width_col] = 0
        
        flag_df.at[index, dab_flag_min_height_col] = 0
        flag_df.at[index, dab_flag_max_height_col] = 0
        
        flag_df.at[index, dab_flag_bad_dims_col] = 0
        
        
        if length_value < minimum_length:
            flag_df.at[index, dab_flag_min_length_col] = 1
        if length_value > maximum_length:
            flag_df.at[index, dab_flag_max_length_col] = 1
        
        if width_value < minimum_width:
            flag_df.at[index, dab_flag_min_width_col] = 1
        if width_value > maximum_width:
            flag_df.at[index, dab_flag_max_width_col] = 1
            
        if height_value < minimum_height:
            flag_df.at[index, dab_flag_min_height_col] = 1
        if height_value > maximum_height:
            flag_df.at[index, dab_flag_max_height_col] = 1
        
        sum_of_dim_flags = 0
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_min_length_col]
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_max_length_col]
        
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_min_width_col]
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_max_width_col]
        
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_min_height_col]
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_max_height_col]
        
        if sum_of_dim_flags > 0:
            flag_df.at[index, dab_flag_bad_dims_col] = 1
        
        if sum_of_dim_flags > 0:
            flag_df.at[index, dab_flag_bad_dims_col] = 1
        
        if average_type == "Average":
            flag_df.at[index, dab_calc_length_to_width_ratio_col] 						= 0.0
            flag_df.at[index, dab_calc_length_to_height_ratio_col] 					    = 0.0
            flag_df.at[index, dab_calc_length_col] 									    = 0.0
            
            
        else:
            flag_df.at[index, dab_calc_weighted_length_to_width_ratio_col] 			    = 0.0
            flag_df.at[index, dab_calc_weighted_length_to_height_ratio_col] 			= 0.0
            flag_df.at[index, dab_calc_weighted_length_col] 							= 0.0
            
            
        if average_type == "Average": 
            if flag_df.at[index, dab_flag_bad_dims_col] == 0:
                flag_df.at[index, dab_calc_length_to_width_ratio_col] 					= length_value / width_value
                flag_df.at[index, dab_calc_length_to_height_ratio_col] 				    = length_value / height_value
                flag_df.at[index, dab_calc_length_col] 								    = length_value
                good_dims_count 												        = good_dims_count + 1
                stats_good_dim_rows 											        = stats_good_dim_rows +1
                
        else:
        
            if flag_df.at[index, dab_flag_bad_dims_col] == 0:
                flag_df.at[index, dab_calc_weighted_length_to_width_ratio_col] 		    = (length_value / width_value) 		* row[quantity_column_name]
                flag_df.at[index, dab_calc_weighted_length_to_height_ratio_col] 		= (length_value / height_value)		* row[quantity_column_name]
                flag_df.at[index, dab_calc_weighted_length_col] 						= (length_value)					* row[quantity_column_name]
                good_dims_count 												        = good_dims_count + row[quantity_column_name]
                stats_good_dim_rows 											        = stats_good_dim_rows +1
                    
    if average_type == "Average":
        replacement_L2W 		= flag_df[dab_calc_length_to_width_ratio_col].sum() 				/ good_dims_count
        replacement_L2H 		= flag_df[dab_calc_length_to_height_ratio_col].sum() 				/ good_dims_count
        replacement_L 			= flag_df[dab_calc_length_col].sum() 								/ good_dims_count
        
    else:
        replacement_L2W 		= flag_df[dab_calc_weighted_length_to_width_ratio_col].sum() 		/ good_dims_count
        replacement_L2H 		= flag_df[dab_calc_weighted_length_to_height_ratio_col].sum() 		/ good_dims_count
        replacement_L 			= flag_df[dab_calc_weighted_length_col].sum() 						/ good_dims_count

        
    for index, row in df.iterrows():
        length_value 												= row[length_column_name]
        width_value 												= row[width_column_name]
        height_value 												= row[height_column_name]
        
        
        new_dims_bad = 0
        
        sum_of_dim_flags = 0
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_min_length_col]
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_max_length_col]
        
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_min_width_col]
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_max_width_col]
        
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_min_height_col]
        sum_of_dim_flags = sum_of_dim_flags + flag_df.at[index, dab_flag_max_height_col]

        if sum_of_dim_flags == 1:
            if flag_df.at[index, dab_flag_min_length_col] == 1 or flag_df.at[index, dab_flag_max_length_col] == 1:
                df.at[index, length_column_name] = replacement_L2W * df.at[index, width_column_name]
                
            if flag_df.at[index, dab_flag_min_width_col] == 1 or flag_df.at[index, dab_flag_max_width_col] == 1:
                df.at[index, width_column_name] = df.at[index, length_column_name] / replacement_L2W
                
            if flag_df.at[index, dab_flag_min_height_col] == 1 or flag_df.at[index, dab_flag_max_height_col] == 1:
                df.at[index, height_column_name] = df.at[index, length_column_name] / replacement_L2H
            
            if length_value < minimum_length:
                new_dims_bad = 1
            if length_value > maximum_length:
                new_dims_bad = 1
            if width_value < minimum_width:
                new_dims_bad = 1
            if width_value > maximum_width:
                new_dims_bad = 1
                
            if height_value < minimum_height:
                new_dims_bad = 1
            if height_value > maximum_height:
                new_dims_bad = 1
        
        if sum_of_dim_flags > 1 or new_dims_bad == 1:
            df.at[index, length_column_name] 	= replacement_L
            df.at[index, width_column_name] 	= replacement_L / replacement_L2W
            df.at[index, height_column_name] 	= replacement_L / replacement_L2H
        
        if sum_of_dim_flags > 0:
            stats_corrected_dim_rows = stats_corrected_dim_rows + 1
        
    for index, row in df.iterrows():
        length_value 												= row[length_column_name]
        width_value 												= row[width_column_name]
        height_value 												= row[height_column_name]
        
        weight_value 												= row[weight_column_name]
        
        flag_df.at[index, dab_flag_min_weight_col] = 0
        flag_df.at[index, dab_flag_max_weight_col] = 0
        
        flag_df.at[index, dab_flag_min_density_col] = 0
        flag_df.at[index, dab_flag_max_density_col] = 0
        
        
        flag_df.at[index, dab_flag_bad_weight_col] = 0
        
        if weight_value < minimum_weight:
            flag_df.at[index, dab_flag_min_weight_col] = 1
        if weight_value > maximum_weight:
            flag_df.at[index, dab_flag_max_weight_col] = 1
        
        if (length_value * width_value * height_value) > 0:
            density_value = weight_value / (length_value * width_value * height_value)
        else:
            density_value = 0
        
        if density_value < minimum_density or density_value == 0:
            flag_df.at[index, dab_flag_min_density_col] = 1
        if density_value > maximum_density:
            flag_df.at[index, dab_flag_max_density_col] = 1
        
        sum_of_weight_flags = 0
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_min_weight_col]
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_max_weight_col]
        
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_min_density_col]
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_max_density_col]
        
        if sum_of_weight_flags > 0:
            flag_df.at[index, dab_flag_bad_weight_col] = 1
            
        
        
        if average_type == "Average":
            flag_df.at[index, dab_calc_density_col] 									= 0.0
        else:
            flag_df.at[index, dab_calc_weighted_density_col] 							= 0.0
        
        
        if average_type == "Average":
            if flag_df.at[index, dab_flag_bad_weight_col] == 0:
                flag_df.at[index, dab_calc_density_col] 							= density_value
                good_weight_count 											= good_weight_count + 1
                stats_good_weight_rows  									= stats_good_weight_rows + 1
                
        else:
            if flag_df.at[index, dab_flag_bad_weight_col] == 0:
                flag_df.at[index, dab_calc_weighted_density_col] 					= density_value 					* row[quantity_column_name]
                good_weight_count 											= good_weight_count + row[quantity_column_name]
                stats_good_weight_rows  									= stats_good_weight_rows + 1
                
    if average_type == "Average":
        replacement_density 	= flag_df[dab_calc_density_col].sum() 								/ good_weight_count
        
    else:
        replacement_density 	= flag_df[dab_calc_weighted_density_col].sum() 					/ good_weight_count
        
        
    for index, row in df.iterrows():
        
        sum_of_weight_flags = 0
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_min_weight_col]
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_max_weight_col]
        
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_min_density_col]
        sum_of_weight_flags = sum_of_weight_flags + flag_df.at[index, dab_flag_max_density_col]
        
        if sum_of_weight_flags > 0:
            df.at[index, weight_column_name] = (df.at[index, length_column_name] * df.at[index, width_column_name] * df.at[index, height_column_name]) * replacement_density
            stats_corrected_weight_rows = stats_corrected_weight_rows + 1

    statistics_df = add_row_to_df("", 					"Name", "Value")
    statistics_df = add_row_to_df(statistics_df, 		"Inputs:", "")
    statistics_df = add_row_to_df(statistics_df, 		"average_type", average_type)
    statistics_df = add_row_to_df(statistics_df, 		"minimum_length", str(minimum_length))
    statistics_df = add_row_to_df(statistics_df, 		"maximum_length", str(maximum_length))
    statistics_df = add_row_to_df(statistics_df, 		"minimum_width", str(minimum_width))
    statistics_df = add_row_to_df(statistics_df, 		"maximum_width", str(maximum_width))
    statistics_df = add_row_to_df(statistics_df, 		"minimum_height", str(minimum_height))
    statistics_df = add_row_to_df(statistics_df, 		"maximum_height", str(maximum_height))
    statistics_df = add_row_to_df(statistics_df, 		"minimum_weight", str(minimum_weight))
    statistics_df = add_row_to_df(statistics_df, 		"maximum_weight", str(maximum_weight))
    statistics_df = add_row_to_df(statistics_df, 		"minimum_density", str(minimum_density))
    statistics_df = add_row_to_df(statistics_df, 		"maximum_density", str(maximum_density))
    statistics_df = add_row_to_df(statistics_df, 		"Total Rows:", str(row_count))
    statistics_df = add_row_to_df(statistics_df)
    statistics_df = add_row_to_df(statistics_df, 		"Outputs:", "")
    statistics_df = add_row_to_df(statistics_df, 		"stats_good_dim_rows", str(stats_good_dim_rows))
    statistics_df = add_row_to_df(statistics_df, 		"stats_corrected_dim_rows", str(stats_corrected_dim_rows))
    statistics_df = add_row_to_df(statistics_df, 		"stats_good_weight_rows", str(stats_good_weight_rows))
    statistics_df = add_row_to_df(statistics_df, 		"stats_corrected_weight_rows", str(stats_corrected_weight_rows))

    if average_type == "Average":
        statistics_df = add_row_to_df(statistics_df, 		"Average Length", format_float_with_commas(replacement_L, 2))
        statistics_df = add_row_to_df(statistics_df, 		"Average Length to Width ratio", format_float_with_commas(replacement_L2W, 2))
        statistics_df = add_row_to_df(statistics_df, 		"Average Length to Height ratio", format_float_with_commas(replacement_L2H, 2))
        statistics_df = add_row_to_df(statistics_df, 		"Average Density", format_float_with_commas(replacement_density, 2))
    else:
        statistics_df = add_row_to_df(statistics_df, 		"Weighted Average Length", format_float_with_commas(replacement_L, 2))
        statistics_df = add_row_to_df(statistics_df, 		"Weighted Average Length to Width ratio", format_float_with_commas(replacement_L2W, 2))
        statistics_df = add_row_to_df(statistics_df, 		"Weighted Average Length to Height ratio", format_float_with_commas(replacement_L2H, 2))
        statistics_df = add_row_to_df(statistics_df, 		"Weighted Average Density", format_float_with_commas(replacement_density, 2))
        


    statistics_df = statistics_df.loc[:, (statistics_df != "").any()]

    return df, statistics_df
