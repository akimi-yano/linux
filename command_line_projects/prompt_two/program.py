import sys
import json


# make into key-value pairs
def make_key_values(text):
    result = {}
    # process each line in the input text
    for line in text.split('\n'):
        # there might be empty lines in the data
        if line.strip() == '':
            continue
        # split the line on the first ":"
        key_value_split = line.split(':', 1)
        if len(key_value_split) < 2:
            # print(key_value_split)
            raise Exception('*** ERROR: The data not following the format of Field : value ***')
        key, value = key_value_split[0].strip(), key_value_split[1].strip()
        if key in result:
            raise Exception('*** ERROR: There is at least one duplicated field ***')
        result[key] = value
    return result


# read the header section
def read_header(text):
    key_values = make_key_values(text)
    if 'Batch' not in key_values:
        raise Exception('*** ERROR: "Batch" is not specified ***')
    if 'Description' not in key_values:
        raise Exception('*** ERROR: "Description" is not specified ***')
    return key_values['Batch'], key_values['Description']


# read the transaction section
def read_transaction(text):
    key_values = make_key_values(transaction_text)
    # check that we have all the fields we need
    if 'Originator' not in key_values:
        raise Exception('*** ERROR: "Originator" is not specified ***')
    if 'Recipient' not in key_values:
        raise Exception('*** ERROR: "Recipient" is not specified ***')
    if 'Type' not in key_values:
        raise Exception('*** ERROR: "Type" is not specified ***')
    if 'Amount' not in key_values:
        raise Exception('*** ERROR: "Amount" is not specified ***')
    if 'Transaction' not in key_values:
        raise Exception('*** ERROR: "Transaction" is not specified ***')

    originator_split = key_values['Originator'].split('/')
    if len(originator_split) != 2:
        raise Exception('*** ERROR: "Originator" information is missing ***')
    originator_routing = originator_split[0].strip()
    originator_account = originator_split[1].strip()

    recipient_split = key_values['Recipient'].split('/')
    if len(recipient_split) != 2:
        raise Exception('*** ERROR: "Recipient" information is missing ***')
    recipient_routing = recipient_split[0].strip()
    recipient_account = recipient_split[1].strip()

    trans_type = key_values['Type']
    credit = True
    if trans_type == 'Credit':
        credit = True
    elif trans_type == 'Debit':
            credit = False
    else:
        raise Exception('*** ERROR: Only "Credit" or "Debit" can be valid input options for "Type" ***')

    amount = key_values['Amount']
    try:
        amount = int(amount)
    except ValueError:
        raise Exception('*** ERROR: "Amount" input is invalid ***')
    
    transaction = key_values['Transaction']
    
    return ((originator_routing, originator_account),
            (recipient_routing, recipient_account),
            credit,
            amount,
            transaction
    )


################ Main Program ################

# Step 1: read in the text file contents from stdin
all_text = sys.stdin.read()

# Step 2: check the first line
first_line_split = all_text.split('\n', 1)
if first_line_split[0].strip() != '/*BDI*/':
    raise Exception('*** ERROR: The file type /*BDI*/ is not specified ***')

# Step 3: split the rest of the file using ==
rest_text = first_line_split[1]
sections = rest_text.split('\n==\n')

# Step 4: read the header section
batch, description = read_header(sections[0])

# Step 5: read and process each transaction
transactions = {}
transaction_ids = set([])
for transaction_text in sections[1:]:
    orig_key, recip_key, credit, amount, trans_id = read_transaction(transaction_text)
    # make sure transactions are unique
    if trans_id in transaction_ids:
        raise Exception('*** ERROR: There is at least one duplicated transaction ID ***')
    transaction_ids.add(trans_id)
    # have a multiplier to "flip" the calculation depending on the transaction type
    multiplier = 1
    if not credit:
        multiplier = -1

    if orig_key not in transactions:
        transactions[orig_key] = 0
    if recip_key not in transactions:
        transactions[recip_key] = 0
    transactions[orig_key] -= multiplier * amount
    transactions[recip_key] += multiplier * amount

# Step 6: create the json dictionary
json_dict = {
    "batch": batch,
    "description": description,
    "accounts": []
}

# step 7: read from transactions and update json_dict
for key, net in transactions.items():
    routing, account = key
    json_dict["accounts"].append({
        "routing_number":str(routing),
        "account_number":str(account),
        "net_transactions":str(net)
    })

# set indentation for prettier formatting
obj = json.dumps(json_dict, indent=4)
print(obj)




