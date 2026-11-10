import re, json, urllib.parse, segno
src=open('/home/claude/site/index.src.html').read()
b=open('/home/claude/casa85/build3.py').read()
m=re.search(r"IC=\{(.*?)\n\}",b,flags=re.S); IC=eval('{'+m.group(1)+'}')
IC.update({
'wallet':'<rect x="3.5" y="6" width="17" height="13" rx="3"/><path d="M3.5 9.5h13a2 2 0 0 1 2 2v1a2 2 0 0 1-2 2h-3"/><path d="M6 6l9-2.5a1.5 1.5 0 0 1 1.9 1.4V6"/><circle cx="15" cy="12" r=".8" fill="currentColor"/>',
'compass':'<circle cx="12" cy="4.5" r="1.6"/><path d="M11.2 6L6 20M12.8 6L18 20M8 14.5h8"/>',
'arrow':'<path d="M5 12h14M13 6l6 6-6 6"/>',
'x':'<path d="M6 6l12 12M18 6L6 18"/>',
'grid':'<rect x="4" y="4" width="7" height="7" rx="2"/><rect x="13" y="4" width="7" height="7" rx="2"/><rect x="4" y="13" width="7" height="7" rx="2"/><rect x="13" y="13" width="7" height="7" rx="2"/>',
'pano':'<ellipse cx="12" cy="12" rx="9" ry="4.5"/><path d="M12 7.5c-2 0-3.5 2-3.5 4.5s1.5 4.5 3.5 4.5"/><path d="M3 12h3M18 12h3"/>',
'play':'<path d="M8 5.5v13l10.5-6.5z"/>',
'prev':'<path d="M15 6l-6 6 6 6"/>',
'next':'<path d="M9 6l6 6-6 6"/>',
'plan':'<rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="M3.5 11h7v8.5M10.5 4.5V8M14 11h6.5M14 11v3"/>',
'fs':'<path d="M4 9V5.5A1.5 1.5 0 0 1 5.5 4H9M15 4h3.5A1.5 1.5 0 0 1 20 5.5V9M20 15v3.5a1.5 1.5 0 0 1-1.5 1.5H15M9 20H5.5A1.5 1.5 0 0 1 4 18.5V15"/>',
'home':'<path d="M4 11.2l8-6.7 8 6.7"/><path d="M6 9.6v8.4a1.5 1.5 0 0 0 1.5 1.5h9a1.5 1.5 0 0 0 1.5-1.5V9.6"/>',
'tag':'<path d="M3.5 12.2V5a1.5 1.5 0 0 1 1.5-1.5h7.2a1.5 1.5 0 0 1 1.06.44l7.3 7.3a1.5 1.5 0 0 1 0 2.12l-7.2 7.2a1.5 1.5 0 0 1-2.12 0l-7.3-7.3a1.5 1.5 0 0 1-.44-1.06z"/><circle cx="8" cy="8" r="1.4"/>',
'down':'<path d="M12 4v11M7 10.5l5 5 5-5"/><path d="M4.5 19.5h15"/>'})
def qr(url):
    q=segno.make(url,error='m'); m=[list(r) for r in q.matrix]; n=len(m); B=4; N=n+2*B
    d=''.join(f'M{x+B} {y+B}h1v1h-1z' for y,row in enumerate(m) for x,v in enumerate(row) if v)
    return f'<svg viewBox="0 0 {N} {N}" shape-rendering="crispEdges"><rect width="{N}" height="{N}" fill="#fff"/><path d="{d}" fill="#141613"/></svg>'
base='https://wa.me/5591980245432?text='
WA={'geral':base+urllib.parse.quote('Olá! Vi o site da Bambu Casas e quero simular a minha casa.'),
    'ipe':base+urllib.parse.quote('Olá! Vi a Casa Ipê 85 no site da Bambu Casas e quero simular a minha casa.'),
    'jatoba':base+urllib.parse.quote('Olá! Vi a Casa Jatobá 135 no site da Bambu Casas e quero simular a minha casa.'),
    'soon':base+urllib.parse.quote('Olá! Quero ser avisado quando a Casa Cumaru 110 da Bambu Casas for lançada.')}
QR={k:qr(WA[k]) for k in ['geral','ipe','jatoba']}
json.dump(WA,open('/home/claude/site/wa_urls.json','w'))
ck='<svg viewBox="0 0 24 24"><path d="M5 12l4.5 4.5L19 7"/></svg>'
xx='<svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7L7 17"/></svg>'
t=src.replace('{{CK}}',ck).replace('{{XX}}',xx)
t=re.sub(r'\{\{IC:(\w+)\}\}',lambda m:'<svg class="ic" viewBox="0 0 24 24">'+IC[m.group(1)]+'</svg>',t)
t=t.replace('{{ICONS}}',json.dumps(IC,ensure_ascii=False)).replace('{{QRS}}',json.dumps(QR)).replace('{{WAS}}',json.dumps(WA))
t=t.replace('{{QR_GERAL}}',QR['geral']).replace('{{WA_GERAL}}',WA['geral'])
assert '{{' not in t, t[t.index('{{'):t.index('{{')+40]
open('/home/claude/site/index.html','w').write(t); print(len(t)//1024,'KB')
