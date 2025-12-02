"""
Nord Pool Market Surveillance Alert System
Case Study - Task 2

Monitoring Week: October 6-12, 2025
Focus: Nordic & Baltic bidding zones

Author: Amalie
Date: October 23, 2025
"""

# ============================================================================
# IMPORT LIBRARIES
# ============================================================================

# Data manipulation and analysis
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Visualization
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
import seaborn as sns

# Statistical analysis
from scipy import stats

# Suppress warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("=" * 80)
print("NORD POOL MARKET SURVEILLANCE - ALERT SYSTEM")
print("=" * 80)
print("\n✓ Libraries imported successfully")

# ============================================================================
# LOAD AND CLEAN DATA
# ============================================================================

print("\n" + "=" * 80)
print("STEP 1: DATA LOADING AND PREPARATION")
print("=" * 80)

# Load data - FLEXIBLE FILE PATH
# Option 1: Put the Excel file in the same directory as this script
# Option 2: Specify the full path below

import os
import sys

# Try to find the Excel file in common locations
possible_paths = [
    # Same directory as script
    'AuctionPrice_2025_DayAhead_ATBEBGDK1DK2EEFIFRGERLTLVNLNO1NO2NO3NO4NO5PLSE1SE2SE3SE4TEL_EUR_None.xlsx',
    # Current working directory
    os.path.join(os.getcwd(), 'AuctionPrice_2025_DayAhead_ATBEBGDK1DK2EEFIFRGERLTLVNLNO1NO2NO3NO4NO5PLSE1SE2SE3SE4TEL_EUR_None.xlsx'),
    # Linux path (for testing environment)
    '/mnt/project/AuctionPrice_2025_DayAhead_ATBEBGDK1DK2EEFIFRGERLTLVNLNO1NO2NO3NO4NO5PLSE1SE2SE3SE4TEL_EUR_None.xlsx',
]

# Try to find the file
file_path = None
for path in possible_paths:
    if os.path.exists(path):
        file_path = path
        break

# If not found, ask user to specify
if file_path is None:
    print("\n⚠️  Excel file not found in standard locations.")
    print("Please enter the full path to the Excel file:")
    print("(You can drag and drop the file here, or copy/paste the path)")
    user_input = input("> ").strip()
    
    # Remove quotes that Windows/shells add for paths with special characters
    file_path = user_input.strip('"').strip("'")
    
    if not os.path.exists(file_path):
        print(f"\n❌ Error: File not found at:")
        print(f"   {file_path}")
        print("\n💡 Troubleshooting tips:")
        print("   1. Drag and drop the Excel file into this window")
        print("   2. Make sure the file is in the 'data' folder")
        print("   3. The filename contains commas - that's normal!")
        print(f"\n📁 Script is looking in: {os.path.dirname(os.path.abspath(__file__))}/../data/")
        sys.exit(1)

print(f"\n📂 Loading data from: {file_path}")

df = pd.read_excel(file_path)
print(f"✓ Raw data loaded: {df.shape[0]} rows × {df.shape[1]} columns")

# Skip header row containing "Price (EUR)"
df = df.iloc[1:].copy()
print(f"✓ Header row removed: {df.shape[0]} rows remaining")

# Convert datetime columns
df['Delivery Start (CET)'] = pd.to_datetime(df['Delivery Start (CET)'], 
                                             format='%d.%m.%Y %H:%M:%S')
df['Delivery End (CET)'] = pd.to_datetime(df['Delivery End (CET)'], 
                                           format='%d.%m.%Y %H:%M:%S')
print("✓ Datetime columns converted")

# Define all bidding zones
all_zones = ['AT', 'BE', 'BG', 'DK1', 'DK2', 'EE', 'FI', 'FR', 'GER', 'LT', 'LV', 
             'NL', 'NO1', 'NO2', 'NO3', 'NO4', 'NO5', 'PL', 'SE1', 'SE2', 'SE3', 
             'SE4', 'TEL']

# Convert price columns to numeric
for col in all_zones:
    df[col] = pd.to_numeric(df[col], errors='coerce')
