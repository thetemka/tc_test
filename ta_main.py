import ta_authorize
import ta_actions
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--check_box")
parser.add_argument("--email")
parser.add_argument("--password")
options = parser.parse_args()

email = options.email
state = options.check_box
password = options.password
ta_authorize.authorize(email, password)
ta_actions.actions(email,password)
ta_actions.check_box(state)

