import os
from jinja2 import Environment, FileSystemLoader

def generate_markdown(data, template_name='README.template.md', output_name='README.md'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(data)
    with open(output_name, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"Generated {output_name}")

def generate_svg(data, template_name='dashboard.template.svg', output_name='assets/dashboard.svg'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    output = template.render(data)
    os.makedirs('assets', exist_ok=True)
    with open(output_name, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"Generated {output_name}")
