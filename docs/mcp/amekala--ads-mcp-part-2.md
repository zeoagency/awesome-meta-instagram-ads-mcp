# amekala/ads-mcp — tools 36–70

[All tools](amekala--ads-mcp.md) · [Tool index](../tool-index.md)

<a id="add_sitelinks"></a>

## `add_sitelinks`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add sitelink extensions to a campaign.

Sitelinks are clickable links to specific pages on your website.
Recommended 4-6 sitelinks per campaign.

**CONSTRAINTS:**
- link_text max 25 characters
- description1 max 35 characters (optional)
- description2 max 35 characters (required if description1 is set)

**EXAMPLE SITELINKS:**
{
    "link_text": "How It Works",
    "final_url": "https://example.com/how-it-works",
    "description1": "See the platform in action",
    "description2": "Step-by-step walkthrough"
}

{
    "link_text": "Pricing",
    "final_url": "https://example.com/pricing",
    "description1": "Affordable plans for all",
    "description2": "Start free today"
}

**Parameters:**
- campaign_id: The campaign ID (REQUIRED). Get from list_campaigns.
- sitelinks: List of sitelink objects with link_text, final_url, and optional descriptions.
- customer_id: Optional Google Ads customer ID

**Execution time:** 2-5 seconds

**When to use:**
- User wants to add sitelinks to their campaign
- User asks about adding more links to ads
- User asks about extensions, ad enhancements, or assets generally — sitelinks
  are the highest-impact extension; offer them FIRST (before callouts /
  structured snippets) whenever a user asks to improve or extend an ad/campaign
- After creating a campaign, proactively suggest adding sitelinks

**Example:**
User: "Add sitelinks to my campaign" / "How do I add extensions?" / "Make my ads better"
Agent:
1. Uses list_campaigns to get campaign_id
2. Uses add_sitelinks with relevant page links (Services, Pricing, About, Contact)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding sitelink extensions to a campaign.\n\nSitelinks are clickable links to specific pages on your website.\nRecommended 4-6 sitelinks per campaign.\n\nEXAMPLE:\n    {\n        \"link_text\": \"How It Works\",\n        \"final_url\": \"https://example.com/how-it-works\",\n        \"description1\": \"See the platform in action\",\n        \"description2\": \"Step-by-step walkthrough\"\n    }\n\nConstraints:\n- link_text max 25 characters\n- description1 max 35 characters (optional)\n- description2 max 35 characters (required if description1 set)",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to add sitelinks to. Get from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "sitelinks": {
      "description": "List of sitelink objects. Each has 'link_text' (max 25 chars), 'final_url', and optional 'description1'/'description2' (max 35 chars each).",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Sitelinks",
      "type": "array"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    },
    "ad_group_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional. Pin sitelinks to a SPECIFIC ad group instead of the whole campaign. Use when the campaign has themed ad groups (e.g. Men's vs Women's products) and you want sitelinks per theme so the links shown match each ad group's intent. Per Google's specificity rules, ad-group sitelinks override campaign-level sitelinks for that ad group. Get ad group IDs from get_campaign_structure or list_ad_groups.",
      "title": "Ad Group Id"
    }
  },
  "required": [
    "campaign_id",
    "sitelinks"
  ],
  "title": "AddSitelinksInput",
  "type": "object"
}
```

</details>

<a id="add_structured_snippets"></a>

## `add_structured_snippets`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add structured snippet extensions to a campaign.

Structured snippets highlight specific aspects of your products/services.

**VALID HEADERS:**
- AMENITIES, BRANDS, COURSES, DEGREE_PROGRAMS, DESTINATIONS
- FEATURED_HOTELS, INSURANCE_COVERAGE, MODELS, NEIGHBORHOODS
- SERVICE_CATALOG, SHOWS, STYLES, TYPES

**RULES:**
- Header must be from predefined list
- 3-10 values required per snippet
- Each value max 25 characters

**EXAMPLES:**
For SaaS/Platform:
    Header: "Types"
    Values: ["Google Ads", "Meta Ads", "LinkedIn Ads", "TikTok Ads"]

For Services:
    Header: "Services" (maps to SERVICE_CATALOG)
    Values: ["Campaign Launch", "Analytics", "Optimization", "Reporting"]

For Brands:
    Header: "Brands"
    Values: ["Nike", "Adidas", "Puma", "New Balance"]

**Parameters:**
- campaign_id: The campaign ID (REQUIRED). Get from list_campaigns.
- snippets: List of {header, values} objects (REQUIRED).
- customer_id: Optional Google Ads customer ID

**Execution time:** 2-5 seconds

**When to use:**
- User wants to add structured snippets
- User asks to highlight product types, services, or brands
- After creating a campaign, suggest adding snippets

**Example:**
User: "Add structured snippets showing our ad platform types"
Agent:
1. Uses list_campaigns to get campaign_id
2. Uses add_structured_snippets with header "Types" and relevant values

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding structured snippet extensions to a campaign.\n\nStructured snippets highlight specific aspects of your products/services.\n\nValid Headers: AMENITIES, BRANDS, COURSES, DEGREE_PROGRAMS, DESTINATIONS,\nFEATURED_HOTELS, INSURANCE_COVERAGE, MODELS, NEIGHBORHOODS, SERVICE_CATALOG,\nSHOWS, STYLES, TYPES\n\nEXAMPLE for SaaS:\n    Header: \"Types\"\n    Values: [\"Google Ads\", \"Meta Ads\", \"LinkedIn Ads\", \"TikTok Ads\"]\n\nEXAMPLE for Services:\n    Header: \"Services\" (maps to SERVICE_CATALOG)\n    Values: [\"Campaign Launch\", \"Analytics\", \"Optimization\", \"Reporting\"]",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to add snippets to. Get from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "snippets": {
      "description": "List of snippet objects. Each has 'header' (from valid list) and 'values' (3-10 strings, each max 25 chars). Example: [{'header': 'Types', 'values': ['Google Ads', 'Meta Ads', 'LinkedIn Ads']}]",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Snippets",
      "type": "array"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    },
    "ad_group_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional. Pin structured snippets to a SPECIFIC ad group instead of the whole campaign. Use when ad groups target distinct themes and need different snippet content. Get ad group IDs from get_campaign_structure or list_ad_groups.",
      "title": "Ad Group Id"
    }
  },
  "required": [
    "campaign_id",
    "snippets"
  ],
  "title": "AddStructuredSnippetsInput",
  "type": "object"
}
```

</details>

<a id="analyze_meta_ad_performance"></a>

## `analyze_meta_ad_performance`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants detailed analysis of specific Meta ads, creative performance, or wants to identify winning/losing ad variations.

This tool provides ad-level and creative-level insights for Meta campaigns.

Returns:
- Top performing ads by CTR and conversion rate
- Underperforming ads that need attention
- Creative fatigue indicators (high frequency, declining CTR)
- Video completion metrics (25%, 50%, 75%, 100% watched)
- Creative optimization recommendations

When to use this tool:
- "Which of my Meta ads are performing best?"
- "Are any of my Facebook ads fatigued?"
- "Show me my Instagram video ad performance"
- "Which creatives should I pause?"
- "Analyze my ad variations"

Parameters:
- lookback_days: 7, 14, 30 (default), 60, or 90 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- campaign_id: Optional - filter to specific campaign
- include_video_metrics: true (default) or false
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 1-3 seconds (cached database query)
Data source: ad_group_daily_metrics table (Meta ad sets stored as ad groups)

Creative fatigue detection:
- High frequency (>4.0) with declining CTR
- CTR dropped >20% from first week
- Same creative running >14 days without refresh

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta ad/creative performance analysis",
  "properties": {
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date (YYYY-MM-DD). If provided with end_date, overrides lookback_days for custom date range queries.",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date (YYYY-MM-DD). If provided with start_date, overrides lookback_days for custom date range queries.",
      "title": "End Date"
    },
    "date_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Date range preset: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. Overrides lookback_days. Ignored if start_date/end_date are provided.",
      "title": "Date Range"
    },
    "raw_data": {
      "default": false,
      "description": "If true, return ONLY raw metrics as a JSON code block (spend, clicks, impressions, conversions, CPA, CPC, CTR, CVR, ROAS by campaign/ad/date). Strips severity labels, suggested bids/budgets, industry benchmarks, and optimization recommendations. Use when you run your own attribution model or want to minimize token usage.",
      "title": "Raw Data",
      "type": "boolean"
    },
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze (7, 14, 30, 60, or 90 days). Default is 30 days.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter to specific campaign ID (optional - analyzes all campaigns if not provided)",
      "title": "Campaign Id"
    },
    "include_video_metrics": {
      "default": true,
      "description": "Include video completion metrics (25%, 50%, 75%, 100% watched). Default is true.",
      "title": "Include Video Metrics",
      "type": "boolean"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of ads to return (default 100, max 200). Use with offset for pagination.",
      "title": "Limit",
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of ads to skip for pagination (default 0). Use with limit to get next page.",
      "title": "Offset",
      "type": "integer"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Ad Account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    }
  },
  "title": "MetaAdPerformanceInput",
  "type": "object"
}
```

</details>

<a id="analyze_meta_audiences"></a>

## `analyze_meta_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks about Meta/Facebook/Instagram audience performance by demographics, age group or gender targeting optimization, audience saturation, or which demographic segments to target or exclude.

This tool provides deep analysis of audience segment performance and detects audience saturation to optimize demographic targeting for Meta Ads.

Returns:
- Age group performance breakdown (18-24, 25-34, 35-44, 45-54, 55-64, 65+)
- Gender performance breakdown (male, female, unknown)
- Age + Gender combination analysis
- Segments categorized as SCALE/MAINTAIN/REDUCE/EXCLUDE based on ROAS
- Audience saturation score (0-100) with contributing factors
- Best performing segments to scale
- Underperforming segments to reduce/exclude
- Targeting optimization recommendations
- Quick actionable items

When to use this tool:
- "Which age groups perform best for my Meta ads?"
- "Should I target men or women on Facebook?"
- "Is my Meta audience saturated?"
- "Which demographics should I exclude?"
- "Analyze my Instagram audience performance"
- "Best demographic targeting for my Facebook campaigns"
- "Age and gender breakdown for my Meta ads"
- "Are my lookalike audiences exhausted?"
- "Which audience segments are wasting money?"

Parameters:
- lookback_days: 7, 14, 30 (default), 60, or 90 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- breakdown_type: 'age', 'gender', 'age_gender', or 'all' (default)
- include_saturation: Include saturation analysis (default: True)
- target_roas: Optional override (default: from account goals or 2.0x)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 2-5 seconds (cached database query with analysis)
Data source: meta_audience_daily_metrics table (demographic-level daily metrics)

ROAS Thresholds for Segment Recommendations:
- 🚀 SCALE (ROAS ≥ 1.5x target): Increase budget to this segment
- ➖ MAINTAIN (ROAS 0.75x-1.5x target): Keep current allocation
- ⚠️ REDUCE (ROAS 0.5x-0.75x target): Decrease budget
- 🔴 EXCLUDE (ROAS < 0.5x target): Remove from targeting

Saturation Score Factors (weighted):
- Frequency Score (35%): How often users see ads (>3 indicates fatigue)
- CTR Decline Score (30%): Week-over-week CTR changes
- CPA Increase Score (25%): Rising cost per acquisition
- Reach Saturation Score (10%): Audience reach exhaustion

Saturation Levels:
- ✅ HEALTHY (<40): Audience is fresh, continue scaling
- 🟡 AT_RISK (40-69): Monitor frequency, prepare new audiences
- 🔴 SATURATED (≥70): Expand targeting or refresh creatives

Common Insights:
- Age 25-44 typically has highest ROAS for e-commerce
- Gender targeting varies significantly by product category
- High frequency (>4) combined with declining CTR indicates saturation
- Lookalike audiences can exhaust within 4-8 weeks at high spend

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta audience performance analysis",
  "properties": {
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date (YYYY-MM-DD). If provided with end_date, overrides lookback_days for custom date range queries.",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date (YYYY-MM-DD). If provided with start_date, overrides lookback_days for custom date range queries.",
      "title": "End Date"
    },
    "date_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Date range preset: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. Overrides lookback_days. Ignored if start_date/end_date are provided.",
      "title": "Date Range"
    },
    "raw_data": {
      "default": false,
      "description": "If true, return ONLY raw metrics as a JSON code block (spend, clicks, impressions, conversions, CPA, CPC, CTR, CVR, ROAS by campaign/ad/date). Strips severity labels, suggested bids/budgets, industry benchmarks, and optimization recommendations. Use when you run your own attribution model or want to minimize token usage.",
      "title": "Raw Data",
      "type": "boolean"
    },
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze (7, 14, 30, 60, or 90 days). Default is 30 days.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "breakdown_type": {
      "default": "all",
      "description": "Type of audience breakdown: 'age' (age groups), 'gender', 'age_gender' (combined), or 'all' (default).",
      "title": "Breakdown Type",
      "type": "string"
    },
    "include_saturation": {
      "default": true,
      "description": "Include audience saturation analysis for lookalike and custom audiences (default: True).",
      "title": "Include Saturation",
      "type": "boolean"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional target ROAS override (e.g., 3.0 for 3.0x ROAS). If not provided, will use account goals or historical average.",
      "title": "Target Roas"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Ad Account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    }
  },
  "title": "MetaAudienceAnalysisInput",
  "type": "object"
}
```

</details>

<a id="analyze_meta_catalog_performance"></a>

## `analyze_meta_catalog_performance`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to analyze how their Advantage+ Catalog / Dynamic Product Ads are performing AT THE PRODUCT or PRODUCT-SET level. Keywords: "which products are selling", "catalog performance", "best/worst products", "product ROAS", "product set performance", "which SKUs are wasting money".

Breaks catalog performance down by PRODUCT and PRODUCT SET (the campaign-level perf tools can't do this). Returns:
- Top products by catalog-attributed ROAS, and underperforming products (below target)
- Products spending with ZERO conversions (the catalog waste signal) and zero-impression products
- Per-product-set ROAS comparison + the funnel (views → carts → checkouts → purchases)
- Units sold, and actionable recommendations (scale winners, exclude losers, shift budget between sets)

Uses the same target-ROAS, severity and data-confidence conventions as the other performance tools. Reads cached nightly product metrics — if none exist yet, says so.

When to use: "How are my catalog products doing?", "Which products should I scale or pause?", "What's my ROAS by product set?"

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Advantage+ Catalog (DPA) performance by product + product set.",
  "properties": {
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze: 7, 30, 60, 90, or 120 (default 30).",
      "title": "Lookback Days",
      "type": "integer"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional target ROAS override (e.g. 3.0). Defaults to the account goal, else 90-day average, else 2.0x.",
      "title": "Target Roas"
    },
    "product_set_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional product set ID to scope the analysis to one set.",
      "title": "Product Set Id"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date YYYY-MM-DD (overrides lookback_days with end_date).",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date YYYY-MM-DD (overrides lookback_days with start_date).",
      "title": "End Date"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta ad account ID. Required for multi-account users.",
      "title": "Ad Account Id"
    }
  },
  "title": "AnalyzeMetaCatalogPerformanceInput",
  "type": "object"
}
```

</details>

<a id="analyze_meta_wasted_spend"></a>

## `analyze_meta_wasted_spend`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks about Meta/Facebook/Instagram ad spend efficiency, wasted money, underperforming campaigns, placement optimization, or creative fatigue.

This tool identifies Meta Ads campaigns and placements that are wasting money by performing below target ROAS or below breakeven (ROAS < 1.0). It extends the base wasted spend detector with Meta-specific features:

Returns:
- Campaign-level wasted spend analysis (ROAS < 1.0 = actual losses)
- Underperforming spend analysis (1.0 <= ROAS < target = opportunity cost)
- Placement-level breakdown (which placements are wasting money: Feed, Stories, Reels, etc.)
- Creative fatigue detection (high frequency + declining CTR)
- Actionable recommendations for campaigns, placements, and creatives
- Quick action items

When to use this tool:
- "Where am I wasting money on Meta/Facebook ads?"
- "Which Meta placements should I exclude?"
- "Are any of my Facebook creatives fatigued?"
- "How can I reduce wasted ad spend on Instagram?"
- "Which Meta campaigns are losing money?"
- "What's my Meta ROAS by placement?"

Parameters:
- lookback_days: 7, 30 (default), 60, 90, or 120 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- target_roas: Optional override (e.g., 3.0 for 3.0x ROAS)
- include_placements: true (default) - Include placement-level analysis
- include_fatigue: true (default) - Include creative fatigue analysis
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 2-5 seconds (cached database query with analysis)
Data source: campaign_daily_metrics + meta_placement_daily_metrics + meta_ad_creative_metrics tables

Key definitions:
- Wasted Spend (ROAS < 1.0): Actual money lost - for every $1 spent, getting back <$1
- Underperforming (1.0 <= ROAS < target): Profitable but below target - opportunity cost
- Creative Fatigue: Ads with frequency >4x (cold traffic) or >7x (retargeting) showing declining CTR

Meta-specific placement optimization:
- Audience Network often has lowest ROAS - consider excluding
- Instagram Stories/Reels typically perform differently than Feed
- Facebook Marketplace can waste spend if not relevant

**Quick Actions (IMPORTANT — read severity context first):**
- ⏳ LEARNING campaigns → Do NOT pause. Monitor for 14+ days before judging.
- ❓ INSUFFICIENT_DATA campaigns → Need more spend before analysis is meaningful.
- 🚨 CRITICAL campaigns (established, 14+ days, ZERO conversions) → Consider pausing
- 🚨 CRITICAL campaigns (established, 14+ days, HAS conversions) → Review performance, verify revenue in ad platform before reducing budget
- 🔴 HIGH severity (established, 14+ days) → Consider reducing budget by 50-70%
- 🟡 MEDIUM → Optimize targeting, ad copy, landing pages

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta wasted spend analysis with placement and fatigue detection",
  "properties": {
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date (YYYY-MM-DD). If provided with end_date, overrides lookback_days for custom date range queries.",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date (YYYY-MM-DD). If provided with start_date, overrides lookback_days for custom date range queries.",
      "title": "End Date"
    },
    "date_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Date range preset: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. Overrides lookback_days. Ignored if start_date/end_date are provided.",
      "title": "Date Range"
    },
    "raw_data": {
      "default": false,
      "description": "If true, return ONLY raw metrics as a JSON code block (spend, clicks, impressions, conversions, CPA, CPC, CTR, CVR, ROAS by campaign/ad/date). Strips severity labels, suggested bids/budgets, industry benchmarks, and optimization recommendations. Use when you run your own attribution model or want to minimize token usage.",
      "title": "Raw Data",
      "type": "boolean"
    },
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze (7, 30, 60, 90, or 120 days). Default is 30 days.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional target ROAS override (e.g., 3.0 for 3.0x ROAS). If not provided, will use account goals or historical average.",
      "title": "Target Roas"
    },
    "include_placements": {
      "default": true,
      "description": "Include placement-level analysis (Feed, Stories, Reels, etc.). Default is true.",
      "title": "Include Placements",
      "type": "boolean"
    },
    "include_fatigue": {
      "default": true,
      "description": "Include creative fatigue analysis. Default is true.",
      "title": "Include Fatigue",
      "type": "boolean"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Ad Account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    }
  },
  "title": "MetaWastedSpendAnalysisInput",
  "type": "object"
}
```

</details>

<a id="analyze_pmax_search_categories"></a>

## `analyze_pmax_search_categories`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

See the search CATEGORIES a Performance Max campaign matched (grouped queries), with metrics.

⚠️ READ-ONLY. Safe to call repeatedly.

This reads campaign_search_term_insight — Google's aggregated view that groups a
Performance Max campaign's queries into search categories (themes), each with its
own clicks, impressions, conversions, and conversion value. It complements
`analyze_pmax_search_terms` (individual terms): categories show the shape of demand
at a theme level. Google returns a residual "(Other search terms)" bucket for
long-tail queries it doesn't categorize.

**High-volume — this pages** (same interface as analyze_pmax_search_terms):
- `sort_by`: impressions (default), clicks, conversions, conversion_value
- `sort_order`: desc (default) or asc
- `query`: free-text filter on the category name
- `offset` / `limit`: check `has_more` and re-call with a bigger offset

**Parameters:**
- campaign_id (required): the Performance Max campaign ID (from list_campaigns)
- lookback_days: 7, 30, 60, 90, or 120 (default 30)
- customer_id: required for multi-account users

**Use when:** "what search themes is my PMax campaign showing for?", "break down
PMax demand by category", "which search categories convert best in Performance Max".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Aggregated Performance Max search categories (campaign_search_term_insight).",
  "properties": {
    "campaign_id": {
      "description": "Performance Max campaign ID (required). Get it from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    },
    "lookback_days": {
      "default": 30,
      "description": "Trailing window in days: 7, 30, 60, 90, or 120. Default 30.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "query": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Free-text filter — case-insensitive substring match against the search term / category text. E.g. 'free' to surface low-intent queries.",
      "title": "Query"
    },
    "sort_by": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Sort field. Terms: cost (default), clicks, impressions, conversions, conversion_value, ctr, cpc. Categories: impressions (default), clicks, conversions, conversion_value.",
      "title": "Sort By"
    },
    "sort_order": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "desc",
      "description": "'desc' (default, biggest first) or 'asc'.",
      "title": "Sort Order"
    },
    "offset": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 0,
      "description": "Row offset for paging (0-based). Default 0. Paging is capped near the top (you cannot page far into a large result) — filter with `query` or re-sort instead of paging deep.",
      "title": "Offset"
    },
    "limit": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 100,
      "description": "Rows per page (1-200). Default 100 — one call shows the top 100 by your sort, which is almost always enough.",
      "title": "Limit"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "PmaxSearchCategoriesInput",
  "type": "object"
}
```

</details>

<a id="analyze_pmax_search_terms"></a>

## `analyze_pmax_search_terms`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

See the actual search terms a Performance Max campaign matched, with per-term metrics.

⚠️ READ-ONLY. Safe to call repeatedly.

Performance Max search terms live in a different Google Ads resource
(campaign_search_term_view) than Search-campaign terms, so `analyze_search_terms`
returns "No search term data" for a PMax campaign. Use THIS tool for a PMax campaign.

**What you get, per search term:** cost, clicks, impressions, conversions,
conversion value, CTR, CPC — the raw numbers the user needs to spot high-cost /
zero-conversion queries and converting queries, and decide what to do.

**High-volume — do NOT page through everything.** PMax campaigns can have
thousands of search terms. The response ALREADY gives you the answer without
paging:
- Results are sorted by cost (biggest spender first), so the top page is the
  highest-spend set — the terms most worth reviewing.
- A **summary** line reports totals over the WHOLE set (term count, total cost,
  total conversions, and how many terms recorded 0 conversions and the spend on
  them) — read that instead of enumerating every term. These are facts; whether a
  0-conversion term is a problem depends on the account (some are upper-funnel or
  tracked elsewhere) — surface the number, let the user decide.
- To find something specific, **filter with `query` or re-rank with `sort_by`** —
  don't walk page after page. Paging is capped (you cannot page past the top ~100).

Controls:
- `sort_by`: cost (default), clicks, impressions, conversions, conversion_value, ctr, cpc
- `sort_order`: desc (default) or asc
- `query`: free-text filter on the term (e.g. 'free' to surface low-intent queries)
- `offset` / `limit`: only if you truly need more of the same ranking; check `has_more`

**Parameters:**
- campaign_id (required): the Performance Max campaign ID (from list_campaigns)
- lookback_days: 7, 30, 60, 90, or 120 (default 30)
- customer_id: required for multi-account users (from get_connections_status)

