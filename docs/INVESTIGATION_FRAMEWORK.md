# Investigation Framework
## 5-Phase Methodology for Market Surveillance

**Document Version:** 1.0  
**Last Updated:** October 2025  
**Author:** Amalie Berg

---

## Overview

This document outlines the systematic investigation approach developed for analyzing suspicious price behavior detected by the Nord Pool Market Surveillance Alert System. The framework was successfully applied to investigate the October 7, 2025 critical price event (1,173.65 EUR/MWh in Lithuania/Latvia).

---

## Phase 1: Data Verification & Initial Assessment

### Objective
Confirm the accuracy of detected anomalies and gather initial context.

### Actions

**1.1 Validate Alert Data**
- [ ] Cross-check alert timestamps with original data
- [ ] Verify price values in multiple data sources
- [ ] Confirm zone mappings are correct
- [ ] Check for data transmission errors

**1.2 Check REMIT Transparency Platform**
- [ ] Review Urgent Market Messages (UMM) for relevant dates
- [ ] Look for planned/unplanned outage notifications
- [ ] Check capacity reduction announcements
- [ ] Note publication delays or system issues

**1.3 Initial Severity Assessment**
- [ ] Categorize alerts by type and severity
- [ ] Identify clustering (time, zone, participant)
- [ ] Prioritize investigation targets
- [ ] Determine if immediate escalation needed

### Deliverables
- Data validation report
- UMM publication summary
- Initial priority ranking
- Timeline of events

### Example: October 7, 2025
✅ Verified 1,173.65 EUR/MWh in LT/LV at 07:00 CET  
✅ Found UMM: Publication delay (12:55→13:49 CET)  
✅ Found UMM: Intraday partial decoupling (14:35 CET)  
✅ Priority: CRITICAL - immediate investigation

---

## Phase 2: Fundamental Analysis

### Objective
Understand the physical and operational factors that could explain price behavior.

### Actions

**2.1 Weather Conditions**
- [ ] Check weather patterns for affected zones
- [ ] Review wind speed/direction (impacts wind generation)
- [ ] Assess temperature (impacts demand)
- [ ] Identify storm systems or extreme events
- [ ] Compare forecasts vs. actual conditions

**2.2 Generation Analysis**
- [ ] Review generation mix by zone
- [ ] Check for unplanned outages (nuclear, thermal, hydro)
- [ ] Assess renewable generation (wind/solar actuals vs. forecast)
- [ ] Identify must-run generation constraints
- [ ] Calculate available capacity vs. demand

**2.3 Transmission System**
- [ ] Review interconnector capacities (day-ahead values)
- [ ] Compare to historical capacity baselines
- [ ] Check for line outages or derating
- [ ] Assess if capacity reductions were justified
- [ ] Map congestion patterns (bottlenecks)

**2.4 Demand Patterns**
- [ ] Analyze demand levels vs. forecasts
- [ ] Check for unusual consumption patterns
- [ ] Assess temperature-sensitive demand
- [ ] Compare to historical demand curves
- [ ] Identify demand-side response actions

### Deliverables
- Weather impact assessment
- Generation availability report
- Transmission capacity analysis
- Demand analysis summary
- Fundamental supply-demand balance

### Example: October 7, 2025
✅ **Weather**: Storm Amy active - high winds in Norway/Sweden  
✅ **Generation**: Excess wind in north → negative prices  
✅ **Transmission**: Likely derating for storm safety  
✅ **Demand**: Baltic heating load spike (cold weather)  
✅ **Conclusion**: Physical scarcity, not artificial

---

## Phase 3: Market Behavior Analysis

### Objective
Analyze participant actions and market dynamics to identify suspicious patterns.

### Actions

**3.1 Order Book Analysis**
- [ ] Review bid/offer curves for affected hours
- [ ] Calculate order book depth
- [ ] Assess liquidity levels
- [ ] Identify unusual bid/offer patterns
- [ ] Check for strategic withholding indicators

**3.2 Participant Behavior**
- [ ] Identify major participants in affected zones
- [ ] Review bidding patterns (volume, price levels)
- [ ] Compare to historical behavior
- [ ] Check for coordinated actions
- [ ] Assess market concentration (HHI index)

