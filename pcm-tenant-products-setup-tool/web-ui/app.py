#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
import subprocess
import os
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).parent.parent
PARAMS_FILE = BASE_DIR / 'params' / 'params.txt'
SCRIPTS_DIR = BASE_DIR / 'scripts'
RESULTS_DIR = BASE_DIR / 'results'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/load-params', methods=['GET'])
def load_params():
    if not PARAMS_FILE.exists():
        return jsonify({'error': 'params.txt not found'}), 404
    
    with open(PARAMS_FILE) as f:
        lines = f.readlines()
    
    params = {}
    products = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if '=' in stripped:
            key, value = stripped.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            if '_Product_' in key:
                parts = key.split('_Product_')
                product_type = parts[0]
                products.append({'type': product_type, 'name': value})
            else:
                params[key] = value
    
    return jsonify({'params': params, 'products': products})

@app.route('/api/save-params', methods=['POST'])
def save_params():
    data = request.json
    
    # Read existing params.txt
    if PARAMS_FILE.exists():
        with open(PARAMS_FILE) as f:
            lines = f.readlines()
    else:
        return jsonify({'error': 'params.txt not found'}), 404
    
    # Set workingDirectory to results
    results_dir = str(RESULTS_DIR)
    
    # Update specific values
    updated_lines = []
    products_line_index = -1
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Track where to insert products
        if stripped == '# List of Products to be created':
            products_line_index = i
            updated_lines.append(line)
            continue
        
        # Skip existing product lines (will be replaced)
        if products_line_index != -1 and '_Product_' in line and '=' in line:
            continue
        
        # Update specific parameters
        if '=' in line and not line.strip().startswith('#'):
            key = line.split('=')[0].strip()
            if key == 'destination_repo_github_url':
                updated_lines.append(f"{key}={data['destRepo']}\n")
            elif key == 'tenant-domain':
                updated_lines.append(f"{key}={data['tenantDomain']}\n")
            elif key == 'tenant-id':
                updated_lines.append(f"{key}={data['tenantId']}\n")
            elif key == 'template_vars_tag':
                updated_lines.append(f"{key}={data['templateTag']}\n")
            elif key == 'pr_title':
                updated_lines.append(f"{key}={data['prTitle']}\n")
            elif key == 'branchName':
                updated_lines.append(f"{key}={data['branchName']}\n")
            elif key == 'workingDirectory':
                # Override workingDirectory to results
                updated_lines.append(f"{key}={results_dir}\n")
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    
    # Insert products after "# List of Products to be created"
    if products_line_index != -1:
        product_counts = {}
        product_lines = []
        
        for product in data['products']:
            ptype = product['type']
            if ptype not in product_counts:
                product_counts[ptype] = 0
            product_counts[ptype] += 1
            product_lines.append(f"{ptype}_Product_{product_counts[ptype]}={product['name']}\n")
        
        # Insert products right after the comment line
        updated_lines = (
            updated_lines[:products_line_index + 1] + 
            product_lines + 
            ['\n'] +
            updated_lines[products_line_index + 1:]
        )
    
    with open(PARAMS_FILE, 'w') as f:
        f.writelines(updated_lines)
    
    return jsonify({'success': True, 'workdir': results_dir})

@app.route('/api/run-setup', methods=['POST'])
def run_setup():
    script = SCRIPTS_DIR / 'PCM_Tenants_Configs_Setup.py'
    if not script.exists():
        return jsonify({'error': 'Setup script not found'}), 404
    
    try:
        result = subprocess.run(
            ['python3', str(script)],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            timeout=300
        )
        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Script execution timed out'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/validate/<script_type>', methods=['POST'])
def validate(script_type):
    script_map = {
        'template_vars': 'validate_template_vars.py',
        'env_files': 'validate_env_files.py',
        'summary': 'print_products_summary.py'
    }
    
    script_name = script_map.get(script_type)
    if not script_name:
        return jsonify({'error': 'Invalid script type'}), 400
    
    script = SCRIPTS_DIR / script_name
    if not script.exists():
        return jsonify({'error': f'{script_name} not found'}), 404
    
    try:
        result = subprocess.run(
            ['python3', str(script)],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            timeout=60
        )
        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/readme', methods=['GET'])
def get_readme():
    readme_file = BASE_DIR / 'README.md'
    if not readme_file.exists():
        return jsonify({'error': 'README.md not found'}), 404
    
    try:
        content = readme_file.read_text(encoding='utf-8')
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting PCM Tenants Configuration Setup Web UI")
    print("📍 Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