**Use when:** "show me the search terms for my PMax campaign", "what queries is
Performance Max spending on?", "find wasted spend / irrelevant queries in PMax".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Per-term Performance Max search terms (campaign_search_term_view).",
  "properties": {
    "campaign_id": {
      "description": "Performance Max campaign ID (required). Get it from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    },
    "lookback_days": {
      "default": 30,
      "description": "Trailing window in days: 7, 30, 60, 90, or 120. Default 30.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "query": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Free-text filter — case-insensitive substring match against the search term / category text. E.g. 'free' to surface low-intent queries.",
      "title": "Query"
    },
    "sort_by": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Sort field. Terms: cost (default), clicks, impressions, conversions, conversion_value, ctr, cpc. Categories: impressions (default), clicks, conversions, conversion_value.",
      "title": "Sort By"
    },
    "sort_order": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "desc",
      "description": "'desc' (default, biggest first) or 'asc'.",
      "title": "Sort Order"
    },
    "offset": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 0,
      "description": "Row offset for paging (0-based). Default 0. Paging is capped near the top (you cannot page far into a large result) — filter with `query` or re-sort instead of paging deep.",
      "title": "Offset"
    },
    "limit": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 100,
      "description": "Rows per page (1-200). Default 100 — one call shows the top 100 by your sort, which is almost always enough.",
      "title": "Limit"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "PmaxSearchTermsInput",
  "type": "object"
}
```

</details>

<a id="analyze_search_terms"></a>

## `analyze_search_terms`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Discover keyword opportunities and optimize match types by analyzing actual search terms.

⚠️ IMPORTANT: This tool retrieves READ-ONLY data. Safe to call multiple times. Google Ads only - NOT available for TikTok.

🎯 **What This Tool Does (Performance Agent - Phase 1 Feature 3):**
- Identifies OPPORTUNITY keywords: Converting search terms NOT in your keyword list
- Identifies NEGATIVE keywords: Expensive terms with zero conversions
- Analyzes MATCH TYPE performance: Exact vs Phrase vs Broad efficiency
- Provides specific recommendations with suggested bids and match types
- Ranks opportunities by profit potential (not just ROAS)

**Returns comprehensive keyword intelligence:**
- Top 20 opportunity keywords with suggested bids and match types
- Top 20 negative keyword candidates with wasted cost breakdown
- Match type performance comparison (Exact/Phrase/Broad)
- Broad→Exact conversion recommendations
- Total opportunity value and wasted spend amounts
- Actionable recommendations for immediate implementation

🔍 **What Search Term Mining Reveals:**

**Opportunity Keywords (Money Left on Table):**
- Search terms that ARE converting but you're NOT bidding on them directly
- These are queries triggering your ads via Broad/Phrase match, but should be added as Exact keywords
- Example: User searches "enterprise security software pricing" → converts → but you only have "security software" as keyword
- **Action:** Add high-converting search terms as new keywords with suggested bids

**Negative Keywords (Money Wasted):**
- Search terms costing >$10 with ZERO conversions
- Low-intent queries like "free", "download", "crack", "how to"
- Example: "free security software download" → 120 clicks, $540 spent, 0 conversions
- **Action:** Add as negative keywords to stop wasting budget

**Match Type Optimization:**
- Compares performance of Exact vs Phrase vs Broad match
- Identifies Broad keywords that should be converted to Exact for better control
- Example: Broad "security software" has 45% wasted spend, but top search terms have 20x ROAS
- **Action:** Convert high-performing Broad keywords to Exact match

**Parameters:**
- lookback_days: 7, 30, 60, 90, or 120 days (default: 30)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- analysis_type: 'opportunities', 'negatives', 'match_types', 'all', or **'raw_report'** (default: 'all')
  - Use **'raw_report'** when the user wants to SEE their actual search terms — the words customers type into Google
- force_refresh: true to trigger immediate API collection (default: false, uses cached data)
- customer_id: Optional (uses connected account if omitted)
- **campaign_id**: Optional — filter search terms to a specific campaign (get from list_campaigns)
- **page**: Page number for raw_report pagination (default: 1)
- **page_size**: Results per page for raw_report (1-100, default: 50)
- **sort_by**: Sort for raw_report: 'cost' (default), 'clicks', 'impressions', 'conversions'
- **min_clicks**: Minimum clicks filter for raw_report (default: 0)

**Execution time:** 1-3 seconds (cached database query)
**Data source:** search_term_daily_metrics table (updated nightly, 120-day retention)

**⚡ RAW REPORT PAGINATION CONTRACT:**
- When using analysis_type='raw_report', results are paginated
- Check `pagination.has_more` — if true, call again with next `page`
- Continue until `has_more` is false, then present consolidated results
- Use `campaign_id` to focus on a specific campaign's search terms

**Use this tool when:**
- User asks "what keywords should I add?"
- User wants to find wasted spend at keyword level
- User asks "what should I add as negative keywords?"
- User wants to improve match type efficiency
- User asks "which Broad keywords should be Exact?"
- User wants to discover hidden keyword opportunities
- **User asks "show me my search terms" or "what are people searching for?"** → use analysis_type='raw_report'
- **User asks "show me search terms for campaign X"** → use analysis_type='raw_report' with campaign_id

⚠️ **Platform Limitation:**
This tool ONLY works for Google Ads. TikTok Ads does not provide search term data due to privacy restrictions.



<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for search term mining and keyword opportunity analysis",
  "properties": {
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date (YYYY-MM-DD). If provided with end_date, overrides lookback_days for custom date range queries.",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date (YYYY-MM-DD). If provided with start_date, overrides lookback_days for custom date range queries.",
      "title": "End Date"
    },
    "date_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Date range preset: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. Overrides lookback_days. Ignored if start_date/end_date are provided.",
      "title": "Date Range"
    },
    "raw_data": {
      "default": false,
      "description": "If true, return ONLY raw metrics as a JSON code block (spend, clicks, impressions, conversions, CPA, CPC, CTR, CVR, ROAS by campaign/ad/date). Strips severity labels, suggested bids/budgets, industry benchmarks, and optimization recommendations. Use when you run your own attribution model or want to minimize token usage.",
      "title": "Raw Data",
      "type": "boolean"
    },
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze search term data (7, 30, 60, 90, or 120 days). Default is 30 days.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "analysis_type": {
      "default": "all",
      "description": "Type of analysis: 'opportunities', 'negatives', 'match_types', 'all', or 'raw_report'. Use 'raw_report' to see all actual search terms with their metrics. Default is 'all'.",
      "title": "Analysis Type",
      "type": "string"
    },
    "force_refresh": {
      "default": false,
      "description": "If true, triggers immediate API collection from Google Ads (not yet implemented - currently uses cached data). Default is false.",
      "title": "Force Refresh",
      "type": "boolean"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional campaign ID to filter search terms to a specific campaign. Get from list_campaigns.",
      "title": "Campaign Id"
    },
    "page": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 1,
      "description": "Page number for raw_report (1-based). Default: 1",
      "title": "Page"
    },
    "page_size": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 50,
      "description": "Results per page for raw_report (1-100). Default: 50",
      "title": "Page Size"
    },
    "sort_by": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cost",
      "description": "Sort field for raw_report: 'cost' (default), 'clicks', 'impressions', 'conversions'",
      "title": "Sort By"
    },
    "min_clicks": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 0,
      "description": "Minimum clicks filter for raw_report. Default: 0 (show all)",
      "title": "Min Clicks"
    }
  },
  "title": "SearchTermMiningInput",
  "type": "object"
}
```

</details>

<a id="analyze_wasted_spend"></a>

## `analyze_wasted_spend`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Analyze wasted ad spend and identify campaigns losing money or underperforming.

⚠️ IMPORTANT: This tool retrieves READ-ONLY data. Safe to call multiple times.

🎯 **What This Tool Does (Performance Agent - Phase 1):**
- Identifies campaigns LOSING money (ROAS < 1.0x)
- Identifies campaigns UNDERPERFORMING (1.0x ≤ ROAS < target)
- Separates true waste from opportunity cost
- Provides severity-based classification (CRITICAL/HIGH/MEDIUM)
- Generates actionable recommendations with expected impact
- Shows top performing campaigns for budget reallocation

**Returns detailed analysis:**
- Total wasted spend (campaigns with ROAS < 1.0)
- Total underperforming spend (profitable but below target)
- Campaign-by-campaign breakdown with severity levels
- Specific recommendations (PAUSE/REDUCE/OPTIMIZE)
- Quick actions for immediate implementation
- Budget reallocation suggestions

**Target ROAS Resolution (3-tier priority):**
1. Account goals table (user-set or API-pulled)
2. 90-day historical average ROAS
3. Default to 2.0x if no data available

**Severity Levels:**
- 🚨 CRITICAL: ROAS < 0.5x (losing money severely)
- 🔴 HIGH: ROAS < 1.0x (unprofitable/breakeven)
- 🟡 MEDIUM: 1.0x ≤ ROAS < target (profitable but underperforming)

**Parameters:**
- lookback_days: 7, 30, 60, 90, or 120 days (default: 30)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- target_roas: Optional override (e.g., 3.0 for 3.0x ROAS)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 1-3 seconds (cached database query)
**Data source:** campaign_daily_metrics table (updated nightly)

**Use this tool when:**
- User asks "where is my money going?"
- User wants to identify wasted spend
- User wants to optimize campaign budgets
- User asks which campaigns to pause/reduce
- User wants to know which campaigns are losing money



<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date (YYYY-MM-DD). If provided with end_date, overrides lookback_days for custom date range queries.",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date (YYYY-MM-DD). If provided with start_date, overrides lookback_days for custom date range queries.",
      "title": "End Date"
    },
    "date_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Date range preset: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. Overrides lookback_days. Ignored if start_date/end_date are provided.",
      "title": "Date Range"
    },
    "raw_data": {
      "default": false,
      "description": "If true, return ONLY raw metrics as a JSON code block (spend, clicks, impressions, conversions, CPA, CPC, CTR, CVR, ROAS by campaign/ad/date). Strips severity labels, suggested bids/budgets, industry benchmarks, and optimization recommendations. Use when you run your own attribution model or want to minimize token usage.",
      "title": "Raw Data",
      "type": "boolean"
    },
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze (7, 30, 60, 90, or 120 days). Default is 30 days.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional target ROAS override (e.g., 3.0 for 3.0x ROAS). If not provided, will use account goals or historical average.",
      "title": "Target Roas"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "title": "WastedSpendAnalysisInput",
  "type": "object"
}
```

</details>

<a id="attach_negative_keyword_list_to_campaign"></a>

## `attach_negative_keyword_list_to_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Attach a shared negative keyword list to a campaign.

Links an existing negative keyword list (SharedSet) to a campaign so the campaign
starts excluding the list's keywords. One list can be attached to many campaigns.

**Parameters:**
- shared_set_id (required — from list_negative_keyword_lists)
- campaign_id (required — from list_campaigns)

**Use when:** "attach my negatives list to this campaign", "apply the shared negative
list to campaign X".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Attach a shared negative keyword list to a campaign.",
  "properties": {
    "shared_set_id": {
      "description": "The negative keyword list ID (shared set ID). Get it from list_negative_keyword_lists.",
      "title": "Shared Set Id",
      "type": "string"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users.",
      "title": "Customer Id"
    },
    "campaign_id": {
      "description": "The campaign to attach the list to. Get it from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    }
  },
  "required": [
    "shared_set_id",
    "campaign_id"
  ],
  "title": "AttachNegativeKeywordListToCampaignInput",
  "type": "object"
}
```

</details>

<a id="audit_conversion_tracking"></a>

## `audit_conversion_tracking`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Review your conversion tracking setup across ad platforms. Checks Meta Pixel (event volume, CAPI status, dedup, diagnostics), LinkedIn (conversion rules, CAPI, Insight Tag), and Google Ads (conversion actions, enhanced conversions, attribution). Returns a health score (0-100), grade (A-F), detailed findings, and suggestions with self-validation steps for each platform.

Note: Some checks rely on API data availability and may not capture all configurations. Where findings are inconclusive, the tool provides guidance on how to verify directly in the platform's dashboard.

Parameters:
- platform (optional): 'google_ads', 'meta_ads', or 'linkedin_ads'. If omitted, reviews all connected platforms.
- account_id (optional): scope the audit to ONE account (Google Ads customer ID, Meta ad account ID, or LinkedIn account ID). If omitted, EVERY active account on the platform is audited — for a user with many active accounts that is many live API calls. To audit a single account, pass account_id; do NOT switch or deactivate active accounts to narrow the audit (that changes account state for the whole login).
- customer_id (optional): alias for account_id.
- lookback_days (optional): 7, 14, 30, 60, or 90 days (default: 30)

Execution time: ~5-15 seconds (includes live API calls to ad platforms).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for the conversion tracking audit tool.",
  "properties": {
    "platform": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Ad platform to audit: 'google_ads', 'meta_ads', or 'linkedin_ads'. If omitted, audits all connected platforms.",
      "title": "Platform"
    },
    "account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional. Scope the audit to ONE account (e.g. a single Google Ads customer ID like '5835090207', a Meta ad account ID, or a LinkedIn account ID). If omitted, EVERY active account on the platform is audited — for a user with many active accounts that is many live API calls. To audit just one account, pass account_id; do NOT switch/deactivate active accounts to narrow the audit.",
      "title": "Account Id"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Alias for account_id (Google Ads clients often say 'customer_id'). If both are given, account_id wins.",
      "title": "Customer Id"
    },
    "lookback_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 30,
      "description": "Number of days to look back for trend analysis (7, 14, 30, 60, 90). Default: 30.",
      "title": "Lookback Days"
    }
  },
  "title": "AuditConversionTrackingInput",
  "type": "object"
}
```

</details>

<a id="browse_meta_targeting"></a>

## `browse_meta_targeting`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to browse all targeting options in a specific category without a search query.

This tool retrieves all options in a Meta targeting category for exploration and discovery.

Returns:
- List of all targeting options in the category
- IDs, names, and audience sizes
- Useful for discovering targeting options when user doesn't have a specific query

When to use this tool:
- "Show me all available behaviors for Meta targeting"
- "What interest categories are available?"
- "Browse demographic targeting options"
- "List all life events I can target"
- "What income targeting options exist?"

Categories Available:
- interests: All interest targeting categories
- behaviors: All behavior targeting options
- demographics: All demographic targeting options
- life_events: All life event targeting options
- industries: Industry targeting options
- income: Income bracket targeting options
- family_statuses: Family status targeting options

Parameters:
- category: Category to browse (required)
- limit: Maximum results (1-500, default: 100)
- locale: Locale for results (default: en_US)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 1-3 seconds
Data source: Meta Marketing API Targeting Search

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for browsing Meta targeting categories",
  "properties": {
    "category": {
      "description": "Category to browse:\n- 'interests': Browse all interest categories\n- 'behaviors': Browse all behavior categories\n- 'demographics': Browse all demographic categories\n- 'life_events': Browse all life event categories\n- 'industries': Browse industry targeting options\n- 'income': Browse income targeting options\n- 'family_statuses': Browse family status targeting options",
      "title": "Category",
      "type": "string"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of results to return (1-500). Default is 100.",
      "title": "Limit",
      "type": "integer"
    },
    "locale": {
      "default": "en_US",
      "description": "Locale for results (e.g., 'en_US', 'es_ES'). Default is 'en_US'.",
      "title": "Locale",
      "type": "string"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Ad Account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "category"
  ],
  "title": "BrowseMetaTargetingInput",
  "type": "object"
}
```

</details>

<a id="bulk_update_ad_group_status"></a>

## `bulk_update_ad_group_status`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Pause or enable MANY ad groups in a SINGLE call.

Use this instead of calling pause_ad_group / resume_ad_group once per ad group —
pausing or enabling N ad groups here is ONE tool call (and one quota debit) instead
of N. Works on any campaign type (Search, PMax, Display, Demand Gen). Fully
reversible: it sets status, it never removes ad groups.

**Parameters:**
- ad_group_ids: List of ad group IDs to update (REQUIRED). No limit.
- status: PAUSED or ENABLED (REQUIRED)
- campaign_id: Optional. If set, the ad groups are checked to belong to this campaign.
- customer_id: Optional

**Get ad_group_ids from:** get_campaign_structure or list_campaigns.

**Example:**
User: "Pause all the ad groups in that campaign"
Agent:
1. get_campaign_structure to list the ad groups + IDs
2. bulk_update_ad_group_status(ad_group_ids=[...], campaign_id=..., status="PAUSED")

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for bulk pausing/enabling ad groups.",
  "properties": {
    "ad_group_ids": {
      "description": "Ad group IDs to update (get from get_campaign_structure or list_campaigns). No limit — pass thousands if you have them; applied in one tool call.",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Ad Group Ids",
      "type": "array"
    },
    "status": {
      "description": "New status for all listed ad groups: PAUSED or ENABLED. Reversible — this never removes ad groups.",
      "title": "Status",
      "type": "string"
    },
    "campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional. When set, ad groups are checked to belong to this campaign (an ID from another campaign is reported as not found).",
      "title": "Campaign Id"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_ids",
    "status"
  ],
  "title": "BulkUpdateAdGroupStatusInput",
  "type": "object"
}
```

</details>

<a id="bulk_update_ad_status"></a>

## `bulk_update_ad_status`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Pause or enable MANY ads in one ad group in a SINGLE call.

Use this instead of calling pause_ad / resume_ad once per ad — pausing or resuming
N ads here is ONE tool call (and one quota debit) instead of N. This is the tool for
swapping/refreshing ads across an account without burning your monthly tool-call
limit. Fully reversible: it sets status, it never removes ads.

**Parameters:**
- ad_group_id: The ad group containing the ads (REQUIRED). One call per ad group.
- ad_ids: List of ad IDs to update, all in that ad group (REQUIRED). No limit — pass
  thousands if you have them; they are applied in one call (chunked internally).
- status: PAUSED or ENABLED (REQUIRED)
- customer_id: Optional

**Get ad_ids from:** get_campaign_structure or get_ad_performance (both show ad IDs).

**To pause/enable ads across several ad groups:** make one call per ad group.

**Execution time:** 2-10 seconds depending on ad count.

**Example:**
User: "Pause all the old ads in that ad group so I can swap in the new ones"
Agent:
1. get_campaign_structure to list the ads + IDs
2. bulk_update_ad_status(ad_group_id, ad_ids=[...], status="PAUSED")

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for bulk pausing/enabling ads in one ad group.",
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID the ads belong to. One call per ad group. Use get_campaign_structure to find this.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "ad_ids": {
      "description": "Ad IDs to update, all in this ad group (get from get_campaign_structure or get_ad_performance). No limit — pass thousands if you have them; they are applied in one tool call.",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Ad Ids",
      "type": "array"
    },
    "status": {
      "description": "New status for all listed ads: PAUSED or ENABLED. Reversible — this never removes ads.",
      "title": "Status",
      "type": "string"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id",
    "ad_ids",
    "status"
  ],
  "title": "BulkUpdateAdStatusInput",
  "type": "object"
}
```

</details>

<a id="bulk_update_campaign_status"></a>

## `bulk_update_campaign_status`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Pause or enable MANY campaigns in a SINGLE call.

Use this instead of calling pause_campaign / resume_campaign once per campaign —
pausing or enabling N campaigns here is ONE tool call (and one quota debit) instead
of N. Fully reversible: it sets status, it never removes campaigns.

⚠️ Enabling campaigns can start real ad spend. Confirm with the user before enabling.

**Parameters:**
- campaign_ids: List of campaign IDs to update (REQUIRED). No limit.
- status: PAUSED or ENABLED (REQUIRED)
- customer_id: Optional

**Get campaign_ids from:** list_campaigns.

**Example:**
User: "Pause all my search campaigns"
Agent:
1. list_campaigns to get the campaign IDs
2. bulk_update_campaign_status(campaign_ids=[...], status="PAUSED")

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for bulk pausing/enabling campaigns.",
  "properties": {
    "campaign_ids": {
      "description": "Campaign IDs to update (get from list_campaigns). No limit — pass thousands if you have them; applied in one tool call.",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Campaign Ids",
      "type": "array"
    },
    "status": {
      "description": "New status for all listed campaigns: PAUSED or ENABLED. Reversible — this never removes campaigns. Enabling can start real spend.",
      "title": "Status",
      "type": "string"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_ids",
    "status"
  ],
  "title": "BulkUpdateCampaignStatusInput",
  "type": "object"
}
```

</details>

<a id="bulk_update_keyword_status"></a>

## `bulk_update_keyword_status`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Pause or enable MANY keywords in one ad group in a SINGLE call.

Use this instead of calling update_keyword once per keyword — pausing N keywords
here is ONE tool call (and one quota debit) instead of N. Fully reversible: it sets
status, it never removes keywords (unlike remove_keywords).

**Parameters:**
- ad_group_id: The ad group containing the keywords (REQUIRED). One call per ad group.
- keyword_ids: List of keyword IDs to update, all in that ad group (REQUIRED). Max 300/call.
- status: PAUSED or ENABLED (REQUIRED)
- customer_id: Optional

**Get keyword_ids from:** get_campaign_structure (shows every keyword + its ID).

**To pause keywords across several ad groups:** make one call per ad group.

**Execution time:** 2-6 seconds

**Example:**
User: "Pause all the non-core keywords in that ad group"
Agent:
1. get_campaign_structure to list the keywords + IDs
2. Confirms which ones to pause
3. bulk_update_keyword_status(ad_group_id, keyword_ids=[...], status="PAUSED")

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for bulk pausing/enabling keywords in one ad group.",
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID the keywords belong to. One call per ad group. Use get_campaign_structure to find this.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "keyword_ids": {
      "description": "Keyword IDs to update, all in this ad group (get from get_campaign_structure). Max 300 per call (Google's keyword ops/hour limit) — split larger sets across calls.",
      "items": {
        "type": "string"
      },
      "maxItems": 300,
      "minItems": 1,
      "title": "Keyword Ids",
      "type": "array"
    },
    "status": {
      "description": "New status for all listed keywords: PAUSED or ENABLED. Reversible — this never removes keywords.",
      "title": "Status",
      "type": "string"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id",
    "keyword_ids",
    "status"
  ],
  "title": "BulkUpdateKeywordStatusInput",
  "type": "object"
}
```

</details>

<a id="compare_meta_catalog_product_sets"></a>

## `compare_meta_catalog_product_sets`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to compare their catalog PRODUCT SETS against each other and decide where to put budget. Keywords: "which product set is best", "compare product sets", "where should budget go", "best sellers vs the rest", "product set ROAS".

Ranks product sets by catalog-attributed ROAS, sizes a suggested budget shift from the weakest set toward the strongest, and flags OVERLAP — the same product spending across multiple sets (self-competition that fragments budget and inflates costs).

Reads cached nightly product metrics (never calls Meta live). When to use: "Which product set performs best?", "Should I move budget between my product sets?"

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for the product-set vs product-set comparison diagnostic.",
  "properties": {
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze: 7, 30, 60, 90, or 120 (default 30).",
      "title": "Lookback Days",
      "type": "integer"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional target ROAS override (e.g. 3.0). Defaults to account goal, else 90-day average, else 2.0x.",
      "title": "Target Roas"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date YYYY-MM-DD (overrides lookback_days with end_date).",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date YYYY-MM-DD (overrides lookback_days with start_date).",
      "title": "End Date"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta ad account ID. Required for multi-account users.",
      "title": "Ad Account Id"
    }
  },
  "title": "CompareMetaCatalogProductSetsInput",
  "type": "object"
}
```

</details>

<a id="competitor_ads_research"></a>

## `competitor_ads_research`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Research what a COMPETITOR is actually advertising right now — their live ad creatives, headlines, offers, calls to action, formats, and how long each ad has been running — pulled from public ad-transparency sources and read with vision analysis, then placed SIDE BY SIDE with the user's own connected ad account.

**Call this when the user asks:**
- "what ads is <competitor> running", "show me my competitor's ads"
- "what are competitors doing", "competitor ad research/analysis/intelligence"
- "what messaging/offers/creatives do they use", "what's working for them"
- "how do my ads compare to <competitor>", "am I bidding on their brand"
- anything about competitor creative, competitor copy, or competitive ad strategy

**Inputs:** `competitor_domains` (REQUIRED — a list of competitor WEBSITE DOMAINS like ['semrush.com','ahrefs.com']). ⛔ It must be a DOMAIN, not a brand name: a bare brand returns zero results. If the user names a company without giving a website, ASK for the domain — do NOT guess it and do NOT auto-discover competitors. `region` (optional ISO country like 'US','IN','GB' — defaults to the user's own account market; note TikTok and LinkedIn ads are worldwide and cannot be filtered by market). `sources` (optional list — which ad platforms to pull: `['google']` (default, Google Search/Display/YouTube ads), add `'meta'` for their Facebook/Instagram ads, `'tiktok'` for their TikTok ads, and/or `'linkedin'` for their LinkedIn ads — e.g. `['google','meta','tiktok','linkedin']`. Add 'meta' when the user asks about Facebook/Instagram/Meta ads, 'tiktok' when they ask about TikTok ads, and 'linkedin' when they ask about LinkedIn/B2B ads or want a fuller picture). `max_creatives` (optional cap).

**What it returns:** an interactive gallery of their real creatives with run-durations, plus the user's own ads and any competitor brand terms they already pay for. ⛔ It does NOT return competitor spend, ROAS, conversions, CPC or impressions — no source publishes those, so the tool never estimates them. Do not ask it for, or infer, how a competitor's ads PERFORM; a long run-duration is a duration, not proof it works.

⚠️ Plus, Pro & Max (not Free). Renders an interactive widget; the text fallback carries the same findings.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Inputs. `competitor_domains` is REQUIRED and must be DOMAINS, not brand\nnames — the transparency API returns zero results for a bare brand\n('brandname' → 0, 'brandname.com' → 40 creatives). If the user names a company\nwithout a domain, ask for the website rather than guessing it.",
  "properties": {
    "competitor_domains": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Competitor Domains"
    },
    "region": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Region"
    },
    "max_creatives": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Max Creatives"
    },
    "sources": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Sources"
    },
    "account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional. Scope the YOUR-ADS half of the comparison to ONE of your ad accounts (a Google customer ID like '5835090207', a Meta ad account ID, or a TikTok/Amazon/LinkedIn account ID). **Required for multi-account users** — get the IDs from get_connections_status. If omitted, the comparison covers every connected account and says so. Do NOT switch or deactivate accounts to narrow it; just pass account_id.",
      "title": "Account Id"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Alias for account_id (Google Ads clients often say 'customer_id'). If both are given, account_id wins.",
      "title": "Customer Id"
    }
  },
  "title": "CompetitorAdsResearchInput",
  "type": "object"
}
```

</details>

<a id="create_ad"></a>

## `create_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Create a new Responsive Search Ad (RSA) in an existing ad group.

Useful for A/B testing different ad copy or adding variation to an ad group.

**Parameters:**
- ad_group_id: The ad group to add the ad to (REQUIRED)
- headlines: 3-15 headlines (REQUIRED, max 30 chars each)
- descriptions: 2-4 descriptions (REQUIRED, max 90 chars each)
- final_urls: Landing page URLs (REQUIRED, at least one)
- path1: Optional display path 1 (max 15 chars)
- path2: Optional display path 2 (max 15 chars)
- customer_id: Optional

**Execution time:** 3-5 seconds

**New ad goes through Google's review process.**

**Example:**
User: "Create a new ad to test different messaging"
Agent:
1. Gets ad_group_id from get_campaign_structure
2. Prepares headlines and descriptions
3. Creates new ad with create_ad

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating a new RSA",
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID to add the ad to. Get from get_campaign_structure.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "headlines": {
      "description": "List of 3-15 headlines. Each max 30 characters. Include mix of: product identity, benefits, and CTAs.",
      "items": {
        "type": "string"
      },
      "maxItems": 15,
      "minItems": 3,
      "title": "Headlines",
      "type": "array"
    },
    "descriptions": {
      "description": "List of 2-4 descriptions. Each max 90 characters.",
      "items": {
        "type": "string"
      },
      "maxItems": 4,
      "minItems": 2,
      "title": "Descriptions",
      "type": "array"
    },
    "final_urls": {
      "description": "Landing page URLs. At least one required.",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Final Urls",
      "type": "array"
    },
    "path1": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display path 1 (max 15 chars). Shows in ad URL.",
      "title": "Path1"
    },
    "path2": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display path 2 (max 15 chars). Shows after path1.",
      "title": "Path2"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id",
    "headlines",
    "descriptions",
    "final_urls"
  ],
  "title": "CreateAdInput",
  "type": "object"
}
```

</details>

<a id="create_app_campaign"></a>

## `create_app_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Create a Google App campaign (Universal App Campaign / UAC) to drive app installs, in-app engagement, or Play pre-registrations.

⚠️ Creates a REAL campaign (starts PAUSED — resume_campaign when ready). Call ONCE; do NOT auto-retry.

PREREQUISITE: a real, published app listing. Pass its store id as `app_id` (Play package name for
GOOGLE_APP_STORE, e.g. com.company.app; numeric App Store id for APPLE_APP_STORE, e.g. 1234567890) and the
matching `app_store`. Google validates the app_id against the store — a made-up id is rejected.

WHAT THIS BUILDS: budget + MULTI_CHANNEL/App campaign (with the app + bidding goal) + one auto-managed ad
group + one app ad. App campaigns are largely automated — Google assembles ads from your store listing plus
the assets you provide.

TYPES (`app_campaign_type`): install (default) | engagement (re-engagement — needs a deep-link + audience) |
pre_registration (Google Play only). Install is the common case.

