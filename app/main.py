import streamlit as st
from yahoo_api.client import YahooFantasyClient  
import pandas as pd

st.title("Yahoo Fantasy Basketball Manager")

# Instantiate your API client
client = YahooFantasyClient()

# (You could eventually allow league_key selection in the UI)
league_key = '454.l.100725'
league = client.get_league(league_key)
team = client.get_team(league)

# Fetch roster as DataFrame (using your get_roster_dataframe method)
df = client.get_roster_dataframe(team, league)

# Always include a 'news' column, even if empty
if 'editorial_player_news' in df.columns or 'notes' in df.columns:
    # Try to fill 'news' from the available Yahoo columns
    df['news'] = df.get('editorial_player_news', pd.Series(dtype='str')).combine_first(
        df.get('notes', pd.Series(dtype='str'))
    )
else:
    # If neither exists, create a blank 'news' column
    df['news'] = None

# Replace empty or missing news with 'None' (the string)
df['news'] = df['news'].fillna('None')
df['news'] = df['news'].replace('', 'None')

if 'editorial_player_news' in df.columns or 'notes' in df.columns:
    df['news'] = df.get('editorial_player_news', pd.Series(dtype='str')).combine_first(
        df.get('notes', pd.Series(dtype='str'))
    )

def highlight_status(status):
    if status in ['INJ', 'O', 'IL', 'IL+']:
        return "🔴 " + str(status)
    if status == 'GTD':
        return "🟠 " + str(status)
    return "🟢 " + str(status)

if 'status' in df.columns:
    df['status'] = df['status'].apply(highlight_status)

display_columns = [
    'player_id', 'name', 'status', 'eligible_positions', 'selected_position', 'news'
]
display_columns = [col for col in display_columns if col in df.columns]

st.subheader("My Team Roster")
st.dataframe(df)

# Optionally: allow CSV download
st.download_button(
    "Download roster as CSV",
    df.to_csv(index=False),
    file_name="my_roster.csv",
    mime="text/csv"
)