import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Sample dataset
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 30, 40, 50, 60],
    'Subcategory': ['X', 'X', 'Y', 'Y', 'Z', 'Z']
}

df = pd.DataFrame(data)

# Create a function to update the figure based on selected category and subcategory
def update_figure(selected_category, selected_subcategory):
    filtered_df = df[(df['Category'] == selected_category) & (df['Subcategory'] == selected_subcategory)]

    fig = px.bar(filtered_df, x='Subcategory', y='Value', title=f'Values for Category {selected_category} and Subcategory {selected_subcategory}')
    
    fig.update_layout(
        updatemenus=[
            {
                'buttons': [
                    {
                        'args': [{'visible': [True, True]}],
                        'label': 'Show All',
                        'method': 'update'
                    },
                    {
                        'args': [{'visible': [True, False]}],
                        'label': 'Show Filtered',
                        'method': 'update'
                    }
                ],
                'direction': 'down',
                'showactive': True,
            }
        ],
        sliders=[
            {
                'steps': [
                    {
                        'label': category,
                        'method': 'update',
                        'args': [{'visible': [category == selected_category, category == selected_subcategory]}]
                    } for category in df['Category'].unique()
                ],
                'currentvalue': {
                    'prefix': 'Category: '
                }
            },
            {
                'steps': [
                    {
                        'label': subcategory,
                        'method': 'update',
                        'args': [{'visible': [subcategory == selected_subcategory, subcategory == selected_category]}]
                    } for subcategory in df['Subcategory'].unique()
                ],
                'currentvalue': {
                    'prefix': 'Subcategory: '
                }
            }
        ]
    )
    
    return fig

# Initialize figure
fig = update_figure('A', 'X')

# Show the figure
fig.show()
