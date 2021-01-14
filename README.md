# lambdata
This is a package that is being created as part of my coursework for Unit 3 of Lambda School's Data Science program.

To use 
`from lambdata_nsriniva import helper_functions`

The `helper_functions` module implements:
`null_count(df)`: Check a dataframe for nulls and return the number of missing values.
				returns null count integer

and

`abbr_2_st(state_series, abbr_2_st=True)`: Return a new column with the full name from a State abbreviation column -> An input of FL would return Florida. This function should also take a boolean (abbr_2_state) and when False takes full state names and return state abbreviations. -> An input of Florida would return Fl.
										returns pd.Dataframe with translations