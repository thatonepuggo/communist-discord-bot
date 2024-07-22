def format_var(string: str, vars: dict):
    ret = string
    for var, replacement in vars.items():
        ret = ret.replace("%" + var + "%", str(replacement))
    return ret

def plural(number: int, plural='s', non_plural='') -> str:
    return plural if number != 1 else non_plural