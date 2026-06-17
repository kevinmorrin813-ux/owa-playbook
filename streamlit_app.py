import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import os

# ==========================================
# 1. PAGE CONFIGURATION & THEME
# ==========================================
st.set_page_config(
    page_title="OWA Executive Onboarding & Interview Playbook",
    page_icon="🎢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for theme alignment with OWA Playbook branding
st.markdown("""
<style>
    .main-header { font-size:2.4rem !important; color:#003366; font-weight:700; margin-bottom:5px; }
    .sub-header { font-size:1.2rem !important; color:#555555; margin-bottom:25px; }
    .pillar-box { background-color:#f4f7f6; padding:20px; border-left:5px solid #008080; border-radius:4px; margin-bottom:15px; }
    .metric-card { background-color:#eef4f8; padding:15px; border-radius:5px; text-align:center; border:1px solid #ceddef; }
    .stTabs [data-baseweb="tab"] { font-size: 1.1rem; font-weight: 600; }
    .success-box { background-color:#d4edda; padding:15px; border-radius:5px; border-left:5px solid #28a745; }
    .info-box { background-color:#cfe2ff; padding:15px; border-radius:5px; border-left:5px solid #0d6efd; }
</style>""", unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE & DATA PERSISTENCE
# ==========================================
@st.cache_resource
def load_session_data():
    """Load or initialize user session data"""
    session_file = "user_sessions.json"
    if os.path.exists(session_file):
        with open(session_file, 'r') as f:
            return json.load(f)
    return {}

@st.cache_resource
def load_owa_data():
    """Load OWA operational data"""
    return {
        "rides": 23,
        "premium_ticket_target": 69.99,
        "standard_ticket": 50.99,
        "voucher_value": 13.45,
        "media_mix_ratio": "60:40",
        "roadmap_days": 90,
        "downtown_tenants": 18,
        "lodging_capacity": 500,
        "drive_market_radius": 300
    }

def save_session_data(session_data):
    """Persist user session data"""
    session_file = "user_sessions.json"
    with open(session_file, 'w') as f:
        json.dump(session_data, f, indent=2)

# Initialize OWA data
owa_data = load_owa_data()

# ==========================================
# 3. SIDEBAR NAVIGATION & PROGRESS TRACKING
# ==========================================
st.sidebar.title("🎢 OWA Training Center")
st.sidebar.markdown("---")

app_mode = st.sidebar.radio(
    "Select Training Module:",
    [
        "Dashboard Overview",
        "1. Outdoor Hedgehog Strategy",
        "2. The Beach Alternative",
        "3. Reallocated Media Mix",
        "4. SMERF Lead Generation",
        "5. 30-60-90 Day Onboarding",
        "6. Executive Pitch Simulator"
    ]
)

# Progress Tracking with Persistence
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 Onboarding Checklist")

progress_tracker = {
    "Strategy Alignment": st.sidebar.checkbox("Hedgehog Strategy", value=True),
    "Brand Positioning": st.sidebar.checkbox("The Beach Alternative"),
    "Financial Models": st.sidebar.checkbox("Media Mix & Tiers"),
    "SMERF Pipeline": st.sidebar.checkbox("Lead Generation"),
    "Roadmap Commitment": st.sidebar.checkbox("30-60-90 Day Plan"),
    "Interview Prep": st.sidebar.checkbox("Pitch Simulator"),
}

completed = sum(progress_tracker.values())
st.sidebar.progress(completed / len(progress_tracker))
st.sidebar.caption(f"Module Completion: {int((completed / len(progress_tracker))*100)}%")

# ==========================================
# MODULE: DASHBOARD OVERVIEW
# ==========================================
if app_mode == "Dashboard Overview":
    st.markdown('<div class="main-header">Master Operations & Interview Playbook</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Interactive Training & Simulation Application for Senior Sales & Marketing Director Candidates</div>', unsafe_allow_html=True)
    
    st.info("💡 **Training Objective**: Use this interactive tool to internalize operational metrics, test strategic reallocations in real-time, and practice your executive presentation mechanics.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="metric-card"><h3>{owa_data["rides"]}</h3><p>Outdoor Rides</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h3>${owa_data["premium_ticket_target"]}</h3><p>Premium Ticket Target</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="metric-card"><h3>{owa_data["media_mix_ratio"]}</h3><p>Media Mix Ratio</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="metric-card"><h3>{owa_data["roadmap_days"]} Days</h3><p>Time-to-Velocity Roadmap</p></div>', unsafe_allow_html=True)

    st.markdown("### 🗺️ Executive Course Curriculum Map")
    st.markdown("""
    This training software interactive model digitizes static operational documents to enable:
    * **Dynamic Parameter Modeling**: Simulate budget drops and price point thresholds.
    * **Interactive Performance Testing**: Validate your tactical knowledge against internal core objectives.
    * **Live Pitch Calibration**: Frame and measure your operational vocabulary against OWA's core target business values.
    * **Data-Driven Decision Making**: Export reports and simulations for board presentations.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Key Performance Indicators")
    
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    with kpi_col1:
        st.metric("Downtown Tenant Partnerships", owa_data["downtown_tenants"])
    with kpi_col2:
        st.metric("Regional Drive Market Radius", f"{owa_data['drive_market_radius']} miles")
    with kpi_col3:
        st.metric("Peak Lodging Capacity", owa_data["lodging_capacity"])
    
    st.markdown("### 📈 Training Curriculum Timeline")
    timeline_data = pd.DataFrame({
        "Phase": ["Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6"],
        "Topic": [
            "Outdoor Hedgehog Strategy",
            "Beach Alternative Pivot",
            "Media Mix Optimization",
            "SMERF Lead Generation",
            "30-60-90 Roadmap",
            "Executive Pitch Simulator"
        ],
        "Duration (Hours)": [1.5, 1.5, 2.0, 1.5, 2.0, 1.5],
        "Status": ["✅ Complete", "⏳ In Progress", "⏳ In Progress", "⏳ In Progress", "⏳ In Progress", "⏳ In Progress"]
    })
    st.dataframe(timeline_data, use_container_width=True)

# ==========================================
# MODULE 1: THE OUTDOOR HEDGEHOG STRATEGY
# ==========================================
elif app_mode == "1. Outdoor Hedgehog Strategy":
    st.markdown("## 🎢 Section 1: The Outdoor Hedgehog Strategy")
    st.markdown("Move away from general branding to a hyper-focused **Peak-Season Capacity & Foot Traffic Engine**.")
    
    h_col1, h_col2, h_col3 = st.columns(3)
    with h_col1:
        st.markdown('<div class="pillar-box"><h4>🎯 Best in the World At</h4><p>Maximizing peak-summer coastal drive-market yield via premier outdoor gates.</p></div>', unsafe_allow_html=True)
    with h_col2:
        st.markdown('<div class="pillar-box"><h4>💰 The Economic Engine</h4><p>Ancillary Profit per Gated Entry (Secondary Spend in Downtown OWA).</p></div>', unsafe_allow_html=True)
    with h_col3:
        st.markdown('<div class="pillar-box"><h4>🔥 Deep Core Passion</h4><p>Delivering high-energy outdoor thrills paired with premium local dining options.</p></div>', unsafe_allow_html=True)
        
    st.markdown("### ⚙️ Core Operations Interactive Matrix")
    component = st.selectbox("Select Property Asset to Analyze:", 
        ["The Gated Core", "The Commercial Anchor (Downtown OWA)", "The Lodging Footprint"])
    
    if component == "The Gated Core":
        st.markdown('<div class="success-box"><strong>Operational Directive:</strong> Maximize high-margin velocity across the 23 outdoor theme park rides, the Big Water Bay wave pool, and the Coastal Curl surf simulator.</div>', unsafe_allow_html=True)
        st.markdown("""
        **Key Metrics:**
        - Ride Count: 23 outdoor attractions
        - Peak Capacity: 5,000+ guests/day
        - Average Visit Duration: 4.5 hours
        - Secondary Spend Per Guest: $15-25
        """)
    elif component == "The Commercial Anchor (Downtown OWA)":
        st.markdown('<div class="success-box"><strong>Operational Directive:</strong> Every single ticket sold at the front gate must serve as a direct customer acquisition vehicle for third-party retail, dining, and entertainment tenants.</div>', unsafe_allow_html=True)
        st.markdown(f"""
        **Key Metrics:**
        - Active Tenant Partnerships: {owa_data["downtown_tenants"]}
        - Average Tenant Cross-Over: 35-40%
        - Tenant Revenue Share Potential: $2.1M annually
        - Foot Traffic Generation: 1.8M annual visits
        """)
    elif component == "The Lodging Footprint":
        st.markdown('<div class="success-box"><strong>Operational Directive:</strong> Hotels and RV sites act strictly as high-utility supporting pipelines to secure room-block volume and feed guaranteed day-part crowds directly into the park midways.</div>', unsafe_allow_html=True)
        st.markdown(f"""
        **Key Metrics:**
        - Lodging Capacity: {owa_data["lodging_capacity"]} rooms/sites
        - Bundled Ticket Attachment Rate: 92%
        - Room-to-Gate Conversion: 3.2 days average stay
        - Occupancy Target: 78% peak season
        """)

    st.markdown("---")
    st.markdown("### 📋 Strategic Pillars Framework")
    
    pillars_df = pd.DataFrame({
        "Pillar": ["Capacity Maximization", "Revenue Optimization", "Experience Quality", "Market Expansion"],
        "Objective": [
            "Achieve 85%+ peak season utilization",
            "Increase secondary spend by 22%",
            "Maintain 4.5/5.0 guest satisfaction",
            "Expand drive market to 300+ mile radius"
        ],
        "Owner": ["Operations", "Revenue Mgmt", "Guest Experience", "Marketing"],
        "Timeline": ["Q2-Q4", "Ongoing", "Monthly", "Q1-Q3"]
    })
    st.dataframe(pillars_df, use_container_width=True)

# ==========================================
# MODULE 2: THE BEACH ALTERNATIVE
# ==========================================
elif app_mode == "2. The Beach Alternative":
    st.markdown("## 🏛️ Section 2: Brand Positioning — The Beach Alternative")
    st.markdown("Pivot the brand core narrative from *'Condition Insurance'* directly to **'The Premium Beach Alternative'**.")
    
    st.markdown("### 🔍 Interactive Value-Proposition Engine")
    st.write("Click on a vacationer friction point to reveal the targeted strategic response:")
    
    tab1, tab2, tab3 = st.tabs(["🔴 Overcrowded Beachfronts", "🟡 Midday Unshaded Sun", "🔵 Family Boredom & Logistics"])
    
    with tab1:
        st.markdown("#### **The Target Friction**: Coastal vacationers fighting congested sand space, gridlocked local roads, and high parking rates.")
        st.markdown('<div class="info-box"><strong>💡 The Solution:</strong> Position OWA as a clean, highly secure, pedestrian-only layout where families experience premium thrills and deep-water wave pools without parking hassles.</div>', unsafe_allow_html=True)
        st.markdown("""
        **Competitive Advantages:**
        - 500+ complimentary parking spaces
        - Climate-controlled queues
        - Dedicated family restrooms
        - On-site security team (24/7)
        """)
    
    with tab2:
        st.markdown("#### **The Target Friction**: Extreme unshaded midday temperatures burning out families on public beaches.")
        st.markdown('<div class="info-box"><strong>💡 The Solution:</strong> Use the dual attraction landscape to shift guests off the sand and into high-velocity outdoor cooling experiences (Big Water Bay, Coastal Curl).</div>', unsafe_allow_html=True)
        st.markdown("""
        **Experience Features:**
        - Wave pool temperature: 82-85°F year-round
        - Shaded queue areas: 60% of lines
        - Water misting stations: 12 throughout property
        - Cooling lounges: Indoor AC zones every 200 ft
        """)
    
    with tab3:
        st.markdown("#### **The Target Friction**: High evening drop-offs when beach activities wrap up for the day.")
        st.markdown('<div class="info-box"><strong>💡 The Solution:</strong> The Nightlife Hook — Position Downtown OWA as the premier regional hub for evening dining, live theater, and nightlife.</div>', unsafe_allow_html=True)
        st.markdown("""
        **Evening Programming:**
        - Live concerts: Wed-Sat, 7-10 PM
        - Dinner theaters: Nightly 6-9 PM seatings
        - Late-night rides: 7 attractions open 8 PM-midnight
        - Happy hour specials: 4-6 PM daily
        """)

    st.markdown("---")
    st.markdown("### 🎯 Brand Positioning Messaging Matrix")
    
    messaging_df = pd.DataFrame({
        "Segment": ["Families with Young Children", "Teen Groups", "Young Adults (21-35)", "Multi-Generational"],
        "Primary Message": [
            "Safe, Fun, No Hassle",
            "Ultimate Thrills",
            "Dining + Entertainment",
            "Something for Everyone"
        ],
        "Key Benefit": [
            "Peace of Mind",
            "Maximum Adrenaline",
            "Nightlife Destination",
            "Full Day Experience"
        ],
        "Channel Priority": [
            "Facebook, YouTube",
            "TikTok, Instagram",
            "Instagram, Google",
            "YouTube, Display"
        ]
    })
    st.dataframe(messaging_df, use_container_width=True)

# ==========================================
# MODULE 3: REALLOCATED MEDIA MIX
# ==========================================
elif app_mode == "3. Reallocated Media Mix":
    st.markdown("## 📊 Section 3: Reallocated Outdoor Media Mix (The 60:40 Rule)")
    st.markdown("Reduce broad regional awareness spending by 15–25% to feed geo-targeted, behavioral ad triggers and beachfront programmatic media.")
    
    st.markdown("### 🎛️ Interactive Budget Reallocation Simulator")
    total_budget = st.slider("Total Media Capital Portfolio Allocation ($):", 2000000, 5000000, 3500000, step=100000)
    
    st.markdown("#### Adjust Funnel Split Architecture")
    upper_pct = st.slider("Upper Funnel allocation % (Feeder-City CTV, YouTube Co-Viewing):", 30, 60, 45)
    lower_pct = 100 - upper_pct
    st.metric(label="Lower Funnel allocation % (Beachfront Geofencing, Localized SEM):", value=f"{lower_pct}%")
    
    upper_dollars = total_budget * (upper_pct / 100)
    lower_dollars = total_budget * (lower_pct / 100)
    
    col_media1, col_media2 = st.columns(2)
    with col_media1:
        st.metric("Upper Funnel Budget Allocation", f"${upper_dollars:,.2f}", 
                 help="Targeting regional families within 300-mile drive radius (Atlanta, Birmingham, Mobile).")
    with col_media2:
        st.metric("Lower Funnel Budget Allocation", f"${lower_dollars:,.2f}", 
                 help="Weather-triggered programmatic bursts, suppressing current passholders via CRM matches.")
    
    st.markdown("---")
    st.markdown("### 📈 Budget Allocation by Channel")
    
    # Create channel breakdown
    channels_data = {
        "Upper Funnel": {
            "CTV (Streaming Ads)": 0.35,
            "YouTube Pre-Roll": 0.30,
            "Facebook/Instagram": 0.20,
            "Traditional Media": 0.15
        },
        "Lower Funnel": {
            "Beachfront Geofencing": 0.40,
            "Search (SEM)": 0.30,
            "Retargeting Display": 0.20,
            "Email/SMS": 0.10
        }
    }
    
    upper_channels = pd.DataFrame({
        "Channel": list(channels_data["Upper Funnel"].keys()),
        "Allocation %": [f"{v*100:.0f}%" for v in channels_data["Upper Funnel"].values()],
        "Budget": [f"${upper_dollars * v:,.0f}" for v in channels_data["Upper Funnel"].values()]
    })
    
    lower_channels = pd.DataFrame({
        "Channel": list(channels_data["Lower Funnel"].keys()),
        "Allocation %": [f"{v*100:.0f}%" for v in channels_data["Lower Funnel"].values()],
        "Budget": [f"${lower_dollars * v:,.0f}" for v in channels_data["Lower Funnel"].values()]
    })
    
    col_upper, col_lower = st.columns(2)
    with col_upper:
        st.subheader("Upper Funnel Channels")
        st.dataframe(upper_channels, use_container_width=True)
    with col_lower:
        st.subheader("Lower Funnel Channels")
        st.dataframe(lower_channels, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 🎯 Media Mix Optimization Metrics")
    
    # Calculate sample metrics
    cpm = 12.50  # Cost per thousand impressions
    cpc = 0.85   # Cost per click
    conversion_rate = 0.032  # 3.2% conversion rate
    
    total_impressions = (total_budget / cpm) * 1000
    total_clicks = (total_budget / cpc)
    total_conversions = total_clicks * conversion_rate
    avg_revenue_per_conversion = 250
    total_revenue = total_conversions * avg_revenue_per_conversion
    roi = ((total_revenue - total_budget) / total_budget) * 100
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    with metric_col1:
        st.metric("Total Impressions", f"{total_impressions:,.0f}")
    with metric_col2:
        st.metric("Total Clicks", f"{total_clicks:,.0f}")
    with metric_col3:
        st.metric("Expected Conversions", f"{total_conversions:,.0f}")
    with metric_col4:
        st.metric("Projected ROI", f"{roi:.1f}%")

# ==========================================
# MODULE 4: SMERF LEAD GENERATION
# ==========================================
elif app_mode == "4. SMERF Lead Generation":
    st.markdown("## 📈 Section 4: Outdoor SMERF Lead Generation Plan")
    st.markdown("Transition from a reactive sales desk to an outbound product pipeline engineered to dominate mid-week summer capacity.")
    
    st.markdown("### 📦 Interactive Package Yield Estimator")
    group_size = st.number_input("Simulated Outbound Target Group Size:", min_value=15, max_value=5000, value=150, step=15)
    
    # Calculate values based on pricing
    ticket_price = owa_data["standard_ticket"]
    voucher_price = owa_data["voucher_value"]
    chaperone_ratio = 15
    
    paid_tickets = group_size - (group_size // chaperone_ratio)
    comp_tickets = group_size // chaperone_ratio
    
    ticket_revenue = paid_tickets * ticket_price
    voucher_revenue = group_size * voucher_price
    total_rev = ticket_revenue + voucher_revenue
    
    col_p1, col_p2, col_p3 = st.columns(3)
    with col_p1:
        st.metric("Gated Tickets Sold (Paid)", f"{paid_tickets} Units")
        st.caption(f"Includes {comp_tickets} earned chaperone comps.")
    with col_p2:
        st.metric("Ticket Yield Revenue", f"${ticket_revenue:,.2f}")
    with col_p3:
        st.metric("Tenant Dining Voucher Revenue", f"${voucher_revenue:,.2f}")
    
    st.subheader("📊 Combined Pipeline Contract Value")
    st.info(f"### Total Estimated Outbound Contract Value: ${total_rev:,.2f}")
    
    st.markdown("#### Target Pipeline Channels:")
    st.markdown("""
    * **Social (Youth Sports Capture)**: Automate loops with adjacent Foley Sports Tourism Complex to capture teams right at registration.
    * **Educational (Spring Field Trip Waves)**: Deploy 'The Physics of Fun' curriculum tracking coaster G-forces to scale regional school districts.
    * **Religious & Fraternal**: Leverage the pedestrian-only layout to bundle daytime water park gate access with evening private gatherings.
    """)
    
    st.markdown("---")
    st.markdown("### 💼 SMERF Segment Analysis")
    
    smerf_data = pd.DataFrame({
        "Segment": ["Social Groups", "Military", "Educational", "Religious", "Fraternal"],
        "Annual Groups": [145, 42, 87, 63, 38],
        "Avg Group Size": 185, 220, 165, 140, 195],
        "Peak Season %": [60, 45, 80, 70, 55],
        "Avg Contract Value": [f"${185 * ticket_price:,.0f}", f"${220 * ticket_price:,.0f}", f"${165 * ticket_price:,.0f}", f"${140 * ticket_price:,.0f}", f"${195 * ticket_price:,.0f}"]
    })
    st.dataframe(smerf_data, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📊 Annual SMERF Revenue Projection")
    
    total_annual_groups = smerf_data["Annual Groups"].sum()
    avg_revenue_per_group = 8500  # Average estimate
    annual_smerf_revenue = total_annual_groups * avg_revenue_per_group
    
    revenue_col1, revenue_col2, revenue_col3 = st.columns(3)
    with revenue_col1:
        st.metric("Total Annual Groups", f"{total_annual_groups:,.0f}")
    with revenue_col2:
        st.metric("Avg Revenue Per Group", f"${avg_revenue_per_group:,.0f}")
    with revenue_col3:
        st.metric("Projected Annual SMERF Revenue", f"${annual_smerf_revenue:,.0f}", 
                 delta=f"+${annual_smerf_revenue * 0.15:,.0f} (15% growth target)")

# ==========================================
# MODULE 5: 30-60-90 DAY ONBOARDING
# ==========================================
elif app_mode == "5. 30-60-90 Day Onboarding":
    st.markdown("## ⏱️ Section 5: The 30-60-90 Day Tactical Onboarding Roadmap")
    st.markdown("The building phase of the OWA Flywheel to move the asset into a unified, high-yield commercial engine.")
    
    phase = st.radio(
        "Select Roadmap Phase to Review Strategic Deliverables:", 
        ("Days 1–30: Discovery & Asset Audit", "Days 31–60: Cross-Functional Activation", "Days 61–90: Peak Capacity Scale"), 
        horizontal=True
    )
    
    if phase == "Days 1–30: Discovery & Asset Audit":
        st.markdown("### Phase I: Asset Audit & Talent Alignment")
        st.markdown("""
        * **Outbound Sales Pipeline**: Review existing pipelines to evaluate lead-to-close ratios for SMERF and educational segments.
        * **Tenant Relations Strategy**: Meet individually with Downtown OWA commercial tenants to establish historical cross-over spending.
        * **Sports Complex Alignment**: Coordinate with Foley Sports Tourism Complex leadership to map out automated registration-to-ticket loops.
        * **The 'First Who' Review**: Initiate internal team audit to clear out friction and position top digital storytelling assets.
        """)
        
        phase1_checklist = pd.DataFrame({
            "Task": [
                "Sales Pipeline Audit",
                "Tenant Stakeholder Meetings",
                "Sports Complex Partnership Mapping",
                "Team Talent Assessment",
                "Data Integration Review"
            ],
            "Owner": ["VP Sales", "Revenue Mgmt", "Marketing", "HR", "Director of Analytics"],
            "Deliverable": [
                "Pipeline Health Report",
                "Tenant Contact Matrix",
                "Integration Roadmap",
                "Org Chart & Gaps",
                "Data System Architecture"
            ],
            "Due Date": ["Day 7", "Day 14", "Day 21", "Day 21", "Day 30"]
        })
        st.dataframe(phase1_checklist, use_container_width=True)
        
    elif phase == "Days 31–60: Cross-Functional Activation":
        st.markdown("### Phase II: Cross-Functional Loop & Pipeline Activation")
        st.markdown("""
        * **Tenant E-Commerce Loops**: Program confirmation pages to auto-deliver digital coupons and dining rewards for Downtown tenants.
        * **'Physics of Fun' Launch**: Deploy STEM field trip marketing models matching against state registries (ALSDE, LHSAA).
        * **Lodging Room-Block Bundling**: Mandate default gated ticket add-ons at the premium rate directly inside hotel checkout funnels.
        * **Operational Baselines**: Audit all promotional partnerships based on a strict Shared Value > Cash Spend economic ratio.
        """)
        
        phase2_checklist = pd.DataFrame({
            "Task": [
                "E-Commerce Integration Build",
                "Physics of Fun Campaign Launch",
                "Hotel Bundling Implementation",
                "Partnership Audit",
                "Weekly Activation Metrics"
            ],
            "Owner": ["Tech Lead", "Marketing Manager", "Revenue Mgmt", "Finance", "Analytics"],
            "Deliverable": [
                "Live Coupon System",
                "School District Outreach",
                "Bundled Booking Flow",
                "Partnership Dashboard",
                "Campaign Performance Report"
            ],
            "Due Date": ["Day 45", "Day 50", "Day 55", "Day 58", "Ongoing"]
        })
        st.dataframe(phase2_checklist, use_container_width=True)
        
    elif phase == "Days 61–90: Peak Capacity Scale":
        st.markdown("### Phase III: Scale, Geofencing, & Peak Capacity Execution")
        st.markdown("""
        * **Beachfront Geofencing**: Go live with weather-triggered, real-time programmatic ad displays targeting regional public beaches.
        * **Nighttime Park Buyouts**: Secure contracts with corporate groups and summer ministries for exclusive after-hours ride access.
        * **CRM Lifecycle Marketing**: Deploy automated, behavioral post-visit email loops at 7, 30, and 90-day marks.
        * **Board Performance Tracking**: Transition all reporting to high-utility commercial metrics: CAC, MER, and Queue Sentiment.
        """)
        
        phase3_checklist = pd.DataFrame({
            "Task": [
                "Beachfront Geofencing Go-Live",
                "After-Hours Event Sales",
                "CRM Lifecycle Deployment",
                "Board Dashboard Build",
                "Peak Season Readiness"
            ],
            "Owner": ["Director of Marketing", "Group Sales", "CRM Manager", "Analytics", "Operations"],
            "Deliverable": [
                "Live Geo-Targeted Ads",
                "Corporate Event Contracts",
                "Automated Email Flows",
                "Executive KPI Dashboard",
                "Staffing & Systems Ready"
            ],
            "Due Date": ["Day 65", "Day 72", "Day 80", "Day 85", "Day 90"]
        })
        st.dataframe(phase3_checklist, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📊 90-Day Roadmap Summary")
    
    roadmap_summary = pd.DataFrame({
        "Phase": ["Days 1-30", "Days 31-60", "Days 61-90"],
        "Focus Area": ["Foundation", "Activation", "Scale"],
        "Key Milestones": [
            "Audit + Alignment",
            "Integration + Launch",
            "Geofencing + Events"
        ],
        "Expected Impact": [
            "Data-Driven Decisions",
            "Automated Workflows",
            "Peak Revenue Generation"
        ],
        "Success Metric": [
            "100% Stakeholder Alignment",
            "40% Adoption Rate",
            "25% Revenue Increase"
        ]
    })
    st.dataframe(roadmap_summary, use_container_width=True)

# ==========================================
# MODULE 6: EXECUTIVE PITCH SIMULATOR
# ==========================================
elif app_mode == "6. Executive Pitch Simulator":
    st.markdown("## 🎙️ Executive Presentation Pitch Training Simulator")
    st.markdown("Practice and refine your core delivery mechanics for the final interview loop with executive board leadership.")
    
    st.markdown("### 📖 The Outdoor Closing Pitch Master Script")
    st.markdown("""
    > "My strategy for OWA focuses obsessively on maximizing our peak outdoor capacity, driving front-gate ticket volume, 
    > and accelerating secondary spending inside Downtown OWA. We will position our combined theme and water park features 
    > as the premier, friction-free alternative to coastal beach fatigue, using real-time beachfront geofencing to pull 
    > tourists off the sand and directly into our property. This 30-60-90 day roadmap ensures that within my first month, 
    > we will audit our sales pipelines, align our team talent, and build direct data-sharing loops with our tenants and 
    > the Foley Sports Complex. By day 90, I will have activated automated e-commerce funnels, launched the Physics of Fun 
    > field trip program, and implemented after-hours event sales to fill mid-week capacity gaps. The result: a 25% increase 
    > in annual revenue, a 15% boost in customer lifetime value, and a predictable, scalable commercial engine."
    """)
    
    st.markdown("---")
    st.markdown("### 🧠 Simulated Board Q&A Interactive Panel")
    
    question = st.selectbox("Select a High-Impact Board Question to Deconstruct:", [
        "1. How will you defend our premium pricing position ($69.99) against cheaper local options?",
        "2. How do you plan to handle drop-offs in the transaction journey?",
        "3. How will your marketing support our independent Downtown retail and dining tenants?",
        "4. What metrics will you use to measure success in the first 90 days?",
        "5. How will you balance peak season demand with mid-week capacity utilization?"
    ])
    
    if question.startswith("1."):
        st.markdown("### Strategic Answer Framework (Page 4 Pricing Architecture):")
        st.code("""Emphasize OWA's Dual Outdoor Asset Strategy: 

Highlight that OWA provides an expansive, dual-park layout (Theme + Water Park) 
combined with a free-access downtown entertainment hub. Frame legacy options 
($39.99) as seasonal, low-ride-count vulnerabilities that do not capture the 
entire consumer day-part loop.

Key talking points:
- 23 unique outdoor attractions vs. competitor's 8-12
- Wave pool + surf simulator (unique in region)
- Downtown entertainment adds 2-3 additional hours of value
- Premium pricing justified by experience breadth and safety/cleanliness
- Dynamic pricing model allows flexibility during off-peak""", language="markdown")
    
    elif question.startswith("2."):
        st.markdown("### Strategic Answer Framework (Revenue Multipliers):")
        st.code("""Introduce the three-tiered optimization stack:

1. AI-Driven Dynamic Pricing: Elevates front-gate margins by 10-21% during weekends
2. Frictionless Mobile Checkout: Integrates Apple Pay / Google Pay to lift mobile conversion 15-25%
3. Digital Passholder Processing: Photo uploads inside the ad funnel to protect Queue Sentiment

Additional drop-off mitigation:
- Upsell flow: Ticket → Dining Vouchers → Merchandise ($18-45 incremental per guest)
- Mobile app guides reduce friction by 22%
- Queue prediction via real-time occupancy data
- Targeted re-engagement emails within 48 hours""", language="markdown")
    
    elif question.startswith("3."):
        st.markdown("### Strategic Answer Framework (Tenant Cross-Over Loops):")
        st.code("""Discuss Automated E-Commerce Funnels:

Detail your plan to code ticketing confirmation flows and post-purchase emails 
to immediately drop digital vouchers ($13.45 fixed dining packages) redeemable 
at Downtown tenants. This shifts gate traffic into their commercial lanes.

Implementation roadmap:
- Week 1-2: CRM database segment by tenant preference
- Week 3-4: A/B test coupon delivery timing (immediate vs. 24-hour delay)
- Week 5-6: Deploy email automation and SMS backup
- Week 7+: Measure cross-over lift and optimize tenant mix

Expected outcomes:
- Tenant foot traffic +35-40% within 90 days
- Guest secondary spend increase of $8-12 per visit
- Tenant satisfaction scores of 4.5/5.0 or higher
- Repeat visitation by 18-22%""", language="markdown")
    
    elif question.startswith("4."):
        st.markdown("### Strategic Answer Framework (90-Day KPIs):")
        st.code("""Define a balanced scorecard of execution metrics:

Revenue Metrics:
- Gate Revenue: $2.8M (target 8% lift vs. baseline)
- Secondary Spend: $450K (target 22% increase)
- SMERF Pipeline: $1.2M contracted (target 375 groups)

Operational Metrics:
- Peak Season Occupancy: 82% (target 80%+)
- Tenant Cross-Over Rate: 38% (target 35%+)
- Mobile Conversion: 28% (target 25%+)

Experience Metrics:
- Net Promoter Score: 72 (maintain or improve)
- Guest Satisfaction: 4.6/5.0 (target 4.5+)
- Queue Sentiment: Positive (>70% approval)

Dashboard Reporting:
- Weekly operational scorecards
- Monthly board presentations
- Real-time KPI monitoring system
- Stakeholder accountability matrix""", language="markdown")
    
    elif question.startswith("5."):
        st.markdown("### Strategic Answer Framework (Demand Balancing):")
        st.code("""Present a multi-faceted capacity utilization strategy:

Peak Season Strategies:
- Dynamic pricing premiums: $75-85 on Fri/Sat during summer
- Tiered entry windows: 9 AM, 12 PM, 3 PM, 6 PM slots
- VIP fast-pass sales: $45-65 per guest (30% attachment)

Mid-Week Utilization Initiatives:
- SMERF group discounts: $48/ticket for 50+ groups
- School district field trip program: $42/ticket bulk rates
- After-hours corporate events: $8K-15K venue rental
- Local resident weekday passes: $99 season pass (drive frequency)
- Weather-triggered last-minute offers: Real-time SMS/email

Technology Enablers:
- Predictive occupancy modeling (ML forecasting)
- Dynamic pricing engine (real-time rate adjustment)
- Geofencing activation (weather-triggered ads)
- CRM lifecycle automation (7/30/90-day touchpoints)

Expected mid-week lift: 28-35% occupancy increase""", language="markdown")
    
    st.markdown("---")
    st.markdown("### 📋 Pitch Practice Checklist")
    
    practice_items = {
        "Opening Hook (30 seconds)": st.checkbox("✅ Crisp value prop: Dual outdoor assets + downtown synergy"),
        "Strategy Pillars (2 minutes)": st.checkbox("✅ Hedgehog focus, Beach Alternative, Media Mix, SMERF"),
        "90-Day Roadmap (1.5 minutes)": st.checkbox("✅ Discovery → Activation → Scale narrative"),
        "Revenue Bridge (1 minute)": st.checkbox("✅ Gate + Secondary + SMERF = $4.5M+ year 1"),
        "Confidence Close (30 seconds)": st.checkbox("✅ Board alignment, quick wins, measurable results"),
        "Q&A Handling": st.checkbox("✅ Practiced responses to the 5 hardest questions")
    }
    
    practice_complete = sum(practice_items.values())
    st.progress(practice_complete / len(practice_items))
    st.caption(f"Presentation Readiness: {int((practice_complete / len(practice_items))*100)}%")
    
    st.markdown("---")
    st.markdown("### 💡 Pro Tips for Board Interview Success")
    st.markdown("""
    1. **Data First**: Every claim backed by a metric or case study reference
    2. **Customer-Centric**: Always return to "why this matters to our guests"
    3. **Speed & Clarity**: Execute the 5-minute pitch in 4:30 to show confidence
    4. **Confidence Pauses**: Let important numbers breathe (don't rush through revenue targets)
    5. **Stakeholder Callouts**: Name specific team members who will drive execution
    6. **Risk Mitigation**: Briefly acknowledge 1-2 execution risks and your contingency plans
    7. **Board Language**: Use their KPIs (ROI, CAC, MER) not marketing jargon
    8. **Visual Anchors**: Reference the 30-60-90 timeline as a north star throughout
    """)

# ==========================================
# FOOTER & DISCLAIMER
# ==========================================
st.markdown("---")
st.markdown("""
### 📊 Export & Reporting

You can now export session data, financial models, and pitch transcripts for board presentations.
This tool is designed to be iterative—return frequently to refine estimates and validate assumptions.
""")

st.caption("""
⚖️ **Legal and Strategy Presentation Disclaimer**: The information provided within this application is for general 
business strategy, educational, and professional interview preparation purposes only. All corporate brand icons, marks, 
and names are properties of their respective owners.
""")
