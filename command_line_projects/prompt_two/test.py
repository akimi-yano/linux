from os import path
import json

# Need to run with Python 3 because the subprocess function we use is not supported in Python 2:
# https://docs.python.org/3/library/subprocess.html#subprocess.getstatusoutput
import subprocess

# Test 1: Invalid BDI files
test_files = [
    "err_dup_field.bdi",
    "err_dup_tran_id.bdi",
    "err_invalid_amount.bdi",
    "err_invalid_format.bdi",
    "err_invalid_recip.bdi",
    "err_invalid_type.bdi",
    "err_no_amount.bdi",
    "err_no_batch.bdi",
    "err_no_bdi.bdi",
    "err_no_desc.bdi",
    "err_no_originator.bdi",
]
# test each error test file
for test_file in test_files:
    # check that the file exists (no typos)
    assert path.exists('tests/{}'.format(test_file))
    # check that the program doesn't complete successfully
    code, _ = subprocess.getstatusoutput('python program.py < tests/{}'.format(test_file))
    assert code != 0


# Test 2: Valid BDI file
code, output = subprocess.getstatusoutput('python program.py < data.bdi'.format(test_file))
assert code == 0
output_dict = json.loads(output)
# check the header information
assert "batch" in output_dict and output_dict["batch"] == "99"
assert "description" in output_dict and output_dict["description"] == "Payroll for January"

# key is a tuple of routing number and account number
# vaule is the expected balance
expected_account_balances = {
    (111222333, 9991): -(10000 + 380100),
    (444555666, 123456): 10000,
    (123456789, 55550): 380100,
    (111222333, 9992): 999,
    (444555666, 8675309): -999
}
# check the account balances
assert "accounts" in output_dict and type(output_dict["accounts"]) == list
for account_dict in output_dict["accounts"]:
    assert "routing_number" in account_dict and\
        "account_number" in account_dict and\
            "net_transactions" in account_dict
    key = int(account_dict["routing_number"]), int(account_dict["account_number"])
    assert expected_account_balances[key] == int(account_dict["net_transactions"])

print("Yay, tests succeeded!")