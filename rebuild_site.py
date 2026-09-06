from pathlib import Path
from html import escape

out = Path('/mnt/data/nepal_update_package/index.html')

sections = [
    ('INTRO', 'Viral Intro — The Question Changed', [
        ('SHOW', 'USGS — Official disaster science', 'https://www.usgs.gov/programs/landslide-hazards/science/2026-nepal-debris-avalanche-and-flash-flood', 'Official'),
        ('SHOW', 'Nature — Pre-collapse acceleration', 'https://www.nature.com/articles/d41586-026-02746-4', 'Analysis'),
        ('SHOW', 'NASA FIRMS — Thermal / fire map', 'https://firms.modaps.eosdis.nasa.gov/map/', 'Tool'),
    ]),
    ('1', 'The Collapse — What Actually Failed', [
        ('SHOW', 'USGS — Primary seismic event', 'https://earthquake.usgs.gov/earthquakes/eventpage/us7000tbwb/executive', 'Official'),
        ('SHOW', 'USGS — Landslide hazards investigation', 'https://www.usgs.gov/programs/landslide-hazards/science/2026-nepal-debris-avalanche-and-flash-flood', 'Official'),
        ('SHOW', 'USGS — Mapped debris avalanche / flood extent', 'https://www.usgs.gov/media/images/2026-nepal-debris-avalanche-and-flash-flood-map', 'Map'),
    ]),
    ('2', 'Follow the Flood — Source to Hydropower Corridor', [
        ('SHOW', 'Rasuwa Flood — Technical reconstruction', 'https://rasuwaflood.org/', 'Interactive'),
        ('SHOW', 'The Guardian — Visual guide to flood path', 'https://www.theguardian.com/world/2026/aug/27/nepal-tibet-flash-flood-visual-guide-why-how-flooding-happened-floods-cause-reason-explained', 'Visual'),
        ('SHOW', 'Reuters — Field report from destroyed valley', 'https://www.reuters.com/business/environment/flood-ravaged-nepal-valley-nothing-is-left-standing-2026-09-03/', 'Report'),
    ]),
    ('3', 'New Evidence — Mountain Moving Before Aug. 26', [
        ('SHOW', 'Nature — Satellite warning signs / acceleration', 'https://www.nature.com/articles/d41586-026-02746-4', 'Analysis'),
        ('SHOW', 'SAR analysis — Pre/post satellite sequence', 'https://blog.ringsaturn.me/en/posts/2026-08-28-langtang-sar/', 'Satellite'),
    ]),
    ('4', '10-Mile Sweep — Nepal and Tibet / China', [
        ('SHOW', 'Khabarhub — Timure dry port status, July 18', 'https://english.khabarhub.com/2026/18/559159/', 'Report'),
        ('SHOW', 'Nepal News — Timure / Rasuwagadhi photo feature', 'https://english.nepalnews.com/s/gallery/rasuwagadhi-dry-port-stalled-as-timure-customs-operates-amid-flood-ruins-photo-feature/', 'Photos'),
        ('SHOW', 'Reuters — G216 road restored after disaster', 'https://www.reuters.com/world/china/china-restores-road-access-tibet-disaster-zone-search-intensifies-2026-09-02/', 'Report'),
    ]),
    ('5', 'Why the Tunnels Are Real — Without Assuming Trigger', [
        ('SHOW', 'Reuters — Hydropower rescue inventory', 'https://www.reuters.com/world/asia-pacific/nepal-hydropower-sites-centre-flood-rescue-efforts-2026-08-31/', 'Report'),
        ('SHOW', 'AP — Workers feared trapped in hydro tunnels', 'https://apnews.com/article/744fe6e15ae7751e15efcd6dff70170c', 'Report'),
        ('SHOW', 'Rasuwagadhi Hydropower — Official project details', 'https://rghpcl.com.np/about-the-project/', 'Project'),
    ]),
    ('6', 'Upper Trishuli-1 — Documented Blasting Receipts', [
        ('SHOW', 'IFC — Upper Trishuli-1 environmental disclosure', 'https://disclosures.ifc.org/project-detail/ESRS/35701/upper-trishuli-1', 'Official'),
        ('SHOW', 'NWEDC — ESIA document archive', 'https://nwedcpl.com/esia-disclosure/', 'Documents'),
        ('SHOW', 'NWEDC — Upper Trishuli-1 project specifications', 'https://nwedcpl.com/project/upper-trishuli-1-hep-216-mw/', 'Project'),
        ('PDF', 'Download — UT-1 Blasting Impact Assessment, April 2026', 'https://nwedcpl.com/wp-content/uploads/2026/07/UT-1-Final-report-February-2-2026_NWDEC-EGC-Rev_17-April-2026_Clean.pdf', 'PDF'),
        ('PDF', 'Download — UT-1 Disaster Management Plan / project map', 'https://nwedcpl.com/wp-content/uploads/2021/04/nwedc_disclosure_7._Disaster_Management_Plan.pdf', 'PDF'),
    ]),
    ('7', 'Distance, Blast Logs and the Missing Receipt', [
        ('SHOW', 'NWEDC — UT-1 official project layout / specifications', 'https://nwedcpl.com/project/upper-trishuli-1-hep-216-mw/', 'Project'),
        ('SHOW', 'Nepal Department of Electricity Development — Project registry', 'https://doed.gov.np/pages/clhydromorethan1/', 'Official'),
        ('SHOW', 'Niti Foundation — Nepal hydropower dataset', 'https://hydro.naxa.com.np/core/datasets/', 'Dataset'),
    ]),
    ('8', 'Short Investigation — Aircraft, Military Activity and Missile Theory', [
        ('SHOW', 'Fiscal Nepal — Helicopter standby at 10:37 AM', 'https://www.fiscalnepal.com/2026/08/26/27818/bhotekoshi-flood-all-helicopter-companies-put-on-standby-for-rescue-operations/', 'Timeline'),
        ('SHOW', 'OnlineKhabar — Nepal Army helicopters sent to Rasuwa', 'https://english.onlinekhabar.com/two-army-helicopters-fly-to-rasuwa.html', 'Timeline'),
        ('SHOW', 'Radio Nepal — Army / private helicopter rescue deployment', 'https://radionepalonline.com/en/2026/08/26/434752.html', 'Timeline'),
        ('SHOW', 'Fiscal Nepal — Private helicopter mobilization', 'https://www.fiscalnepal.com/2026/08/26/27825/rasuwa-flood-rescue-altitude-air-helicopter-heads-to-disaster-zone-kailash-on-standby/', 'Timeline'),
    ]),
    ('9', 'Heat-Signature Check — NASA FIRMS', [
        ('SHOW', 'NASA FIRMS — Global active-fire map', 'https://firms.modaps.eosdis.nasa.gov/map/', 'Tool'),
        ('SHOW', 'NASA FIRMS — System overview', 'https://firms.modaps.eosdis.nasa.gov/', 'Official'),
        ('SHOW', 'NASA FIRMS — Active-fire data / limitations', 'https://firms.modaps.eosdis.nasa.gov/content/active_fire/', 'Reference'),
    ]),
    ('10', 'Why the Natural-Failure Model Is Getting Stronger', [
        ('SHOW', 'Nature — Glacier collapse / high-altitude instability', 'https://www.nature.com/articles/d41586-026-02716-w', 'Analysis'),
        ('SHOW', 'Nature — Accelerated pre-collapse movement', 'https://www.nature.com/articles/d41586-026-02746-4', 'Analysis'),
        ('SHOW', 'USGS — Official disaster science', 'https://www.usgs.gov/programs/landslide-hazards/science/2026-nepal-debris-avalanche-and-flash-flood', 'Official'),
    ]),
    ('11', 'Human Story — Tunnel Rescues, Warning and Correlated Risk', [
        ('SHOW', 'Reuters — Two workers rescued after nine days', 'https://www.reuters.com/world/china/two-people-pulled-alive-nepal-hydropower-tunnel-2026-09-04/', 'Report'),
        ('SHOW', 'Reuters — Engineers / WhatsApp tunnel rescue coordination', 'https://www.reuters.com/business/environment/how-engineers-whatsapp-group-are-guiding-nepals-flood-rescue-efforts-2026-09-04/', 'Report'),
        ('SHOW', 'Reuters — Chinese worker rescued after ten days', 'https://www.reuters.com/world/china/chinese-national-rescued-nepal-tunnel-day-after-2-nepalis-pulled-out-alive-2026-09-05/', 'Report'),
    ]),
    ('12', 'Final Evidence Board — Proven, Open, Unsupported', [
        ('SHOW', 'USGS — Disaster science', 'https://www.usgs.gov/programs/landslide-hazards/science/2026-nepal-debris-avalanche-and-flash-flood', 'Official'),
        ('SHOW', 'Nature — Pre-collapse acceleration', 'https://www.nature.com/articles/d41586-026-02746-4', 'Analysis'),
        ('SHOW', 'IFC — Blasting documentation', 'https://disclosures.ifc.org/project-detail/ESRS/35701/upper-trishuli-1', 'Official'),
        ('SHOW', 'Reuters — China G216 / Gyirong access', 'https://www.reuters.com/world/china/china-restores-road-access-tibet-disaster-zone-search-intensifies-2026-09-02/', 'Report'),
    ]),
    ('13', 'Visual Evidence — Videos Without Losing Provenance', [
        ('PLAY', 'Watch — Nepal Catastrophe source video', 'https://www.youtube.com/watch?v=5uuDFLtVlds', 'Video'),
        ('SHOW', 'Reuters — Hydropower rescue work', 'https://www.reuters.com/world/asia-pacific/nepal-hydropower-sites-centre-flood-rescue-efforts-2026-08-31/', 'Report'),
        ('SHOW', 'Reuters — Valley destruction / rescue activity', 'https://www.reuters.com/business/environment/flood-ravaged-nepal-valley-nothing-is-left-standing-2026-09-03/', 'Report'),
    ]),
    ('14', 'China-Side Findings — Confirmed vs. Black Box', [
        ('SHOW', 'Reuters — G216 access restoration', 'https://www.reuters.com/world/china/china-restores-road-access-tibet-disaster-zone-search-intensifies-2026-09-02/', 'Report'),
        ('SHOW', 'Reuters — China-side rescue work / G216 damage', 'https://www.reuters.com/business/environment/chinese-rescue-work-tibet-flood-disaster-zone-still-trudging-along-days-later-2026-09-01/', 'Report'),
    ]),
    ('15', 'What to Demand Next — Records That Can Settle This', [
        ('SHOW', 'IFC — Upper Trishuli-1 blasting / vibration disclosure', 'https://disclosures.ifc.org/project-detail/ESRS/35701/upper-trishuli-1', 'Official'),
        ('SHOW', 'Nature — Deformation evidence', 'https://www.nature.com/articles/d41586-026-02746-4', 'Analysis'),
        ('SHOW', 'Fiscal Nepal — Helicopter response timeline anchor', 'https://www.fiscalnepal.com/2026/08/26/27818/bhotekoshi-flood-all-helicopter-companies-put-on-standby-for-rescue-operations/', 'Timeline'),
        ('SHOW', 'NASA FIRMS — Thermal-map tool', 'https://firms.modaps.eosdis.nasa.gov/map/', 'Tool'),
    ]),
]

