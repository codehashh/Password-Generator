src = open('app.py', encoding='utf-8').read()
print('len', len(src))
print(repr(src[:400]))
ns = {'__name__':'not_main'}
exec(src, ns)
print('symbols:', sorted([k for k in ns.keys() if not k.startswith('__')]))
