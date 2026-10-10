(function(root){
'use strict';
const looks=[['peach','奶桃团子','#f8d9bf'],['berry','草莓糯米','#f4bad2'],['cream','奶油布丁','#f7e7bf'],['taro','芋泥啵啵','#d8c8eb']];
let active='peach';try{const saved=JSON.parse(localStorage.getItem('piggy2-look'));if(looks.some(v=>v[0]===saved))active=saved}catch(e){}
function src(role,skin){const key=(skin||active)+'-'+(role||'pig');return root.PIG_SKIN_URI&&root.PIG_SKIN_URI[key]||'assets/skins/'+key+'.svg'}
function apply(){document.querySelectorAll('img[data-pig-role]').forEach(im=>im.src=src(im.dataset.pigRole));document.body.dataset.look=active;document.querySelectorAll('[data-look]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.look===active))}
root.PigLook={looks,src,apply,get active(){return active},get colors(){return {peach:['#ffe3c9','#f4c5ad','#e79a9f','#b66c7d'],berry:['#ffd6e2','#f4aeca','#ee8aa9','#b85c85'],cream:['#fff2d5','#efdab3','#e7aa9f','#ad7e65'],taro:['#e8ddf8','#ccbbe8','#ce9dcc','#9075aa']}[active]},onchange:null,choose(id){if(!looks.some(v=>v[0]===id))return;active=id;try{localStorage.setItem('piggy2-look',JSON.stringify(id))}catch(e){}apply();if(this.onchange)this.onchange(id)}};
})(window);
