"""
Nord Pool Market Surveillance Alert System
VISUALIZATION MODULE 

Creates professional visualizations of prices and alerts for the monitoring week.

Author: Amalie Berg
Date: October 23, 2025
"""

# ============================================================================
# IMPORT LIBRARIES
# ============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle, Patch
import seaborn as sns
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

print("=" * 80)
print("NORD POOL MARKET SURVEILLANCE - VISUALIZATION MODULE")
print("=" * 80)
print("\n✓ Libraries imported successfully")

# ============================================================================
# LOAD DATA
# ============================================================================

print("\n" + "=" * 80)
print("LOADING DATA")
print("=" * 80)

# Try to find the auction price data file
print("\n🔍 Searching for auction price data...")

possible_paths = [
    # Current directory
    'AuctionPrice_2025_DayAhead_ATBEBGDK1DK2EEFIFRGERLTLVNLNO1NO2NO3NO4NO5PLSE1SE2SE3SE4TEL_EUR_None.xlsx',
    'data/AuctionPrice_2025_DayAhead_ATBEBGDK1DK2EEFIFRGERLTLVNLNO1NO2NO3NO4NO5PLSE1SE2SE3SE4TEL_EUR_None.xlsx',
    '../data/AuctionPrice_2025_DayAhead_ATBEBGDK1DK2EEFIFRGERLTLVNLNO1NO2NO3NO4NO5PLSE1SE2SE3SE4TEL_EUR_None.xlsx',
    # With commas in filename (actual Nord Pool format)
    'AuctionPrice_2025_DayAhead_AT,BE,BG,DK1,DK2,EE,FI,FR,GER,LT,LV,NL,NO1,NO2,NO3,NO4,NO5,PL,SE1,SE2,SE3,SE4,TEL_EUR_None.xlsx',
    'data/AuctionPrice_2025_DayAhead_AT,BE,BG,DK1,DK2,EE,FI,FR,GER,LT,LV,NL,NO1,NO2,NO3,NO4,NO5,PL,SE1,SE2,SE3,SE4,TEL_EUR_None.xlsx',
    '../data/AuctionPrice_2025_DayAhead_AT,BE,BG,DK1,DK2,EE,FI,FR,GER,LT,LV,NL,NO1,NO2,NO3,NO4,NO5,PL,SE1,SE2,SE3,SE4,TEL_EUR_None.xlsx',
    # Simplified name
    'AuctionPrice_2025_DayAhead.xlsx',
    'data/AuctionPrice_2025_DayAhead.xlsx',
    '../data/AuctionPrice_2025_DayAhead.xlsx',
    # Any xlsx in data folder
]

# Add any xlsx files found in data directory
if os.path.exists('data'):
    for file in os.listdir('data'):
        if file.endswith('.xlsx'):
            possible_paths.insert(0, os.path.join('data', file))
elif os.path.exists('../data'):
    for file in os.listdir('../data'):
        if file.endswith('.xlsx'):
            possible_paths.insert(0, os.path.join('../data', file))

file_path = None
for path in possible_paths:
    if os.path.exists(path):
        file_path = path
        print(f"✓ Found: {path}")
        break

# If not found, ask user
if file_path is None:
    print("\n⚠️  Excel file not found in standard locations.")
    print("Please enter the full path to the Excel file:")
    print("(You can drag and drop the file here, or copy/paste the path)")
    user_input = input("> ").strip()
    
    # Remove quotes that Windows/shells add
    file_path = user_input.strip('"').strip("'")
    
    if not os.path.exists(file_path):
        print(f"\n❌ Error: File not found at:")
        print(f"   {file_path}")
        print("\n💡 Tips:")
        print("   1. Drag and drop the Excel file into this window")
        print("   2. Make sure the file is in the 'data' folder")
        print("   3. Check the filename matches (commas are OK!)")
        import sys
        sys.exit(1)

print(f"\n📂 Loading auction data from: {file_path}")
df = pd.read_excel(file_path)
df = df.iloc[1:].copy()
df['Delivery Start (CET)'] = pd.to_datetime(df['Delivery Start (CET)'], format='%d.%m.%Y %H:%M:%S')

