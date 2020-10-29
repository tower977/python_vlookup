import pandas as pd
import numpy as np

#retrieve inputted filnames
initial_workbook = sys.argv[1] #workbook1
info_workbook = sys.argv[2] #workbook2
output_workbook = 'output.xlsx' #output workbook
column_rename = sys.argv[3] #column to be renamed
new_column_name = sys.argv[4] # renamed column
column_to_merge = sys.argv[5] #column to be merged or searched


#assign each workbook to a dataframe

df_initial = pd.read_excel(initial_workbook)
df_info = pd.read_excel(info_workbook)

#rename column to column
df_initial.rename(columns={column_rename:new_column_name}, inplace=True)

#merge columns
df_3 = pd.merge(df_initial, df_info[[new_column_name,column_to_merge]], on=new_column_name, how='left')

#rename column to original heading
df_3.rename(columns={new_column_name:column_rename}, inplace=True)

#replace all nan's with white space
df_3 = df_3.replace(np.nan, '', regex=True)

#reaad out to desire file
df_3.to_excel(output_workbook, index=False)