**3.3 Cross-Market Analysis**
- [ ] Compare day-ahead vs. intraday prices
- [ ] Check balancing market prices
- [ ] Assess forward curve movements
- [ ] Review cross-border arbitrage opportunities
- [ ] Identify unusual spreads

**3.4 Trading Volume Analysis**
- [ ] Review volumes in affected hours
- [ ] Check for unusual trading patterns
- [ ] Assess cleared volumes vs. capacity
- [ ] Identify if any participants gained positions
- [ ] Review post-clearing adjustments

### Deliverables
- Order book concentration analysis
- Participant behavior assessment
- Cross-market consistency check
- Trading pattern summary
- Red flag identification

### Example: October 7, 2025
✅ **Order Book**: High concentration in Baltic zones  
✅ **Behavior**: No obvious strategic withholding  
✅ **Cross-Market**: Intraday also showed high prices  
✅ **Conclusion**: Consistent with physical shortage

---

## Phase 4: Regulatory Compliance Assessment

### Objective
Determine if there is evidence of REMIT violations or other regulatory breaches.

### Actions

**4.1 REMIT Article 3 - Insider Trading**
- [ ] Check if inside information was properly disclosed
- [ ] Review timing of information publication
- [ ] Assess if anyone traded on inside information
- [ ] Identify information asymmetries
- [ ] Compare participant positions before/after disclosure

**4.2 REMIT Article 4 - Inside Information Disclosure**
- [ ] Verify all material information was disclosed
- [ ] Check timeliness of disclosures
- [ ] Assess completeness of information
- [ ] Review if thresholds were met for disclosure
- [ ] Identify any non-disclosure violations

**4.3 REMIT Article 5 - Market Manipulation**
- [ ] Assess evidence of price manipulation
- [ ] Check for artificial price signals
- [ ] Review capacity withholding evidence
- [ ] Identify wash trades or layering
- [ ] Assess coordinated manipulation

**4.4 Market Abuse Indicators**
- [ ] Unusual profit patterns
- [ ] Coordinated actions across participants
- [ ] Price manipulation techniques
- [ ] Information-based manipulation
- [ ] Abuse of dominant position

### Deliverables
- REMIT compliance checklist
- Evidence matrix (supports/refutes violation)
- Legal assessment memo
- Confidence level in findings
- Recommendation for NRA notification

### Example: October 7, 2025
✅ **Article 3**: No evidence of insider trading  
✅ **Article 4**: UMM publications timely  
✅ **Article 5**: No evidence of manipulation  
✅ **Conclusion**: REMIT compliant - legitimate market response

---

## Phase 5: Documentation & Escalation

### Objective
Document findings comprehensively and determine appropriate follow-up actions.

### Actions

**5.1 Case File Preparation**
- [ ] Executive summary (1-page)
- [ ] Detailed timeline of events
- [ ] Data analysis and evidence
- [ ] Visualizations and charts
- [ ] Regulatory assessment
- [ ] Conclusions and confidence level

**5.2 Risk Classification**
- [ ] **No Action Required**: Normal market behavior
- [ ] **Monitor**: Unusual but explainable, watch for patterns
- [ ] **Educate**: Provide guidance to market participants
- [ ] **Investigate Further**: Gather additional evidence
- [ ] **Escalate to NRA**: Potential violation identified

**5.3 Internal Review**
- [ ] Present to team lead
- [ ] Discuss in surveillance team meeting
- [ ] Obtain peer review
- [ ] Assess need for escalation
- [ ] Document decision rationale

**5.4 External Communication (if needed)**
- [ ] Prepare NRA notification (STOR)
- [ ] Draft participant inquiry letters
- [ ] Coordinate with TSOs if needed
- [ ] Follow up on information requests
- [ ] Track case through to resolution

**5.5 Lessons Learned**
- [ ] Update alert thresholds if needed
- [ ] Refine detection algorithms
- [ ] Document investigation insights
- [ ] Share with surveillance team
- [ ] Contribute to best practices

### Deliverables
- Comprehensive case file
- Risk classification decision
- Escalation recommendation
- Communication materials (if needed)
- Process improvement notes