print(f"✓ {len(all_zones)} price columns converted to numeric")

# Define Nordic and Baltic zones (our focus)
NORDIC_BALTIC_ZONES = ['NO1', 'NO2', 'NO3', 'NO4', 'NO5', 
                       'SE1', 'SE2', 'SE3', 'SE4', 
                       'FI', 'EE', 'LT', 'LV']

print(f"\n📍 Focus zones (Nordic & Baltic): {len(NORDIC_BALTIC_ZONES)} zones")
print(f"   {', '.join(NORDIC_BALTIC_ZONES)}")

# Date range
print(f"\n📅 Data coverage:")
print(f"   Start: {df['Delivery Start (CET)'].min()}")
print(f"   End:   {df['Delivery Start (CET)'].max()}")
print(f"   Days:  {(df['Delivery Start (CET)'].max() - df['Delivery Start (CET)'].min()).days + 1}")

# ============================================================================
# DEFINE TIME PERIODS
# ============================================================================

print("\n" + "=" * 80)
print("STEP 2: DEFINE BASELINE AND MONITORING PERIODS")
print("=" * 80)

# Monitoring week: October 6-12, 2025
MONITORING_START = pd.Timestamp('2025-10-06 00:00:00')
MONITORING_END = pd.Timestamp('2025-10-12 23:59:59')

# Baseline: January 1 - October 5, 2025
BASELINE_START = pd.Timestamp('2025-01-01 00:00:00')
BASELINE_END = pd.Timestamp('2025-10-05 23:59:59')

print(f"\n📊 Baseline period (for statistical comparison):")
print(f"   {BASELINE_START.date()} to {BASELINE_END.date()}")

baseline_df = df[(df['Delivery Start (CET)'] >= BASELINE_START) & 
                 (df['Delivery Start (CET)'] <= BASELINE_END)].copy()
print(f"   Hours: {len(baseline_df)}")

print(f"\n🔍 Monitoring week:")
print(f"   {MONITORING_START.date()} to {MONITORING_END.date()}")

monitoring_df = df[(df['Delivery Start (CET)'] >= MONITORING_START) & 
                   (df['Delivery Start (CET)'] <= MONITORING_END)].copy()
print(f"   Hours: {len(monitoring_df)}")

print("\n✓ Data preparation complete!")

# ============================================================================
# CALCULATE BASELINE STATISTICS
# ============================================================================

print("\n" + "=" * 80)
print("STEP 3: CALCULATE BASELINE STATISTICS PER ZONE")
print("=" * 80)

# Calculate mean, std dev, min, max for each zone in baseline period
baseline_stats = {}

for zone in NORDIC_BALTIC_ZONES:
    zone_data = baseline_df[zone].dropna()
    baseline_stats[zone] = {
        'mean': zone_data.mean(),
        'std': zone_data.std(),
        'min': zone_data.min(),
        'max': zone_data.max(),
        'median': zone_data.median(),
        'q25': zone_data.quantile(0.25),
        'q75': zone_data.quantile(0.75)
    }

# Display baseline statistics
print("\n📈 Baseline Statistics (Jan 1 - Oct 5, 2025):\n")
print(f"{'Zone':<6} {'Mean':>8} {'Std':>8} {'Min':>8} {'Max':>8} {'Median':>8}")
print("-" * 54)
for zone in NORDIC_BALTIC_ZONES:
    stats = baseline_stats[zone]
    print(f"{zone:<6} {stats['mean']:>8.2f} {stats['std']:>8.2f} "
          f"{stats['min']:>8.2f} {stats['max']:>8.2f} {stats['median']:>8.2f}")

print("\n✓ Baseline statistics calculated")

# ============================================================================
# ALERT DETECTION FUNCTIONS
# ============================================================================

print("\n" + "=" * 80)
print("STEP 4: DEFINE ALERT DETECTION FUNCTIONS")
print("=" * 80)

