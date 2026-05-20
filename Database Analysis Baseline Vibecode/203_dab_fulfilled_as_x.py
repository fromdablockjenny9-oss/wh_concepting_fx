import pandas as pd
from category import data_analysis_category

import numpy as np
import json
import math
import copy

import io
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from datetime import timedelta



# Copyright (c) 2026 fromdablockjenny9-oss @Github
# This project and its source code are the property of fromdablockjenny9-oss @Github
# Unauthorized copying, modification, or distribution is prohibited
# fromdablockjenny9@gmail.com

def plot_1(data_df, data_cols_df, parameter_df):
    def format_float_with_commas(number, decimal_places=0):
        
        floored_number = round(number, decimal_places)
        
        formatted_number = f"{floored_number:,.{decimal_places}f}"
        
        return formatted_number
        
    def fill_missing_dates(df, date_col):
        
        
        df[date_col] = pd.to_datetime(df[date_col])
        full_date_range = pd.date_range(start=df[date_col].min(), end=df[date_col].max())
        df = df.set_index(date_col).reindex(full_date_range).reset_index()
        
        
        df = df.rename(columns={'index': date_col})

        
        df = df.fillna(0)
        
        return df
        
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
            

    cases_as_cases_col 		= data_cols_df.at[0,"cases_as_cases_col"]
    cases_as_layers_col		= data_cols_df.at[0,"cases_as_layers_col"]
    layers_shipped_col		= data_cols_df.at[0,"layers_shipped_col"]
    cases_as_pallets_col	= data_cols_df.at[0,"cases_as_pallets_col"]
    pallets_shipped_col		= data_cols_df.at[0,"pallets_shipped_col"]

    sku_id_column_name		= parameter_df.at[0,"sku_id_column_name"]
    case_qty_column_name 	= parameter_df.at[0,"case_qty_column_name"]
    ti_column_name 			= parameter_df.at[0,"ti_column_name"]
    cpp_column_name 		= parameter_df.at[0,"cpp_column_name"]
    date_column_name		= parameter_df.at[0,"date_column_name"]
    qty_percentile			= parameter_df.at[0,"qty_percentile"]


    data_df[date_column_name] = pd.to_datetime(data_df[date_column_name])
    data_df[date_column_name] = data_df[date_column_name].dt.date
    total_sku_ids 				= format_float_with_commas(data_df[sku_id_column_name].nunique())
    total_sku_ids_cases 		= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0, sku_id_column_name].nunique())
    total_sku_ids_layers 		= format_float_with_commas(data_df.loc[data_df[cases_as_layers_col] > 0, sku_id_column_name].nunique())
    total_sku_ids_pallets 		= format_float_with_commas(data_df.loc[data_df[cases_as_pallets_col] > 0, sku_id_column_name].nunique())


    max_daily_sku_ids 			= format_float_with_commas(data_df.groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_cases 	= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_layers 	= format_float_with_commas(data_df.loc[data_df[cases_as_layers_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_pallets 	= format_float_with_commas(data_df.loc[data_df[cases_as_pallets_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())

    pick_unit_qty_sum_cases 	= format_float_with_commas(data_df[cases_as_cases_col].sum())
    pick_unit_qty_sum_layers 	= format_float_with_commas(data_df[layers_shipped_col].sum())
    pick_unit_qty_sum_pallets 	= format_float_with_commas(data_df[pallets_shipped_col].sum())

    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col, layers_shipped_col, pallets_shipped_col]].sum().reset_index()

    pick_unit_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())
    pick_unit_qty_max_layers 	= format_float_with_commas(max_daily_df[layers_shipped_col].max())
    pick_unit_qty_max_pallets 	= format_float_with_commas(max_daily_df[pallets_shipped_col].max())

    pick_unit_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    pick_unit_qty_mean_layers	= format_float_with_commas(max_daily_df[layers_shipped_col].mean())
    pick_unit_qty_mean_pallets 	= format_float_with_commas(max_daily_df[pallets_shipped_col].mean())

    pick_unit_qty_percentile_cases 		= format_float_with_commas(max_daily_df[cases_as_cases_col].quantile(qty_percentile/100))
    pick_unit_qty_percentile_layers 	= format_float_with_commas(max_daily_df[layers_shipped_col].quantile(qty_percentile/100))
    pick_unit_qty_percentile_pallets 	= format_float_with_commas(max_daily_df[pallets_shipped_col].quantile(qty_percentile/100))

    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col, cases_as_layers_col, cases_as_pallets_col]].sum().reset_index()

    num1 = data_df[cases_as_cases_col].sum()
    num2 = data_df[cases_as_layers_col].sum()
    num3 = data_df[cases_as_pallets_col].sum()


    cases_qty_sum_cases 	= format_float_with_commas(num1)
    cases_qty_sum_layers 	= format_float_with_commas(num2)
    cases_qty_sum_pallets 	= format_float_with_commas(num3)

    cases_qty_sum_cases_total = format_float_with_commas(num1 + num2 + num3)

    cases_qty_sum_cases_proc 			= format_float_with_commas((num1/(num1 + num2 + num3))*100,2)
    cases_qty_sum_layers_proc 			= format_float_with_commas((num2/(num1 + num2 + num3))*100,2)
    cases_qty_sum_pallets_proc 			= format_float_with_commas((num3/(num1 + num2 + num3))*100,2)
    cases_qty_sum_cases_total_proc 		= format_float_with_commas((1)*100,2)

    cases_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())
    cases_qty_max_layers 	= format_float_with_commas(max_daily_df[cases_as_layers_col].max())
    cases_qty_max_pallets 	= format_float_with_commas(max_daily_df[cases_as_pallets_col].max())

    cases_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    cases_qty_mean_layers	= format_float_with_commas(max_daily_df[cases_as_layers_col].mean())
    cases_qty_mean_pallets 	= format_float_with_commas(max_daily_df[cases_as_pallets_col].mean())

    num1 = max_daily_df[cases_as_cases_col].quantile(qty_percentile/100)
    num2 = max_daily_df[cases_as_layers_col].quantile(qty_percentile/100)
    num3 = max_daily_df[cases_as_pallets_col].quantile(qty_percentile/100)

    cases_qty_percentile_cases 		= format_float_with_commas(num1)
    cases_qty_percentile_layers 	= format_float_with_commas(num2)
    cases_qty_percentile_pallets 	= format_float_with_commas(num3)

    cases_qty_percentile_cases_total = format_float_with_commas((num1 + num2 + num3))

    cases_qty_percentile_cases_proc 	= format_float_with_commas(((num1)/(num1 + num2 + num3))*100,2)
    cases_qty_percentile_layers_proc 	= format_float_with_commas(((num2)/(num1 + num2 + num3))*100,2)
    cases_qty_percentile_pallets_proc 	= format_float_with_commas(((num3)/(num1 + num2 + num3))*100,2)

    cases_qty_percentile_cases_total_proc = format_float_with_commas((1)*100,2)







    grouped_df = data_df.groupby(date_column_name, as_index=False)[[cases_as_cases_col, cases_as_layers_col, cases_as_pallets_col]].sum()


    grouped_df = grouped_df.sort_values(by=date_column_name)
    grouped_df[date_column_name] = pd.to_datetime(grouped_df[date_column_name])



    dpi = 100
    fig_width = 1920 / dpi
    fig_height = 840 / dpi

    height_scale_adjustment = 1080/840

    font_color = "#000000"
    plt.rcParams.update({
        'font.family': 'Arial', 
        'font.size': 12, 
        'text.color': font_color
    })




    fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)
    ax = fig.add_axes([0.1, 0.55, 0.875, 0.4])
    min_date = grouped_df[date_column_name].min() - timedelta(hours=24)
    max_date = grouped_df[date_column_name].max() + timedelta(hours=18) + timedelta(hours=24)

    color_order = ["#007FFF", "#FFA359", "#A5A5A5", "#0000FF", "#FF7F00", "#707070", "#000051", "#9E4900", "#353535"]

    bar_width = 0.2

    grouped_df_as_cases = grouped_df[[date_column_name, cases_as_cases_col]].copy(deep=True)
    grouped_df_as_cases[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=2)

    grouped_df_as_layers = grouped_df[[date_column_name, cases_as_layers_col]].copy(deep=True)
    grouped_df_as_layers[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=10)

    grouped_df_as_pallets = grouped_df[[date_column_name, cases_as_pallets_col]].copy(deep=True)
    grouped_df_as_pallets[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=18)

    col_name = cases_as_cases_col
    plot_df = grouped_df_as_cases
    my_label = "Cases As Cases"
    my_color = color_order[0]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)


    col_name = cases_as_layers_col
    plot_df = grouped_df_as_layers
    my_label = "Cases As Layers"
    my_color = color_order[1]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)

    col_name = cases_as_pallets_col
    plot_df = grouped_df_as_pallets
    my_label = "Cases As Pallets"
    my_color = color_order[2]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.set_xlim(min_date, max_date)

    plt.xlabel('Date')
    plt.ylabel('Case QTY')
    plt.title('Case QTY of different Order fulfilment methods')

    plt.legend(loc='upper center', bbox_to_anchor=(0.945, -0.07), ncol=1)

    if qty_percentile % 10 == 1:
        percentile_txt = str(qty_percentile) + "st\nPercentile"
    else:
        if qty_percentile % 10 == 2:
            percentile_txt = str(qty_percentile) + "nd\nPercentile"
        else:
            if qty_percentile % 10 == 3:
                percentile_txt = str(qty_percentile) + "rd\nPercentile"
            else:
                percentile_txt = str(qty_percentile) + "th\nPercentile"
                

    my_summary_df = add_row_to_df()
    my_summary_df = add_row_to_df(my_summary_df, "", 					"Total SKUs", 					"Max Daily\nSKUs", 			"Pick Unit\nQTY Sum", 		"Max Daily", 				"Average Daily", 				percentile_txt, 						"Case QTY\nSum", 			"%", 										"Case QTY\nMax", 				"Average Daily", 					percentile_txt, 					"%")                 
    my_summary_df = add_row_to_df(my_summary_df, "Pallets", 			total_sku_ids_pallets, 			max_daily_sku_ids_pallets, 	pick_unit_qty_sum_pallets, 	pick_unit_qty_max_pallets, 	pick_unit_qty_mean_pallets, 	pick_unit_qty_percentile_pallets, 		cases_qty_sum_pallets, 		cases_qty_sum_pallets_proc + "%",			cases_qty_max_pallets, 			cases_qty_mean_pallets, 			cases_qty_percentile_pallets, 		cases_qty_percentile_pallets_proc + "%")
    my_summary_df = add_row_to_df(my_summary_df, "Layers", 				total_sku_ids_layers, 			max_daily_sku_ids_layers, 	pick_unit_qty_sum_layers, 	pick_unit_qty_max_layers, 	pick_unit_qty_mean_layers, 		pick_unit_qty_percentile_layers, 		cases_qty_sum_layers, 		cases_qty_sum_layers_proc + "%",			cases_qty_max_layers, 			cases_qty_mean_layers, 				cases_qty_percentile_layers, 		cases_qty_percentile_layers_proc + "%")
    my_summary_df = add_row_to_df(my_summary_df, "Cases", 				total_sku_ids_cases, 			max_daily_sku_ids_cases, 	pick_unit_qty_sum_cases, 	pick_unit_qty_max_cases, 	pick_unit_qty_mean_cases, 		pick_unit_qty_percentile_cases, 		cases_qty_sum_cases, 		cases_qty_sum_cases_proc + "%",				cases_qty_max_cases, 			cases_qty_mean_cases, 				cases_qty_percentile_cases, 		cases_qty_percentile_cases_proc + "%")
    my_summary_df = add_row_to_df(my_summary_df)
    my_summary_df = add_row_to_df(my_summary_df, "Total", 				total_sku_ids, 					max_daily_sku_ids, 			"", 						"", 						"", 							"Sum:", 								cases_qty_sum_cases_total, 	cases_qty_sum_cases_total_proc + "%", 		"", 							"", 								cases_qty_percentile_cases_total, 	cases_qty_percentile_cases_total_proc + "%")

    my_summary_df = my_summary_df.loc[:, (my_summary_df != "").any()]

    horizontal_alignment = [

    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']


    ]


    vertical_alignment = [
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center']

    ]

    uniform_width = 0.3
    procentage_width = 0.2
    procentile_width = 0.3
    col_widths = [procentage_width, uniform_width, uniform_width, uniform_width, uniform_width, uniform_width, procentile_width, uniform_width, procentage_width, uniform_width, uniform_width, procentile_width, procentage_width]







    table_ax = fig.add_axes([0.737, -0.13, 0.243, 0.55])
    table = plt.table(cellText=my_summary_df.values, loc='upper right', cellLoc='center')




    edge_color = "#343A40"
    table_color = "#EFF1F2"



    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        cell.set_width(col_widths[key[1]]) 
        
        cell.get_text().set_horizontalalignment(horizontal_alignment[key[0]][key[1]])
        cell.get_text().set_verticalalignment(vertical_alignment[key[0]][key[1]])

        cell.set_height(0.06 * height_scale_adjustment)
        
        cell.set_edgecolor(edge_color)
        cell.get_text().set_fontname('Arial')
        cell.get_text().set_color(font_color)
        
        
        
        
            
        if key[0] == 0:
            cell.set_facecolor(table_color)
            cell.set_height(0.12)
            
            
            
    table_ax.axis('off')



    buffer_png = io.BytesIO()
    plt.savefig(buffer_png, format="png")
    
    return buffer_png