# Convert price columns
price_columns = ['AT', 'BE', 'BG', 'DK1', 'DK2', 'EE', 'FI', 'FR', 'GER', 'LT', 'LV', 'NL', 
                 'NO1', 'NO2', 'NO3', 'NO4', 'NO5', 'PL', 'SE1', 'SE2', 'SE3', 'SE4', 'TEL']
for col in price_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("✓ Auction data loaded")

# Load alerts
print("\n🔍 Searching for alerts CSV...")
alerts_path = None
possible_alert_paths = [
    'alerts_oct6-12.csv',
    'output/alerts_oct6-12.csv',
    '../output/alerts_oct6-12.csv',
    os.path.join(os.getcwd(), 'alerts_oct6-12.csv'),
    os.path.join(os.getcwd(), 'output', 'alerts_oct6-12.csv'),
]

# Check output directory
if os.path.exists('output'):
    for file in os.listdir('output'):
        if file.endswith('.csv') and 'alert' in file.lower():
            possible_alert_paths.insert(0, os.path.join('output', file))
elif os.path.exists('../output'):
    for file in os.listdir('../output'):
        if file.endswith('.csv') and 'alert' in file.lower():
            possible_alert_paths.insert(0, os.path.join('../output', file))

for path in possible_alert_paths:
    if os.path.exists(path):
        alerts_path = path
        print(f"✓ Found: {path}")
        break

if alerts_path is None:
    print("\n⚠️  Alerts CSV not found!")
    print("Please run 'python src/market_surveillance_alerts.py' first to generate alerts.")
    print("Or enter the path to alerts_oct6-12.csv:")
    user_input = input("> ").strip()
    alerts_path = user_input.strip('"').strip("'")
    
    if not os.path.exists(alerts_path):
        print(f"\n❌ Error: Alerts file not found at: {alerts_path}")
        import sys
        sys.exit(1)

print(f"\n📂 Loading alerts from: {alerts_path}")
alerts = pd.read_csv(alerts_path)
alerts['timestamp'] = pd.to_datetime(alerts['timestamp'])
print(f"✓ Alerts loaded: {len(alerts)} alerts")

# Define monitoring week
MONITORING_START = pd.Timestamp('2025-10-06 00:00:00')
MONITORING_END = pd.Timestamp('2025-10-12 23:59:59')

monitoring_df = df[(df['Delivery Start (CET)'] >= MONITORING_START) & 
                   (df['Delivery Start (CET)'] <= MONITORING_END)].copy()

NORDIC_BALTIC_ZONES = ['NO1', 'NO2', 'NO3', 'NO4', 'NO5', 
                       'SE1', 'SE2', 'SE3', 'SE4', 
                       'FI', 'EE', 'LT', 'LV']

print(f"\n✓ Monitoring week data prepared: {len(monitoring_df)} hours")

# ============================================================================
# VISUALIZATION 1: TIME SERIES WITH ALERTS - ALL ZONES
# ============================================================================

print("\n" + "=" * 80)
print("CREATING VISUALIZATION 1: Time Series with Alerts")
print("=" * 80)

fig, axes = plt.subplots(4, 1, figsize=(16, 16))
fig.suptitle('Nord Pool Day-Ahead Prices - Monitoring Week (Oct 6-12, 2025)\nNordic & Baltic Zones with Alert Markers', 
             fontsize=16, fontweight='bold', y=0.996)

# Group zones for plotting
zone_groups = [
    (['NO1', 'NO2', 'NO5'], 'Norway (NO1, NO2, NO5)', 0),
    (['NO3', 'NO4'], 'Norway Hydro-Rich (NO3, NO4)', 1),
    (['SE1', 'SE2', 'SE3', 'SE4'], 'Sweden (SE1-SE4)', 2),
    (['FI', 'EE', 'LT', 'LV'], 'Finland & Baltics (FI, EE, LT, LV)', 3),
]

