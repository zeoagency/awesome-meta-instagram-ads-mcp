"""Check snapshot schemas, generated tool coverage, and local Markdown links."""
import json
import re
from pathlib import Path
from urllib.parse import unquote
from jsonschema import validators

ROOT=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in (ROOT/'catalog').glob('*.json')]
count=0
for r in records:
    page=ROOT/'docs/mcp'/f"{r['id']}.md"
    text=page.read_text()+'\n'+'\n'.join(p.read_text() for p in page.parent.glob(f"{r['id']}-part-*.md"))
    assert r['reviewed']
    for t in r['tools']:
        validators.validator_for(t['inputSchema']).check_schema(t['inputSchema'])
        assert f"## `{t['name']}`" in text
        assert t['source'] in text
        assert not t['description'] or t['description'] in text
        assert json.dumps(t['inputSchema'],ensure_ascii=False,indent=2) in text
        count+=1
index=(ROOT/'docs/tool-index.md').read_text()
assert len(re.findall(r'^\| \[`',index,re.M))==count
for r in records:
    for t in r['tools']:
        assert any(f"[`{t['name']}`]" in line and f"(mcp/{r['id']}.md)" in line for line in index.splitlines()), (r['id'],t['name'])
for path in [ROOT/'README.md',ROOT/'CONTRIBUTING.md',*ROOT.glob('docs/**/*.md')]:
    text=path.read_text()
    for link in re.findall(r'\]\(([^)]+)\)',text):
        if link.startswith(('https://','http://')):continue
        target,_,fragment=link.partition('#')
        dest=(path.parent/unquote(target)).resolve() if target else path
        assert dest.is_file(),(path,link)
        if fragment:
            content=dest.read_text()
            anchors=set(re.findall(r'<a id="([^"]+)"',content))
            for h in re.findall(r'^#+ (.*)$',content,re.M):
                anchors.add(re.sub(r'[^\w -]','',h.lower()).replace(' ','-'))
            assert fragment in anchors,(path,link)
print(f'Validated {len(records)} snapshots, {count} schemas, full tool index coverage, and all local links.')
