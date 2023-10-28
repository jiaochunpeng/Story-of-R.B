import json

def _json_search_key(json, key):
    found={}
    if type(json) == type({}):
        if key in json.keys():
            found[key]= json[key]
        elif len(json.keys())>0:
            for k in json.keys():
                result= _json_search_key(json[k], key)
                if result:
                    for k,v in result.items():
                        found[key]=v
    return found

