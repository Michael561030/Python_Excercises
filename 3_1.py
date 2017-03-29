from html import escape
def html_p(s: str) -> str:
    new_s = '<p>{}<p>'.format(s)
    return new_s
def html_b(s: str) -> str:
    new_s = '<b>{}<b>'.format(s)
    return new_s
def html_i(s: str) -> str:
    new_s = '<i>{}<i>'.format(s)
    return new_s
def html_u(s: str) -> str:
    new_s = '<u>{}<u>'.format(s)
    return new_s
functions={'p':html_p,'b':html_b,'i':html_i,'u':html_u}
def writer(s:str) -> str:
        def wrapper(*args,**kwargs):
            for i in functions.keys():
                if isinstance(i,s):
                    return writer(s)
                else:
                    continue
        return wrapper

@writer('df')
def html_printer(s: str) -> str:
    return (escape(s))

print(html_printer('I"ll give you +++ cash for this stuff'))