**Required:** campaign_name, budget_daily, app_id, app_store.
**Bidding:** bidding_strategy (leave UNSET to auto-pick the strategy that matches the goal | TARGET_CPA | MAXIMIZE_CONVERSIONS | TARGET_ROAS) + target_cpa_micros /
target_roas + optional bidding_goal_type.
**Creative (`ad`):** headlines (≤30), descriptions (≤90), image_assets /
video_assets (resource names of EXISTING assets). start_date/end_date (YYYYMMDD).

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "AppAdSpec": {
      "description": "The single app ad's creative assets for an App (UAC) campaign.",
      "properties": {
        "headlines": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Short headlines (each ≤30 chars). Google mixes these into the ad.",
          "title": "Headlines"
        },
        "descriptions": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Descriptions (each ≤90 chars).",
          "title": "Descriptions"
        },
        "image_assets": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Resource names of EXISTING image assets (customers/<cid>/assets/<id>). Upload/discover assets first; this create tool references, it does not upload.",
          "title": "Image Assets"
        },
        "video_assets": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Resource names of EXISTING YouTube video assets. References only, not uploads.",
          "title": "Video Assets"
        }
      },
      "title": "AppAdSpec",
      "type": "object"
    }
  },
  "description": "Input schema for create_app_campaign (Universal App / UAC — install/engagement/pre-reg).",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (e.g. 'Sahaayak Installs — US').",
      "title": "Campaign Name",
      "type": "string"
    },
    "budget_daily": {
      "description": "Daily budget in the account's native currency. Do NOT convert currencies — pass as-is.",
      "minimum": 1.0,
      "title": "Budget Daily",
      "type": "number"
    },
    "app_id": {
      "description": "The app's store id: the Play package name (e.g. com.company.app) for GOOGLE_APP_STORE, or the numeric App Store id (e.g. 1234567890) for APPLE_APP_STORE. Must be a real, published listing in that store.",
      "title": "App Id",
      "type": "string"
    },
    "app_store": {
      "description": "GOOGLE_APP_STORE or APPLE_APP_STORE (which store app_id lives in).",
      "title": "App Store",
      "type": "string"
    },
    "app_campaign_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "install",
      "description": "install (default) | engagement (re-engagement; needs a deep-link + audience) | pre_registration (Google Play only).",
      "title": "App Campaign Type"
    },
    "bidding_goal_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "AppCampaignBiddingStrategyGoalType override. Defaults per type (install→OPTIMIZE_INSTALLS_WITHOUT_TARGET_INSTALL_COST, pre_reg→OPTIMIZE_PRE_REGISTRATION_CONVERSION_VOLUME). Advanced; leave unset normally.",
      "title": "Bidding Goal Type"
    },
    "bidding_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "TARGET_CPA | MAXIMIZE_CONVERSIONS | TARGET_ROAS. Leave unset to let the server pick the strategy that pairs with the goal (Google rejects incompatible combos).",
      "title": "Bidding Strategy"
    },
    "target_cpa_micros": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target CPA in micros — used with TARGET_CPA / MAXIMIZE_CONVERSIONS.",
      "title": "Target Cpa Micros"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target ROAS (e.g. 4.0). REQUIRED if bidding_strategy=TARGET_ROAS.",
      "title": "Target Roas"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign start date YYYYMMDD.",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign end date YYYYMMDD.",
      "title": "End Date"
    },
    "ad": {
      "anyOf": [
        {
          "$ref": "#/$defs/AppAdSpec"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "The app ad's creative assets (headlines/descriptions/image_assets/video_assets). Google auto-generates the rest from your store listing."
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID (10 digits, no dashes). REQUIRED whenever the user has more than one Google Ads account connected — this creates a REAL campaign that spends REAL money, so it must land in the account the user actually meant. Do NOT omit it and do NOT guess: carry over the customer_id already in use in this conversation, or call list_connected_accounts / get_connections_status and ask the user which account. If a call fails asking you to disambiguate, RETRY with this parameter — that error does NOT mean the account is disconnected.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_name",
    "budget_daily",
    "app_id",
    "app_store"
  ],
  "title": "CreateAppCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_conversion_action"></a>

## `create_conversion_action`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Create a WEBPAGE conversion action so the account can use TARGET_CPA / MAXIMIZE_CONVERSIONS / TARGET_ROAS bidding.

**Why this matters:**
Without conversion actions, Smart Bidding strategies (TARGET_CPA, MAXIMIZE_CONVERSIONS, TARGET_ROAS) can't function correctly. They need a "what counts as a conversion" definition to optimize toward. This tool creates that definition.

**v1 scope:** WEBPAGE conversion actions only. After creating, the customer must:
1. Install the Google site tag (gtag.js) on their website if not already present
2. Add an event snippet on the conversion page (or fire it on a click/form submit)
3. Wait 24-48 hours for the first conversions to flow in
4. THEN apply TARGET_CPA bidding (it needs a few conversions to optimize)

Phone-call / app / Firebase / Floodlight conversion types are deferred to a future tool.

**Pick the right category:**
- E-commerce purchase → PURCHASE (set value + currency)
- Lead-gen form submit → SUBMIT_LEAD_FORM (set value if leads have known $ worth)
- Newsletter signup / account creation → SIGNUP
- Add-to-cart tracking → ADD_TO_CART
- Begin-checkout (abandonment funnel) → BEGIN_CHECKOUT
- Phone-call lead from ad → PHONE_CALL_LEAD
- Outbound click on partner site → OUTBOUND_CLICK
- Engagement metric (page time, scroll, video play) → ENGAGEMENT
- "Get directions" tap on a map ad → GET_DIRECTIONS
- Quote request → REQUEST_QUOTE
- Appointment booked → BOOK_APPOINTMENT
- Generic contact form → CONTACT
- Use DEFAULT only if none fit.

**Counting type:**
- ONE_PER_CLICK (default): one conversion per ad click. Use for lead-gen, signups, downloads.
- MANY_PER_CLICK: every purchase counts, even multiple from same click. Use for e-commerce.

**Value settings:**
- Recommended for lead-gen: set `value` to your average lead $ worth (e.g. 50.0 for $50/lead). This gives TARGET_CPA something to optimize.
- Set `always_use_default_value=true` if every conversion has the same value (lead-gen).
- Leave both unset for e-commerce — the tag sends actual transaction values.

**Example:**
User: "Set up TARGET_CPA bidding for my lead-gen campaign"
Agent:
1. Calls create_conversion_action(name="Lead Form Submit", category="SUBMIT_LEAD_FORM", value=50.0, always_use_default_value=true)
2. Tells user: "Created the conversion goal. Now install the Google tag on your thank-you page, then I'll switch the campaign to TARGET_CPA."
3. After tag is installed and conversions are flowing, calls update_bid_strategy(strategy="TARGET_CPA", target_cpa=20.0).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating a WEBPAGE conversion action.\n\nWhy this matters:\nWithout a conversion action set up, Google Ads bidding strategies that\noptimize toward conversions (TARGET_CPA, MAXIMIZE_CONVERSIONS, TARGET_ROAS)\nare unavailable or won't work correctly. Creating one unblocks those.\n\nv1 scope: WEBPAGE only. Phone-call / app / Firebase types are deferred.\nAfter creating, the customer must install the Google tag and event snippet\non the conversion page to start recording conversions.",
  "properties": {
    "name": {
      "description": "Display name in the Google Ads UI (e.g. 'Lead Form Submit', 'Pricing Page View', 'Newsletter Signup'). Must be unique per account.",
      "title": "Name",
      "type": "string"
    },
    "category": {
      "description": "Conversion category. Pick the closest match: PURCHASE, SIGNUP, ADD_TO_CART, BEGIN_CHECKOUT, SUBMIT_LEAD_FORM, BOOK_APPOINTMENT, REQUEST_QUOTE, GET_DIRECTIONS, ENGAGEMENT, CONTACT, PHONE_CALL_LEAD, OUTBOUND_CLICK, QUALIFIED_LEAD, CONVERTED_LEAD, DOWNLOAD, PAGE_VIEW, SUBSCRIBE_PAID, IMPORTED_LEAD, STORE_VISIT, STORE_SALE, DEFAULT (use only if none fit).",
      "title": "Category",
      "type": "string"
    },
    "value": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Default conversion value in account currency (e.g. 50.00 for $50/lead). Recommended for lead-gen — gives TARGET_CPA bidding something to optimize.",
      "title": "Value"
    },
    "currency_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "3-letter currency code (USD, EUR, etc). Defaults to account currency.",
      "title": "Currency Code"
    },
    "always_use_default_value": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "If True, every conversion is worth `value` regardless of what the tag sends. Useful for lead-gen where each lead's dollar value isn't dynamic. Requires `value` > 0.",
      "title": "Always Use Default Value"
    },
    "counting_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "ONE_PER_CLICK",
      "description": "ONE_PER_CLICK (default; lead-gen, signups, downloads — count one conversion per ad click) or MANY_PER_CLICK (e-commerce — count every purchase, including repeat sales from same click).",
      "title": "Counting Type"
    },
    "click_through_lookback_window_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 30,
      "description": "1-30. How many days post-click a conversion still counts. Default 30.",
      "title": "Click Through Lookback Window Days"
    },
    "view_through_lookback_window_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 1,
      "description": "1-30. How many days post-impression (no click) a conversion still counts. Default 1.",
      "title": "View Through Lookback Window Days"
    },
    "primary_for_goal": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": true,
      "description": "Whether this is a primary conversion for its category. Default True.",
      "title": "Primary For Goal"
    },
    "attribution_model": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "GOOGLE_ADS_LAST_CLICK",
      "description": "Default GOOGLE_ADS_LAST_CLICK (most common). Other options: EXTERNAL, GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK, GOOGLE_SEARCH_ATTRIBUTION_LINEAR, GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY, GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED, GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN.",
      "title": "Attribution Model"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "name",
    "category"
  ],
  "title": "CreateConversionActionInput",
  "type": "object"
}
```

</details>

<a id="create_demandgen_campaign"></a>

## `create_demandgen_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

🔄 LONG-RUNNING TOOL: Creates a Demand Gen campaign across ALL Google channels — YouTube, Discover, Gmail, Display, and Maps. Emits MCP progress updates during creation (typically 10-20 seconds).

⚠️ CRITICAL WARNING ⚠️
- Call this tool ONLY ONCE per campaign
- Creates REAL campaigns that cost REAL money
- Do NOT retry automatically if errors occur
- Report errors to user instead of retrying

🌐 **Demand Gen Campaign Channels (ALL enabled by default):**
✅ YouTube In-Feed (search results & related videos)
✅ YouTube In-Stream (before/during/after videos)
✅ YouTube Shorts (Shorts feed)
✅ Gmail (Promotions & Social tabs)
✅ Discover (Google Discover feed)
✅ Display (Google Display Network)
❌ Maps (opt-in, disabled by default)

📋 **YOUR CRITICAL ROLE: Campaign Strategist & Text Creator**

**STEP 1: Collect Campaign Details from User**

YOU MUST collect these from the user:
1. **Campaign Name** - Descriptive and unique
2. **Daily Budget** - In account's native currency (recommended $20+/day)
3. **Ad Format** - multi_asset (images) or video_responsive (videos)
4. **Final URL** - Landing page
5. **Business Name** - Max 25 characters

**STEP 2: Discover Existing Assets**
🔴 MANDATORY: Call discover_existing_assets to find existing logos/images.
- If logos found → use logo_asset_id or existing_images.logos_square
- If NO logos → ask user for logo URL, run validate_and_prepare_assets

**STEP 3: Generate Ad Copy**
- Headlines (1-5): STRICT 40 character max each
- Descriptions (1-5): STRICT 90 character max each
- Long Headlines (optional, for video_responsive): 90 char max each

**STEP 4: Prepare Images/Videos**
For multi_asset: Need landscape (1.91:1) OR square (1:1) marketing images + logo
For video_responsive: Need YouTube video IDs (validate first) + logo

**STEP 5: Call create_demandgen_campaign with complete payload**

**Bidding Options (your choice is honored — engine is advisory only):**
- MAXIMIZE_CLICKS: Default, works without conversion tracking
- MAXIMIZE_CONVERSIONS: Requires conversion tracking
- TARGET_CPA: Requires target_cpa value
- MAXIMIZE_CONVERSION_VALUE: Requires conversion tracking
- TARGET_ROAS: Requires target_roas value

**Channel Controls (optional):**
Pass channels dict to disable specific channels:
{"gmail": false, "display": false} → YouTube + Discover only

**STEP 6: MANDATORY — Add Extensions After Creation**
After success, add sitelinks, callouts, and structured snippets.

**Execution Time:** 10-20 seconds

