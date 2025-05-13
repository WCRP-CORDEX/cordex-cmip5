import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

url = "https://raw.githubusercontent.com/WCRP-CORDEX/cordex-cmip5/refs/heads/main/esgf-data-loss/Missing_CORDEX_Data.txt"
response = requests.get(url)
data = response.text.splitlines()

df = pd.DataFrame([line.split('.') for line in data if line.strip()], 
                 columns=['project', 'product', 'domain', 'institute', 'driving_model',
                         'experiment', 'ensemble', 'model', 'version', 'frequency',
                         'variable', 'version_date'])
df[['domain', 'resolution']] = df['domain'].str.split('-', n=1, expand=True)

plt.figure(figsize=(20, 12))
#plt.suptitle('CORDEX Missing Data Statistics', fontsize=16, y=1.02)

categories = ['domain', 'resolution', 'frequency', 'experiment', 'variable']
colors = sns.color_palette('pastel')

for i, category in enumerate(categories, 2):
    plt.subplot(2, 3, i)
    counts = df[category].value_counts()
    
    # For variable chart, show only most common with "Others" category
    if category == 'variable':
        ntop = 40
        top_counts = counts.head(ntop)
        others = pd.Series([counts[ntop:].sum()], index=['Others'])
        top_counts = pd.concat([top_counts, others])
        plt.pie(top_counts, labels=top_counts.index, autopct='%1.1f%%',
                startangle=90, colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
    else:
        plt.pie(counts, labels=counts.index, autopct='%1.1f%%',
                startangle=90, colors=colors, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
    
    plt.title(f"by {category}", fontsize=14, loc="left")
    plt.axis('equal')

plt.subplot(2, 3, 1)
plt.axis('off')
plt.text(0.5, 0.5, 'CORDEX-CMIP5 data loss (2025) statistics', 
         ha='center', va='center', fontsize=16, fontweight='bold')
plt.text(0.5, 0.4, f'Total missing datasets: {len(df)}', 
         ha='center', va='center', fontsize=12)

plt.tight_layout()
plt.savefig('docs/cordex_data_loss_2025_piecharts.png', dpi=90, bbox_inches='tight')
plt.close()
