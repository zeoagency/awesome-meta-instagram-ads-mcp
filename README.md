# Awesome Meta & Instagram Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of MCP servers, command-line tools (CLIs), and SDKs for Meta advertising, including Facebook and Instagram ads.

## Scope

Entries must provide an implemented Meta advertising integration or a documented hosted MCP connection. This includes campaign management, advertising Insights, audiences, creatives, catalogs for ads, Meta Ad Library research, and Meta Pixel or Conversions API tooling. Multi-platform tools qualify when their Meta advertising support is explicit.

Organic-only publishing, messaging, follower tools, generic creative generators, standalone agent skills, and demonstrations using mock advertising data are outside this list. Instagram advertising support means working with Meta advertising accounts and placements; an Instagram publishing integration alone does not qualify.

## Contents

- [Meta Ads MCP servers](#meta-ads-mcp-servers)
- [Multi-platform advertising MCPs](#multi-platform-advertising-mcps)
- [Ad Library MCPs](#ad-library-mcps)
- [Pixel and Conversions API validation](#pixel-and-conversions-api-validation)
- [Command-line tools](#command-line-tools)
- [Official Business SDKs](#official-business-sdks)
- [Contributing](#contributing)

## Meta Ads MCP servers

| Project | What it does |
|---|---|
| [attainmentlabs/meta-ads-mcp](https://github.com/attainmentlabs/meta-ads-mcp) | Creates paused Meta campaigns, retrieves Insights, uploads images, and changes budgets or campaign status, with dry-run and confirmation options for selected operations. |
| [brandu-mos/konquest-meta-ads-mcp](https://github.com/brandu-mos/konquest-meta-ads-mcp) | Provides Meta campaign management, media uploads, targeting, catalogs, reporting, and tracking diagnostics. The public server includes validation and rate-limit checks. |
| [brijr/meta-mcp](https://github.com/brijr/meta-mcp) | Runs on Cloudflare Workers and manages Meta campaigns, ad sets, ads, creatives, audiences, and performance Insights through the Marketing API. |
| [byadsco/meta-ads-mcp](https://github.com/byadsco/meta-ads-mcp) | Provides Meta campaign management, reporting, audiences, creatives, and Ad Library research, with multi-tenant authentication and write pacing. |
| [dengineproblem/meta-ads-mcp-extended](https://github.com/dengineproblem/meta-ads-mcp-extended) | Extends Pipeboard's Meta Ads MCP with campaign status controls, lookalike audiences, conversion events, batch operations, and resumable video uploads. |
| [EfrainTorres/armavita-meta-ads-mcp](https://github.com/EfrainTorres/armavita-meta-ads-mcp) | Local Rust server for Meta campaigns, reporting, audiences, lead forms, catalogs, media, Ad Library searches, and conversion events, with mutation previews. |
| [gomarble-ai/facebook-ads-mcp-server](https://github.com/gomarble-ai/facebook-ads-mcp-server) | Read-only server for Meta ad accounts, campaigns, ad sets, ads, creatives, performance Insights, and activity history. |
| [mikusnuz/meta-ads-mcp](https://github.com/mikusnuz/meta-ads-mcp) | Supports Meta campaign management, targeting, audiences, creatives, catalogs, Insights reporting, automated rules, Ad Library searches, and Conversions API events. |
| [oliverames/meta-mcp-server](https://github.com/oliverames/meta-mcp-server) | Supports Meta campaign management, Insights reporting, audiences, Ad Library searches, and Conversions API events within a broader Meta platform server. |
| [pipeboard-co/meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp) | Manages Meta campaigns and ads, creative uploads, budgets, targeting, Insights reporting, and Ad Library searches, with local and remote connection options. |
| [serkanhaslak/meta-mcp](https://github.com/serkanhaslak/meta-mcp) | MCP server and REST gateway for Meta campaign management, audiences, creatives, Insights reporting, automated rules, and Conversions API events. |

## Multi-platform advertising MCPs

Hosted entries below provide remote MCP connection manifests and documented Meta advertising operations. Their server implementations are hosted by their providers.

| Project | Delivery | Meta advertising support |
|---|---|---|
| [amekala/ads-mcp](https://github.com/amekala/ads-mcp) | Hosted Adspirer MCP | Documents Meta campaign management, creatives, lead forms, and performance analysis alongside other advertising platforms. |
| [Draivix/aidvertaiser](https://github.com/Draivix/aidvertaiser) | Self-hosted MCP server | Implements Meta campaign and ad management, audiences, creatives, reporting, and conversion tracking alongside Google advertising and analytics services. |
| [irinabuht12-oss/google-ads-meta-ads-mcp](https://github.com/irinabuht12-oss/google-ads-meta-ads-mcp) | Hosted Ryze MCP | Documents Meta account discovery, Insights queries, creative and lead-form access, Ad Library searches, and Graph API operations alongside Google Ads and GA4. |
| [markifact/markifact-mcp](https://github.com/markifact/markifact-mcp) | Hosted Markifact MCP | Documents Meta campaign creation, creative updates, audiences, and performance reporting alongside other advertising platforms. |

## Ad Library MCPs

| Project | What it does |
|---|---|
| [proxy-intell/facebook-ads-library-mcp](https://github.com/proxy-intell/facebook-ads-library-mcp) | Searches advertiser pages and retrieves public Meta Ad Library ads through the third-party ScrapeCreators API, with creative media analysis and caching tools. |
| [RamsesAguirre777/facebook-ads-library-mcp](https://github.com/RamsesAguirre777/facebook-ads-library-mcp) | Scrapes the public Facebook Ad Library with a headless browser to return ad copy, creative links, advertiser details, and landing pages. |

## Pixel and Conversions API validation

| Project | Type | What it does |
|---|---|---|
| [aleksUIX/pixellint](https://github.com/aleksUIX/pixellint) | CLI, MCP server, library | Validates Meta Pixel requests and Conversions API payloads against vendor rules. Also supports other analytics vendors. |

## Command-line tools

| Project | What it does |
|---|---|
| [Meta Ads CLI](https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-cli/ads-cli-overview) | Official Meta command-line interface for creating and managing advertising campaigns and debugging Marketing API objects from the terminal. |
| [attainmentlabs/meta-ads-cli](https://github.com/attainmentlabs/meta-ads-cli) | Python CLI for creating campaigns from YAML, uploading creatives, querying performance, and managing budgets and campaign status, with dry-run support. |
| [Enriquefft/meta-cli](https://github.com/Enriquefft/meta-cli) | Go CLI and MCP server for creating campaigns, configuring targeting, uploading creatives, and managing ads through the Meta Marketing API. |
| [holdenjrussell/meta-ads-cli](https://github.com/holdenjrussell/meta-ads-cli) | Python CLI for reporting performance, staging creatives, launching campaigns, and updating budgets through account-specific configuration and preview-before-execution workflows. |

## Official Business SDKs

These Meta-maintained SDKs expose Marketing API advertising objects for Facebook and Instagram ads.

| SDK | Package | What it does |
|---|---|---|
| [Java](https://github.com/facebook/facebook-java-business-sdk) | `com.facebook.business.sdk:facebook-java-business-sdk` | Provides typed advertising requests, campaign management, ad account queries, and batch Marketing API operations. |
| [JavaScript / Node.js](https://github.com/facebook/facebook-nodejs-business-sdk) | `facebook-nodejs-business-sdk` | Provides advertising objects, campaign creation, ad account access, and paginated Marketing API queries. |
| [PHP](https://github.com/facebook/facebook-php-business-sdk) | `facebook/php-business-sdk` | Provides advertising object classes for campaign creation, ad set configuration, account access, and Insights reporting. |
| [Python](https://github.com/facebook/facebook-python-business-sdk) | `facebook_business` | Provides Marketing API objects for campaign management, ad account access, and Insights reporting. |
| [Ruby](https://github.com/facebook/facebook-ruby-business-sdk) | `facebookbusiness` | Provides advertising object classes, campaign edges, ad account queries, and batched Marketing API requests. |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria and the source verification checklist. Add each project once, under its primary category, with a short factual description and a direct upstream link.
