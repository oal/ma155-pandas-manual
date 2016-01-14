import os
from nbconvert import HTMLExporter

html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

css = None
files = sorted(os.listdir('notebooks'))
for f in files:
	(body, resources) = html_exporter.from_filename('notebooks/{}'.format(f))
	print(resources['inlining'].keys())
	if not css:
		css = resources['inlining']['css'][0]

	with open('html/{}'.format(f), 'w') as target:
		target.write(body)

links = ['<a class="list-group-item" href="#">{}</a>'.format('.'.join(chapter.split('.')[0:-1])) for chapter in files]

with open('html/index.tmpl', 'r') as f:
	print(links)
	source = f.read().format(
		css=css,
		menu='\n'.join(links)
	)

with open('index.html', 'w') as f:
	f.write(source)