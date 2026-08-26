from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')

start = text.find('function trySwordSlash(e){')
end = text.find('\nfunction collect(e){', start)
if start == -1 or end == -1:
    raise SystemExit('Could not find trySwordSlash function')

new_fn = '''function trySwordSlash(e){
 if(!e || !['slippage','mev','spike','boss'].includes(e.type))return false;
 if(e.__destroyed || swordSlashCooldown>0 || swordStock()<=0)return false;

 const playerFront=P.x+P.w;
 const enemyLeft=e.x;
 const enemyRight=e.x+e.w;
 const attackReach=Math.max(125,Math.min(190,P.w+80));
 const playerH=P.duck?Math.max(56,P.h*.62):P.h;
 const inFront=enemyRight>=P.x-8 && enemyLeft<=playerFront+attackReach;
 const verticalClose=(e.y+e.h>P.y+4) && (e.y<P.y+playerH+14);
 if(!inFront || !verticalClose)return false;

 if(!consumeSword())return false;
 swordSlashCooldown=.22;
 slashFxTime=.52;
 slashFxSkin=equippedSkin||'default';

 const slashColor=slashFxSkin==='usdz'?'#ffd45a':(slashFxSkin==='cyber'?'#b96cff':'#8fffee');
 burst(Math.max(playerFront,e.x)+e.w*.35,e.y+e.h/2,slashColor,12);
 score+=50;

 const enemyName={slippage:'SLIPPAGE',mev:'MEV',spike:'PRICE IMPACT',boss:'MEV BOT'}[e.type]||'ENEMY';
 toast('⚔️ '+enemyName+' SLASHED!  SWORD ×'+swordStock());
 try{beep(820,.07)}catch(_){}
 e.__destroyed=true;
 return true;
}'''

path.write_text(text[:start] + new_fn + text[end:], encoding='utf-8')
