# QUICK START GUIDE - Windows Users
## Nord Pool Market Surveillance Alert System

---

## 🚀 Step-by-Step Setup (Windows)

### Step 1: Install Python (if not already installed)
1. Download Python from: https://www.python.org/downloads/
2. During installation, **CHECK** "Add Python to PATH"
3. Verify installation:
   - Open Command Prompt (Win + R, type `cmd`, press Enter)
   - Type: `python --version`
   - Should show: Python 3.x.x

### Step 2: Install Required Packages
Open Command Prompt and run ONE of these commands:

**Option A (Recommended):**
```bash
pip install openpyxl pandas numpy matplotlib seaborn scipy
```

**Option B (If Option A fails):**
```bash
python -m pip install openpyxl pandas numpy matplotlib seaborn scipy
```

**Option C (Using requirements file):**
```bash
cd "C:\Users\Amalie Berg\Desktop\NORD POOL\Case Interview"
pip install -r requirements.txt
```

### Step 3: Organize Your Files
Make sure these files are in the same folder:
```
C:\Users\Amalie Berg\Desktop\NORD POOL\Case Interview\
├── market_surveillance_alerts.py
├── AuctionPrice_2025_DayAhead_AT,BE,BG,DK1,DK2,EE,FI,FR,GER,LT,LV,NL,NO1,NO2,NO3,NO4,NO5,PL,SE1,SE2,SE3,SE4,TEL_EUR_None.xlsx
├── requirements.txt
└── README.md
```

### Step 4: Run the Script

**Method 1: Using Command Prompt**
```bash
cd "C:\Users\Amalie Berg\Desktop\NORD POOL\Case Interview"
python market_surveillance_alerts.py
```

**Method 2: Double-click the .py file**
- Right-click on `market_surveillance_alerts.py`
- Choose "Open with" → "Python"

### Step 5: Check Output
After running, you should see:
- ✅ Console output with statistics
- ✅ New file created: `alerts_oct6-12.csv` (in same folder)

---

## ❌ Troubleshooting Common Errors

### Error 1: "ModuleNotFoundError: No module named 'openpyxl'"
**Solution:**
```bash
pip install openpyxl
```

### Error 2: "pip is not recognized as an internal or external command"
**Solution:** Python not added to PATH. Try:
```bash
python -m pip install openpyxl
```

### Error 3: "Permission denied"
**Solution:** Run Command Prompt as Administrator
- Right-click on Command Prompt
- Select "Run as administrator"
- Try installation again

### Error 4: "File not found"
**Solution:** The script will prompt you to enter the full path to the Excel file. Copy and paste:
```
C:\Users\Amalie Berg\Desktop\NORD POOL\Case Interview\AuctionPrice_2025_DayAhead_AT,BE,BG,DK1,DK2,EE,FI,FR,GER,LT,LV,NL,NO1,NO2,NO3,NO4,NO5,PL,SE1,SE2,SE3,SE4,TEL_EUR_None.xlsx
```

---

## 📝 What You Should See (Expected Output)

```
================================================================================
NORD POOL MARKET SURVEILLANCE - ALERT SYSTEM
================================================================================

✓ Libraries imported successfully

================================================================================
STEP 1: DATA LOADING AND PREPARATION
================================================================================

📂 Loading data from: [your path]
✓ Raw data loaded: 8568 rows × 25 columns
...

📊 TOTAL ALERTS GENERATED: 1244

TOP 10 CRITICAL ALERTS
2025-10-07 07:00     LT       Extreme Absolute Price       1173.65 CRITICAL
...

💾 All alerts saved to: alerts_oct6-12.csv
```

---

## 📦 Files for Submission

When ready to submit, include:
1. ✅ `market_surveillance_alerts.py` - Main script
2. ✅ `requirements.txt` - Dependencies list
3. ✅ `README.md` - Full documentation
4. ✅ `alerts_oct6-12.csv` - Output file (generated)
5. ✅ Excel data file (if requested)

---

## ⏱️ Estimated Time
- Installation: 5 minutes
- Running script: 30 seconds
- Reviewing output: 5 minutes
- **Total: ~10 minutes**

---

## 💡 Tips for the Interview

When presenting this code:
1. **Show you understand the logic:** Explain why you chose each alert type
2. **Discuss trade-offs:** Why 3σ for outliers? Why 500 EUR threshold?
3. **Highlight October 7:** Point out the 1,173 EUR/MWh in Lithuania/Latvia
4. **Explain next steps:** How would you investigate these alerts?
5. **Show flexibility:** Mention what you'd add with more time/data

---

## 🆘 Need Help?

If you encounter issues:
1. Check that Python 3.8+ is installed: `python --version`
2. Verify packages are installed: `pip list`
3. Ensure Excel file is in correct location
4. Check file path doesn't have special characters

**During the interview:** If technical issues arise, you can:
- Walk through the code logic without running it
- Show the pre-generated `alerts_oct6-12.csv`
- Explain your methodology verbally

---

## ✅ Pre-Interview Checklist

- [ ] Python installed and working
- [ ] All packages installed (`openpyxl`, `pandas`, etc.)
- [ ] Script runs successfully
- [ ] `alerts_oct6-12.csv` generated
- [ ] Reviewed top 10 critical alerts
- [ ] Understand October 7 price event
- [ ] Can explain each alert type
- [ ] Ready to discuss investigation approach

**You're ready! Good luck with your interview! 🍀**
