# Define your paragraph of text
paragraph = """VIEW NAMING:
PRIMARY FOLDER: ViewSeries*       
VIEW NAME: Drawing Number_ViewName
	e.g. A_WorkingDrawings
		W1000_SitePlan
*project parameter


SHEETS NAMING:
PRIMARY FOLDER: SheetSeries*       
SHEET NAME:Drawing Number_Sheet name
	e.g. 01_PresentationDrawings
		P1000_SitePlan
*project parameter


Series and Prefix:
A_WorkingDrawings | W
	W_Description_GroundFloor
B_InformationView | IV
	IV_ET_GroundFloorPlan
	IV_RT_GroundFloorPlan
C_ImportExport | IE

00_ProjectInfo
0.0_Admin
1.0_PresentationDrawings | P
2.0_HOADrawings | H
3.0_LocalAuthority | LA
4.0_TenderDrawings | T
5.0_ConstructionDrawings | CD
5.1_Contractor | C
5.2_EngineeringConsultants | EC
5.3_SubContractors | SC
6.0_RoomDataSheets | RM


Drawing Numbers:
Admin: 0000
Plans: 1000
	e.g.
	P1000_SitePlan
	P1001_GroundFloorPlan
	P1002_FirstFloorPlan
Sections: 2000
Elevations: 3000
3D: 4000
Schedules/ Legends/ ProjectInfo: 5000
Details: 6000

"""

# Display the paragraph using the print function
print(paragraph)
