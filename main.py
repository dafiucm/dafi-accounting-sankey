import openpyxl
import plotly.graph_objects as go

from utils.fund_recipients import get_all_fund_recipients
from utils.fund_sources import get_all_fund_sources
from utils.sankey import generate_sankey
from utils.source_recipient_transfers import get_all_source_recipient_transfers

path = '.tmp/Contabilidad DAFI 2023.xlsx'

workbook = openpyxl.load_workbook(path, data_only=True)
workbook.active = workbook['Sankey']

worksheet = workbook.active

g_validation_cell = \
    'Esta hoja permite configurar la generación automática del diagrama de Sankey en el servidor de DAFI. NO TOCAR.'

if worksheet['A1'].value != g_validation_cell:
    raise Exception('Source XLSX data is not valid. Please try again.')

fund_sources = get_all_fund_sources(worksheet)
fund_recipients = get_all_fund_recipients(worksheet)
source_recipient_transfers = get_all_source_recipient_transfers(worksheet)

fig = go.Figure(
    data=[
        generate_sankey(fund_sources, fund_recipients, source_recipient_transfers)
    ]
)

fig.update_layout(
    title_text="Distribución de gasto de la DAFI ejecutado en el ejercicio 2023",
    font_size=12
)

fig.write_html(".tmp/index.html")
