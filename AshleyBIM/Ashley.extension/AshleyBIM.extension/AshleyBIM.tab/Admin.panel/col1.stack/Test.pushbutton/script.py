import clr
import sys
sys.path.append(r'C:\Program Files (x86)\IronPython 2.7\Lib')

import System
from System import Array
from System.Collections.Generic import *

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

watch = []

# Current doc/app/ui
doc = __revit__.ActiveUIDocument.Document

# Get CurveElement Ids:
id_inuse = []

curves_inuse = FilteredElementCollector(doc).OfClass(CurveElement)
converted_list = list(curves_inuse)

for ci in curves_inuse:
    styleid_inuse = ci.LineStyle.Id.IntegerValue
    id_inuse.append(styleid_inuse)

id_inuse = list(set(id_inuse))

# Get all line styles by getting the first item
first_item = converted_list[-1]
line_style_ids_all = first_item.GetLineStyleIds()

# Ids to delete
ids_to_delete = List[ElementId]()

for line_style_id in line_style_ids_all:
    style = doc.GetElement(line_style_id)
    if style is None:
        continue
    if style.Name[0] == "<":
        continue
    if line_style_id.IntegerValue in id_inuse:
        continue

    watch.append(style.Name)
    ids_to_delete.Add(line_style_id)

tr = Transaction(doc, 'Purge unused line styles')
tr.Start()
doc.Delete(ids_to_delete)
tr.Commit()

# Preparing output
deleted_count = len(watch)

print('Deleted Elements:', deleted_count, 'elements deleted.')
print('Line styles:', watch)
