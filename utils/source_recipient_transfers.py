from openpyxl.worksheet.worksheet import Worksheet

from utils.fund_recipients import FundRecipient
from utils.fund_sources import FundSource

sheet_first_row_index = 4
sheet_sr_transfer_column_offset = 11
sheet_sr_transfer_source_column_index = 0 + sheet_sr_transfer_column_offset
sheet_sr_transfer_include_column_index = 1 + sheet_sr_transfer_column_offset
sheet_sr_transfer_recipient_column_index = 2 + sheet_sr_transfer_column_offset
sheet_sr_transfer_amount_column_index = 3 + sheet_sr_transfer_column_offset
sheet_sr_transfer_color_column_index = 4 + sheet_sr_transfer_column_offset


class SourceRecipientTransfer:
    def __init__(self, source: FundSource, recipient: FundRecipient, amount: float, color: str):
        self.source = source
        self.recipient = recipient
        self.amount = amount
        self.color = color

    def __str__(self):
        return f"SourceRecipientTransfer({self.source}, {self.recipient}, {self.amount}, {self.color})"

    def __repr__(self):
        return self.__str__()


def get_all_source_recipient_transfers(sheet: Worksheet) -> list:
    current_row = 0

    sr_transfers = []

    for row in sheet:
        if current_row < sheet_first_row_index:
            current_row += 1
            continue

        if row[sheet_sr_transfer_include_column_index].value:
            sr_transfers.append(
                SourceRecipientTransfer(
                    source=row[sheet_sr_transfer_source_column_index].value,
                    recipient=row[sheet_sr_transfer_recipient_column_index].value,
                    amount=row[sheet_sr_transfer_amount_column_index].value,
                    color=row[sheet_sr_transfer_color_column_index].value
                )
            )

    return sr_transfers
