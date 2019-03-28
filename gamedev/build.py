import os
import yaml
from collections import OrderedDict

from jinja2 import Template, Environment, FileSystemLoader, meta, contextfunction, contextfilter


def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


# LOAD YAML
yaml_entries = {}
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
for file_name in os.listdir(SCRIPT_PATH):
    file_root = os.path.splitext(file_name)[0]
    file_ext = os.path.splitext(file_name)[-1]

    # IGNORE NON YAML FILES
    if not file_ext == '.yaml':
        continue

    with open(os.path.join(SCRIPT_PATH, file_name), 'r', encoding="utf-8") as f:
        yaml_entries[file_root] = ordered_load(f, yaml.SafeLoader)


# JINJA RENDERING
env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

tpl_html = env.get_template("index.jinja")

html_output = tpl_html.render(y=yaml_entries)

# GENERATE INDEX.HTML
INDEX_FULL_PATH = os.path.join(os.path.dirname(__file__), "index.html")
with open(INDEX_FULL_PATH, "wb") as fh:
    fh.write(html_output.encode('utf-8'))


