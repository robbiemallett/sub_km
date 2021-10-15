## Code repository for:

# Sub-kilometre scale distribution of snow depth on Arctic sea ice from Soviet drifting stations

## Mallett et al. (In Prep)
### Structure

All analysis for this paper was performed in Python in Jupyter Notebooks.

The notebooks required to reproduce the analysis in the paper are in the notebooks directory.

The NP snow depth transect is stored in the NP_transects directory.

### Reproducing the main analysis

The first step is to wrangle the numerous transect files (in NP_transects) into one object. This is done in the Process_line_data.ipynb notebook. It gathers all the transects into one Python dictionary. This dictionary is then saved as a pickle file (pickles/line_depths_dict.p') for future use by different notebooks. The pickle file is included in the github repo, so you don't need to make it yourself.

I have also produced a spreadsheet called stake_depths.xlsx that has all the data from the individual files. But the main analysis uses the raw data - this excel file is just for the convenience of others.

The coefficient of variation regression and skew normal fit of the data are done in Make_fit.ipynb. Once again, the results of this analysis are stored in a Python dictionary (pickles/statistics.p) for use within other notebooks. The analysis is performed for all seasons, winter and summer.



