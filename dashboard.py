import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Cleaned Data Load
# 1. Cleaned Data Load directly
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.drop_duplicates()
df['age'] = df.groupby('pclass')['age'].transform(lambda x: x.fillna(x.median()))
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
if 'cabin' in df.columns:
    df.drop(columns=['cabin'], inplace=True)
# 2. Key Metrics (KPIs)
total_passengers = len(df)
survival_rate = f"{(df['survived'].mean() * 100):.1f}%"
avg_age = f"{df['age'].mean():.1f} yrs"
avg_fare = f"${df['fare'].mean():.2f}"

# 3. Create Dashboard Visuals
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "Survival Rate by Gender",
        "Passenger Class Distribution",
        "Survival Rate by Passenger Class",
        "Age Distribution by Survival"
    ),
    specs=[[{"type": "bar"}, {"type": "pie"}],
           [{"type": "bar"}, {"type": "histogram"}]]
)

# Visual 1: Survival by Gender
gender_surv = df.groupby('sex')['survived'].mean().reset_index()
fig.add_trace(go.Bar(x=gender_surv['sex'], y=gender_surv['survived'], marker_color=['#1f77b4', '#e377c2'], name="Survival Rate"), row=1, col=1)

# Visual 2: Class Split (Donut)
pclass_counts = df['pclass'].value_counts().reset_index()
fig.add_trace(go.Pie(labels=pclass_counts['pclass'], values=pclass_counts['count'], hole=0.4, name="Class Share"), row=1, col=2)

# Visual 3: Survival by Class
pclass_surv = df.groupby('pclass')['survived'].mean().reset_index()
fig.add_trace(go.Bar(x=pclass_surv['pclass'], y=pclass_surv['survived'], marker_color='#2ca02c', name="Class Survival"), row=2, col=1)

# Visual 4: Age Distribution
fig.add_trace(go.Histogram(x=df[df['survived']==1]['age'], name='Survived', marker_color='teal', opacity=0.7), row=2, col=2)
fig.add_trace(go.Histogram(x=df[df['survived']==0]['age'], name='Not Survived', marker_color='crimson', opacity=0.7), row=2, col=2)

# Layout Setup with KPIs Header
fig.update_layout(
    title_text=f"<b>Interactive Dashboard - Titanic Analysis</b><br><sup>Total Passengers: {total_passengers} | Survival Rate: {survival_rate} | Avg Age: {avg_age} | Avg Fare: {avg_fare}</sup>",
    barmode='overlay',
    showlegend=False,
    height=800,
    template="plotly_white"
)

# 4. Save HTML Dashboard
fig.write_html("interactive_dashboard.html")
print("SUCCESS: interactive_dashboard.html ready ho gayi!")