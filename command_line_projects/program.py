import sys
import json

# read in the text  file contents from stdin
file_contents = sys.stdin.read()



# split the sections based on the "=="
sections = file_contents.split('\n==\n')  
transactions = {}
for section in sections:
    # print("=============Section============")

    if '/*BDI*/' in section:
        if 'Batch' in section.split('\n')[1]:
            batch = int(section.split('\n')[1][len('Batch:'):])
        if 'Description' in section.split('\n')[2]:
            description = section.split('\n')[2][len('Description:'):]
        continue
    
    for s in section.split('\n'):
        if 'Originator' in s:
            temp_o = s[len('Originator:'):].split('/')
            originater_routing = temp_o[0]
            originater_account = temp_o[1]
            
        elif 'Recipient' in s:
            temp_r = s[len('Recipient:'):].split('/')
            recipient_routing = temp_r[0]
            recipient_account = temp_r[1]
            
        elif 'Type' in s:
            if 'Credit' in s[len('Type:'):]:
                credit = True
            elif 'Debit' in s[len('Type:'):]:
                credit = False
                
        elif 'Amount' in s: 
            amount = s[len('Amount:'):]

    if credit == True:
        if (originater_routing, originater_account) not in transactions:
            transactions[(originater_routing, originater_account)] = 0
        transactions[(originater_routing, originater_account)] += (int(amount)*(-1))
        if (recipient_routing, recipient_account) not in transactions:                
            transactions[(recipient_routing, recipient_account)] = 0
        transactions[(recipient_routing, recipient_account)] += (int(amount))
    elif credit == False:
        if (recipient_routing, recipient_account) not in transactions:
            transactions[(recipient_routing, recipient_account)] = 0
        transactions[(recipient_routing, recipient_account)] += (int(amount)*(-1))
        if (originater_routing, originater_account) not in transactions:
            transactions[(originater_routing, originater_account)] = 0
        transactions[(originater_routing, originater_account)] += (int(amount))

test_obj = {
    "batch": batch,
    "description": description,
    "accounts": []
}

for key,net in transactions.items():
    routing,account = key
    test_obj["accounts"].append({"routing_number":str(routing),"account_number":str(account),"net_transactions":str(net)})

# sort keys,  and set indentation for prettier formatting
obj = json.dumps(test_obj, sort_keys=True, indent=4)
print(obj)




