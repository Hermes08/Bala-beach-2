import urllib.request, io, os
from PIL import Image

DEST = "/tmp/bb/repo/assets/img"
# slug -> source URL (unique images used across hero/gallery/tours/og)
IMGS = {
  "living-room":  "https://i.ibb.co/KxmKQ4Lc/living-room-2.jpg",
  "ocean-view":   "https://i.ibb.co/0RbW3B6g/Ocean-View.jpg",
  "balcony":      "https://i.ibb.co/ZRLRdpCs/balcony.jpg",
  "bedroom-1":    "https://i.ibb.co/5xrb03gY/bedroom-1.jpg",
  "pool":         "https://i.ibb.co/kVjVshpM/Pool.jpg",
  "kitchen":      "https://i.ibb.co/hJv1NcC4/kitchen-3.jpg",
  "beach":        "https://i.ibb.co/1fXxZZgH/beach.jpg",
  "bedroom-2":    "https://i.ibb.co/Y47qg6Nt/bedroom-2.jpg",
  "bathroom":     "https://i.ibb.co/BHtZsxD8/bathroom-1.jpg",
  "building":     "https://i.ibb.co/Nk87jjB/building.jpg",
  "sofa-bed":     "https://i.ibb.co/bgLsNQwV/sofa-bed.jpg",
  "gym":          "https://i.ibb.co/NdyZLcmd/gym-2.jpg",
  "portobelo":    "https://i.ibb.co/sv9Nz0rS/portobello.jpg",
  "jungle":       "https://i.ibb.co/WpcbmNG1/jungle.jpg",
  "diving":       "https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=1600&auto=format&fit=crop",
  "islands":      "https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?q=80&w=1600&auto=format&fit=crop",
}
WIDTHS = [1600, 800]
hdr = {"User-Agent": "Mozilla/5.0"}
total_before = total_after = 0
for slug, url in IMGS.items():
    try:
        req = urllib.request.Request(url, headers=hdr)
        raw = urllib.request.urlopen(req, timeout=40).read()
        total_before += len(raw)
        im = Image.open(io.BytesIO(raw)).convert("RGB")
        w0 = im.width
        for w in WIDTHS:
            tw = min(w, w0)
            ratio = tw / im.width
            resized = im.resize((tw, int(im.height*ratio)), Image.LANCZOS)
            out = os.path.join(DEST, f"{slug}-{w}.webp")
            resized.save(out, "WEBP", quality=72, method=6)
            total_after += os.path.getsize(out)
        print(f"{slug}: {len(raw)//1024}KB -> {w0}px ok")
    except Exception as e:
        print(f"{slug}: ERROR {e}")
print(f"\nTOTAL source {total_before//1024//1024}MB -> webp {total_after//1024//1024}MB ({total_after//1024}KB)")
