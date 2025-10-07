import plotly.express as px
import plotly.graph_objects as go
 
# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 25, 15, 30]}
 
# Create a bar chart using Plotly Express
fig1 = px.bar(data, x='Category', y='Values', title='Bar Chart')
 
# Create a scatter plot using Plotly Graph Objects
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data['Category'], y=data['Values'], mode='markers', name='Scatter Plot'))
 
# Show the visualizations
fig1.show()
fig2.show()