def plot_2(data_df, data_cols_df, parameter_df):
    def format_float_with_commas(number, decimal_places=0):
        
        floored_number = round(number, decimal_places)
        formatted_number = f"{floored_number:,.{decimal_places}f}"
        
        return formatted_number
        
    def fill_missing_dates(df, date_col):
        
        df[date_col] = pd.to_datetime(df[date_col])
        
        full_date_range = pd.date_range(start=df[date_col].min(), end=df[date_col].max())

        df = df.set_index(date_col).reindex(full_date_range).reset_index()
        
        df = df.rename(columns={'index': date_col})

        df = df.fillna(0)
        
        return df
        
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
            


    data_df 				= data_df.reset_index(drop=True)
    data_cols_df 			= data_cols_df.reset_index(drop=True)
    parameter_df 			= parameter_df.reset_index(drop=True)

    cases_as_cases_col 		= data_cols_df.at[0,"cases_as_cases_col"]
    cases_as_layers_col		= data_cols_df.at[0,"cases_as_layers_col"]
    layers_shipped_col		= data_cols_df.at[0,"layers_shipped_col"]

    sku_id_column_name		= parameter_df.at[0,"sku_id_column_name"]
    case_qty_column_name 	= parameter_df.at[0,"case_qty_column_name"]
    ti_column_name 			= parameter_df.at[0,"ti_column_name"]
    cpp_column_name 		= parameter_df.at[0,"cpp_column_name"]
    date_column_name		= parameter_df.at[0,"date_column_name"]
    qty_percentile			= parameter_df.at[0,"qty_percentile"]


    data_df[date_column_name] = pd.to_datetime(data_df[date_column_name])
    data_df[date_column_name] = data_df[date_column_name].dt.date

    total_sku_ids 				= format_float_with_commas(data_df[sku_id_column_name].nunique())
    total_sku_ids_cases 		= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0, sku_id_column_name].nunique())
    total_sku_ids_layers 		= format_float_with_commas(data_df.loc[data_df[cases_as_layers_col] > 0, sku_id_column_name].nunique())

    max_daily_sku_ids 			= format_float_with_commas(data_df.groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_cases 	= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_layers 	= format_float_with_commas(data_df.loc[data_df[cases_as_layers_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())

    pick_unit_qty_sum_cases 	= format_float_with_commas(data_df[cases_as_cases_col].sum())
    pick_unit_qty_sum_layers 	= format_float_with_commas(data_df[layers_shipped_col].sum())
    
    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col, layers_shipped_col]].sum().reset_index()

    pick_unit_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())
    pick_unit_qty_max_layers 	= format_float_with_commas(max_daily_df[layers_shipped_col].max())

    pick_unit_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    pick_unit_qty_mean_layers	= format_float_with_commas(max_daily_df[layers_shipped_col].mean())

    pick_unit_qty_percentile_cases 		= format_float_with_commas(max_daily_df[cases_as_cases_col].quantile(qty_percentile/100))
    pick_unit_qty_percentile_layers 	= format_float_with_commas(max_daily_df[layers_shipped_col].quantile(qty_percentile/100))

    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col, cases_as_layers_col]].sum().reset_index()

    num1 = data_df[cases_as_cases_col].sum()
    num2 = data_df[cases_as_layers_col].sum()

    cases_qty_sum_cases 	= format_float_with_commas(num1)
    cases_qty_sum_layers 	= format_float_with_commas(num2)

    cases_qty_sum_cases_total = format_float_with_commas(num1 + num2)

    cases_qty_sum_cases_proc 			= format_float_with_commas((num1/(num1 + num2))*100,2)
    cases_qty_sum_layers_proc 			= format_float_with_commas((num2/(num1 + num2))*100,2)
    cases_qty_sum_cases_total_proc 		= format_float_with_commas((1)*100,2)

    cases_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())
    cases_qty_max_layers 	= format_float_with_commas(max_daily_df[cases_as_layers_col].max())

    cases_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    cases_qty_mean_layers	= format_float_with_commas(max_daily_df[cases_as_layers_col].mean())
    
    num1 = max_daily_df[cases_as_cases_col].quantile(qty_percentile/100)
    num2 = max_daily_df[cases_as_layers_col].quantile(qty_percentile/100)

    cases_qty_percentile_cases 		= format_float_with_commas(num1)
    cases_qty_percentile_layers 	= format_float_with_commas(num2)

    cases_qty_percentile_cases_total = format_float_with_commas((num1 + num2))

    cases_qty_percentile_cases_proc 	= format_float_with_commas(((num1)/(num1 + num2))*100,2)
    cases_qty_percentile_layers_proc 	= format_float_with_commas(((num2)/(num1 + num2))*100,2)

    cases_qty_percentile_cases_total_proc = format_float_with_commas((1)*100,2)

    grouped_df = data_df.groupby(date_column_name, as_index=False)[[cases_as_cases_col, cases_as_layers_col]].sum()


    grouped_df = grouped_df.sort_values(by=date_column_name)
    grouped_df[date_column_name] = pd.to_datetime(grouped_df[date_column_name])

    dpi = 100
    fig_width = 1920 / dpi
    fig_height = 840 / dpi

    height_scale_adjustment = 1080/840

    font_color = "#000000"
    plt.rcParams.update({
        'font.family': 'Arial', 
        'font.size': 12, 
        'text.color': font_color
    })

    fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)
    ax = fig.add_axes([0.1, 0.55, 0.875, 0.4])
    min_date = grouped_df[date_column_name].min() - timedelta(hours=24)
    max_date = grouped_df[date_column_name].max() + timedelta(hours=18) + timedelta(hours=24)

    color_order = ["#007FFF", "#FFA359", "#A5A5A5", "#0000FF", "#FF7F00", "#707070", "#000051", "#9E4900", "#353535"]

    bar_width = 0.2

    grouped_df_as_cases = grouped_df[[date_column_name, cases_as_cases_col]].copy(deep=True)
    grouped_df_as_cases[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=2)

    grouped_df_as_layers = grouped_df[[date_column_name, cases_as_layers_col]].copy(deep=True)
    grouped_df_as_layers[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=10)

    col_name = cases_as_cases_col
    plot_df = grouped_df_as_cases
    my_label = "Cases As Cases"
    my_color = color_order[0]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)

    col_name = cases_as_layers_col
    plot_df = grouped_df_as_layers
    my_label = "Cases As Layers"
    my_color = color_order[1]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.set_xlim(min_date, max_date)


    plt.xlabel('Date')
    plt.ylabel('Case QTY')
    plt.title('Case QTY of different Order fulfilment methods')

    plt.legend(loc='upper center', bbox_to_anchor=(0.945, -0.07), ncol=1)

    if qty_percentile % 10 == 1:
        percentile_txt = str(qty_percentile) + "st\nPercentile"
    else:
        if qty_percentile % 10 == 2:
            percentile_txt = str(qty_percentile) + "nd\nPercentile"
        else:
            if qty_percentile % 10 == 3:
                percentile_txt = str(qty_percentile) + "rd\nPercentile"
            else:
                percentile_txt = str(qty_percentile) + "th\nPercentile"
                

    my_summary_df = add_row_to_df()
    my_summary_df = add_row_to_df(my_summary_df, "", 					"Total SKUs", 					"Max Daily\nSKUs", 			"Pick Unit\nQTY Sum", 		"Max Daily", 				"Average Daily", 				percentile_txt, 						"Case QTY\nSum", 			"%", 										"Case QTY\nMax", 				"Average Daily", 					percentile_txt, 					"%")                 
    my_summary_df = add_row_to_df(my_summary_df, "Layers", 				total_sku_ids_layers, 			max_daily_sku_ids_layers, 	pick_unit_qty_sum_layers, 	pick_unit_qty_max_layers, 	pick_unit_qty_mean_layers, 		pick_unit_qty_percentile_layers, 		cases_qty_sum_layers, 		cases_qty_sum_layers_proc + "%",			cases_qty_max_layers, 			cases_qty_mean_layers, 				cases_qty_percentile_layers, 		cases_qty_percentile_layers_proc + "%")
    my_summary_df = add_row_to_df(my_summary_df, "Cases", 				total_sku_ids_cases, 			max_daily_sku_ids_cases, 	pick_unit_qty_sum_cases, 	pick_unit_qty_max_cases, 	pick_unit_qty_mean_cases, 		pick_unit_qty_percentile_cases, 		cases_qty_sum_cases, 		cases_qty_sum_cases_proc + "%",				cases_qty_max_cases, 			cases_qty_mean_cases, 				cases_qty_percentile_cases, 		cases_qty_percentile_cases_proc + "%")
    my_summary_df = add_row_to_df(my_summary_df)
    my_summary_df = add_row_to_df(my_summary_df, "Total", 				total_sku_ids, 					max_daily_sku_ids, 			"", 						"", 						"", 							"Sum:", 								cases_qty_sum_cases_total, 	cases_qty_sum_cases_total_proc + "%", 		"", 							"", 								cases_qty_percentile_cases_total, 	cases_qty_percentile_cases_total_proc + "%")

    my_summary_df = my_summary_df.loc[:, (my_summary_df != "").any()]


    horizontal_alignment = [

    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']


    ]


    vertical_alignment = [
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center']

    ]

    uniform_width = 0.3
    procentage_width = 0.2
    procentile_width = 0.3
    col_widths = [procentage_width, uniform_width, uniform_width, uniform_width, uniform_width, uniform_width, procentile_width, uniform_width, procentage_width, uniform_width, uniform_width, procentile_width, procentage_width]







    table_ax = fig.add_axes([0.737, -0.13, 0.243, 0.55])
    table = plt.table(cellText=my_summary_df.values, loc='upper right', cellLoc='center')

    edge_color = "#343A40"
    table_color = "#EFF1F2"



    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        cell.set_width(col_widths[key[1]]) 
        
        cell.get_text().set_horizontalalignment(horizontal_alignment[key[0]][key[1]])
        cell.get_text().set_verticalalignment(vertical_alignment[key[0]][key[1]])

        
        cell.set_height(0.06 * height_scale_adjustment)
        
        cell.set_edgecolor(edge_color)
        cell.get_text().set_fontname('Arial')
        cell.get_text().set_color(font_color)
        
        
        
        
            
        if key[0] == 0:  
            
            cell.set_facecolor(table_color)         
            cell.set_height(0.12)
            
            
            
    table_ax.axis('off')
    

    buffer_png = io.BytesIO()
    plt.savefig(buffer_png, format="png")
    
    return buffer_png
