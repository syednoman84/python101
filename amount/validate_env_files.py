import json
import re
import sys
from pathlib import Path

def load_params(file_path):
    """Load parameters from params.txt"""
    params = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            params[key.strip()] = value.strip()
    return params

def validate_env_file(file_path, tenant_domain, tenant_id):
    """Validate that placeholders are replaced in env file"""
    if not file_path.exists():
        return {"status": "missing", "message": f"File not found: {file_path}"}
    
    try:
        content = file_path.read_text(encoding="utf-8")
        
        # Check for unreplaced placeholders
        has_domain_placeholder = "<tenant-domain>" in content
        has_id_placeholder = "<tenant-id>" in content
        
        issues = []
        if has_domain_placeholder:
            issues.append("Found unreplaced placeholder: <tenant-domain>")
        if has_id_placeholder:
            issues.append("Found unreplaced placeholder: <tenant-id>")
        
        # Try to parse as JSON
        data = json.loads(content)
        
        # Recursively find all string values in JSON
        def find_all_strings(obj, path=""):
            """Recursively find all string values in JSON structure"""
            strings = []
            if isinstance(obj, dict):
                for key, value in obj.items():
                    strings.extend(find_all_strings(value, f"{path}.{key}" if path else key))
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    strings.extend(find_all_strings(item, f"{path}[{i}]"))
            elif isinstance(obj, str):
                strings.append((path, obj))
            return strings
        
        all_strings = find_all_strings(data)
        
        # Check each string value for exact tenant values
        domain_found = False
        id_found = False
        wrong_values = []
        
        for path, value in all_strings:
            # Check if this value contains the tenant domain or id
            if tenant_domain in value:
                # Check if it's an exact match or part of a URL/path
                # For URLs, check if it's exactly the tenant value, not a variation
                import re
                # Look for the tenant value as a standalone component (not followed by alphanumeric)
                if re.search(rf'(?:^|[^a-zA-Z0-9-])({re.escape(tenant_domain)})(?:[^a-zA-Z0-9-]|$)', value):
                    domain_found = True
                # Check for incorrect variations
                if re.search(rf'{re.escape(tenant_domain)}[a-zA-Z0-9]+', value):
                    wrong_values.append(f"Found incorrect tenant-domain variation in '{path}': {value}")
                # Check for trailing spaces
                if value.endswith(' ') and tenant_domain in value:
                    wrong_values.append(f"Found trailing space in '{path}': '{value}'")
                # Check for space after tenant value (e.g., "vnb /" instead of "vnb/")
                if re.search(rf'{re.escape(tenant_domain)}\s+/', value):
                    wrong_values.append(f"Found space before '/' in '{path}': {value}")
            
            if tenant_id in value:
                if re.search(rf'(?:^|[^a-zA-Z0-9-])({re.escape(tenant_id)})(?:[^a-zA-Z0-9-]|$)', value):
                    id_found = True
                if re.search(rf'{re.escape(tenant_id)}[a-zA-Z0-9]+', value):
                    wrong_values.append(f"Found incorrect tenant-id variation in '{path}': {value}")
                if value.endswith(' ') and tenant_id in value:
                    wrong_values.append(f"Found trailing space in '{path}': '{value}'")
                if re.search(rf'{re.escape(tenant_id)}\s+/', value):
                    wrong_values.append(f"Found space before '/' in '{path}': {value}")
        
        if not domain_found and not any(tenant_domain in v for _, v in all_strings):
            issues.append(f"tenant-domain value '{tenant_domain}' not found in file")
        
        if not id_found and not any(tenant_id in v for _, v in all_strings):
            issues.append(f"tenant-id value '{tenant_id}' not found in file")
        
        # Add wrong values to issues
        issues.extend(wrong_values)
        
        return {
            "status": "success",
            "has_placeholders": has_domain_placeholder or has_id_placeholder,
            "has_values": domain_found and id_found and not wrong_values,
            "issues": issues,
            "valid_json": True
        }
    except json.JSONDecodeError as e:
        return {
            "status": "error",
            "message": f"Invalid JSON: {e}",
            "valid_json": False
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error reading file: {e}"
        }

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    params_file = script_dir / "params.txt"
    
    if not params_file.exists():
        print(f"❌ Parameters file not found: {params_file}")
        sys.exit(1)
    
    params = load_params(params_file)
    working_dir = Path(params.get("workingDirectory", "workdir")).expanduser().absolute()
    env_dir = working_dir / "destination" / "env"
    
    tenant_domain = params.get("tenant-domain")
    tenant_id = params.get("tenant-id")
    
    if not tenant_domain or not tenant_id:
        print("❌ tenant-domain or tenant-id not found in params.txt")
        sys.exit(1)
    
    if not env_dir.exists():
        print(f"❌ Env directory not found: {env_dir}")
        sys.exit(1)
    
    print(f"\n{'='*80}")
    print(f"Environment Files Validation Report")
    print(f"{'='*80}")
    print(f"Expected tenant-domain: {tenant_domain}")
    print(f"Expected tenant-id: {tenant_id}")
    print(f"Env directory: {env_dir}\n")
    
    env_files = ["serenityprdpr.json", "serenityprod1.json"]
    all_valid = True
    
    for filename in env_files:
        file_path = env_dir / filename
        result = validate_env_file(file_path, tenant_domain, tenant_id)
        
        print(f"{'-'*80}")
        print(f"File: {filename}")
        print(f"{'-'*80}")
        
        if result["status"] == "missing":
            print(f"❌ {result['message']}")
            all_valid = False
        elif result["status"] == "error":
            print(f"❌ {result['message']}")
            all_valid = False
        else:
            if not result["valid_json"]:
                print(f"❌ Invalid JSON format")
                all_valid = False
            elif result["issues"]:
                print(f"❌ FAILED - Issues found:")
                for issue in result["issues"]:
                    print(f"   - {issue}")
                all_valid = False
            else:
                print(f"✅ PASSED - All placeholders replaced correctly")
                print(f"   - tenant-domain: {tenant_domain} ✓")
                print(f"   - tenant-id: {tenant_id} ✓")
        print()
    
    print(f"{'='*80}")
    if all_valid:
        print("✅ All environment files validated successfully!")
    else:
        print("❌ Some environment files have issues")
    print(f"{'='*80}\n")
