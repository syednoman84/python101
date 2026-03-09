# Scripts Directory

This directory contains all Python automation scripts for PCM Tenants Configuration Setup.

## Scripts

- **PCM_Tenants_Configs_Setup.py** - Main automation script that sets up tenant configurations
- **validate_template_vars.py** - Validates template variables are copied correctly
- **validate_env_files.py** - Validates environment files have correct tenant values
- **print_products_summary.py** - Displays summary of all created products

## Usage

Run scripts directly:
```bash
cd pcm-tenant-products-setup-tool
python3 scripts/PCM_Tenants_Configs_Setup.py
python3 scripts/validate_template_vars.py
python3 scripts/validate_env_files.py
python3 scripts/print_products_summary.py
```

Or use the web UI which calls these scripts automatically.

All scripts read configuration from `params/params.txt` and generate output in `results/`.
