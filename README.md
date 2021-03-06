## Code and data repository for:

# Sub-kilometre scale distribution of snow depth on Arctic sea ice from Soviet drifting stations

## Mallett et al., 2022
## Journal of Glaciology

### General

You can download the paper and supplement in the */submission* directory, and you can get the raw figure files in */figures*.

All analysis for this paper was performed in Python in Jupyter Notebooks on a Linux machine. 

The notebooks required to reproduce the analysis in the paper are in the */notebooks* directory. The NP snow depth transect data are stored in the */NP_transects* directory.

The transect data were supplied in a private communication from the National Snow and Ice Data Center, in Boulder, CO, USA. They are not (to the lead author's knowledge) currently publicly available elsewhere on the internet.

### Reproducing the main analysis & Figure 3

The first step is to wrangle the numerous transect files (in /NP_transects) into one data structure. This is done in the Process_line_data.ipynb notebook. It gathers all the transects into one Python dictionary. This dictionary is then saved as a pickle file (/pickles/line_depths_dict.p') for future use by different notebooks. The pickle file is included in the github repo, so you don't need to make it yourself.

I have also produced a spreadsheet called stake_depths.xlsx that has all the data from the individual files. But the main analysis uses the raw data - this excel file is just for the convenience of others.

The coefficient of variation regression and skew normal fit of the data are done in /notebooks/Make_fit.ipynb. Once again, the results of this analysis are stored in a Python dictionary (/pickles/statistics.p) for use within other notebooks. The analysis is performed for all seasons, winter and summer. This notebook also generates **Figure 3**. 

### Reproducing other main text figures

**Figure 1** (showing the map of the snow transects used in the study) is used in F1_make_map.ipynb.

**Figure 2** (showing the timeline of the NP station transects) is made using F2_make_transects_fig.ipynb.

**Figure 4** (showing the fits of the gamma, log-normal and skew normal distributions) is made using F4_compare_distributions.ipynb. 

**Figure 5** (showing the LOOCV analysis) is made using F5_cross_validation.ipynb

**Figure 6** and **Figure 7** (showing the MOSAiC evaluations) are made using F6_7_compare_MOSAiC.ipynb. However, these data are not currently available. As soon as they become available, I will link them here. This will either be in January 2023 when the embargo on MOSAiC data is lifted, or earlier when a dedicated paper to the magnaprobe data is released.

**Figure 8** and **Figure 9** (showing the SHEBA evaluations) are made using F8_9_compare_SHEBA.ipynb

**Figure 10** (showing best skew normal fits to the above evaluation data) is also made using F10_compare_SHEBA.ipynb

**Figure 11** (showing the FYI evaluations) is made using F11_compare_FYI.ipynb

**Figure 12** (showing the correlation lengths and sampling interval analysis) is made using F12_autocorrelation.ipynb (top two panels) and Explore_sampling_density.ipynb (bottom two panels)

### Reproducing supplementary figures

**Figure S1** (showing the point density of Fig. 2a) is made using Make_fit.ipynb

**Figure S2** (showing the sample skewness of the evaluation data) is made using compare_FYI.ipynb

**Figure S3** (showing the best skew normal fits to the MOSAiC runway transects) is made using compare_MOSAiC.ipynb

**Figure S4** (showing the areal coverage of negative snow depths in the NP model) is made using Negative_depths.ipynb

**Figure S5** (showing the coefficient of variation for the FYI evaluations) is made using compare_FYI.ipynb

**Figure S6** (showing the best skew normal fits to the MOSAiC runway transects) is made using compare_FYI.ipynb

**Figure S7** (showing the correlation lengths of the NP transects) is made using autocorrelation.ipynb

### Key python modules used

All data visualisation was made using Matplotlib (Hunter, 2007). 

Numerical analysis was performed with numpy (Harris et al., 2020), pandas (McKinney, 2010) and scipy (Virtanen et al., 2020).

### References

Harris, C.R., Millman, K.J., van der Walt, S.J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N.J. and Kern, R., 2020. Array programming with NumPy. Nature, 585(7825), pp.357-362.

Hunter, J.D., 2007, Matplotlib: A 2D Graphics Environment, Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95

McKinney, W., 2010, June. Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).

Mallett, R., Stroeve, J.C., Tsamados, M., Willatt, R., Newman, T., Nandan, V., Landy, J., Itkin, P., Oggier, M., Jaggi, M. and Perovich, D., 2021. Sub-kilometre scale distribution of snow depth on Arctic sea ice from Soviet drifting stations. _EarthArXiv Preprint_

Virtanen, P., Gommers, R., Oliphant, T.E., Haberland, M., Reddy, T., Cournapeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J. and Van Der Walt, S.J., 2020. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nature methods, 17(3), pp.261-272.




