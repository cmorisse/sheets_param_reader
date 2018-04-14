# sheets_param_reader
A one liner to get a Google Spreadsheet - shared to all users having the URL - range content as a list of dict.


# Licence 

This is MIT Licensed

# Usage

    import read_sheet
    SPREADSHEET_ID = "..."
    RANGE_NAME = 'Params!A1:N'
    datas = get_params_dict(SPREADSHEET_ID, RANGE_NAME)


