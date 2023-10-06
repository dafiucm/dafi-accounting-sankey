from plotly.graph_objs import Sankey
import plotly.graph_objects as go

from utils.color import rgba_to_string, hex_to_rgba
from utils.fund_recipients import FundRecipient
from utils.source_recipient_transfers import SourceRecipientTransfer


def generate_sankey(
        fund_sources: list,
        fund_recipients: list,
        source_recipient_transfers: list,
) -> Sankey:
    nodes = dict()

    for fund_source in fund_sources:
        nodes = append_node(nodes, fund_source)

    for fund_recipient in fund_recipients:
        nodes = append_node(nodes, fund_recipient)

    return go.Sankey(
        valueformat=".2f",
        valuesuffix=" €",
        node=dict(
            pad=35,
            thickness=30,
            line=dict(color="black", width=0),
            label=inline_labels(nodes),
            color=inline_colors(nodes)
        ),
        link=dict(
            source=inline_source_nodes(nodes, source_recipient_transfers),
            target=inline_target_nodes(nodes, source_recipient_transfers),
            value=inline_values(source_recipient_transfers),
            color=inline_link_colors(source_recipient_transfers),
            customdata=inline_custom_data(source_recipient_transfers),
            hovertemplate='"%{target.label}" recibe de "%{source.label}" un total de %{value}.'  # TODO: use %{customdata[index]}
        )
    )


def append_node(nodes: dict, content) -> dict:
    node_id = len(nodes)
    nodes[node_id] = {
        'content': content,
        'id': node_id
    }
    return nodes


def find_node_by_name(nodes: dict, name: str) -> dict:
    for node in nodes.values():
        if node['content'].name == name:
            return node
    raise Exception('Node not found')


def inline_labels(nodes: dict) -> list:
    labels = []

    for node in nodes.values():
        content = node['content']
        if isinstance(content, FundRecipient):
            label = f"<b>{content.name}</b><br />" \
                    f"{content.total_amount} €<br />" \
                    f"{content.percentage_over_initial_budget:.2%}"
        else:
            label = f"<b>{content.name}</b>"
        labels.append(label)

    return labels


def inline_colors(nodes: dict) -> list:
    colors = []

    for node in nodes.values():
        colors.append(node['content'].color)

    return colors


def inline_source_nodes(nodes: dict, sr_transfers: list) -> list:
    source_nodes = []

    for sr_transfer in sr_transfers:
        source_nodes.append(find_node_by_name(nodes, sr_transfer.source)['id'])

    return source_nodes


def inline_target_nodes(nodes: dict, sr_transfers: list) -> list:
    target_nodes = []

    for sr_transfer in sr_transfers:
        target_nodes.append(find_node_by_name(nodes, sr_transfer.recipient)['id'])

    return target_nodes


def inline_values(sr_transfers: list) -> list:
    amounts = []

    for sr_transfer in sr_transfers:
        amounts.append(sr_transfer.amount)

    return amounts


def inline_custom_data(sr_transfers: list) -> list:
    custom_data = []

    for sr_transfer in sr_transfers:
        custom_data.append([])  # TODO: fill with actual data

    return custom_data


def inline_link_colors(sr_transfers: list) -> list:
    colors = []

    for sr_transfer in sr_transfers:
        colors.append(rgba_to_string(hex_to_rgba(sr_transfer.color, 0.2)))

    return colors
