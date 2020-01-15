import win32com.client

CATIA = win32com.client.Dispatch('catia.application')
Part = CATIA.ActiveDocument.part
myBody = Part.HybridBodies.Add()
ref_body = Part.CreateReferenceFromObject(myBody)
Part.HybridShapeFactory.ChangeFeatureName(ref_body, "generated Involute")



def creat_spline(point_list):
    ''' point_list is a list which every element is a instance
    '''
    PassingPtList = []
    spline = Part.HybridShapeFactory.AddNewSpline()
    spline.SetSplineType(0)
    spline.SetClosing(0)
    for index, i in enumerate(point_list):
        PassingPtList.append(Part.HybridShapeFactory.\
                AddNewPointCoord(i.x*25.4, i.y*25.4, i.z*25.4))
        myBody.AppendHybridShape(PassingPtList[index])

        ReferenceOnPoint = Part.CreateReferenceFromObject(PassingPtList[index])
        spline.AddPointWithConstraintExplicit(ReferenceOnPoint, None, -1, 1, None, 0)


    myBody.AppendHybridShape(spline)
    Part.update()
