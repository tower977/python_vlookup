# python_vlookup

This program aims to replace the need to write cumbersome excel vba functions, particularly excel vlookup.

Playing with excel files can lead to human error, as excel functions are easily broken. This method when used correctly can be used on any two excel files. With the correct parameters entered the results will be slightly quicker than the row by row macro application. This is due to the beauty of pandas, a vectorised package.

Additionally, this method not only works well with workbooks; but if we needed to access JSON and sql data. Using python to combine them all is simply the smartest use of resources.


The sequence in which the parameters need to be entered for the script in the terminal;

python3 | name of script | workbook1 | workbook2 | output workbook | column to be renamed | renamed column | column to be merged or searched
