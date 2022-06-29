import pandas
import pandas as pd
import pyodbc
import requests
import json


def extract_sql_to_csv(table):  # credentials removed as Jonny has already created these CSVs

    # create connection

    def sql_wga_create_connection():
        server = 'wgapowerbi.database.windows.net'
        database = 'powerbi_staging'
        username = 'powerbi'
        password = '<password>>'
        driver = '{ODBC Driver 17 for SQL Server}'
        wgacnxn = pyodbc.connect(
            'DRIVER=' + driver + ';PORT=1433;SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        wgacursor = wgacnxn.cursor()

        return wgacnxn, wgacursor

    wgacnxn, wgacursor = sql_wga_create_connection()

    print('downloading', 'sql', table)

    df = pandas.read_sql(f'select * from dbo.synergy_{table}',wgacnxn)

    print('rows downloaded', len(df))

    output_file_name = 'wga_{}_{}.csv'.format('sql', table.replace(' ', '_').lower())

    df.to_csv(output_file_name)

    print('saved to', output_file_name)


def extract_dataflow_to_csv(dataflow, table):
    url = 'https://api-powerbi.s2ranalytics.com/getjson?workspace=Data Flows_&dataflow={}&table={}&apikey={}&customer=wga'.format(
        dataflow, table, '7tgP2ZuGuj89JHHw')

    print('downloading', dataflow, table)

    response = requests.get(url)
    page = json.loads(response.text)

    df = pd.DataFrame(page)

    print('rows downloaded', len(df))

    output_file_name = 'wga_{}_{}.csv'.format(dataflow.replace(' ', '_').lower(), table.replace(' ', '_').lower())

    df.to_csv(output_file_name)

    print('saved to', output_file_name)


# update this function with the Data Flow and Entity (Table) Name

extracts = ['Reference - Staff Data', 'Reference - Stages Forecast Custom Distribution']

for extract in extracts:
    extract_dataflow_to_csv('Synergy Reports S2R API', extract)

