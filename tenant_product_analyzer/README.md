# 🔍 Tenant Product Analyzer

A Python script that scans tenant configuration repositories to extract and analyze product definitions across multiple tenants.

## 📋 Overview

This tool automates the process of discovering and cataloging products across all tenant repositories in the `odx-platform-configs` organization. It clones repositories, scans for product definitions, and generates comprehensive reports.

## ✨ Features

- 🔄 Fetches repositories from GitHub Enterprise using `gh` CLI
- 🔎 Scans each repository for product configurations
- 📊 Extracts product metadata from `definition.json` files
- 📝 Generates three types of reports:
  - Detailed JSON report with all product definitions
  - Summary report showing product counts by tenant
  - Breakdown report showing product type distribution

## 🛠️ Prerequisites

- Python 3.6+
- GitHub CLI (`gh`) installed and authenticated
- Access to `git.shared.linearft.tools`

### 💻 Installing GitHub CLI

```bash
# macOS
brew install gh

# Authenticate with your GitHub Enterprise instance
gh auth login --hostname git.shared.linearft.tools
```

## 📁 Repository Structure

The script expects tenant repositories to follow this structure:

```
tenant-repo/
└── product/
    ├── <uuid-1>/
    │   └── definition.json
    ├── <uuid-2>/
    │   └── definition.json
    └── ...
```

Each `definition.json` contains:
```json
{
  "productId": "uuid",
  "productName": "Product Name",
  "productType": "PRODUCT_TYPE",
  "policy": "policy-name",
  "selfServiceManaged": true/false
}
```

## 🚀 Usage

### ▶️ Basic Usage

Scan all repositories (up to 1000):
```bash
python3 tenant_product_analyzer.py
```

### 🔢 Limit Number of Repositories

Scan only 5 repositories:
```bash
python3 tenant_product_analyzer.py 5
```

### 💾 Keep Cloned Repositories

By default, cloned repositories are deleted after scanning. To keep them:
```bash
python3 tenant_product_analyzer.py 10 false
```

### ⚙️ Parameters

1. **Limit** (optional, default: 1000)
   - Number of repositories to fetch and scan
   
2. **Cleanup** (optional, default: true)
   - `true`: Delete cloned repositories after scanning
   - `false`: Keep cloned repositories in `temp_repos/` directory

## 📄 Generated Reports

### 1️⃣ product_definitions.json

Detailed JSON report containing all product definitions grouped by repository.

**Format:**
```json
{
  "ODXP-DPLOY--odx-config-tenant1-deploy": [
    {
      "productId": "uuid",
      "productName": "Product Name",
      "productType": "CONSUMER_DAO",
      "policy": "amt-consumer-dao-policy",
      "selfServiceManaged": true
    }
  ]
}
```

### 2️⃣ products_count_by_tenant.txt

Summary report showing total product count per tenant, sorted by repository name.

**Format:**
```
S. No.    Repo Name                                                   Total Products 
=====================================================================================
1         ODXP-DPLOY--odx-config-tenant1-deploy                       13             
2         ODXP-DPLOY--odx-config-tenant2-deploy                       25             
```

### 3️⃣ product_type_count_by_tenant.txt

Detailed breakdown showing count of each product type per tenant, sorted by repository name.

**Format:**
```
S. No.    Repo Name                                                   Product Type                            Count     
========================================================================================================================
1         ODXP-DPLOY--odx-config-tenant1-deploy                       CONSUMER_DAO                            10        
2         ODXP-DPLOY--odx-config-tenant1-deploy                       SMB_DAO                                 3         
```

## ⚙️ Configuration

### 🚫 Excluded Repositories

The script excludes certain repositories from scanning. To modify the exclusion list, edit the `EXCLUDE_REPOS` variable in the script:

```python
EXCLUDE_REPOS = ["ODXP-DPLOY--odx-config-platform-deploy"]
```

### 🏢 Organization and Host

To scan a different organization or GitHub Enterprise instance, modify these variables:

```python
ORG = "odx-platform-configs"
GH_HOST = "git.shared.linearft.tools"
```

## 🔄 How It Works

1. **🔍 Fetch Repositories**: Uses `gh` CLI to list all repositories in the organization
2. **🔀 Filter**: Excludes repositories in the `EXCLUDE_REPOS` list
3. **📥 Clone**: Performs shallow clone (`--depth 1`) of each repository
4. **🔎 Scan**: Looks for `product/` directory and iterates through UUID subdirectories
5. **📤 Extract**: Reads `definition.json` from each product directory
6. **📊 Aggregate**: Collects all product data grouped by repository
7. **📝 Generate Reports**: Creates three report files with different views of the data
8. **🧹 Cleanup**: Optionally removes cloned repositories

## 💡 Examples

### Scan first 10 repositories and keep clones for inspection
```bash
python3 tenant_product_analyzer.py 10 false
```

### Full scan with automatic cleanup
```bash
python3 tenant_product_analyzer.py
```

### Quick test with 1 repository
```bash
python3 tenant_product_analyzer.py 1 false
```

## 📤 Output Example

```
Fetching repositories from odx-platform-configs (limit: 5)...
Found 5 repositories

Scanning ODXP-DPLOY--odx-config-tenant1-deploy...
  Found 13 product(s)
Scanning ODXP-DPLOY--odx-config-tenant2-deploy...
  Found 25 product(s)

Product Definitions Report is saved to product_definitions.json
Products Count by Tenant Report is saved to products_count_by_tenant.txt
Product Type Count by Tenant Report is saved to product_type_count_by_tenant.txt
Total repositories with products: 2
Total products found: 38
```

## 🔧 Troubleshooting

### 🔐 Authentication Issues
```bash
# Re-authenticate with GitHub Enterprise
gh auth login --hostname git.shared.linearft.tools
```

### ❌ No Repositories Found
- Verify you have access to the organization
- Check that `GH_HOST` is set correctly
- Ensure `gh` CLI is properly authenticated

### ⚠️ Missing Products
- Verify repository structure matches expected format
- Check that `definition.json` files exist in product directories
- Ensure JSON files are valid

## 📌 Notes

- ⚠️ Reports are overwritten on each run - backup previous reports if needed
- ⚡ Shallow clones are used for efficiency (only latest commit)
- 📂 Only repositories with a `product/` directory are included in reports
- 🔇 Invalid JSON files are silently skipped
