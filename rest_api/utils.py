from datetime import datetime

def date_format_dict(dict):
    """
    check if date is present in dict and format it
    """
    ls = []
    for entry in dict:
        a = {}
        for key, value in entry.items():
            if key == 'date':
                a[key] = datetime.strptime(value, '%Y-%m-%d').strftime('%a, %b %d %Y')
            elif key == 'time':
                if value is None:
                    a[key] = 'All Day'
                else :
                    a[key] = value
            else:
                a[key] = value
        ls.append(a)
    return ls