def detect_statistical_outliers(df, baseline_stats, zones, threshold_sigma=3):
    """
    Alert Type 1: Statistical Outliers (Z-score method)
    
    Flags prices that deviate significantly from baseline mean.
    
    Parameters:
    - df: DataFrame with monitoring week data
    - baseline_stats: Dictionary with baseline statistics per zone
    - zones: List of zones to check
    - threshold_sigma: Number of standard deviations for threshold (default: 3)
    
    Returns:
    - DataFrame with alerts
    """
    alerts = []
    
    for zone in zones:
        mean = baseline_stats[zone]['mean']
        std = baseline_stats[zone]['std']
        
        # Define outlier thresholds
        upper_threshold = mean + threshold_sigma * std
        lower_threshold = mean - threshold_sigma * std
        
        # Find outliers
        outliers = df[
            (df[zone] > upper_threshold) | 
            (df[zone] < lower_threshold)
        ].copy()
        
        for idx, row in outliers.iterrows():
            price = row[zone]
            z_score = (price - mean) / std if std > 0 else 0
            
            alerts.append({
                'timestamp': row['Delivery Start (CET)'],
                'zone': zone,
                'alert_type': 'Statistical Outlier',
                'price': price,
                'baseline_mean': mean,
                'baseline_std': std,
                'z_score': z_score,
                'deviation': price - mean,
                'severity': 'HIGH' if abs(z_score) > 4 else 'MEDIUM'
            })
    
    return pd.DataFrame(alerts)


def detect_negative_prices(df, zones):
    """
    Alert Type 2: Negative Prices
    
    Flags all instances of negative prices.
    
    Parameters:
    - df: DataFrame with monitoring week data
    - zones: List of zones to check
    
    Returns:
    - DataFrame with alerts
    """
    alerts = []
    
    for zone in zones:
        negative = df[df[zone] < 0].copy()
        
        for idx, row in negative.iterrows():
            alerts.append({
                'timestamp': row['Delivery Start (CET)'],
                'zone': zone,
                'alert_type': 'Negative Price',
                'price': row[zone],
                'baseline_mean': None,
                'baseline_std': None,
                'z_score': None,
                'deviation': None,
                'severity': 'LOW' if row[zone] > -5 else 'MEDIUM'
            })
    
    return pd.DataFrame(alerts)


def detect_extreme_absolute_prices(df, zones, high_threshold=500):
    """
    Alert Type 3: Extreme Absolute Prices
    
    Flags prices above a certain absolute threshold (e.g., 500 EUR/MWh).
    
    Parameters:
    - df: DataFrame with monitoring week data
    - zones: List of zones to check
    - high_threshold: Absolute price threshold in EUR/MWh
    
    Returns:
    - DataFrame with alerts
    """
    alerts = []
    
    for zone in zones:
        extreme = df[df[zone] > high_threshold].copy()
        
        for idx, row in extreme.iterrows():
            price = row[zone]
            alerts.append({
                'timestamp': row['Delivery Start (CET)'],
                'zone': zone,
                'alert_type': 'Extreme Absolute Price',
                'price': price,
                'baseline_mean': None,
                'baseline_std': None,
                'z_score': None,
                'deviation': None,
                'severity': 'CRITICAL' if price > 800 else 'HIGH'
            })
    
    return pd.DataFrame(alerts)


