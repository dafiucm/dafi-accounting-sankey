from openpyxl.worksheet.worksheet import Worksheet

g_sheet_first_row_index = 4
sheet_fund_source_source_column_index = 0
sheet_fund_source_include_column_index = 1
sheet_fund_source_color_column_index = 2


class FundSource:
    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def __str__(self):
        return f'IncomeSource({self.name}, {self.color})'

    def __repr__(self):
        return self.__str__()


def get_all_fund_sources(sheet: Worksheet) -> list:
    current_row = 0

    income_sources = []

    for row in sheet:
        if current_row < g_sheet_first_row_index:
            current_row += 1
            continue

        if row[sheet_fund_source_include_column_index].value:
            income_sources.append(
                FundSource(
                    name=row[sheet_fund_source_source_column_index].value,
                    color=row[sheet_fund_source_color_column_index].value
                )
            )

    return income_sources
