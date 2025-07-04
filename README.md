# Marketing Mix Model
### Overview
__Marketing Mix Modeling__ (_MMM_) is a forecasting technique that evaluates how different marketing strategies affect product sales. It uses statistical methods like multivariate regression on sales and marketing time-series data. MMM helps optimize advertising and promotional efforts to maximize sales, revenue, or profit, improving return on investment through data-driven decisions.

In our implementation we utilize the [robyn](https://pypi.org/project/robynpy/) package.

### Input file & Variables:
Input file ```marketing_data.csv``` includes the following variables:
- $${ \color{blue} \mathrm{sales} }$$ (_target variable_)
- $${ \color{green} \mathrm{TV\\_impressions^*, \space Digital\\_clicks,  \space Radio\\_GRPs^{**}} }$$ (_predictor variables_; $${ \color{purple} paid \space media \space variables }$$)
- $${ \color{green} \mathrm{Newsletter\\_sends, \space Social\\_media\\_posts} }$$ (_predictor variables_; $${ \color{purple} organic \space variables }$$)
- $${ \color{green} \mathrm{Competitor\\_sales, \space Holiday} }$$ (_predictor variables_; $${ \color{purple} context \space variables }$$)

\* _TV impressions_ := _number of times a television advertisement is displayed or seen_  
** _Radio Gross Rating Points_ := _measures the total audience reach and frequency of a radio advertisement_

### Usage
- install package __robyn__ with ```pip install robynpy```
- input file ```marketing_data.csv``` needs to be saved in the same folder with file ```main.py```

### Dependencies
Python interpreter version used for this project: **3.9.4**
