from opentrons import protocol_api
from opentrons import types
import numpy as np
import json

'''Defining Custom Labware used'''

# Insert the Shien PP Box + 3D Printed grids
LABWARE_DEF_grid_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1","L1"],["A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","K2","L2"],["A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","K3","L3"],["A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","K4","L4"],["A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","K5","L5"],["A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","K6","L6"],["A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","K7","L7"],["A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","K8","L8"],["A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","K9","L9"],["A10","B10","C10","D10","E10","F10","G10","H10","I10","J10","K10","L10"],["A11","B11","C11","D11","E11","F11","G11","H11","I11","J11","K11","L11"],["A12","B12","C12","D12","E12","F12","G12","H12","I12","J12","K12","L12"],["A13","B13","C13","D13","E13","F13","G13","H13","I13","J13","K13","L13"],["A14","B14","C14","D14","E14","F14","G14","H14","I14","J14","K14","L14"],["A15","B15","C15","D15","E15","F15","G15","H15","I15","J15","K15","L15"],["A16","B16","C16","D16","E16","F16","G16","H16","I16","J16","K16","L16"],["A17","B17","C17","D17","E17","F17","G17","H17","I17","J17","K17","L17"],["A18","B18","C18","D18","E18","F18","G18","H18","I18","J18","K18","L18"],["A19","B19","C19","D19","E19","F19","G19","H19","I19","J19","K19","L19"],["A20","B20","C20","D20","E20","F20","G20","H20","I20","J20","K20","L20"],["A21","B21","C21","D21","E21","F21","G21","H21","I21","J21","K21","L21"],["A22","B22","C22","D22","E22","F22","G22","H22","I22","J22","K22","L22"],["A23","B23","C23","D23","E23","F23","G23","H23","I23","J23","K23","L23"],["A24","B24","C24","D24","E24","F24","G24","H24","I24","J24","K24","L24"],["A25","B25","C25","D25","E25","F25","G25","H25","I25","J25","K25","L25"]],"brand":{"brand":"CH_grid_box_pp","brandId":[]},"metadata":{"displayName":"CH_grid_box_pp 300 Well Plate 10 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":128,"yDimension":85.6,"zDimension":20.5},"wells":{"A1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":68.1,"z":1.5},"B1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":63.6,"z":1.5},"C1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":59.1,"z":1.5},"D1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":54.6,"z":1.5},"E1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":50.1,"z":1.5},"F1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":45.6,"z":1.5},"G1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":41.1,"z":1.5},"H1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":36.6,"z":1.5},"I1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":32.1,"z":1.5},"J1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":27.6,"z":1.5},"K1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":23.1,"z":1.5},"L1":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":9.6,"y":18.6,"z":1.5},"A2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":68.1,"z":1.5},"B2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":63.6,"z":1.5},"C2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":59.1,"z":1.5},"D2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":54.6,"z":1.5},"E2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":50.1,"z":1.5},"F2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":45.6,"z":1.5},"G2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":41.1,"z":1.5},"H2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":36.6,"z":1.5},"I2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":32.1,"z":1.5},"J2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":27.6,"z":1.5},"K2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":23.1,"z":1.5},"L2":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":14.1,"y":18.6,"z":1.5},"A3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":68.1,"z":1.5},"B3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":63.6,"z":1.5},"C3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":59.1,"z":1.5},"D3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":54.6,"z":1.5},"E3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":50.1,"z":1.5},"F3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":45.6,"z":1.5},"G3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":41.1,"z":1.5},"H3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":36.6,"z":1.5},"I3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":32.1,"z":1.5},"J3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":27.6,"z":1.5},"K3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":23.1,"z":1.5},"L3":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":18.6,"y":18.6,"z":1.5},"A4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":68.1,"z":1.5},"B4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":63.6,"z":1.5},"C4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":59.1,"z":1.5},"D4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":54.6,"z":1.5},"E4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":50.1,"z":1.5},"F4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":45.6,"z":1.5},"G4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":41.1,"z":1.5},"H4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":36.6,"z":1.5},"I4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":32.1,"z":1.5},"J4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":27.6,"z":1.5},"K4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":23.1,"z":1.5},"L4":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":23.1,"y":18.6,"z":1.5},"A5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":68.1,"z":1.5},"B5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":63.6,"z":1.5},"C5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":59.1,"z":1.5},"D5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":54.6,"z":1.5},"E5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":50.1,"z":1.5},"F5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":45.6,"z":1.5},"G5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":41.1,"z":1.5},"H5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":36.6,"z":1.5},"I5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":32.1,"z":1.5},"J5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":27.6,"z":1.5},"K5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":23.1,"z":1.5},"L5":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":27.6,"y":18.6,"z":1.5},"A6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":68.1,"z":1.5},"B6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":63.6,"z":1.5},"C6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":59.1,"z":1.5},"D6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":54.6,"z":1.5},"E6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":50.1,"z":1.5},"F6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":45.6,"z":1.5},"G6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":41.1,"z":1.5},"H6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":36.6,"z":1.5},"I6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":32.1,"z":1.5},"J6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":27.6,"z":1.5},"K6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":23.1,"z":1.5},"L6":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":32.1,"y":18.6,"z":1.5},"A7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":68.1,"z":1.5},"B7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":63.6,"z":1.5},"C7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":59.1,"z":1.5},"D7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":54.6,"z":1.5},"E7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":50.1,"z":1.5},"F7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":45.6,"z":1.5},"G7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":41.1,"z":1.5},"H7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":36.6,"z":1.5},"I7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":32.1,"z":1.5},"J7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":27.6,"z":1.5},"K7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":23.1,"z":1.5},"L7":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":36.6,"y":18.6,"z":1.5},"A8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":68.1,"z":1.5},"B8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":63.6,"z":1.5},"C8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":59.1,"z":1.5},"D8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":54.6,"z":1.5},"E8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":50.1,"z":1.5},"F8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":45.6,"z":1.5},"G8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":41.1,"z":1.5},"H8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":36.6,"z":1.5},"I8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":32.1,"z":1.5},"J8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":27.6,"z":1.5},"K8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":23.1,"z":1.5},"L8":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":41.1,"y":18.6,"z":1.5},"A9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":68.1,"z":1.5},"B9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":63.6,"z":1.5},"C9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":59.1,"z":1.5},"D9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":54.6,"z":1.5},"E9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":50.1,"z":1.5},"F9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":45.6,"z":1.5},"G9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":41.1,"z":1.5},"H9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":36.6,"z":1.5},"I9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":32.1,"z":1.5},"J9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":27.6,"z":1.5},"K9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":23.1,"z":1.5},"L9":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":45.6,"y":18.6,"z":1.5},"A10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":68.1,"z":1.5},"B10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":63.6,"z":1.5},"C10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":59.1,"z":1.5},"D10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":54.6,"z":1.5},"E10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":50.1,"z":1.5},"F10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":45.6,"z":1.5},"G10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":41.1,"z":1.5},"H10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":36.6,"z":1.5},"I10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":32.1,"z":1.5},"J10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":27.6,"z":1.5},"K10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":23.1,"z":1.5},"L10":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":50.1,"y":18.6,"z":1.5},"A11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":68.1,"z":1.5},"B11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":63.6,"z":1.5},"C11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":59.1,"z":1.5},"D11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":54.6,"z":1.5},"E11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":50.1,"z":1.5},"F11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":45.6,"z":1.5},"G11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":41.1,"z":1.5},"H11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":36.6,"z":1.5},"I11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":32.1,"z":1.5},"J11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":27.6,"z":1.5},"K11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":23.1,"z":1.5},"L11":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":54.6,"y":18.6,"z":1.5},"A12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":68.1,"z":1.5},"B12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":63.6,"z":1.5},"C12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":59.1,"z":1.5},"D12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":54.6,"z":1.5},"E12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":50.1,"z":1.5},"F12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":45.6,"z":1.5},"G12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":41.1,"z":1.5},"H12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":36.6,"z":1.5},"I12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":32.1,"z":1.5},"J12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":27.6,"z":1.5},"K12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":23.1,"z":1.5},"L12":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":59.1,"y":18.6,"z":1.5},"A13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":68.1,"z":1.5},"B13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":63.6,"z":1.5},"C13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":59.1,"z":1.5},"D13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":54.6,"z":1.5},"E13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":50.1,"z":1.5},"F13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":45.6,"z":1.5},"G13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":41.1,"z":1.5},"H13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":36.6,"z":1.5},"I13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":32.1,"z":1.5},"J13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":27.6,"z":1.5},"K13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":23.1,"z":1.5},"L13":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":63.6,"y":18.6,"z":1.5},"A14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":68.1,"z":1.5},"B14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":63.6,"z":1.5},"C14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":59.1,"z":1.5},"D14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":54.6,"z":1.5},"E14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":50.1,"z":1.5},"F14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":45.6,"z":1.5},"G14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":41.1,"z":1.5},"H14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":36.6,"z":1.5},"I14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":32.1,"z":1.5},"J14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":27.6,"z":1.5},"K14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":23.1,"z":1.5},"L14":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":68.1,"y":18.6,"z":1.5},"A15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":68.1,"z":1.5},"B15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":63.6,"z":1.5},"C15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":59.1,"z":1.5},"D15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":54.6,"z":1.5},"E15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":50.1,"z":1.5},"F15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":45.6,"z":1.5},"G15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":41.1,"z":1.5},"H15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":36.6,"z":1.5},"I15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":32.1,"z":1.5},"J15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":27.6,"z":1.5},"K15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":23.1,"z":1.5},"L15":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":72.6,"y":18.6,"z":1.5},"A16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":68.1,"z":1.5},"B16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":63.6,"z":1.5},"C16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":59.1,"z":1.5},"D16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":54.6,"z":1.5},"E16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":50.1,"z":1.5},"F16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":45.6,"z":1.5},"G16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":41.1,"z":1.5},"H16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":36.6,"z":1.5},"I16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":32.1,"z":1.5},"J16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":27.6,"z":1.5},"K16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":23.1,"z":1.5},"L16":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":77.1,"y":18.6,"z":1.5},"A17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":68.1,"z":1.5},"B17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":63.6,"z":1.5},"C17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":59.1,"z":1.5},"D17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":54.6,"z":1.5},"E17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":50.1,"z":1.5},"F17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":45.6,"z":1.5},"G17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":41.1,"z":1.5},"H17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":36.6,"z":1.5},"I17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":32.1,"z":1.5},"J17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":27.6,"z":1.5},"K17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":23.1,"z":1.5},"L17":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":81.6,"y":18.6,"z":1.5},"A18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":68.1,"z":1.5},"B18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":63.6,"z":1.5},"C18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":59.1,"z":1.5},"D18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":54.6,"z":1.5},"E18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":50.1,"z":1.5},"F18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":45.6,"z":1.5},"G18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":41.1,"z":1.5},"H18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":36.6,"z":1.5},"I18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":32.1,"z":1.5},"J18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":27.6,"z":1.5},"K18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":23.1,"z":1.5},"L18":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":86.1,"y":18.6,"z":1.5},"A19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":68.1,"z":1.5},"B19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":63.6,"z":1.5},"C19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":59.1,"z":1.5},"D19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":54.6,"z":1.5},"E19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":50.1,"z":1.5},"F19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":45.6,"z":1.5},"G19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":41.1,"z":1.5},"H19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":36.6,"z":1.5},"I19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":32.1,"z":1.5},"J19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":27.6,"z":1.5},"K19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":23.1,"z":1.5},"L19":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":90.6,"y":18.6,"z":1.5},"A20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":68.1,"z":1.5},"B20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":63.6,"z":1.5},"C20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":59.1,"z":1.5},"D20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":54.6,"z":1.5},"E20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":50.1,"z":1.5},"F20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":45.6,"z":1.5},"G20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":41.1,"z":1.5},"H20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":36.6,"z":1.5},"I20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":32.1,"z":1.5},"J20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":27.6,"z":1.5},"K20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":23.1,"z":1.5},"L20":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":95.1,"y":18.6,"z":1.5},"A21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":68.1,"z":1.5},"B21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":63.6,"z":1.5},"C21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":59.1,"z":1.5},"D21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":54.6,"z":1.5},"E21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":50.1,"z":1.5},"F21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":45.6,"z":1.5},"G21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":41.1,"z":1.5},"H21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":36.6,"z":1.5},"I21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":32.1,"z":1.5},"J21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":27.6,"z":1.5},"K21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":23.1,"z":1.5},"L21":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":99.6,"y":18.6,"z":1.5},"A22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":68.1,"z":1.5},"B22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":63.6,"z":1.5},"C22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":59.1,"z":1.5},"D22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":54.6,"z":1.5},"E22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":50.1,"z":1.5},"F22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":45.6,"z":1.5},"G22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":41.1,"z":1.5},"H22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":36.6,"z":1.5},"I22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":32.1,"z":1.5},"J22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":27.6,"z":1.5},"K22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":23.1,"z":1.5},"L22":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":104.1,"y":18.6,"z":1.5},"A23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":68.1,"z":1.5},"B23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":63.6,"z":1.5},"C23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":59.1,"z":1.5},"D23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":54.6,"z":1.5},"E23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":50.1,"z":1.5},"F23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":45.6,"z":1.5},"G23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":41.1,"z":1.5},"H23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":36.6,"z":1.5},"I23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":32.1,"z":1.5},"J23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":27.6,"z":1.5},"K23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":23.1,"z":1.5},"L23":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":108.6,"y":18.6,"z":1.5},"A24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":68.1,"z":1.5},"B24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":63.6,"z":1.5},"C24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":59.1,"z":1.5},"D24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":54.6,"z":1.5},"E24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":50.1,"z":1.5},"F24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":45.6,"z":1.5},"G24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":41.1,"z":1.5},"H24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":36.6,"z":1.5},"I24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":32.1,"z":1.5},"J24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":27.6,"z":1.5},"K24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":23.1,"z":1.5},"L24":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":113.1,"y":18.6,"z":1.5},"A25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":68.1,"z":1.5},"B25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":63.6,"z":1.5},"C25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":59.1,"z":1.5},"D25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":54.6,"z":1.5},"E25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":50.1,"z":1.5},"F25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":45.6,"z":1.5},"G25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":41.1,"z":1.5},"H25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":36.6,"z":1.5},"I25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":32.1,"z":1.5},"J25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":27.6,"z":1.5},"K25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":23.1,"z":1.5},"L25":{"depth":19,"totalLiquidVolume":10,"shape":"rectangular","xDimension":3.9,"yDimension":3.9,"x":117.6,"y":18.6,"z":1.5}},"groups":[{"metadata":{"wellBottomShape":"flat"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1","L1","A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","K2","L2","A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","K3","L3","A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","K4","L4","A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","K5","L5","A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","K6","L6","A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","K7","L7","A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","K8","L8","A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","K9","L9","A10","B10","C10","D10","E10","F10","G10","H10","I10","J10","K10","L10","A11","B11","C11","D11","E11","F11","G11","H11","I11","J11","K11","L11","A12","B12","C12","D12","E12","F12","G12","H12","I12","J12","K12","L12","A13","B13","C13","D13","E13","F13","G13","H13","I13","J13","K13","L13","A14","B14","C14","D14","E14","F14","G14","H14","I14","J14","K14","L14","A15","B15","C15","D15","E15","F15","G15","H15","I15","J15","K15","L15","A16","B16","C16","D16","E16","F16","G16","H16","I16","J16","K16","L16","A17","B17","C17","D17","E17","F17","G17","H17","I17","J17","K17","L17","A18","B18","C18","D18","E18","F18","G18","H18","I18","J18","K18","L18","A19","B19","C19","D19","E19","F19","G19","H19","I19","J19","K19","L19","A20","B20","C20","D20","E20","F20","G20","H20","I20","J20","K20","L20","A21","B21","C21","D21","E21","F21","G21","H21","I21","J21","K21","L21","A22","B22","C22","D22","E22","F22","G22","H22","I22","J22","K22","L22","A23","B23","C23","D23","E23","F23","G23","H23","I23","J23","K23","L23","A24","B24","C24","D24","E24","F24","G24","H24","I24","J24","K24","L24","A25","B25","C25","D25","E25","F25","G25","H25","I25","J25","K25","L25"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"chgridboxpp_300_wellplate_10ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""

