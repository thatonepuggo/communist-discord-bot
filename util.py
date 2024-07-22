def format_var(string: str, vars: dict):
    ret = string
    for var, replacement in vars.items():
        ret = ret.replace("%" + var + "%", str(replacement))
    return ret