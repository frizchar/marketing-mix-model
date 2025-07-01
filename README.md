# Marketing Mix Model
### Overview
__Marketing Mix Modeling__ (_MMM_) is a forecasting technique that evaluates how different marketing strategies affect product sales. It uses statistical methods like multivariate regression on sales and marketing time-series data. MMM helps optimize advertising and promotional efforts to maximize sales, revenue, or profit, improving return on investment through data-driven decisions.

In our implementation we utilize the [robyn](https://pypi.org/project/robynpy/) package.

### Input file & Variables:
Input file ```marketing_data.csv``` includes the following variables:
- sales (_target variable_)
- TV_impressions, Digital_clicks, Radio_GRPs (_paid media variables_)
- Newsletter_sends, Social_media_posts (_organic variables_)
- Competitor_sales, Holiday (_context variables_)

### Usage
- install the __robyn__ package with ```pip install robynpy```
- input file ```marketing_data.csv``` needs to be saved in the same folder with file ```main.py```

### Dependencies
Python interpreter version used for this project: **3.9.4**
