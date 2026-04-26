# Notebooks

This folder contains exploratory Jupyter notebooks for market analysis, price-structure research, and portfolio-optimization experiments.

The notebooks here are smaller and more experimental than the sentiment-trading project. They are best understood as a set of practice and research workbooks rather than one single production pipeline.

## Recommended reading order

If you want the clearest path through the folder, read the notebooks in this order:

1. [01_market_data_exploration_basics.ipynb](./01_market_data_exploration_basics.ipynb)  
   Introductory market-data exploration, including downloads, CSV handling, multi-index columns, and simple return calculations.

2. [02_market_screening_and_stock_analysis.ipynb](./02_market_screening_and_stock_analysis.ipynb)  
   Broader stock screening and comparison notebook with return summaries, correlation work, and single-name checks.

3. [03_price_structure_hh_ll_hl_lh.ipynb](./03_price_structure_hh_ll_hl_lh.ipynb)  
   Price-structure notebook focused on higher highs, higher lows, lower highs, and lower lows.

4. [04_markowitz_bootstrapping.ipynb](./04_markowitz_bootstrapping.ipynb)  
   Main portfolio-optimization notebook using a Markowitz-style allocation process with bootstrapped return splits.

## Supporting portfolio notebooks

These notebooks are useful supporting experiments for the optimization work:

- [05_portfolio_optimization_synthetic_demo.ipynb](./05_portfolio_optimization_synthetic_demo.ipynb)  
  Synthetic-data prototype for random portfolios and efficient-frontier intuition.

- [06_portfolio_optimization_equity_demo.ipynb](./06_portfolio_optimization_equity_demo.ipynb)  
  Real-equity continuation of the optimization prototype.

## How to use this folder

- Start with `01` and `02` if you want the broadest market-analysis context.
- Read `03` if you are specifically interested in price-structure logic and swing-pattern detection.
- Read `04` to see the most complete portfolio-optimization workflow in this folder.
- Use `05` and `06` as supporting experiments rather than core notebooks.

## Notes

- These notebooks were developed experimentally, so some are more polished than others.
- The numbering in this folder is a readability aid added after the notebooks were created.
- The scripts in `../scripts` support some of the ideas explored here, but the notebooks remain the main reading surface for this folder.
