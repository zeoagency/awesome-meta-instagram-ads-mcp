"""Render reviewed MCP snapshots into GitHub-readable catalog pages (stdlib only)."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    'reporting': ('Measure advertising performance', 'Query Insights, delivery, spend, attribution, and breakdowns.'),
    'campaigns-read': ('Inspect campaign structure', 'List and inspect campaigns, ad sets, ads, statuses, and object relationships.'),
    'campaigns': ('Launch and change campaigns', 'Create, update, pause, and delete campaigns, ad sets, and ads.'),
    'creatives': ('Build and upload ad creatives', 'Upload media, assemble creatives, and inspect ad assets.'),
    'audiences': ('Find and manage audiences', 'Search targeting, manage custom audiences, and build lookalikes.'),
    'tracking': ('Send and validate conversion signals', 'Work with pixels, conversion events, datasets, and tracking validation.'),
    'ad-library': ('Research public ads', 'Search the Ad Library and inspect competitor advertising.'),
    'catalogs': ('Manage advertising catalogs', 'Work with product catalogs, feeds, and product sets for ads.'),
    'leads': ('Work with lead ads', 'Manage lead forms and retrieve advertising leads.'),
    'automation': ('Automate and control changes', 'Create rules, batch operations, and preview or confirm mutations.'),
    'accounts': ('Connect advertising accounts', 'Discover accounts, permissions, businesses, pages, and advertising identities.'),
    'dispatch': ('Discover and dispatch advertising operations', 'Find operation IDs, retrieve operation-specific input schemas, and dispatch read or write requests through a shared router.'),
    'utilities': ('Inspect and troubleshoot integrations', 'Inspect available APIs, authentication, validation rules, and local supporting data.'),
}

def anchor(value):
    return re.sub(r'[^a-z0-9_-]', '-', value.lower())

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', '<br>')

def render():
    records = [json.loads(p.read_text()) for p in sorted((ROOT/'catalog').glob('*.json'))]
    assert records, 'No snapshots'
    for r in records:
        assert r.get('reviewed'), f"Unreviewed snapshot: {r['id']}"
        assert re.fullmatch(r'[0-9a-f]{40}', r['commit'])
        names = [t['name'] for t in r['tools']]
        assert len(names) == len(set(names)), f"Duplicate tools: {r['id']}"
        for t in r['tools']:
            assert isinstance(t['description'], str)
            assert isinstance(t['inputSchema'], dict)
            assert 'source' in t and t['scope'] in {'meta-ads','supporting','unrelated'}
            assert t['capability'] in GROUPS or t['capability'] == 'unrelated'
    pages = ROOT/'docs'/'mcp'
    pages.mkdir(parents=True, exist_ok=True)
    index = ['# Tool index', '', '[Back to the directory](../README.md)', '',
             'Every captured tool name links to its provider and full input schema. Search this page with your browser’s Find command or use GitHub search. Names shared by several MCPs appear once per provider.', '',
             '| Tool | MCP | Capability |', '|---|---|---|']
    entries = []
    targets = {}
    for r in records:
        total = len(r['tools'])
        title = r['repo']
        state = 'Complete registered tool snapshot' if r['complete'] else 'Incomplete extraction — excluded from the capability directory'
        page = [f'# {title}', '', '[Directory](../../README.md) · [Tool index](../tool-index.md) · '
                f"[Upstream]({r['url']}) · [Machine-readable snapshot](../../catalog/{r['id']}.json)", '',
                f"{state}. **{total} tools captured.**", '',
                'Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.', '',
                f"Repository revision: [`{r['commit'][:12]}`]({r['url']}/tree/{r['commit']}). Method: `{r['method']}`.", '']
        if r.get('displayNotes',r['notes']):
            page += [f'- {note}' for note in r.get('displayNotes',r['notes'])] + ['']
        if total:
            page += ['## Tools', ''] + [f"- [{t['name']}](#{anchor(t['name'])})" for t in sorted(r['tools'],key=lambda t:t['name'])] + ['']
        for t in sorted(r['tools'],key=lambda t:t['name']):
            a=anchor(t['name'])
            page += [f'<a id="{a}"></a>', '', f"## `{t['name']}`", '',
                     f"Scope: **{t['scope']}** · Capability: **{t['capability']}** · [Definition]({t['source']})", '',
                     t['description'] or '*Upstream supplies no description.*', '',
                     *([f"Availability: {t['availability']}", ''] if t.get('availability') else []),
                     *(['### Source parameter notes', '', t['parameterNotes'], ''] if t.get('parameterNotes') else []),
                     *([f"Implementation note: {t['implementationNote']}", ''] if t.get('implementationNote') else []),
                     '<details>', '<summary>Full input schema</summary>', '', '```json',
                     json.dumps(t['inputSchema'],ensure_ascii=False,indent=2), '```', '', '</details>', '']
            entries.append((t['name'],r,t))
        for t in r['tools']:
            targets[(r['id'],t['name'])]=f"{r['id']}.md"
        if len('\n'.join(page).encode()) > 650_000:
            ordered=sorted(r['tools'],key=lambda t:t['name'])
            starts=[page.index(f'<a id="{anchor(t["name"])}"></a>') for t in ordered]
            header=page[:starts[0]]
            for part,offset in enumerate(range(0,len(ordered),35),1):
                filename=f"{r['id']}-part-{part}.md"
                end=min(offset+35,len(ordered))
                blocks=page[starts[offset]:starts[end] if end<len(starts) else len(page)]
                content=[f'# {r["repo"]} — tools {offset+1}–{end}', '',f'[All tools]({r["id"]}.md) · [Tool index](../tool-index.md)', '',*blocks]
                (pages/filename).write_text('\n'.join(content)+'\n')
                for t in ordered[offset:end]:
                    targets[(r['id'],t['name'])]=filename
                    old=f"- [{t['name']}](#{anchor(t['name'])})"
                    new=f"- [{t['name']}]({filename}#{anchor(t['name'])})"
                    header=[new if item==old else item for item in header]
            page=header
        (pages/f"{r['id']}.md").write_text('\n'.join(page)+'\n')
    for name,r,t in sorted(entries,key=lambda x:(x[0].lower(),x[1]['repo'].lower())):
        index.append(f"| [`{cell(name)}`](mcp/{targets[(r['id'],name)]}#{anchor(name)}) | [{r['repo']}](mcp/{r['id']}.md) | {t['capability']} |")
    (ROOT/'docs'/'tool-index.md').write_text('\n'.join(index)+'\n')
    complete=[r for r in records if r['complete'] and any(t['scope']=='meta-ads' for t in r['tools'])]
    n=sum(t['scope']=='meta-ads' for r in complete for t in r['tools'])
    readme=['# Awesome Meta & Instagram Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)', '',
            '> Discover what you can do with Meta and Instagram advertising MCP tools — from launching campaigns to researching competitors and validating conversions.', '',
            f"**{len(complete)} MCPs · {n} advertising tools.** Browse by task below, or [search every tool name](docs/tool-index.md). Each MCP page contains its full tool descriptions and input schemas.", '',
            'Groups come from registered tools and their implementations. A server can appear in several groups. Supporting and unrelated tools remain visible on its full snapshot page, but unrelated tools do not earn advertising capabilities. Counts describe reviewed source or provider-schema snapshots; optional registrations are included where documented. Live advertising operations were not tested.', '',
            '## Browse by task', '']
    for key,(label,_) in GROUPS.items():
        members=[r for r in complete if any(t['capability']==key and t['scope']!='unrelated' and not t.get('unavailable') for t in r['tools'])]
        if members: readme.append(f'- [{label}](#{anchor(label.replace(" ","-"))})')
    readme += ['- [CLI and SDK companions](docs/companions.md)', '- [Extraction coverage](docs/coverage.md)', '',]
    for key,(label,desc) in GROUPS.items():
        members=[r for r in complete if any(t['capability']==key and t['scope']!='unrelated' and not t.get('unavailable') for t in r['tools'])]
        if not members: continue
        readme += [f'## {label}', '', desc, '', '| MCP | Verified tool examples | Full inventory |','|---|---|---|']
        for r in sorted(members,key=lambda r:r['repo'].lower()):
            ts=[t for t in r['tools'] if t['capability']==key and t['scope']!='unrelated' and not t.get('unavailable')]
            examples=' · '.join(f"[`{cell(t['name'])}`](docs/mcp/{targets[(r['id'],t['name'])]}#{anchor(t['name'])})" for t in ts[:3])
            readme.append(f"| [{r['repo']}](docs/mcp/{r['id']}.md) | {examples} | {len(r['tools'])} tools |")
        readme.append('')
    readme += ['## Contributing', '', 'Add a source-backed tool snapshot and its evidence before adding a server. See [CONTRIBUTING.md](CONTRIBUTING.md).', '']
    (ROOT/'README.md').write_text('\n'.join(readme))
    coverage=['# Extraction coverage', '', '[Back to the directory](../README.md)', '',
              'One extraction per MCP, followed by independent source review. Only complete inventories with source-backed or provider-schema-backed Meta advertising tools enter the capability directory. Hosted documentation alone does not establish a full tool schema.', '',
              '| MCP | Result | Captured tools | Method |','|---|---|---|---|']
    for r in records:
        state='Complete' if r['complete'] else 'Incomplete; excluded'
        coverage.append(f"| [{r['repo']}](mcp/{r['id']}.md) | {state} | {len(r['tools'])} | {r['method']} |")
    coverage += ['', 'Tool enumeration and schema inspection do not execute campaigns or establish that live API calls succeed. Source links pin public code revisions; hosted manifests are dated snapshots of provider definitions. Extraction limitations are recorded on each MCP page.', '']
    (ROOT/'docs'/'coverage.md').write_text('\n'.join(coverage))
    print(f'Rendered {len(records)} pages, {len(entries)} tool records, {len(complete)} eligible MCPs.')

if __name__=='__main__':
    render()