def detect_cross_border_spread_anomalies(df, baseline_df, zone_pairs):
    """
    Alert Type 4: Cross-Border Spread Anomalies
    
    Flags unusual price spreads between interconnected zones.
    
    Parameters:
    - df: DataFrame with monitoring week data
    - baseline_df: DataFrame with baseline period data
    - zone_pairs: List of tuples with (zone1, zone2) pairs
    
    Returns:
    - DataFrame with alerts
    """
    alerts = []
    
    for zone1, zone2 in zone_pairs:
        # Calculate historical spread
        baseline_spread = (baseline_df[zone1] - baseline_df[zone2]).dropna()
        spread_mean = baseline_spread.mean()
        spread_std = baseline_spread.std()
        
        # Calculate monitoring week spread
        monitoring_spread = df[zone1] - df[zone2]
        
        # Find anomalies (spread > mean + 2*std or < mean - 2*std)
        upper_threshold = spread_mean + 2 * spread_std
        lower_threshold = spread_mean - 2 * spread_std
        
        anomalies = df[
            (monitoring_spread > upper_threshold) | 
            (monitoring_spread < lower_threshold)
        ].copy()
        
        for idx, row in anomalies.iterrows():
            spread = row[zone1] - row[zone2]
            z_score = (spread - spread_mean) / spread_std if spread_std > 0 else 0
            
            alerts.append({
                'timestamp': row['Delivery Start (CET)'],
                'zone': f"{zone1}-{zone2}",
                'alert_type': 'Spread Anomaly',
                'price': spread,
                'baseline_mean': spread_mean,
                'baseline_std': spread_std,
                'z_score': z_score,
                'deviation': spread - spread_mean,
                'severity': 'HIGH' if abs(z_score) > 3 else 'MEDIUM'
            })
    
    return pd.DataFrame(alerts)


def detect_price_pattern_breaks(df, zones):
    """
    Alert Type 5: Inverted Hourly Pattern
    
    Flags days where peak hours (08:00-20:00) have lower average price 
    than off-peak hours.
    
    Parameters:
    - df: DataFrame with monitoring week data
    - zones: List of zones to check
    
    Returns:
    - DataFrame with alerts
    """
    alerts = []
    
    df_copy = df.copy()
    df_copy['date'] = df_copy['Delivery Start (CET)'].dt.date
    df_copy['hour'] = df_copy['Delivery Start (CET)'].dt.hour
    
    for zone in zones:
        for date in df_copy['date'].unique():
            day_data = df_copy[df_copy['date'] == date]
            
            peak_hours = day_data[day_data['hour'].between(8, 19)]
            off_peak_hours = day_data[~day_data['hour'].between(8, 19)]
            
            if len(peak_hours) > 0 and len(off_peak_hours) > 0:
                peak_avg = peak_hours[zone].mean()
                off_peak_avg = off_peak_hours[zone].mean()
                
                # Alert if peak is cheaper than off-peak by more than 10 EUR/MWh
                if peak_avg < off_peak_avg - 10:
                    alerts.append({
                        'timestamp': pd.Timestamp(date),
                        'zone': zone,
                        'alert_type': 'Inverted Pattern',
                        'price': peak_avg - off_peak_avg,
                        'baseline_mean': None,
                        'baseline_std': None,
                        'z_score': None,
                        'deviation': None,
                        'severity': 'MEDIUM'
                    })
    
    return pd.DataFrame(alerts)


print("\n✓ Alert detection functions defined:")
print("   1. Statistical Outliers (Z-score method)")
print("   2. Negative Prices")
print("   3. Extreme Absolute Prices (>500 EUR/MWh)")
print("   4. Cross-Border Spread Anomalies")
print("   5. Inverted Hourly Patterns")

# ============================================================================
# EXECUTE ALERT DETECTION
# ============================================================================

print("\n" + "=" * 80)
print("STEP 5: RUN ALERT DETECTION ON MONITORING WEEK")
print("=" * 80)

# Alert 1: Statistical Outliers
print("\n🔍 Running Alert 1: Statistical Outliers...")
alerts_outliers = detect_statistical_outliers(
    monitoring_df, 
    baseline_stats, 
    NORDIC_BALTIC_ZONES,
    threshold_sigma=3
)
print(f"   Found {len(alerts_outliers)} outlier alerts")

# Alert 2: Negative Prices
print("\n🔍 Running Alert 2: Negative Prices...")
alerts_negative = detect_negative_prices(monitoring_df, NORDIC_BALTIC_ZONES)
print(f"   Found {len(alerts_negative)} negative price alerts")

# Alert 3: Extreme Absolute Prices
print("\n🔍 Running Alert 3: Extreme Absolute Prices (>500 EUR/MWh)...")
alerts_extreme = detect_extreme_absolute_prices(
    monitoring_df, 
    NORDIC_BALTIC_ZONES,
    high_threshold=500
)
print(f"   Found {len(alerts_extreme)} extreme price alerts")

