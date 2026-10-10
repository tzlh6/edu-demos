"""Original round-bodied SVG pigs, with four palettes and twelve costumes.
Visual direction: soft, stubby pigs seen at pighub.top; no website artwork copied.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent / 'app' / 'assets'
SKINS = {
    'peach': ('#ffe3c9', '#f4c5ad', '#e79a9f', '#b66c7d', '#f9f0df'),
    'berry': ('#ffd6e2', '#f4aeca', '#ee8aa9', '#b85c85', '#fbebf1'),
    'cream': ('#fff2d5', '#efdab3', '#e7aa9f', '#ad7e65', '#f9f4e7'),
    'taro': ('#e8ddf8', '#ccbbe8', '#ce9dcc', '#9075aa', '#f1edf9'),
}
ROLES = ['crown','glasses','pirate','chef','space','bow','flower','music','wizard','scarf','detective','bee']

def costume(role):
    return {
      'pig': '',
      'crown': '<path d="M49 38l-6-22 19 10 15-18 14 18 19-10-7 23z" fill="#efd17d" stroke="#b98c49" stroke-width="2.5"/><circle cx="77" cy="31" r="4" fill="#e599a5"/>',
      'glasses': '<g fill="none" stroke="#637b84" stroke-width="3.5"><circle cx="49" cy="72" r="12"/><circle cx="83" cy="72" r="12"/><path d="M61 71q5-4 10 0m-35-2-10-2m69 2 10-2"/></g>',
      'pirate': '<path d="M30 47q40-39 90 0l-7 7H38z" fill="#687180"/><path d="M76 29v19m-8-10h16" stroke="#fff6e8" stroke-width="3"/><path d="M33 62l67 17" stroke="#6b5962" stroke-width="2.5"/><circle cx="82" cy="73" r="10" fill="#6b5962"/>',
      'chef': '<path d="M47 45l-2-16q-18-19 4-26 13-4 22 7 20-17 31 2 21-3 18 15-1 12-19 12v9z" fill="#fffdf7" stroke="#d6cdbd" stroke-width="2.5"/><path d="M47 40h54" stroke="#d6cdbd" stroke-width="3"/>',
      'space': '<ellipse cx="76" cy="73" rx="64" ry="61" fill="none" stroke="#a4c6d5" stroke-width="5"/><path d="M127 71v31h16V70z" fill="#d3e7ef" stroke="#9bbfce" stroke-width="2"/><path d="M28 117q46 19 87 0" fill="none" stroke="#a4c6d5" stroke-width="9"/>',
      'bow': '<path d="M57 34Q28 6 32 33q2 15 25 8M67 34q29-28 25-1-2 15-25 8" fill="#e997ad" stroke="#c67c93" stroke-width="2.5"/><circle cx="62" cy="37" r="7" fill="#c87892"/>',
      'flower': '<path d="M33 42q44-23 81 1" fill="none" stroke="#91b394" stroke-width="7"/><g fill="#fff7d9" stroke="#d6bc7b" stroke-width="1.5"><circle cx="37" cy="39" r="8"/><circle cx="61" cy="33" r="8"/><circle cx="86" cy="33" r="8"/><circle cx="108" cy="40" r="8"/></g><g fill="#e5bd64"><circle cx="37" cy="39" r="3"/><circle cx="61" cy="33" r="3"/><circle cx="86" cy="33" r="3"/><circle cx="108" cy="40" r="3"/></g>',
      'music': '<path d="M23 76q-3-56 56-56 56 0 53 56" fill="none" stroke="#9688bc" stroke-width="7"/><rect x="14" y="64" width="16" height="28" rx="8" fill="#b9a8d5"/><rect x="123" y="64" width="16" height="28" rx="8" fill="#b9a8d5"/>',
      'wizard': '<path d="M37 44 69 4l31 38z" fill="#b0a2d4" stroke="#897cac" stroke-width="2.5"/><path d="M30 45q38-12 79 0" fill="none" stroke="#897cac" stroke-width="8"/><path d="m67 17 2 6 6 2-6 2-2 6-2-6-6-2 6-2z" fill="#fff2b8"/>',
      'scarf': '<path d="M24 103q38 28 93 7l-3 12q-58 25-92-3z" fill="#b4c9b5"/><path d="m84 120-2 22 18 5 4-30" fill="#93b295"/><path d="M86 137l14 3" stroke="#e1ebd7" stroke-width="3"/>',
      'detective': '<path d="M28 47q5-28 42-26 45-3 49 27z" fill="#cabaa4" stroke="#a19481" stroke-width="2"/><path d="M19 47h109M66 22v21" stroke="#a19481" stroke-width="5"/><circle cx="108" cy="98" r="14" fill="#fff9ec" fill-opacity=".55" stroke="#9c8775" stroke-width="3"/><path d="m118 109 16 19" stroke="#9c8775" stroke-width="6" stroke-linecap="round"/>',
      'bee': '<path d="M100 46q24-27 35-12t-19 27q21-2 16 14t-22 0" fill="#fff9df" stroke="#d0c9a4" stroke-width="2"/><path d="M39 37q-6-15-17-11m78 11q6-15 17-11" fill="none" stroke="#a39068" stroke-width="3" stroke-linecap="round"/><g fill="#efd385"><circle cx="21" cy="25" r="5"/><circle cx="118" cy="25" r="5"/></g><path d="M28 114q36 20 84 1" fill="none" stroke="#d6b765" stroke-width="8"/>',
    }[role]

def svg(skin, role='pig', card=False):
    body, shadow, blush, line, bg = SKINS[skin]
    accessory = costume(role)
    title = '圆滚滚的小猪' if role == 'pig' else role + ' costume pig'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" role="img"><title>{title}</title>
<defs><linearGradient id="body" x2=".7" y2="1"><stop stop-color="{body}"/><stop offset="1" stop-color="{shadow}"/></linearGradient></defs>
{f'<rect x="3" y="3" width="154" height="154" rx="39" fill="{bg}"/>' if card else ''}
<ellipse cx="81" cy="144" rx="48" ry="5" fill="{line}" opacity=".09"/>
<path d="M126 81q26-26 22-4-2 11-13 7 3-10 13-14" fill="none" stroke="{shadow}" stroke-width="6" stroke-linecap="round"/>
<g fill="{shadow}"><rect x="35" y="115" width="17" height="29" rx="8"/><rect x="102" y="114" width="16" height="30" rx="8"/></g>
<path d="M25 56q-8-25 8-30 18-1 26 23M99 46q14-24 27-13 9 9 2 28" fill="{body}"/>
<path d="M23 77q2-40 54-41 59-3 59 46 0 43-55 47-59 6-58-52" fill="url(#body)"/>
<g fill="{body}"><rect x="25" y="113" width="17" height="33" rx="8.5"/><rect x="82" y="116" width="18" height="31" rx="9"/></g>
<path d="M27 46q-9-21 4-17l18 17q-16 13-21-3M105 45q10-18 17-9 5 10-7 17" fill="{blush}" opacity=".9"/>
<path d="M30 42q-4-11 1-12m77 16q8-13 13-7" fill="none" stroke="{line}" stroke-width="3.2" stroke-linecap="round"/>
<ellipse cx="48" cy="72" rx="4.4" ry="5.8" fill="#554c4c"/><ellipse cx="81" cy="73" rx="4.4" ry="5.8" fill="#554c4c"/>
<circle cx="47" cy="70" r="1.3" fill="#fff"/><circle cx="80" cy="71" r="1.3" fill="#fff"/>
<ellipse cx="32" cy="88" rx="8" ry="4.7" fill="{blush}" opacity=".55"/><ellipse cx="99" cy="89" rx="8" ry="4.7" fill="{blush}" opacity=".55"/>
<ellipse cx="62" cy="94" rx="18" ry="12" fill="{blush}"/>
<ellipse cx="56" cy="94" rx="2.4" ry="3.8" fill="{line}"/><ellipse cx="68" cy="94" rx="2.4" ry="3.8" fill="{line}"/>
<path d="M68 113q5 5 10-1" fill="none" stroke="{line}" stroke-width="2.3" stroke-linecap="round"/>
<path d="M96 51q14 0 18 13" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="7" stroke-linecap="round"/>
{accessory}</svg>'''

def main():
    folder = ROOT / 'skins'
    folder.mkdir(exist_ok=True)
    for skin in SKINS:
        for role in ['pig'] + ROLES:
            (folder / (skin + '-' + role + '.svg')).write_text(svg(skin, role, role != 'pig'), encoding='utf8')
    (ROOT / 'pig.svg').write_text(svg('peach'), encoding='utf8')
    for role in ROLES:
        (ROOT / 'cards' / (role + '.svg')).write_text(svg('peach', role, True), encoding='utf8')
    print('Generated 4 pig palettes and 12 costumes per palette (52 SVGs).')

if __name__ == '__main__':
    main()
