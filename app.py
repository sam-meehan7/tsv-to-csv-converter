import streamlit as st
import pandas as pd
import csv
import re
import io

def clean_description(description):
    return re.sub(r'\s+', ' ', description).strip()

def convert_tsv_to_csv(tsv_file):
    # Read TSV file
    df = pd.read_csv(tsv_file, sep='\t')

    # Define the output CSV structure
    output_columns = [
        'id', 'title', 'description', 'availability', 'condition', 'price', 'link', 'image_link',
        'brand', 'google_product_category', 'fb_product_category', 'quantity_to_sell_on_facebook',
        'sale_price', 'sale_price_effective_date', 'item_group_id', 'gender', 'color', 'size',
        'age_group', 'material', 'pattern', 'shipping', 'shipping_weight', 'style[0]'
    ]

    # Create a new DataFrame with the desired structure
    output_df = pd.DataFrame(columns=output_columns)

    # Map the existing columns
    output_df['id'] = df['id']
    output_df['title'] = df['title']
    output_df['description'] = df['description'].apply(clean_description)
    output_df['availability'] = df['availability']
    output_df['condition'] = df['condition']
    output_df['price'] = df['price']
    output_df['link'] = df['link']
    output_df['image_link'] = df['image link']
    output_df['brand'] = df['brand']
    output_df['shipping'] = df['shipping(country)']

    # Convert to CSV
    csv_buffer = io.StringIO()
    output_df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    return csv_buffer

st.title('TSV to CSV Converter')

st.write("""
This app converts a TSV (Tab-Separated Values) file to a CSV (Comma-Separated Values) file
with a specific structure for product data.
""")

uploaded_file = st.file_uploader("Choose a TSV file", type="tsv")

if uploaded_file is not None:
    st.write("File uploaded successfully!")

    if st.button('Convert to CSV'):
        csv_buffer = convert_tsv_to_csv(uploaded_file)

        st.success("Conversion complete!")

        st.download_button(
            label="Download CSV",
            data=csv_buffer.getvalue(),
            file_name="converted_output.csv",
            mime="text/csv"
        )

st.write("""
### Instructions:
1. Upload a TSV file using the file uploader above.
2. Click the 'Convert to CSV' button to process the file.
3. Once conversion is complete, click the 'Download CSV' button to get your converted file.
""")