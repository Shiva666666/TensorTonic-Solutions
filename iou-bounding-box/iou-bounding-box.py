def iou(box_a: list, box_b: list) -> float:
    """
    Returns IoU as a float.
    """
    # Write code here
    intersect = []

    for i in range(4):
        if i == 0 or i == 1:
            intersect.append(max(box_a[i], box_b[i]))
        else:
            intersect.append(min(box_a[i], box_b[i]))            
    
    inter_width = max(0, intersect[2] - intersect[0])
    inter_height = max(0, intersect[3] - intersect[1])

    inter_area = inter_height * inter_width
    a1 = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1])
    a2 = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1])

    union_area = (a1 + a2) - inter_area

    return inter_area/union_area
        
    
    pass