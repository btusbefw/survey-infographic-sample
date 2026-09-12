from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont
OUT=Path(__file__).parent
DATA=[('La rapidité',48),('La clarté',32),('Le design',20)]
assert sum(v for _,v in DATA)==100
for height,name in [(1080,'square'),(1350,'portrait')]:
 im=Image.new('RGB',(1080,height),'#F5F2E9');draw=ImageDraw.Draw(im)
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="{height}" viewBox="0 0 1080 {height}">',f'<rect width="1080" height="{height}" fill="#F5F2E9"/>']
 def rect(x,y,w,h,color):
  draw.rectangle((x,y,x+w,y+h),fill=color)
  svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')
 def text(x,y,s,size=32,color='#202921',bold=False):
  font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',size)
  draw.text((x,y),s,font=font,fill=color,anchor='lt')
  svg.append(f'<text x="{x}" y="{y+size*.8}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(s)}</text>')
 rect(64,64,8,34,'#D34B29');text(90,66,'LE CHIFFRE À RETENIR',25,bold=True)
 text(64,145,'Un site rapide,',68,bold=True);text(64,223,'une priorité.',68,bold=True)
 text(64,334,'Quel critère compte le plus pour vous',31);text(64,378,'sur le site d’une entreprise ?',31)
 top=475 if height==1080 else 520;pitch=122 if height==1080 else 170
 for i,(label,val) in enumerate(DATA):
  y=top+i*pitch;text(64,y,label,32,bold=i==0);text(900,y,f'{val} %',34,bold=True)
  rect(64,y+48,936,30,'#E4E3D9');rect(64,y+48,936*val/100,30,'#D34B29' if i==0 else '#637B6C')
 foot=height-155;rect(64,foot-23,952,1,'#CACDC0')
 text(64,foot,'EXEMPLE FICTIF · DÉMONSTRATION GRAPHIQUE',23,bold=True)
 text(64,foot+43,'Données synthétiques : 200 réponses simulées, choix unique.',20,color='#526054')
 text(64,foot+75,'Aucun sondage réel. Échelle des barres : 0 à 100 %.',20,color='#526054')
 text(904,height-35,'CDRXRX',17,color='#526054')
 svg.append('</svg>');(OUT/f'{name}.svg').write_text('\n'.join(svg));im.save(OUT/f'{name}.png')
