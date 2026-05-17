# Georgian Equities Factor Attribution Dashboard

This project studies Georgian-linked equities listed on the London Stock Exchange: Lion Finance Group, formerly Bank of Georgia, ticker BGEO.L; TBC Bank, ticker TBCG.L; and Georgia Capital, ticker CGEO.L.

The analysis builds a common Georgian equity factor using PCA and studies what drives its movement across global equities, US Treasury rates, regional markets, local currency, commodities, crypto, credit instruments, and trading volumes.

The project is organized around two notebooks:

- `data_cleaning.ipynb` prepares the raw market data. It cleans and aligns prices, FX rates, bond yields, ICE indices, interest rates, volumes, commodities, crypto assets, and benchmark yields into consistent time series.
- `Analytics.ipynb` builds the factor model and dashboard outputs. It creates the Georgian equity factor, runs PCA blocks, estimates Lasso same-day attribution, checks Ridge next-day prediction, applies CUSUM event filtering, and exports the final CSV and JSON files used in the dashboard.

The dashboard combines factor attribution, same-day diagnostics, next-day prediction checks, CUSUM event filtering, and stress simulation. The main conclusion is that same-day factor attribution is meaningful, while next-day prediction remains weak.

Live dashboard:

[Georgian Equities Dashboard](https://georgian-equities-dashboard-gmukhigulas1s-projects.vercel.app/)