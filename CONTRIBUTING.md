# Contributing to Awesome Meta & Instagram Ads MCP

Thank you for contributing! This repository maintains a curated, high-signal index of Model Context Protocol (MCP) servers and agent-facing tooling specifically for **Meta Ads and Instagram Ads automation**.

---

## Scope & Inclusion Guidelines

To maintain focus and utility for performance marketing engineers and agency developers, submissions must strictly satisfy the following criteria:

### In Scope
- **Meta Marketing API Integrations:** Campaign, ad set, ad, and creative CRUD, budget scheduling, bidding strategy adjustments, and Advantage+ automation.
- **Instagram Advertising Specializations:** Creative asset staging for Instagram placements (Feed, Stories, Reels, Explore), aspect ratio linting (`9:16`, `4:5`, `1:1`), and Instagram Business Account actor binding.
- **Conversion Tracking & Telemetry:** Meta Conversions API (CAPI) event dispatch, server-side deduplication (`event_id`), SHA-256 PII formatting, and Meta Pixel validation.
- **Targeting & Custom Audiences:** Custom Audience syncing (CRM customer lists, website visitors), Lookalike Audience generation, and detailed targeting search.
- **Dynamic Product Catalogs:** Commerce Manager catalog feeds, product set batch updates, and Advantage+ catalog ads.
- **Reporting & Ad Intelligence:** Marketing API Insights reporting, breakdown dimensions, and Meta Ad Library competitor scraping.

### Out of Scope (Will Be Rejected)
- ❌ **Organic-Only Social Tooling:** Tools that schedule organic Facebook Page posts, publish organic Instagram feed photos, or read user profiles.
- ❌ **Direct Messaging (DM) & Social Inbox Bots:** Customer service bots for Instagram Messaging or Facebook Messenger (unless explicitly configured for Click-to-Direct ad lead attribution).
- ❌ **Comment Moderation & Social Listening:** Tools scraping organic post discussions or managing comments.
- ❌ **Threads.net Organic Publishing:** Tools publishing to Threads via the organic Threads API.
- ❌ **Generic Customer Support WhatsApp Bots:** WhatsApp Baileys or Cloud API messaging tools without paid ad campaign or CAPI attribution.
- ❌ **Generic Graph API Wrappers:** Unspecialized SDK wrappers lacking advertising tools, schemas, or agent prompts.

---

## Submission Checklist

When opening a Pull Request to add a project:

1. **Repository Quality:** The project must have a clear `README.md`, open source code, and working installation instructions.
2. **Table Entry:** Add the project under its **single primary subcategory** in `README.md`:
   ```markdown
   | [**owner/repo**](https://github.com/owner/repo) | Concise factual description of what it actually does (15–25 words, third-person present tense). |
   ```
3. **Comparison Matrix:** Add a row to the `## Developer Comparison Matrix` documenting its API surface, mutation capability, dry-run mode, multi-account routing, CAPI support, runtime, and tools count.
4. **Link Integrity:** Ensure internal anchors match the format `<a id="owner-repo"></a>`.
5. **Formatting:** Avoid marketing hype, buzzwords, or unverified claims.
