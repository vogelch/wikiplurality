import sys
path = '/home/<username>/web2py'
if path not in sys.path:
    sys.path.append(path)
#import numpy as np
#from SPARQLWrapper import SPARQLWrapper, XML

# ---- example index page ----
def index():
    option_list_instance_of = ['municipality', 'museums', 'statue']
    option_list_properties = ['inhabitants', 'coordinates', 'address']
    return dict(option_list_instance_of=option_list_instance_of, option_list_properties=option_list_properties)

#municipalities, inhabitants
#  typeQ="Q70208"
#  propQ="P1082"
#museums, coordinates
#  typeQ="Q33506"
#  propQ="P1082"
#statue, located at address
#  typeQ="Q179700"
#  propQ="P6375"

def queryresult():
    data = [['population', '2%'], ['height', '3%'], ['position', '7%'], ['name', '2%']] # Dummy data
    items = [['Bern', 'population', ['123456', '121342']],['Zurich', 'population', ['234543', '235234']]]
    return dict(data=data, items=items)

def _get_dropdown(stud_id, att_code, possible_att_code):
    option_list = []
    for pac in possible_att_code:
        if pac == att_code:
            option_list.append(OPTION(pac, _value=pac, _selected='selected'))
        else:
            option_list.append(OPTION(pac, _value=pac))

    return SELECT(*option_list, _name=stud_id)

#def index():
#    response.flash = T("Hello World")
#    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})