# Alert 4: Cross-Border Spread Anomalies
print("\n🔍 Running Alert 4: Cross-Border Spread Anomalies...")

# Define interconnected zone pairs (based on Nordic grid topology)
ZONE_PAIRS = [
    ('NO1', 'NO2'),    # Northern Norway connection
    ('NO2', 'NO5'),    # Mid-Norway connection
    ('NO1', 'SE3'),    # Norway-Sweden border
    ('NO2', 'SE3'),    # Another NO-SE connection
    ('NO4', 'SE2'),    # Northern connection
    ('SE1', 'SE2'),    # Within Sweden
    ('SE2', 'SE3'),    # Within Sweden
    ('SE3', 'SE4'),    # Within Sweden
    ('SE1', 'FI'),     # Sweden-Finland
    ('FI', 'EE'),      # Finland-Estonia
    ('EE', 'LT'),      # Estonia-Lithuania
    ('EE', 'LV'),      # Estonia-Latvia
    ('LT', 'LV'),      # Lithuania-Latvia (should be similar/same)
]

alerts_spreads = detect_cross_border_spread_anomalies(
    monitoring_df,
    baseline_df,
    ZONE_PAIRS
)
print(f"   Found {len(alerts_spreads)} spread anomaly alerts")

# Alert 5: Inverted Patterns
print("\n🔍 Running Alert 5: Inverted Hourly Patterns...")
alerts_patterns = detect_price_pattern_breaks(monitoring_df, NORDIC_BALTIC_ZONES)
print(f"   Found {len(alerts_patterns)} inverted pattern alerts")

# ============================================================================
# CONSOLIDATE ALL ALERTS
# ============================================================================

print("\n" + "=" * 80)
print("STEP 6: CONSOLIDATE AND ANALYZE ALERTS")
print("=" * 80)

# Combine all alerts
all_alerts = pd.concat([
    alerts_outliers,
    alerts_negative,
    alerts_extreme,
    alerts_spreads,
    alerts_patterns
], ignore_index=True)

print(f"\n📊 TOTAL ALERTS GENERATED: {len(all_alerts)}")

# Summary by alert type
print("\n📋 Breakdown by Alert Type:")
print(all_alerts['alert_type'].value_counts().to_string())

# Summary by zone
print("\n📋 Breakdown by Zone:")
zone_counts = all_alerts['zone'].value_counts()
print(zone_counts.head(15).to_string())

# Summary by severity
print("\n📋 Breakdown by Severity:")
print(all_alerts['severity'].value_counts().to_string())

# Top 10 most severe alerts
print("\n" + "=" * 80)
print("TOP 10 CRITICAL ALERTS")
print("=" * 80)

# Sort by severity (CRITICAL > HIGH > MEDIUM > LOW) and price
severity_order = {'CRITICAL': 4, 'HIGH': 3, 'MEDIUM': 2, 'LOW': 1}
all_alerts['severity_rank'] = all_alerts['severity'].map(severity_order)
top_alerts = all_alerts.nlargest(10, ['severity_rank', 'price'])

print(f"\n{'Timestamp':<20} {'Zone':<8} {'Alert Type':<25} {'Price':>10} {'Severity':<10}")
print("-" * 90)
for idx, alert in top_alerts.iterrows():
    ts = alert['timestamp'].strftime('%Y-%m-%d %H:%M') if pd.notna(alert['timestamp']) else 'N/A'
    print(f"{ts:<20} {alert['zone']:<8} {alert['alert_type']:<25} "
          f"{alert['price']:>10.2f} {alert['severity']:<10}")

# Save alerts to CSV for further analysis
output_dir = os.path.dirname(file_path) if os.path.dirname(file_path) else os.getcwd()
output_file = os.path.join(output_dir, 'alerts_oct6-12.csv')
all_alerts.to_csv(output_file, index=False)
print(f"\n💾 All alerts saved to: {output_file}")

print("\n" + "=" * 80)
print("ALERT DETECTION COMPLETE")
print("=" * 80)