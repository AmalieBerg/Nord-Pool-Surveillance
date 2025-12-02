# Data Directory

## Overview

This directory should contain the Nord Pool day-ahead auction price data. Due to **data confidentiality**, the actual data files are **not included** in this public repository.

---

## Required Data File

### Filename Format
```
AuctionPrice_2025_DayAhead_[ZONES]_EUR_None.xlsx
```

### Example
```
AuctionPrice_2025_DayAhead_AT,BE,BG,DK1,DK2,EE,FI,FR,GER,LT,LV,NL,NO1,NO2,NO3,NO4,NO5,PL,SE1,SE2,SE3,SE4,TEL_EUR_None.xlsx
```

---

## Data Structure

### Expected Format

**Sheet:** First sheet (default)

**Columns:**
- `Delivery Start (CET)` - Timestamp for delivery period start
- `Delivery End (CET)` - Timestamp for delivery period end
- `AT`, `BE`, `BG`, etc. - Price columns for each bidding zone (EUR/MWh)

**Header Row:**
- Row 1: Contains "Price (EUR)" labels (skipped by scripts)
- Row 2+: Actual data

### Sample Structure
```
Delivery Start (CET) | Delivery End (CET)   | AT    | BE    | ... | LT     | LV     |
---------------------|----------------------|-------|-------|-----|--------|--------|
Price (EUR)          | Price (EUR)          | Price | Price | ... | Price  | Price  |
01.01.2025 00:00:00  | 01.01.2025 01:00:00  | 45.32 | 48.91 | ... | 52.10  | 52.10  |
01.01.2025 01:00:00  | 01.01.2025 02:00:00  | 42.15 | 45.33 | ... | 49.85  | 49.85  |
...
```

---

## Data Coverage

### Time Period
**January 1, 2025 - October 21, 2025**

**Total Records:** 8,567 hourly observations

### Geographic Coverage
**23 European Bidding Zones:**
- **Nordic:** NO1, NO2, NO3, NO4, NO5 (Norway); SE1, SE2, SE3, SE4 (Sweden); FI (Finland); DK1, DK2 (Denmark)
- **Baltic:** EE (Estonia), LT (Lithuania), LV (Latvia)
- **Central/Western Europe:** AT (Austria), BE (Belgium), BG (Bulgaria), FR (France), GER (Germany), NL (Netherlands), PL (Poland), TEL (Unknown)

### Focus Zones (This Analysis)
**13 Nordic & Baltic Zones:**
NO1, NO2, NO3, NO4, NO5, SE1, SE2, SE3, SE4, FI, EE, LT, LV

---

## Data Source

### Provider
**Nord Pool AS** (part of Euronext Group)
- Official market operator for Nordic/Baltic day-ahead electricity markets
- Website: https://www.nordpoolgroup.com/

### Market Type
**Day-Ahead Market (SDAC - Single Day-Ahead Coupling)**
- Auction closes daily at 12:00 CET
- Results typically published 12:55 CET
- Delivery next day (24 hourly products)

### Data Access
- **Public:** Aggregated market results available on Nord Pool website
- **Detailed:** Full order book data requires Nord Pool membership
- **This Project:** Uses publicly available price data for case study

---

## Data Quality Notes

### Known Issues
1. **Missing Values:** Rare, typically due to system issues
2. **Publication Delays:** Reflected in UMM publications
3. **15-Minute Products:** Starting Oct 1, 2025 (not in this dataset)
4. **Negative Prices:** Valid (oversupply situations)

### Data Validation
Scripts include:
- Datetime parsing with error handling
- Numeric conversion with `errors='coerce'`
- Missing value reporting
- Outlier detection (part of alert system)

---

## How to Obtain Data

### For Academic/Research Use

**Option 1: Nord Pool Data Portal**
- Register at: https://www.nordpoolgroup.com/en/market-data/
- Request historical data access
- Cite appropriate terms of use

**Option 2: ENTSO-E Transparency Platform**
- Free access: https://transparency.entsoe.eu/
- Provides day-ahead prices for European zones
- API available for programmatic access

