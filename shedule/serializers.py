import pathlib
from .models import * 


def get_json():
    import json
    shedule = []

    professors = Professor.objects.all()
    for p in professors:
        shedule.append({"prof":{"id":p.id, "name":p.name}}) 

    courses = Course.objects.all()
    for c in courses:
        shedule.append({"course":{"id":c.id, "name":c.name}})

    rooms = Room.objects.all()
    for r in rooms:
        shedule.append({"room":{"name":r.name, "size":r.size}})
    
    groups = Group.objects.all()
    for g in groups:
        shedule.append({"group":{"id":g.id, "name":g.name, "size":g.size}})
    
    classes = Class.objects.all()
    for c in classes:
        shedule.append({"class":{"professor":c.professor.id, "course":c.course.id, "duration":c.duration, "groups":c.groups.id}})
    
    f = open(str(pathlib.Path().absolute()) +"/algorithm/inai.json", "w", encoding='utf-8')
    json.dump(shedule, f) 