**CRITICAL REMINDERS:**
- Campaign starts PAUSED for user safety
- This costs real money — be transparent
- Never retry on failure — report error to user

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for create_demandgen_campaign tool.\n\nCreates a Demand Gen campaign across ALL Google channels:\nYouTube (In-Feed, In-Stream, Shorts), Discover, Gmail, Display, and Maps.",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (e.g., 'DemandGen Summer Promo 2026')",
      "title": "Campaign Name",
      "type": "string"
    },
    "budget_daily": {
      "description": "Daily budget in the account's native currency. IMPORTANT: Do NOT convert currencies — pass the user's amount as-is. Example: if user says '₹1000/day', pass 1000 (not a USD conversion). Google recommends minimum ~$20/day USD equivalent for Demand Gen campaigns.",
      "minimum": 1.0,
      "title": "Budget Daily",
      "type": "number"
    },
    "ad_format": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "multi_asset",
      "description": "Ad format: 'multi_asset' (image ads, default), 'video_responsive' (video ads). multi_asset requires marketing images. video_responsive requires YouTube video IDs.",
      "title": "Ad Format"
    },
    "final_url": {
      "description": "Landing page URL where users go after clicking the ad. **REQUIRED — ask the user for their website URL before calling this tool. Do NOT guess.** Must be HTTPS, reachable, and match the verified domain on the Google Ads account. Example: 'https://example.com/product'.",
      "title": "Final Url",
      "type": "string"
    },
    "business_name": {
      "description": "Business name, max 25 characters. Example: 'Adspirer'",
      "maxLength": 25,
      "title": "Business Name",
      "type": "string"
    },
    "headlines": {
      "description": "MUST BE JSON ARRAY: 1-5 headlines, each EXACTLY 40 characters maximum. Example: [\"AI Ad Management\", \"Skip the Dashboard\"]. COUNT CHARACTERS! ANY over 40 will be REJECTED!",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Headlines",
      "type": "array"
    },
    "descriptions": {
      "description": "MUST BE JSON ARRAY: 1-5 descriptions, each EXACTLY 90 characters maximum. Example: [\"Manage ads with AI - no dashboard needed.\"]. COUNT CHARACTERS BEFORE CALLING!",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Descriptions",
      "type": "array"
    },
    "long_headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "maxItems": 5,
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "MUST BE JSON ARRAY: Optional 1-5 long headlines, max 90 characters each. Required for video_responsive format. Falls back to headlines if not provided.",
      "title": "Long Headlines"
    },
    "call_to_action": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Call-to-action label. Options: LEARN_MORE, SHOP_NOW, SIGN_UP, SUBSCRIBE, DOWNLOAD, BOOK_NOW, CONTACT_US, GET_QUOTE, APPLY_NOW",
      "title": "Call To Action"
    },
    "target_locations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geographic targets globally (e.g., ['India', 'United States', 'London']). Supports countries, states, cities worldwide. Defaults to United States.",
      "title": "Target Locations"
    },
    "target_languages": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Language targets as ISO codes (e.g., ['en', 'es']). Defaults to English.",
      "title": "Target Languages"
    },
    "bidding_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "MAXIMIZE_CLICKS",
      "description": "Bidding strategy: MAXIMIZE_CLICKS (default), MAXIMIZE_CONVERSIONS, TARGET_CPA, MAXIMIZE_CONVERSION_VALUE, TARGET_ROAS. Your explicit choice is honored — the engine is advisory only.",
      "title": "Bidding Strategy"
    },
    "target_cpa": {
      "anyOf": [
        {
          "minimum": 0.01,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target CPA in account's native currency (only for TARGET_CPA bidding). Example: 25.0",
      "title": "Target Cpa"
    },
    "target_roas": {
      "anyOf": [
        {
          "minimum": 0.01,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target ROAS multiplier (only for TARGET_ROAS bidding). Example: 3.5 means 350% return on ad spend.",
      "title": "Target Roas"
    },
    "channels": {
      "anyOf": [
        {
          "additionalProperties": {
            "type": "boolean"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional channel controls. Keys: youtube_in_feed, youtube_in_stream, youtube_shorts, gmail, discover, display. All default to true (full reach). Example: {\"gmail\": false, \"display\": false} to exclude those channels.",
      "title": "Channels"
    },
    "marketing_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Landscape images (1.91:1) as [{\"url\": \"https://...\", \"name\": \"img1\"}]. At least landscape OR square images required for multi_asset.",
      "title": "Marketing Images"
    },
    "square_marketing_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Square images (1:1) as [{\"url\": \"https://...\", \"name\": \"img1\"}].",
      "title": "Square Marketing Images"
    },
    "portrait_marketing_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Portrait images (4:5) as [{\"url\": \"https://...\", \"name\": \"img1\"}]. Optional.",
      "title": "Portrait Marketing Images"
    },
    "existing_images": {
      "anyOf": [
        {
          "additionalProperties": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Existing image asset resource names to reuse (from discover_existing_assets). Keys: marketing_images_landscape, marketing_images_square, marketing_images_portrait, logos_square. Example: {\"marketing_images_landscape\": [\"customers/123/assets/456\"]}",
      "title": "Existing Images"
    },
    "youtube_video_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "YouTube video IDs (each 11 chars) for video_responsive format. 1-5 videos. Must be validated first using validate_video tool.",
      "title": "Youtube Video Ids"
    },
    "logo_asset_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Logo image asset ID from discover_existing_assets.",
      "title": "Logo Asset Id"
    },
    "logo_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New logo images as [{\"url\": \"https://...\", \"name\": \"logo1\"}].",
      "title": "Logo Images"
    },
    "asset_bundle_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Asset bundle ID (UUID) from validate_and_prepare_assets.",
      "title": "Asset Bundle Id"
    },
    "audience_segments": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: Audience targeting for the campaign. CRITICAL: Only use segment IDs returned by search_audiences tool. NEVER fabricate or guess IDs -- wrong IDs target unrelated audiences and waste budget. If search_audiences returns no results, skip audience_segments entirely. Keys: 'in_market_audience_ids' (List[int] -- people actively researching), 'affinity_audience_ids' (List[int] -- people with long-term interests), 'custom_audience_ids' (List[str] -- custom audience resource names from search_audiences), 'user_list_ids' (List[str] -- remarketing/customer match resource names). Example: {'in_market_audience_ids': [80463, 80520], 'affinity_audience_ids': [92913]}",
      "title": "Audience Segments"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID (10 digits, no dashes). REQUIRED whenever the user has more than one Google Ads account connected — this creates a REAL campaign that spends REAL money, so it must land in the account the user actually meant. Do NOT omit it and do NOT guess: carry over the customer_id already in use in this conversation, or call list_connected_accounts / get_connections_status and ask the user which account. If a call fails asking you to disambiguate, RETRY with this parameter — that error does NOT mean the account is disconnected.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_name",
    "budget_daily",
    "final_url",
    "business_name",
    "headlines",
    "descriptions"
  ],
  "title": "CreateDemandGenCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_display_campaign"></a>

## `create_display_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Create a Google **Display** campaign with a Responsive Display Ad on the Google Display Network (GDN).

🛑 **STOP — IMAGES ARE MANDATORY. ASK THE USER FIRST.** 🛑
A Display campaign cannot be created without images. Before calling this tool you MUST have:
- At least 1 landscape image URL (1.91:1 aspect ratio, min 600×314, max 5 MB)
- At least 1 square image URL (1:1 aspect ratio, min 300×300, max 5 MB)
If the user has not provided image URLs, **ASK THEM** — do not invent URLs, do not guess Wikipedia/stock-photo URLs (they 403 to server fetches), do not pass `marketing_images: null`. Suggest the user upload to a host like postimages.org and paste the direct .jpg/.png URLs.

✅ **STRONGLY RECOMMENDED — pre-validate first**: call `validate_and_prepare_assets` with the user's image URLs BEFORE calling this tool. It checks aspect ratio, dimensions, file size, and content-type, then returns an `asset_bundle_id` you can pass here. This avoids a Google Ads API rejection mid-create (e.g., "aspect ratio doesn't match expected").

**When to use this tool:**
- User explicitly asks for "Display campaign", "Google Display Network", "GDN", "banner ads", or "display ads"
- User wants visual/banner placements across millions of websites, mobile apps, YouTube, and Gmail (display slots only)
- User wants Smart Display (Google-managed automation): pass smart_display=true and bidding_strategy='TARGET_CPA'

**When NOT to use:**
- User wants text ads in Google Search → use create_search_campaign
- User wants cross-channel (YouTube + Discover + Gmail + Display together) → use create_demandgen_campaign
- User wants a PMax-like multi-channel approach → use create_pmax_campaign

**Step-by-step workflow:**
1. Ask user for: budget, landing URL, business name, **AT LEAST 1 LANDSCAPE + 1 SQUARE IMAGE URL**, headlines (1-5 @ 30 chars), long headline (1 @ 90 chars), descriptions (1-5 @ 90 chars)
2. Resolve any free-text locations via `resolve_google_locations` first (returns exact `geoTargetConstants/<id>` to avoid ambiguity)
3. Pre-validate the image URLs with `validate_and_prepare_assets` → use the returned `asset_bundle_id` (recommended) OR pass the URLs directly as `marketing_images` / `square_marketing_images` (we'll validate before upload, but the API may still reject for subtle aspect-ratio mismatches)
4. Optional: logos, YouTube videos, audience/topic/placement targeting
5. Call `create_display_campaign` with the full payload (must include images one way or another)
6. After success, add extensions: `add_sitelinks`, `add_callout_extensions`, `add_structured_snippets`

**Targeting surfaces supported (ad-group level, ignored for Smart Display):**
- audience_segments: user_interests (affinity/in-market via search_audiences), custom_audiences, user_lists, combined_audiences
- topics: topic constants
- managed_placements: specific websites/apps/YouTube channels/videos
- display_keywords: contextual keywords (always BROAD match on Display)
- demographics: age/gender/parental/income (exclude-the-inverse pattern)

**Bidding strategies:**
- MAXIMIZE_CLICKS (default, works without conversion tracking)
- MAXIMIZE_CONVERSIONS (needs conversion tracking)
- TARGET_CPA (needs target_cpa + conversion tracking)
- TARGET_ROAS (needs target_roas + conversion tracking)
- MANUAL_CPC (enhanced CPC, needs cpc_bid in account currency)
- MANUAL_CPM (viewable CPM, needs cpm_bid in account currency)

**Smart Display (smart_display=true):**
- sub_type=DISPLAY_SMART_CAMPAIGN (Google-managed)
- Bidding MUST be TARGET_CPA
- Manual audience/topic/placement/keyword/demographic inputs are REJECTED
- Account needs conversion tracking with enough history (≥50 Display conversions or ≥100 Search conversions in last 30 days)

**Character limits (strictly enforced — validation will reject before hitting the API):**
- Headlines: MAX 30 chars each (1-5)
- Long headline: MAX 90 chars (exactly 1)
- Descriptions: MAX 90 chars each (1-5)
- Business name: MAX 25 chars
- Price prefix: MAX 10 chars
- Promo text: MAX 20 chars

**Image requirements:**
- Landscape (1.91:1): min 600x314, max 5MB, 1-15 images
- Square (1:1): min 300x300, max 5MB, 1-15 images
- Landscape logo (4:1): min 512x128, up to 5 (optional)
- Square logo (1:1): min 128x128, up to 5 (optional)

**Safety:**
- Campaigns always start PAUSED (user must review + enable manually in Google Ads UI)
- Never retry on failure — surface the error to the user

**Execution time:** 10-20 seconds (atomic mutate: budget + campaign + ad group + all criteria + assets + ad)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for create_display_campaign tool.\n\nCreates a Google Display campaign (Responsive Display Ad on the Google Display Network).\nSupports standard DISPLAY channel and Smart Display (sub-type DISPLAY_SMART_CAMPAIGN).",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (e.g., 'Display Spring Promo 2026')",
      "title": "Campaign Name",
      "type": "string"
    },
    "budget_daily": {
      "description": "Daily budget in the account's native currency. IMPORTANT: Do NOT convert currencies — pass the amount as-is.",
      "minimum": 1.0,
      "title": "Budget Daily",
      "type": "number"
    },
    "final_url": {
      "description": "Landing page URL where users go after clicking the ad. **REQUIRED — ask the user for their website URL before calling this tool. Do NOT guess.** Must be HTTPS and reachable. Example: 'https://example.com/product'.",
      "title": "Final Url",
      "type": "string"
    },
    "business_name": {
      "description": "Business name, max 25 characters. Example: 'Adspirer'",
      "maxLength": 25,
      "title": "Business Name",
      "type": "string"
    },
    "headlines": {
      "description": "JSON ARRAY: 1-5 short headlines, each MAX 30 characters. Count characters carefully — any over 30 will be REJECTED.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Headlines",
      "type": "array"
    },
    "long_headline": {
      "description": "Exactly 1 long headline, max 90 characters. Example: 'Run Google, Meta, LinkedIn and TikTok ads from one workspace'",
      "maxLength": 90,
      "title": "Long Headline",
      "type": "string"
    },
    "descriptions": {
      "description": "JSON ARRAY: 1-5 descriptions, each MAX 90 characters.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Descriptions",
      "type": "array"
    },
    "marketing_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Landscape images (1.91:1, min 600x314, max 5MB). Format: [{\"url\": \"https://...\", \"name\": \"img1\"}]. At least 1 landscape required (unless reusing via existing_images).",
      "title": "Marketing Images"
    },
    "square_marketing_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Square images (1:1, min 300x300, max 5MB). Format: [{\"url\": \"https://...\", \"name\": \"img1\"}]. At least 1 square required (unless reusing via existing_images).",
      "title": "Square Marketing Images"
    },
    "logo_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional landscape logos (4:1). Up to 5.",
      "title": "Logo Images"
    },
    "square_logo_images": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional square logos (1:1, min 128x128). Up to 5.",
      "title": "Square Logo Images"
    },
    "existing_images": {
      "anyOf": [
        {
          "additionalProperties": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Reuse existing image asset resource names. Keys: marketing_images_landscape, marketing_images_square, logos_landscape, logos_square.",
      "title": "Existing Images"
    },
    "asset_bundle_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "UUID returned by `validate_and_prepare_assets`. RECOMMENDED PATH — pre-validates URLs, dimensions, aspect ratio, and content-type before upload, avoiding mid-create Google API rejections. The bundle's marketing_images_landscape, marketing_images_square, logos_landscape, logos_square are auto-mapped into this campaign's image fields (only for keys you didn't explicitly pass). Bundle is consumed (deleted) on success.",
      "title": "Asset Bundle Id"
    },
    "youtube_video_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "maxItems": 5,
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional YouTube video IDs (0-5). Each is an 11-char YouTube ID.",
      "title": "Youtube Video Ids"
    },
    "bidding_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "MAXIMIZE_CLICKS",
      "description": "One of: MAXIMIZE_CLICKS, MAXIMIZE_CONVERSIONS, TARGET_CPA, TARGET_ROAS, MANUAL_CPC (enhanced CPC), MANUAL_CPM (viewable CPM). Smart Display requires TARGET_CPA.",
      "title": "Bidding Strategy"
    },
    "target_cpa": {
      "anyOf": [
        {
          "minimum": 0.01,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target CPA in account currency. Required for TARGET_CPA bidding (and Smart Display).",
      "title": "Target Cpa"
    },
    "target_roas": {
      "anyOf": [
        {
          "minimum": 0.01,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target ROAS multiplier. Required for TARGET_ROAS bidding. Example: 3.5 = 350% ROAS.",
      "title": "Target Roas"
    },
    "cpc_bid": {
      "anyOf": [
        {
          "minimum": 0.01,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Max CPC bid in account currency. Required for MANUAL_CPC.",
      "title": "Cpc Bid"
    },
    "cpm_bid": {
      "anyOf": [
        {
          "minimum": 0.01,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Max viewable CPM bid in account currency. Required for MANUAL_CPM.",
      "title": "Cpm Bid"
    },
    "target_locations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geographic targets (e.g., ['India', 'United States']). Defaults to United States.",
      "title": "Target Locations"
    },
    "target_languages": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Language ISO codes (e.g., ['en', 'es']). Defaults to English.",
      "title": "Target Languages"
    },
    "audience_segments": {
      "anyOf": [
        {
          "additionalProperties": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Ad-group audience targeting. Keys: 'user_interests' (affinity/in-market category IDs), 'custom_audiences' (resource names), 'user_lists' (remarketing/customer-match resource names), 'combined_audiences' (resource names). Use search_audiences to get valid IDs. NEVER fabricate IDs. IGNORED when smart_display=true.",
      "title": "Audience Segments"
    },
    "topics": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Topic IDs or 'topicConstants/<id>' resource names for ad-group topic targeting. IGNORED when smart_display=true.",
      "title": "Topics"
    },
    "managed_placements": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": {
              "type": "string"
            },
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Managed placements (ad-group level). List of {type, value}: type in ('website','mobile_app','youtube_channel','youtube_video'). Example: [{\"type\":\"website\",\"value\":\"example.com\"}]. IGNORED when smart_display=true.",
      "title": "Managed Placements"
    },
    "display_keywords": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Contextual display keywords (ad-group level, always BROAD match). List of {text, negative?}: negative=true for negative keywords. IGNORED when smart_display=true.",
      "title": "Display Keywords"
    },
    "demographics": {
      "anyOf": [
        {
          "additionalProperties": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Ad-group demographic targeting (we EXCLUDE everything not listed). Keys: age_ranges (AGE_RANGE_18_24, AGE_RANGE_25_34, etc.), genders (MALE, FEMALE, UNDETERMINED), parental_statuses (PARENT, NOT_A_PARENT, UNDETERMINED), income_ranges (INCOME_RANGE_70_80, etc.). IGNORED when smart_display=true.",
      "title": "Demographics"
    },
    "call_to_action": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CTA label. Options: LEARN_MORE, SHOP_NOW, SIGN_UP, SUBSCRIBE, DOWNLOAD, BOOK_NOW, CONTACT_US, GET_QUOTE, APPLY_NOW, WATCH_NOW, ORDER_NOW, BUY_NOW, SEE_MORE, START_NOW, VISIT_SITE, DONATE_NOW, PLAY_NOW",
      "title": "Call To Action"
    },
    "format_setting": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Display ad format setting: ALL_FORMATS (default), NATIVE, or NON_NATIVE.",
      "title": "Format Setting"
    },
    "main_color": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Main brand color as hex (e.g., '#112233' or '#FFF').",
      "title": "Main Color"
    },
    "accent_color": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Accent color as hex (e.g., '#FFAABB').",
      "title": "Accent Color"
    },
    "allow_flexible_color": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": true,
      "description": "Let Google pick optimal colors when it performs better. Default true.",
      "title": "Allow Flexible Color"
    },
    "price_prefix": {
      "anyOf": [
        {
          "maxLength": 10,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional price prefix displayed before a price. Max 10 chars. Example: 'from'.",
      "title": "Price Prefix"
    },
    "promo_text": {
      "anyOf": [
        {
          "maxLength": 20,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional promotional text. Max 20 chars. Example: 'Up to 50% off'.",
      "title": "Promo Text"
    },
    "smart_display": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "If true, creates a Smart Display campaign (Google-managed, sub_type=DISPLAY_SMART_CAMPAIGN). Requires bidding_strategy=TARGET_CPA. Manual targeting fields (audience_segments/topics/managed_placements/display_keywords/demographics) are rejected when smart_display=true. Account needs conversion tracking + sufficient conversion history.",
      "title": "Smart Display"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional start date YYYY-MM-DD. Defaults to tomorrow.",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional end date YYYY-MM-DD. Defaults to 1 year from now.",
      "title": "End Date"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID (10 digits, no dashes). REQUIRED whenever the user has more than one Google Ads account connected — this creates a REAL campaign that spends REAL money, so it must land in the account the user actually meant. Do NOT omit it and do NOT guess: carry over the customer_id already in use in this conversation, or call list_connected_accounts / get_connections_status and ask the user which account. If a call fails asking you to disambiguate, RETRY with this parameter — that error does NOT mean the account is disconnected.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_name",
    "budget_daily",
    "final_url",
    "business_name",
    "headlines",
    "long_headline",
    "descriptions"
  ],
  "title": "CreateDisplayCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_label"></a>

## `create_label`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Create an account label — a reusable tag for organizing campaigns (e.g. 'Q3 Promo', 'Brand').

After creating, use add_campaign_label to attach it to a campaign. Check list_labels
first to avoid duplicates.

**Required:** name. Optional: description, background_color (hex like '#FF5733').

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Create an account label (for organizing/reporting on campaigns).",
  "properties": {
    "name": {
      "description": "The label name (e.g. 'Q3 Promo', 'High Priority').",
      "title": "Name",
      "type": "string"
    },
    "description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional label description.",
      "title": "Description"
    },
    "background_color": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional hex color like '#FF5733' for the label chip.",
      "title": "Background Color"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "name"
  ],
  "title": "CreateLabelInput",
  "type": "object"
}
```

</details>

<a id="create_meta_carousel_campaign"></a>

## `create_meta_carousel_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to create a Meta (Facebook/Instagram) carousel ad campaign with multiple images.

REQUIRED: You MUST call `select_meta_campaign_type` first and complete ALL phases it describes (audience targeting research via `search_meta_targeting`/`browse_meta_targeting`, asset discovery via `discover_meta_assets`, and user approval) BEFORE calling this tool.

IMPORTANT: This tool creates REAL campaigns that will spend money once activated. Campaign is created in PAUSED status for review.

DO NOT USE for single image - use `create_meta_image_campaign` instead.
DO NOT USE for video - use `create_meta_video_campaign` instead.

This tool creates a complete Meta carousel campaign with:
1. Campaign (objective, budget)
2. Ad Set (targeting, placements, schedule)
3. Multiple Image Uploads (one per card)
4. Ad Creative (carousel with child_attachments)
5. Ad (linking creative to ad set)

When to use this tool:
- "Create a Facebook carousel ad"
- "Launch an Instagram carousel campaign"
- "Create a multi-product ad"
- "Set up an ad with multiple images"
WhatsApp campaigns (destination_type='WHATSAPP'): if the customer's Page has more than one
WhatsApp number, ASK WHICH ONE should receive conversations and pass whatsapp_phone_number.
Leave it out and Meta picks a number itself, which may not be the one they expect.

Required Parameters:
- campaign_name: Name for the campaign
- budget_daily: Daily budget in the account's own currency, NOT cents, NOT USD (for 20/day send 20, not 2000; min 1, recommend 5-20 for testing)
- primary_text: Main ad text (recommended 125 chars for optimal display, longer text shows with "See More")
- cards: Array of 2-10 cards (see card structure below)

Card Structure (each card requires):
- image_url OR image_hash: Image source (one required)
- landing_page_url: Where users go when clicking this card
- headline: Card headline (max 45 chars)
- description: Optional card description (max 20 chars)
- call_to_action: Optional per-card CTA override

Optional Parameters:
- facebook_page_id: Auto-detected from connected account
- instagram_account_id: Enable Instagram placements
- call_to_action: Default CTA for all cards (LEARN_MORE by default)
- objective: OUTCOME_TRAFFIC (default), OUTCOME_SALES, OUTCOME_LEADS
- locations: Country codes (default: ['US'])
- age_min/age_max: Age targeting (18-65)
- genders: ['male'], ['female'], or null for all
- multi_share_optimized: Let Meta optimize card order (default: true)
- pixel_id: Meta Pixel ID for conversion tracking (required for OUTCOME_SALES)
- pixel_event_name: Conversion event (PURCHASE, LEAD, etc.)

After Creation — IMPORTANT:
- This tool created 1 campaign + 1 ad set + 1 ad.
- To add MORE ad sets (different targeting, audiences, or formats), use `add_meta_ad_set` with the returned campaign_id
- To add MORE ads to the same ad set (A/B test copy/creative), use `add_meta_ad` with the returned ad_set_id
- NEVER call this create tool again for the same campaign — that creates a SEPARATE campaign

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating Meta carousel ad campaigns",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (will be automatically suffixed with timestamp for uniqueness)",
      "title": "Campaign Name",
      "type": "string"
    },
    "objective": {
      "default": "OUTCOME_TRAFFIC",
      "description": "Campaign objective. Options: 'OUTCOME_TRAFFIC' (website clicks), 'OUTCOME_SALES' (conversions), 'OUTCOME_LEADS' (lead forms), 'OUTCOME_AWARENESS' (reach), 'OUTCOME_ENGAGEMENT'. Default: OUTCOME_TRAFFIC",
      "title": "Objective",
      "type": "string"
    },
    "budget_daily": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in the ad account's OWN CURRENCY as a decimal — NOT cents, NOT USD (for 20/day send 20, not 2000; minimum 1/day, recommended 5-20/day for testing). Mutually exclusive with budget_lifetime — provide exactly one.",
      "title": "Budget Daily"
    },
    "budget_lifetime": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in account currency (total spend over campaign duration). REQUIRES end_time to be set. Mutually exclusive with budget_daily — provide exactly one.",
      "title": "Budget Lifetime"
    },
    "end_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign/ad set end date in ISO format (e.g. '2026-04-30T23:59:59'). REQUIRED when using budget_lifetime. Optional with budget_daily.",
      "title": "End Time"
    },
    "facebook_page_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook Page ID for the ad. Auto-detected when the ad account has exactly ONE promotable Page. If the account has 2+ Pages, the tool will list them and ask you to pass this (Meta has no default Page). Call list_meta_pages to see options.",
      "title": "Facebook Page Id"
    },
    "primary_text": {
      "description": "**REQUIRED.** Primary ad text (max 2200 characters, recommended 125 or less for optimal display). Ask the user for it before calling this tool. Supports emojis, line breaks (\\n), and bullet points (e.g. '🔥 Limited Offer!\\n\\n✅ Free Shipping\\n✅ 30-Day Returns'). This is the main message that appears above the carousel.",
      "maxLength": 2200,
      "title": "Primary Text",
      "type": "string"
    },
    "cards": {
      "description": "**REQUIRED.** List of 2-10 carousel cards. Each card MUST have: image_url OR image_hash, landing_page_url (HTTPS), headline (max 45 chars). Optional per-card: description (max 20 chars), call_to_action. Ask the user for card content before calling this tool.",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Cards",
      "type": "array"
    },
    "call_to_action": {
      "default": "LEARN_MORE",
      "description": "Default call-to-action button for cards without specific CTA. Options: 'LEARN_MORE', 'SHOP_NOW', 'SIGN_UP', 'DOWNLOAD', 'BOOK_TRAVEL'. Default: LEARN_MORE",
      "title": "Call To Action",
      "type": "string"
    },
    "instagram_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram account ID for Instagram placements. If not provided, ad will run on Facebook only.",
      "title": "Instagram Account Id"
    },
    "pixel_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Pixel ID for conversion tracking. Required for OUTCOME_SALES campaigns. Use list_meta_pixels to find available pixels for your ad account.",
      "title": "Pixel Id"
    },
    "pixel_event_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conversion event to optimize for when pixel_id is provided. Options: PURCHASE, LEAD, COMPLETE_REGISTRATION, ADD_TO_CART, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, SEARCH, CONTENT_VIEW, OTHER. Use OTHER with custom_conversion_id for custom pixel events. Default: PURCHASE",
      "title": "Pixel Event Name"
    },
    "custom_conversion_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom conversion ID for optimizing towards a specific custom conversion. When provided, pixel_event_name is ignored — Meta infers the event type from the custom conversion. Get available custom conversions from your Meta Events Manager.",
      "title": "Custom Conversion Id"
    },
    "destination_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Override the ad set destination type. By default, OUTCOME_LEADS uses ON_AD (Meta lead forms) and OUTCOME_TRAFFIC uses WEBSITE. Set to 'WEBSITE' for OUTCOME_LEADS campaigns that track conversions on your website via Meta Pixel instead of using Meta's built-in lead form. Set to 'WHATSAPP' for a WhatsApp-native (Click-to-WhatsApp) campaign that opens a WhatsApp chat when tapped — requires objective=OUTCOME_ENGAGEMENT (or OUTCOME_LEADS) and facebook_page_id (the Page linked to your WhatsApp number), and does NOT use a pixel or landing_page_url. Optionally set whatsapp_welcome_message and whatsapp_ice_breakers. Options: WEBSITE, ON_AD, WEBSITE_AND_ON_AD, WHATSAPP. Only provide when overriding the default.",
      "title": "Destination Type"
    },
    "whatsapp_welcome_message": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. The greeting the person sees when the WhatsApp chat opens from the ad (the pre-filled/welcome message). Use it to guide the conversation or track which product/property generated the lead. Ignored for non-WhatsApp campaigns.",
      "title": "Whatsapp Welcome Message"
    },
    "whatsapp_phone_number": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Which WhatsApp number should receive the conversations, as displayed on the Page (e.g. '+55 51 99999-0000'). Leave it out and Meta picks a number for the Page itself — which is what you want for a Page with a single number, but on a Page with several Meta may not pick the one you expect. Pass this (or whatsapp_phone_number_id) whenever the Page has more than one number — it is far better to name the number up front than to correct it later.",
      "title": "Whatsapp Phone Number"
    },
    "whatsapp_phone_number_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Alternative to whatsapp_phone_number: the WhatsApp Business phone-number ID, if you have it from Meta Business Settings. Names the same destination — pass either one, not both.",
      "title": "Whatsapp Phone Number Id"
    },
    "whatsapp_ice_breakers": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Up to a few quick-reply prompt buttons shown when the WhatsApp chat opens (e.g. ['See pricing', 'Book a visit']). Ignored for non-WhatsApp campaigns.",
      "title": "Whatsapp Ice Breakers"
    },
    "dsa_beneficiary": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "EU Digital Services Act beneficiary — the entity (usually the advertiser's business/legal name) that benefits from this ad. REQUIRED by Meta when targeting any EU/EEA country (e.g. Spain, Germany, France). Ignored for non-EU targeting. Example: 'Acme Inc'.",
      "title": "Dsa Beneficiary"
    },
    "dsa_payor": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "EU DSA payor — the entity paying for the ad. Optional; defaults to dsa_beneficiary.",
      "title": "Dsa Payor"
    },
    "campaign_budget_optimization": {
      "default": false,
      "description": "Enable Advantage Campaign Budget (CBO). When true, the daily budget is set at the campaign level and Meta automatically distributes it across ad sets. When false (default), each ad set manages its own budget.",
      "title": "Campaign Budget Optimization",
      "type": "boolean"
    },
    "daily_min_spend_target": {
      "anyOf": [
        {
          "minimum": 0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO only: minimum daily spend for this ad set in the account's own currency as a decimal — NOT cents, NOT USD. Meta will try to spend at least this amount on this ad set each day.",
      "title": "Daily Min Spend Target"
    },
    "daily_spend_cap": {
      "anyOf": [
        {
          "minimum": 0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO only: maximum daily spend cap for this ad set in the account's own currency as a decimal — NOT cents, NOT USD. Meta will not spend more than this on this ad set each day.",
      "title": "Daily Spend Cap"
    },
    "locations": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Location targeting. Accepts country codes (['US', 'CA']) OR location objects from search_meta_targeting ([{'key': '2421836', 'type': 'city', 'radius': 25, 'distance_unit': 'mile'}]). For city/region targeting, first call search_meta_targeting with search_type='location'. ALWAYS include the 'type' field (city/region/zip/place) on each object — a key with no type is treated as a country code and rejected by Meta. For ~dozens of cities each with a radius, pass one object per city. Default: ['US']",
      "title": "Locations"
    },
    "location_types": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "DEPRECATED — do not set. Meta removed the location-targeting reach-mode ('people living in' / 'recently in' / 'travelling in'); all ad sets now reach 'people living in or recently in' the selected locations, and sending any location_types value now makes Meta reject the ad set. Leave this unset; any value you pass is ignored.",
      "title": "Location Types"
    },
    "age_min": {
      "default": 18,
      "description": "Minimum age (18-65). Default: 18",
      "maximum": 65,
      "minimum": 18,
      "title": "Age Min",
      "type": "integer"
    },
    "age_max": {
      "default": 65,
      "description": "Maximum age (18-65). Default: 65",
      "maximum": 65,
      "minimum": 18,
      "title": "Age Max",
      "type": "integer"
    },
    "genders": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Gender targeting: ['male'], ['female'], or None for all genders",
      "title": "Genders"
    },
    "interests": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of interest targeting objects from search_meta_targeting. Format: [{'id': '6003139266461', 'name': 'Fitness'}]. Use search_meta_targeting with search_type='interests' to find valid IDs.",
      "title": "Interests"
    },
    "behaviors": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of behavior targeting objects from search_meta_targeting. Format: [{'id': '6002714895372', 'name': 'Small business owners'}]. Use search_meta_targeting with search_type='behaviors' to find valid IDs.",
      "title": "Behaviors"
    },
    "job_titles": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of job title targeting objects for B2B campaigns. Format: [{'id': '123456', 'name': 'Chief Marketing Officer'}]. Use search_meta_targeting with search_type='job_titles' to find valid IDs.",
      "title": "Job Titles"
    },
    "work_employers": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of employer targeting objects for B2B campaigns. Format: [{'id': '123456', 'name': 'Google'}]. Use search_meta_targeting with search_type='work_employers' to find valid IDs.",
      "title": "Work Employers"
    },
    "life_events": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of life event targeting objects. Format: [{'id': '123456', 'name': 'Recently engaged'}]. Use search_meta_targeting with search_type='life_events' to find valid IDs.",
      "title": "Life Events"
    },
    "education_schools": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of education school targeting objects. Format: [{'id': '123456', 'name': 'Harvard University'}]. Use search_meta_targeting with search_type='education_schools' to find valid IDs.",
      "title": "Education Schools"
    },
    "education_majors": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of education major targeting objects. Format: [{'id': '123456', 'name': 'Computer Science'}]. Use search_meta_targeting with search_type='education_majors' to find valid IDs.",
      "title": "Education Majors"
    },
    "custom_audiences": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of Custom Audience IDs to include in targeting. These are audiences created in Meta Ads Manager (website visitors, customer lists, etc.)",
      "title": "Custom Audiences"
    },
    "excluded_custom_audiences": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of Custom Audience IDs to exclude from targeting.",
      "title": "Excluded Custom Audiences"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Ad Account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    },
    "special_ad_categories": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Special ad categories for housing, credit, employment, or social issues. Options: 'HOUSING', 'CREDIT', 'EMPLOYMENT', 'ISSUES_ELECTIONS_POLITICS'. Leave empty for standard ads.",
      "title": "Special Ad Categories"
    },
    "special_ad_category_country": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ISO country codes (e.g. ['BR'], ['US','CA']) the special-ad-category campaign runs in. REQUIRED by Meta whenever special_ad_categories is set. Usually leave this empty: it is filled automatically from your target locations. Only set it when your targeting is cities/regions with no country, or when the campaign country differs from the targeted locations.",
      "title": "Special Ad Category Country"
    },
    "lead_form_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lead form ID to attach when objective is OUTCOME_LEADS. Get available forms using list_meta_lead_forms tool. Only used with OUTCOME_LEADS objective.",
      "title": "Lead Form Id"
    },
    "multi_share_optimized": {
      "default": true,
      "description": "Whether to let Meta optimize card order based on performance. Default: true (recommended).",
      "title": "Multi Share Optimized",
      "type": "boolean"
    },
    "multi_advertiser": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Allow ad to appear in multi-advertiser ad format (multiple ads shown together). Set to false to opt out. Default: Meta's default (enabled). Brands that want exclusive placement should set this to false.",
      "title": "Multi Advertiser"
    },
    "url_tags": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "URL parameters (e.g. 'utm_source=meta&utm_medium=cpc&utm_campaign=brand-launch') appended to the landing-page URL on every click. Use for UTM tracking. Leading '?' is stripped automatically.",
      "title": "Url Tags"
    },
    "ad_set_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom name for the ad set. When omitted, defaults to '<campaign_name> - Ad Set'. Use this when you want a specific naming convention (e.g. 'Lookalike 1% - US - Nov 2026').",
      "title": "Ad Set Name"
    },
    "ad_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom name for the first ad created with this campaign. When omitted, defaults to '<campaign_name> - Ad'. Use this when you want a specific naming convention for the initial ad.",
      "title": "Ad Name"
    },
    "display_link": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display URL (also called 'caption') shown in the ad instead of the full landing page URL — e.g. 'brand.com' instead of 'brand.com/summer-sale-landing-page?utm=...'. Must be a domain that reflects the actual landing page domain or Meta rejects the creative at publish. NOT supported on video ads (Meta's video_data has no caption field).",
      "title": "Display Link"
    },
    "advantage_audience": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Advantage+ Audience (Meta's AI-powered audience expansion). When True, Meta treats hard interests/behaviors/custom_audiences as suggestions rather than strict filters and can deliver beyond them for better performance. When False/None, targeting is strict — Meta only shows ads to users matching the specified filters. Sets targeting.targeting_automation.advantage_audience. NOT compatible with special_ad_categories (HOUSING/CREDIT/EMPLOYMENT/ISSUES_ELECTIONS_POLITICS) — Meta rejects Advantage+ Audience for special-category ads.",
      "title": "Advantage Audience"
    },
    "advantage_plus_creative": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Master switch for Meta's Advantage+ Creative AI enhancements. Set False to opt OUT of ALL granular enhancements at once (image touchups, auto-crop, text optimizations, enhanced CTA, background generation, etc.). Leave None or True to keep Meta's defaults.",
      "title": "Advantage Plus Creative"
    },
    "disabled_creative_features": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of granular Advantage+ Creative features to opt OUT of individually. Valid field names (from Meta SDK): image_brightness_and_contrast, image_auto_crop, image_background_gen, image_enhancement, image_templates, image_touchups, image_uncrop, text_optimizations, enhance_cta, add_text_overlay, media_liquidity_animated_image, adapt_to_placement, text_generation, description_automation, site_extensions, product_extensions. Unknown names rejected. 'standard_enhancements' is NEVER accepted — Meta deprecated this bundled field in v22 and it triggers error_subcode 3858504 on campaign duplication.",
      "title": "Disabled Creative Features"
    },
    "primary_texts": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NOT supported for carousel campaigns — carousel does not use top-level Dynamic-Creative text arrays. For per-card copy variation, set each card's text in cards[]. Passing this will be rejected with a clear error. (Only image/video campaigns accept primary_texts arrays.)",
      "title": "Primary Texts"
    },
    "headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NOT supported for carousel campaigns — use per-card headlines in cards[] instead. Passing this will be rejected.",
      "title": "Headlines"
    },
    "descriptions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "NOT supported for carousel campaigns — use per-card descriptions in cards[] instead. Passing this will be rejected.",
      "title": "Descriptions"
    },
    "publisher_platforms": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Platforms to show ads on. Options: 'facebook', 'instagram', 'audience_network', 'messenger'. Default: automatic (all). To exclude Audience Network/Apps, use ['facebook', 'instagram'].",
      "title": "Publisher Platforms"
    },
    "facebook_positions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook placement positions. Options: 'feed', 'right_hand_column', 'marketplace', 'video_feeds', 'story', 'search', 'instream_video', 'facebook_reels'. Only include positions you WANT — omitted positions are excluded.",
      "title": "Facebook Positions"
    },
    "instagram_positions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram placement positions. Options: 'stream' (feed), 'story', 'reels', 'explore', 'explore_home', 'ig_search', 'profile_feed'. Only include positions you WANT — omitted positions are excluded.",
      "title": "Instagram Positions"
    },
    "app_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook App ID (numeric, registered at developers.facebook.com). Required for OUTCOME_APP_PROMOTION campaigns. NOTE: This is your FB App ID, NOT your iOS bundle ID (com.example.app) or Android package name. Find it in Meta App Dashboard → Settings → Basic.",
      "title": "App Id"
    },
    "app_store_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "App Store or Play Store listing URL for the promoted app. Required for OUTCOME_APP_PROMOTION campaigns. Examples: 'https://apps.apple.com/us/app/example/id123456789' (iOS), 'https://play.google.com/store/apps/details?id=com.example' (Android). The ad set's OS targeting is set from this URL automatically (override with user_os).",
      "title": "App Store Url"
    },
    "user_os": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Operating system to target for an app campaign: 'iOS' or 'Android'. Usually OMIT — derived from app_store_url automatically. Meta REJECTS an ad set whose OS targeting disagrees with the promoted app's platform ('Mobile Targeting Mismatch'), so set this only when you deliberately need targeting that differs from the store URL's platform. Only applies to OUTCOME_APP_PROMOTION.",
      "title": "User Os"
    },
    "app_event_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional in-app event to optimize for. When omitted, Meta defaults to APP_INSTALLS (install optimization via the ad-set optimization_goal). Provide a specific event to optimize for in-app actions: PURCHASE, LEVEL_ACHIEVED, COMPLETE_REGISTRATION, START_TRIAL, SUBSCRIBE, ADD_TO_CART, ACHIEVEMENT_UNLOCKED, D2_RETENTION, D7_RETENTION, etc. Requires Meta SDK integration in the app to fire the event. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "App Event Type"
    },
    "deep_link_url_ios": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional iOS deep-link URL that opens a specific screen in the app for users who already have it installed (e.g. 'myapp://product/123'). When the user doesn't have the app, the App Store URL opens instead. Requires Universal Links / app_link_spec configured by the app team. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "Deep Link Url Ios"
    },
    "deep_link_url_android": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional Android deep-link URL (e.g. 'myapp://product/123' or 'intent://product/123#Intent;scheme=myapp;...'). When the user doesn't have the app, the Play Store URL opens instead. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "Deep Link Url Android"
    }
  },
  "required": [
    "campaign_name",
    "primary_text",
    "cards"
  ],
  "title": "CreateMetaCarouselCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_meta_catalog_campaign"></a>

## `create_meta_catalog_campaign`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to create an Advantage+ Catalog ad / Dynamic Product Ad (DPA) — ads that automatically show products from their Meta product catalog. Keywords: "catalog ad", "dynamic product ads", "DPA", "advantage+ catalog", "shopping ads", "retarget products", "show my products".

Meta renders each product's image, name and price from the catalog at delivery — the user does NOT upload images. Always OUTCOME_SALES.

