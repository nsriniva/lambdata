#from lambdata_nsriniva import helper_functions
from lambdata_nsriniva.helper_functions import null_count, abbr_2_st, train_test_split, list_2_series

#null_count = helper_functions.null_count

#abbr_2_st = helper_functions.abbr_2_st

from pandas import DataFrame, Series
from numpy import NaN

ST_ABBR = ('st', 'abbr')

Null_DF = DataFrame({'col0': [NaN, 4, 3], 'col1': [
                    9, NaN, NaN], 'col2': [10, 2, 2]})

abbr_st = DataFrame({ST_ABBR[1]: ['AL', 'AZ', 'CA', 'DE', 'OH'], ST_ABBR[0]: [
                    'Alabama', 'Arizona', 'California', 'Delaware', 'Ohio']})

Split_DF = DataFrame({'col0': [0, 3, 6], 'col1': [
    1, 4, 7], 'col2': [2, 5, 8]})

print(Null_DF)
print(abbr_st)

print(f'Null Count : {null_count(Null_DF)}\n')
print(f'Output Series:\n{abbr_2_st(abbr_st[ST_ABBR[1]])}\n')
print(f'Output Series:\n{abbr_2_st(abbr_st[ST_ABBR[0]], False)}\n')

train_df, test_df = train_test_split(Split_DF)
print(f'Train DataFrame:\n{train_df}\n')
print(f'Test DataFrame:\n{test_df}\n')

list_2_series([10, 9, 8], Split_DF)

print(f'DataFrame with added column:\n{Split_DF}')
