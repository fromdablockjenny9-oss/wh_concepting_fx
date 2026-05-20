import pandas as pd
from category import data_analysis_category


import numpy as np
import math
import json
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial

import io



# Copyright (c) 2026 fromdablockjenny9-oss @Github
# This project and its source code are the property of fromdablockjenny9-oss @Github
# Unauthorized copying, modification, or distribution is prohibited
# fromdablockjenny9@gmail.com

def plot_1(df, x_column, x_count, y_column, y_sum):
    def format_float_with_commas(number, decimal_places=0):
        floored_number = round(number, decimal_places)
        
        formatted_number = f"{floored_number:,.{decimal_places}f}"
        
        return formatted_number


    abc_projection_x_name = "abc_projection_x"

    color = "#FF7F00"

    dpi = 100
    fig_width = (1920/2) / dpi
    fig_height = (1080/2) / dpi

    fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)
    ax = fig.add_axes([0.1, 0.4, 0.8, 0.5])

    x = df[abc_projection_x_name]
    y = df[y_column]
    ax.plot(x, y, label="Grown Data", color=color, marker='', linestyle='-', linewidth=2)

    h_line_value = df[y_column].mean()
    ax.axhline(y=h_line_value, label="Average", color=color, linestyle='--', linewidth=1)


    plt.title('Pareto Distribution (Grown Data)')
    plt.xlabel('SKU Count')
    plt.ylabel('QTY')
    plt.legend(loc='upper center', bbox_to_anchor=(0.91, -0.15), ncol=1)


    plot_df = pd.DataFrame()
    plot_df["Column"] = None
    plot_df["Value"] = None

    col_i_2 = -1

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "SKU Count"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(len(df), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY Sum"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].sum(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY min"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].min(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY max"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].max(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY average"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].mean(), decimal_places=0)

    table_ax = fig.add_axes([0.15, -0.02, 0.2, 0.45])
    table = plt.table(cellText=plot_df.values, loc='center', cellLoc='center')


    col_widths = [0.9, 0.6]

    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        cell.set_width(col_widths[key[1]])  
        cell.set_fontsize(10)
        cell.set_height(0.10)

    table_ax.axis('off')
    
    buffer_png = io.BytesIO()
    plt.savefig(buffer_png, format="png")
    
    return buffer_png
    

