def join_synonymus(string):
    list_string = string.split(',')
    
    for idx, x in enumerate(list_string):
        list_string[idx] = '"'+x.upper().strip()+'"'
    return ' OR '.join(list_string)

def format_query(string):
    return string.replace("AND", "\nAND")   
