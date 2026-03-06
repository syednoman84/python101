# 🛠️ PCM Tenants Configuration Setup

Automated setup scripts for creating and validating PCM tenant configurations with multiple product types.

## 📋 Overview

This toolkit automates the process of setting up tenant configurations by cloning repositories, creating product directories, copying template variables, and generating configuration files. It includes validation scripts to verify the setup was completed correctly.

## 📂 Files

### 1️⃣ PCM_Tenants_Configs_Setup.py
**🚀 Main automation script** that performs the complete tenant setup.

**What it does:**
- 📥 Clones destination tenant config repository
- 🌱 Creates a new feature branch
- 📄 Clones static files repository and copies baseline files (app, env, .gitignore)
- 🔄 Replaces tenant placeholders in environment files
- 🏷️ Clones template variables repository at specified tag
- 📁 Creates product directories with UUID-based names
- 📊 Copies appropriate template_vars for each product type
- 📝 Generates definition.json for each product
- ✅ Commits all changes and pushes to remote
- 📤 Creates a Pull Request
- 📊 Prints summary with full definition.json for each product

**Usage:**
```bash
python PCM_Tenants_Configs_Setup.py
```

### 2️⃣ print_product_summary.py
**✅ Validation script** to view all created products and their definitions.

**What it does:**
- 🔍 Scans the product directory for all UUID-based product folders
- 📝 Reads definition.json from each product directory
- 📊 Displays formatted summary with complete definition.json content
- 🔢 Sorts products by type and name

**Usage:**
```bash
python print_product_summary.py
```

**When to use:**
- ✅ After running the main setup script
- 🔍 To verify product definitions without re-running setup
- 👀 To review what products were created
- 🔁 Can be run multiple times

### 3️⃣ validate_template_vars.py
**✅ Validation script** to verify template_vars were copied correctly.

**What it does:**
- 🔍 Compares each product's template_vars directory with source default-variables
- 📂 Groups results by product type
- ✅ Checks for missing files, extra files, and JSON content differences
- 📊 Reports success/failure for each product

**Usage:**
```bash
python validate_template_vars.py
```

**When to use:**
- ✅ After running the main setup script
- 🔍 To verify the copy process was successful
- ✅ To ensure correct template_vars were used for each product type
- 🔁 Can be run multiple times

### 4️⃣ validate_env_files.py
**✅ Validation script** to verify environment file placeholder replacements.

**What it does:**
- 🔍 Validates serenityprdpr.json and serenityprod1.json
- 🔎 Checks for unreplaced placeholders (<tenant-domain>, <tenant-id>)
- ✅ Verifies exact tenant values are present (no typos, extra characters, or spaces)
- ⚠️ Detects common issues like:
  - "vnb1" instead of "vnb"
  - "vnb " (trailing space)
  - "vnb /" (space before slash)
- Reports specific issues with file paths and values

**Usage:**
```bash
python validate_env_files.py
```

**When to use:**
- ✅ After running the main setup script
- 🔍 To verify tenant placeholders were replaced correctly
- ⚠️ To catch typos or formatting issues in env files
- 🔁 Can be run multiple times

### 5️⃣ params.txt
**⚙️ Configuration file** containing all parameters for the setup process.

## ⚙️ Configuration (params.txt)

### 📝 Required Inputs (Change for each tenant)

```ini
# Destination tenant config repository
destination_repo_github_url=https://git.shared.linearft.tools/odx-platform-configs/ODXP-DPLOY--odx-config-vnb-deploy.git

# Tenant identifiers (used to replace placeholders in env files)
tenant-domain=vnb
tenant-id=vnb

# Products to create (format: <ProductType>_Product_<Number>=<Product Name>)
Consumer_DAO_Product_1=Cardinal Checking
Consumer_DAO_Product_2=Commonwealth Account
SMB_DAO_Product_1=Business Economy Checking
# ... add more products as needed

# Template vars repository tag
template_vars_tag=12.4.1

# Pull Request title
pr_title=SCS-2991 Initial Setup
```

### 💻 Machine-Specific Settings (Usually don't change)

```ini
# Local working directory for cloning and processing
workingDirectory=/Users/NomanAhmed/Documents/Noman/pcm-tenants-setup/workdir

# Branch name to create in destination repo
branchName=feature-new-products

# Static files repository (baseline app and env files)
static_files_repo_github_url=https://git.shared.linearft.tools/odx-platform-configs/ODXP-DPLOY--odx-config-slt-deploy.git

# Template variables repository
template_vars_github_url=https://git.shared.linearft.tools/odx-platform-configs/ODXP-DPLOY--odx-config-platform-deploy.git

# Cleanup flag (set to true to delete workdir after execution)
cleanup_after_run=false
```

### 🗺️ Product Type Mappings

The following mappings define how each product type is configured:

**TEMPLATE_PATHS** - Maps product types to their template_vars source directories:
```
Consumer_CC → product-type/credit-card-self-service/default-variables
Consumer_DAO → product-type/consumer-dao/default-variables
SMB_DAO → product-type/smb-dao/default-variables
SMB_CC → product-type/smb-credit-card/default-variables
SMB_LOC → product-type/smb-loc/default-variables
SMB_TL → product-type/smb-tl/default-variables
```

**PRODUCT_TYPE_MAP** - Maps to productType field in definition.json:
```
Consumer_CC → CREDIT_CARD_SELF_SERVICE
Consumer_DAO → CONSUMER_DAO
SMB_DAO → SMB_DAO
SMB_CC → SMB_CREDIT_CARD
SMB_LOC → SMB_LOC
SMB_TL → SMB_TL
```