LABWARE_DEF_grid = json.loads(LABWARE_DEF_grid_JSON)
LABWARE_LABEL_grid = LABWARE_DEF_grid.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF_grid.get('wells', {}).get('A1', {}).get('yDimension')

# Custom-designed 5x5 2ml microtube holder (NOTE: We will be using only 24 of the slots; leave last one empty) -> Needs to be changed
LABWARE_microtube_holder_JSON = LABWARE_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1"],["A2","B2","C2","D2","E2","F2"],["A3","B3","C3","D3","E3","F3"],["A4","B4","C4","D4","E4","F4"],["A5","B5","C5","D5","E5","F5"],["A6","B6","C6","D6","E6","F6"]],"brand":{"brand":"CH_0.5ml_centrifuge_rack","brandId":[]},"metadata":{"displayName":"CH_0.5ml_centrifuge_rack 36 Tube Rack with 0.5ml_centrifuge_tube 0.5 mL","displayCategory":"tubeRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.6,"zDimension":33},"wells":{"A1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":75.82,"z":5.1},"B1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":62.63,"z":5.1},"C1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":49.44,"z":5.1},"D1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":36.25,"z":5.1},"E1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":23.06,"z":5.1},"F1":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":16.14,"y":9.87,"z":5.1},"A2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":75.82,"z":5.1},"B2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":62.63,"z":5.1},"C2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":49.44,"z":5.1},"D2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":36.25,"z":5.1},"E2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":23.06,"z":5.1},"F2":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":36.5,"y":9.87,"z":5.1},"A3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":75.82,"z":5.1},"B3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":62.63,"z":5.1},"C3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":49.44,"z":5.1},"D3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":36.25,"z":5.1},"E3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":23.06,"z":5.1},"F3":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":56.86,"y":9.87,"z":5.1},"A4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":75.82,"z":5.1},"B4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":62.63,"z":5.1},"C4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":49.44,"z":5.1},"D4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":36.25,"z":5.1},"E4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":23.06,"z":5.1},"F4":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":77.22,"y":9.87,"z":5.1},"A5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":75.82,"z":5.1},"B5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":62.63,"z":5.1},"C5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":49.44,"z":5.1},"D5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":36.25,"z":5.1},"E5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":23.06,"z":5.1},"F5":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":97.58,"y":9.87,"z":5.1},"A6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":75.82,"z":5.1},"B6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":62.63,"z":5.1},"C6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":49.44,"z":5.1},"D6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":36.25,"z":5.1},"E6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":23.06,"z":5.1},"F6":{"depth":27.9,"totalLiquidVolume":500,"shape":"circular","diameter":7.5,"x":117.94,"y":9.87,"z":5.1}},"groups":[{"brand":{"brand":"0.5ml_centrifuge_tube","brandId":[]},"metadata":{"wellBottomShape":"v","displayCategory":"tubeRack"},"wells":["A1","B1","C1","D1","E1","F1","A2","B2","C2","D2","E2","F2","A3","B3","C3","D3","E3","F3","A4","B4","C4","D4","E4","F4","A5","B5","C5","D5","E5","F5","A6","B6","C6","D6","E6","F6"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"ch0.5mlcentrifugerack_36_tuberack_500ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF_microtube_holder = json.loads(LABWARE_microtube_holder_JSON)
LABWARE_LABEL_microtube_holder = LABWARE_DEF_microtube_holder.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF_microtube_holder.get('wells', {}).get('A1', {}).get('yDimension')


