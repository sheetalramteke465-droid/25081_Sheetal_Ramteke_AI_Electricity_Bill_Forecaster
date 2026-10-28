# AI Electricity Bill Forecaster

**Student:** Sheetal Ramteke  
**Roll No.:** 25081  
**Project type:** Python console-based AI/ML mini project

## Overview
This interactive Python program takes the user's last six monthly electricity bills and units, predicts the next bill using a manually calculated simple linear-regression line, estimates monthly appliance costs, and estimates savings from reducing daily AC usage.

## Features
- Collects six months of bill amounts and units.
- Forecasts month 7 from the trend in bill amounts.
- Estimates appliance costs using power, daily usage, 30 days, and the unit rate.
- Estimates monthly and yearly savings from reduced AC usage.

## Requirements
Python 3.8 or later. No third-party packages are required.

## Run
Open a terminal in this folder and run:
```bash
python main.py
```
Enter the requested values when prompted. The program can also be run in a Python IDE or an online compiler that supports interactive input.

## Prediction method
Month indices 1–6 are used as x values and the six bill amounts as y values. The program calculates the least-squares slope and intercept, then evaluates the line at month 7.

## Limitations
- Bills and units are entered manually; no dataset file is required.
- Units are collected but the current prediction formula uses bill amounts only.
- Six observations and a straight-line trend cannot capture seasonality or changing usage/tariffs.
- Appliance cost is a simplified estimate: kW × hours/day × 30 × rate per kWh.
- Fixed charges, taxes, slab tariffs, and subsidies are not included.
- Yearly savings assumes the same conditions for 12 months.
- Results are estimates, not guarantees.
