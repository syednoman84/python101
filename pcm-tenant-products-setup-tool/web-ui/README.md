# 🌐 PCM Tenants Configuration Setup - Web UI

A Flask-based web interface for managing PCM tenant configurations.

## 🚀 Quick Start

### 1️⃣ Install Dependencies

```bash
cd web-ui
pip install -r requirements.txt
```

### 2️⃣ Start the Server

```bash
python app.py
```

### 3️⃣ Open in Browser

Navigate to: **http://localhost:5000**

## ✨ Features

- 🎨 **Modern UI** - Beautiful gradient design with smooth animations
- 📝 **Form-based Configuration** - Easy-to-use forms for all settings
- ➕ **Dynamic Product Management** - Add/remove products on the fly
- 💾 **Auto-save params.txt** - Automatically updates the params.txt file
- 🚀 **One-click Execution** - Run setup scripts directly from the browser
- ✅ **Integrated Validation** - Run validation scripts and see results instantly
- 📊 **Product Summary** - View all created products in real-time
- 📱 **Responsive Design** - Works on desktop and mobile

## 📂 Structure

```
amount/
├── params/
│   └── params.txt        # Configuration file
├── scripts/
│   ├── PCM_Tenants_Configs_Setup.py
│   ├── validate_template_vars.py
│   ├── validate_env_files.py
│   └── print_products_summary.py
├── results/              # All output files generated here
└── web-ui/
    ├── app.py           # Flask backend server
    ├── requirements.txt # Python dependencies
    ├── templates/
    │   └── index.html  # Main UI template
    └── README.md       # This file
```

## 🔧 How It Works

### Backend (app.py)

The Flask server provides REST API endpoints:

- `GET /` - Serves the main UI
- `GET /api/load-params` - Loads existing params/params.txt
- `POST /api/save-params` - Saves configuration to params/params.txt (automatically sets workingDirectory to results)
- `POST /api/run-setup` - Executes scripts/PCM_Tenants_Configs_Setup.py
- `POST /api/validate/<type>` - Runs validation scripts from scripts directory

**Important:** When running from the web UI, the `workingDirectory` is automatically set to `results`. This keeps all cloned repositories and generated files in the results folder.

### Frontend (index.html)

Single-page application with 4 tabs:

1. **🚀 Setup** - Configure tenant and products
2. **✅ Validate** - Run validation scripts
3. **📊 Summary** - View product summary
4. **ℹ️ About** - Documentation

## 🎯 Usage

### Configure and Run Setup

1. Fill in the form fields (pre-filled with defaults)
2. Add/remove products as needed
3. Click "🚀 Run Setup" to execute
4. View real-time output in the console area

### Validate Configuration

1. Go to the "✅ Validate" tab
2. Click validation buttons to run checks
3. View results instantly

### View Product Summary

1. Go to the "📊 Summary" tab
2. Click "Show Product Summary"
3. See all created products and their definitions

## 🔒 Security Notes

- This UI runs locally on your machine
- All scripts execute with your user permissions
- No data is sent to external servers
- params.txt is saved in the params directory
- All results are generated in the results directory

## 🛠️ Troubleshooting

### Port Already in Use

If port 5000 is busy, edit `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

### Scripts Not Found

Ensure the web-ui folder is inside the amount directory:
```
amount/
├── params/
│   └── params.txt
├── scripts/
│   ├── PCM_Tenants_Configs_Setup.py
│   ├── validate_template_vars.py
│   ├── validate_env_files.py
│   └── print_products_summary.py
├── results/
└── web-ui/
    └── app.py
```

### Permission Errors

Make sure you have write permissions for the amount directory.

## 📌 Notes

- The server must be running to use the UI
- All changes are saved to params/params.txt
- Scripts execute from the scripts directory
- Output is displayed in real-time
- **Working directory is automatically set to `results`** when running from the UI
- All cloned repositories and generated files are stored in `results`
- The `results` folder can be cleaned up after execution
