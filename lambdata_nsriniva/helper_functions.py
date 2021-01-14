from pandas import DataFrame, Series
from numpy import NaN
from .us_state_abbrev import us_state_abbrev, abbrev_us_state

def null_count(df):
    print('Input DataFrame:')
    print(df)

    return df.isna().sum().sum()

ST_ABBR = ('st','abbr')

def abbr_2_st(state_series, abbr_2_st=True):
    ret_list = list()

    opers = ((us_state_abbrev, 'name'),(abbrev_us_state, 'abbreviation'))
    
    oper = int(abbr_2_st)
    
    print('Input Series:')
    print(state_series)

    for elem in state_series:
        ret_list.append(opers[oper][0].get(elem,f'{elem} is not a valid state {opers[oper][1]}'))
    
    #states_df = DataFrame()
    #states_df[ST_ABBR[oper]] = state_series  
    #states_df[ST_ABBR[1-oper]] = Series(ret_list)

    ret_series = Series({ST_ABBR[1-oper]:ret_list})

    return ret_series

if __name__ == "__main__":
    Null_DF = DataFrame({'col0':[NaN, 4, 3],'col1':[9,NaN, NaN], 'col2':[10, 2, 2]})
    abbr_st = DataFrame({ST_ABBR[1]:['AL', 'AZ', 'CA', 'DE', 'OH'], ST_ABBR[0]:['Alabama','Arizona','California','Delaware','Ohio']})

    print(Null_DF)
    print(abbr_st)

    print(f'Null Count : {null_count(Null_DF)}\n')
    print(f'Output Series:\n{abbr_2_st(abbr_st[ST_ABBR[1]])}\n')
    print(f'Output Series:\n{abbr_2_st(abbr_st[ST_ABBR[0]], False)}\n')
