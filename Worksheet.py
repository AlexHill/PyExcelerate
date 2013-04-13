import Range

class Worksheet(object):
	def __init__(self, name):
		self._name = name
		self._cells = []

	def __getitem__(self, key):
		if key not in self._cells:
			raise Exception("Not implemented")
		return Range.Range(key, key, self) # return a row range

	@property
	def num_rows(self):
		if len(self._cells) > 0:
			return max(self._cells.keys())
		else:
			return 1
		
	@property
	def num_columns(self):
		raise Exception("Not implemented")
		
	def get_xml(self):
		xml = """
		<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
		<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
			xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
			xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
			mc:Ignorable="x14ac"
			xmlns:x14ac="http://schemas.microsoft.com/office/spreadsheetml/2009/9/ac">
			<sheetViews>
				<sheetView tabSelected="1" workbookViewId="0">
					<selection activeCell="A3" sqref="A3"/>
				</sheetView>
			</sheetViews>
			<sheetFormatPr defaultRowHeight="15" x14ac:dyDescent="0.25"/>
			<sheetData>"""
		for row in self._cells.keys():
			range = Range.Range(row, row, self)
		
			xml += range.get_xml()
		
		xml += """</sheetData><pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3"/>
</worksheet>"""
		return xml