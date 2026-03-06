import json
import sys
from pathlib import Path

def load_params(file_path):
    """Load workingDirectory from params.txt"""
    params = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            params[key.strip()] = value.strip()
    return params

def print_summary(product_dir):
    """Print summary of all products in the product directory"""
    product_dir = Path(product_dir)
    
    if not product_dir.exists():
        print(f"❌ Product directory not found: {product_dir}")
        sys.exit(1)
    
    # Find all product directories (UUID directories with definition.json)
    products = []
    for item in product_dir.iterdir():
        if item.is_dir():
            def_file = item / "definition.json"
            if def_file.exists():
                with open(def_file, "r", encoding="utf-8") as f:
                    definition = json.load(f)
                products.append((item, definition))
    
    if not products:
        print(f"⚠️ No products found in {product_dir}")
        return
    
    # Sort by product type and name for consistent output
    products.sort(key=lambda x: (x[1].get("productType", ""), x[1].get("productName", "")))
    
    print(f"📋 Summary of products in: {product_dir}")
    print(f"Total products: {len(products)}\n")
    
    for product_path, definition in products:
        ptype = definition.get("productType", "UNKNOWN")
        pname = definition.get("productName", "UNKNOWN")
        
        print(f"{'='*80}")
        print(f"{ptype}: {pname}")
        print(f"Path: {product_path}")
        print(f"{'='*80}")
        print(json.dumps(definition, indent=2, ensure_ascii=False))
        print()

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    params_file = script_dir / "params.txt"
    
    if not params_file.exists():
        print(f"❌ Parameters file not found: {params_file}")
        sys.exit(1)
    
    params = load_params(params_file)
    working_dir = Path(params.get("workingDirectory", "workdir")).expanduser().absolute()
    product_dir = working_dir / "destination" / "product"
    
    print_summary(product_dir)
