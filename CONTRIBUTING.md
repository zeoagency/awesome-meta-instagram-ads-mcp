# Contributing

This directory groups MCPs by what their registered tools actually do. CLI and SDK companions are listed separately.

## Add or update an MCP

1. Pin an upstream commit or a versioned hosted schema. Inspect the actual registration path; README feature claims do not establish tools.
2. Enumerate the full tool list, following pagination. Capture exact names, complete descriptions, and full JSON input schemas, including nested fields, required arguments, enums, defaults, constraints, and referenced definitions.
3. Inspect each tool implementation. Label its scope `meta-ads`, `supporting`, or `unrelated`; assign its capability from its behavior. A generic Graph transport needs explicit implemented advertising usage to qualify.
4. Include pinned source links and extraction evidence. Explain conditional registrations, private modules, dependency constraints, and unavailable descriptions. Never infer a schema from a tool name or promotional text.
5. Add the reviewed snapshot to `catalog/`. Run `python tooling/render_catalog.py` to update the MCP page, capability directory, coverage page, and complete tool-name index. Run `uv run --with jsonschema tooling/check_catalog.py` to check full-schema coverage and local links. Review the generated changes.

A complete public/open-core inventory can qualify when proprietary modules are absent and that limitation is explicit. A hosted MCP needs an accessible full `tools/list` response or complete provider-published schemas; connection manifests and example workflows alone are insufficient for the detailed catalog. Record failed or incomplete extractions on the coverage page instead of ranking them as verified inventories.

## Keep the scope focused

Qualifying tools work with Meta advertising campaigns, Insights, audiences, ad creatives, advertising catalogs, lead ads, Ad Library research, or Meta Pixel/Conversions API integration and validation. Multi-platform servers qualify through their implemented Meta tools. Keep every tool in each snapshot, including unrelated tools, so readers can see the complete server surface; unrelated tools never determine its advertising groups.

Exclude standalone skills, prompts, generic image generators, organic-only social tools, and mock-data demonstrations. CLI and SDK entries must implement advertising operations and belong in [companions](docs/companions.md).

Use concise English around verbatim upstream definitions. Do not add star rankings, promotional tiers, unsupported safety guarantees, or general marketing guides. A tool inventory establishes its exposed interface; it does not prove that authenticated live advertising operations succeed.