LABWARE_deep_well_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"NEST_2ml_deep_well","brandId":[]},"metadata":{"displayName":"NEST_2ml_deep_well 96 Well Plate 2 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.7,"yDimension":85.4,"zDimension":41.3},"wells":{"A1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":74.7,"z":2.9},"B1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":65.7,"z":2.9},"C1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":56.7,"z":2.9},"D1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":47.7,"z":2.9},"E1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":38.7,"z":2.9},"F1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":29.7,"z":2.9},"G1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":20.7,"z":2.9},"H1":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":13.7,"y":11.7,"z":2.9},"A2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":74.7,"z":2.9},"B2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":65.7,"z":2.9},"C2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":56.7,"z":2.9},"D2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":47.7,"z":2.9},"E2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":38.7,"z":2.9},"F2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":29.7,"z":2.9},"G2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":20.7,"z":2.9},"H2":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":22.7,"y":11.7,"z":2.9},"A3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":74.7,"z":2.9},"B3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":65.7,"z":2.9},"C3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":56.7,"z":2.9},"D3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":47.7,"z":2.9},"E3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":38.7,"z":2.9},"F3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":29.7,"z":2.9},"G3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":20.7,"z":2.9},"H3":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":31.7,"y":11.7,"z":2.9},"A4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":74.7,"z":2.9},"B4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":65.7,"z":2.9},"C4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":56.7,"z":2.9},"D4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":47.7,"z":2.9},"E4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":38.7,"z":2.9},"F4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":29.7,"z":2.9},"G4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":20.7,"z":2.9},"H4":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":40.7,"y":11.7,"z":2.9},"A5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":74.7,"z":2.9},"B5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":65.7,"z":2.9},"C5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":56.7,"z":2.9},"D5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":47.7,"z":2.9},"E5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":38.7,"z":2.9},"F5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":29.7,"z":2.9},"G5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":20.7,"z":2.9},"H5":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":49.7,"y":11.7,"z":2.9},"A6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":74.7,"z":2.9},"B6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":65.7,"z":2.9},"C6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":56.7,"z":2.9},"D6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":47.7,"z":2.9},"E6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":38.7,"z":2.9},"F6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":29.7,"z":2.9},"G6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":20.7,"z":2.9},"H6":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":58.7,"y":11.7,"z":2.9},"A7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":74.7,"z":2.9},"B7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":65.7,"z":2.9},"C7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":56.7,"z":2.9},"D7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":47.7,"z":2.9},"E7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":38.7,"z":2.9},"F7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":29.7,"z":2.9},"G7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":20.7,"z":2.9},"H7":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":67.7,"y":11.7,"z":2.9},"A8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":74.7,"z":2.9},"B8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":65.7,"z":2.9},"C8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":56.7,"z":2.9},"D8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":47.7,"z":2.9},"E8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":38.7,"z":2.9},"F8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":29.7,"z":2.9},"G8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":20.7,"z":2.9},"H8":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":76.7,"y":11.7,"z":2.9},"A9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":74.7,"z":2.9},"B9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":65.7,"z":2.9},"C9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":56.7,"z":2.9},"D9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":47.7,"z":2.9},"E9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":38.7,"z":2.9},"F9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":29.7,"z":2.9},"G9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":20.7,"z":2.9},"H9":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":85.7,"y":11.7,"z":2.9},"A10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":74.7,"z":2.9},"B10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":65.7,"z":2.9},"C10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":56.7,"z":2.9},"D10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":47.7,"z":2.9},"E10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":38.7,"z":2.9},"F10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":29.7,"z":2.9},"G10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":20.7,"z":2.9},"H10":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":94.7,"y":11.7,"z":2.9},"A11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":74.7,"z":2.9},"B11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":65.7,"z":2.9},"C11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":56.7,"z":2.9},"D11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":47.7,"z":2.9},"E11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":38.7,"z":2.9},"F11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":29.7,"z":2.9},"G11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":20.7,"z":2.9},"H11":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":103.7,"y":11.7,"z":2.9},"A12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":74.7,"z":2.9},"B12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":65.7,"z":2.9},"C12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":56.7,"z":2.9},"D12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":47.7,"z":2.9},"E12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":38.7,"z":2.9},"F12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":29.7,"z":2.9},"G12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":20.7,"z":2.9},"H12":{"depth":38.4,"totalLiquidVolume":2,"shape":"rectangular","xDimension":8,"yDimension":8,"x":112.7,"y":11.7,"z":2.9}},"groups":[{"metadata":{"wellBottomShape":"v"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"nest2mldeepwell_96_wellplate_2ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
LABWARE_DEF_deep_well = json.loads(LABWARE_deep_well_JSON)
LABWARE_LABEL_deep_well = LABWARE_DEF_deep_well.get('metadata', {}).get(
    'displayName', 'test labware')
LABWARE_DIMENSIONS = LABWARE_DEF_deep_well.get('wells', {}).get('A1', {}).get('yDimension')

# Metadata for protocol
metadata = {
'apiLevel': '2.0',
'author': 'Tan_Ching_Hai'}

# User inputs (This is dynamic and will be automatically taken in the user input from the UI python file)
samples = 25


''' Start of OT-2 Protocol'''

def run (protocol:protocol_api.ProtocolContext):
    
    '''Declaring the labware used'''
    sample_box_1 = protocol.load_labware_from_definition(LABWARE_DEF_grid,'1',LABWARE_LABEL_grid)
    sample_box_2 = protocol.load_labware_from_definition(LABWARE_DEF_grid,'2',LABWARE_LABEL_grid)
    sample_box_3 = protocol.load_labware_from_definition(LABWARE_DEF_grid,'4',LABWARE_LABEL_grid)
    
    # Racks holding the environmental stock solution at log(2) dilution
    rack_1 = protocol.load_labware_from_definition(LABWARE_DEF_microtube_holder, '10',LABWARE_LABEL_microtube_holder)
    rack_2 = protocol.load_labware_from_definition(LABWARE_DEF_microtube_holder, '11',LABWARE_LABEL_microtube_holder)
    
    # NEST 96-well deep well plates
    deep_well_1 = protocol.load_labware_from_definition(LABWARE_DEF_deep_well, '5', LABWARE_LABEL_deep_well)
    deep_well_2 = protocol.load_labware_from_definition(LABWARE_DEF_deep_well, '7', LABWARE_LABEL_deep_well)
    deep_well_3 = protocol.load_labware_from_definition(LABWARE_DEF_deep_well, '8', LABWARE_LABEL_deep_well)
    
    # Tip Racks
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_20ul', '9')
    tiprack_2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '6')
    tiprack_3 = protocol.load_labware('opentrons_96_filtertiprack_200ul', '3')
    
    '''Declaring the Pipette heads used'''
    left = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tiprack_1])
    right = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=[tiprack_2, tiprack_3])
    
    '''Setting OT-2 hardware parameters'''
    # Flow Rate Settings
    left.flow_rate.aspirate = 70
    left.flow_rate.blow_out = 50
    
    # Control Speed of Axis Movement (Motors)
    left.default_speed = 800  # Speed of Motors
    
    '''Hardware offset as we are using only 6 channels of the 8-channel pipette'''
    # Offset to accommodate for fact that we are using 6 channels on the multi-channel pipette & not 8 (hence need less current so don't damage head and motors)
    num_channels_per_pickup = 1
    # (only pickup tips on front-most channel)    

    per_tip_pickup_current = .075
    # (current required for picking up one tip, do not modify unless
    # you are using a GEN2 P20 8-Channel in which case change it to 
    # 0.075)

    pick_up_current = num_channels_per_pickup*per_tip_pickup_current
    protocol._hw_manager.hardware._attached_instruments[
        right._implementation.get_mount()].update_config_item(
        'pick_up_current', pick_up_current)
    
    '''Parameters for aspiration & dispensation'''
    
    # Stock solution aspiration and dispensing volume (from stock solution into deep-well plate)
    stock_vol = 3 # 297 ul of PBS each well for Deep Well Plates (This dilutes the sample to log(2) dilution)
    
    # Mixing volume
    mix_vol = 100 # Mix only using the multi-channel pipette
    
    # Air gap volume
    air_gap_vol = 3
    
    # Volume to be transferred from deep-well plate to the custom-3D_grids
    transfer_aspirate_vol = 30
    transfer_dispense_vol = transfer_aspirate_vol / 3
    
    '''Positioning offset'''
    
    # Vertical offset for 3D_grids
    grid_offset = -5 # Offset from top
    
    # Vertical offset for deep well plate
    well_offset = 5 # From bottom
    
    # Vertical offset for microtubes
    tube_offset = 3 # From bottom
    
    '''Start of Protocol'''
    
    # Create sample box list to determine how many && which sample PP_boxes to use
    box_list = [sample_box_1, sample_box_2, sample_box_3]
    
    # Create rack list to determine how many && which rack to aspirate from
    rack_list = [rack_1, rack_2]
    
    # Create a deep_plate list to determine how many && which deep-well plate to dispense into
    well_list = [deep_well_1,deep_well_2,deep_well_3]
        
        
    '''Defining the coordinates for the labware'''
    
    # Coordinates for the 96-well deep-well plate
    well_coord = np.array([]) # NumPy array to store coordinates of the well
    alphabet_well = ['A','B','C','D','E','F','G','H']
    number_well = ['1','2','3','4','5','6','7','8','9','10','11','12']
    for alpha_well in alphabet_well:
        for num_well in number_well:
            coord_well = alpha_well + num_well
            well_coord = np.append(well_coord, coord_well)

    # Coordinates for the 96-well deep-well plate (TO BE USED BY MULTI-CHANNEL PIPETTE ONLY)
    well_coord_multi = np.array([])
    alphabet_well_multi = ['A']
    number_well_multi = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    for alpha_well_multi in alphabet_well_multi:
        for num_well_multi in number_well_multi:
            coord_well_multi = alpha_well_multi + num_well_multi
            well_coord_multi = np.append(well_coord_multi, coord_well_multi)
    
    # Coordinates for the microtube holder
    rack_coord = np.array([]) # NumPy array to store coordinates of the microtube tubes
    alphabet_rack = ['A','B','C','D','E','F','G','H']
    number_rack = ['1','2','3','4','5','6']
    for alpha_rack in alphabet_rack:
        for num_rack in number_rack:
            coord_rack = alpha_rack + num_rack
            rack_coord = np.append(rack_coord, coord_rack)
    
    # Coordinates for PP_box w/ 3D_printed grids
    grid_coord = np.array([])
    alphabet_grid = ['A','B','C','D','E','F','G','H','I','J','K','L']
    number_grid = ['2','3','4','6','7','8','10','11','12','14','15','16','18','19','20','22','23','24']
    for alpha_grid in alphabet_grid:
        for num_grid in number_grid:
            coord_grid = alpha_grid + num_grid
            grid_coord = np.append(grid_coord,coord_grid)    
    
    # Transfer the stock solution from the respective "rack for stock solutions" into the respective deep-wells
    def transfer(samples):
        
        # Create an iterator to determine which sample the machine is currently running
        z = 1 # Count z = 1 as the 1st iteration
        
        while z <= samples:
            
            # Choose which rack to pick environmental sample from
            if z <= 36:
                rack = rack_list[0]
            else:
                rack = rack_list[1]
            
            # Choose which centrifuge tube the machine picks up from (for each rack)
            if z <= 36:
                tube = rack_coord[z-1]
            elif z > 36: # If user input value is larger than 36 tubes per rack, it will still pick the correct tube from the correct rack
                div = (z-1) % 36 # Determines which coordinate tube to pick from (when input sample > 36)
                tube = rack_coord[div-1]
            
            # Choose which deep-well plate to dispense environmental sample into
            if z <= 24:
                well = well_list[0]
            elif 24 < z <= 48:
                well = well_list[1]
            else:
                well = well_list[2]
                
            # Choose which coordinate well to dispense the environmental sample into
            
            # As we only want -3 samples to be present in columns 1,4,7 && 10 for rows A-F, we slice the original NumPy array which has coordinates of all 96 wells in the deep-well plate
            well_operation_coord = well_coord[0:-1:3]
            
            if z <= 24:
                well_dispense_coord = well_operation_coord[z-1]
            elif z > 24:
                divi = (z - 1) % 24
                well_dispense_coord = well_operation_coord[divi-1]
            
            left.pick_up_tip()
            
            # Move to the correct rack and aspirate the stock environmental solution of log(2) dilution
            left.aspirate(volume = stock_vol, location = rack[tube].bottom(tube_offset))
            left.move_to(location = rack[tube].top())
            left.air_gap(volume = air_gap_vol)
            
            # Move to the appropriate deep-well && dispense the environmental sample
            left.dispense(volume = stock_vol + air_gap_vol, location = well[well_dispense_coord].bottom(well_offset))
            
            # Move to top to touch_tip & prevent spilling (contamination)
            left.move_to(well[well_dispense_coord].top())
            left.touch_tip(speed = 50, v_offset = -0.5, radius = 1.5)
            left.move_to(well[well_dispense_coord].top())
            protocol.delay(0.5)
            left.air_gap(volume = air_gap_vol)
            left.drop_tip()
            z += 1
    
    def serial_dilution(samples):

        # Decide how many deep_well_plates have been pipetted into from the 'transferring' function and print out the array containing these wells
        if samples <= 24:
            wells = well_list[0:1]
        elif 24 < samples <= 48:
            wells = well_list[0:2]
        else:
            wells = well_list[0:3]        
        
        # We want to group each sample into a set of log(3), log(4) and log(5) dilution. We achieve this by reshaping the 'well_coord' array into a 2D-array which we will name: "dilution_sets". Example output would be [['A1','A2','A3'],['B1','B2','B3']...]
        overall_dilution_sets = np.reshape(well_coord_multi, (4,3))
        
        # Keep track of how many columns of samples are left for serial dilution
        leftover = samples 
        
        for well in wells:
            
            # In each deep-well plate, we want to check how many samples there are. If 1 only then we only want coordinates: 'A1','A2','A3' to be utilised. If 2 then 'A1','A2','A3','B1','B2','B3' and so on for more samples
            if leftover == 1:
                dilution_sets = overall_dilution_sets[0:1] # If left 1 leftover samples, use wells A1,A2,A3 
            elif leftover == 2:
                dilution_sets = overall_dilution_sets[0:2] # If left 2 leftover samples, use wells A1,A2,A3 then A4,A5,A6
            elif leftover == 3:
                dilution_sets =  overall_dilution_sets[0:3] # If left 3 leftover samples, use wells A1,A2,A3 then A4,A5,A6 then A7,A8,A9
            elif leftover >= 4:
                dilution_sets = overall_dilution_sets[0:4] # If left 4 or more leftover samples, use wells A1,A2,A3 then A4,A5,A6 then A7,A8,A9 then A10,A11,A12 
            
            # Loop through the 'dilution_sets' array and conduct serial dilution
            for set in dilution_sets:
            
                right.pick_up_tip()
                
                # Create an iterator 'i' for conducting serial dilution within the set of -3,-4,-5 dilution wells
                i = 0 # Initialise the iterator w/ a value of 0
                
                while i < 2:
                    
                    # Do mixing
                    right.mix(1, volume = mix_vol, location = well[set[i]].bottom(well_offset))
                    
                    # Aspirate pre-defined volume of sample for serial dilution
                    right.aspirate(volume = stock_vol)
                    
                    # Move to the next dilution factor well (-3 moves to -4, -4 moves to -5)                   
                    # Dispense the sample into the next well for dilution
                    right.dispense(volume = stock_vol,location = well[set[i+1]].bottom(well_offset))
                    
                    
                    # Increase iterator (i) value by 1
                    i += 1
                
                # Steps after the -4 to -5 dilution
                right.mix(volume = mix_vol, location = well[set[i]].bottom(well_offset))
                right.move_to(location = well[set[i]].top())
                right.air_gap(volume = air_gap_vol)
                right.drop_tip()
            
            # To ensure that the correct no. of wells are serial diluted. Let's say we have 25 samples remaining then this 'leftover' variable will let us run a full plate serial dilution. Once process is completed then it will subtract 24 from the 'leftover' which tells the program there is only 1 sample left to serial dilute. From there, the program will only do serial dilution from 'A1' to 'A3' to save time and resources.
            leftover = leftover - 6 * len(dilution_sets) # The reason we use '6' is because we are only using 6 channels of the multi-channel pipette
                
    def plating(samples):
        
        '''For 96 well Deep-well plates'''
        # To save pipette tips, we will do transferring from the deep-well plates to the PP_box from the lowest concentration to the highest concentration
        
        alphabet_well_transfer = ['A']
        number_well_transfer = ['3','2','1','6','5','4','9','8','7','12','11','10']
        
        # Create NumPy array for the above purpose
        well_coord_transfer = np.array([])
        
        for alpha_well_transfer in alphabet_well_transfer:
            for num_well_transfer in number_well_transfer:
                coord_well_transfer = alpha_well_transfer + num_well_transfer
                well_coord_transfer = np.append(well_coord_transfer, coord_well_transfer)
                
        '''For PP_box w/ 3D Printed grids'''
        
        # Following the order of the transfer of transfer from the 96 well Deep-well plates
        alphabet_grid_transfer = ['A','B']
        number_grid_transfer = ['12','11','10','8','7','6','4','3','2','24','23','22','20','19','18','16','15','14']
        
        # Create a NumPy array for the 3D_printed grids transfer
        grid_coord_transfer = np.array([])
        
        for alpha_grid_transfer in alphabet_grid_transfer:
            for num_grid_transfer in number_grid_transfer:
                coord_grid_transfer = alpha_grid_transfer + num_grid_transfer
                grid_coord_transfer = np.append(grid_coord_transfer, coord_grid_transfer)
                 
        # Synchronise both the coordinates for deep-well plates && PP_box
        grid_coord_transfer_resize = grid_coord_transfer.reshape(-1,3) # Now this array also has 12 elements in the form of nested arrays
        
        # Initiate a var to check whether we need to conduct full plate or 1/2 plate dilution based on how much sample is leftover from user input
        leftover = samples # Leftover initially is the same as user input (before 1st round of serial dilution)
        
        # Create dictionaries to assign coordinates (values) to keys
        position_1 = {
                
                # LHS -> Start position -> Coordinate on the Deep-well plate
                # RHS -> End position -> Coordinate on the PP_box w/ 3D_grids
                
                # Column_Set_1 transfer from Deep-well plate to PP_box w/ 3D_grids
                
                # log(5) diluted triplet
                'A3':['A12','A11','A10'],    
                
                # log(4) diluted triplet
                'A2':['A8','A7','A6'],

                # log(3) diluted triplet
                'A1':['A4','A3','A2'], 
                
            }   
                
        position_2 = {
                # Column_Set_2 transfer from Deep-well plate to PP_box w/ 3D_grids
                
                # log(5) diluted triplet
                'A6':['A24','A23','A22'], 
                
                # log(4) diluted triplet
                'A5': ['A20','A19','A18'], 
                
                # log(3) diluted triplet
                'A4':['A16','A15','A14'], 
                
            }
        
        position_3 = {
                # Column_Set_3 transfer from Deep-well plate to PP_box w/ 3D_grids
                
                # log(5) diluted triplet
                'A9':['B12','B11','B10'], 
                
                # log(4) diluted triplet
                'A8':['B8','B7','B6'], 
                
                # log(3) diluted triplet
                'A7':['B4','B3','B2'], 
                
            }
                
        position_4 = {
                # Column_Set_4 transfer from Deep-well plate to PP_box w/ 3D_grids
                
                # log(4) diluted triplet
                'A12':['B24','B23','B22'], 
                
                # log(4) diluted triplet
                'A11':['B20','B19','B18'], 
                
                # log(4) diluted triplet
                'A10':['B16','B15','B14'], 
                
            }
        
        # Determine how many boxes && how many Deep-well plates to use
        
        if samples <= 24:
            boxes = box_list[0:1]
        elif 24 < samples <= 48:
            boxes = box_list[0:2]
        elif 48 < samples <= 72:
            boxes = box_list[0:3]
        
        if samples <= 24:
            wells = well_list[0:1]
        elif 24 < samples <= 48:
            wells = well_list[0:2]
        elif 48 < samples <= 72:
            wells = well_list[0:3]
        
        
        def quad_grid():
            right.pick_up_tip()
            
            for start,end_list in position_1.items():
                # Move to the Deep-well plate
                right.aspirate(location = deep_well_1[start].bottom(well_offset), volume = transfer_aspirate_vol)
                
                for end in end_list: 
                    # Move to the PP_box w/ 3D_printed grids
                    right.move_to(location = box[end].bottom(4.5))
                    right.dispense(volume = transfer_dispense_vol)
                
            right.drop_tip()
            
        def half_grid():
            
            quad_grid()
            right.pick_up_tip()        
            
            for start,end_list in position_2.items():
                # Move to the Deep-well plate
                right.aspirate(location = deep_well_1[start].bottom(well_offset), volume = transfer_aspirate_vol)

                for end in end_list:
                    # Move to the PP_box w/ 3D_printed grids
                    right.move_to(location = box[end].bottom(4.5))
                    right.dispense(volume = transfer_dispense_vol)
            
            right.drop_tip()
        
        def three_quads():
            
            half_grid()
            right.pick_up_tip()
            
            for start,end_list in position_3.items():
                # Move to the Deep-well plate
                right.aspirate(location = deep_well_1[start].bottom(well_offset), volume = transfer_aspirate_vol)
                
                for end in end_list:    
                    # Move to the PP_box w/ 3D_printed grids
                    right.move_to(location = box[end].bottom(4.5))
                    right.dispense(volume = transfer_dispense_vol)
                
            right.drop_tip()
        
        def full_grid():
            
            three_quads()
            right.pick_up_tip()
            
            for start,end_list in position_4.items():
                # Move to the Deep-well plate
                right.aspirate(location = deep_well_1[start].bottom(well_offset), volume = transfer_aspirate_vol)
                
                for end in end_list:  
                    # Move to the PP_box w/ 3D_printed grids
                    right.move_to(location = box[end].bottom(4.5))
                    right.dispense(volume = transfer_dispense_vol)
                
            right.drop_tip()
            
        for box,well in zip(boxes,wells):
            if leftover <= 24:
                
                if leftover == 1:
                    for box,well in zip(boxes,wells):
                        quad_grid()
                
                if 2 < leftover <= 12:
                    for box,well in zip(boxes,wells):
                        half_grid()
                        
                if leftover == 13:
                    for box,well in zip(boxes,wells):
                        three_quads()
                
                if 13 < leftover <= 24:
                    for box,well in zip(boxes,wells):
                        full_grid()
            
            elif leftover > 12:
                full_grid()
                leftover = leftover -12
    transfer(samples)
    serial_dilution(samples)
    plating(samples)
            