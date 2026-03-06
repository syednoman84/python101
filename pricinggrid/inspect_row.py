import json
import sys

if len(sys.argv) < 3:
    print('Usage: python inspect_row.py <category> <json_index>')
    print('Example: python inspect_row.py bronze 144')
    sys.exit(1)

category = sys.argv[1]
index = int(sys.argv[2])

with open(f'{category}/{category}.json', 'r') as f:
    data = json.load(f)

if index >= len(data['gridRows']):
    print(f'Error: Index {index} out of range (max: {len(data["gridRows"])-1})')
    sys.exit(1)

row = data['gridRows'][index]
print(f'\nJSON Row at index {index}:')
print(f'  riskTier: {row["riskTier"]}')
print(f'  term: {row["term"]}')
print(f'  inrR: {row["inrR"]}')
print(f'  interestRate: {row["interestRate"]}')
print(f'  annualPercentageInterest: {row["annualPercentageInterest"]}')
print(f'\nFull row:')
print(json.dumps(row, indent=2))
