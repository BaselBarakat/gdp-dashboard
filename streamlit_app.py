
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
@st.cache
def load_data(file):
    data = pd.read_csv(file)
    data['from'] = pd.to_datetime(data['from'])
    data['to'] = pd.to_datetime(data['to'])
    return data

# File uploader to read CSV file
st.title('Forecast Data Visualization')
uploaded_file = st.file_uploader('carbon', type='csv')

if uploaded_file is not None:
    df = load_data(uploaded_file)
    
    # Show the dataframe
    st.subheader('Data Preview')
    st.write(df.head())

    # Plotting forecast values over time
    st.subheader('Forecast Visualization')
    fig, ax = plt.subplots()
    ax.plot(df['from'], df['forecast'], marker='o', linestyle='-', color='b')
    ax.set_title('Forecast Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Forecast')
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Displaying additional statistics
    st.subheader('Forecast Statistics')
    st.write(df.describe())

    # Interactive Slider to select a time range
    min_time = df['from'].min()
    max_time = df['from'].max()
    time_range = st.slider('Select Time Range', min_value=min_time, max_value=max_time, value=(min_time, max_time))

    # Filtered Data
    filtered_data = df[(df['from'] >= time_range[0]) & (df['from'] <= time_range[1])]
    st.write(f"Data from {time_range[0]} to {time_range[1]}")
    st.line_chart(filtered_data.set_index('from')['forecast'])

else:
    st.write('Please upload a CSV file to continue.')