Two audience strategies:
- **prospecting** — broad audience to find new buyers (no pixel needed)
- **retargeting** — show products to people who engaged via the Pixel (REQUIRES pixel_id). Presets: viewed_not_purchased, carted_not_purchased, all_engaged_not_purchased, cross_sell_purchasers, or custom.

REQUIRED FIRST: run `validate_catalog_readiness` (confirms the catalog has products with images and whether retargeting is viable), and resolve catalog_id + product_set_id via `list_meta_catalogs` / `list_meta_product_sets`. For retargeting, get pixel_id from `list_meta_pixels`.

The campaign is created **PAUSED** so the user can review it in Ads Manager before spending.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating an Advantage+ Catalog (Dynamic Product Ad) campaign.\n\nMeta renders product images/prices/names from the catalog — you do NOT upload\nimages. Always OUTCOME_SALES. Run `validate_catalog_readiness` first.",
  "properties": {
    "campaign_name": {
      "description": "Name for the campaign.",
      "title": "Campaign Name",
      "type": "string"
    },
    "product_catalog_id": {
      "description": "Product catalog ID (required). Get it from list_meta_catalogs.",
      "title": "Product Catalog Id",
      "type": "string"
    },
    "product_set_id": {
      "description": "Product set ID to advertise (required). Get it from list_meta_product_sets — use the catalog's 'All Products' set to advertise everything, or a narrower set to boost specific items.",
      "title": "Product Set Id",
      "type": "string"
    },
    "primary_text": {
      "description": "Primary ad text shown above the products (max ~125 chars). You may use {{product.name}} / {{product.current_price}} tokens.",
      "title": "Primary Text",
      "type": "string"
    },
    "audience_type": {
      "default": "prospecting",
      "description": "'prospecting' (broad audience — find new buyers) or 'retargeting' (show products to people who already engaged via the Pixel). Retargeting REQUIRES pixel_id.",
      "title": "Audience Type",
      "type": "string"
    },
    "destination_type": {
      "default": "WEBSITE",
      "description": "Where the ad sends people. 'WEBSITE' (default — your product pages off Facebook) or 'FACEBOOK' (an on-Facebook product listing / Shop). Use WEBSITE unless you run a Facebook/Instagram Shop.",
      "title": "Destination Type",
      "type": "string"
    },
    "budget_daily": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in the account's own currency as a decimal — NOT cents, NOT USD (for 20/day send 20, not 2000; e.g. 20.0). Provide this OR budget_lifetime.",
      "title": "Budget Daily"
    },
    "budget_lifetime": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in the account's own currency as a decimal — NOT cents, NOT USD. Provide this OR budget_daily. Requires end_time.",
      "title": "Budget Lifetime"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta ad account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    },
    "headline": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Headline. Defaults to the product name ({{product.name}}) when omitted.",
      "title": "Headline"
    },
    "description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Description line. Defaults to the product price ({{product.current_price}}) when omitted.",
      "title": "Description"
    },
    "call_to_action": {
      "default": "SHOP_NOW",
      "description": "CTA button type (e.g. SHOP_NOW, LEARN_MORE, BUY_NOW).",
      "title": "Call To Action",
      "type": "string"
    },
    "landing_page_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional override landing page. Defaults to each product's own URL ({{product.url}}).",
      "title": "Landing Page Url"
    },
    "facebook_page_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook Page ID. Auto-detected when the ad account has exactly ONE promotable Page. If the account has 2+ Pages, the tool will list them and ask you to pass this (Meta has no default Page). Call list_meta_pages to see options.",
      "title": "Facebook Page Id"
    },
    "instagram_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram account ID for IG placements (optional, auto-detected).",
      "title": "Instagram Account Id"
    },
    "pixel_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Pixel ID. REQUIRED when audience_type='retargeting' (used to build the viewed/added-to-cart product audience). Optional for prospecting. Get it from list_meta_pixels.",
      "title": "Pixel Id"
    },
    "pixel_event_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conversion event to optimize/track (default PURCHASE).",
      "title": "Pixel Event Name"
    },
    "retargeting_preset": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Retargeting audience preset (audience_type='retargeting' only): 'viewed_not_purchased' (default, 14d), 'carted_not_purchased' (7d), 'all_engaged_not_purchased' (30d), 'cross_sell_purchasers' (180d), or 'custom'.",
      "title": "Retargeting Preset"
    },
    "retention_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Override the lookback window (days) for the retargeting audience.",
      "title": "Retention Days"
    },
    "include_events": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For retargeting_preset='custom': pixel events to INCLUDE (e.g. ['ViewContent','AddToCart']).",
      "title": "Include Events"
    },
    "exclude_events": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For retargeting_preset='custom': pixel events to EXCLUDE (e.g. ['Purchase'] to skip recent buyers).",
      "title": "Exclude Events"
    },
    "locations": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of country codes / location specs (default ['US']).",
      "title": "Locations"
    },
    "age_min": {
      "default": 18,
      "description": "Minimum age (default 18).",
      "title": "Age Min",
      "type": "integer"
    },
    "age_max": {
      "default": 65,
      "description": "Maximum age (default 65).",
      "title": "Age Max",
      "type": "integer"
    },
    "genders": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "['male'] / ['female'] / omit for all.",
      "title": "Genders"
    },
    "interests": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Interest targeting specs from search_meta_targeting.",
      "title": "Interests"
    },
    "behaviors": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Behavior targeting specs from search_meta_targeting.",
      "title": "Behaviors"
    },
    "custom_audiences": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom audience IDs to include (from list_meta_custom_audiences).",
      "title": "Custom Audiences"
    },
    "excluded_custom_audiences": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom audience IDs to exclude.",
      "title": "Excluded Custom Audiences"
    },
    "advantage_audience": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Enable Advantage+ Audience expansion.",
      "title": "Advantage Audience"
    },
    "special_ad_categories": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "HOUSING/EMPLOYMENT/CREDIT/etc. if applicable.",
      "title": "Special Ad Categories"
    },
    "special_ad_category_country": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ISO country codes (e.g. ['BR']) for a special-ad-category campaign. Required by Meta when special_ad_categories is set; usually auto-filled from target locations, so leave empty unless targeting cities/regions with no country.",
      "title": "Special Ad Category Country"
    },
    "campaign_budget_optimization": {
      "default": false,
      "description": "Enable CBO (budget at campaign level).",
      "title": "Campaign Budget Optimization",
      "type": "boolean"
    },
    "end_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign/ad set end time (ISO 8601). Required for lifetime budget.",
      "title": "End Time"
    },
    "ad_set_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom ad set name.",
      "title": "Ad Set Name"
    },
    "ad_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom ad name.",
      "title": "Ad Name"
    }
  },
  "required": [
    "campaign_name",
    "product_catalog_id",
    "product_set_id",
    "primary_text"
  ],
  "title": "CreateMetaCatalogCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_meta_dco_ad"></a>

## `create_meta_dco_ad`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants Meta to automatically TEST MULTIPLE IMAGES and find the best combination.

This is Dynamic Creative Optimization (DCO). Meta tests all combinations of images × headlines × primary texts and optimizes delivery automatically.

USE THIS TOOL when the user says ANY of these:
- "test these images" / "test multiple images"
- "let Meta find the winner" / "let Meta optimize"
- "Dynamic Creative" / "DCO"
- "which image performs best"
- Provides multiple images and wants Meta to choose the best
- "test combinations" / "mix and match"
- "10 images × 5 headlines"

DO NOT USE add_meta_ad multiple times for this — that creates separate ads (A/B test).
DCO is ONE ad with multiple assets that Meta mixes and optimizes.

Prerequisites:
1. You need an ad_set_id with is_dynamic_creative=true
2. If the user doesn't have one, first call `add_meta_ad_set` with `is_dynamic_creative=true`
3. Then call this tool with the image_urls and text variations

Asset limits (from Meta):
- Images: 2-10 (required)
- Headlines: up to 5 (optional)
- Primary texts: up to 5 (optional)
- Descriptions: up to 5 (optional)
- Total assets: max 30

DCO ad sets support only 1 ad — do NOT add more ads to a DCO ad set.

Example: 5 images × 3 headlines × 2 primary texts = 30 combinations, Meta finds the winner.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating a Dynamic Creative Optimization (DCO) ad.\n\nDCO lets Meta test combinations of multiple images, headlines, primary texts,\nand descriptions to find the best-performing mix automatically.",
  "properties": {
    "ad_set_id": {
      "description": "The Meta Ad Set ID. The ad set must have is_dynamic_creative=true (create one with add_meta_ad_set using is_dynamic_creative=true).",
      "title": "Ad Set Id",
      "type": "string"
    },
    "image_urls": {
      "description": "List of 2-10 image URLs for Meta to test. Meta will try all combinations.",
      "items": {
        "type": "string"
      },
      "title": "Image Urls",
      "type": "array"
    },
    "primary_text": {
      "description": "Default primary text (used if primary_texts is not provided).",
      "maxLength": 2200,
      "title": "Primary Text",
      "type": "string"
    },
    "landing_page_url": {
      "description": "**REQUIRED.** Landing page URL (HTTPS). Ask the user for it before calling.",
      "title": "Landing Page Url",
      "type": "string"
    },
    "call_to_action": {
      "default": "LEARN_MORE",
      "description": "CTA button",
      "title": "Call To Action",
      "type": "string"
    },
    "display_link": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display URL (caption) shown in the ad instead of the full landing page URL (e.g. 'brand.com'). Must match or redirect to the landing_page_url domain.",
      "title": "Display Link"
    },
    "advantage_plus_creative": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Master switch for Meta's Advantage+ Creative AI enhancements. Set False to opt OUT of ALL granular enhancements at once.",
      "title": "Advantage Plus Creative"
    },
    "disabled_creative_features": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of granular Advantage+ Creative features to opt OUT of individually. 'standard_enhancements' rejected.",
      "title": "Disabled Creative Features"
    },
    "headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of headline variations (up to 5) for Meta to test.",
      "title": "Headlines"
    },
    "headline": {
      "anyOf": [
        {
          "maxLength": 255,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Single headline (used if headlines is not provided).",
      "title": "Headline"
    },
    "primary_texts": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of primary text variations (up to 5) for Meta to test.",
      "title": "Primary Texts"
    },
    "descriptions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of description variations (up to 5) for Meta to test.",
      "title": "Descriptions"
    },
    "description": {
      "anyOf": [
        {
          "maxLength": 255,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Single description (used if descriptions is not provided).",
      "title": "Description"
    },
    "lead_form_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lead form ID for OUTCOME_LEADS campaigns.",
      "title": "Lead Form Id"
    },
    "facebook_page_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook Page ID. Auto-detected when the ad account has exactly ONE promotable Page. If the account has 2+ Pages, the tool will list them and ask you to pass this — Meta has no default Page, so pick the right one for this ad. Call list_meta_pages to see the options.",
      "title": "Facebook Page Id"
    },
    "instagram_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram account ID",
      "title": "Instagram Account Id"
    },
    "ad_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom name for the DCO ad",
      "title": "Ad Name"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta ad account ID",
      "title": "Ad Account Id"
    },
    "deep_link_url_ios": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional iOS deep link to open a specific app screen (e.g. 'myapp://product/123'). Only takes effect when the parent ad set's campaign is OUTCOME_APP_PROMOTION. Populates asset_feed_spec.link_urls[0].ios_url.",
      "title": "Deep Link Url Ios"
    },
    "deep_link_url_android": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional Android deep link (e.g. 'myapp://product/123'). Only takes effect when the parent ad set's campaign is OUTCOME_APP_PROMOTION. Populates asset_feed_spec.link_urls[0].android_url.",
      "title": "Deep Link Url Android"
    }
  },
  "required": [
    "ad_set_id",
    "image_urls",
    "primary_text",
    "landing_page_url"
  ],
  "title": "CreateMetaDcoAdInput",
  "type": "object"
}
```

</details>

<a id="create_meta_image_campaign"></a>

## `create_meta_image_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to create a Meta (Facebook/Instagram) single-image ad campaign.

REQUIRED: You MUST call `select_meta_campaign_type` first and complete ALL phases it describes (audience targeting research via `search_meta_targeting`/`browse_meta_targeting`, asset discovery via `discover_meta_assets`, and user approval) BEFORE calling this tool.

IMPORTANT: This tool creates REAL campaigns that will spend money once activated. Campaign is created in PAUSED status for review.

DO NOT USE for video ads - use `create_meta_video_campaign` instead.
DO NOT USE for carousel/multi-image - use `create_meta_carousel_campaign` instead.

This tool creates a complete Meta campaign with:
1. Campaign (objective, budget)
2. Ad Set (targeting, placements, schedule)
3. Ad Creative (image, text, CTA)
4. Ad (linking creative to ad set)

When to use this tool:
- "Create a Facebook ad campaign"
- "Launch an Instagram image ad"
- "Set up a Meta traffic campaign"
- "Create an ad with this image"

Required Parameters:
- campaign_name: Name for the campaign
- budget_daily: Daily budget in the account's own currency, NOT cents, NOT USD (for 20/day send 20, not 2000; min 1, recommend 5-20 for testing)
- primary_text: Main ad text (recommended 125 chars for optimal display, longer text shows with "See More")
- headline: Headline below image (max 255 chars, recommended 40)
- landing_page_url: Where users go when clicking

Image Source (choose ONE):
- asset_bundle_id: From `validate_and_prepare_meta_assets` (recommended for new images)
- existing_image_hash: From `discover_meta_assets` (for reusing existing images)
- image_url: Direct URL (uploaded during creation - use validate_and_prepare for better error handling)

Optional Parameters:
- facebook_page_id: Auto-detected from connected account. Only provide if multiple pages.
- instagram_account_id: Auto-detected if linked. Enable Instagram placements.
- WhatsApp campaigns (destination_type='WHATSAPP'): if the customer's Page has more than one
  WhatsApp number, ASK WHICH ONE should receive conversations and pass whatsapp_phone_number.
  Leave it out and Meta picks a number itself, which may not be the one they expect.
- objective: OUTCOME_TRAFFIC (default), OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_AWARENESS
- call_to_action: LEARN_MORE (default), SHOP_NOW, SIGN_UP, etc.
- locations: Country codes (default: ['US']) or location objects from search_meta_targeting
- age_min/age_max: Age targeting (18-65)
- genders: ['male'], ['female'], or null for all
- pixel_id: Meta Pixel ID for conversion tracking (required for OUTCOME_SALES)
- pixel_event_name: Conversion event (PURCHASE, LEAD, etc.)
- story_image_url: Different image for Stories/Reels (9:16, 1080x1920px). Uses asset_feed_spec.
- right_column_image_url: Different image for Right Column (1.91:1, 1200x628px). Uses asset_feed_spec.

Multi-Placement Creatives:
If the user wants different images for different placements (Feed, Stories, Right Column),
provide story_image_url and/or right_column_image_url. The main image will be used for Feed.
This uses Meta's asset_feed_spec with asset_customization_rules instead of object_story_spec.

After Creation — IMPORTANT:
- This tool created 1 campaign + 1 ad set + 1 ad.
- To add MORE ad sets (different targeting, audiences, or formats), use `add_meta_ad_set` with the returned campaign_id
- To add MORE ads to the same ad set (A/B test copy/creative), use `add_meta_ad` with the returned ad_set_id
- NEVER call this create tool again for the same campaign — that creates a SEPARATE campaign

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating Meta single-image ad campaigns",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (will be automatically suffixed with timestamp for uniqueness)",
      "title": "Campaign Name",
      "type": "string"
    },
    "objective": {
      "default": "OUTCOME_TRAFFIC",
      "description": "Campaign objective. Options: 'OUTCOME_TRAFFIC' (website clicks), 'OUTCOME_SALES' (conversions), 'OUTCOME_LEADS' (lead forms), 'OUTCOME_AWARENESS' (reach), 'OUTCOME_ENGAGEMENT'. Default: OUTCOME_TRAFFIC",
      "title": "Objective",
      "type": "string"
    },
    "budget_daily": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in the ad account's OWN CURRENCY as a decimal — NOT cents, NOT USD (for 20/day send 20, not 2000; minimum 1/day, recommended 5-20/day for testing). Mutually exclusive with budget_lifetime — provide exactly one.",
      "title": "Budget Daily"
    },
    "budget_lifetime": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in account currency (total spend over campaign duration). REQUIRES end_time to be set. Mutually exclusive with budget_daily — provide exactly one.",
      "title": "Budget Lifetime"
    },
    "end_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign/ad set end date in ISO format (e.g. '2026-04-30T23:59:59'). REQUIRED when using budget_lifetime. Optional with budget_daily.",
      "title": "End Time"
    },
    "asset_bundle_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Asset bundle ID from validate_and_prepare_meta_assets tool. Use this for NEW image uploads. Mutually exclusive with existing_image_hash and image_url.",
      "title": "Asset Bundle Id"
    },
    "existing_image_hash": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Existing Meta image hash from discover_meta_assets tool. Use this to REUSE images from Meta Ad Library. Mutually exclusive with asset_bundle_id and image_url.",
      "title": "Existing Image Hash"
    },
    "image_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Public image URL to upload (will be uploaded during campaign creation). Use validate_and_prepare_meta_assets for better error handling. Mutually exclusive with asset_bundle_id and existing_image_hash.",
      "title": "Image Url"
    },
    "facebook_page_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook Page ID for the ad. Auto-detected when the ad account has exactly ONE promotable Page. If the account has 2+ Pages, the tool will list them and ask you to pass this (Meta has no default Page). Call list_meta_pages to see options.",
      "title": "Facebook Page Id"
    },
    "primary_text": {
      "anyOf": [
        {
          "maxLength": 2200,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "**REQUIRED (this OR `primary_texts`).** Primary ad text (max 2200 characters, recommended 125 or less for optimal display). Ask the user for it before calling this tool. Supports emojis, line breaks (\\n), and bullet points (e.g. '🔥 Limited Offer!\\n\\n✅ Free Shipping\\n✅ 30-Day Returns'). This is the main message that appears above the image. ⚠️ If the user supplies MORE THAN ONE primary text variation, do NOT pick one and do NOT use this field — put ALL of them in the `primary_texts` array instead (Meta tests the combinations as Dynamic Creative in a single ad). Use this singular field only for a single body text. Exactly one of `primary_text` or `primary_texts` is required.",
      "title": "Primary Text"
    },
    "headline": {
      "anyOf": [
        {
          "maxLength": 255,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Headline text (max 255 characters, recommended 40). Recommended — provide this OR `headlines`. Ask the user for it before calling this tool. Appears below the image as clickable text. ⚠️ If the user supplies MORE THAN ONE headline variation, do NOT pick one and do NOT use this field — put ALL of them in the `headlines` array instead.",
      "title": "Headline"
    },
    "landing_page_url": {
      "description": "**REQUIRED.** Landing page URL where users will be directed when clicking the ad. Must be HTTPS. Ask the user for it before calling this tool.",
      "title": "Landing Page Url",
      "type": "string"
    },
    "call_to_action": {
      "default": "LEARN_MORE",
      "description": "Call-to-action button. Options: 'LEARN_MORE', 'SHOP_NOW', 'SIGN_UP', 'DOWNLOAD', 'BOOK_TRAVEL', 'CONTACT_US', 'GET_QUOTE', 'SUBSCRIBE', 'WATCH_MORE'. Default: LEARN_MORE",
      "title": "Call To Action",
      "type": "string"
    },
    "description": {
      "anyOf": [
        {
          "maxLength": 255,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional description text (max 255 characters, recommended 30). Appears under the headline on some placements. If the user supplies more than one description variation, use the `descriptions` array field instead.",
      "title": "Description"
    },
    "story_image_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional image URL for Stories/Reels placements (9:16 ratio, recommended 1080x1920px). If provided, the main image is used for Feed and this image for Stories/Reels. Meta's asset_feed_spec will be used instead of object_story_spec.",
      "title": "Story Image Url"
    },
    "right_column_image_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional image URL for Right Column placement (1.91:1 ratio, recommended 1200x628px). If provided, Meta's asset_feed_spec will be used instead of object_story_spec.",
      "title": "Right Column Image Url"
    },
    "instagram_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram account ID for Instagram placements. If not provided, ad will run on Facebook only.",
      "title": "Instagram Account Id"
    },
    "pixel_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Pixel ID for conversion tracking. Required for OUTCOME_SALES campaigns. Use list_meta_pixels to find available pixels for your ad account.",
      "title": "Pixel Id"
    },
    "pixel_event_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conversion event to optimize for when pixel_id is provided. Options: PURCHASE, LEAD, COMPLETE_REGISTRATION, ADD_TO_CART, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, SEARCH, CONTENT_VIEW, OTHER. Use OTHER with custom_conversion_id for custom pixel events. Default: PURCHASE",
      "title": "Pixel Event Name"
    },
    "custom_conversion_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom conversion ID for optimizing towards a specific custom conversion. When provided, pixel_event_name is ignored — Meta infers the event type from the custom conversion. Get available custom conversions from your Meta Events Manager.",
      "title": "Custom Conversion Id"
    },
    "destination_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Override the ad set destination type. By default, OUTCOME_LEADS uses ON_AD (Meta lead forms) and OUTCOME_TRAFFIC uses WEBSITE. Set to 'WEBSITE' for OUTCOME_LEADS campaigns that track conversions on your website via Meta Pixel instead of using Meta's built-in lead form. Set to 'WHATSAPP' for a WhatsApp-native (Click-to-WhatsApp) campaign that opens a WhatsApp chat when tapped — requires objective=OUTCOME_ENGAGEMENT (or OUTCOME_LEADS) and facebook_page_id (the Page linked to your WhatsApp number), and does NOT use a pixel or landing_page_url. Optionally set whatsapp_welcome_message and whatsapp_ice_breakers. Options: WEBSITE, ON_AD, WEBSITE_AND_ON_AD, WHATSAPP. Only provide when overriding the default.",
      "title": "Destination Type"
    },
    "whatsapp_welcome_message": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. The greeting the person sees when the WhatsApp chat opens from the ad (the pre-filled/welcome message). Use it to guide the conversation or track which product/property generated the lead. Ignored for non-WhatsApp campaigns.",
      "title": "Whatsapp Welcome Message"
    },
    "whatsapp_phone_number": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Which WhatsApp number should receive the conversations, as displayed on the Page (e.g. '+55 51 99999-0000'). Leave it out and Meta picks a number for the Page itself — which is what you want for a Page with a single number, but on a Page with several Meta may not pick the one you expect. Pass this (or whatsapp_phone_number_id) whenever the Page has more than one number — it is far better to name the number up front than to correct it later.",
      "title": "Whatsapp Phone Number"
    },
    "whatsapp_phone_number_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Alternative to whatsapp_phone_number: the WhatsApp Business phone-number ID, if you have it from Meta Business Settings. Names the same destination — pass either one, not both.",
      "title": "Whatsapp Phone Number Id"
    },
    "whatsapp_ice_breakers": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Up to a few quick-reply prompt buttons shown when the WhatsApp chat opens (e.g. ['See pricing', 'Book a visit']). Ignored for non-WhatsApp campaigns.",
      "title": "Whatsapp Ice Breakers"
    },
    "dsa_beneficiary": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "EU Digital Services Act beneficiary — the entity (usually the advertiser's business/legal name) that benefits from this ad. REQUIRED by Meta when targeting any EU/EEA country (e.g. Spain, Germany, France). Ignored for non-EU targeting. Example: 'Acme Inc'.",
      "title": "Dsa Beneficiary"
    },
    "dsa_payor": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "EU DSA payor — the entity paying for the ad. Optional; defaults to dsa_beneficiary.",
      "title": "Dsa Payor"
    },
    "campaign_budget_optimization": {
      "default": false,
      "description": "Enable Advantage Campaign Budget (CBO). When true, the daily budget is set at the campaign level and Meta automatically distributes it across ad sets. When false (default), each ad set manages its own budget.",
      "title": "Campaign Budget Optimization",
      "type": "boolean"
    },
    "daily_min_spend_target": {
      "anyOf": [
        {
          "minimum": 0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO only: minimum daily spend for this ad set in the account's own currency as a decimal — NOT cents, NOT USD. Meta will try to spend at least this amount on this ad set each day.",
      "title": "Daily Min Spend Target"
    },
    "daily_spend_cap": {
      "anyOf": [
        {
          "minimum": 0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO only: maximum daily spend cap for this ad set in the account's own currency as a decimal — NOT cents, NOT USD. Meta will not spend more than this on this ad set each day.",
      "title": "Daily Spend Cap"
    },
    "locations": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Location targeting. Accepts country codes (['US', 'CA']) OR location objects from search_meta_targeting ([{'key': '2421836', 'type': 'city', 'radius': 25, 'distance_unit': 'mile'}]). For city/region targeting, first call search_meta_targeting with search_type='location'. ALWAYS include the 'type' field (city/region/zip/place) on each object — a key with no type is treated as a country code and rejected by Meta. For ~dozens of cities each with a radius, pass one object per city. Default: ['US']",
      "title": "Locations"
    },
    "location_types": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "DEPRECATED — do not set. Meta removed the location-targeting reach-mode ('people living in' / 'recently in' / 'travelling in'); all ad sets now reach 'people living in or recently in' the selected locations, and sending any location_types value now makes Meta reject the ad set. Leave this unset; any value you pass is ignored.",
      "title": "Location Types"
    },
    "age_min": {
      "default": 18,
      "description": "Minimum age (18-65). Default: 18",
      "maximum": 65,
      "minimum": 18,
      "title": "Age Min",
      "type": "integer"
    },
    "age_max": {
      "default": 65,
      "description": "Maximum age (18-65). Default: 65",
      "maximum": 65,
      "minimum": 18,
      "title": "Age Max",
      "type": "integer"
    },
    "genders": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Gender targeting: ['male'], ['female'], or None for all genders",
      "title": "Genders"
    },
    "interests": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of interest targeting objects from search_meta_targeting. Format: [{'id': '6003139266461', 'name': 'Fitness'}]. Use search_meta_targeting with search_type='interests' to find valid IDs.",
      "title": "Interests"
    },
    "behaviors": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of behavior targeting objects from search_meta_targeting. Format: [{'id': '6002714895372', 'name': 'Small business owners'}]. Use search_meta_targeting with search_type='behaviors' to find valid IDs.",
      "title": "Behaviors"
    },
    "job_titles": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of job title targeting objects for B2B campaigns. Format: [{'id': '123456', 'name': 'Chief Marketing Officer'}]. Use search_meta_targeting with search_type='job_titles' to find valid IDs.",
      "title": "Job Titles"
    },
    "work_employers": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of employer targeting objects for B2B campaigns. Format: [{'id': '123456', 'name': 'Google'}]. Use search_meta_targeting with search_type='work_employers' to find valid IDs.",
      "title": "Work Employers"
    },
    "life_events": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of life event targeting objects. Format: [{'id': '123456', 'name': 'Recently engaged'}]. Use search_meta_targeting with search_type='life_events' to find valid IDs.",
      "title": "Life Events"
    },
    "education_schools": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of education school targeting objects. Format: [{'id': '123456', 'name': 'Harvard University'}]. Use search_meta_targeting with search_type='education_schools' to find valid IDs.",
      "title": "Education Schools"
    },
    "education_majors": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of education major targeting objects. Format: [{'id': '123456', 'name': 'Computer Science'}]. Use search_meta_targeting with search_type='education_majors' to find valid IDs.",
      "title": "Education Majors"
    },
    "custom_audiences": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of Custom Audience IDs to include in targeting. These are audiences created in Meta Ads Manager (website visitors, customer lists, etc.)",
      "title": "Custom Audiences"
    },
    "excluded_custom_audiences": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of Custom Audience IDs to exclude from targeting.",
      "title": "Excluded Custom Audiences"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Ad Account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    },
    "special_ad_categories": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Special ad categories for housing, credit, employment, or social issues. Options: 'HOUSING', 'CREDIT', 'EMPLOYMENT', 'ISSUES_ELECTIONS_POLITICS'. Leave empty for standard ads.",
      "title": "Special Ad Categories"
    },
    "special_ad_category_country": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ISO country codes (e.g. ['BR'], ['US','CA']) the special-ad-category campaign runs in. REQUIRED by Meta whenever special_ad_categories is set. Usually leave this empty: it is filled automatically from your target locations. Only set it when your targeting is cities/regions with no country, or when the campaign country differs from the targeted locations.",
      "title": "Special Ad Category Country"
    },
    "lead_form_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lead form ID to attach when objective is OUTCOME_LEADS. Get available forms using list_meta_lead_forms tool. Only used with OUTCOME_LEADS objective.",
      "title": "Lead Form Id"
    },
    "multi_advertiser": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Allow ad to appear in multi-advertiser ad format (multiple ads shown together). Set to false to opt out. Default: Meta's default (enabled). Brands that want exclusive placement should set this to false.",
      "title": "Multi Advertiser"
    },
    "url_tags": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "URL parameters (e.g. 'utm_source=meta&utm_medium=cpc&utm_campaign=brand-launch') appended to the landing-page URL on every click. Use for UTM tracking. Leading '?' is stripped automatically.",
      "title": "Url Tags"
    },
    "ad_set_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom name for the ad set. When omitted, defaults to '<campaign_name> - Ad Set'. Use this when you want a specific naming convention (e.g. 'Lookalike 1% - US - Nov 2026').",
      "title": "Ad Set Name"
    },
    "ad_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom name for the first ad created with this campaign. When omitted, defaults to '<campaign_name> - Ad'. Use this when you want a specific naming convention for the initial ad.",
      "title": "Ad Name"
    },
    "display_link": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display URL (also called 'caption') shown in the ad instead of the full landing page URL — e.g. 'brand.com' instead of 'brand.com/summer-sale-landing-page?utm=...'. Must be a domain that reflects the actual landing page domain or Meta rejects the creative at publish. NOT supported on video ads (Meta's video_data has no caption field).",
      "title": "Display Link"
    },
    "advantage_audience": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Advantage+ Audience (Meta's AI-powered audience expansion). When True, Meta treats hard interests/behaviors/custom_audiences as suggestions rather than strict filters and can deliver beyond them for better performance. When False/None, targeting is strict — Meta only shows ads to users matching the specified filters. Sets targeting.targeting_automation.advantage_audience. NOT compatible with special_ad_categories (HOUSING/CREDIT/EMPLOYMENT/ISSUES_ELECTIONS_POLITICS) — Meta rejects Advantage+ Audience for special-category ads.",
      "title": "Advantage Audience"
    },
    "advantage_plus_creative": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Master switch for Meta's Advantage+ Creative AI enhancements. Set False to opt OUT of ALL granular enhancements at once (image touchups, auto-crop, text optimizations, enhanced CTA, background generation, etc.). Leave None or True to keep Meta's defaults.",
      "title": "Advantage Plus Creative"
    },
    "disabled_creative_features": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of granular Advantage+ Creative features to opt OUT of individually. Valid field names (from Meta SDK): image_brightness_and_contrast, image_auto_crop, image_background_gen, image_enhancement, image_templates, image_touchups, image_uncrop, text_optimizations, enhance_cta, add_text_overlay, media_liquidity_animated_image, adapt_to_placement, text_generation, description_automation, site_extensions, product_extensions. Unknown names rejected. 'standard_enhancements' is NEVER accepted — Meta deprecated this bundled field in v22 and it triggers error_subcode 3858504 on campaign duplication.",
      "title": "Disabled Creative Features"
    },
    "primary_texts": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of primary text (body) variations (2-5). **USE THIS whenever the user gives you 2 or more primary texts** — it creates ONE ad where Meta's asset_feed_spec (Dynamic Creative) tests every body/headline combination, which is what users mean by 'multiple primary texts per creative'. Do NOT instead create separate ads or drop the extras into the singular primary_text field. Supersedes primary_text — provide EITHER primary_text (single) OR primary_texts (list), not both.",
      "title": "Primary Texts"
    },
    "headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of headline (title) variations (2-5). **USE THIS whenever the user gives you 2 or more headlines** — it creates ONE ad where Meta's asset_feed_spec (Dynamic Creative) tests every combination. Do NOT instead create separate ads or drop the extras into the singular headline field. Supersedes headline — provide EITHER headline (single) OR headlines (list), not both.",
      "title": "Headlines"
    },
    "descriptions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of description variations (2-5). Use this whenever the user gives you 2 or more descriptions — Meta's asset_feed_spec (Dynamic Creative) tests the combinations in ONE ad. Supersedes description — provide EITHER description (single) OR descriptions (list), not both.",
      "title": "Descriptions"
    },
    "publisher_platforms": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Platforms to show ads on. Options: 'facebook', 'instagram', 'audience_network', 'messenger'. Default: automatic (all). To exclude Audience Network/Apps, use ['facebook', 'instagram'].",
      "title": "Publisher Platforms"
    },
    "facebook_positions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook placement positions. Options: 'feed', 'right_hand_column', 'marketplace', 'video_feeds', 'story', 'search', 'instream_video', 'facebook_reels'. Only include positions you WANT — omitted positions are excluded.",
      "title": "Facebook Positions"
    },
    "instagram_positions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram placement positions. Options: 'stream' (feed), 'story', 'reels', 'explore', 'explore_home', 'ig_search', 'profile_feed'. Only include positions you WANT — omitted positions are excluded.",
      "title": "Instagram Positions"
    },
    "app_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook App ID (numeric, registered at developers.facebook.com). Required for OUTCOME_APP_PROMOTION campaigns. NOTE: This is your FB App ID, NOT your iOS bundle ID (com.example.app) or Android package name. Find it in Meta App Dashboard → Settings → Basic.",
      "title": "App Id"
    },
    "app_store_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "App Store or Play Store listing URL for the promoted app. Required for OUTCOME_APP_PROMOTION campaigns. Examples: 'https://apps.apple.com/us/app/example/id123456789' (iOS), 'https://play.google.com/store/apps/details?id=com.example' (Android). The ad set's OS targeting is set from this URL automatically (override with user_os).",
      "title": "App Store Url"
    },
    "user_os": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Operating system to target for an app campaign: 'iOS' or 'Android'. Usually OMIT — derived from app_store_url automatically. Meta REJECTS an ad set whose OS targeting disagrees with the promoted app's platform ('Mobile Targeting Mismatch'), so set this only when you deliberately need targeting that differs from the store URL's platform. Only applies to OUTCOME_APP_PROMOTION.",
      "title": "User Os"
    },
    "app_event_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional in-app event to optimize for. When omitted, Meta defaults to APP_INSTALLS (install optimization via the ad-set optimization_goal). Provide a specific event to optimize for in-app actions: PURCHASE, LEVEL_ACHIEVED, COMPLETE_REGISTRATION, START_TRIAL, SUBSCRIBE, ADD_TO_CART, ACHIEVEMENT_UNLOCKED, D2_RETENTION, D7_RETENTION, etc. Requires Meta SDK integration in the app to fire the event. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "App Event Type"
    },
    "deep_link_url_ios": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional iOS deep-link URL that opens a specific screen in the app for users who already have it installed (e.g. 'myapp://product/123'). When the user doesn't have the app, the App Store URL opens instead. Requires Universal Links / app_link_spec configured by the app team. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "Deep Link Url Ios"
    },
    "deep_link_url_android": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional Android deep-link URL (e.g. 'myapp://product/123' or 'intent://product/123#Intent;scheme=myapp;...'). When the user doesn't have the app, the Play Store URL opens instead. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "Deep Link Url Android"
    }
  },
  "required": [
    "campaign_name",
    "landing_page_url"
  ],
  "title": "CreateMetaImageCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_meta_product_set"></a>

