# Sentiment Trading Strategy

This is my largest research project in the repository. It is connected to my bachelor’s thesis, **“The Rise of Reddit in Investment Decisions: A Sentiment-Based Trading Perspective.”**

The project started from a simple question: Reddit clearly became important in retail-investor culture, but can that discussion actually be measured in a useful way? More specifically, can sentiment, engagement, and discussion intensity tell us anything about stock returns?

## What I tried to do

The project uses Reddit discussion data and market data to build sentiment-based indicators. I then tested whether those indicators could be used in a simple trading-strategy framework.

The workflow is roughly:

1. collect Reddit posts/comments;
2. clean and combine the data;
3. connect discussion data to tickers;
4. create sentiment and engagement-weighted signals;
5. compare the signals with market returns;
6. test simple strategy rules;
7. visualize annual, cumulative, and adjusted returns.

## Folder structure

```text
Sentiment Trading Strategy/
├── data/
├── notebooks/
├── outputs/
└── README.md
- `Realistic_Returns.png`
- `Chart3_Cumulative_Returns.png`
- `Annual_Performance_Analysis.png`
