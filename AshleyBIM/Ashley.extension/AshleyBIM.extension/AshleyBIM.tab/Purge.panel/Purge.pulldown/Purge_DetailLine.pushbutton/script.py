import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from pyrevit import forms

def delete_detail_lines_with_selected_style(doc, view):
    # Create a filter to select detail lines
    category = BuiltInCategory.OST_Lines
    detail_line_filter = ElementCategoryFilter(category)

    # Create a collector to get the detail lines in the view
    collector = FilteredElementCollector(doc, view.Id).WherePasses(detail_line_filter)

    # Create a list to store the detail lines to be deleted
    lines_to_delete = []

    # Iterate over the detail lines and collect line style and element IDs
    for line in collector:
        if isinstance(line, DetailLine):
            line_style = line.LineStyle.Name
            line_id = line.Id
            if line_style == selected_style:
                lines_to_delete.append(line_id)

    # Delete the selected elements
    with Transaction(doc, 'Delete Elements') as transaction:
        transaction.Start()
        for line_id in lines_to_delete:
            doc.Delete(line_id)
        transaction.Commit()

# Get the current active view
doc = __revit__.ActiveUIDocument.Document
view = doc.ActiveView

# Get the detail lines and their styles
detail_lines = set()  # Use a set to store unique line styles

# Iterate through the elements and add unique line styles to the set
for line in FilteredElementCollector(doc, view.Id).OfClass(CurveElement):
    line_style = line.LineStyle.Name
    detail_lines.add(line_style)  # Add the line style to the set

# Convert the set back to a list for displaying
unique_line_styles = list(detail_lines)

# Show the selection form
selected_style = forms.SelectFromList.show(unique_line_styles, button_name='Select Item')


# Delete the detail lines with the selected style
delete_detail_lines_with_selected_style(doc, view)