## `create_meta_product_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to advertise a SUBSET of their catalog — "boost just these items / these SKUs", "promote my sale items", "make a set of my new arrivals".

Creates a product SET (a filtered grouping of EXISTING catalog products) — it does NOT create or upload products (those come from Shopify / Commerce Manager).

Provide either:
- retailer_ids: a list of SKUs to include (simplest — "boost just these items"), or
- filter: an advanced raw Meta product-set filter

When to use:
- "Boost these 3 products", "create a set of my sale items"
- Before a catalog ad when the user wants a specific subset, not the whole catalog

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating a product set (a filtered grouping of EXISTING catalog products).",
  "properties": {
    "catalog_id": {
      "description": "Product catalog ID the set belongs to (required). Get it from list_meta_catalogs.",
      "title": "Catalog Id",
      "type": "string"
    },
    "name": {
      "description": "Name for the new product set (e.g. 'Summer Sale', 'Footwear').",
      "title": "Name",
      "type": "string"
    },
    "retailer_ids": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of product retailer IDs / SKUs to include (e.g. ['SKU-001','SKU-002']). Use this to 'boost just these items'. Either retailer_ids or filter is required.",
      "title": "Retailer Ids"
    },
    "filter": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Advanced: a raw Meta product-set filter dict, e.g. {'product_type': {'i_contains': 'shoes'}}. Overrides retailer_ids if both are given.",
      "title": "Filter"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta ad account ID. If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "catalog_id",
    "name"
  ],
  "title": "CreateMetaProductSetInput",
  "type": "object"
}
```

</details>

<a id="create_meta_video_campaign"></a>

## `create_meta_video_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to create a Meta (Facebook/Instagram) video ad campaign.

REQUIRED: You MUST call `select_meta_campaign_type` first and complete ALL phases it describes (audience targeting research via `search_meta_targeting`/`browse_meta_targeting`, asset discovery via `discover_meta_assets`, and user approval) BEFORE calling this tool.

IMPORTANT: This tool creates REAL campaigns that will spend money once activated. Campaign is created in PAUSED status for review.

DO NOT USE for image ads - use `create_meta_image_campaign` instead.
DO NOT USE for carousel - use `create_meta_carousel_campaign` instead.

This tool creates a complete Meta video campaign with:
1. Campaign (objective, budget)
2. Ad Set (targeting, placements, schedule)
3. Video Upload (handles large files with chunked upload)
4. Ad Creative (video, text, CTA)
5. Ad (linking creative to ad set)

When to use this tool:
- "Create a Facebook video ad campaign"
- "Launch an Instagram video ad"
- "Set up a Meta Reels campaign"
- "Create an ad with this video"
WhatsApp campaigns (destination_type='WHATSAPP'): if the customer's Page has more than one
WhatsApp number, ASK WHICH ONE should receive conversations and pass whatsapp_phone_number.
Leave it out and Meta picks a number itself, which may not be the one they expect.

Required Parameters:
- campaign_name: Name for the campaign
- budget_daily: Daily budget in the account's own currency, NOT cents, NOT USD (for 20/day send 20, not 2000; min 1, recommend 5-20 for testing)
- primary_text: Main ad text (recommended 125 chars for optimal display, longer text shows with "See More")
- landing_page_url: Where users go when clicking

Video Source (choose ONE):
- video_url: Public video URL (will be uploaded during creation)
- existing_video_id: Existing Meta video ID (for reusing previously uploaded videos)

Optional Parameters:
- facebook_page_id: Auto-detected from connected account
- instagram_account_id: Enable Instagram placements
- thumbnail_url: Custom thumbnail image (Meta auto-generates if not provided)
- headline: Headline below video (optional for video ads)
- description: Description text (max 255 chars, recommended 30)
- call_to_action: WATCH_MORE (default), LEARN_MORE, SHOP_NOW, etc.
- objective: OUTCOME_TRAFFIC (default), OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_AWARENESS
- locations: Country codes (default: ['US'])
- age_min/age_max: Age targeting (18-65)
- genders: ['male'], ['female'], or null for all
- optimize_for_reels: true for vertical (9:16) videos
- pixel_id: Meta Pixel ID for conversion tracking (required for OUTCOME_SALES)
- pixel_event_name: Conversion event (PURCHASE, LEAD, etc.)

Video Specifications:
- Formats: MP4, MOV (recommended: MP4 H.264)
- Max size: 4GB (recommended under 1GB)
- Duration: 1 sec - 240 min (recommended 15-60 sec)
- Feed: 1:1 or 4:5 aspect ratio
- Stories/Reels: 9:16 aspect ratio

After Creation — IMPORTANT:
- This tool created 1 campaign + 1 ad set + 1 ad.
- To add MORE ad sets (different targeting, audiences, or formats), use `add_meta_ad_set` with the returned campaign_id
- To add MORE ads to the same ad set (A/B test copy/creative), use `add_meta_ad` with the returned ad_set_id
- NEVER call this create tool again for the same campaign — that creates a SEPARATE campaign

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for creating Meta video ad campaigns",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (will be automatically suffixed with timestamp for uniqueness)",
      "title": "Campaign Name",
      "type": "string"
    },
    "objective": {
      "default": "OUTCOME_TRAFFIC",
      "description": "Campaign objective. Options: 'OUTCOME_TRAFFIC' (website clicks), 'OUTCOME_SALES' (conversions), 'OUTCOME_LEADS' (lead forms), 'OUTCOME_AWARENESS' (reach), 'OUTCOME_ENGAGEMENT'. Default: OUTCOME_TRAFFIC",
      "title": "Objective",
      "type": "string"
    },
    "budget_daily": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in the ad account's OWN CURRENCY as a decimal — NOT cents, NOT USD (for 20/day send 20, not 2000; minimum 1/day, recommended 5-20/day for testing). Mutually exclusive with budget_lifetime — provide exactly one.",
      "title": "Budget Daily"
    },
    "budget_lifetime": {
      "anyOf": [
        {
          "minimum": 1.0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in account currency (total spend over campaign duration). REQUIRES end_time to be set. Mutually exclusive with budget_daily — provide exactly one.",
      "title": "Budget Lifetime"
    },
    "end_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign/ad set end date in ISO format (e.g. '2026-04-30T23:59:59'). REQUIRED when using budget_lifetime. Optional with budget_daily.",
      "title": "End Time"
    },
    "video_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Public video URL to upload. Video will be uploaded during campaign creation. Supports MP4, MOV formats. Max 4GB, recommended under 1GB. Mutually exclusive with existing_video_id.",
      "title": "Video Url"
    },
    "existing_video_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Existing Meta video ID from your Ad Library. Use this to REUSE videos already uploaded to Meta. Mutually exclusive with video_url.",
      "title": "Existing Video Id"
    },
    "thumbnail_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional custom thumbnail image URL. If not provided, Meta will auto-generate thumbnails from video.",
      "title": "Thumbnail Url"
    },
    "facebook_page_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook Page ID for the ad. Auto-detected when the ad account has exactly ONE promotable Page. If the account has 2+ Pages, the tool will list them and ask you to pass this (Meta has no default Page). Call list_meta_pages to see options.",
      "title": "Facebook Page Id"
    },
    "primary_text": {
      "anyOf": [
        {
          "maxLength": 2200,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "**REQUIRED (this OR `primary_texts`).** Primary ad text (max 2200 characters, recommended 125 or less for optimal display). Ask the user for it before calling this tool. Supports emojis, line breaks (\\n), and bullet points (e.g. '🔥 Limited Offer!\\n\\n✅ Free Shipping\\n✅ 30-Day Returns'). This is the main message that appears above the video. ⚠️ If the user supplies MORE THAN ONE primary text variation, do NOT pick one and do NOT use this field — put ALL of them in the `primary_texts` array instead (Meta tests the combinations as Dynamic Creative in a single ad). Use this singular field only for a single body text. Exactly one of `primary_text` or `primary_texts` is required.",
      "title": "Primary Text"
    },
    "headline": {
      "anyOf": [
        {
          "maxLength": 255,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Headline text (max 255 characters, recommended 40). Optional for video ads. Appears below the video on some placements. ⚠️ If the user supplies MORE THAN ONE headline variation, put ALL of them in the `headlines` array field instead of picking one.",
      "title": "Headline"
    },
    "landing_page_url": {
      "description": "**REQUIRED.** Landing page URL where users will be directed when clicking the ad. Must be HTTPS. Ask the user for it before calling this tool.",
      "title": "Landing Page Url",
      "type": "string"
    },
    "call_to_action": {
      "default": "WATCH_MORE",
      "description": "Call-to-action button. Options: 'WATCH_MORE' (default for video), 'LEARN_MORE', 'SHOP_NOW', 'SIGN_UP', 'DOWNLOAD', 'BOOK_TRAVEL', 'CONTACT_US'. Default: WATCH_MORE",
      "title": "Call To Action",
      "type": "string"
    },
    "description": {
      "anyOf": [
        {
          "maxLength": 255,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional description text (max 255 characters, recommended 30). Appears under the headline on some placements. If the user supplies more than one description variation, use the `descriptions` array field instead.",
      "title": "Description"
    },
    "instagram_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram account ID for Instagram placements. If not provided, ad will run on Facebook only.",
      "title": "Instagram Account Id"
    },
    "pixel_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Pixel ID for conversion tracking. Required for OUTCOME_SALES campaigns. Use list_meta_pixels to find available pixels for your ad account.",
      "title": "Pixel Id"
    },
    "pixel_event_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Conversion event to optimize for when pixel_id is provided. Options: PURCHASE, LEAD, COMPLETE_REGISTRATION, ADD_TO_CART, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, SEARCH, CONTENT_VIEW, OTHER. Use OTHER with custom_conversion_id for custom pixel events. Default: PURCHASE",
      "title": "Pixel Event Name"
    },
    "custom_conversion_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom conversion ID for optimizing towards a specific custom conversion. When provided, pixel_event_name is ignored — Meta infers the event type from the custom conversion. Get available custom conversions from your Meta Events Manager.",
      "title": "Custom Conversion Id"
    },
    "destination_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Override the ad set destination type. By default, OUTCOME_LEADS uses ON_AD (Meta lead forms) and OUTCOME_TRAFFIC uses WEBSITE. Set to 'WEBSITE' for OUTCOME_LEADS campaigns that track conversions on your website via Meta Pixel instead of using Meta's built-in lead form. Set to 'WHATSAPP' for a WhatsApp-native (Click-to-WhatsApp) campaign that opens a WhatsApp chat when tapped — requires objective=OUTCOME_ENGAGEMENT (or OUTCOME_LEADS) and facebook_page_id (the Page linked to your WhatsApp number), and does NOT use a pixel or landing_page_url. Optionally set whatsapp_welcome_message and whatsapp_ice_breakers. Options: WEBSITE, ON_AD, WEBSITE_AND_ON_AD, WHATSAPP. Only provide when overriding the default.",
      "title": "Destination Type"
    },
    "whatsapp_welcome_message": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. The greeting the person sees when the WhatsApp chat opens from the ad (the pre-filled/welcome message). Use it to guide the conversation or track which product/property generated the lead. Ignored for non-WhatsApp campaigns.",
      "title": "Whatsapp Welcome Message"
    },
    "whatsapp_phone_number": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Which WhatsApp number should receive the conversations, as displayed on the Page (e.g. '+55 51 99999-0000'). Leave it out and Meta picks a number for the Page itself — which is what you want for a Page with a single number, but on a Page with several Meta may not pick the one you expect. Pass this (or whatsapp_phone_number_id) whenever the Page has more than one number — it is far better to name the number up front than to correct it later.",
      "title": "Whatsapp Phone Number"
    },
    "whatsapp_phone_number_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Alternative to whatsapp_phone_number: the WhatsApp Business phone-number ID, if you have it from Meta Business Settings. Names the same destination — pass either one, not both.",
      "title": "Whatsapp Phone Number Id"
    },
    "whatsapp_ice_breakers": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For destination_type='WHATSAPP' only. Up to a few quick-reply prompt buttons shown when the WhatsApp chat opens (e.g. ['See pricing', 'Book a visit']). Ignored for non-WhatsApp campaigns.",
      "title": "Whatsapp Ice Breakers"
    },
    "dsa_beneficiary": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "EU Digital Services Act beneficiary — the entity (usually the advertiser's business/legal name) that benefits from this ad. REQUIRED by Meta when targeting any EU/EEA country (e.g. Spain, Germany, France). Ignored for non-EU targeting. Example: 'Acme Inc'.",
      "title": "Dsa Beneficiary"
    },
    "dsa_payor": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "EU DSA payor — the entity paying for the ad. Optional; defaults to dsa_beneficiary.",
      "title": "Dsa Payor"
    },
    "campaign_budget_optimization": {
      "default": false,
      "description": "Enable Advantage Campaign Budget (CBO). When true, the daily budget is set at the campaign level and Meta automatically distributes it across ad sets. When false (default), each ad set manages its own budget.",
      "title": "Campaign Budget Optimization",
      "type": "boolean"
    },
    "daily_min_spend_target": {
      "anyOf": [
        {
          "minimum": 0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO only: minimum daily spend for this ad set in the account's own currency as a decimal — NOT cents, NOT USD. Meta will try to spend at least this amount on this ad set each day.",
      "title": "Daily Min Spend Target"
    },
    "daily_spend_cap": {
      "anyOf": [
        {
          "minimum": 0,
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO only: maximum daily spend cap for this ad set in the account's own currency as a decimal — NOT cents, NOT USD. Meta will not spend more than this on this ad set each day.",
      "title": "Daily Spend Cap"
    },
    "locations": {
      "anyOf": [
        {
          "items": {},
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Location targeting. Accepts country codes (['US', 'CA']) OR location objects from search_meta_targeting ([{'key': '2421836', 'type': 'city', 'radius': 25, 'distance_unit': 'mile'}]). For city/region targeting, first call search_meta_targeting with search_type='location'. ALWAYS include the 'type' field (city/region/zip/place) on each object — a key with no type is treated as a country code and rejected by Meta. For ~dozens of cities each with a radius, pass one object per city. Default: ['US']",
      "title": "Locations"
    },
    "location_types": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "DEPRECATED — do not set. Meta removed the location-targeting reach-mode ('people living in' / 'recently in' / 'travelling in'); all ad sets now reach 'people living in or recently in' the selected locations, and sending any location_types value now makes Meta reject the ad set. Leave this unset; any value you pass is ignored.",
      "title": "Location Types"
    },
    "age_min": {
      "default": 18,
      "description": "Minimum age (18-65). Default: 18",
      "maximum": 65,
      "minimum": 18,
      "title": "Age Min",
      "type": "integer"
    },
    "age_max": {
      "default": 65,
      "description": "Maximum age (18-65). Default: 65",
      "maximum": 65,
      "minimum": 18,
      "title": "Age Max",
      "type": "integer"
    },
    "genders": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Gender targeting: ['male'], ['female'], or None for all genders",
      "title": "Genders"
    },
    "interests": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of interest targeting objects from search_meta_targeting. Format: [{'id': '6003139266461', 'name': 'Fitness'}]. Use search_meta_targeting with search_type='interests' to find valid IDs.",
      "title": "Interests"
    },
    "behaviors": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of behavior targeting objects from search_meta_targeting. Format: [{'id': '6002714895372', 'name': 'Small business owners'}]. Use search_meta_targeting with search_type='behaviors' to find valid IDs.",
      "title": "Behaviors"
    },
    "job_titles": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of job title targeting objects for B2B campaigns. Format: [{'id': '123456', 'name': 'Chief Marketing Officer'}]. Use search_meta_targeting with search_type='job_titles' to find valid IDs.",
      "title": "Job Titles"
    },
    "work_employers": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of employer targeting objects for B2B campaigns. Format: [{'id': '123456', 'name': 'Google'}]. Use search_meta_targeting with search_type='work_employers' to find valid IDs.",
      "title": "Work Employers"
    },
    "life_events": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of life event targeting objects. Format: [{'id': '123456', 'name': 'Recently engaged'}]. Use search_meta_targeting with search_type='life_events' to find valid IDs.",
      "title": "Life Events"
    },
    "education_schools": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of education school targeting objects. Format: [{'id': '123456', 'name': 'Harvard University'}]. Use search_meta_targeting with search_type='education_schools' to find valid IDs.",
      "title": "Education Schools"
    },
    "education_majors": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of education major targeting objects. Format: [{'id': '123456', 'name': 'Computer Science'}]. Use search_meta_targeting with search_type='education_majors' to find valid IDs.",
      "title": "Education Majors"
    },
    "custom_audiences": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of Custom Audience IDs to include in targeting. These are audiences created in Meta Ads Manager (website visitors, customer lists, etc.)",
      "title": "Custom Audiences"
    },
    "excluded_custom_audiences": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of Custom Audience IDs to exclude from targeting.",
      "title": "Excluded Custom Audiences"
    },
    "ad_account_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Meta Ad Account ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Ad Account Id"
    },
    "special_ad_categories": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Special ad categories for housing, credit, employment, or social issues. Options: 'HOUSING', 'CREDIT', 'EMPLOYMENT', 'ISSUES_ELECTIONS_POLITICS'. Leave empty for standard ads.",
      "title": "Special Ad Categories"
    },
    "special_ad_category_country": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ISO country codes (e.g. ['BR'], ['US','CA']) the special-ad-category campaign runs in. REQUIRED by Meta whenever special_ad_categories is set. Usually leave this empty: it is filled automatically from your target locations. Only set it when your targeting is cities/regions with no country, or when the campaign country differs from the targeted locations.",
      "title": "Special Ad Category Country"
    },
    "lead_form_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lead form ID to attach when objective is OUTCOME_LEADS. Get available forms using list_meta_lead_forms tool. Only used with OUTCOME_LEADS objective.",
      "title": "Lead Form Id"
    },
    "optimize_for_reels": {
      "default": false,
      "description": "Whether to optimize for Reels placement. Set to true for vertical videos (9:16 aspect ratio).",
      "title": "Optimize For Reels",
      "type": "boolean"
    },
    "multi_advertiser": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Allow ad to appear in multi-advertiser ad format (multiple ads shown together). Set to false to opt out. Default: Meta's default (enabled). Brands that want exclusive placement should set this to false.",
      "title": "Multi Advertiser"
    },
    "url_tags": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "URL parameters (e.g. 'utm_source=meta&utm_medium=cpc&utm_campaign=brand-launch') appended to the landing-page URL on every click. Use for UTM tracking. Leading '?' is stripped automatically.",
      "title": "Url Tags"
    },
    "ad_set_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom name for the ad set. When omitted, defaults to '<campaign_name> - Ad Set'. Use this when you want a specific naming convention (e.g. 'Lookalike 1% - US - Nov 2026').",
      "title": "Ad Set Name"
    },
    "ad_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Custom name for the first ad created with this campaign. When omitted, defaults to '<campaign_name> - Ad'. Use this when you want a specific naming convention for the initial ad.",
      "title": "Ad Name"
    },
    "display_link": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display URL (also called 'caption') shown in the ad instead of the full landing page URL — e.g. 'brand.com' instead of 'brand.com/summer-sale-landing-page?utm=...'. Must be a domain that reflects the actual landing page domain or Meta rejects the creative at publish. NOT supported on video ads (Meta's video_data has no caption field).",
      "title": "Display Link"
    },
    "advantage_audience": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Advantage+ Audience (Meta's AI-powered audience expansion). When True, Meta treats hard interests/behaviors/custom_audiences as suggestions rather than strict filters and can deliver beyond them for better performance. When False/None, targeting is strict — Meta only shows ads to users matching the specified filters. Sets targeting.targeting_automation.advantage_audience. NOT compatible with special_ad_categories (HOUSING/CREDIT/EMPLOYMENT/ISSUES_ELECTIONS_POLITICS) — Meta rejects Advantage+ Audience for special-category ads.",
      "title": "Advantage Audience"
    },
    "advantage_plus_creative": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Master switch for Meta's Advantage+ Creative AI enhancements. Set False to opt OUT of ALL granular enhancements at once (image touchups, auto-crop, text optimizations, enhanced CTA, background generation, etc.). Leave None or True to keep Meta's defaults.",
      "title": "Advantage Plus Creative"
    },
    "disabled_creative_features": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of granular Advantage+ Creative features to opt OUT of individually. Valid field names (from Meta SDK): image_brightness_and_contrast, image_auto_crop, image_background_gen, image_enhancement, image_templates, image_touchups, image_uncrop, text_optimizations, enhance_cta, add_text_overlay, media_liquidity_animated_image, adapt_to_placement, text_generation, description_automation, site_extensions, product_extensions. Unknown names rejected. 'standard_enhancements' is NEVER accepted — Meta deprecated this bundled field in v22 and it triggers error_subcode 3858504 on campaign duplication.",
      "title": "Disabled Creative Features"
    },
    "primary_texts": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of primary text (body) variations (2-5). **USE THIS whenever the user gives you 2 or more primary texts** — it creates ONE ad where Meta's asset_feed_spec (Dynamic Creative) tests every body/headline combination, which is what users mean by 'multiple primary texts per creative'. Do NOT instead create separate ads or drop the extras into the singular primary_text field. Supersedes primary_text — provide EITHER primary_text (single) OR primary_texts (list), not both.",
      "title": "Primary Texts"
    },
    "headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of headline (title) variations (2-5). **USE THIS whenever the user gives you 2 or more headlines** — it creates ONE ad where Meta's asset_feed_spec (Dynamic Creative) tests every combination. Do NOT instead create separate ads or drop the extras into the singular headline field. Supersedes headline — provide EITHER headline (single) OR headlines (list), not both.",
      "title": "Headlines"
    },
    "descriptions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "List of description variations (2-5). Use this whenever the user gives you 2 or more descriptions — Meta's asset_feed_spec (Dynamic Creative) tests the combinations in ONE ad. Supersedes description — provide EITHER description (single) OR descriptions (list), not both.",
      "title": "Descriptions"
    },
    "publisher_platforms": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Platforms to show ads on. Options: 'facebook', 'instagram', 'audience_network', 'messenger'. Default: automatic (all). To exclude Audience Network/Apps, use ['facebook', 'instagram'].",
      "title": "Publisher Platforms"
    },
    "facebook_positions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook placement positions. Options: 'feed', 'right_hand_column', 'marketplace', 'video_feeds', 'story', 'search', 'instream_video', 'facebook_reels'. Only include positions you WANT — omitted positions are excluded.",
      "title": "Facebook Positions"
    },
    "instagram_positions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Instagram placement positions. Options: 'stream' (feed), 'story', 'reels', 'explore', 'explore_home', 'ig_search', 'profile_feed'. Only include positions you WANT — omitted positions are excluded.",
      "title": "Instagram Positions"
    },
    "app_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Facebook App ID (numeric, registered at developers.facebook.com). Required for OUTCOME_APP_PROMOTION campaigns. NOTE: This is your FB App ID, NOT your iOS bundle ID (com.example.app) or Android package name. Find it in Meta App Dashboard → Settings → Basic.",
      "title": "App Id"
    },
    "app_store_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "App Store or Play Store listing URL for the promoted app. Required for OUTCOME_APP_PROMOTION campaigns. Examples: 'https://apps.apple.com/us/app/example/id123456789' (iOS), 'https://play.google.com/store/apps/details?id=com.example' (Android). The ad set's OS targeting is set from this URL automatically (override with user_os).",
      "title": "App Store Url"
    },
    "user_os": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Operating system to target for an app campaign: 'iOS' or 'Android'. Usually OMIT — derived from app_store_url automatically. Meta REJECTS an ad set whose OS targeting disagrees with the promoted app's platform ('Mobile Targeting Mismatch'), so set this only when you deliberately need targeting that differs from the store URL's platform. Only applies to OUTCOME_APP_PROMOTION.",
      "title": "User Os"
    },
    "app_event_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional in-app event to optimize for. When omitted, Meta defaults to APP_INSTALLS (install optimization via the ad-set optimization_goal). Provide a specific event to optimize for in-app actions: PURCHASE, LEVEL_ACHIEVED, COMPLETE_REGISTRATION, START_TRIAL, SUBSCRIBE, ADD_TO_CART, ACHIEVEMENT_UNLOCKED, D2_RETENTION, D7_RETENTION, etc. Requires Meta SDK integration in the app to fire the event. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "App Event Type"
    },
    "deep_link_url_ios": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional iOS deep-link URL that opens a specific screen in the app for users who already have it installed (e.g. 'myapp://product/123'). When the user doesn't have the app, the App Store URL opens instead. Requires Universal Links / app_link_spec configured by the app team. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "Deep Link Url Ios"
    },
    "deep_link_url_android": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional Android deep-link URL (e.g. 'myapp://product/123' or 'intent://product/123#Intent;scheme=myapp;...'). When the user doesn't have the app, the Play Store URL opens instead. Only valid for OUTCOME_APP_PROMOTION.",
      "title": "Deep Link Url Android"
    }
  },
  "required": [
    "campaign_name",
    "landing_page_url"
  ],
  "title": "CreateMetaVideoCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_negative_keyword_list"></a>