for zones, title, idx in zone_groups:
    ax = axes[idx]
    
    # Plot price lines
    for zone in zones:
        ax.plot(monitoring_df['Delivery Start (CET)'], monitoring_df[zone], 
                label=zone, linewidth=1.5, alpha=0.8)
    
    # Add alert markers
    for zone in zones:
        zone_alerts = alerts[alerts['zone'] == zone]
        if len(zone_alerts) > 0:
            # Get prices at alert times
            alert_prices = []
            for ts in zone_alerts['timestamp']:
                price_row = monitoring_df[monitoring_df['Delivery Start (CET)'] == ts]
                if len(price_row) > 0:
                    alert_prices.append(price_row[zone].values[0])
                else:
                    alert_prices.append(np.nan)
            
            # Plot alerts
            critical_alerts = zone_alerts[zone_alerts['severity'] == 'CRITICAL']
            high_alerts = zone_alerts[zone_alerts['severity'] == 'HIGH']
            
            if len(critical_alerts) > 0:
                crit_prices = [alert_prices[i] for i, idx in enumerate(zone_alerts.index) 
                              if idx in critical_alerts.index]
                ax.scatter(critical_alerts['timestamp'], crit_prices, 
                          color='red', s=100, marker='X', zorder=5, 
                          edgecolors='darkred', linewidths=1.5,
                          label='CRITICAL Alert' if idx == 3 else '')
            
            if len(high_alerts) > 0:
                high_prices = [alert_prices[i] for i, idx in enumerate(zone_alerts.index) 
                              if idx in high_alerts.index]
                ax.scatter(high_alerts['timestamp'], high_prices, 
                          color='orange', s=50, marker='o', zorder=4,
                          alpha=0.6, edgecolors='darkorange',
                          label='HIGH Alert' if idx == 3 else '')
    
    # Formatting
    ax.set_ylabel('Price (EUR/MWh)', fontsize=11, fontweight='bold')
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    
    # Adjust legend placement based on subplot
    if idx == 3:  # Finland & Baltics - move legend to avoid overlap with high prices
        ax.legend(loc='upper right', fontsize=9, ncol=2, framealpha=0.95)
    else:
        ax.legend(loc='upper left', fontsize=9, ncol=3)
    
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
    
    # Format x-axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    
    # Highlight October 7
    oct7_start = pd.Timestamp('2025-10-07 00:00:00')
    oct7_end = pd.Timestamp('2025-10-07 23:59:59')
    ax.axvspan(oct7_start, oct7_end, alpha=0.1, color='red', label='Oct 7 (Critical Day)' if idx == 0 else '')

axes[-1].set_xlabel('Date (October 2025)', fontsize=11, fontweight='bold')
plt.tight_layout()

output_file_1 = 'visualization_1_timeseries_alerts.png'
plt.savefig(output_file_1, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_file_1}")
plt.close()

# ============================================================================
# VISUALIZATION 2: HEATMAP - PRICES ACROSS ZONES AND TIME
# ============================================================================

print("\n" + "=" * 80)
print("CREATING VISUALIZATION 2: Price Heatmap")
print("=" * 80)

# Prepare data for heatmap - hourly aggregation
monitoring_df['Date'] = monitoring_df['Delivery Start (CET)'].dt.date
monitoring_df['Hour'] = monitoring_df['Delivery Start (CET)'].dt.hour

# Create pivot table
heatmap_data = []
dates = sorted(monitoring_df['Date'].unique())

for zone in NORDIC_BALTIC_ZONES:
    zone_prices = []
    for date in dates:
        day_data = monitoring_df[monitoring_df['Date'] == date]
        # Average price per hour
        hourly_avg = day_data.groupby('Hour')[zone].mean()
        zone_prices.extend(hourly_avg.values)
    heatmap_data.append(zone_prices)

# Create figure
fig, ax = plt.subplots(figsize=(16, 8))

# Create heatmap
im = ax.imshow(heatmap_data, aspect='auto', cmap='RdYlGn_r', 
               interpolation='nearest', vmin=-50, vmax=400)

