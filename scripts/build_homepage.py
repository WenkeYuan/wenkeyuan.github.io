"""Build the GitHub Pages artifact using only the Python standard library."""
from pathlib import Path
import re, html, shutil, json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
OUT.mkdir(exist_ok=True)

def markdown(text):
    text = html.escape(text)
    text = text.replace('\\*', '&#42;')
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1 ↗</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*]+)\*', r'<em>\1</em>', text)
    return text.replace('\\*', '*')

rows = json.loads((ROOT / 'homepage-publications.json').read_text())

publication_html = ''.join(f'<article class="paper" data-category="{html.escape(p["category"])}"><span class="paper-type">{html.escape(p["category"])}</span><p>{markdown(p["text"])}</p></article>' for p in rows)
awards = [
    ('future-network-achievement-2025.jpg', 'Future Network Achievement', '2025 · First student contributor'),
    ('iccc-best-student-paper-2025.png', 'Best Student Paper', 'ICCC 2025'),
    ('innovation-competition-silver-2025.jpg', 'Innovation Competition · Silver', '2025'),
    ('icaus-best-paper-2024.png', 'Best Paper', 'ICAUS 2024'),
    ('icaus-best-poster-2024.png', 'Best Poster', 'ICAUS 2024'),
]
award_html = ''.join(f'<a class="award" href="images/awards/{file}" target="_blank" rel="noopener"><img src="images/awards/{file}" alt="{title}" loading="lazy"><h3>{title}</h3><p>{subtitle} ↗</p></a>' for file,title,subtitle in awards)
template = (ROOT / 'homepage.html').read_text()
(OUT / 'index.html').write_text(template.replace('{{PUBLICATIONS}}', publication_html).replace('{{AWARDS}}', award_html))
for name in ('homepage.css', 'homepage.js'):
    shutil.copy2(ROOT / name, OUT / name)
(OUT / 'images/awards').mkdir(parents=True, exist_ok=True)
shutil.copy2(ROOT / 'images/ywk2.png', OUT / 'images/ywk2.png')
for file,_,_ in awards:
    shutil.copy2(ROOT / 'images/awards' / file, OUT / 'images/awards' / file)
(OUT / '.nojekyll').touch()
print(f'Built {len(rows)} publications and {len(awards)} awards into {OUT}')