## `create_negative_keyword_list`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Create a new (empty) shared negative keyword list.

Creates a reusable negative keyword list (SharedSet) you can then fill with
`add_negative_keywords_to_list` and attach to campaigns with
`attach_negative_keyword_list_to_campaign`.

**Parameters:** name (required).
**Use when:** "create a negative keyword list called ...", "make a shared negatives list".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Create a new (empty) shared negative keyword list.",
  "properties": {
    "name": {
      "description": "Name for the new negative keyword list.",
      "title": "Name",
      "type": "string"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID. Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "name"
  ],
  "title": "CreateNegativeKeywordListInput",
  "type": "object"
}
```

</details>

<a id="create_pmax_campaign"></a>

## `create_pmax_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

🔄 LONG-RUNNING TOOL: Creates a Google Performance Max campaign with validated images. Emits MCP progress updates during authentication, asset upload, and campaign creation (typically 15-30 seconds). Progress stages: validate → commit.

⚠️ CRITICAL PREREQUISITES:
1. MUST have valid asset_bundle_id from validate_and_prepare_assets tool OR existing_image_ids from discover_existing_assets
2. MUST have all campaign text details from user
3. Creates REAL campaigns that cost REAL money
4. Call ONLY ONCE per campaign - do NOT retry automatically

🎥 **VIDEOS ARE OPTIONAL BUT RECOMMENDED:**
- Videos significantly improve PMAX performance (higher CTR, better engagement)
- **Always ask the user**: "Would you like to add YouTube videos to this campaign?"
- If yes: validate with `validate_video` tool, then include `youtube_video_ids` parameter
- If no: proceed without videos (campaigns work fine either way)
- See STEP 3.5 below for complete video guidance

⚠️ GOOGLE ADS POLICY NOTE:
Avoid keywords related to health conditions, medical treatments, financial hardship, or political topics. These may trigger policy violations. Use general service terms instead.
Example: Use "senior care services" not "nursing care", "home services" not "medical services"

📋 **YOUR CRITICAL ROLE: Campaign Strategist & Text Creator**

**STEP 1: Verify Prerequisites**

Before calling this tool, ensure you have:
- ✅ Valid asset_bundle_id from validate_and_prepare_assets (max 1 hour old)
- ✅ All required campaign details from user (see below)

If asset_bundle_id is missing or expired:
- Guide user to re-upload images
- Call validate_and_prepare_assets again
- Get new asset_bundle_id

**STEP 2: Collect Campaign Details from User**

YOU MUST collect these from the user (ask if not provided):

**REQUIRED Fields:**
1. **Campaign Name**
   - Example: "Premium Watches Summer 2025"
   - Make it descriptive and unique

2. **Daily Budget**
   - Google recommends ~$50/day USD equivalent for Performance Max
   - IMPORTANT: Accept the user's budget in their stated currency — do NOT convert to USD
   - Ask: "What's your daily advertising budget?"

3. **Final URL** (Landing Page)
   - Must match verified domain in Google Ads
   - Example: "https://example.com/watches"
   - Ask: "What's the landing page URL for this campaign?"

4. **Business Name**
   - Maximum 25 characters
   - Example: "Luxury Watch Co"
   - Will appear in ads

**STEP 3: Generate High-Quality Ad Copy**

As an expert copywriter, you MUST create compelling ad text:

**🚨 BEFORE GENERATING TEXT - READ CHARACTER LIMITS 🚨**

**Headlines (3-15 required):**
- **STRICT LIMIT: 30 characters maximum per headline**
- Count characters BEFORE calling this tool!
- Examples:
  - "Premium Luxury Watches" (22 chars) ✅
  - "Free Shipping" (13 chars) ✅
  - "Certified Authentic" (19 chars) ✅

**Descriptions (2-4 required):**
- **STRICT LIMIT: 80 characters maximum per description**
- Count characters BEFORE calling this tool!
- Examples:
  - "Shop authentic luxury timepieces with free worldwide shipping." (63 chars) ✅
  - "Expert-curated Swiss watches. Certified authentic. Shop now." (61 chars) ✅

**Long Headlines (1-5 REQUIRED):**
- **STRICT LIMIT: 90 characters maximum per long headline**
- At least 1 is REQUIRED for Performance Max
- Count characters BEFORE calling this tool!
- Example: "Premium Swiss Watches - Certified Authentic, Free Worldwide Shipping" (70 chars) ✅

**⚠️ WILL BE REJECTED IF YOU EXCEED LIMITS - NO RETRIES!**
**⚠️ COUNT CHARACTERS CAREFULLY - VALIDATION IS STRICT!**

**How to Count Characters:**
- Use extended thinking to count each text element
- Double-check your character counts before calling
- If close to limit, shorten it to be safe
- Do NOT assume backend will fix it - it won't!
- Use clear, concise language
- Focus on user benefits

**OPTIONAL Fields (use defaults if not provided):**
- target_locations: Defaults to ["United States"]
- target_languages: Defaults to ["English"]

**🎥 STEP 3.5: YouTube Videos (OPTIONAL but Highly Recommended)**

**⚠️ IMPORTANT: Always ask the user about videos!**

Videos significantly improve Performance Max campaign performance:
- **Higher CTR**: Video ads stand out more than static images
- **Better engagement**: Users watch videos longer
- **Wider reach**: Serves on YouTube, Display, Discover, Gmail, Search
- **Lower CPA**: Video ads often convert better

**When to Ask:**
- AFTER discovering existing assets
- AFTER user uploads images
- BEFORE calling create_pmax_campaign

**What to Say:**
"I've prepared your images. Would you like to add YouTube videos to this campaign? Videos can significantly improve performance (higher CTR and engagement). They're optional but recommended.

If yes:
- You'll need videos uploaded to YouTube (public or unlisted)
- Minimum 10 seconds duration
- I can validate them for you

If no:
- We can proceed with images only
- You can add videos later if needed"

**How to Include Videos:**

1. **User provides YouTube video URL or ID**
   - Example: "https://youtu.be/eIZtladpm6c"
   - Example: "eIZtladpm6c"

2. **You validate it**
   ```
   Call: validate_video
   Arguments: {
     "video_url_or_id": "eIZtladpm6c",
     "platform": "pmax"
   }
   ```

3. **Include in campaign**
   - Add `youtube_video_ids` parameter: `["eIZtladpm6c"]`
   - Can include up to 5 videos

**Video Specifications:**
- **Aspect Ratios**: Landscape (16:9), Square (1:1), Vertical (9:16)
- **Duration**: Minimum 10 seconds (no maximum)
- **Maximum**: 5 videos per campaign
- **Source**: Must be on YouTube (public or unlisted, NOT private)
- **Validation**: Happens via Google Ads API during campaign creation

**If user doesn't have videos:**
- Proceed without them (campaigns work fine without videos)
- Mention they can add videos later
- Note: Google may auto-generate videos from images if none provided

**STEP 4: Call create_pmax_campaign**

After you have ALL details:
- Validate character counts yourself BEFORE calling
- Call create_pmax_campaign with complete payload
- Wait for response (may take 15-30 seconds)

**STEP 5: Handle Response**

**If SUCCESS:**
- Celebrate with user! 🎉
- Show campaign ID, name, budget, status
- Explain campaign starts PAUSED for safety
- 🔴 **IMMEDIATELY proceed to STEP 6 (Extensions)** — do NOT stop here!

**If FAILURE:**

1. **Asset Bundle Expired:**
   - Error: "Asset bundle not found or expired"
   - Action: Guide user to re-upload images
   - Call validate_and_prepare_assets again

2. **Character Limit Errors:**
   - Error: "Headline exceeds 30 characters"
   - Action: Shorten the text and try again
   - Show user which field caused the error

3. **Google Ads API Errors:**
   - Domain not verified
   - Budget too low
   - Account suspended
   - Action: Explain error clearly, provide troubleshooting steps

4. **Authentication Errors:**
   - Error: "No Google Ads account connected"
   - Action: Guide user to connect their Google Ads account

🔴 **STEP 6: MANDATORY — Add Extensions After Creation**
After the campaign is successfully created, you MUST:
1. Crawl the user's website to gather relevant page links, features, and service categories
2. Add sitelinks: at least 4 links to key pages (add_sitelinks tool)
3. Add callout extensions: 4-6 business highlights (add_callout_extensions tool)
4. Add structured snippets: categorized features (add_structured_snippets tool)
5. Verify with list_campaign_extensions to confirm all extensions are attached
Extensions are FREE and increase ad visibility by 15-25%. NEVER skip this step.

**DO NOT:**
- Retry automatically on failure
- Call multiple times for same campaign
- Skip collecting user's campaign details
- Proceed without valid asset_bundle_id
- Skip adding extensions after campaign creation

**Campaign Creation Best Practices:**

🔴 **PRE-STEP: ALWAYS Discover Assets First**
   - Before ANY PMAX campaign, call discover_existing_assets
   - Show user what assets were found (images, logos with dimensions)
   - Ask: "Would you like to reuse these existing assets, upload new ones, or mix both?"
   - Based on answer:
     - Reuse → Use existing_image_ids in create_pmax_campaign
     - Upload new → Use validate_and_prepare_assets → asset_bundle_id
     - Mix both → Use both parameters (hybrid mode)
   - 🚫 NEVER skip this step

1. **Research First:**
   - Understand the business, products, audience
   - Review website messaging
   - Identify key selling points

2. **Strategic Ad Copy:**
   - Use action verbs
   - Include numbers/stats if available
   - Highlight benefits over features
   - Create urgency when appropriate
   - Match brand voice

3. **Quality Over Quantity:**
   - Better to have 5 great headlines than 15 mediocre ones
   - Each headline should be unique and valuable
   - Avoid repetition

4. **User Safety:**
   - Confirm budget with user before creating
   - Explain campaigns start PAUSED
   - Remind them this costs real money

**Example Complete Flow:**

User: "Create a PMax campaign for my luxury watch store"

You: "I'll help you create a PMax campaign! First, let me check if you have any existing assets we can reuse."

[Call discover_existing_assets(target_domain="luxurywatches.com")]

[Returns: 8 images found]

You: "Great news! I found 8 validated images from your previous campaigns:
- 4 landscape images (1200x628)
- 2 square images (1200x1200)
- 2 logo images (1200x1200)

Would you like to:
A) Reuse these existing images (saves time, consistent branding)
B) Upload new images
C) Mix both (reuse some + add new ones)"

[User chooses A - Reuse]

You: "Perfect! Now I need a few details:
1. What daily budget would you like? (minimum $10, recommended $50+)
2. What's your landing page URL?
3. What locations should we target? (e.g., 'Bay Area', 'San Francisco', 'United States')

I'll create compelling headlines and descriptions based on your luxury watch business."

