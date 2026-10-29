#!/usr/bin/env python3
"""Build the self-contained profile artwork. Python standard library only."""
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ASSETS.mkdir(exist_ok=True)


def field():
    # A family of tilted ellipses. Two copies drift out of phase, producing
    # slow interference rather than a loading-spinner rotation.
    ellipses = []
    for i in range(64):
        angle = math.pi * i / 64
        rx = 188 + 14 * math.sin(3 * angle)
        ry = 72 + 12 * math.cos(2 * angle)
        ellipses.append(f'<ellipse rx="{rx:.3f}" ry="{ry:.3f}" transform="rotate({180 * i / 64:.4f})"/>')
    return '<g transform="scale(1 .88)">' + ''.join(ellipses) + '</g>'


FIELD = field()
STYLE = '''
  .phase-a { animation: phase-a 32s cubic-bezier(.45,0,.55,1) infinite alternate; }
  .phase-b { animation: phase-b 43s cubic-bezier(.45,0,.55,1) infinite alternate; }
  @keyframes phase-a { from { transform: rotate(-9deg) scale(.97); } to { transform: rotate(9deg) scale(1.03); } }
  @keyframes phase-b { from { transform: rotate(7deg) scale(1.025); } to { transform: rotate(-7deg) scale(.975); } }
  @media (prefers-reduced-motion: reduce) { .phase-a, .phase-b { animation: none !important; } }
'''


def sculpture(color, prefix='field', static=False):
    a = '' if static else ' class="phase-a"'
    b = '' if static else ' class="phase-b"'
    return f'''<defs><g id="{prefix}">{FIELD}</g></defs>
    <g fill="none" stroke="{color}" stroke-width=".6" stroke-linejoin="round">
      <g{a} opacity=".62"><use href="#{prefix}"/></g>
      <g{b} opacity=".24"><use href="#{prefix}"/></g>
    </g>'''


def hero(theme, mobile=False, static=False):
    bg, fg, muted, rule = ('#080808', '#f5f5f5', '#a3a3a3', '#333333') if theme == 'dark' else ('#fafafa', '#111111', '#666666', '#d4d4d4')
    width, height = (720, 900) if mobile else (1280, 640)
    if mobile:
        typography = f'''
        <text x="48" y="69" class="meta" fill="{muted}">ZHUGEHYUK / SEOUL, EARTH</text>
        <text x="43" y="213" class="name" font-size="132" letter-spacing="-9">icedac<tspan font-size="58" dx="10">.</tspan></text>
        <text x="48" y="266" class="body">Systems, agents &amp; experiments.</text>
        <g transform="translate(360 533) scale(1.14)">{sculpture(fg, static=static)}</g>
        <path d="M48 801H672" stroke="{rule}"/>
        <text x="48" y="849" class="meta" fill="{muted}">A CONTINUOUS WORK IN PROGRESS</text>
        '''
    else:
        typography = f'''
        <text x="64" y="76" class="meta" fill="{muted}">ZHUGEHYUK / SEOUL, EARTH</text>
        <text x="1216" y="76" text-anchor="end" class="meta" fill="{muted}">CONTINUOUS STUDY — 01</text>
        <text x="55" y="324" class="name" font-size="148" letter-spacing="-10">icedac<tspan font-size="64" dx="12">.</tspan></text>
        <text x="64" y="387" class="body">Systems, agents</text>
        <text x="64" y="425" class="body">&amp; experiments.</text>
        <g transform="translate(938 316) scale(1.1)">{sculpture(fg, static=static)}</g>
        <path d="M64 548H1216" stroke="{rule}"/>
        <text x="64" y="593" class="meta" fill="{muted}">A CONTINUOUS WORK IN PROGRESS</text>
        <text x="1216" y="593" text-anchor="end" class="meta" fill="{muted}">2LAB.AI ↗</text>
        '''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
    <title id="title">icedac — zhugehyuk</title>
    <desc id="desc">Systems, agents and experiments. Seoul, Earth. A continuous work in progress. Fine monochrome ellipses slowly drift into an interference sculpture.</desc>
    <style>{'' if static else STYLE}
    text {{ fill: {fg}; }}
    .name {{ font-family: 'Avenir Next', 'Trebuchet MS', sans-serif; font-weight: 500; }}
    .body {{ font-family: 'Avenir Next', 'Trebuchet MS', sans-serif; font-size: 28px; font-weight: 400; }}
    .meta {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace; font-size: 14px; letter-spacing: 1.5px; }}
    </style>
    <rect width="{width}" height="{height}" fill="{bg}"/>
    {typography}
    </svg>'''


for theme in ('dark', 'light'):
    for mobile in (False, True):
        suffix = '-mobile' if mobile else ''
        for static in (False, True):
            mode = '-still' if static else ''
            (ASSETS / f'profile-{theme}{suffix}{mode}.svg').write_text(hero(theme, mobile, static))

template = (ROOT / 'tools' / 'preview.template.html').read_text()
art = f'<svg viewBox="-240 -240 480 480" role="img" aria-label="Slowly shifting monochrome interference sculpture"><style>{STYLE}</style>{sculpture("currentColor", "preview-field")}</svg>'
(ROOT / 'preview.html').write_text(template.replace('<!-- SCULPTURE -->', art))
print('Built 8 SVG variants and preview.html; no network or third-party dependencies.')
