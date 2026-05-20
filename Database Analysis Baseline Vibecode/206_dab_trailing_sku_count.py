import pandas as pd
from category import data_analysis_category

from datetime import datetime, timedelta
import matplotlib.pyplot as plt

import io



# Copyright (c) 2026 fromdablockjenny9-oss @Github
# This project and its source code are the property of fromdablockjenny9-oss @Github
# Unauthorized copying, modification, or distribution is prohibited
# fromdablockjenny9@gmail.com

def fill_missing_dates(df):
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    min_date = df['Date'].min()
    max_date = df['Date'].max()
    all_dates = pd.date_range(start=min_date, end=max_date).to_frame(index=False, name="Date")
    all_dates['Date'] = all_dates['Date'].dt.date
    df_full = pd.merge(all_dates, df, on="Date", how="left")
    for col in df_full.columns:
        if df_full[col].dtype == 'string':  
            df_full[col].fillna("", inplace=True)
        elif pd.api.types.is_numeric_dtype(df_full[col]): 
            df_full[col].fillna(0, inplace=True)
    return df_full
    
def get_unique_sorted_dates(df, date_col):
    unique_dates = df[[date_col]].drop_duplicates().sort_values(by=date_col, ascending=True)
    unique_dates.reset_index(drop=True, inplace=True)
    return unique_dates
    
def trailing_unique_id_count(df, num_days, date_col, id_col):
    unique_date_df = get_unique_sorted_dates(df, date_col)
    result_col_name = id_col + " Count (" + str(num_days) + "d.)"
    unique_date_df[result_col_name] = 0
    df[date_col] = pd.to_datetime(df[date_col]).dt.date
    for i in range(len(unique_date_df)):
        current_date = unique_date_df.at[i,date_col]
        start_date = current_date - pd.Timedelta(days=(num_days-1))
        trailing_ids = df[(df[date_col] >= start_date) & (df[date_col] <= current_date)][id_col]
        if trailing_ids.nunique() > 1:
            trailing_ids1 = trailing_ids[trailing_ids != '']
            unique_id_count = trailing_ids1.nunique()
        else:
            unique_id_count = 0
        unique_date_df.at[i,result_col_name] = unique_id_count
    return unique_date_df
    
def format_float_with_commas(number, decimal_places=0):
    floored_number = round(number, decimal_places)
    formatted_number = f"{floored_number:,.{decimal_places}f}"
    return formatted_number	
df = input_1.to_pandas()

sku_id_column_name    = self.column_param_sku_id
date_column_name    = self.column_param_date

plot_0_day_count = int(self.plot_0_day_count)
plot_1_day_count = int(self.plot_1_day_count)
plot_2_day_count = int(self.plot_2_day_count)
plot_3_day_count = int(self.plot_3_day_count)
plot_4_day_count = int(self.plot_4_day_count)

df1 = df[df[sku_id_column_name] != '']
unique_SKU_ID_count = df1[sku_id_column_name].nunique()


df_filled = fill_missing_dates(df)


df = df_filled


if plot_0_day_count != 0:
    result_df_0 = trailing_unique_id_count(df, plot_0_day_count, date_col=date_column_name, id_col=sku_id_column_name)
    
if plot_1_day_count != 0:
    result_df_1 = trailing_unique_id_count(df, plot_1_day_count, date_col=date_column_name, id_col=sku_id_column_name)

if plot_2_day_count != 0:
    result_df_2 = trailing_unique_id_count(df, plot_2_day_count, date_col=date_column_name, id_col=sku_id_column_name)

if plot_3_day_count != 0:
    result_df_3 = trailing_unique_id_count(df, plot_3_day_count, date_col=date_column_name, id_col=sku_id_column_name)

if plot_4_day_count != 0:
    result_df_4 = trailing_unique_id_count(df, plot_4_day_count, date_col=date_column_name, id_col=sku_id_column_name)

merged_df = get_unique_sorted_dates(df, date_col=date_column_name)


