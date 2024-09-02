import json

import pandas as pd

df = pd.read_csv(
    r"C:\Users\ShashankMauli\Documents\MINI PROJECTS\webdev\Frontend Streamlit App\csv to json using python\LEAF_KPI_CSV.csv")

filtered_sector = df[(df['SECTOR'] == 'Automobile')]

df_structure = {
    "SECTOR": [
        {
            "Automobile": {
                "CLASSIFICATION": [
                    {}
                ]
            }
        }
    ]
}

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

# print(distinct_classification_list)

for classification in distinct_classification_list:
    department_df = filtered_sector[(filtered_sector['CLASSIFICATION'] == classification)]
    distinct_department_list = department_df['DEPARTMENT'].unique()
    key = classification
    file_prefix = r'C:\\Users\\ShashankMauli\\Documents\\GitHub\\fastapi-react-app\\FastAPI\\segregated_kpis\\'
    filename = file_prefix + key.replace(" ", "") + ".json"
    segregated_classification_data = {key: department_df.to_dict(orient='records')}
    # print(segregated_classification_data)

    # temporary_classification_dict = {classification: department_df.to_dict(orient='records')}

    # temporary_classification_dict = {classification: list_department}

    temporary_classification_dict = {}
    list_department = []

    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(segregated_classification_data, outfile, ensure_ascii=False, separators=(',', ': '))
    # list_classification = df_structure["SECTOR"][0]["CLASSIFICATION"]


    for dept in distinct_department_list:
        subdepartment_df = department_df[(filtered_sector['DEPARTMENT'] == dept)]
        distinct_subdepartment_list = subdepartment_df['SUBDEPARTMENT'].unique()

        temporary_dept_dict = {}
        list_subdepartment = []
        key = classification + '+' + dept
        file_prefix = r'C:\\Users\\ShashankMauli\\Documents\\GitHub\\fastapi-react-app\\FastAPI\\segregated_kpis\\'
        filename = file_prefix + key.replace(" ", "") + ".json"
        segregated_department_data = {key: subdepartment_df.to_dict(orient='records')}
        # print(segregated_department_data)

        # temporary_dept_dict = {dept: list_subdepartment}


        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(segregated_department_data, outfile, ensure_ascii=False, separators=(',', ': '))

        for subdept in distinct_subdepartment_list:
            kpis_df = subdepartment_df[(filtered_sector['SUBDEPARTMENT'] == subdept)]
            distinct_kpis_list = kpis_df['KPIS'].unique()
            # print(distinct_kpis_list)

            temporary_subdept_dict = {}

            key = classification + '+' + dept + '+' + subdept
            file_prefix = r'C:\\Users\\ShashankMauli\\Documents\\GitHub\\fastapi-react-app\\FastAPI\\segregated_kpis\\'
            filename = file_prefix + key.replace(" ", "") + ".json"
            segregated_kpis_data = {key: kpis_df.to_dict(orient='records')}
            # print(segregated_kpis_data)

            temporary_subdept_dict = {subdept: kpis_df.to_dict(orient='records')}

            # print (kpis_df.to_dict(orient='records'))
            # print(kpis_df.to_json(orient="records", indent=4))
            # data = json.dumps(segregated_kpis_data, ensure_ascii=False, sort_keys=True, separators=(',', ': '))
            # data = json.dumps(segregated_kpis_data, ensure_ascii=False, sort_keys=True, separators=(',', ': '))
            with open(filename, 'w', encoding='utf-8') as outfile:
                # with open(filename, 'w', encoding='utf-8') as outfile:
                json.dump(segregated_kpis_data, outfile, ensure_ascii=False, separators=(',', ': '))
            # break
            list_subdepartment.append(temporary_subdept_dict)
        # break
        # list_department.append(temporary_dept_dict)

        y = {
            dept: {
                "SUBDEPARTMENT": list_subdepartment
            }
        }

        # internal_dept_dict = {"SUBDEPARTMENT": list_subdepartment}
        # temporary_dept_dict = {dept: internal_dept_dict}
        # list_department.append(temporary_dept_dict)
        list_department.append(y)
    # break
    # list_classification.append(segregated_classification_data)

    x = {
        classification: {
            "DEPARTMENT": list_department
        }
    }

    # internal_classification_dict = {"DEPRATMENT": list_department}
    # list_classification.append(temporary_classification_dict)
    # temporary_classification_dict = {classification: internal_classification_dict}
    # list_classification.append(temporary_classification_dict)
    list_classification.append(x)

internal_sector_dict = {"CLASSIFICATION": list_classification}
df_schema = {
    "SECTOR": [{
        "Automobile": internal_sector_dict
    }]
}

print ("len(df_schema[\"SECTOR\"]): ", len(df_schema["SECTOR"]))

print ("df_schema[\"SECTOR\"][0][\"Automobile\"][\"CLASSIFICATION\"]: ", len(df_schema["SECTOR"][0]["Automobile"]["CLASSIFICATION"]))

print ("df_schema[\"SECTOR\"][0][\"Automobile\"][\"CLASSIFICATION\"][0][\"Product Development\"][\"DEPARTMENT\"]: ", len(df_schema["SECTOR"][0]["Automobile"]["CLASSIFICATION"][0]["Product Development"]["DEPARTMENT"]))

print ("df_schema[\"SECTOR\"][0][\"Automobile\"][\"CLASSIFICATION\"][0][\"Product Development\"][\"DEPARTMENT\"][0][\"Research and Development\"][\"SUBDEPARTMENT\"][0][\"Concept Development\"]: ", len(df_schema["SECTOR"][0]["Automobile"]["CLASSIFICATION"][0]["Product Development"]["DEPARTMENT"][0]["Research and Development"]["SUBDEPARTMENT"][0]["Concept Development"]))


with open("nested_json_structure.json", 'w', encoding='utf-8') as outfile:
    json.dump(df_schema, outfile, ensure_ascii=False, separators=(',', ': '))
