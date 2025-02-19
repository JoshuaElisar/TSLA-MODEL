import streamlit as st
import matplotlib.pyplot as plt

SHARES_OUTSTANDING = 3.2e9
PE_RATIO = 40

def format_with_apostrophes(value):
    return f"{value:,.2f}".replace(",", "'")

st.title("Tesla Valuation Model")

r_produced = st.slider("Robotaxis Produced:", 0, 100000000, 100000, step=1000)
o_produced = st.slider("Optimus Bots Produced Total:", 0, 1000000000, 10000, step=1000)
p_per_mile = st.slider("Profit per Mile ($):", 0.0, 2.0, 0.50, step=0.01)
m_per_robotaxi = st.slider("Miles per Robotaxi/Year:", 0, 100000, 50000, step=1000)
o_sub_price = st.slider("Optimus Subscription ($/yr):", 0, 100000, 5000, step=100)

robotaxi_profit = r_produced * m_per_robotaxi * p_per_mile
optimus_profit = o_produced * o_sub_price
total_profit = robotaxi_profit + optimus_profit
market_cap = total_profit * PE_RATIO
stock_price = market_cap / SHARES_OUTSTANDING

st.markdown(f"### Yearly Profit: ${format_with_apostrophes(total_profit)}")
st.markdown(f"### Stock Price (P/E 40): ${format_with_apostrophes(stock_price)}")

fig, ax = plt.subplots(figsize=(9, 5), facecolor='#1E1E2F')
ax.set_facecolor('#2A2A40')
categories = ['Robotaxi Profit', 'Optimus Profit', 'Total Profit']
values = [robotaxi_profit, optimus_profit, total_profit]
colors = ['#4A90E2', '#E94E77', '#50C878']
bars = ax.bar(categories, values, color=colors, edgecolor='white', linewidth=0.5)
ax.set_title(f"Valuation Breakdown\nMarket Cap: ${format_with_apostrophes(market_cap)}",
             color='white', fontsize=18, pad=60, fontweight='bold')
ax.set_ylabel("Value ($)", color='white', fontsize=14)
ax.tick_params(axis='x', colors='white', labelsize=12)
ax.tick_params(axis='y', colors='white', labelsize=12)
ax.grid(alpha=0.1, linestyle='--', color='#A9A9A9')
ax.set_ylim(0, max(values) * 1.3)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${format_with_apostrophes(x)}"))
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + yval*0.02, f"${format_with_apostrophes(yval)}",
            ha='center', va='bottom', color='white', fontsize=10)
st.pyplot(fig)