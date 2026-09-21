# Awesome Meta & Instagram Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of Model Context Protocol (MCP) servers and agentic tools for **[Meta Ads](https://developers.facebook.com/docs/marketing-apis/)** and **[Instagram Ads](https://developers.facebook.com/docs/instagram-platform/)** automation.

Official links: [Meta for Developers](https://developers.facebook.com/) · [Marketing API Reference](https://developers.facebook.com/docs/marketing-apis/) · [Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/) · [Meta Ad Library](https://www.facebook.com/ads/library/) · [Model Context Protocol](https://modelcontextprotocol.io/)

---

## Contents

- [**Developer Comparison Matrix (27)**](#developer-comparison-matrix)
1. [Campaign lifecycle and budget execution (9)](#1-campaign-lifecycle-and-budget-execution)
   - [Automated campaign and ad set launching (4)](#automated-campaign-and-ad-set-launching)
   - [Budget pacing and automated pause triggers (3)](#budget-pacing-and-automated-pause-triggers)
   - [Mutation safety gates and dry-run execution (2)](#mutation-safety-gates-and-dry-run-execution)
2. [Performance reporting and Insights analytics (4)](#2-performance-reporting-and-insights-analytics)
   - [Real-time Marketing API Insights reporting (3)](#real-time-marketing-api-insights-reporting)
   - [SQLite and edge-cached reporting daemons (1)](#sqlite-and-edge-cached-reporting-daemons)
3. [Cross-platform advertising orchestrators (7)](#3-cross-platform-advertising-orchestrators)
   - [Universal advertising routers and schema abstractions (3)](#universal-advertising-routers-and-schema-abstractions)
   - [Multi-channel performance marketing skill packs (4)](#multi-channel-performance-marketing-skill-packs)
4. [Conversion tracking and CAPI engineering (2)](#4-conversion-tracking-and-capi-engineering)
   - [Conversions API (CAPI) event dispatch (1)](#conversions-api-capi-event-dispatch)
   - [Pixel validation and SHA-256 PII linters (1)](#pixel-validation-and-sha-256-pii-linters)
5. [Creative intelligence and Ad Library discovery (5)](#5-creative-intelligence-and-ad-library-discovery)
   - [Meta Ad Library competitor intelligence (2)](#meta-ad-library-competitor-intelligence)
   - [Ad creative generation and asset staging (3)](#ad-creative-generation-and-asset-staging)
- [Resources](#resources)
- [Reference](#reference)
- [Contributing](#contributing)

---

## Developer Comparison Matrix

*27 projects. Side-by-side technical comparison across API mutations, dynamic multi-account routing, server-side CAPI tracking, and safety guardrails. Project names jump directly to their detailed section entries.*

| Project | Stars | Writes | Multi-Acc | CAPI | Ad Lib | Safety | Runtime | Tier |
|---|---|---|---|:---:|:---:|---|---|---|
| [**byadsco/meta-ads-mcp**](#byadsco-meta-ads-mcp) | ⭐ 16 | ✅ CRUD | ✅ Dynamic | ✅ | ✅ | 🛡️ Paced | TypeScript | Tier 1 |
| [**oliverames/meta-mcp-server**](#oliverames-meta-mcp-server) | ⭐ 36 | ✅ CRUD | ✅ Dynamic | — | ✅ | — | TypeScript | Tier 1 |
| [**Draivix/aidvertaiser**](#draivix-aidvertaiser) | ⭐ 20 | ✅ CRUD | ✅ Dynamic | ✅ | — | — | Python | Tier 1 |
| [**mikusnuz/meta-ads-mcp**](#mikusnuz-meta-ads-mcp) | ⭐ 79 | ✅ CRUD | ✅ Dynamic | — | ✅ | — | TypeScript | Tier 2 |
| [**brandu-mos/konquest-meta-ads-mcp**](#brandu-mos-konquest-meta-ads-mcp) | ⭐ 44 | ✅ CRUD | ✅ Dynamic | — | — | — | Python | Tier 1 |
| [**gomarble-ai/facebook-ads-mcp-server**](#gomarble-ai-facebook-ads-mcp-server) | ⭐ 366 | 🔍 Read | ✅ Dynamic | — | — | — | Python | Tier 2 |
| [**dengineproblem/meta-ads-mcp-extended**](#dengineproblem-meta-ads-mcp-extended) | ⭐ 8 | ✅ CRUD | ✅ Dynamic | ✅ | ✅ | 🛡️ Paced | Python | Tier 2 |
| [**attainmentlabs/meta-ads-mcp**](#attainmentlabs-meta-ads-mcp) | ⭐ 13 | ✅ CRUD | ⚠️ Single | ✅ | — | 🛡️ Dry-Run | Python | Tier 2 |
| [**EfrainTorres/armavita-meta-ads-mcp**](#efraintorres-armavita-meta-ads-mcp) | ⭐ 74 | ✅ CRUD | ✅ Dynamic | ✅ | ✅ | 🛡️ Dry-Run | Rust | Tier 1 |
| [**pipeboard-co/meta-ads-mcp**](#pipeboard-co-meta-ads-mcp) | ⭐ 1.3k | ✅ CRUD | ✅ Dynamic | — | ✅ | — | Python | Tier 1 |
| [**serkanhaslak/meta-mcp**](#serkanhaslak-meta-mcp) | ⭐ 10 | ✅ CRUD | ✅ Dynamic | ✅ | — | 🛡️ Paced | TypeScript | Tier 1 |
| [**mathiaschu/meta-ads-analyzer**](#mathiaschu-meta-ads-analyzer) | ⭐ 429 | 🔍 Read | ⚠️ Single | — | — | — | Python/Skill | Tier 2 |
| [**brijr/meta-mcp**](#brijr-meta-mcp) | ⭐ 200 | ✅ CRUD | ✅ Dynamic | — | — | — | TypeScript | Tier 1 |
| [**markifact/markifact-mcp**](#markifact-markifact-mcp) | ⭐ 48 | ✅ CRUD | ✅ Dynamic | — | — | 🛡️ Dry-Run | TypeScript | Tier 1 |
| [**amekala/ads-mcp**](#amekala-ads-mcp) | ⭐ 94 | ✅ CRUD | ✅ Dynamic | — | ✅ | 🛡️ Dry-Run | Python/Skill | Tier 1 |
| [**itallstartedwithaidea/advertising-hub**](#itallstartedwithaidea-advertising-hub) | ⭐ 42 | ✅ CRUD | ✅ Dynamic | ✅ | ✅ | — | Python/Skill | Tier 1 |
| [**irinabuht12-oss/google-meta-ads-ga4-mcp**](#irinabuht12-oss-google-meta-ads-ga4-mcp) | ⭐ 2.0k | ✅ CRUD | ✅ Dynamic | — | ✅ | — | Python/Skill | Tier 1 |
| [**irinabuht12-oss/marketing-skills**](#irinabuht12-oss-marketing-skills) | ⭐ 1.6k | 🔍 Read | ✅ Dynamic | — | ✅ | — | Python/Skill | Tier 2 |
| [**eduardocornelsen/full-funnel-ai-analytics**](#eduardocornelsen-full-funnel-ai-analytics) | ⭐ 22 | 🔍 Read | ⚠️ Single | — | — | 🛡️ Dry-Run | Python | Tier 2 |
| [**Dataslayer-AI/Marketing-skills**](#dataslayer-ai-marketing-skills) | ⭐ 23 | 🔍 Read | ✅ Dynamic | — | — | — | Python | Tier 1 |
| [**Lifecycle-Innovations-Limited/claude-ops**](#lifecycle-innovations-limited-claude-ops) | ⭐ 210 | 🔍 Read | ✅ Dynamic | ✅ | ✅ | 🛡️ Dry-Run | Python/Skill | Tier 1 |
| [**aleksUIX/pixellint**](#aleksuix-pixellint) | ⭐ 0 | 🔍 Read | ✅ Dynamic | ✅ | — | — | Rust | Tier 1 |
| [**proxy-intell/facebook-ads-library-mcp**](#proxy-intell-facebook-ads-library-mcp) | ⭐ 300 | 🔍 Read | ⚠️ Single | — | ✅ | — | Python | Tier 1 |
| [**RamsesAguirre777/facebook-ads-library-mcp**](#ramsesaguirre777-facebook-ads-library-mcp) | ⭐ 256 | 🔍 Read | ⚠️ Single | — | ✅ | — | Python | Tier 2 |
| [**DV0x/creative-ad-agent**](#dv0x-creative-ad-agent) | ⭐ 117 | 🔍 Read | ⚠️ Single | — | ✅ | — | TypeScript | Tier 2 |
| [**tenfoldmarc/meta-ads-generator-skill**](#tenfoldmarc-meta-ads-generator-skill) | ⭐ 22 | 🔍 Read | ⚠️ Single | — | ✅ | — | Python/Skill | Tier 3 |
| [**guimatheus92/mcp-video-analyzer**](#guimatheus92-mcp-video-analyzer) | ⭐ 71 | 🔍 Read | ⚠️ Single | — | — | 🛡️ Dry-Run | TypeScript | Tier 2 |

---

## 1. Campaign lifecycle and budget execution

*9 projects. Servers and agent tools that launch campaigns, adjust flight schedules, update ad set budgets, and enforce mutation guardrails.*

### Automated campaign and ad set launching

*4 projects. Tools capable of creating new campaigns, configuring targeting parameters, and publishing ad sets to the Meta Marketing API.*

| Project | What it does |
|---|---|
| <a id="byadsco-meta-ads-mcp"></a>[**byadsco/meta-ads-mcp**](https://github.com/byadsco/meta-ads-mcp) | Enterprise TypeScript MCP server with 142 tools, Firestore multi-tenant token vaulting, Gemini 2.0 creative video auditing, and a proactive write-pacing daemon designed to prevent Meta API checkpoint bans. |
| <a id="oliverames-meta-mcp-server"></a>[**oliverames/meta-mcp-server**](https://github.com/oliverames/meta-mcp-server) | Comprehensive 200-tool server covering the full Meta Marketing API, Instagram Graph, and Business Portfolios with multi-account asset traversal. |
| <a id="draivix-aidvertaiser"></a>[**Draivix/aidvertaiser**](https://github.com/Draivix/aidvertaiser) | AI-assisted advertising execution platform with 50 tools for generating creative copy variants, calculating budget distributions, and launching live Meta ad campaigns. |
| <a id="mikusnuz-meta-ads-mcp"></a>[**mikusnuz/meta-ads-mcp**](https://github.com/mikusnuz/meta-ads-mcp) | Deep 134-tool TypeScript server implementing granular ad set targeting parameters, custom audience lookups, and campaign lifecycle mutations. |

### Budget pacing and automated pause triggers

*3 projects. Servers designed to monitor spend pacing, clamp daily budgets, and autonomously pause underperforming ad sets.*

| Project | What it does |
|---|---|
| <a id="brandu-mos-konquest-meta-ads-mcp"></a>[**brandu-mos/konquest-meta-ads-mcp**](https://github.com/brandu-mos/konquest-meta-ads-mcp) | Safety-first Meta Ads MCP server designed for agency teams, featuring 57 tools, daily budget caps, spend velocity monitors, and automated pause triggers. |
| <a id="gomarble-ai-facebook-ads-mcp-server"></a>[**gomarble-ai/facebook-ads-mcp-server**](https://github.com/gomarble-ai/facebook-ads-mcp-server) | Python FastMCP server tailored for e-commerce performance marketers, providing 21 tools for spend threshold alerts and automated campaign pausing. |
| <a id="dengineproblem-meta-ads-mcp-extended"></a>[**dengineproblem/meta-ads-mcp-extended**](https://github.com/dengineproblem/meta-ads-mcp-extended) | Extended Python FastMCP server offering 59 tools for ad set flight scheduling, dayparting adjustments, and placement-level budget pacing. |

### Mutation safety gates and dry-run execution

*2 projects. Safety-first frameworks that enforce dry-run approvals, spend rate-limits, and append-only audit trails before committing changes.*

| Project | What it does |
|---|---|
| <a id="attainmentlabs-meta-ads-mcp"></a>[**attainmentlabs/meta-ads-mcp**](https://github.com/attainmentlabs/meta-ads-mcp) | Safety-first Python FastMCP server with 13 tools enforcing mandatory dry-run approvals, daily mutation limits, and append-only audit logs. |
| <a id="efraintorres-armavita-meta-ads-mcp"></a>[**EfrainTorres/armavita-meta-ads-mcp**](https://github.com/EfrainTorres/armavita-meta-ads-mcp) | High-throughput Rust native Marketing API server providing 125 tools with async connection pooling, strict type checking, and mutation safeguards. |

---

## 2. Performance reporting and Insights analytics

*4 projects. Read-only servers, breakdown analyzers, and local caching daemons querying the Marketing API Insights endpoints.*

### Real-time Marketing API Insights reporting

*3 projects. Live query bridges calculating ROAS, CPA, click-through rates, and attribution metrics directly from Meta Graph API.*

| Project | What it does |
|---|---|
| <a id="pipeboard-co-meta-ads-mcp"></a>[**pipeboard-co/meta-ads-mcp**](https://github.com/pipeboard-co/meta-ads-mcp) | Flagship agency-ready FastMCP server backed by official OAuth 2.0 PKCE, 42 tools, 59 automated test suites, and read-only Insights performance reporting. |
| <a id="serkanhaslak-meta-mcp"></a>[**serkanhaslak/meta-mcp**](https://github.com/serkanhaslak/meta-mcp) | Cloud-hosted MCP and REST gateway exposing 77 tools for querying ad account insights, delivery statuses, and campaign metrics. |
| <a id="mathiaschu-meta-ads-analyzer"></a>[**mathiaschu/meta-ads-analyzer**](https://github.com/mathiaschu/meta-ads-analyzer) | Automated Insights analytics engine calculating day-over-day CPA/ROAS variances and breakdown effect anomalies across placements. |

### SQLite and edge-cached reporting daemons

*1 project. Implementation running an edge Cloudflare D1 SQLite worker to shield the agent from Meta rate limits.*

| Project | What it does |
|---|---|
| <a id="brijr-meta-mcp"></a>[**brijr/meta-mcp**](https://github.com/brijr/meta-mcp) | Serverless TypeScript MCP server deployed on Cloudflare Workers, using an edge D1 SQLite cache to answer performance queries in 12ms. |

---

## 3. Cross-platform advertising orchestrators

*7 projects. Multi-network hubs and skill packs coordinating Meta Ads alongside Google Ads, TikTok, LinkedIn, and GA4.*

### Universal advertising routers and schema abstractions

*3 projects. Normalized multi-platform MCP routers abstracting ad concepts across Meta and complementary advertising networks.*

| Project | What it does |
|---|---|
| <a id="markifact-markifact-mcp"></a>[**markifact/markifact-mcp**](https://github.com/markifact/markifact-mcp) | Ultra-lean 8-tool dynamic dispatch router (<1,800 prompt tokens) coordinating cross-platform ad campaigns across Meta and Google Ads with human-in-the-loop gates. |
| <a id="amekala-ads-mcp"></a>[**amekala/ads-mcp**](https://github.com/amekala/ads-mcp) | Sophisticated multi-platform router with 20 tools normalizing advertising operations across Meta Ads, Google Ads, TikTok Ads, and LinkedIn Ads. |
| <a id="itallstartedwithaidea-advertising-hub"></a>[**itallstartedwithaidea/advertising-hub**](https://github.com/itallstartedwithaidea/advertising-hub) | Standardized cross-platform advertising MCP specification and FastMCP template defining universal campaign, ad set, and reporting schemas. |

### Multi-channel performance marketing skill packs

*4 projects. Curated agent instructions and operational prompt libraries for cross-channel advertising analytics and execution.*

| Project | What it does |
|---|---|
| <a id="irinabuht12-oss-google-meta-ads-ga4-mcp"></a>[**irinabuht12-oss/google-meta-ads-ga4-mcp**](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) | Turnkey hosted multi-service platform featuring 250 tools that unifies Meta Ads, Google Ads, and GA4 analytics into a cohesive agent workspace. |
| <a id="irinabuht12-oss-marketing-skills"></a>[**irinabuht12-oss/marketing-skills**](https://github.com/irinabuht12-oss/marketing-skills) | Domain-specific operational skill library teaching Claude Code agents how to structure multi-channel ad audits, ROAS benchmarks, and pacing reports. |
| <a id="eduardocornelsen-full-funnel-ai-analytics"></a>[**eduardocornelsen/full-funnel-ai-analytics**](https://github.com/eduardocornelsen/full-funnel-ai-analytics) | Full-funnel marketing analytics server with 5 tools combining Meta Ads top-of-funnel reach metrics with post-click conversion analytics. |
| <a id="dataslayer-ai-marketing-skills"></a>[**Dataslayer-AI/Marketing-skills**](https://github.com/Dataslayer-AI/Marketing-skills) | Specialized prompt engineering and schema skill pack connecting LLM agents to Dataslayer's multi-platform ad data connectors. |

---

## 4. Conversion tracking and CAPI engineering

*2 projects. Server-side event dispatchers and offline tracking linters enforcing Meta Conversions API (CAPI) contracts.*

### Conversions API (CAPI) event dispatch

*1 project. Operations engines that transmit server-side conversion payloads with deduplication and event match quality checks.*

| Project | What it does |
|---|---|
| <a id="lifecycle-innovations-limited-claude-ops"></a>[**Lifecycle-Innovations-Limited/claude-ops**](https://github.com/Lifecycle-Innovations-Limited/claude-ops) | Enterprise operations engine with 66 tools providing secure, production-grade Meta Conversions API (CAPI) event dispatch and telemetry logging. |

### Pixel validation and SHA-256 PII linters

*1 project. Static analysis engines verifying Meta Pixel events, URL leak hazards, and SHA-256 hashing format compliance.*

| Project | What it does |
|---|---|
| <a id="aleksuix-pixellint"></a>[**aleksUIX/pixellint**](https://github.com/aleksUIX/pixellint) | Static linting and verification engine written in pure Rust that audits Meta Pixel tags and CAPI payloads for SHA-256 PII compliance. |

---

## 5. Creative intelligence and Ad Library discovery

*5 projects. Competitor ad scrapers, creative hook synthesizers, and aspect-ratio linters for Instagram and Facebook placements.*

### Meta Ad Library competitor intelligence

*2 projects. Specialized scrapers querying the Meta Ad Library API for active competitor creatives, copy variants, and spend estimates.*

| Project | What it does |
|---|---|
| <a id="proxy-intell-facebook-ads-library-mcp"></a>[**proxy-intell/facebook-ads-library-mcp**](https://github.com/proxy-intell/facebook-ads-library-mcp) | Ad Library scraping server with 8 tools and residential proxy rotation for querying competitor ad creatives, copy variants, and active spend. |
| <a id="ramsesaguirre777-facebook-ads-library-mcp"></a>[**RamsesAguirre777/facebook-ads-library-mcp**](https://github.com/RamsesAguirre777/facebook-ads-library-mcp) | Focused FastMCP server with 2 tools for querying the official Meta Ad Library API to inspect brand transparency data and active ads. |

### Ad creative generation and asset staging

*3 projects. Generative AI creative assistants producing hook copy, carousel formats, and Instagram-compatible aspect ratios.*

| Project | What it does |
|---|---|
| <a id="dv0x-creative-ad-agent"></a>[**DV0x/creative-ad-agent**](https://github.com/DV0x/creative-ad-agent) | Creative production co-pilot with 2 in-process tools that analyzes Ad Library exemplars and generates hook-first static and carousel concepts. |
| <a id="tenfoldmarc-meta-ads-generator-skill"></a>[**tenfoldmarc/meta-ads-generator-skill**](https://github.com/tenfoldmarc/meta-ads-generator-skill) | Claude Code agent skill designed to guide models through generating compliant Meta ad copy, headline variations, and creative staging files. |
| <a id="guimatheus92-mcp-video-analyzer"></a>[**guimatheus92/mcp-video-analyzer**](https://github.com/guimatheus92/mcp-video-analyzer) | Multimodal video analysis server with 8 tools for evaluating video ad hooks, transcript pacing, and creative aspect ratios for Instagram Reels. |

---

## Resources

- **[Meta Marketing API Official Documentation](https://developers.facebook.com/docs/marketing-apis/)**: The primary documentation covering campaigns, ad sets, creatives, and budget structures.
- **[Meta Conversions API (CAPI) Overview](https://developers.facebook.com/docs/marketing-api/conversions-api/)**: Guide for wiring server-side web and offline conversion events.
- **[Meta Graph API Explorer](https://developers.facebook.com/tools/explorer/)**: Interactive tool to test access tokens, permissions, and Marketing API endpoints.
- **[Meta Ad Library API](https://www.facebook.com/ads/library/api/)**: Official programmatic interface for querying advertising transparency and active ads.
- **[Model Context Protocol Specification](https://modelcontextprotocol.io/)**: Open protocol connecting LLM desktop clients (Claude, Cursor, Windsurf) to local/remote tool servers.

## Reference

- **System User Tokens vs User Access Tokens:** Production MCP deployments require a Meta Business Manager System User token with `ads_management` and `ads_read` scopes to prevent session expiry.
- **Rate Limit Headers (`X-Business-Use-Case-Usage`):** Meta throttles ad accounts per business use case. Production servers must parse this header and pace writes before reaching 100% capacity.
- **Event Deduplication (`event_id` & `external_id`):** When combining browser Meta Pixel with server-side CAPI, both events must share an identical `event_id` within a 48-hour deduplication window.
- **Advantage+ & Dynamic Creative Schemas:** Automated creative variations require nesting `asset_feed_spec` objects inside `adcreative` payloads rather than static image hashes.

---

## Contributing

Contributions are welcome! Please ensure that suggested MCP servers strictly interact with the **Meta Marketing API, CAPI, or ad infrastructure**. Organic-only social media tools will be excluded to preserve the repository's focus.

