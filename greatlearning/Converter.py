# import nbformat
# from nbconvert import HTMLExporter
#
# # Load the notebook
# with open("EasyVisa_Full_Code.ipynb", "r", encoding="utf-8") as f:
#     notebook_content = nbformat.read(f, as_version=4)
#
# # Convert to HTML
# html_exporter = HTMLExporter()
# (body, resources) = html_exporter.from_notebook_node(notebook_content)
#
# # Save to an HTML file
# with open("your_notebook.html", "w", encoding="utf-8") as f:
#     f.write(body)


import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup

# Load notebook
with open("Full_Code_SuperKart_Model_Deployment_Notebook.ipynb", "r", encoding="utf-8") as f:
    notebook_content = nbformat.read(f, as_version=4)

# Convert to HTML
html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(notebook_content)

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(body, 'html.parser')

# Wrap all <table> tags in scrollable div
for table in soup.find_all("table"):
    wrapper = soup.new_tag("div", style="overflow-x:auto; width:100%;")
    table.wrap(wrapper)

# Write final HTML
with open("Full_Code_SuperKart_Model_Deployment_Notebook.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