**PRODUCT_POLICY_MAP** - Maps to policy field in definition.json:
```
Consumer_CC → catalyst-cc-policy-poc
Consumer_DAO → amt-consumer-dao-policy
SMB_DAO → amt-smb-dao-policy
SMB_CC → amt-smb-credit-card-policy
SMB_LOC → amt-smb-loc-policy
SMB_TL → amt-smb-tl-policy
```

**PRODUCT_TYPE_NAME_MAP** - Maps to productTypeName field in definition.json:
```
Consumer_CC → Credit Card Self Service
Consumer_DAO → Consumer Deposit Account
SMB_DAO → Deposit Account
SMB_CC → SMB Credit Card
SMB_LOC → Business Line of Credit
SMB_TL → Business Term Loan
```

## 🏷️ Supported Product Types

- **Consumer_CC** - Consumer Credit Card Self Service
- **Consumer_DAO** - Consumer Deposit Account Opening
- **SMB_DAO** - Small Business Deposit Account Opening
- **SMB_CC** - Small Business Credit Card
- **SMB_LOC** - Small Business Line of Credit
- **SMB_TL** - Small Business Term Loan

## 🔄 Workflow

### 📝 Step 1: Configure params.txt
Edit the required inputs section:
- Set destination repository URL
- Set tenant-domain and tenant-id
- Define products using format: `<ProductType>_Product_<N>=<Product Name>`
- Set template_vars_tag (version to use)
- Set PR title

### 🚀 Step 2: Run Main Setup
```bash
python PCM_Tenants_Configs_Setup.py
```

This will:
1. 📥 Clone all required repositories
2. 🌱 Create branch in destination repo
3. 📄 Copy baseline files
4. 🔄 Replace tenant placeholders in env files
5. 📁 Create product directories with UUIDs
6. 📊 Copy template_vars for each product
7. 📝 Generate definition.json for each product
8. ✅ Commit, push, and create PR
9. 📊 Print summary with all definition.json files

### ✅ Step 3: Validate Setup (Optional but Recommended)

**Validate product definitions:**
```bash
python print_product_summary.py
```

**Validate template_vars copy:**
```bash
python validate_template_vars.py
```

**Validate env file placeholders:**
```bash
python validate_env_files.py
```

## 📁 Product Directory Structure

After execution, the destination repository will have this structure:

```
destination/
├── app/                          # Baseline application files
├── env/                          # Environment configuration files
│   ├── serenityprdpr.json       # Preview environment config
│   └── serenityprod1.json       # Production environment config
├── product/                      # Product configurations
│   ├── <uuid-1>/                # First product
│   │   ├── definition.json      # Product metadata
│   │   └── template_vars/       # Product-specific template variables
│   ├── <uuid-2>/                # Second product
│   │   ├── definition.json
│   │   └── template_vars/
│   └── ...
└── .gitignore
```

## 📝 definition.json Structure

Each product has a definition.json file with the following structure:

```json
{
  "productId": "b274f78a-0210-4242-b7e5-7e0f5ad5674b",
  "productName": "Cardinal Checking",
  "productType": "CONSUMER_DAO",
  "productTypeName": "Consumer Deposit Account",
  "policy": "amt-consumer-dao-policy",
  "selfServiceManaged": true
}
```

## ➕ Adding New Products

To add new products, edit params.txt:

```ini
# Add to existing product type
Consumer_DAO_Product_10=New Checking Account

# Or add new product type (ensure all mappings exist)
Consumer_CC_Product_1=Rewards Card
```

## 🆕 Adding New Product Types

To support a new product type:

1. Add to TEMPLATE_PATHS (source directory in template_vars repo)
2. Add to PRODUCT_TYPE_MAP (productType code)
3. Add to PRODUCT_POLICY_MAP (policy name)
4. Add to PRODUCT_TYPE_NAME_MAP (display name)
5. Define products using the new type prefix

Example:
```ini
TEMPLATE_PATHS=...,NewType:product-type/new-type/default-variables
PRODUCT_TYPE_MAP=...,NewType:NEW_TYPE_CODE
PRODUCT_POLICY_MAP=...,NewType:new-type-policy
PRODUCT_TYPE_NAME_MAP=...,NewType:New Type Display Name

NewType_Product_1=First New Type Product
```

## 🔧 Troubleshooting

### ❌ Script fails with "mapping validation failed"
- Ensure all product types used have entries in all four mapping parameters
- Check for typos in product type prefixes

### 📂 Validation scripts show "directory not found"
- Ensure main setup script completed successfully
- Check workingDirectory path in params.txt
- Verify cleanup_after_run is set to false

### ⚠️ Env validation fails
- Check for typos in tenant-domain and tenant-id values
- Look for extra spaces or characters
- Verify placeholders were replaced correctly

### 📄 Template vars validation fails
- Check that template_vars_tag exists in the repository
- Verify TEMPLATE_PATHS point to valid directories
- Ensure source repository was cloned successfully

## 🛠️ Prerequisites

- Python 3.6+
- Git CLI
- GitHub CLI (gh) - for PR creation
- Access to the required Git repositories
- Git credentials configured

## 📌 Notes

- 📄 All scripts read from the same params.txt file
- 🔁 Validation scripts can be run multiple times without side effects
- 🧹 Set cleanup_after_run=true to automatically delete workdir after execution
- 🆔 Product UUIDs are randomly generated for each product
- 🔢 Products are processed in sorted order (by type, then index number)
