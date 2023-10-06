from openpyxl.worksheet.worksheet import Worksheet

sheet_first_row_index = 4
sheet_fund_recipients_column_offset = 4
sheet_fund_recipients_recipient_column_index = 0 + sheet_fund_recipients_column_offset
sheet_fund_recipients_include_column_index = 1 + sheet_fund_recipients_column_offset
sheet_fund_recipients_color_column_index = 2 + sheet_fund_recipients_column_offset
sheet_fund_recipients_total_amount_column_index = 3 + sheet_fund_recipients_column_offset
sheet_fund_recipients_percentage_over_initial_budget_column_index = 5 + sheet_fund_recipients_column_offset


class FundRecipient:
    def __init__(self, name: str, color: str, total_amount: float, percentage_over_initial_budget: float):
        self.name = name
        self.color = color
        self.total_amount = total_amount
        self.percentage_over_initial_budget = percentage_over_initial_budget

    def __str__(self):
        return f"FundRecipient({self.name}, {self.color}, {self.total_amount}, {self.percentage_over_initial_budget})"

    def __repr__(self):
        return self.__str__()


def get_all_fund_recipients(sheet: Worksheet) -> list:
    current_row = 0

    fund_recipients = []

    for row in sheet:
        if current_row < sheet_first_row_index:
            current_row += 1
            continue

        if row[sheet_fund_recipients_include_column_index].value:
            fund_recipients.append(
                FundRecipient(
                    name=row[sheet_fund_recipients_recipient_column_index].value,
                    color=row[sheet_fund_recipients_color_column_index].value,
                    total_amount=row[sheet_fund_recipients_total_amount_column_index].value,
                    percentage_over_initial_budget=row[sheet_fund_recipients_percentage_over_initial_budget_column_index].value
                )
            )

    return fund_recipients