**Option 3: Commercial Providers**
- Various energy data vendors
- Typically paid subscriptions
- May include additional market data

### For This Repository

If you want to run the scripts:
1. Obtain Nord Pool day-ahead price data (see options above)
2. Place Excel file in this `data/` directory
3. Ensure filename matches expected format
4. Run scripts - they will auto-detect the file

---

## Data Privacy & Confidentiality

### What's Included in This Repo
✅ Alert detection algorithms (public)  
✅ Visualization code (public)  
✅ Analysis methodology (public)  
✅ Generated alerts (aggregated, anonymized)  
✅ Visualizations (no sensitive data)  

### What's NOT Included
❌ Raw price data (confidential)  
❌ Order book details (confidential)  
❌ Participant identities (confidential)  
❌ Proprietary Nord Pool data (confidential)  

---

## Data Preprocessing

### Performed by Scripts

**1. Loading:**
```python
df = pd.read_excel(file_path)
df = df.iloc[1:]  # Skip header row
```

**2. Datetime Conversion:**
```python
df['Delivery Start (CET)'] = pd.to_datetime(
    df['Delivery Start (CET)'], 
    format='%d.%m.%Y %H:%M:%S'
)
```

**3. Numeric Conversion:**
```python
for col in price_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
```

**4. Period Selection:**
```python
# Baseline: Jan 1 - Oct 5, 2025
baseline_df = df[df['Delivery Start (CET)'] < '2025-10-06']

# Monitoring: Oct 6-12, 2025
monitoring_df = df[
    (df['Delivery Start (CET)'] >= '2025-10-06') &
    (df['Delivery Start (CET)'] <= '2025-10-12')
]
```

---

## Baseline Statistics (Reference)

### Nordic & Baltic Zones (Jan 1 - Oct 5, 2025)

| Zone | Mean (EUR) | Std Dev | Min (EUR) | Max (EUR) | Negative Hours |
|------|------------|---------|-----------|-----------|----------------|
| NO1  | 54.30      | 33.15   | -18.75    | 448.28    | 57             |
| NO2  | 62.24      | 33.35   | -10.60    | 493.32    | 57             |
| NO3  | 14.32      | 18.98   | -14.93    | 210.27    | 90             |
| NO4  | 4.68       | 9.92    | -26.40    | 202.93    | 234            |
| NO5  | 42.69      | 24.89   | -21.66    | 290.52    | 34             |
| SE1  | 12.38      | 23.16   | -94.59    | 275.19    | 493            |
| SE2  | 12.12      | 23.33   | -25.22    | 269.26    | 637            |
| SE3  | 43.50      | 41.99   | -25.05    | 393.38    | 356            |
| SE4  | 58.32      | 49.18   | -25.30    | 426.44    | 377            |
| FI   | 39.18      | 53.48   | -21.39    | 467.52    | 500            |
| EE   | 78.20      | 72.61   | -21.71    | 773.00    | 227            |
| LT   | 80.43      | 70.57   | -23.58    | 773.00    | 180            |
| LV   | 80.96      | 70.31   | -23.58    | 773.00    | 164            |

**Key Observations:**
- Northern zones (NO3, NO4, SE1, SE2) have low mean prices and frequent negative prices
- Baltic zones (EE, LT, LV) have higher mean prices and higher volatility
- Negative prices common in renewable-heavy zones (wind/hydro)
- Maximum prices in baseline period: 773 EUR/MWh (EE, LT, LV)

---

## Citation

If you use Nord Pool data in your work, please cite:

```
Nord Pool AS. (2025). Day-Ahead Market Prices, Nordic and Baltic Zones. 
Retrieved from https://www.nordpoolgroup.com/
```

---

## Questions?

For questions about:
- **Data access:** Contact Nord Pool directly
- **This repository:** See main README.md
- **Technical issues:** Open an issue on GitHub

---

## Disclaimer

This repository is for **educational and demonstration purposes** as part of a case study for a Market Surveillance Analyst position. While the analysis follows professional surveillance methodologies and uses realistic scenarios, specific market data access and usage must comply with Nord Pool's terms of service and applicable data protection regulations.