# Set ticks
ax.set_yticks(range(len(NORDIC_BALTIC_ZONES)))
ax.set_yticklabels(NORDIC_BALTIC_ZONES, fontsize=11)

# X-axis: dates
date_labels = [f"{d.strftime('%b %d')}" for d in dates]
ax.set_xticks([i * 24 + 12 for i in range(len(dates))])
ax.set_xticklabels(date_labels, fontsize=10)

# Add colorbar
cbar = plt.colorbar(im, ax=ax, pad=0.02)
cbar.set_label('Price (EUR/MWh)', rotation=270, labelpad=20, fontsize=11, fontweight='bold')

# Title and labels
ax.set_title('Day-Ahead Price Heatmap: Nordic & Baltic Zones (Oct 6-12, 2025)', 
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Date (Hourly Resolution)', fontsize=11, fontweight='bold')
ax.set_ylabel('Bidding Zone', fontsize=11, fontweight='bold')

# Add grid
for i in range(len(NORDIC_BALTIC_ZONES) + 1):
    ax.axhline(i - 0.5, color='white', linewidth=0.5)

# Highlight October 7
oct7_idx = list(dates).index(pd.Timestamp('2025-10-07').date())
ax.axvline(oct7_idx * 24 - 0.5, color='red', linewidth=3, linestyle='--', alpha=0.7)
ax.axvline((oct7_idx + 1) * 24 - 0.5, color='red', linewidth=3, linestyle='--', alpha=0.7)
ax.text(oct7_idx * 24 + 12, -1.5, 'CRITICAL DAY', ha='center', 
        fontsize=11, fontweight='bold', color='red')

plt.tight_layout()

output_file_2 = 'visualization_2_heatmap.png'
plt.savefig(output_file_2, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_file_2}")
plt.close()

# ============================================================================
# VISUALIZATION 3: OCTOBER 7 CRITICAL EVENT - DETAILED VIEW
# ============================================================================

print("\n" + "=" * 80)
print("CREATING VISUALIZATION 3: October 7 Critical Event Detail")
print("=" * 80)

# Filter for October 7
oct7_start = pd.Timestamp('2025-10-07 00:00:00')
oct7_end = pd.Timestamp('2025-10-07 23:59:59')
oct7_df = monitoring_df[(monitoring_df['Delivery Start (CET)'] >= oct7_start) & 
                        (monitoring_df['Delivery Start (CET)'] <= oct7_end)].copy()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))
fig.suptitle('October 7, 2025: Critical Price Event Analysis', 
             fontsize=16, fontweight='bold')

# Upper plot: Baltic states (extreme prices)
baltic_zones = ['LT', 'LV', 'EE']
for zone in baltic_zones:
    ax1.plot(oct7_df['Delivery Start (CET)'], oct7_df[zone], 
            label=zone, linewidth=2.5, marker='o', markersize=4)

# Mark critical hours
critical_hours = oct7_df[oct7_df['LT'] > 800]
ax1.scatter(critical_hours['Delivery Start (CET)'], critical_hours['LT'], 
           color='red', s=200, marker='X', zorder=5, edgecolors='darkred', 
           linewidths=2, label='CRITICAL (>800 EUR)')

ax1.axhline(y=500, color='orange', linestyle='--', linewidth=2, alpha=0.7, label='Extreme Threshold (500 EUR)')
ax1.set_ylabel('Price (EUR/MWh)', fontsize=12, fontweight='bold')
ax1.set_title('Baltic States: Extreme Price Levels', fontsize=13, fontweight='bold', pad=10)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_ylim(0, 1300)

# Add annotations for peak
max_idx = oct7_df['LT'].idxmax()
max_time = oct7_df.loc[max_idx, 'Delivery Start (CET)']
max_price = oct7_df.loc[max_idx, 'LT']
ax1.annotate(f'Peak: {max_price:.0f} EUR/MWh\n{max_time.strftime("%H:%M")}', 
            xy=(max_time, max_price), xytext=(max_time + pd.Timedelta(hours=4), max_price - 150),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=11, fontweight='bold', color='red',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))