def resource_card(kind, label, url, tag):
    icon = {'SHOW':'↗','PLAY':'▶','PDF':'↓'}.get(kind,'↗')
    cls = ' video' if kind=='PLAY' else (' pdf' if kind=='PDF' else '')
    return f'''<a class="resource{cls}" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">
      <span class="ricon">{icon}</span><span class="rtext"><b>{escape(label)}</b><small>{escape(tag)}</small></span><span class="go">Open</span>
    </a>'''

nav = ''.join(f'<a href="#s-{escape(n.lower())}">{escape(n)}</a>' for n,_,_ in sections if n!='INTRO')
sec_html=[]
for i,(n,title,items) in enumerate(sections):
    cards=''.join(resource_card(*x) for x in items)
    extra=''
    if n=='13':
        extra='''<div class="video-wrap"><iframe src="https://www.youtube.com/embed/5uuDFLtVlds" title="Nepal Catastrophe: What Really Triggered the Mountain Collapse?" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'''
    sec_html.append(f'''<section class="cue" id="s-{escape(n.lower())}">
      <div class="cuehead"><span class="num">{escape(n)}</span><div><h2>{escape(title)}</h2><p>Open these in order as this chapter comes up in the livestream.</p></div></div>
      <div class="resources">{cards}</div>{extra}
    </section>''')

