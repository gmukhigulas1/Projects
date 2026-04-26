# Notebooks

This folder contains the working notebooks for the sentiment trading project. The notebooks are grouped into three roles:

- core pipeline notebooks: the main research flow from raw Reddit data to the final weighted sentiment and strategy analysis
- support notebooks: side notebooks used for visualization, testing, or model exploration
- case study notebooks: smaller end-to-end examples for individual assets or companies

## Recommended reading order

If you want to understand the main project from start to finish, read these notebooks first:

1. [01_pull_reddit_data.ipynb](./01_pull_reddit_data.ipynb)  
   Pulls or prepares the raw Reddit source data used in the project.

2. [02_extract_reddit_features.ipynb](./02_extract_reddit_features.ipynb)  
   Extracts post and comment features needed for downstream sentiment and weighting work.

3. [03_combine_tickers_and_sectors.ipynb](./03_combine_tickers_and_sectors.ipynb)  
   Maps Reddit discussion to tickers and sectors so the text data can be tied back to the index structure.

4. [04_assign_VADER_sentiment_scores.ipynb](./04_assign_VADER_sentiment_scores.ipynb)  
   Assigns sentiment scores to the processed Reddit content.

5. [05_weighting_visualize_strategy_results.ipynb](./05_weighting_visualize_strategy_results.ipynb)  
   The main analysis notebook. This is the clearest place to see how the project moves from weighted sentiment construction to sector interpolation, daily S&P sentiment, strategy development, testing, and visualization.

## Support notebooks

These notebooks are not part of the main reading path, but they are useful for inspection, testing, and side analysis:

- [00_utility_combine_reddit_data.ipynb](./00_utility_combine_reddit_data.ipynb)  
  Utility notebook for combining CSV files. Helpful for data assembly, but not central to the research narrative.

- [06_support_visual_sentiment_analysis.ipynb](./06_support_visual_sentiment_analysis.ipynb)  
  Additional sentiment visualizations and exploratory views.

- [08_support_test_sentiment_weighting.ipynb](./08_support_test_sentiment_weighting.ipynb)  
  Testing notebook for weighting ideas and intermediate checks.

- [09_support_sentiment_trading_model.ipynb](./09_support_sentiment_trading_model.ipynb)  
  Additional trading-model exploration outside the main notebook path.

## Case study notebooks

These notebooks apply the same general ideas in more focused case-study settings:

- [10_case_gitlab.ipynb](./10_case_gitlab.ipynb)  
  GitLab sentiment case study, including weighted sentiment construction and company-level visualization.

- [11_case_ethereum.ipynb](./11_case_ethereum.ipynb)  
  Ethereum case study, including daily sentiment construction, market alignment, and strategy testing.

## How to use this folder

- Start with `01` to `05` if you want the main research story.
- Use `06`, `08`, and `09` only if you want extra testing or exploratory context.
- Use `10` and `11` if you want compact examples of the framework applied to a single case.
- Treat `.bak` files as historical backups from notebook cleanup and restructuring work.

## Notes

- The numbering reflects project history as well as reading priority. A lower notebook number does not always mean it is more important than every later notebook.
- The core notebook for understanding the final methodology is [05_weighting_visualize_strategy_results.ipynb](./05_weighting_visualize_strategy_results.ipynb).
