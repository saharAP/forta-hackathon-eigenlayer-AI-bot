from forta_agent import Finding, FindingType, FindingSeverity
stETH_MINT_EVENT = '{"name":"Transfer","type":"event","anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}]}'
stETH_ADDRESS = '0xae7ab96520de3a18e5e111b5eaab095312d7fe84'

stETH_DECIMALS = 18

AMOUNT_THRESHOLD = 0.1


def provide_handle_transaction(amount_threshold):
    def handle_transaction(transaction_event):
        findings = []
        events=transaction_event.filter_log(stETH_MINT_EVENT,stETH_ADDRESS)
        for event in events:
            
            if(event['args']['from']=='0x0000000000000000000000000000000000000000'): #mint stEth tokens
            
                value=event['args']['value']
                stEth_amount=value/10**18
                if (stEth_amount > amount_threshold):
                    findings.append(Finding({
                        'protocol': 'Lido',
                        'name': 'Large stETh Mint',
                        'description': f'{stEth_amount} stEth minted',
                        'alert_id': 'FORTA-7',
                        'type': FindingType.Info,
                        'severity': FindingSeverity.Info,
                        'metadata': {
                        'to': event["args"]["to"],
                        'amount': stEth_amount
                }
            }))
                
        return findings

    return handle_transaction


real_handle_transaction = provide_handle_transaction(AMOUNT_THRESHOLD)


def handle_transaction(transaction_event):
    return real_handle_transaction(transaction_event)