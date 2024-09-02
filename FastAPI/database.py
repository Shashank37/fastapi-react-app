import json

import pandas as pd

df = pd.read_csv(
    r"C:\Users\ShashankMauli\Documents\MINI PROJECTS\webdev\Frontend Streamlit App\csv to json using python\LEAF_KPI_CSV.csv")

filtered_sector = df[(df['SECTOR'] == 'Automobile')]

distinct_classification_list = filtered_sector['CLASSIFICATION'].unique()

#print(distinct_classification_list)

for classification in distinct_classification_list:
    department_df = filtered_sector[(filtered_sector['CLASSIFICATION'] == classification)]
    distinct_department_list = department_df['DEPARTMENT'].unique()
    for dept in distinct_department_list:
        subdepartment_df = department_df[(filtered_sector['DEPARTMENT'] == dept)]
        distinct_subdepartment_list = subdepartment_df['SUBDEPARTMENT'].unique()
        for subdept in distinct_subdepartment_list:
            kpis_df = subdepartment_df[(filtered_sector['SUBDEPARTMENT'] == subdept)]
            distinct_kpis_list = kpis_df['KPIS'].unique()
            # print(distinct_kpis_list)
            key = classification + '+' + dept + '+' + subdept
            file_prefix = r'C:\\Users\\ShashankMauli\\Documents\\GitHub\\fastapi-react-app\\FastAPI\\segregated_kpis\\'
            filename = file_prefix + key.replace(" ", "") + ".json"
            segregated_kpis_data = {key: kpis_df.to_dict(orient='records')}
            print (segregated_kpis_data)
            # print (kpis_df.to_dict(orient='records'))
            # print(kpis_df.to_json(orient="records", indent=4))
            # data = json.dumps(segregated_kpis_data, ensure_ascii=False, sort_keys=True, separators=(',', ': '))
            # data = json.dumps(segregated_kpis_data, ensure_ascii=False, sort_keys=True, separators=(',', ': '))
            with open(filename, 'w', encoding='utf-8') as outfile:
                # with open(filename, 'w', encoding='utf-8') as outfile:
                json.dump(segregated_kpis_data, outfile, ensure_ascii=False, separators=(',', ': '))
            # break
        # break
    # break