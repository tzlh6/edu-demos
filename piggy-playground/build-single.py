"""Bundle app/ into one self-contained HTML file for browsers (Chrome 109 / Firefox 115 on Windows 7 also work)."""
import base64,re,sys,json,os
from html import escape
from pathlib import Path
A=str(Path(__file__).resolve().parent / 'app') + os.sep
def uri(p,mime):return f"data:{mime};base64,"+base64.b64encode(open(A+p,'rb').read()).decode()
html=open(A+'index.html',encoding='utf8').read()
html=re.sub(r'<meta http-equiv="Content-Security-Policy"[^>]*>','',html)
license_details='<details class="github-licenses"><summary>4.1 GitHub 参考项目 MIT 许可证</summary>'
for f in sorted(os.listdir(A+'assets/licenses')):
    if f.endswith('-MIT.txt'):
        name=f[:-8].replace('_','/',1)
        license_details+='<h4>'+escape(name)+'</h4><pre>'+escape(open(A+'assets/licenses/'+f,encoding='utf8').read())+'</pre>'
license_details+='</details>'
assert html.count('<pre id="license"></pre>')==1
html=html.replace('<pre id="license"></pre>','<pre id="license"></pre>'+license_details)
pig=uri('assets/pig.svg','image/svg+xml')
cards={f[:-4]:uri('assets/cards/'+f,'image/svg+xml') for f in sorted(os.listdir(A+'assets/cards')) if f.endswith('.svg')}
html=html.replace('<link rel="stylesheet" href="style.css">','<style>'+open(A+'style.css',encoding='utf8').read()+'</style>')
html=html.replace('href="assets/pig.png"','href="'+uri('assets/pig.png','image/png')+'"')
for k,v in cards.items():html=html.replace(f'src="assets/cards/{k}.svg"',f'src="{v}"')
def js(n):
    s=open(A+n,encoding='utf8').read().replace('assets/pig.svg',pig)
    return '<script>'+s.replace('</script','<\\/script')+'</script>'
skins={f[:-4]:uri('assets/skins/'+f,'image/svg+xml') for f in sorted(os.listdir(A+'assets/skins')) if f.endswith('.svg')}
match_art={f[:-4]:uri('assets/match/'+f,'image/svg+xml') for f in sorted(os.listdir(A+'assets/match')) if f.endswith('.svg')}
scripts='<script>window.PIG_MATCH_URI='+json.dumps(match_art)+';window.CARD_URI='+json.dumps(cards)+';window.PIG_SKIN_URI='+json.dumps(skins)+';</script>'+''.join(js(n) for n in ['core.js','match-core.js','arcade-core.js','challenge-core.js','look.js','sounds.js','audio.js','match-ui.js','arcade.js','challenge.js','app.js'])
html=re.sub(r'<script src="core.js"></script>.*?<script src="app.js"></script>',lambda m:scripts,html,flags=re.S)
html=html.replace('assets/pig.svg',pig)
assert 'src="assets/' not in html and "href=\"assets/" not in html, 'unbundled asset left'
open(sys.argv[1],'w',encoding='utf8').write(html);print(sys.argv[1],len(html)//1024,'KB')
