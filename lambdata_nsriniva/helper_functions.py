'''
This module exports the following methods

null_count(input_df)
abbr_2_st(abbr_or_st_series, input_abbr=True)
train_test_split(input_df, frac=0.2)
list_2_series(list_2_series, input_df, col_name='NewCol')
'''

from pandas import DataFrame, Series
from numpy import NaN
from sklearn.model_selection import train_test_split as skl_split
from .us_state_abbrev import us_state_abbrev, abbrev_us_state

import unittest


def null_count(input_df):
    '''
    Check a dataframe for nulls and return the number of missing values.
    Input:
    input_df -> DataFrame to be checked for nulls
    Return:
    int -> number of nulls in input_df
    '''
    print('Input DataFrame:')
    print(input_df)

    return input_df.isna().sum().sum()


ST_ABBR = ('abbr', 'st')


def abbr_2_st(abbr_or_st_series, input_abbr=True):
    '''
    Takes US state abbreviations and returns names or vice versa
    Input:
    abbr_or_st_series -> Series with abbreviations or names
    input_abbr        -> bool with value set to True if abbr_or_st_series contains
                        abbreviations and False otherwise
    Return:
    Series -> state names if input_abbr is True else abbreviations
    '''
    ret_list = list()

    # us_state_abbrev -> dictionary mapping state names to abbreviations
    # abbrev_us_state -> dictionary mapping state abbreviations to names
    opers = ((us_state_abbrev, 'name'), (abbrev_us_state, 'abbreviation'))

    # oper will be set to 1 if input_abbr is True else 0
    oper = int(input_abbr)

    print('Input Series:')
    print(abbr_or_st_series)

    for elem in abbr_or_st_series:
        # opers[oper][0] -> abbrev_us_state if input_abbr is True else us_state_abbrev
        # opers[oper][1] -> 'abbreviation' if input_abbr is True else 'name'
        # Get state name from abbreviation if input_abbr is True else vice_versa
        # If there is no valid mapping, get an appropriate error string
        # Append the return value to ret_list
        ret_list.append(opers[oper][0].get(
            elem, f'{elem} is not a valid state {opers[oper][1]}'))

    # ST_ABBR[oper] -> 'st' if input_abbr is True else 'abbr'
    # Convert the list to a Series named 'st' if ret_list contains state names and 'abbr'
    # if it containts abbreviations
    ret_series = Series({ST_ABBR[oper]: ret_list})

    return ret_series


def train_test_split(input_df, frac=0.2):
    '''
    Given an input dataframe and the percentage required for the training set returns
    training and test dataframes.
    Input:
    input_df  -> DataFrame to be split
    frac      -> Percent of data to set aside for training
    '''

    # The smallest value that frac can be to have at least one entry
    # in the training dataset
    min_frac = 1/input_df.shape[0]

    # Force frac to be at least min_frac
    frac = max(frac, min_frac)

    return skl_split(input_df, train_size=frac)


def list_2_series(input_list, input_df, col_name='NewCol'):
    '''
    Given a list and a  dataframe add the list as a new column to the dataframe.
    Input:
    input_df        -> DataFrame to which the list needs to be added as a column
    list_2_seriex   -> list to be added as new column to the dataframe
    col_name        -> name of the new column to be added
    '''
    input_df[col_name] = Series(input_list)


class TestHelperFunctions(unittest.TestCase):

    Split_DF = DataFrame({'col0': [0, 3, 6], 'col1': [
        1, 4, 7], 'col2': [2, 5, 8]})

    def test_null_count(self):
        Null_DF = DataFrame({'col0': [NaN, 4, 3], 'col1': [
            9, NaN, NaN], 'col2': [10, 2, 2]})

        self.assertEqual(null_count(Null_DF), 3)

    def test_abbr_2_st(self):
        abbr_st = DataFrame({ST_ABBR[0]: ['AL', 'AZ', 'CA', 'DE', 'OH'],
                             ST_ABBR[1]: ['Alabama', 'Arizona', 'California', 'Delaware', 'Ohio']})

        self.assertEqual(abbr_2_st(abbr_st[ST_ABBR[0]]).tolist()[
                         0], abbr_st[ST_ABBR[1]].tolist())
        self.assertEqual(abbr_2_st(abbr_st[ST_ABBR[1]], False).tolist()[
                         0], abbr_st[ST_ABBR[0]].tolist())

    def test_train_test_split(self):

        train_df, test_df = train_test_split(TestHelperFunctions.Split_DF)

        self.assertEqual(train_df.shape[0], 1)
        self.assertEqual(test_df.shape[0], 2)

    def test_list_2_series(self):

        orig_cols = len(TestHelperFunctions.Split_DF.columns)

        list_2_series([10, 9, 8], TestHelperFunctions.Split_DF)
        self.assertEqual(TestHelperFunctions.Split_DF.shape[1], orig_cols+1)


if __name__ == "__main__":
    unittest.main()
