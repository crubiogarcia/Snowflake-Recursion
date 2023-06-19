"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "k4rm3n"
__version__ = "2021.11.23"

import rhinoscriptsyntax as rs
import Rhino as rh
import Grasshopper as gh
import ghpythonlib.treehelpers as gt 

pt = rs.AddPoint(point)
it = iterations
sz = size


vector = [0,sz,0]
pt2 = rs.MoveObject(pt,vector)
ln1 = []
ln1.append(rs.AddLine(point, pt2))



def polar(elem, center, number_of_rot):
    array = []
    for i in range(number_of_rot):
        angle = (360/number_of_rot)*i
        for n in range(len(elem)):
            obj = elem[n]
            array.append(rs.RotateObject(obj, center, angle, None, True))
    return array

def snowflake(lines):
    flake = []
    for line in lines:
        stpt = rs.CurveStartPoint(line)
        endpt = rs.CurveEndPoint(line)
        dist = rs.Distance(stpt, endpt)
        #midpoints and third and two thirds
        crvdomain = rs.CurveDomain(line)
        p0 = rs.CurveParameter(line, 0.5)
        midpt = rs.EvaluateCurve(line,p0)
        #get normal vector
        dx = endpt[0] - stpt[0] 
        dy = endpt[1] - stpt[1] 
        dz = endpt[2] - stpt[2] 
        vector = [dy, -dx, -dz]
        univect = rs.VectorUnitize(vector)
        param = rs.CurveParameter(line, depth)
        pt_two_thirds= rs.EvaluateCurve(line,param)
        mid1 = list(pt_two_thirds)
        middle1 = rs.AddPoint(mid1)
        mid2 = list(pt_two_thirds)
        middle2 = rs.AddPoint(mid2)
        #getlines
        newpt1 = rs.MoveObject(middle1,univect*(dist*width))
        newpt2 = rs.MoveObject(middle2,-univect*(dist*width))
        newline1 = rs.AddLine(stpt, midpt)
        newline2 = rs.AddLine(midpt, endpt)
        newline3 = rs.AddLine(midpt, middle1)
        newline4 = rs.AddLine(midpt, middle2)
        flake.append(newline1)
        flake.append(newline2)
        flake.append(newline3)
        flake.append(newline4)
    return flake




def recursive(polar, num_it, list):
    if num_it > 0:
        new_lines = snowflake(polar)
        num_it -=1
        recursive(new_lines, num_it, list)
        if num_it == 0:
                list.append(new_lines)
    return gt.list_to_tree(list)

ln = []
branch = recursive(ln1,iterations,ln)
branch.Flatten()

list_br = gt.tree_to_list(branch)
snowflake = polar(list_br, point, branches)
