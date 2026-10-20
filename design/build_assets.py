"""Original vector artwork and optional pixel motion, built without external services."""
from pathlib import Path
import math
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
BG, PANEL, EDGE, VIOLET, LAV, WHITE, CYAN = '#0B0914', '#151024', '#382650', '#A855F7', '#C4B5FD', '#F5F3FF', '#22D3EE'

def svg(path, w, h, body):
    target = ROOT / 'assets' / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">{body}</svg>\n', encoding='utf-8')

def frame(w, h):
    return f'<rect width="{w}" height="{h}" rx="16" fill="{BG}"/><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="15" fill="none" stroke="{EDGE}"/>'

def line(x1,y1,x2,y2,color=EDGE,width=2):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none"/>'

def node(x,y,r=5):
    return f'<circle cx="{x}" cy="{y}" r="{r+5}" fill="{VIOLET}" opacity=".1"/><circle cx="{x}" cy="{y}" r="{r}" fill="{LAV}"/>'

# Profile: an engineer's original console crest, no fictitious level or score.
svg('characters/engineer-crest.svg',128,128,frame(128,128)+f'<path d="M64 16L104 38V88L64 112L24 88V38Z" fill="{PANEL}" stroke="{VIOLET}"/><path d="M51 48L35 64L51 80M77 48L93 64L77 80M70 43L58 85" fill="none" stroke="{LAV}" stroke-width="5"/>'+node(64,20,3))

# Three original conceptual mission emblems, not product screenshots.
svg('projects/sabli.svg',160,128,frame(160,128)+f'<path d="M28 76Q80 15 132 76Z" fill="{PANEL}" stroke="{LAV}" stroke-width="3"/><path d="M22 82H138M45 98H115" stroke="{VIOLET}" stroke-width="3"/><path d="M62 37Q56 28 63 20M81 31Q74 22 81 14M100 37Q93 28 100 20" fill="none" stroke="{EDGE}" stroke-width="3"/>'+node(80,46,3))
svg('projects/nivva.svg',160,128,frame(160,128)+f'<rect x="48" y="17" width="64" height="96" rx="12" fill="{PANEL}" stroke="{LAV}" stroke-width="2"/><path d="M58 82L72 68L84 74L102 48" fill="none" stroke="{VIOLET}" stroke-width="4"/><path d="M68 26H92M70 103H90" stroke="{EDGE}" stroke-width="3"/>'+node(102,48,3))
svg('projects/nexum.svg',160,128,frame(160,128)+f'<path d="M31 94V63L54 50V94M65 94V30L88 18V94M99 94V53L122 39V94" fill="{PANEL}" stroke="{LAV}" stroke-width="2"/><path d="M18 105H142M42 72L78 47L111 67" fill="none" stroke="{VIOLET}" stroke-width="2"/>'+node(42,72,3)+node(78,47,3)+node(111,67,3))

# Skill constellation. Large category labels survive scaling to phone width.
body=frame(720,300)
body+=f'<path d="M360 42V258M170 64H550M170 150H550M170 236H550" fill="none" stroke="{EDGE}" stroke-width="2"/>'
items=[(24,32,'BACKEND'),(394,32,'WEB + MOBILE'),(24,118,'DATA + CLOUD'),(394,118,'ENGINEERING'),(24,204,'AI WORKFLOW'),(394,204,'JAVA FOCUS')]
for x,y,label in items:
    body+=f'<rect x="{x}" y="{y}" width="302" height="64" rx="10" fill="{PANEL}" stroke="{EDGE}"/>'
    body+=node(x+26,y+32,4)+f'<text x="{x+46}" y="{y+40}" fill="{LAV}" font-family="monospace" font-size="32">{label}</text>'
for y in (64,150,236): body+=node(360,y,5)
svg('skills/constellation.svg',720,300,body)

body=frame(128,128)
for a in range(0,360,60):
    x,y=64+45*math.cos(math.radians(a)),64+45*math.sin(math.radians(a))
    body+=line(64,64,round(x,2),round(y,2))+node(round(x,2),round(y,2),3)
body+=f'<path d="M64 36L88 50V78L64 92L40 78V50Z" fill="{PANEL}" stroke="{VIOLET}" stroke-width="2"/>'+node(64,64,8)
svg('decorations/ai-core.svg',128,128,body)

body=frame(800,120)
for x,y in ((35,22),(113,42),(213,23),(372,33),(479,15),(598,36),(730,26)):
    body+=f'<rect x="{x}" y="{y}" width="2" height="2" fill="{LAV}" opacity=".55"/>'
body+=f'<path d="M0 101L80 64L170 99L250 77L340 102L430 72L530 103L630 65L720 96L800 78V120H0Z" fill="{PANEL}"/><path d="M355 104V59Q400 5 445 59V104M370 104V65Q400 29 430 65V104" fill="none" stroke="{EDGE}" stroke-width="3"/><path d="M380 104V70Q400 47 420 70V104" fill="none" stroke="{VIOLET}" stroke-width="2"/><path d="M388 120L394 104H406L412 120" fill="{VIOLET}" opacity=".15"/>'
svg('decorations/next-horizon.svg',800,120,body)

# Small provisional companion. This is deliberately not represented as Nina.
def companion(draw,x,y,scale=1,blink=False):
    pixels=[(3,0,2,1),(2,1,4,1),(1,2,6,1),(0,3,8,3),(1,6,6,1),(2,7,4,1),(1,8,2,1),(5,8,2,1)]
    for px,py,w,h in pixels:
        draw.rectangle((x+px*scale,y+py*scale,x+(px+w)*scale-1,y+(py+h)*scale-1),fill=VIOLET)
    for px in (2,5):
        draw.rectangle((x+px*scale,y+3*scale,x+(px+1)*scale-1,y+(4 if blink else 5)*scale-1),fill=WHITE)

pic=Image.new('RGB',(96,96),BG); d=ImageDraw.Draw(pic); companion(d,24,21,6)
(ROOT/'assets/characters').mkdir(exist_ok=True,parents=True)
pic.save(ROOT/'assets/characters/companion-concept.png',optimize=True)

# Optional opening animation: 4-second, calm, seamless native GIF; no rapid flashes.
frames=[]
for i in range(32):
    im=Image.new('RGB',(640,144),BG); d=ImageDraw.Draw(im)
    d.rounded_rectangle((1,1,638,142),radius=12,outline=EDGE,width=2)
    for j in range(20):
        x=(j*89+37)%630; y=(j*31+17)%100
        c=LAV if (j+i//8)%5==0 else EDGE
        d.rectangle((x,y,x+1,y+1),fill=c)
    d.line((24,119,616,119),fill=EDGE,width=1)
    pulse=int(130+35*math.sin(i*math.tau/32))
    glow=(pulse,75,200)
    d.arc((250,20,390,154),180,360,fill=glow,width=3)
    d.line((250,87,250,118),fill=glow,width=3);d.line((390,87,390,118),fill=glow,width=3)
    companion(d,296,58+round(3*math.sin(i*math.tau/32)),6,blink=i in (18,19))
    for x in range(30,215,18): d.rectangle((x,119,x+5,120),fill=EDGE)
    frames.append(im)
(ROOT/'assets/animations').mkdir(exist_ok=True,parents=True)
frames[0].save(ROOT/'assets/animations/start-screen.gif',save_all=True,append_images=frames[1:],duration=125,loop=0,optimize=True,disposal=2)
print('Created 8 original static components and one optional 32-frame GIF.')