if plot_0_day_count != 0:
    merged_df = pd.merge(merged_df, result_df_0, how='left', on=date_column_name)

if plot_1_day_count != 0:
    merged_df = pd.merge(merged_df, result_df_1, how='left', on=date_column_name)

if plot_2_day_count != 0:
    merged_df = pd.merge(merged_df, result_df_2, how='left', on=date_column_name)

if plot_3_day_count != 0:
    merged_df = pd.merge(merged_df, result_df_3, how='left', on=date_column_name)

if plot_4_day_count != 0:
    merged_df = pd.merge(merged_df, result_df_4, how='left', on=date_column_name)

def format_float_with_commas(number, decimal_places=0):
    floored_number = round(number, decimal_places)
    formatted_number = f"{floored_number:,.{decimal_places}f}"
    
    return formatted_number

data = merged_df
column_inclusion_list = []

color_order = []

if int(self.plot_0_day_count) > 0:
    column_inclusion_list.append("SKU ID Count (" + str(self.plot_0_day_count) + "d.)")
    color_order.append("#007FFF")
    
if int(self.plot_1_day_count) > 0:
    column_inclusion_list.append("SKU ID Count (" + str(self.plot_1_day_count) + "d.)")
    color_order.append("#FFA359")
    
if int(self.plot_2_day_count) > 0:
    column_inclusion_list.append("SKU ID Count (" + str(self.plot_2_day_count) + "d.)")
    color_order.append("#A5A5A5")
    
if int(self.plot_3_day_count) > 0:
    column_inclusion_list.append("SKU ID Count (" + str(self.plot_3_day_count) + "d.)")
    color_order.append("#0000FF")
    
if int(self.plot_4_day_count) > 0:
    column_inclusion_list.append("SKU ID Count (" + str(self.plot_4_day_count) + "d.)")
    color_order.append("#FF7F00")

dpi = 100
fig_width = 1920 / dpi
fig_height = 1080 / dpi

fig = plt.figure(figsize = (fig_width, fig_height), dpi = dpi)

first_run = 1
color_order_i = 0
table_row_i = 0

ax = fig.add_axes([0.1, 0.6, 0.8, 0.35])

plot_df = pd.DataFrame()
plot_df["Column"] = None
plot_df["Value"] = None

plot_df.at[table_row_i, "Column"] = "Total Active SKUs"
plot_df.at[table_row_i, "Value"] = format_float_with_commas(unique_SKU_ID_count, decimal_places=0)
table_row_i = table_row_i + 1

for col in data.columns:

    if color_order_i == len(color_order):
        color_order_i = 0


    if first_run == 1:
        x = data[col]
    else:
        if col in column_inclusion_list:
            y = data[col]
            ax.plot(x, y, label=col, color=color_order[color_order_i], marker='', linestyle='-', linewidth=3)
            
            h_line_value = max(y)
            ax.axhline(y=h_line_value, color=color_order[color_order_i], linestyle='--', linewidth=1)
            plot_df.at[table_row_i, "Column"] = "Max Of " + col
            plot_df.at[table_row_i, "Value"] = format_float_with_commas(h_line_value, decimal_places=0)
            
            color_order_i = color_order_i + 1
            table_row_i = table_row_i + 1
        
    if first_run == 1:
        first_run = 0

plt.xlabel('Date')
plt.ylabel('SKUs')
plt.title('Trailing Count of unique SKUs\n')

plt.legend(loc='upper center', bbox_to_anchor=(0.94, -0.15), ncol=1)

table_ax = fig.add_axes([0.11, 0.25, 0.2, 0.45])
table = plt.table(cellText=plot_df.values, loc='center', cellLoc='center')


col_widths = [0.9, 0.2]

for i, key in enumerate(table.get_celld().keys()):
    cell = table.get_celld()[key]
    cell.set_width(col_widths[key[1]])  
    cell.set_fontsize(12)
    cell.set_height(0.05)

table_ax.axis('off')


buffer_png = io.BytesIO()
plt.savefig(buffer_png, format="png")

return merged_df, buffer_png.getvalue())
