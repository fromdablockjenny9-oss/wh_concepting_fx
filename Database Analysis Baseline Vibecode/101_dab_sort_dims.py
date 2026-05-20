from category import data_cleanup_category
import pandas as pd
import numpy as np
import json
import math
import copy



# Copyright (c) 2026 fromdablockjenny9-oss @Github
# This project and its source code are the property of fromdablockjenny9-oss @Github
# Unauthorized copying, modification, or distribution is prohibited
# fromdablockjenny9@gmail.com

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


def fx_column_name(dataframe1, column_to_join):
dataframe1 = dataframe1.copy(deep=True)
suffix = ''
new_column_name = column_to_join
while new_column_name in dataframe1.columns:
    suffix = f'_{int(suffix[1:]) + 1 if suffix else 1}'
    new_column_name = column_to_join + suffix
assigned_column_name = new_column_name
return assigned_column_name 

df = input_1.to_pandas()
df = df.reset_index(drop=True)
df = df.copy(deep=True)

row_count = len(df)

length_column_name                                      = self.column_param_length
width_column_name                                       = self.column_param_width
height_column_name                                      = self.column_param_height
sort_selection                                          = self.selection_param

err = 0.00001
rotation_none = 0
rotation_2d = 0
rotation_3d = 0

dab_length_column = fx_column_name(df, "DAB_Length")
dab_width_column = fx_column_name(df, "DAB_Width")
dab_height_column = fx_column_name(df, "DAB_Height")
dab_rotated_column = fx_column_name(df, "DAB_Rotated")




df[dab_length_column] = None
df[dab_width_column] = None
df[dab_height_column] = None
df[dab_rotated_column] = None

for index, row in df.iterrows():
length_value 												= row[length_column_name]
width_value 												= row[width_column_name]
height_value 												= row[height_column_name]

df.at[index, dab_length_column] = length_value
df.at[index, dab_width_column] = width_value
df.at[index, dab_height_column] = height_value
df.at[index, dab_rotated_column] = ""

if sort_selection == "L>W>H":
    max_value = max(length_value,width_value,height_value)
    min_value = min(length_value,width_value,height_value)
    
    sum_value = length_value + width_value + height_value
    
    diff_value = sum_value - (max_value + min_value)
    
    df.at[index, dab_length_column]			= max_value
    df.at[index, dab_width_column]			= diff_value
    df.at[index, dab_height_column]			= min_value
else:
    max_value = max(length_value,width_value)
    min_value = min(length_value,width_value)
    
    df.at[index, dab_length_column]			= max_value
    df.at[index, dab_width_column]			= min_value

rotated_string = ""
    
    
    
if ((length_value < df.at[index, dab_length_column] + err) and (length_value > df.at[index, dab_length_column] - err)) and ((width_value < df.at[index, dab_width_column] + err) and (width_value > df.at[index, dab_width_column] - err)) and ((height_value < df.at[index, dab_height_column] + err) and (height_value > df.at[index, dab_height_column] - err)):
    rotated_string = "No"
    rotation_none = rotation_none + 1
if (not ((length_value < df.at[index, dab_length_column] + err) and (length_value > df.at[index, dab_length_column] - err))) and (not ((width_value < df.at[index, dab_width_column] + err) and (width_value > df.at[index, dab_width_column] - err))) and ((height_value < df.at[index, dab_height_column] + err) and (height_value > df.at[index, dab_height_column] - err)):
    rotated_string = "L>W"
    rotation_2d = rotation_2d + 1
if (not((height_value < df.at[index, dab_height_column] + err) and (height_value > df.at[index, dab_height_column] - err))):
    rotated_string = "L>W>H"
    rotation_3d = rotation_3d + 1
        

df.at[index, dab_rotated_column]				= rotated_string

statistics_df = add_row_to_df("", 					"Name", "Value")
statistics_df = add_row_to_df(statistics_df, 		"Inputs:", "")
statistics_df = add_row_to_df(statistics_df, 		"Sort Selection", sort_selection)
statistics_df = add_row_to_df(statistics_df, 		"Total Rows", str(row_count))
statistics_df = add_row_to_df(statistics_df)
statistics_df = add_row_to_df(statistics_df, 		"Outputs:", "")
statistics_df = add_row_to_df(statistics_df, 		"L>W Rotation", str(rotation_2d))
statistics_df = add_row_to_df(statistics_df, 		"L>W>H Rotation", str(rotation_3d))
statistics_df = add_row_to_df(statistics_df, 		"Rotation Unchanged", str(rotation_none))
statistics_df = add_row_to_df(statistics_df, 		"Sum", str(rotation_none + rotation_2d + rotation_3d))

statistics_df = statistics_df.loc[:, (statistics_df != "").any()]

return df, statistics_df
