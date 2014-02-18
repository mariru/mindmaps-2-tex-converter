import xml.etree.ElementTree as ET

def itemize_children(node):
	#method to create nested list in Latex
	#check if node is leaf
	if len(node)==0:
		return ''

	#else itemize
	str='\\begin{itemize}\n'
	for child in node:
		str=str+'\item '+child.attrib['TEXT']+'\n'+itemize_children(child)
	return str+'\end{itemize}\n'

def enumerate_children(node):
	#method to create nested list in Latex
	#check if node is leaf
	if len(node)==0:
		return ''

	#else itemize
	str='\\begin{enumerate}\n'
	for child in node:
		str=str+'\item '+child.attrib['TEXT']+'\n'+itemize_children(child)
	return str+'\end{enumerate}\n'
def create_sections(root):
	str=''
	for child in root:
		str=str+'\section*{'+child.attrib['TEXT'] +'}\n'+enumerate_children(child)
	return str

def create_frames(root):
	str=''
	for child in root:
		str=str+'\\begin{frame}{'+child.attrib['TEXT'] +'}\n'+itemize_children(child)+'\n\end{frame}'
	return str


def convert_mm_2_tex(mmfile,texfile):
	# Method to convert mind maps into nice latex notes
	# parse mind map
	tree = ET.parse(mmfile)
	# create header for tex document
	file=open('targetTex.tex','r')
	str=file.read()
	file.close()

	# replace title
	root=tree.getroot()[0]
	title = root.attrib['TEXT']
	str=str.replace("Notes",title)

	# recursively create latex document
	str=str+create_sections(root)
	str=str+'\n\end{document}'

	# write tex to target
	file=open(texfile,"w")
	file.write(str)
	file.close()
	

def convert_mm_2_beamer(mmfile,texfile):
	# Method to convert mind maps into nice beamer slides
	# parse mind map
	tree = ET.parse(mmfile)
	# create header for tex document
	file=open('targetBeamer.tex','r')
	str=file.read()
	file.close()

	# replace title
	root=tree.getroot()[0]
	title = root.attrib['TEXT']

	# recursively create latex document
	str=str+create_frames(root)
	str=str+'\n\end{document}'

	# write tex to target
	file=open(texfile,"w")
	file.write(str)
	file.close()
