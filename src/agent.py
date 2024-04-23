from .steth_mint_event import handle_transaction as handle_large_mint_event

findings_count = 0


def provide_handle_transaction(handle_large_mint_event):
    def handle_transaction(transaction_event):
        # limiting this agent to emit only 5 findings so that the alert feed is not spammed
        global findings_count
        if findings_count >= 5:
            return []

        findings = handle_large_mint_event(
            transaction_event) 

        findings_count += len(findings)
        return findings

    return handle_transaction


real_handle_transaction = provide_handle_transaction(
    handle_large_mint_event)


def handle_transaction(transaction_event):
    return real_handle_transaction(transaction_event)