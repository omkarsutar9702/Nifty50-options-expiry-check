#%%
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta
import yfinance as yf
import pandas as pd
#%%
# Define the ticker symbol for Nifty 50
ticker_symbol = '^NSEI'

# Define the start and end dates for the data
end_date = date.today()
start_date = end_date - relativedelta(years=2)
print(end_date)
print(start_date)
#%%
# Download historical data
nifty_data = yf.download(ticker_symbol, start=start_date, end=end_date)
# %%
# Reset index
df = nifty_data.reset_index()
# %%
# Get the day name
df['Day of Week'] = df['Date'].dt.day_name()

df['Day of Week'] = df['Date'].dt.day

# %%
# Extract day of the week and count occurrences
df['Date'].dt.day_name().value_counts()
# %%
