import nbformat
from traitlets.config import Config
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup
import os

# Paths
ipynb_path = "HelmNet_Full_Code_in_progress.ipynb"
html_path  = "HelmNet_Full_Code_Final.html"
base_dir   = os.path.dirname(os.path.abspath(ipynb_path)) or "."

# Load notebook
with open(ipynb_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# nbconvert config: embed images + (optional) choose template
c = Config()
c.HTMLExporter.embed_images = True           # <-- critical
# c.HTMLExporter.exclude_input = True        # optional: hide code in output
# c.HTMLExporter.template_name = "lab"       # optional: nicer styling ("classic" is default)

exporter = HTMLExporter(config=c)

# Ensure relative image paths (in markdown) resolve from the notebook folder
resources = {"metadata": {"path": base_dir}}

# Convert
body, resources = exporter.from_notebook_node(nb, resources=resources)

# Post-process HTML (your table wrapping)
soup = BeautifulSoup(body, "html.parser")
for table in soup.find_all("table"):
    wrapper = soup.new_tag("div", style="overflow-x:auto; width:100%;")
    table.wrap(wrapper)

# Save
with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"✅ Exported to {html_path}")
