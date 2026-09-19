import subprocess, sys, os
from PIL import Image
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
B=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{B}/rendus",exist_ok=True)
pages=sys.argv[1:] or [f[:-5] for f in sorted(os.listdir(f"{B}/www")) if f.endswith(".html")]
for name in pages:
    raw=f"{B}/rendus/_{name}.png"; out=f"{B}/rendus/{name}_1440.png"
    subprocess.run([CH,"--headless=new","--disable-gpu","--hide-scrollbars",f"--screenshot={raw}","--window-size=1440,9000","--virtual-time-budget=8000",f"file://{B}/www/{name}.html"],check=True,capture_output=True)
    im=Image.open(raw).convert("RGB"); w,h=im.size; bar=im.crop((0,h-32,w,h)); px=im.load()
    bg=px[w//2,h-60]; last=h-33
    for y in range(h-33,0,-1):
        if any(sum(abs(px[x,y][i]-bg[i]) for i in range(3))>18 for x in range(0,w-340,24)): last=y; break
    cut=last+40; fin=Image.new("RGB",(w,cut+32),bg); fin.paste(im.crop((0,0,w,cut)),(0,0)); fin.paste(bar,(0,cut)); fin.save(out); os.remove(raw); print(name,fin.size)
