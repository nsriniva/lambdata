from lambdata_nsriniva import helper_functions

null_count = helper_functions.null_count

abbr_2_st = helper_functions.abbr_2_st

from pandas import DataFrame, Series
from numpy import NaN

ST_ABBR = ('st','abbr')

Null_DF = DataFrame({'col0':[NaN, 4, 3],'col1':[9,NaN, NaN], 'col2':[10, 2, 2]})

abbr_st = DataFrame({ST_ABBR[1]:['AL', 'AZ', 'CA', 'DE', 'OH'], ST_ABBR[0]:['Alabama','Arizona','California','Delaware','Ohio']})

print(Null_DF)
print(abbr_st)

print(f'Null Count : {null_count(Null_DF)}\n')
print(f'Output Series:\n{abbr_2_st(abbr_st[ST_ABBR[1]])}\n')
print(f'Output Series:\n{abbr_2_st(abbr_st[ST_ABBR[0]], False)}\n')
