# Contributing to Awesome Meta & Instagram Ads MCP

This list includes MCP servers, command-line tools (CLIs), and SDKs with explicit Meta advertising support, including Facebook and Instagram ads.

## Inclusion criteria

A project must satisfy both requirements:

1. It implements an MCP server, advertising CLI, or relevant SDK/library; or it provides a usable hosted MCP connection with documented Meta advertising operations.
2. Its primary documentation and implementation, or its hosted connection manifest and documented operations, demonstrate Meta advertising functionality: campaign/ad management, advertising Insights, targeting or audiences, ad creatives, catalogs for ads, Ad Library research, or Meta Pixel/Conversions API integration and validation.

Multi-platform projects qualify when their Meta advertising integration is explicit. Official Business SDKs qualify because they implement Marketing API advertising objects. Projects with multiple interfaces appear once, with those interfaces identified in the entry.

## Exclusions

- Organic-only publishing, profiles, followers, messaging, moderation, and social listening tools.
- Standalone agent skills, prompts, setup scripts, and workflow collections that only use another project's MCP, CLI, or SDK.
- Generic creative or image generators without a Meta advertising integration.
- Mock-data demonstrations presented as real advertising integrations.
- General-purpose Graph API wrappers without implemented advertising objects or operations.
- Advertising guides, courses, general marketing resources, and unrelated tools.

## Verify before submitting

- Read the upstream documentation and inspect the relevant source files, tool registrations, and package or CLI entry points. A project name or an SDK dependency alone is insufficient evidence.
- For hosted MCPs, verify the remote connection manifest and documented Meta operations. Label the entry as hosted; do not imply that the repository contains the server implementation.
- Confirm that the upstream link resolves and provides installation or connection instructions.
- Distinguish read-only reporting from campaign mutations. Distinguish public Ad Library scraping, third-party scraping APIs, and the official Meta Ad Library API.
- Describe implemented behavior. Do not convert plans, optional proprietary modules, skills, or examples into shipped features.
- Include the supporting upstream documentation and source links in your pull request. State whether verification used source inspection, hosted-service documentation, or live execution.

## Entry format

Add one entry under its primary category, following the existing table format:

```markdown
| [owner/repo](https://github.com/owner/repo) | Short factual description of its Meta advertising functionality. |
```

Use the additional delivery, type, or package columns where the category includes them. Keep descriptions concise and written in English. Sort entries alphabetically within each category, with the official Meta CLI first in its category.

Avoid star counts, tool totals, undocumented rankings, marketing language, untested performance claims, and blanket safety or compliance guarantees. Update the contents links when changing categories, and check that all local links and table rows remain valid.
