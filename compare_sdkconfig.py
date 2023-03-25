import argparse
import re

# Parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('sdkconfig_file', help='the path to the SDKConfig file')
parser.add_argument('default_file', help='the path to the default SDKConfig file')
args = parser.parse_args()

# Dictionary to store default values
defaults = {}

# Open the default SDKConfig file for reading
with open(args.default_file, 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Split the contents of the file into lines
dft_lines = contents.split('\n')

# Loop through each line in the file
for dft_line in dft_lines:
    # Check if the line is a configuration setting
    if dft_line.startswith('CONFIG_'):
        # Split the line into a key and a value
        key, value = re.split('=| ', dft_line)[0:2]
        defaults[key] = value
    else:
        result = re.search(r"^# ([A-Z\_]*) is not set", dft_line)
        if result:
            key = result.group(1)
            defaults[key] = 'n'

# Open the SDKConfig compare file for reading
with open(args.sdkconfig_file, 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Split the contents of the compare file into lines
cmp_lines = contents.split('\n')

# Dictionary to store non-default values
non_defaults = {}
lst_defaults = {}

# Loop through each line in the file
for cmp_line in cmp_lines:
    # Check if the line is a configuration setting
    if cmp_line.startswith('CONFIG_'):
        # Split the line into a key and a value
        key, value = re.split('=| ', cmp_line)[0:2]
        # Check if the value is different from the default
        if key in defaults and value != defaults[key]:
            non_defaults[key] = value
            lst_defaults[key] = defaults[key]

# Print the non-default values
for key, value in non_defaults.items():
    print(key + ': ' + value + ' (Default=' + lst_defaults[key] + ')')
