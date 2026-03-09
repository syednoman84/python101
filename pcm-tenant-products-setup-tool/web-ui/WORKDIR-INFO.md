# 📁 Working Directory Behavior

## Overview

The PCM Tenants Configuration Setup uses a working directory to store cloned repositories and generated files. The location depends on how you run the scripts.

## 🖥️ Command Line Execution

When running scripts directly from the command line:

```bash
python PCM_Tenants_Configs_Setup.py
```

**Working Directory:** As specified in `params.txt`
```ini
workingDirectory=/Users/NomanAhmed/Documents/Noman/pcm-tenants-setup/workdir
```

## 🌐 Web UI Execution

When running from the web UI:

```bash
cd web-ui
./start.sh
```

**Working Directory:** Automatically set to `web-ui/workdir`

The Flask backend automatically overrides the `workingDirectory` parameter to keep everything isolated within the web-ui folder.

## 🗂️ What's Stored in workdir

```
workdir/
├── destination/          # Cloned tenant config repo
│   ├── app/
│   ├── env/
│   └── product/         # Generated products
├── static-repo/         # Cloned static files repo
└── template_vars/       # Cloned template vars repo
```

## 🧹 Cleanup Behavior

### At Start (Always)
The workdir is **always deleted** at the beginning of each run to ensure a clean state.

### At End (Configurable)
Controlled by `cleanup_after_run` in params.txt:

- `cleanup_after_run=false` → Keeps workdir after completion
- `cleanup_after_run=true` → Deletes workdir after completion

## 📌 Key Points

✅ **Web UI isolates everything** - All files stay in `web-ui/workdir`  
✅ **Command line uses custom path** - As specified in params.txt  
✅ **Always fresh start** - workdir is cleaned at the beginning of each run  
✅ **Configurable cleanup** - Choose whether to keep or delete after completion  
✅ **Git ignored** - `web-ui/workdir` is excluded from version control  

## 🔍 Finding Your Generated Files

### From Web UI
```bash
cd web-ui/workdir/destination/product
```

### From Command Line
```bash
cd /Users/NomanAhmed/Documents/Noman/pcm-tenants-setup/workdir/destination/product
```

## 💡 Tip

Set `cleanup_after_run=false` to inspect the generated files after execution. The workdir will be preserved until the next run.