def plot_2(df, x_column, x_count, y_column, y_sum):
    def format_float_with_commas(number, decimal_places=0):
        floored_number = round(number, decimal_places)
        formatted_number = f"{floored_number:,.{decimal_places}f}"
        
        return formatted_number

    abc_projection_x_name = "abc_projection_x"

    color = "#0000FF"



    dpi = 100
    fig_width = (1920/2) / dpi
    fig_height = (1080/2) / dpi

    fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)
    ax = fig.add_axes([0.1, 0.4, 0.8, 0.5])

    x = df[abc_projection_x_name]
    y = df[y_column]
    ax.plot(x, y, label="Original Data", color=color, marker='', linestyle='-', linewidth=2)

    h_line_value = df[y_column].mean()
    ax.axhline(y=h_line_value, label="Average", color=color, linestyle='--', linewidth=1)


    plt.title('Pareto Distribution (Original Data)')
    plt.xlabel('SKU Count')
    plt.ylabel('QTY')
    plt.legend(loc='upper center', bbox_to_anchor=(0.91, -0.15), ncol=1)


    plot_df = pd.DataFrame()
    plot_df["Column"] = None
    plot_df["Value"] = None

    col_i_2 = -1

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "SKU Count"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(len(df), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY Sum"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].sum(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY min"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].min(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY max"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].max(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY average"
    plot_df.at[col_i_2, "Value"] = format_float_with_commas(df[y_column].mean(), decimal_places=0)

    table_ax = fig.add_axes([0.15, -0.02, 0.2, 0.45])
    table = plt.table(cellText=plot_df.values, loc='center', cellLoc='center')


    col_widths = [0.9, 0.6]

    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        cell.set_width(col_widths[key[1]])  
        cell.set_fontsize(10)
        cell.set_height(0.10)

    table_ax.axis('off')
    buffer_png = io.BytesIO()
    plt.savefig(buffer_png, format="png")
    
    return buffer_png

def plot_3(df_new, df, x_column, x_count, y_column, y_sum):
    
    def format_float_with_commas(number, decimal_places=0):
        floored_number = round(number, decimal_places)
        formatted_number = f"{floored_number:,.{decimal_places}f}"
        
        return formatted_number

    abc_projection_x_name = "abc_projection_x"

    color = "#0000FF"



    dpi = 100
    fig_width = (1920) / dpi
    fig_height = (1080) / dpi

    fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)
    ax = fig.add_axes([0.1, 0.4, 0.8, 0.5])  

    x = df[abc_projection_x_name]
    y = df[y_column]
    ax.plot(x, y, label="Original Data", color=color, marker='', linestyle='-', linewidth=2)

    h_line_value = df[y_column].mean()
    ax.axhline(y=h_line_value, label="Average", color=color, linestyle='--', linewidth=1)


    color = "#FF7F00"
    x = df_new[abc_projection_x_name]
    y = df_new[y_column]
    ax.plot(x, y, label="Grown Data", color=color, marker='', linestyle='-', linewidth=2)

    h_line_value = df_new[y_column].mean()
    ax.axhline(y=h_line_value, label="Average", color=color, linestyle='--', linewidth=1)

    plt.title('Pareto Distribution\n')
    plt.xlabel('SKU Count')
    plt.ylabel('QTY')
    plt.legend(loc='upper center', bbox_to_anchor=(0.94, -0.15), ncol=1)



    plot_df = pd.DataFrame()
    plot_df["Column"] = None
    plot_df["Value1"] = None
    plot_df["Value2"] = None

    col_i_2 = -1


    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = ""
    plot_df.at[col_i_2, "Value1"] = "Original Data"
    plot_df.at[col_i_2, "Value2"] = "Grown Data"



    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "SKU Count"
    plot_df.at[col_i_2, "Value1"] = format_float_with_commas(len(df), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY Sum"
    plot_df.at[col_i_2, "Value1"] = format_float_with_commas(df[y_column].sum(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY min"
    plot_df.at[col_i_2, "Value1"] = format_float_with_commas(df[y_column].min(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY max"
    plot_df.at[col_i_2, "Value1"] = format_float_with_commas(df[y_column].max(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY average"
    plot_df.at[col_i_2, "Value1"] = format_float_with_commas(df[y_column].mean(), decimal_places=0)



    col_i_2 = 0
    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "SKU Count"
    plot_df.at[col_i_2, "Value2"] = format_float_with_commas(len(df_new), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY Sum"
    plot_df.at[col_i_2, "Value2"] = format_float_with_commas(df_new[y_column].sum(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY min"
    plot_df.at[col_i_2, "Value2"] = format_float_with_commas(df_new[y_column].min(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY max"
    plot_df.at[col_i_2, "Value2"] = format_float_with_commas(df_new[y_column].max(), decimal_places=0)

    col_i_2 = col_i_2 + 1
    plot_df.at[col_i_2, "Column"] = "QTY average"
    plot_df.at[col_i_2, "Value2"] = format_float_with_commas(df_new[y_column].mean(), decimal_places=0)









    table_ax = fig.add_axes([0.11, 0.03, 0.2, 0.45]) 
    table = plt.table(cellText=plot_df.values, loc='center', cellLoc='center')



    col_widths = [0.45, 0.3, 0.3]  

    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        cell.set_width(col_widths[key[1]])  
        cell.set_fontsize(12)
        if key[0] == 0:
            cell.set_height(0.05)
        else:
            cell.set_height(0.05)

    table_ax.axis('off')

    buffer_png = io.BytesIO()
    plt.savefig(buffer_png, format="png")
    
    return buffer_png

def fx_print_param_fx(d):
    for key, value in d.items():
        print(key + ' = ' + 'my_parameters["' + key + '"]')
       
def count_unique_values(arr):
    unique_counts = {}
    for item in arr:
        if str(item) in unique_counts:
            unique_counts[str(item)] += 1
        else:
            unique_counts[str(item)] = 1
    return unique_counts
    
def fx_adjust_dataframe_row_count(df, id_column, target_size):
    current_size = len(df)
    if target_size == current_size:
        return df.copy()
    
    if target_size > current_size:
    
        extra_value_count = target_size - current_size
        step = current_size / extra_value_count
        half_step = step//2
        index_to_copy_array = []
        for i in range(0, extra_value_count):
            index_to_copy_array.append(math.floor(half_step + step*i))
        
        new_df = pd.DataFrame(columns=df_sorted.columns)
        new_df_i = -1
        
        index_to_copy_json = count_unique_values(index_to_copy_array)

        for index, row in df.iterrows():
            new_df_i = new_df_i + 1
            
            for column in df.columns:
                if column == id_column:
                    new_df.at[new_df_i,column] = str(row[column])
                else:
                    new_df.at[new_df_i,column] = row[column]
            
            if str(index) in index_to_copy_json:
                
                for j in range(0,index_to_copy_json[str(index)]):
                    new_df_i = new_df_i + 1
                    for column in df.columns:
                        if column == id_column:
                            new_df.at[new_df_i,column] = str(row[column]) + "-" + str(j+1)
                        else:
                            new_df.at[new_df_i,column] = row[column]
                
        return new_df
        
    elif target_size < current_size:
    
        extra_value_count = current_size - target_size
        step = current_size / extra_value_count
        half_step = step//2
        indices_to_remove = set()
        
        for i in range(0, extra_value_count):
            
            indices_to_remove.add(math.floor(half_step + step*i))
            
        indices_to_remove = sorted(indices_to_remove)
    
        df1 = df.copy()
        df1 = df1.drop(df1.index[indices_to_remove])
        
        df1.reset_index(drop=True, inplace=True)
        return df1
    
    
    return

def assign_polynomial_y_values(
    first_dataframe, first_dataframe_x_column_name, first_dataframe_y_column_name,
    second_dataframe, second_dataframe_x_column_name, second_dataframe_y_column_name
):
    first_df = first_dataframe.copy()
    second_df = second_dataframe.copy()
    second_df[second_dataframe_y_column_name] = np.nan

    for index, row in second_df.iterrows():
        x_target = row[second_dataframe_x_column_name]
        first_df['distance'] = np.abs(first_df[first_dataframe_x_column_name] - x_target)
        closest_points = first_df.nsmallest(7, 'distance')

        x_values = closest_points[first_dataframe_x_column_name].values
        y_values = closest_points[first_dataframe_y_column_name].values

        p = Polynomial.fit(x_values, y_values, 2)

        predicted_y = p(x_target)

        second_df.at[index, second_dataframe_y_column_name] = predicted_y

    return second_df
    
def line_from_points(x1, y1, x2, y2):
    if x1 == x2:
        return 0, y1

    k = (y2 - y1) / (x2 - x1)   
    b = y1 - k * x1            

    return k, b
def assign_linear_y_values(
    first_dataframe, first_dataframe_x_column_name, first_dataframe_y_column_name,
    second_dataframe, second_dataframe_x_column_name, second_dataframe_y_column_name
):
    first_df = first_dataframe.copy()
    second_df = second_dataframe.copy()

    
    second_df[second_dataframe_y_column_name] = np.nan

    for index, row in second_df.iterrows():
        x_target = row[second_dataframe_x_column_name]

        
        first_df['distance'] = np.abs(first_df[first_dataframe_x_column_name] - x_target)

        
        closest_points = first_df.nsmallest(2, 'distance')
        
        
        
        first_row = 0
        for index_1, row_1 in closest_points.iterrows():
            if first_row == 0:
                x1 = row_1[first_dataframe_x_column_name]
                y1 = row_1[first_dataframe_y_column_name]
                
                first_row = 1
            else:
                x2 = row_1[first_dataframe_x_column_name]
                y2 = row_1[first_dataframe_y_column_name]
        
        if x1 <= x2:
            k, b = line_from_points(x1, y1, x2, y2)
        else:
            k, b = line_from_points(x2, y2, x1, y1)
            
            
            
        predicted_y = k*x_target + b
        
        second_df.at[index, second_dataframe_y_column_name] = predicted_y


    return second_df	



df = input_1.to_pandas()




x_column    = str(self.column_param_sku_id)
x_count     = int(self.param_new_sku_count)
y_column    = str(self.column_param_qty)
y_sum       = float(self.param_new_qty)

abc_projection_x_name = "abc_projection_x"




df_sorted = df.sort_values(by=y_column, ascending=False).reset_index(drop=True)
df_sorted[abc_projection_x_name] = float(0)
        
start = float(1)
step = float(1)

for i in range(0,len(df_sorted)):
    df_sorted.at[i,abc_projection_x_name] = start + step*i
    
x_min = df_sorted[abc_projection_x_name].min()
x_max = df_sorted[abc_projection_x_name].max()

start = x_min
step = (x_max - x_min) / (x_count-1)

df_adjusted_len = fx_adjust_dataframe_row_count(df_sorted, x_column, x_count)

for index, row in df_adjusted_len.iterrows():
    df_adjusted_len.at[index, abc_projection_x_name] = start + step*index

df_adjusted_len.at[0,abc_projection_x_name] = x_min
df_adjusted_len.at[len(df_adjusted_len)-1,abc_projection_x_name] = x_max


result_df = assign_linear_y_values(
    first_dataframe=df_sorted,
    first_dataframe_x_column_name=abc_projection_x_name,
    first_dataframe_y_column_name=y_column,
    second_dataframe=df_adjusted_len,
    second_dataframe_x_column_name=abc_projection_x_name,
    second_dataframe_y_column_name=y_column
)




current_sum = result_df[y_column].sum()
scale_factor = y_sum / current_sum


for index, row in result_df.iterrows():
    result_df.at[index, y_column] = result_df.at[index, y_column] * scale_factor

start = float(1)
step = float(1)

for i in range(0,len(result_df)):
    result_df.at[i,abc_projection_x_name] = start + step*i




result_df_reduced = result_df[[col for col in result_df.columns if col != abc_projection_x_name]]


buffer_png_1 = plot_1(result_df, x_column, x_count, y_column, y_sum)
buffer_png_2 = plot_2(df_sorted, x_column, x_count, y_column, y_sum)
buffer_png_3 = plot_3(result_df, df_sorted, x_column, x_count, y_column, y_sum)

return result_df_reduced, buffer_png_1.getvalue(), buffer_png_2.getvalue(), buffer_png_3.getvalue())
