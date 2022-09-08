from playwright.sync_api import Page
from RPA.Excel.Files import Files
from RPA.HTTP import HTTP

def submit_form(config: dict, page: Page) -> Page:

    # Download the SalesData Excel file
    excelFile = config['OutputFolder'] + config['Filenames']['Report']
    HTTP().download(config['SiteUrl'] + config['Filenames']['Report'],
        overwrite=True, target_file=excelFile)

    # Read the Excel sheet into a table
    wb = Files()
    wb.open_workbook(excelFile)
    sales_reps = wb.read_worksheet_as_table(config['SheetName'], header=True)
    wb.close_workbook()

    # For each row in the sheet, enter rep's info and submit
    for rep in sales_reps:
        page.type(config['Selectors']['FirstName'], rep['First Name'])
        page.type(config['Selectors']['LastName'], rep['Last Name'])
        page.type(config['Selectors']['SalesResult'], str(rep['Sales']))
        page.select_option(config['Selectors']['SalesTarget'],
            str(rep['Sales Target']))
        page.click(config['Selectors']['Submit'])
    
    return page