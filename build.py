import os
import json
from nbconvert import HTMLExporter

with open('manual.json') as f:
	config = json.load(f)

html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

with open('main.tmpl', 'r') as f:
	template = f.read()

files = [chapter.get('name') for chapter in config['chapters']]
files_slugs = [chapter.get('slug') for chapter in config['chapters']]

links = ['<a class="list-group-item" href="{}.html">{}</a>'.format(files_slugs[i], files[i]) for i in range(len(files))]

for i in range(len(files)):
	(body, resources) = html_exporter.from_filename('notebooks/{}.ipynb'.format(files[i]))

	with open('manual/{}.html'.format(files_slugs[i]), 'wb') as target:
		#print(body[1430-5:1430+5].encode('utf-8'))
		source = template % dict(
			menu='\n'.join(links),
			content=body
		)
		target.write(source.encode('utf-8'))


links_index = ['<a class="list-group-item" href="manual/{}.html">{}</a>'.format(files_slugs[i], files[i]) for i in range(len(files))]
with open('index.tmpl', 'r') as f:
	template_index = f.read()

with open('index.html', 'w') as f:
	source = template_index % dict(
			menu='\n'.join(links_index),
		)
	f.write(source)