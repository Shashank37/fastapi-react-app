import json

import pandas as pd

df = pd.read_csv(
    r"C:\Users\ShashankMauli\Documents\MINI PROJECTS\webdev\Frontend Streamlit App\csv to json using python\LEAF_KPI_CSV.csv")

df_schema = {
    "SECTOR": [{
        "Automobile" : {}
    }]
}

list_classification = []
list_department = []
list_subdepartment = []


filtered_sector = df[(df['SECTOR'] == 'Automobile')]
distinct_classification_list = filtered_sector['CLASSIFICATION'].unique()