def plot_3(data_df, data_cols_df, parameter_df):
    def format_float_with_commas(number, decimal_places=0):
        floored_number = round(number, decimal_places)
        
        formatted_number = f"{floored_number:,.{decimal_places}f}"
        
        return formatted_number
        
    def fill_missing_dates(df, date_col):
        
        df[date_col] = pd.to_datetime(df[date_col])
        full_date_range = pd.date_range(start=df[date_col].min(), end=df[date_col].max())
        df = df.set_index(date_col).reindex(full_date_range).reset_index()
        df = df.rename(columns={'index': date_col})
        df = df.fillna(0)
        
        return df
        
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
            
            
        


    data_df 				= data_df.reset_index(drop=True)
    data_cols_df 			= data_cols_df.reset_index(drop=True)
    parameter_df 			= parameter_df.reset_index(drop=True)

    cases_as_cases_col 		= data_cols_df.at[0,"cases_as_cases_col"]
    cases_as_pallets_col	= data_cols_df.at[0,"cases_as_pallets_col"]
    pallets_shipped_col		= data_cols_df.at[0,"pallets_shipped_col"]

    sku_id_column_name		= parameter_df.at[0,"sku_id_column_name"]
    case_qty_column_name 	= parameter_df.at[0,"case_qty_column_name"]
    ti_column_name 			= parameter_df.at[0,"ti_column_name"]
    cpp_column_name 		= parameter_df.at[0,"cpp_column_name"]
    date_column_name		= parameter_df.at[0,"date_column_name"]
    qty_percentile			= parameter_df.at[0,"qty_percentile"]


    data_df[date_column_name] = pd.to_datetime(data_df[date_column_name])
    data_df[date_column_name] = data_df[date_column_name].dt.date
    total_sku_ids 				= format_float_with_commas(data_df[sku_id_column_name].nunique())
    total_sku_ids_cases 		= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0, sku_id_column_name].nunique())
    total_sku_ids_pallets 		= format_float_with_commas(data_df.loc[data_df[cases_as_pallets_col] > 0, sku_id_column_name].nunique())


    max_daily_sku_ids 			= format_float_with_commas(data_df.groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_cases 	= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_pallets 	= format_float_with_commas(data_df.loc[data_df[cases_as_pallets_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())

    pick_unit_qty_sum_cases 	= format_float_with_commas(data_df[cases_as_cases_col].sum())
    pick_unit_qty_sum_pallets 	= format_float_with_commas(data_df[pallets_shipped_col].sum())

    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col, pallets_shipped_col]].sum().reset_index()

    pick_unit_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())
    pick_unit_qty_max_pallets 	= format_float_with_commas(max_daily_df[pallets_shipped_col].max())
    pick_unit_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    pick_unit_qty_mean_pallets 	= format_float_with_commas(max_daily_df[pallets_shipped_col].mean())

    pick_unit_qty_percentile_cases 		= format_float_with_commas(max_daily_df[cases_as_cases_col].quantile(qty_percentile/100))
    pick_unit_qty_percentile_pallets 	= format_float_with_commas(max_daily_df[pallets_shipped_col].quantile(qty_percentile/100))

    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col, cases_as_pallets_col]].sum().reset_index()

    num1 = data_df[cases_as_cases_col].sum()
    num3 = data_df[cases_as_pallets_col].sum()


    cases_qty_sum_cases 	= format_float_with_commas(num1)
    cases_qty_sum_pallets 	= format_float_with_commas(num3)

    cases_qty_sum_cases_total = format_float_with_commas(num1 + num3)

    cases_qty_sum_cases_proc 			= format_float_with_commas((num1/(num1 + num3))*100,2)
    cases_qty_sum_pallets_proc 			= format_float_with_commas((num3/(num1 + num3))*100,2)
    cases_qty_sum_cases_total_proc 		= format_float_with_commas((1)*100,2)

    cases_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())
    cases_qty_max_pallets 	= format_float_with_commas(max_daily_df[cases_as_pallets_col].max())

    cases_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    cases_qty_mean_pallets 	= format_float_with_commas(max_daily_df[cases_as_pallets_col].mean())

    num1 = max_daily_df[cases_as_cases_col].quantile(qty_percentile/100)
    num3 = max_daily_df[cases_as_pallets_col].quantile(qty_percentile/100)

    cases_qty_percentile_cases 		= format_float_with_commas(num1)
    cases_qty_percentile_pallets 	= format_float_with_commas(num3)

    cases_qty_percentile_cases_total = format_float_with_commas((num1 + num3))

    cases_qty_percentile_cases_proc 	= format_float_with_commas(((num1)/(num1 + num3))*100,2)
    cases_qty_percentile_pallets_proc 	= format_float_with_commas(((num3)/(num1 + num3))*100,2)

    cases_qty_percentile_cases_total_proc = format_float_with_commas((1)*100,2)

    grouped_df = data_df.groupby(date_column_name, as_index=False)[[cases_as_cases_col, cases_as_pallets_col]].sum()


    grouped_df = grouped_df.sort_values(by=date_column_name)
    grouped_df[date_column_name] = pd.to_datetime(grouped_df[date_column_name])



    dpi = 100
    fig_width = 1920 / dpi
    fig_height = 840 / dpi

    height_scale_adjustment = 1080/840

    font_color = "#000000"
    plt.rcParams.update({
        'font.family': 'Arial', 
        'font.size': 12, 
        'text.color': font_color
    })




    fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)
    ax = fig.add_axes([0.1, 0.55, 0.875, 0.4])  
    min_date = grouped_df[date_column_name].min() - timedelta(hours=24)
    max_date = grouped_df[date_column_name].max() + timedelta(hours=18) + timedelta(hours=24)


    color_order = ["#007FFF", "#FFA359", "#A5A5A5", "#0000FF", "#FF7F00", "#707070", "#000051", "#9E4900", "#353535"]



    bar_width = 0.2

    grouped_df_as_cases = grouped_df[[date_column_name, cases_as_cases_col]].copy(deep=True)
    grouped_df_as_cases[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=2)

    grouped_df_as_pallets = grouped_df[[date_column_name, cases_as_pallets_col]].copy(deep=True)
    grouped_df_as_pallets[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=18)





    col_name = cases_as_cases_col
    plot_df = grouped_df_as_cases
    my_label = "Cases As Cases"
    my_color = color_order[0]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)

    col_name = cases_as_pallets_col
    plot_df = grouped_df_as_pallets
    my_label = "Cases As Pallets"
    my_color = color_order[2]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.set_xlim(min_date, max_date)

    plt.xlabel('Date')
    plt.ylabel('Case QTY')
    plt.title('Case QTY of different Order fulfilment methods')

    plt.legend(loc='upper center', bbox_to_anchor=(0.945, -0.07), ncol=1)



    if qty_percentile % 10 == 1:
        percentile_txt = str(qty_percentile) + "st\nPercentile"
    else:
        if qty_percentile % 10 == 2:
            percentile_txt = str(qty_percentile) + "nd\nPercentile"
        else:
            if qty_percentile % 10 == 3:
                percentile_txt = str(qty_percentile) + "rd\nPercentile"
            else:
                percentile_txt = str(qty_percentile) + "th\nPercentile"
                

    my_summary_df = add_row_to_df()
    my_summary_df = add_row_to_df(my_summary_df, "", 					"Total SKUs", 					"Max Daily\nSKUs", 			"Pick Unit\nQTY Sum", 		"Max Daily", 				"Average Daily", 				percentile_txt, 						"Case QTY\nSum", 			"%", 										"Case QTY\nMax", 				"Average Daily", 					percentile_txt, 					"%")                 
    my_summary_df = add_row_to_df(my_summary_df, "Pallets", 			total_sku_ids_pallets, 			max_daily_sku_ids_pallets, 	pick_unit_qty_sum_pallets, 	pick_unit_qty_max_pallets, 	pick_unit_qty_mean_pallets, 	pick_unit_qty_percentile_pallets, 		cases_qty_sum_pallets, 		cases_qty_sum_pallets_proc + "%",			cases_qty_max_pallets, 			cases_qty_mean_pallets, 			cases_qty_percentile_pallets, 		cases_qty_percentile_pallets_proc + "%")

    my_summary_df = add_row_to_df(my_summary_df, "Cases", 				total_sku_ids_cases, 			max_daily_sku_ids_cases, 	pick_unit_qty_sum_cases, 	pick_unit_qty_max_cases, 	pick_unit_qty_mean_cases, 		pick_unit_qty_percentile_cases, 		cases_qty_sum_cases, 		cases_qty_sum_cases_proc + "%",				cases_qty_max_cases, 			cases_qty_mean_cases, 				cases_qty_percentile_cases, 		cases_qty_percentile_cases_proc + "%")
    my_summary_df = add_row_to_df(my_summary_df)
    my_summary_df = add_row_to_df(my_summary_df, "Total", 				total_sku_ids, 					max_daily_sku_ids, 			"", 						"", 						"", 							"Sum:", 								cases_qty_sum_cases_total, 	cases_qty_sum_cases_total_proc + "%", 		"", 							"", 								cases_qty_percentile_cases_total, 	cases_qty_percentile_cases_total_proc + "%")

    my_summary_df = my_summary_df.loc[:, (my_summary_df != "").any()]

    horizontal_alignment = [

    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']


    ]


    vertical_alignment = [
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center']

    ]

    uniform_width = 0.3
    procentage_width = 0.2
    procentile_width = 0.3
    col_widths = [procentage_width, uniform_width, uniform_width, uniform_width, uniform_width, uniform_width, procentile_width, uniform_width, procentage_width, uniform_width, uniform_width, procentile_width, procentage_width]







    table_ax = fig.add_axes([0.737, -0.13, 0.243, 0.55])
    table = plt.table(cellText=my_summary_df.values, loc='upper right', cellLoc='center')




    edge_color = "#343A40"
    table_color = "#EFF1F2"
    greyout_color = "#7F7F7F"


    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        cell.set_width(col_widths[key[1]]) 
        
        cell.get_text().set_horizontalalignment(horizontal_alignment[key[0]][key[1]])
        cell.get_text().set_verticalalignment(vertical_alignment[key[0]][key[1]])

        cell.set_height(0.06 * height_scale_adjustment)
        
        cell.set_edgecolor(edge_color)
        cell.get_text().set_fontname('Arial')
        cell.get_text().set_color(font_color)
        
        
        
        
            
        if key[0] == 0:
            cell.set_facecolor(table_color)         
            cell.set_height(0.12)
            
            
    table_ax.axis('off')


    buffer_png = io.BytesIO()
    plt.savefig(buffer_png, format="png")
    
    return buffer_png
    
