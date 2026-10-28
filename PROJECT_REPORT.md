# Project Report: AI Electricity Bill Forecaster

## Student Details
- **Name:** Sheetal Ramteke
- **Roll Number:** 25081
- **Project Title:** AI Electricity Bill Forecaster
- **Academic Level:** Intermediate
- **Institute:** Not provided

## 1. Abstract
This Python console application estimates the next month's electricity bill from six user-entered monthly bills using a simple linear-regression calculation. It also estimates appliance costs and possible savings from reducing daily air-conditioner usage.

## 2. Problem Statement
Households may want to anticipate electricity costs and understand how appliance usage affects estimated bills. This program provides a simple interactive way to explore a recent bill trend and estimate appliance energy costs.

## 3. Objectives
- Collect six months of bill amounts and units.
- Estimate the next bill from the recent bill trend.
- Calculate approximate monthly appliance costs.
- Estimate savings from reducing AC usage.
- Demonstrate Python input/output, lists, dictionaries, loops, functions, and a regression formula.

## 4. Tools
Python 3 and the Python standard library. No external packages are required.

## 5. Methodology
**Bill prediction:** Assign month numbers 1–6 to the bill amounts, calculate the least-squares slope and intercept, then evaluate the line at month 7.

**Appliance cost:** Monthly cost (₹) = power (kW) × daily hours × 30 days × rate (₹/kWh).

**Savings:** Calculate the estimated cost before and after reducing AC hours. Monthly savings are the difference; yearly savings are monthly savings multiplied by 12.

## 6. Algorithm
1. Read six bill amounts and six monthly unit values.
2. Read the electricity rate per unit.
3. Calculate the least-squares line for month indices and bill amounts.
4. Predict the bill for month 7.
5. Read appliance details and calculate estimated monthly costs.
6. Read AC power, current daily hours, and hours to reduce.
7. If reduction is valid, calculate monthly and yearly savings.
8. Display estimates and the disclaimer.

## 7. Testing
Test with six numeric bill values, six unit values, a positive unit rate, and at least one appliance. For the AC section, test a valid reduction from zero to current daily usage and an invalid reduction greater than current usage.

## 8. Limitations
- User data is entered manually; there is no included dataset.
- The unit values are collected but not used in the current forecast formula.
- Six months is a small sample, and a straight-line trend does not model seasonal effects.
- Tariff changes, fixed charges, taxes, and slab pricing are not included.
- Appliance costs and yearly savings are estimates and depend on the assumptions entered.

## 9. Future Improvements
- Use consumption units as part of the analysis.
- Add input validation and error handling.
- Save entries to a file and compare predictions with later actual bills.
- Add charts or a graphical interface.
- Evaluate forecast error on a larger historical dataset.
- Support tariff slabs and fixed charges.

## 10. Conclusion
The project demonstrates a basic regression calculation for bill forecasting and simple energy-cost calculations for appliances. It is an educational prototype, not a guaranteed utility-bill forecast.

## References
- Python documentation: https://docs.python.org/3/
- Least-squares linear regression concept.
