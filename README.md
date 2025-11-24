# Oil_Specific_Stress_Test
This is a project I did during my rotation with Oil Desk at RWE Supply & Trading. Due to company policy, the output of the notebook, source data, the complete structure of original folder, and Jobs & Pipelines will not be displayed here. Instead, the core notebook, sql files, and modules file are available. 



## Business Purpose & Introduction
As a part of monthly task for risk analysis, we carry out stress test on the current exposure with the worst 5-day return during the past five years on portfolio level. Portfolios with the largest 5 loss will be displayed along with dates those losses happend. One portfolio usually contains one pair or several pairs of indices (commodities) to reflect the views we have on the spreads. For example, if we take a long position on EU Diesel Cracks Portfolio, that means we have long positions on diesel and short positions on Brent Crude. 

## Data
The following three types of data are queried through three .sql files from the company's database.

### Exposure
Exposure measures how much delta do we have under each index for each delivery month. 

### Historical Prices 
Price data includes closing price of each index for each delivery month in the past five years.

### FX Spot Rate
As not all products are traded in USD, we introduce FX rate to standardize the currency. 

## Technique Realization (Brief)
1. Load the exposure, price, and fx rate data above
2. Prepare these data. For example, for price data, we need to convert the unit of the commodity so that it is aligned with the one used in the exposure data.
3. Calculate 5 days price change of each index for each relative delivery period.
4. Calculate 5 days return based on current exposure data.
5. Aggregate return on index to return on portfolio.
6. Sort returns and display results.
7. Upload results to the database.

## Jobs & Pipelines
This notebook is scheduled to be run daily on 8:30 AM (GMT) using the last business exposure data, and relavent output will be sent to the desk through email. For manual execution, users may select the Date parameter through the widget built in cob_widget.py. This module sets the Date as the last business day by default and restricts users to select working days in the past only. 

































