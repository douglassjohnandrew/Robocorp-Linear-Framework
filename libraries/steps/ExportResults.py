from playwright.sync_api import Page
from xhtml2pdf import pisa

def export_results(config: dict, page: Page) -> Page:

    # Save image of the sales summary
    page.locator(config['Selectors']['Summary']).screenshot(
        path=config['OutputFolder'] + config['Filenames']['Summary'])
    
    # Get the sales results as an HTML table
    sales_html = page.locator(config['Selectors']['Results']).evaluate(
        config['OuterHTML'])

    # Save the HTML table to a PDF file
    pdf_file = open(config['OutputFolder'] +
        config['Filenames']['Results'], 'w+b')
    pisa.CreatePDF(sales_html, dest=pdf_file)
    pdf_file.close()

    return page