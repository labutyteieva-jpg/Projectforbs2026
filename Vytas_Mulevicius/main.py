import streamlit as st

st.set_page_config(
    page_title="CERN Open Data Explorer - Home",
    page_icon="⚛️",
    layout="wide"
)

st.write("# Welcome to the CERN Open Data Explorer! ⚛️")

st.markdown("""
This application allows you to explore authentic High Energy Physics data released by the CMS experiment at CERN.

Using the tools built into this dashboard, you can "rediscover" fundamental particles like the $J/\\psi$, $\\Upsilon$, and $Z$ bosons by analyzing the invariant mass of dimuon pairs ($\\mu^+\\mu^-$) generated in proton-proton collisions during Run 2011A.

### 👈 Getting Started
To begin your interactive physics analysis, **select the `1 Analysis` page from the sidebar menu to the left.**

### What you will find in the Analysis module:
- **Interactive Mass Histograms:** Apply custom kinematic cuts and scan through millions of events.
- **Advanced 3D Event Display:** Visualize the individual momentum vectors ($p_x, p_y, p_z$) of the emitted muons, just like physicists do at CERN.
- **3D Event Animation:** Native browser animations to scan through massive collision datasets seamlessly.

### Datasets Included:
1. **$J/\\psi \\rightarrow \\mu\\mu$**: A lower mass resonance proving the existence of the charm quark.
2. **$\\Upsilon \\rightarrow \\mu\\mu$**: The bottomonium resonance that confirms the bottom quark.
3. **$Z \\rightarrow \\mu\\mu$**: The massive weak force carrier boson. 
""")

st.info("💡 **Navigation:** Use the sidebar on the left to switch between this Home page and the actual interactive Analysis dashboard.")
st.success("Head over to the Analysis page to start your journey!")
