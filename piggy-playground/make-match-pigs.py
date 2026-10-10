"""Six colour-and-silhouette-coded pigs for small match-3 cells."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent/'app/assets/match'
KINDS=[('ribbon','#f05f86','#a62d59'),('crown','#efc238','#9c7313'),('leaf','#63bd76','#286d43'),('diver','#53b7ea','#28679d'),('wizard','#ac7ade','#684494'),('tiger','#f59a45','#a85220')]
HATS=[
 '<path d="M61 27Q30-2 30 26q0 24 32 13M71 27q31-29 31-1 0 24-32 13" fill="#e93a68" stroke="#fff0f6" stroke-width="4"/><circle cx="66" cy="33" r="10" fill="#a82653"/>',
 '<path d="m35 45-7-31 28 14L78 1l21 26 26-13-7 31z" fill="#ffe05f" stroke="#b98b12" stroke-width="4"/><circle cx="78" cy="29" r="6" fill="#fa7a59"/>',
 '<path d="M79 42Q39 15 60 4q33-10 19 38 28-40 48-26 9 24-48 26" fill="#247d4a" stroke="#a0f2a4" stroke-width="3"/><path d="M26 113q48 25 109 0v17q-49 19-106 0z" fill="#287f4a"/>',
 '<circle cx="81" cy="87" r="66" fill="none" stroke="#def8ff" stroke-width="8"/><path d="M138 67h16v37h-16M54 31v-9h49v9" fill="#396db0"/><path d="M35 120q49 20 94-1" fill="none" stroke="#396db0" stroke-width="11"/>',
 '<path d="M35 49 80 0l41 48z" fill="#663b9f" stroke="#e5c9ff" stroke-width="3"/><path d="M23 51q55-16 112 0" fill="none" stroke="#663b9f" stroke-width="11"/><path d="m78 13 4 9 10 2-8 6 1 10-8-6-9 5 3-10-7-7 10-1z" fill="#ffe78b"/>',
 '<path d="m29 52 15-17 15 18M98 51l17-16 14 19" fill="#faab4e" stroke="#a84d18" stroke-width="4"/><path d="m55 57 10 16 5-18m23 0-5 18-10-15M24 88l24 8-26 4m113-14-22 10 24 5" fill="#a85220"/><path d="M137 105q23-13 11-25" fill="none" stroke="#a85220" stroke-width="6"/>'
]
def main():
 ROOT.mkdir(exist_ok=True)
 for k,(name,body,dark) in enumerate(KINDS):
  svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160"><title>{name} pig</title><ellipse cx="80" cy="145" rx="47" ry="5" fill="{dark}" opacity=".12"/><path d="M132 99q23-24 19-4-2 10-13 4" fill="none" stroke="{dark}" stroke-width="5"/><g fill="{body}" stroke="{dark}" stroke-width="2.5"><path d="M28 65 15 34q17-20 39 10M105 45q17-26 34-11l-10 37"/><ellipse cx="80" cy="94" rx="62" ry="49"/><rect x="31" y="124" width="20" height="24" rx="9"/><rect x="103" y="124" width="20" height="24" rx="9"/></g><path d="M24 43 34 57m87 0 11-13" stroke="#ffd6d9" stroke-width="8" stroke-linecap="round"/><ellipse cx="57" cy="85" rx="6" ry="8" fill="#38303c"/><ellipse cx="98" cy="85" rx="6" ry="8" fill="#38303c"/><g fill="#fff"><circle cx="55" cy="82" r="2"/><circle cx="96" cy="82" r="2"/></g><ellipse cx="79" cy="111" rx="23" ry="16" fill="#ffd2d5" stroke="{dark}" stroke-width="2"/><g fill="{dark}"><ellipse cx="70" cy="110" rx="3.5" ry="5"/><ellipse cx="88" cy="110" rx="3.5" ry="5"/></g><path d="M71 133q8 7 16 0" fill="none" stroke="{dark}" stroke-width="3" stroke-linecap="round"/>{HATS[k]}</svg>'''
  (ROOT/(name+'.svg')).write_text(svg,encoding='utf-8')
 print('Generated six distinct match pigs.')
if __name__=='__main__':main()