# Lower plot: Nordic zones (negative/low prices showing contrast)
nordic_zones = ['NO3', 'NO4', 'SE1', 'SE2']
for zone in nordic_zones:
    ax2.plot(oct7_df['Delivery Start (CET)'], oct7_df[zone], 
            label=zone, linewidth=2.5, marker='o', markersize=4)

ax2.axhline(y=0, color='black', linestyle='-', linewidth=1.5, alpha=0.7)
ax2.set_ylabel('Price (EUR/MWh)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Time (CET)', fontsize=12, fontweight='bold')
ax2.set_title('Northern Zones: Low/Negative Prices (Oversupply)', fontsize=13, fontweight='bold', pad=10)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, alpha=0.3)

# Format x-axis
for ax in [ax1, ax2]:
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=2))
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, ha='center')

# Highlight morning crisis (06:00-09:00)
morning_start = pd.Timestamp('2025-10-07 06:00:00')
morning_end = pd.Timestamp('2025-10-07 09:00:00')
for ax in [ax1, ax2]:
    ax.axvspan(morning_start, morning_end, alpha=0.15, color='red', label='Morning Crisis')
    
# Highlight evening crisis (17:00-21:00)
evening_start = pd.Timestamp('2025-10-07 17:00:00')
evening_end = pd.Timestamp('2025-10-07 21:00:00')
for ax in [ax1, ax2]:
    ax.axvspan(evening_start, evening_end, alpha=0.15, color='orange', label='Evening Crisis')

plt.tight_layout()

output_file_3 = 'visualization_3_oct7_detail.png'
plt.savefig(output_file_3, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_file_3}")
plt.close()

# ============================================================================
# VISUALIZATION 4: ALERT DASHBOARD
# ============================================================================

print("\n" + "=" * 80)
print("CREATING VISUALIZATION 4: Alert Dashboard")
print("=" * 80)

fig = plt.figure(figsize=(18, 11))
gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)

fig.suptitle('Market Surveillance Alert Dashboard - Monitoring Week (Oct 6-12, 2025)', 
             fontsize=16, fontweight='bold')

# 1. Alerts by Type (Pie Chart)
ax1 = fig.add_subplot(gs[0, 0])
alert_counts = alerts['alert_type'].value_counts()
colors_pie = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#ffa07a', '#98d8c8']

# Slightly explode slices to create space
explode = (0.08, 0.08, 0.08, 0.08, 0.08)

# Create pie chart with connection lines
wedges, texts, autotexts = ax1.pie(alert_counts.values, 
                                     labels=alert_counts.index,
                                     autopct='%1.1f%%',
                                     startangle=45,  # Changed start angle to spread labels better
                                     colors=colors_pie,
                                     explode=explode,
                                     pctdistance=0.7,
                                     labeldistance=1.25,
                                     wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
                                     textprops={'fontsize': 9, 'fontweight': 'bold'})

# Style the percentage text (black with white background as requested)
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(9)
    autotext.set_bbox(dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='gray', linewidth=0.5))

ax1.set_title('Alerts by Type', fontweight='bold', fontsize=11, pad=10)

# 2. Alerts by Severity (Bar Chart)
ax2 = fig.add_subplot(gs[0, 1])
severity_counts = alerts['severity'].value_counts()
severity_order = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']
severity_counts = severity_counts.reindex(severity_order)
colors_severity = ['#d32f2f', '#f57c00', '#fbc02d', '#7cb342']
bars = ax2.bar(severity_order, severity_counts.values, color=colors_severity, edgecolor='black')
ax2.set_title('Alerts by Severity', fontweight='bold', fontsize=11)
ax2.set_ylabel('Number of Alerts', fontweight='bold')
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}', ha='center', va='bottom', fontweight='bold')

