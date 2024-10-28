import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import plotly.graph_objects as go

def pieChart(data):
    total_nutrition = {
      'Protein': data['Protein'].sum(),
      'Carbohydrates': data['Carbohydrates'].sum(),
      'Fats': data['Fats'].sum()
    }

    # Create dataframe and figure based on aggregated data
    nutrition_df = pd.DataFrame(total_nutrition.items(), columns=['Nutrient','Amount'])
    fig = px.pie(nutrition_df, 
                values='Amount',
                names='Nutrient',
                color_discrete_sequence=['#ffeb7f', '#ff7f7f', '#7fdbff'])
    
    fig.update_traces(textinfo='percent+label', textfont_size=14)  # Show percentage and label
    fig.update_layout(title_font_size=24, title_font_color='black', 
                        paper_bgcolor='rgba(255, 255, 255, 0)', 
                        plot_bgcolor='rgba(0, 0, 0, 0)', 
                        margin=dict(l=40, r=40, t=40, b=40))  # Adjust margins

    return fig.to_html(full_html=False, include_plotlyjs='cdn')