html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#090909">
<title>Nepal Disaster — TriggerSmart Livestream Companion</title>
<meta name="description" content="TriggerSmart host companion for the Nepal disaster livestream. Stream-order evidence buttons, embedded video, map downloads and document shortcuts.">
<style>
:root{{--bg:#070707;--panel:#111;--panel2:#161616;--line:#2b2b2b;--text:#f4f4f4;--muted:#9f9f9f;--orange:#ff5c00;--orange2:#ff7b32;--blue:#65bfff;--max:1220px}}
*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:radial-gradient(circle at 88% 0,rgba(255,92,0,.10),transparent 27%),#070707;color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.45}}
a{{color:inherit}}.wrap{{max-width:var(--max);margin:auto;padding:0 20px}}
.top{{position:sticky;top:0;z-index:30;background:rgba(7,7,7,.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}}.topin{{display:flex;min-height:64px;align-items:center;gap:18px;justify-content:space-between}}.brand{{font-weight:950;letter-spacing:.05em;white-space:nowrap}}.brand span{{color:var(--orange)}}.nav{{display:flex;gap:7px;overflow:auto;scrollbar-width:none}}.nav a{{text-decoration:none;border:1px solid #333;background:#111;border-radius:999px;padding:7px 10px;color:#bbb;font-size:.79rem;white-space:nowrap}}
.hero{{padding:36px 0 22px}}.heroBox{{border:1px solid #282828;border-radius:26px;overflow:hidden;background:linear-gradient(120deg,#111 0,#090909 52%,rgba(255,92,0,.16));padding:clamp(26px,5vw,58px)}}.eyebrow{{font-size:.74rem;color:var(--orange);font-weight:900;letter-spacing:.14em;text-transform:uppercase}}h1{{font-size:clamp(2.2rem,5vw,4.4rem);line-height:.96;letter-spacing:-.05em;margin:.35rem 0 1rem}}.hero p{{max-width:760px;color:#c5c5c5;margin:0;font-size:1.04rem}}
.quick{{display:flex;gap:9px;flex-wrap:wrap;margin:18px 0 26px}}.qbtn{{display:inline-flex;align-items:center;text-decoration:none;font-weight:850;border:1px solid #333;background:#121212;padding:10px 13px;border-radius:11px}}.qbtn.primary{{background:var(--orange);border-color:var(--orange)}}
.graphic{{margin:0 0 28px;border:1px solid var(--line);border-radius:20px;overflow:hidden;background:#090d11}}.graphic img{{display:block;width:100%;height:auto}}.graphic figcaption{{color:#999;padding:10px 13px;border-top:1px solid var(--line);font-size:.82rem}}
.notice{{border-left:4px solid var(--orange);background:#111;padding:13px 15px;border-radius:0 12px 12px 0;margin:0 0 26px;color:#cfcfcf}}.notice b{{color:white}}
.cue{{scroll-margin-top:80px;border-top:1px solid var(--line);padding:26px 0}}.cuehead{{display:flex;gap:14px;align-items:flex-start;margin-bottom:14px}}.num{{display:grid;place-items:center;min-width:44px;height:44px;padding:0 10px;background:var(--orange);border-radius:12px;font-weight:950}}.cue h2{{font-size:1.25rem;margin:0 0 3px;letter-spacing:-.01em}}.cuehead p{{margin:0;color:#818181;font-size:.86rem}}
.resources{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}.resource{{min-width:0;text-decoration:none;background:linear-gradient(135deg,#151515,#0e0e0e);border:1px solid #303030;border-radius:14px;padding:13px;display:grid;grid-template-columns:38px minmax(0,1fr) auto;align-items:center;gap:10px;transition:.15s ease}}.resource:hover{{border-color:#5d5d5d;transform:translateY(-1px)}}.resource.video{{border-color:#493020}}.resource.pdf{{border-color:#35434b}}.ricon{{display:grid;place-items:center;width:36px;height:36px;border-radius:10px;background:#222;color:var(--orange);font-weight:900;font-size:1.05rem}}.resource.video .ricon{{background:rgba(255,92,0,.16)}}.resource.pdf .ricon{{color:var(--blue);background:rgba(101,191,255,.11)}}.rtext{{min-width:0}}.rtext b{{display:block;font-size:.92rem;overflow-wrap:anywhere}}.rtext small{{display:block;color:#777;margin-top:2px;font-size:.74rem;text-transform:uppercase;letter-spacing:.08em}}.go{{font-size:.78rem;color:#bbb;border:1px solid #333;border-radius:8px;padding:6px 8px}}
.video-wrap{{position:relative;padding-top:56.25%;margin-top:13px;border:1px solid #333;border-radius:15px;overflow:hidden;background:#000;max-width:760px}}.video-wrap iframe{{position:absolute;inset:0;width:100%;height:100%;border:0}}
.footer{{color:#777;padding:34px 0 64px;border-top:1px solid var(--line)}}
@media(max-width:760px){{.topin{{align-items:flex-start;flex-direction:column;padding:10px 0}}.nav{{width:100%}}.resources{{grid-template-columns:1fr}}.wrap{{padding:0 14px}}}}
</style></head><body>
<header class="top"><div class="wrap topin"><div class="brand">TRIGGER<span>SMART</span> / HOST COMPANION</div><nav class="nav">{nav}</nav></div></header>
<main class="wrap">
<section class="hero"><div class="heroBox"><div class="eyebrow">Livestream Evidence Control Panel · Updated Sept. 5, 2026</div><h1>Nepal Disaster Investigation</h1><p>No livestream script is reproduced here. This page is a stream-order launch panel for the exact evidence, maps, videos and documents used in the current livestream.</p></div></section>
<div class="quick">
<a class="qbtn primary" href="nepal_2026_updated_livestream.txt" download>Download Current Livestream TXT</a>
<a class="qbtn" href="nepal_2026_updated_investigation_map.kmz" download>Download Google Map KMZ</a>
<a class="qbtn" href="nepal_2026_updated_investigation_map.kml" download>Download Raw KML</a>
<a class="qbtn" href="nepal_disaster_investigation_update.png" target="_blank">Open Investigation Graphic</a>
</div>
<figure class="graphic"><img src="nepal_disaster_investigation_update.png" alt="Nepal disaster investigation update infographic"><figcaption>Custom investigation graphic for the updated aircraft, heat-map, China-side infrastructure and pre-collapse movement findings.</figcaption></figure>
<div class="notice"><b>Use this page in order with the livestream.</b> Each chapter contains only the evidence controls needed at that point. Buttons open the original source in a new tab; the source video is embedded where it appears in the script. Raw URLs are intentionally not displayed.</div>
{''.join(sec_html)}
</main><footer class="wrap footer">TriggerSmart evidence companion · Built to match the current livestream source order. External sources remain the property of their respective publishers.</footer>
</body></html>'''
out.write_text(html, encoding='utf-8')
print(out)
print('bytes', out.stat().st_size)