# 3. Top 10 Zones by Alert Count
ax3 = fig.add_subplot(gs[0, 2])
zone_counts = alerts['zone'].value_counts().head(10)
ax3.barh(range(len(zone_counts)), zone_counts.values, color='steelblue', edgecolor='black')
ax3.set_yticks(range(len(zone_counts)))
ax3.set_yticklabels(zone_counts.index)
ax3.set_xlabel('Number of Alerts', fontweight='bold')
ax3.set_title('Top 10 Zones by Alert Count', fontweight='bold', fontsize=11)
ax3.invert_yaxis()
for i, v in enumerate(zone_counts.values):
    ax3.text(v + 3, i, str(v), va='center', fontweight='bold')

# 4. Alerts Timeline (Large plot)
ax4 = fig.add_subplot(gs[1, :])
alerts['date'] = alerts['timestamp'].dt.date
daily_alerts = alerts.groupby('date').size()
dates_range = pd.date_range(start='2025-10-06', end='2025-10-12', freq='D')
daily_counts = [daily_alerts.get(d.date(), 0) for d in dates_range]

bars = ax4.bar(dates_range, daily_counts, color='coral', edgecolor='black', alpha=0.8)
ax4.set_xlabel('Date', fontweight='bold', fontsize=11)
ax4.set_ylabel('Number of Alerts', fontweight='bold', fontsize=11)
ax4.set_title('Daily Alert Count', fontweight='bold', fontsize=12)
ax4.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Highlight October 7
oct7_bar_idx = 1  # Oct 7 is second bar
bars[oct7_bar_idx].set_color('darkred')
bars[oct7_bar_idx].set_alpha(1.0)

for i, bar in enumerate(bars):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=10)

# 5. Price Distribution (Box Plot)
ax5 = fig.add_subplot(gs[2, :2])
price_data = [monitoring_df[zone].dropna() for zone in ['NO4', 'SE1', 'SE3', 'FI', 'EE', 'LT', 'LV']]
bp = ax5.boxplot(price_data, labels=['NO4', 'SE1', 'SE3', 'FI', 'EE', 'LT', 'LV'],
                 patch_artist=True, showfliers=True)
for patch, color in zip(bp['boxes'], ['lightblue']*3 + ['lightcoral']*4):
    patch.set_facecolor(color)
ax5.set_ylabel('Price (EUR/MWh)', fontweight='bold')
ax5.set_title('Price Distribution by Zone (Monitoring Week)', fontweight='bold', fontsize=12)
ax5.axhline(y=0, color='black', linestyle='--', linewidth=1)
ax5.grid(axis='y', alpha=0.3)

# 6. Summary Statistics (Text)
ax6 = fig.add_subplot(gs[2, 2])
ax6.axis('off')

summary_text = f"""
SUMMARY STATISTICS

Total Alerts: {len(alerts)}

By Severity:
 • CRITICAL: {len(alerts[alerts['severity']=='CRITICAL'])}
 • HIGH: {len(alerts[alerts['severity']=='HIGH'])}
 • MEDIUM: {len(alerts[alerts['severity']=='MEDIUM'])}
 • LOW: {len(alerts[alerts['severity']=='LOW'])}

Critical Event:
 • Date: Oct 7, 2025
 • Peak: 1,173.65 EUR/MWh
 • Zone: LT/LV
 • Time: 07:00 CET

Key Pattern:
 • North: Negative prices
 • South: Extreme prices
 • Indication: Severe
   transmission
   congestion
"""

ax6.text(0.05, 0.98, summary_text, transform=ax6.transAxes,
        fontsize=9.5, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))

plt.tight_layout()

output_file_4 = 'visualization_4_dashboard.png'
plt.savefig(output_file_4, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {output_file_4}")
plt.close()

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("VISUALIZATION COMPLETE")
print("=" * 80)
print("\n📊 Generated 4 visualizations:")
print(f"  1. {output_file_1} - Time series with alerts (all zones)")
print(f"  2. {output_file_2} - Price heatmap")
print(f"  3. {output_file_3} - October 7 critical event detail")
print(f"  4. {output_file_4} - Alert dashboard")
print("\n✓ All visualizations saved successfully!")
print("\n" + "=" * 80)