import json
import csv
import os
from datetime import datetime

def load_csv(category):
    rates = {}
    with open(f'{category}/{category}.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Key']:
                rates[row['Key']] = row['Value']
    return rates

def load_json(category):
    with open(f'{category}/{category}.json', 'r') as f:
        return json.load(f)

def percent_to_decimal(percent_str):
    return round(float(percent_str.strip('%')) / 100, 4)

def normalize_percent(percent_str):
    return str(float(percent_str.strip('%'))) + '%'

def validate(category):
    """Validate pricing data. JSON index refers to the position in gridRows array."""
    rates = load_csv(category)
    data = load_json(category)
    
    errors = []
    terms = [60, 84, 120, 144, 180]
    
    for tier in range(1, 7):
        for term in terms:
            key = f'Tier{tier}_{term}_Terms'
            expected_inrR = rates.get(key)
            
            if not expected_inrR:
                errors.append(f'Missing {key} in CSV')
                continue
            
            expected_decimal = percent_to_decimal(expected_inrR)
            
            matching_rows = [(i, r) for i, r in enumerate(data['gridRows']) if r['riskTier'] == tier and r['term'] == term]
            
            if not matching_rows:
                errors.append(f'No gridRows found for riskTier={tier}, term={term}')
                continue
            
            for idx, (json_idx, row) in enumerate(matching_rows):
                if normalize_percent(row['inrR']) != normalize_percent(expected_inrR):
                    errors.append(f'Tier{tier}_Term{term} Row{idx} (JSON index {json_idx}): inrR mismatch - expected {expected_inrR}, got {row["inrR"]}')
                
                if round(row['interestRate'], 4) != expected_decimal:
                    errors.append(f'Tier{tier}_Term{term} Row{idx} (JSON index {json_idx}): interestRate mismatch - expected {expected_decimal}, got {row["interestRate"]}')
                
                if round(row['annualPercentageInterest'], 4) != expected_decimal:
                    errors.append(f'Tier{tier}_Term{term} Row{idx} (JSON index {json_idx}): annualPercentageInterest mismatch - expected {expected_decimal}, got {row["annualPercentageInterest"]}')
    
    return errors

if __name__ == '__main__':
    print('Select category:')
    print('1. Gold')
    print('2. Silver')
    print('3. Bronze')
    
    choice = input('Enter choice (1-3): ').strip()
    
    categories = {'1': 'gold', '2': 'silver', '3': 'bronze'}
    category = categories.get(choice)
    
    if not category:
        print('Invalid choice')
        exit(1)
    
    if not os.path.exists(category):
        print(f'Directory {category} does not exist')
        exit(1)
    
    print(f'\nValidating {category}...\n')
    errors = validate(category)
    
    output_file = f'{category}/validation_errors.txt'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(output_file, 'w') as f:
        f.write(f'Validation Report - {category.upper()}\n')
        f.write(f'Timestamp: {timestamp}\n')
        f.write('=' * 60 + '\n')
        f.write('Note: JSON index refers to the position in the gridRows array\n')
        f.write('=' * 60 + '\n\n')
        
        if errors:
            f.write(f'Found {len(errors)} error(s):\n\n')
            for error in errors:
                f.write(f'  - {error}\n')
            print(f'Found {len(errors)} error(s) - saved to {output_file}')
        else:
            f.write('✓ All validations passed!\n')
            print(f'✓ All validations passed! - report saved to {output_file}')
