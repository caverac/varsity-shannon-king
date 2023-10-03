# Display a hello message with the current time
import datetime
import argparse

# create a parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "-n",
    "--name",
    default="shannon",
    help="👉 the name that will be displayed on the screen",
)

parser.add_argument(
    "-d",
    "--date",
    default="now",
    help="⏰ which time should be use to be displayed",
)

options = parser.parse_args()

name = options.name

if options.date == "now":
    date = datetime.datetime.now()
else:
    date = options.date


# message = "hello " + name + " date"
message = f"hello {name} [{date}]"

print(message)