def plot_4(data_df, data_cols_df, parameter_df):
    def format_float_with_commas(number, decimal_places=0):
        floored_number = round(number, decimal_places)
        
        formatted_number = f"{floored_number:,.{decimal_places}f}"
        
        return formatted_number
        
    def fill_missing_dates(df, date_col):
        
        df[date_col] = pd.to_datetime(df[date_col])
        full_date_range = pd.date_range(start=df[date_col].min(), end=df[date_col].max())
        df = df.set_index(date_col).reindex(full_date_range).reset_index()
        df = df.rename(columns={'index': date_col})
        df = df.fillna(0)
        
        return df
        
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
            
            
        


    data_df 				= data_df.reset_index(drop=True)
    data_cols_df 			= data_cols_df.reset_index(drop=True)
    parameter_df 			= parameter_df.reset_index(drop=True)

    cases_as_cases_col 		= data_cols_df.at[0,"cases_as_cases_col"]

    sku_id_column_name		= parameter_df.at[0,"sku_id_column_name"]
    case_qty_column_name 	= parameter_df.at[0,"case_qty_column_name"]
    ti_column_name 			= parameter_df.at[0,"ti_column_name"]
    cpp_column_name 		= parameter_df.at[0,"cpp_column_name"]
    date_column_name		= parameter_df.at[0,"date_column_name"]
    qty_percentile			= parameter_df.at[0,"qty_percentile"]


    data_df[date_column_name] = pd.to_datetime(data_df[date_column_name])
    data_df[date_column_name] = data_df[date_column_name].dt.date

    total_sku_ids 				= format_float_with_commas(data_df[sku_id_column_name].nunique())
    total_sku_ids_cases 		= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0, sku_id_column_name].nunique())


    max_daily_sku_ids 			= format_float_with_commas(data_df.groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    max_daily_sku_ids_cases 	= format_float_with_commas(data_df.loc[data_df[cases_as_cases_col] > 0].groupby(date_column_name)[sku_id_column_name].nunique().reset_index(name=sku_id_column_name)[sku_id_column_name].max())
    pick_unit_qty_sum_cases 	= format_float_with_commas(data_df[cases_as_cases_col].sum())

    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col]].sum().reset_index()

    pick_unit_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())

    pick_unit_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    
    pick_unit_qty_percentile_cases 		= format_float_with_commas(max_daily_df[cases_as_cases_col].quantile(qty_percentile/100))

    max_daily_df = data_df.groupby(date_column_name)[[cases_as_cases_col]].sum().reset_index()

    num1 = data_df[cases_as_cases_col].sum()


    cases_qty_sum_cases 	= format_float_with_commas(num1)

    cases_qty_sum_cases_total = format_float_with_commas(num1)

    cases_qty_sum_cases_proc 			= format_float_with_commas((num1/(num1))*100,2)
    cases_qty_sum_cases_total_proc 		= format_float_with_commas((1)*100,2)

    cases_qty_max_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].max())

    cases_qty_mean_cases 	= format_float_with_commas(max_daily_df[cases_as_cases_col].mean())
    num1 = max_daily_df[cases_as_cases_col].quantile(qty_percentile/100)

    cases_qty_percentile_cases 		= format_float_with_commas(num1)

    cases_qty_percentile_cases_total = format_float_with_commas((num1))

    cases_qty_percentile_cases_proc 	= format_float_with_commas(((num1)/(num1))*100,2)

    cases_qty_percentile_cases_total_proc = format_float_with_commas((1)*100,2)

    grouped_df = data_df.groupby(date_column_name, as_index=False)[[cases_as_cases_col]].sum()


    grouped_df = grouped_df.sort_values(by=date_column_name)
    grouped_df[date_column_name] = pd.to_datetime(grouped_df[date_column_name])



    dpi = 100
    fig_width = 1920 / dpi
    fig_height = 840 / dpi

    height_scale_adjustment = 1080/840

    font_color = "#000000"
    plt.rcParams.update({
        'font.family': 'Arial', 
        'font.size': 12, 
        'text.color': font_color
    })

    fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)
    ax = fig.add_axes([0.1, 0.55, 0.875, 0.4])
    min_date = grouped_df[date_column_name].min() - timedelta(hours=24)
    max_date = grouped_df[date_column_name].max() + timedelta(hours=18) + timedelta(hours=24)

    color_order = ["#007FFF", "#FFA359", "#A5A5A5", "#0000FF", "#FF7F00", "#707070", "#000051", "#9E4900", "#353535"]



    bar_width = 0.2

    grouped_df_as_cases = grouped_df[[date_column_name, cases_as_cases_col]].copy(deep=True)
    grouped_df_as_cases[date_column_name] = grouped_df_as_cases[date_column_name] + timedelta(hours=2)

    col_name = cases_as_cases_col
    plot_df = grouped_df_as_cases
    my_label = "Cases As Cases"
    my_color = color_order[0]

    x = plot_df[date_column_name]
    y = plot_df[col_name]

    ax.bar(x, y, width=bar_width, label=my_label, color=my_color)
    h_line_value = max(y)
    ax.axhline(y=h_line_value, color=my_color, linestyle='--', linewidth=1)

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))
    ax.set_xlim(min_date, max_date)


    plt.xlabel('Date')
    plt.ylabel('Case QTY')
    plt.title('Case QTY of different Order fulfilment methods')

    plt.legend(loc='upper center', bbox_to_anchor=(0.945, -0.07), ncol=1)

    if qty_percentile % 10 == 1:
        percentile_txt = str(qty_percentile) + "st\nPercentile"
    else:
        if qty_percentile % 10 == 2:
            percentile_txt = str(qty_percentile) + "nd\nPercentile"
        else:
            if qty_percentile % 10 == 3:
                percentile_txt = str(qty_percentile) + "rd\nPercentile"
            else:
                percentile_txt = str(qty_percentile) + "th\nPercentile"
                

    my_summary_df = add_row_to_df()
    my_summary_df = add_row_to_df(my_summary_df, "", 					"Total SKUs", 					"Max Daily\nSKUs", 			"Pick Unit\nQTY Sum", 		"Max Daily", 				"Average Daily", 				percentile_txt, 						"Case QTY\nSum", 			"%", 										"Case QTY\nMax", 				"Average Daily", 					percentile_txt, 					"%")                 
    my_summary_df = add_row_to_df(my_summary_df, "Cases", 				total_sku_ids_cases, 			max_daily_sku_ids_cases, 	pick_unit_qty_sum_cases, 	pick_unit_qty_max_cases, 	pick_unit_qty_mean_cases, 		pick_unit_qty_percentile_cases, 		cases_qty_sum_cases, 		cases_qty_sum_cases_proc + "%",				cases_qty_max_cases, 			cases_qty_mean_cases, 				cases_qty_percentile_cases, 		cases_qty_percentile_cases_proc + "%")
    my_summary_df = add_row_to_df(my_summary_df)
    my_summary_df = add_row_to_df(my_summary_df, "Total", 				total_sku_ids, 					max_daily_sku_ids, 			"", 						"", 						"", 							"Sum:", 								cases_qty_sum_cases_total, 	cases_qty_sum_cases_total_proc + "%", 		"", 							"", 								cases_qty_percentile_cases_total, 	cases_qty_percentile_cases_total_proc + "%")

    my_summary_df = my_summary_df.loc[:, (my_summary_df != "").any()]


    horizontal_alignment = [

    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right'],
    ['left', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right', 'right']


    ]


    vertical_alignment = [
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center'], 
    ['center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center', 'center']

    ]

    uniform_width = 0.3
    procentage_width = 0.2
    procentile_width = 0.3
    col_widths = [procentage_width, uniform_width, uniform_width, uniform_width, uniform_width, uniform_width, procentile_width, uniform_width, procentage_width, uniform_width, uniform_width, procentile_width, procentage_width]







    table_ax = fig.add_axes([0.737, -0.13, 0.243, 0.55])
    table = plt.table(cellText=my_summary_df.values, loc='upper right', cellLoc='center')




    edge_color = "#343A40"
    table_color = "#EFF1F2"



    for i, key in enumerate(table.get_celld().keys()):
        cell = table.get_celld()[key]
        cell.set_width(col_widths[key[1]]) 
        
        cell.get_text().set_horizontalalignment(horizontal_alignment[key[0]][key[1]])
        cell.get_text().set_verticalalignment(vertical_alignment[key[0]][key[1]])

        cell.set_height(0.06 * height_scale_adjustment)
        
        cell.set_edgecolor(edge_color)
        cell.get_text().set_fontname('Arial')
        cell.get_text().set_color(font_color)
        
        
        
        
            
        if key[0] == 0:  
            cell.set_facecolor(table_color)
            cell.set_height(0.12)
            
    table_ax.axis('off')

    
    buffer_png = io.BytesIO()
    plt.savefig(buffer_png, format="png")
    
    return buffer_png 

def format_float_with_commas(number, decimal_places=0):
    floored_number = round(number, decimal_places)
    
    formatted_number = f"{floored_number:,.{decimal_places}f}"
    
    return formatted_number

def fx_print_param_fx(d):
    for key, value in d.items():
        print(key + ' = ' + 'my_parameters["' + key + '"]')
        
        
def fx_get_unused_name(dataframe1, column_to_join):
    
    suffix = ''
    new_column_name = column_to_join
    
    while new_column_name in dataframe1.columns:
        suffix = f'_{int(suffix[1:]) + 1 if suffix else 1}'
        new_column_name = column_to_join + suffix
    
    assigned_column_name = new_column_name
    
    
    
    return assigned_column_name 

data_df = input_1.to_pandas()
data_df = data_df.reset_index(drop=True)
parameter_df = pd.DataFrame()

parameter_df.at[0,"sku_id_column_name"] = self.column_param_sku_id
parameter_df.at[0,"case_qty_column_name"] = self.column_param_case_qty
parameter_df.at[0,"ti_column_name"] = self.column_param_ti
parameter_df.at[0,"cpp_column_name"] = self.column_param_cpp
parameter_df.at[0,"date_column_name"] = self.column_param_date
parameter_df.at[0,"qty_percentile"] = self.percentile_param

case_qty_column_name = parameter_df.at[0,"case_qty_column_name"]
ti_column_name = parameter_df.at[0,"ti_column_name"]
cpp_column_name = parameter_df.at[0,"cpp_column_name"]





col_name_df = pd.DataFrame()
cases_as_cases_col = "dab_fax_cases_as_cases"
cases_as_cases_col = fx_get_unused_name(data_df, cases_as_cases_col)
col_name_df.at[0, "cases_as_cases_col"] = cases_as_cases_col

cases_as_layers_col = "dab_fax_cases_as_layers"
cases_as_layers_col = fx_get_unused_name(data_df, cases_as_layers_col)
col_name_df.at[0, "cases_as_layers_col"] = cases_as_layers_col

layers_shipped_col = "dab_fax_layers_shipped"
layers_shipped_col = fx_get_unused_name(data_df, layers_shipped_col)
col_name_df.at[0, "layers_shipped_col"] = layers_shipped_col

cases_as_pallets_col = "dab_fax_cases_as_pallets"
cases_as_pallets_col = fx_get_unused_name(data_df, cases_as_pallets_col)
col_name_df.at[0, "cases_as_pallets_col"] = cases_as_pallets_col

pallets_shipped_col = "dab_fax_pallets_shipped"
pallets_shipped_col = fx_get_unused_name(data_df, pallets_shipped_col)
col_name_df.at[0, "pallets_shipped_col"] = pallets_shipped_col

data_df_cac = data_df.copy(deep=True)
data_df_cac[cases_as_cases_col] = 0

data_df_cac[cases_as_cases_col] = data_df_cac[case_qty_column_name]
data_df_cacl = data_df.copy(deep=True)

data_df_cacl[cases_as_cases_col] = 0

data_df_cacl[cases_as_layers_col] = 0
data_df_cacl[layers_shipped_col] = 0

data_df_cacl[cases_as_cases_col] = data_df_cacl[case_qty_column_name]


data_df_cacl[layers_shipped_col] = np.where(
    data_df_cacl[ti_column_name] == 0,
    0,
    np.floor(data_df_cacl[cases_as_cases_col] / data_df_cacl[ti_column_name])
)

data_df_cacl[cases_as_layers_col] = data_df_cacl[layers_shipped_col] * data_df_cacl[ti_column_name]
data_df_cacl[cases_as_cases_col] = data_df_cacl[cases_as_cases_col] - data_df_cacl[cases_as_layers_col]

data_df_cacp = data_df.copy(deep=True)

data_df_cacp[cases_as_cases_col] = 0

data_df_cacp[cases_as_pallets_col] = 0
data_df_cacp[pallets_shipped_col] = 0

data_df_cacp[cases_as_cases_col] = data_df_cacp[case_qty_column_name]


data_df_cacp[pallets_shipped_col] = np.where(
    data_df_cacp[cpp_column_name] == 0,
    0,
    np.floor(data_df_cacp[cases_as_cases_col] / data_df_cacp[cpp_column_name])
)

data_df_cacp[cases_as_pallets_col] = data_df_cacp[pallets_shipped_col] * data_df_cacp[cpp_column_name]
data_df_cacp[cases_as_cases_col] = data_df_cacp[cases_as_cases_col] - data_df_cacp[cases_as_pallets_col]

data_df_caclp = data_df.copy(deep=True)

data_df_caclp[cases_as_cases_col] = 0

data_df_caclp[cases_as_layers_col] = 0
data_df_caclp[layers_shipped_col] = 0

data_df_caclp[cases_as_pallets_col] = 0
data_df_caclp[pallets_shipped_col] = 0

data_df_caclp[cases_as_cases_col] = data_df_caclp[case_qty_column_name]


data_df_caclp[pallets_shipped_col] = np.where(
    data_df_caclp[cpp_column_name] == 0,
    0,
    np.floor(data_df_caclp[cases_as_cases_col] / data_df_caclp[cpp_column_name])
)

data_df_caclp[cases_as_pallets_col] = data_df_caclp[pallets_shipped_col] * data_df_caclp[cpp_column_name]
data_df_caclp[cases_as_cases_col] = data_df_caclp[cases_as_cases_col] - data_df_caclp[cases_as_pallets_col]

data_df_caclp[layers_shipped_col] = np.where(
    data_df_caclp[ti_column_name] == 0,
    0,
    np.floor(data_df_caclp[cases_as_cases_col] / data_df_caclp[ti_column_name])
)

data_df_caclp[cases_as_layers_col] = data_df_caclp[layers_shipped_col] * data_df_caclp[ti_column_name]
data_df_caclp[cases_as_cases_col] = data_df_caclp[cases_as_cases_col] - data_df_caclp[cases_as_layers_col]

data_cols_df = pd.DataFrame()

data_cols_df.at[0,"cases_as_cases_col"] = "dab_fax_cases_as_cases"
data_cols_df.at[0,"cases_as_layers_col"] = "dab_fax_cases_as_layers"
data_cols_df.at[0,"layers_shipped_col"] = "dab_fax_layers_shipped"
data_cols_df.at[0,"cases_as_pallets_col"] = "dab_fax_cases_as_pallets"
data_cols_df.at[0,"pallets_shipped_col"] = "dab_fax_pallets_shipped"

buffer_png_1 = plot_1(data_df_caclp, data_cols_df, parameter_df)
buffer_png_2 = plot_2(data_df_cacl, data_cols_df, parameter_df)
buffer_png_3 = plot_3(data_df_cacp, data_cols_df, parameter_df)
buffer_png_4 = plot_4(data_df_cac, data_cols_df, parameter_df)

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
ax.plot(x, y)

buffer_png = io.BytesIO()
plt.savefig(buffer_png, format="png")

return data_df_caclp, buffer_png_1.getvalue(), data_df_cacl, buffer_png_2.getvalue(), data_df_cacp, buffer_png_3.getvalue(), data_df_cac, buffer_png_4.getvalue())
