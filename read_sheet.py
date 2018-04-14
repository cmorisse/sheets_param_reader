# coding: utf-8
from __future__ import print_function
import os, sys
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from google_auth_oauthlib.flow import InstalledAppFlow


try:
    SHEET_READER_API_KEY = os.environ['SHEET_READER_API_KEY']
except KeyError:
    print("Error: Environment variable 'SHEET_READER_API_KEY' is not defined.")
    sys.exit(1)
    

SPREADSHEET_SERVICE = build('sheets', 'v4', developerKey=SHEET_READER_API_KEY)


def get_params_dict(spreadsheet_id, range_name):
    """ returns a Google Sheet range as a dict
    :param spreadsheet_id: Google sheet id. It's found in the URL after the "/d/"
        and before "/edit.../"
        Example: For https://docs.google.com/spreadsheets/d/1KsDIX5WeExxxxxxxxxxxxxxxIXV1_OFlbGKH5eFKr3g/edit#gid=0
        sheet id is '1KsDIX5WeExxxxxxxxxxxxxxxIXV1_OFlbGKH5eFKr3g'
    :type spreadsheet_id: str
    
    :param range_name: The cell's range (including sheet name) that holds data 
        to return as dict.
        Type a formula in Google sheet to get it.
        Example: 'Params!A1:N' where Params is the sheet name.
    :type range_name: str
    
    :returns: a list of dict.
    """
    result = SPREADSHEET_SERVICE.spreadsheets().values()\
        .get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    if not values:
        return []
    
    header_line = values[0]
    data_lines = values[1:]
    results = []
    for line_num, row in enumerate(data_lines):
        ld = {'_line_number': line_num}
        for idx, val in enumerate(header_line):
            try:
                ld[val] = row[idx] or None
            except IndexError:
                ld[val] = None
        results.append(ld)
    return results

if __name__ == '__main__':
    """Google sheet identified by SPREADSHEET_ID must be shared
       in readonly to all non identified users knowing the URL.
    """
    SPREADSHEET_ID = sys.argv[1]
    RANGE_NAME = 'Params!A1:N'
    datas = get_params_dict(SPREADSHEET_ID, RANGE_NAME)
    print(datas)    
