import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CERN educational dataset
df = pd.read_csv('data/Jpsimumu_Run2011A.csv')

# The dataset already contains an 'M' column, but we calculate it manually 
# from the 4-vectors to demonstrate the actual physics calculation.
# Formula: M^2 = (E1+E2)^2 - (px1+px2)^2 - (py1+py2)^2 - (pz1+pz2)^2
print("Calculating invariant mass...")
E_tot  = df['E1'] + df['E2']
px_tot = df['px1'] + df['px2']
py_tot = df['py1'] + df['py2']
pz_tot = df['pz1'] + df['pz2']

# Invariant mass squared
M2 = E_tot**2 - (px_tot**2 + py_tot**2 + pz_tot**2)

# Handle potential tiny negative values before sqrt due to floating point precision
M2 = np.maximum(M2, 0)
df['Calculated_M'] = np.sqrt(M2)

# Create the plot
plt.figure(figsize=(10, 6))

# The J/psi mass is approx 3.1 GeV, so we plot the range around it
# For J/psi, it usually spans roughly 2.0 to 5.0 GeV in these educational sets
plt.hist(df['Calculated_M'], bins=200, range=(2.0, 5.0), color='royalblue', edgecolor='none')

plt.title('Invariant Mass of Dimuon Pairs (J/ψ → μμ)', fontsize=16)
plt.xlabel('Invariant Mass [GeV/c²]', fontsize=14)
plt.ylabel('Number of Events / 15 MeV', fontsize=14)

# Adding a text box or line pointing to the exact J/psi mass
plt.axvline(x=3.096, color='red', linestyle='--', label='J/ψ Mass (3.096 GeV/c²)')
plt.legend(fontsize=12)

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

output_plot = 'Jpsi_mass_histogram.png'
plt.savefig(output_plot, dpi=300)
print(f"Plot saved successfully as {output_plot}!")
