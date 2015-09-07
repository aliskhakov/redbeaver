def calc(fn_name, eq):
    if fn_name in eq.eq_registry:
        params = {}
        for arg in eq.eq_registry[fn_name]['args']:
            params[arg] = eq.params.get(arg, calc(arg, eq))

        res = eq.eq_registry[fn_name]['fn'](**params)
    else:
        raise Exception('undefined fn: %s' % (fn_name,))

    return res