[User provides budget: $75, URL: https://luxurywatches.com, Location: Bay Area]

You: "Great! Here's what I'll create:

**Campaign Name:** Premium Watches Campaign 2025
**Budget:** $75/day
**Landing Page:** https://luxurywatches.com
**Locations:** Bay Area (targeted precisely)

**Headlines I've generated:**
- Premium Luxury Watches
- Certified Authentic
- Free Worldwide Shipping
[...12 more]

**Descriptions:**
- Shop authentic Swiss timepieces with lifetime warranty and expert curation.
- Discover premium watches from top brands. Free shipping. 30-day returns.
[...2 more]

**Using existing images:** 8 validated images (reuse mode)

Ready to create this campaign? (It will start PAUSED so you can review first)"

[User confirms]

[Call create_pmax_campaign with existing_image_ids from discovery]

**Returns:**
- Campaign ID, name, status
- Asset group summary
- Next steps for activation

**Execution Time:** 15-30 seconds (direct backend API call)

**Authentication:** Required (MCP OAuth 2.1)

**CRITICAL REMINDERS:**
- Asset bundle expires after 1 hour
- Campaign starts PAUSED for user safety
- This costs real money - be transparent
- Never retry on failure - report error to user
- Provide excellent user experience throughout

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for create_pmax_campaign tool.\n\nSupports two modes:\n1. Single asset group (flat fields — backward compatible)\n2. Multiple asset groups (asset_groups array — #183)\n\nIf asset_groups is provided, it takes priority over flat fields.",
  "properties": {
    "asset_bundle_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Asset bundle ID from validate_and_prepare_assets tool (UUID format). Optional if existing_image_ids provided.",
      "title": "Asset Bundle Id"
    },
    "existing_image_ids": {
      "anyOf": [
        {
          "additionalProperties": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Resource names of existing images to reuse (from discover_existing_assets). Optional if asset_bundle_id provided. ⚠️ MUST include 'logos_square' — Google Ads REQUIRES a logo for every PMax asset group. If discover_existing_assets found no logos, use hybrid mode: upload a logo via validate_and_prepare_assets (asset_bundle_id) + pass existing_image_ids for other images. Example: {'marketing_images_landscape': ['customers/123/assets/456'], 'marketing_images_square': ['customers/123/assets/789'], 'logos_square': ['customers/123/assets/101']}",
      "title": "Existing Image Ids"
    },
    "campaign_name": {
      "description": "Campaign name (e.g., 'Premium Watches Summer 2025')",
      "title": "Campaign Name",
      "type": "string"
    },
    "budget_daily": {
      "description": "Daily budget in the account's native currency. IMPORTANT: Do NOT convert currencies — pass the user's amount as-is. Example: if user says '₹5000/day', pass 5000 (not a USD conversion). The Google Ads API interprets this in the account's currency automatically. Google recommends minimum ~$50/day USD equivalent for Performance Max campaigns.",
      "minimum": 1.0,
      "title": "Budget Daily",
      "type": "number"
    },
    "merchant_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Link a Merchant Center account to make this a RETAIL Performance Max campaign (it advertises the MC feed's products; asset groups then support product listing filters via add_asset_group_listing_filter). Get it from get_merchant_center_links. Omit for a standard (non-retail) PMax campaign.",
      "title": "Merchant Id"
    },
    "feed_label": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For retail PMax: the Merchant Center feed label to advertise (must match a label in the MC account, or it serves no products). Omit to target unlabeled products.",
      "title": "Feed Label"
    },
    "headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "MUST BE JSON ARRAY: 3-15 headlines, each EXACTLY 30 characters maximum. REQUIRED for single-group mode. Omit if using asset_groups array. Commas ARE allowed within headlines. Example: [\"Luxury Watches\", \"Swiss Made\"]. COUNT CHARACTERS! ANY over 30 will be REJECTED!",
      "title": "Headlines"
    },
    "descriptions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "MUST BE JSON ARRAY: 2-4 descriptions, each EXACTLY 80 characters maximum (STRICT!). REQUIRED for single-group mode. Omit if using asset_groups array. Commas ARE allowed within descriptions. Example: [\"Shop authentic luxury timepieces with expert curation.\"] (63 chars). COUNT CHARACTERS BEFORE CALLING - ANY over 80 will be REJECTED!",
      "title": "Descriptions"
    },
    "business_name": {
      "anyOf": [
        {
          "maxLength": 25,
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Business name, max 25 characters. REQUIRED for single-group mode. Omit if using asset_groups array. Commas ARE allowed.",
      "title": "Business Name"
    },
    "final_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Landing page URL. REQUIRED for single-group mode. Omit if using asset_groups array.",
      "title": "Final Url"
    },
    "long_headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "MUST BE JSON ARRAY: REQUIRED 1-5 long headlines, each EXACTLY 90 characters maximum. REQUIRED for single-group mode. Omit if using asset_groups array. Google Ads REQUIRES at least 1 long headline for Performance Max campaigns. Commas ARE allowed. Example: [\"Premium Swiss Watches - Certified Authentic, Free Shipping\"]. COUNT CHARACTERS! ANY over 90 will be REJECTED!",
      "title": "Long Headlines"
    },
    "target_locations": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: Geographic targets -- supports countries, states, cities, and regions globally. Examples: ['India'], ['Bangalore, India'], ['Karnataka'], ['New York, NY'], ['United States', 'Canada']. Defaults to United States.",
      "title": "Target Locations"
    },
    "target_languages": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: Language targets (e.g., ['English', 'Spanish']). Defaults to English.",
      "title": "Target Languages"
    },
    "youtube_video_ids": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: List of YouTube video IDs (11 characters each). Videos must be validated first using validate_video tool. Maximum 5 videos per campaign. Example: ['dQw4w9WgXcQ', 'jNQXAC9IVRw']. Videos are OPTIONAL for PMAX - campaigns can be created without them.",
      "title": "Youtube Video Ids"
    },
    "search_themes": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: Search themes hint Google AI about what your customers search for. Max 50 per asset group. NOT keywords — no match types, no bids. Derive from keyword research, business profile, or user input. Example: ['AI ad management', 'automate google ads', 'MCP advertising tool']. Duplicates and blanks are filtered automatically. Pass [] (empty list) to explicitly skip search themes (e.g., remarketing-only campaigns). If omitted (null), themes are auto-derived from headlines.",
      "title": "Search Themes"
    },
    "brand_guidelines_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: enable Brand Guidelines (default off). When true, the logo and business name are linked as CAMPAIGN-level assets (Google's brand-controlled layout). ⚠️ This can ONLY be set at creation — it is NOT changeable later. After create, complete the asset group with add_pmax_asset_group (brand-guidelines-aware) or link the campaign logo with add_pmax_campaign_logo.",
      "title": "Brand Guidelines Enabled"
    },
    "audience_signals": {
      "anyOf": [
        {
          "additionalProperties": true,
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: Audience signals tell Google AI who your ideal customers are. CRITICAL: Only use segment IDs returned by the search_audiences tool. NEVER fabricate, guess, or invent audience IDs. Wrong IDs will target completely unrelated audiences (e.g., 'Vehicles' instead of 'Jewelry') and waste the customer's ad budget. If search_audiences returns no results, skip audience signals entirely rather than guessing IDs. Keys: 'in_market_audience_ids' (List[int]), 'affinity_audience_ids' (List[int]), 'custom_audience_ids' (List[str] resource names), 'user_list_ids' (List[str] userList resource names for remarketing/customer match -- e.g. 'customers/123/userLists/456' from search_audiences), 'audience_name' (str). Example: {'in_market_audience_ids': [80432, 80210], 'user_list_ids': ['customers/123/userLists/456'], 'audience_name': 'SaaS Buyers'}",
      "title": "Audience Signals"
    },
    "bidding_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Bidding strategy for the campaign. Options: 'MAXIMIZE_CONVERSIONS' - Get the most conversions within budget. 'MAXIMIZE_CONVERSION_VALUE' - Optimize for highest value conversions. If not specified, the system auto-selects based on account data. Recommended: MAXIMIZE_CONVERSIONS for most new campaigns.",
      "title": "Bidding Strategy"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target ROAS (Return on Ad Spend) for MAXIMIZE_CONVERSION_VALUE bidding. Example: 3.0 means you want $3 revenue for every $1 spent. Only used when bidding_strategy='MAXIMIZE_CONVERSION_VALUE'.",
      "title": "Target Roas"
    },
    "asset_groups": {
      "anyOf": [
        {
          "items": {
            "additionalProperties": true,
            "type": "object"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "OPTIONAL: Multiple asset groups for a single PMax campaign. When provided, this OVERRIDES the flat headline/description/business_name/final_url fields. Each group is a dict with keys: group_name (required, unique), headlines (3-15), descriptions (2-4), long_headlines (1-5), business_name, final_url, existing_image_ids (optional), search_themes (optional), audience_signals (optional). Max 100 groups per campaign. All groups share the same campaign budget and bidding strategy. Example: [{'group_name': 'SaaS Founders', 'headlines': ['AI Ad Manager', 'Skip Dashboards', 'Automate Ads'], 'descriptions': ['Manage ads via AI chat.', '100+ tools.'], 'long_headlines': ['AI Ad Management'], 'business_name': 'Adspirer', 'final_url': 'https://adspirer.com', 'search_themes': ['AI ads'], 'audience_signals': {'in_market_audience_ids': [80432]}}]",
      "title": "Asset Groups"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID (10 digits, no dashes). REQUIRED whenever the user has more than one Google Ads account connected — this creates a REAL campaign that spends REAL money, so it must land in the account the user actually meant. Do NOT omit it and do NOT guess: carry over the customer_id already in use in this conversation, or call list_connected_accounts / get_connections_status and ask the user which account. If a call fails asking you to disambiguate, RETRY with this parameter — that error does NOT mean the account is disconnected.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_name",
    "budget_daily"
  ],
  "title": "CreatePMaxCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_search_campaign"></a>

## `create_search_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

🔄 LONG-RUNNING TOOL: Creates a Google Ads Search campaign with full structure.

Emits MCP progress updates during authentication and campaign creation (typically 5-10 seconds).
Progress stages: validate → commit.

⚠️ CRITICAL WARNING ⚠️
- Call this tool ONLY ONCE per campaign
- Creates REAL campaigns that cost REAL money
- Do NOT retry automatically if errors occur
- Report errors to user instead of retrying

⚠️ GOOGLE ADS POLICY NOTE:
Avoid keywords related to health conditions, medical treatments, financial hardship, or political topics. These may trigger policy violations. Use general service terms instead.
Example: Use "senior care services" not "nursing care", "home services" not "medical services"

YOUR ROLE: Expert Google Ads Campaign Strategist

BEFORE calling this tool, YOU MUST:
1. **Research the business thoroughly:**
   - Understand products/services, target audience, value propositions
   - Analyze competitive landscape and market positioning
   - Review website messaging and offers
   - Consider seasonal factors and current trends

2. **🔍 KEYWORD RESEARCH (CRITICAL - Call research_keywords tool FIRST):**
   Do NOT use generic SEO keywords. Get HIGH-INTENT keywords with real CPC data!

   **YOU MUST call the research_keywords tool BEFORE this tool:**

   Steps:
   a) Call the research_keywords tool:
      ```
      Tool: research_keywords
      Arguments: {
        "business_description": "Emergency plumbing services for homeowners",
        "website_url": "https://example.com",
        "target_location": "New York, NY"
      }
      ```

   b) The tool will return:
      - Keyword table with dynamic CPC thresholds (adapts to industry)
      - HIGH/MEDIUM/LOW intent keywords
      - Budget recommendations (Conservative/Moderate/Aggressive)
      - Top 15-20 recommended keywords

   c) Show the keyword table to the user

   d) Ask user if they want to modify keyword selection:
      - Can add/remove specific keywords
      - Can use only HIGH intent keywords
      - Default: use recommended keywords

   e) Extract keyword texts from the research_keywords result
      - Use the recommended keywords for this tool's 'keywords' parameter
      - Max 15-20 keywords per ad group
      - Will use BROAD match automatically (Google's 2025 recommendation)

3. **Analyze Target Demographics:**
   For each ad group, consider who the ideal customer is:
   - **Age**: What age groups are most likely to buy? (e.g., luxury products → 35-54, gaming → 18-34)
   - **Gender**: Is the product/service gender-specific? (e.g., women's fashion → FEMALE)
   - **Income**: What income level can afford this? (e.g., luxury → TOP_10/80_90, budget → 0_50/50_60)

   **Examples:**
   - Luxury watches: Males 35-54, income top 20%
   - Budget fashion: Females 18-34, all income levels
   - Senior services: Age 65+, income 50%+
   - Gaming products: 18-34, all genders, middle income

   If unclear, leave demographics empty for broad reach.

3. **Generate complete campaign structure with ALL details:**

**Required Fields (all mandatory):**
1. **campaign_name** - Unique descriptive name
2. **business_description** - What the business sells
3. **website_url** - Landing page URL
4. **budget_daily** - Daily budget in the account's native currency (do NOT convert — pass user's amount as-is)
5. **target_locations** - Geographic targets (cities/states/countries)
6. **ad_groups** - Array of 2-4 ad groups, each containing:
   - name: Ad group theme (e.g., "Premium Care Services")
   - keywords: 15-20 keywords from Keyword Planner research (will use BROAD match - Google's 2025 recommendation)
   - headlines: Exactly 15 headlines (MAXIMUM 30 chars each - NO EXCEPTIONS)
   - descriptions: Exactly 4 descriptions (MAXIMUM 80 chars each - NO EXCEPTIONS)
   - final_url: Landing page for this ad group
   - sitelinks (optional): 2-4 additional links below ad
   - audiences (optional): Demographics and audience targeting
     - demographics: {age_ranges: [...], genders: [...], income_ranges: [...]}
     - custom_audiences: [...], in_market_audiences: [...], affinity_audiences: [...]
7. **negative_keywords** (optional) - Terms to exclude

**🚨 CRITICAL CHARACTER LIMITS - COUNT BEFORE CALLING 🚨**
- **Headlines:** MAXIMUM 30 characters (NO EXCEPTIONS - will be rejected!)
- **Descriptions:** MAXIMUM 80 characters (NO EXCEPTIONS - will be rejected!)
- **Long Headlines (PMAX):** MAXIMUM 90 characters (NO EXCEPTIONS - will be rejected!)
- Generate ALL content BEFORE calling this tool
- COUNT the characters in each headline and description
- If ANY exceed limits, you MUST shorten them BEFORE calling
- Do NOT rely on retry - fix it the first time!
- ✅ Commas ARE ALLOWED and encouraged for natural language
- ❌ Do NOT use pipes (|) as separators - they will appear literally in ads
- ❌ Do NOT send comma-delimited strings - use proper JSON arrays
- Example: ["Expert Care, 24/7 Support", "Premium Service Available"]
- Do NOT call this tool multiple times - it creates REAL campaigns
- If errors occur, show them to the user - do NOT retry automatically
- Each call costs money and creates actual Google Ads campaigns

**SITELINK RULES (if using):**
⚠️ Google will REJECT sitelinks that violate these rules:
- ALL sitelink URLs MUST be same domain as final_url
  ✅ Good: final_url='https://example.com' → sitelink='https://example.com/shipping'
  ❌ Bad: final_url='https://example.com' → sitelink='https://different-site.com'
- Each sitelink must link to a UNIQUE, WORKING page (no duplicates, no 404s)
- Link text must be DESCRIPTIVE (not "Click Here", "Learn More")
- If you add description1, you MUST also add description2
- Only add sitelinks if you've verified the URLs exist and work

**Execution Time:** 15-30 seconds

**What happens:**
- Campaign created immediately in Google Ads
- Real money will be spent on the campaign
- Returns campaign_id for tracking

**Use for:**
- Launching new advertising campaigns
- Testing new market segments
- Scaling successful products

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "AdGroupInput": {
      "properties": {
        "name": {
          "description": "Ad group name (e.g., 'Premium Watches', 'Luxury Timepieces')",
          "title": "Name",
          "type": "string"
        },
        "keywords": {
          "description": "Keywords for this ad group (10-20 keywords recommended, minimum 5). Should come from Google Keyword Planner research.\n\nTwo accepted shapes — mix and match within the same list:\n  1. Plain string — defaults to BROAD match. Example: \"running shoes\"\n  2. Object — {\"text\": \"running shoes\", \"match_type\": \"BROAD|PHRASE|EXACT\"}\n\nExample mixed list: [\n  \"running shoes\",                                # BROAD (default)\n  {\"text\": \"running shoes\", \"match_type\": \"PHRASE\"},  # PHRASE\n  {\"text\": \"running shoes\", \"match_type\": \"EXACT\"}    # EXACT\n]\n\nNote: a strategy that wants PHRASE+EXACT variants of the same root keyword no longer needs a follow-up `add_keywords` call — pass them directly here.",
          "items": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
          },
          "minItems": 5,
          "title": "Keywords",
          "type": "array"
        },
        "headlines": {
          "description": "EXACTLY 15 headlines required (max 30 chars each). Google Ads requires 15 headlines for Responsive Search Ads. Commas ARE allowed within headlines. Example: [\"Premium Watches, Since 1950\", \"Luxury Timepieces\", ...]. MUST BE JSON ARRAY - do NOT send comma-delimited strings.",
          "items": {
            "type": "string"
          },
          "maxItems": 15,
          "minItems": 15,
          "title": "Headlines",
          "type": "array"
        },
        "descriptions": {
          "description": "EXACTLY 4 descriptions required (max 80 chars each - STRICT LIMIT). Google Ads requires 4 descriptions for Responsive Search Ads. ANY description over 80 chars will be REJECTED. Commas ARE allowed within descriptions. Example: [\"Discover handcrafted timepieces for collectors.\"] (50 chars). MUST BE JSON ARRAY. COUNT CHARACTERS BEFORE CALLING!",
          "items": {
            "type": "string"
          },
          "maxItems": 4,
          "minItems": 4,
          "title": "Descriptions",
          "type": "array"
        },
        "final_url": {
          "description": "Landing page URL for this ad group — where users go after clicking. **REQUIRED — ask the user for their website URL or specific landing page before calling this tool. Do NOT guess.** Must be HTTPS and reachable. Usually the same as the campaign's final_url, or a deeper page on the same domain.",
          "title": "Final Url",
          "type": "string"
        },
        "sitelinks": {
          "anyOf": [
            {
              "items": {
                "$ref": "#/$defs/SitelinkExtension"
              },
              "maxItems": 4,
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Optional: 2-4 sitelink extensions (additional links below ad). IMPORTANT: All sitelink URLs MUST be same domain as final_url. Example: [{'link_text': 'Free Shipping', 'final_url': 'https://example.com/shipping', 'description1': 'Fast delivery', 'description2': 'Order by 5pm'}]",
          "title": "Sitelinks"
        },
        "audiences": {
          "anyOf": [
            {
              "$ref": "#/$defs/AudienceTargeting"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Optional: Audience targeting to reach specific user segments. Leave empty for broad reach. Use if you have specific audience IDs from Google Ads."
        },
        "additional_ads": {
          "anyOf": [
            {
              "items": {
                "$ref": "#/$defs/ExtraRsaInput"
              },
              "maxItems": 2,
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Optional: 1-2 ADDITIONAL Responsive Search Ads in this ad group (beyond the primary RSA built from this group's headlines/descriptions). Google allows up to 3 RSAs/group and they must be DISTINCT. Each entry needs its own headlines/descriptions (a different angle). Omit for the standard 1 ad/group.",
          "title": "Additional Ads"
        }
      },
      "required": [
        "name",
        "keywords",
        "headlines",
        "descriptions",
        "final_url"
      ],
      "title": "AdGroupInput",
      "type": "object"
    },
    "AudienceTargeting": {
      "description": "Audience targeting for ad groups - reach specific user segments",
      "properties": {
        "demographics": {
          "anyOf": [
            {
              "$ref": "#/$defs/DemographicTargeting"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Optional: Target specific demographics (age, gender, income). Analyze the business to determine ideal customer profile. Leave empty for broad demographic reach."
        },
        "custom_audiences": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Custom audience IDs from your Google Ads account. Leave empty if you don't have pre-created custom audiences.",
          "title": "Custom Audiences"
        },
        "in_market_audiences": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "In-market audience IDs. Users actively researching/comparing products. Leave empty to skip audience targeting.",
          "title": "In Market Audiences"
        },
        "affinity_audiences": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Affinity audience IDs. Users with demonstrated interest in related topics. Leave empty to skip audience targeting.",
          "title": "Affinity Audiences"
        }
      },
      "title": "AudienceTargeting",
      "type": "object"
    },
    "DemographicTargeting": {
      "description": "Demographic targeting - target specific age groups, genders, and income levels",
      "properties": {
        "age_ranges": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Target specific age groups. Options: 'AGE_RANGE_18_24', 'AGE_RANGE_25_34', 'AGE_RANGE_35_44', 'AGE_RANGE_45_54', 'AGE_RANGE_55_64', 'AGE_RANGE_65_UP'. Leave empty to target all ages. Example: ['AGE_RANGE_25_34', 'AGE_RANGE_35_44'] for 25-44 year olds.",
          "title": "Age Ranges"
        },
        "genders": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Target specific genders. Options: 'MALE', 'FEMALE'. Leave empty to target all genders. Example: ['MALE'] for male-only targeting.",
          "title": "Genders"
        },
        "income_ranges": {
          "anyOf": [
            {
              "items": {
                "type": "string"
              },
              "type": "array"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Target household income levels. Options: 'INCOME_RANGE_0_50' (Lower 50%), 'INCOME_RANGE_50_60' (50-60%), 'INCOME_RANGE_60_70' (60-70%), 'INCOME_RANGE_70_80' (70-80%), 'INCOME_RANGE_80_90' (80-90%), 'INCOME_RANGE_TOP_10' (Top 10%). Leave empty to target all income levels. Example: ['INCOME_RANGE_TOP_10', 'INCOME_RANGE_80_90'] for top 20% earners.",
          "title": "Income Ranges"
        }
      },
      "title": "DemographicTargeting",
      "type": "object"
    },
    "ExtraRsaInput": {
      "description": "One ADDITIONAL Responsive Search Ad in an ad group (beyond the group's primary RSA).\n\nGoogle Ads allows up to 3 RSAs per ad group, and they must be DISTINCT (identical\nRSAs are rejected). Give each extra ad its own headlines/descriptions — a different\nangle/message — so the ad group can test multiple creatives.",
      "properties": {
        "headlines": {
          "description": "3-15 headlines for THIS extra ad (max 30 chars each). Must differ from the ad group's other ads. MUST BE JSON ARRAY.",
          "items": {
            "type": "string"
          },
          "maxItems": 15,
          "minItems": 3,
          "title": "Headlines",
          "type": "array"
        },
        "descriptions": {
          "description": "2-4 descriptions for THIS extra ad (max 90 chars each). MUST BE JSON ARRAY.",
          "items": {
            "type": "string"
          },
          "maxItems": 4,
          "minItems": 2,
          "title": "Descriptions",
          "type": "array"
        },
        "final_url": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Optional landing page for this ad; defaults to the ad group's final_url. Must be HTTPS and same domain.",
          "title": "Final Url"
        }
      },
      "required": [
        "headlines",
        "descriptions"
      ],
      "title": "ExtraRsaInput",
      "type": "object"
    },
    "SitelinkExtension": {
      "description": "Sitelink extension - additional links that appear below your ad\n\nCRITICAL SITELINK RULES:\n- URL MUST be same domain as main ad (e.g., if ad goes to example.com, sitelinks must go to example.com/*)\n- Link text must be DESCRIPTIVE and RELEVANT to the page it links to\n- Each sitelink must go to a UNIQUE URL (no duplicates)\n- URLs must be HTTPS and WORKING pages (Google will reject broken links)\n- Don't use generic terms like \"Click Here\" - be specific\n- Common violations: wrong domain, broken links, duplicate URLs, misleading text",
      "properties": {
        "link_text": {
          "description": "Link text displayed (max 25 chars). MUST be descriptive and match the page content. Good: 'Free Shipping Info', 'Pricing Plans', 'Contact Support'. Bad: 'Click Here', 'Learn More', 'Website'",
          "maxLength": 25,
          "title": "Link Text",
          "type": "string"
        },
        "final_url": {
          "description": "HTTPS URL for this sitelink. MUST be same domain as main ad URL. Must be a working page (Google validates). Each sitelink needs UNIQUE URL. Example: If ad goes to 'https://example.com', sitelink could be 'https://example.com/shipping'",
          "title": "Final Url",
          "type": "string"
        },
        "description1": {
          "anyOf": [
            {
              "maxLength": 35,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "First description line (max 35 chars, optional). Adds context to the link. Example: 'Fast nationwide delivery'",
          "title": "Description1"
        },
        "description2": {
          "anyOf": [
            {
              "maxLength": 35,
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Second description line (max 35 chars, required if description1 provided). Example: 'Orders ship within 24 hours'",
          "title": "Description2"
        }
      },
      "required": [
        "link_text",
        "final_url"
      ],
      "title": "SitelinkExtension",
      "type": "object"
    }
  },
  "properties": {
    "campaign_name": {
      "description": "Campaign name (e.g., 'Luxury Watches Q4 2025')",
      "title": "Campaign Name",
      "type": "string"
    },
    "business_description": {
      "description": "REQUIRED. What the business sells/does, in one sentence — used to generate ad copy and keyword themes. Example: 'Luxury watch retailer specializing in pre-owned Rolex and Omega'. If the user hasn't told you, ask them or infer it from the website before calling.",
      "title": "Business Description",
      "type": "string"
    },
    "website_url": {
      "description": "REQUIRED. The landing-page URL ads send clicks to. Example: 'https://example.com' or 'https://example.com/watches'. Use the user's site; if unknown, ask — do not omit this field.",
      "title": "Website Url",
      "type": "string"
    },
    "budget_daily": {
      "description": "REQUIRED. Daily budget in the account's native currency. Example: 50 for $50/day, or 1000 if the user says '₹1000/day'. Do NOT convert currencies — pass the user's amount as-is; the Google Ads API interprets it in the account's currency. Google recommends ~$10/day USD min for Search. If the user hasn't given a budget, ask for one — do not guess or omit.",
      "minimum": 1.0,
      "title": "Budget Daily",
      "type": "number"
    },
    "target_locations": {
      "description": "REQUIRED. Geographic targets as a JSON array of strings — countries, states, cities, or regions. Examples: ['India'], ['Mumbai, India'], ['New York, NY'], ['United States', 'Canada']. Always provide at least one; if the user didn't specify, ask where they want ads shown.",
      "items": {
        "type": "string"
      },
      "title": "Target Locations",
      "type": "array"
    },
    "ad_groups": {
      "description": "REQUIRED. One or more themed ad groups (2-5 is typical; more is allowed for a fuller structure), each with keywords, headlines, and descriptions. Each ad group is one theme/audience segment, and can carry up to 3 distinct RSAs via `additional_ads`. Example: [{'name': 'Rolex Watches', 'keywords': ['rolex for sale', 'buy rolex'], 'headlines': ['Authentic Pre-Owned Rolex', 'Certified Rolex Watches'], 'descriptions': ['Shop certified pre-owned Rolex with warranty.']}]. Run research_keywords first if you need keyword ideas.",
      "items": {
        "$ref": "#/$defs/AdGroupInput"
      },
      "minItems": 1,
      "title": "Ad Groups",
      "type": "array"
    },
    "negative_keywords": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign-level negative keywords (optional, e.g., ['free', 'cheap', 'used'])",
      "title": "Negative Keywords"
    },
    "bidding_strategy": {
      "default": "MAXIMIZE_CONVERSIONS",
      "description": "Bidding strategy for the campaign. Options: 'MAXIMIZE_CONVERSIONS' (default) - Get the most conversions within budget. 'MAXIMIZE_CONVERSION_VALUE' - Optimize for highest value conversions (requires target_roas). Recommended: MAXIMIZE_CONVERSIONS for new campaigns.",
      "title": "Bidding Strategy",
      "type": "string"
    },
    "objective": {
      "default": "CONVERSIONS",
      "description": "Campaign objective/goal. Options: 'CONVERSIONS' (default) - Track and optimize for sales, leads, or sign-ups. 'CLICKS' - Maximize website traffic. Recommended: CONVERSIONS for performance-focused campaigns.",
      "title": "Objective",
      "type": "string"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target ROAS (Return on Ad Spend) for MAXIMIZE_CONVERSION_VALUE bidding. Example: 3.0 means you want $3 revenue for every $1 spent. Only required when bidding_strategy='MAXIMIZE_CONVERSION_VALUE'.",
      "title": "Target Roas"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID (10 digits, no dashes). REQUIRED whenever the user has more than one Google Ads account connected — this creates a REAL campaign that spends REAL money, so it must land in the account the user actually meant. Do NOT omit it and do NOT guess: carry over the customer_id already in use in this conversation, or call list_connected_accounts / get_connections_status and ask the user which account. If a call fails asking you to disambiguate, RETRY with this parameter — that error does NOT mean the account is disconnected.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_name",
    "business_description",
    "website_url",
    "budget_daily",
    "target_locations",
    "ad_groups"
  ],
  "title": "SearchCampaignInput",
  "type": "object"
}
```

</details>

<a id="create_shopping_campaign"></a>

## `create_shopping_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Create a full Standard Shopping campaign advertising the products in a linked Merchant Center feed.

⚠️ Creates a REAL campaign (starts PAUSED — resume_campaign when ready). Call ONCE; do NOT auto-retry.

PREREQUISITE: a Merchant Center account must be linked. Check get_merchant_center_links; if none, link
one with link_merchant_center first. Pass that MC id as `merchant_id`.

WHAT THIS BUILDS: budget + SHOPPING campaign (bound to the MC feed) + one or MORE ad groups, each with
one or more product ads. Supports the full bidding + settings surface. The campaign serves ALL products
in the feed until you subdivide with `add_product_group` (the listing-group tree).

MULTIPLE AD GROUPS: pass `ad_groups: [{name, cpc_bid_micros, num_product_ads}, ...]` to build several at
once (e.g. one ad group per product category). Omit it to create a single ad group from ad_group_name/cpc_bid_micros.

**Required:** campaign_name, budget_daily, merchant_id.
**Bidding:** bidding_strategy (MANUAL_CPC default | TARGET_SPEND=MaxClicks | TARGET_ROAS | MAXIMIZE_CONVERSION_VALUE
| MAXIMIZE_CONVERSIONS | TARGET_CPA) + target_roas / target_cpa_micros / cpc_bid_ceiling_micros / cpc_bid_floor_micros
/ enhanced_cpc as applicable.
**Settings:** campaign_priority (0-2), enable_local, disable_product_feed, network_settings, feed_label (omit
unless the MC account uses feed labels — a wrong value serves zero products), start_date/end_date (YYYYMMDD).

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "ShoppingAdGroupSpec": {
      "description": "One ad group in a Shopping campaign create.",
      "properties": {
        "name": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Ad group name. Auto-named if omitted.",
          "title": "Name"
        },
        "cpc_bid_micros": {
          "anyOf": [
            {
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "This ad group's default max CPC in micros (1,000,000 = 1 currency unit).",
          "title": "Cpc Bid Micros"
        },
        "num_product_ads": {
          "anyOf": [
            {
              "maximum": 5,
              "minimum": 1,
              "type": "integer"
            },
            {
              "type": "null"
            }
          ],
          "default": 1,
          "description": "How many product ads to create in this ad group (default 1). Product ads are markers — products come from the Merchant Center feed; more than 1 is rarely needed.",
          "title": "Num Product Ads"
        }
      },
      "title": "ShoppingAdGroupSpec",
      "type": "object"
    },
    "ShoppingNetworkSettings": {
      "description": "Which networks a Shopping campaign serves on.",
      "properties": {
        "target_google_search": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Serve on Google Search (default on).",
          "title": "Target Google Search"
        },
        "target_search_network": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Serve on Search Partners.",
          "title": "Target Search Network"
        },
        "target_content_network": {
          "anyOf": [
            {
              "type": "boolean"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Serve on Display network (rarely valid for Shopping).",
          "title": "Target Content Network"
        }
      },
      "title": "ShoppingNetworkSettings",
      "type": "object"
    }
  },
  "description": "Input schema for create_shopping_campaign (Standard Shopping, full structure).",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (e.g. 'Summer Catalog Shopping').",
      "title": "Campaign Name",
      "type": "string"
    },
    "budget_daily": {
      "description": "Daily budget in the account's native currency. Do NOT convert currencies — pass the user's amount as-is.",
      "minimum": 1.0,
      "title": "Budget Daily",
      "type": "number"
    },
    "merchant_id": {
      "description": "The linked Merchant Center account ID whose product feed this campaign advertises. Get it from get_merchant_center_links (link one first with link_merchant_center if none).",
      "title": "Merchant Id",
      "type": "string"
    },
    "feed_label": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Merchant Center feed label for the products to advertise. MUST match a feed label that exists in the linked Merchant Center account, or the campaign will serve ZERO products. Leave unset (omit) to target products that have no feed label — the common single-feed case. Do NOT guess a country code; confirm the account's actual feed label first.",
      "title": "Feed Label"
    },
    "bidding_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "MANUAL_CPC",
      "description": "MANUAL_CPC (default, classic Shopping) | TARGET_SPEND (Maximize Clicks) | TARGET_ROAS | MAXIMIZE_CONVERSION_VALUE | MAXIMIZE_CONVERSIONS | TARGET_CPA.",
      "title": "Bidding Strategy"
    },
    "target_roas": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target ROAS (e.g. 4.0 = 400%). REQUIRED if bidding_strategy=TARGET_ROAS; optional booster for MAXIMIZE_CONVERSION_VALUE.",
      "title": "Target Roas"
    },
    "target_cpa_micros": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target CPA in micros. REQUIRED if bidding_strategy=TARGET_CPA; optional for MAXIMIZE_CONVERSIONS.",
      "title": "Target Cpa Micros"
    },
    "cpc_bid_ceiling_micros": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Max CPC bid limit (micros) for automated strategies (Target ROAS/CPA/Max Clicks).",
      "title": "Cpc Bid Ceiling Micros"
    },
    "cpc_bid_floor_micros": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Min CPC bid limit (micros) for Target ROAS/CPA/Max-Conv-Value.",
      "title": "Cpc Bid Floor Micros"
    },
    "enhanced_cpc": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Enable Enhanced CPC for MANUAL_CPC bidding.",
      "title": "Enhanced Cpc"
    },
    "campaign_priority": {
      "anyOf": [
        {
          "maximum": 2,
          "minimum": 0,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 0,
      "description": "Standard Shopping priority 0 (low, default) / 1 / 2 (high) — which campaign wins for a product when several overlap. Leave 0 unless you run multiple Shopping campaigns.",
      "title": "Campaign Priority"
    },
    "enable_local": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Include local-inventory (in-store) products from the Merchant Center feed. Default false.",
      "title": "Enable Local"
    },
    "disable_product_feed": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Disable the product feed (feedless Shopping). Advanced; leave unset normally.",
      "title": "Disable Product Feed"
    },
    "network_settings": {
      "anyOf": [
        {
          "$ref": "#/$defs/ShoppingNetworkSettings"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Which networks to serve on. Omit for Google's Shopping defaults."
    },
    "ad_groups": {
      "anyOf": [
        {
          "items": {
            "$ref": "#/$defs/ShoppingAdGroupSpec"
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Multiple ad groups to create, each with its own name/cpc_bid/num_product_ads. Omit to create a single default ad group (use ad_group_name/cpc_bid_micros below).",
      "title": "Ad Groups"
    },
    "ad_group_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Name for the single initial ad group (when ad_groups is not used).",
      "title": "Ad Group Name"
    },
    "cpc_bid_micros": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Default max CPC (micros) for the single initial ad group (when ad_groups is not used).",
      "title": "Cpc Bid Micros"
    },
    "num_product_ads": {
      "anyOf": [
        {
          "maximum": 5,
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 1,
      "description": "Number of product ads in the single initial ad group (when ad_groups is not used).",
      "title": "Num Product Ads"
    },
    "start_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date YYYYMMDD (optional).",
      "title": "Start Date"
    },
    "end_date": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date YYYYMMDD (optional).",
      "title": "End Date"
    },
    "customer_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads customer ID (10 digits, no dashes). REQUIRED whenever the user has more than one Google Ads account connected — this creates a REAL campaign that spends REAL money, so it must land in the account the user actually meant. Do NOT omit it and do NOT guess: carry over the customer_id already in use in this conversation, or call list_connected_accounts / get_connections_status and ask the user which account. If a call fails asking you to disambiguate, RETRY with this parameter — that error does NOT mean the account is disconnected.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_name",
    "budget_daily",
    "merchant_id"
  ],
  "title": "CreateShoppingCampaignInput",
  "type": "object"
}
```

</details>