### Example: October 7, 2025
✅ **Case File**: Complete documentation prepared  
✅ **Classification**: Monitor - legitimate but systemic issues  
✅ **Recommendation**: No NRA escalation needed  
✅ **Follow-up**: Recommend Nord Pool review:
   - Market coupling algorithm performance under stress
   - TSO capacity reduction protocols
   - System reliability (prevent manual fallbacks)

---

## Investigation Timeline

### Standard Timeline
- **Phase 1 (Data Verification)**: 2-4 hours
- **Phase 2 (Fundamentals)**: 1-2 days
- **Phase 3 (Market Behavior)**: 2-3 days
- **Phase 4 (Regulatory)**: 1-2 days
- **Phase 5 (Documentation)**: 1 day
- **Total**: 5-8 days for complete investigation

### Expedited Timeline (Critical Cases)
- **Phase 1**: 1 hour
- **Phase 2**: 4-6 hours
- **Phase 3**: 1 day
- **Phase 4**: 4-6 hours
- **Phase 5**: 4 hours
- **Total**: 2 days maximum

---

## Quality Standards

### Evidence Requirements
- **High Confidence** (>80%): Multiple independent sources confirm findings
- **Medium Confidence** (50-80%): Evidence supports conclusion but gaps remain
- **Low Confidence** (<50%): Inconclusive, needs further investigation

### Documentation Standards
- All data sources cited
- Assumptions clearly stated
- Alternative explanations considered
- Uncertainty acknowledged
- Chain of custody maintained

### Escalation Thresholds
- **Immediate**: Evidence of ongoing manipulation with market impact
- **24 hours**: Clear REMIT violation identified
- **1 week**: Suspicious patterns requiring NRA awareness
- **Monitor**: Unusual but insufficient evidence for escalation

---

## Tools & Resources

### Internal Systems
- Alert detection system (this repository)
- Market data warehouse
- Participant database
- Historical case files

### External Resources
- REMIT Transparency Platform (ARIS)
- Nord Pool UMM publications
- ENTSO-E Transparency Platform
- TSO websites
- Weather services (met.no, etc.)
- News sources

### Analytical Tools
- Python (data analysis)
- Excel (quick calculations)
- Power BI (visualization)
- SQL (database queries)

---

## Case Study: October 7, 2025 - Complete Application

### Initial Alert
**Time**: October 8, 08:00 CET (day after event)  
**Alert**: 373 alerts on October 7, including 17 CRITICAL  
**Trigger**: LT/LV prices 1,173.65 EUR/MWh at 07:00

### Phase 1 (2 hours)
- ✅ Verified data accuracy
- ✅ Found UMM: Publication delay + intraday decoupling
- ✅ Classified as CRITICAL priority

### Phase 2 (1 day)
- ✅ Identified Storm Amy weather event
- ✅ Confirmed high wind in north, cold in Baltics
- ✅ Found September UMMs showing system stress
- ✅ Assessed transmission likely derated for safety

### Phase 3 (1 day)
- ✅ Reviewed order book (high concentration but expected)
- ✅ Checked intraday (consistent high prices)
- ✅ No evidence of strategic withholding

### Phase 4 (1 day)
- ✅ REMIT Article 3: Compliant
- ✅ REMIT Article 4: Compliant
- ✅ REMIT Article 5: Compliant
- ✅ Conclusion: Legitimate market response

### Phase 5 (1 day)
- ✅ Documented comprehensive case file
- ✅ Classification: Monitor (no violation, but systemic concerns)
- ✅ Recommendations: System improvements needed
- ✅ No NRA escalation required

**Total Investigation Time**: 4 days  
**Outcome**: Case closed - legitimate market event with systemic learnings

---

## Continuous Improvement

### Metrics Tracked
- Average investigation time
- False positive rate
- Cases escalated to NRA
- Cases resulting in enforcement
- Process improvement suggestions

### Review Cycle
- Monthly: Team review of closed cases
- Quarterly: Methodology refinement
- Annually: Comprehensive process audit

---

**Document Control:**  
Version 1.0 - October 2025  
Approved by: Surveillance Team Lead  
Next Review: October 2026
