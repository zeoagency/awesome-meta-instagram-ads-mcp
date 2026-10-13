# amekala/ads-mcp — tools 106–140

[All tools](amekala--ads-mcp.md) · [Tool index](../tool-index.md)

<a id="get_display_keywords"></a>

## `get_display_keywords`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List contextual display keywords on a Display campaign's ad groups.

Display keywords are always BROAD-match (Google ignores match_type on Display).

**Execution time:** 1-3 seconds (read-only).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read-only input: targeting listed at the campaign level.",
  "properties": {
    "campaign_id": {
      "description": "Display campaign ID.",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "DisplayCampaignScopedInput",
  "type": "object"
}
```

</details>

<a id="get_display_placements"></a>

## `get_display_placements`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List all managed placements (websites, mobile apps, YouTube channels, YouTube videos) on a Display campaign's ad groups.

**Returns** list of placements with ad_group_id, criterion_id, type, value, status.

Use `criterion_id` + ad_group_id to construct a resource name for `remove_display_criteria`:
`customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}`

**Execution time:** 1-3 seconds (read-only).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read-only input: targeting listed at the campaign level.",
  "properties": {
    "campaign_id": {
      "description": "Display campaign ID.",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "DisplayCampaignScopedInput",
  "type": "object"
}
```

</details>

<a id="get_display_topics"></a>

## `get_display_topics`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List topic targeting on a Display campaign's ad groups.

Topics are Google's content categories (e.g., Finance, Travel, Technology). See Google's topic taxonomy at
https://developers.google.com/google-ads/api/data/codes-formats#verticals

**Execution time:** 1-3 seconds (read-only).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read-only input: targeting listed at the campaign level.",
  "properties": {
    "campaign_id": {
      "description": "Display campaign ID.",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "DisplayCampaignScopedInput",
  "type": "object"
}
```

</details>

<a id="get_merchant_center_links"></a>

## `get_merchant_center_links`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List the Merchant Center accounts linked to this Google Ads account.

A Merchant Center link is required before you can create a Shopping campaign. Returns
each link's merchant_center_id and product_link_id. An empty list means no Merchant
Center account is linked yet — use link_merchant_center to add one.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "List Merchant Center accounts linked to this Google Ads account.",
  "properties": {
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
  "title": "GetMerchantCenterLinksInput",
  "type": "object"
}
```

</details>

<a id="get_meta_ad_creatives"></a>

## `get_meta_ad_creatives`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see their Meta ad creatives, ad copy, media URLs, or creative performance.

Returns ad-level data including full creative content and media URLs alongside performance metrics.

When to use this tool:
- "Show me my Meta ad creatives"
- "What ads are running and how are they performing?"
- "Show me the headlines and images for my ads"
- "Which ad creatives are performing best?"
- "What's the creative content for campaign X?"
- "Show me ad performance with creative details"
- "Get me the image URLs for my ads"
- "Export my ad copy"
- "What images and videos are my ads using?"

Returns per ad — ALWAYS display ALL of these fields when present:
- Ad copy: headline, primary_text, description, call_to_action_type
- Media URLs: image_url (direct CDN link to ad image), thumbnail_url, video_url (playable video source), video_id
- Landing page: landing_page_url
- Carousel cards: carousel_cards array with per-card image_url, headline, description, landing_page_url
- Performance: spend, impressions, clicks, CTR, CPC, reach, frequency
- Video engagement: 25%, 50%, 75%, 100% watched (for video ads)
- Creative metadata: creative_type (image/video/carousel/dynamic_creative), first_seen_date

IMPORTANT: Always show the full image_url, thumbnail_url, video_url, and landing_page_url values — these are direct CDN links users need to download/export their creative media. Do not summarize or omit URLs.

Parameters:
- lookback_days: Number of days to analyze (7, 14, 30, 60, 90). Default: 30
- campaign_id: Optional filter to specific campaign
- ad_set_id: Optional filter to specific ad set
- ad_account_id: Required for multi-account users. Get from list_connected_accounts
- start_date/end_date: Optional custom date range (overrides lookback_days)
- limit: Max ads per page (default 20, max 50). Use for pagination.
- offset: Number of ads to skip (default 0). Use with limit to page through results.

Pagination: Results are paginated. Response includes total_ads count and has_more flag. To get next page, increase offset by limit.

Execution time: 1-3 seconds
Data source: Cached database (collected daily)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta ad creatives with content and performance",
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
      "description": "Filter to specific campaign ID (optional)",
      "title": "Campaign Id"
    },
    "ad_set_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter to specific ad set ID (optional)",
      "title": "Ad Set Id"
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
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze (7, 14, 30, 60, or 90 days). Default is 30 days.",
      "title": "Lookback Days",
      "type": "integer"
    },
    "limit": {
      "default": 20,
      "description": "Maximum number of ads to return per page (default 20, max 50). Use with offset for pagination.",
      "title": "Limit",
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of ads to skip for pagination (default 0). Use with limit to page through results.",
      "title": "Offset",
      "type": "integer"
    }
  },
  "title": "MetaAdCreativesInput",
  "type": "object"
}
```

</details>

<a id="get_meta_adset_performance"></a>

## `get_meta_adset_performance`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants ad-set-level Meta performance — the middle layer between campaigns and individual ads. Use this when the user asks about ad set performance, has accounts with one campaign and many ad sets, or wants to compare audiences/budgets at the ad set level.

This tool fills the gap between `get_meta_campaign_performance` (campaign rollups) and `analyze_meta_ad_performance` (per-ad creatives).

Returns:
- Per-ad-set metrics: spend, impressions, CTR, frequency, conversions, CPA, ROAS, reach
- Top performing ad sets (ranked by ROAS when conversions exist, else CTR)
- Underperforming ad sets (high spend, zero conversions, or ROAS < 1)
- Frequency fatigue alerts (frequency ≥ 3.0)
- Recommendations for budget reallocation and creative refresh

When to use this tool:
- "How are my Meta ad sets performing?"
- "Which ad sets in this campaign are best?"
- "Compare ad set performance across audiences"
- "Find ad sets with high frequency"
- "Which ad sets should I scale or pause?"
- Any question about ad-set-level (ad group / audience-level) Meta performance

Parameters:
- lookback_days: 7, 14, 30 (default), 60, or 90 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently"), ask the user to specify exact dates before calling this tool.
- campaign_id: Optional - filter to a single campaign (recommended when one campaign has many ad sets)
- include_video_metrics: true (default) or false
- include_recommendations: true (default) or false
- limit: max ad sets to return (default 100, max 200)
- offset: pagination offset (default 0)
- ad_account_id: Required for multi-account users. Get from get_connections_status.

Execution time: 1-3 seconds (cached database query)
Data source: ad_group_daily_metrics table (Meta ad sets stored as ad groups)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta ad-set-level performance analysis (the middle layer between campaign and ad).",
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
      "description": "Filter to a single campaign ID (optional). Useful when one campaign contains many ad sets.",
      "title": "Campaign Id"
    },
    "include_video_metrics": {
      "default": true,
      "description": "Include video completion metrics (25%, 50%, 75%, 100% watched) per ad set. Default is true.",
      "title": "Include Video Metrics",
      "type": "boolean"
    },
    "include_recommendations": {
      "default": true,
      "description": "Include optimization recommendations. Default is true.",
      "title": "Include Recommendations",
      "type": "boolean"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of ad sets to return (default 100, max 200). Use with offset for pagination.",
      "title": "Limit",
      "type": "integer"
    },
    "offset": {
      "default": 0,
      "description": "Number of ad sets to skip for pagination (default 0). Use with limit to get next page.",
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
  "title": "MetaAdSetPerformanceInput",
  "type": "object"
}
```

</details>

<a id="get_meta_app_adsets"></a>

## `get_meta_app_adsets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants PER-AD-SET install cost for app-promotion (AEO) campaigns — drill into a campaign's ad sets to see which audiences/placements deliver the cheapest installs. Keywords: "CPI by ad set", "which ad set / audience has the cheapest installs", "ad set install cost".

Pass campaign_id (from get_meta_app_campaigns) to scope to one campaign. Each ad set shows installs, CPI, and a self-relative comparison to the account average.

Reads cached nightly metrics. When to use: "Which ad set in this campaign has the lowest CPI?", "Cost per install by audience".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for per-ad-set app-promotion installs + CPI.",
  "properties": {
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
      "description": "Scope to one campaign (from get_meta_app_campaigns). Omit for all ad sets.",
      "title": "Campaign Id"
    },
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze (default 30, 1-365).",
      "title": "Lookback Days",
      "type": "integer"
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
      "description": "Start date YYYY-MM-DD.",
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
      "description": "End date YYYY-MM-DD.",
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
  "title": "GetMetaAppAdsetsInput",
  "type": "object"
}
```

</details>

<a id="get_meta_app_campaigns"></a>

## `get_meta_app_campaigns`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants PER-CAMPAIGN install cost for their app-promotion (AEO) campaigns. Keywords: "CPI by campaign", "which campaign has the cheapest/most expensive installs", "per-campaign cost per install", "compare install cost across app campaigns".

Lists each app campaign's installs and CPI, with a self-relative comparison to the account average CPI (e.g. "+105% vs account" = pricier installs). Honest CPI severity is applied to the top spenders; the rest show install/CPI facts. Run get_meta_app_summary first for the account headline, then this to find the cheap and expensive campaigns.

Reads cached nightly metrics. When to use: "Which app campaign has the lowest CPI?", "Break down cost per install by campaign".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for per-campaign app-promotion installs + CPI.",
  "properties": {
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze (default 30, 1-365).",
      "title": "Lookback Days",
      "type": "integer"
    },
    "grade_top_n": {
      "default": 20,
      "description": "Apply honest CPI severity to the top-N campaigns by spend (default 20); the rest show install/CPI facts only.",
      "title": "Grade Top N",
      "type": "integer"
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
      "description": "Start date YYYY-MM-DD.",
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
      "description": "End date YYYY-MM-DD.",
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
  "title": "GetMetaAppCampaignsInput",
  "type": "object"
}
```

</details>

<a id="get_meta_app_creatives"></a>

## `get_meta_app_creatives`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants PER-CREATIVE (per-ad) install cost for app-promotion (AEO) campaigns — which creatives/videos drive the cheapest installs. Keywords: "CPI by creative/ad", "best/worst creative for installs", "which ad has the cheapest installs", "creative install cost".

Ranks creatives cheapest-install-first. Pass campaign_id or ad_group_id (from the campaigns/ad-sets tools) to scope.

Reads cached nightly metrics. When to use: "Which creative has the lowest CPI?", "Best-performing ad for installs".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for per-creative (ad) app-promotion installs + CPI.",
  "properties": {
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
      "description": "Scope to one campaign (from get_meta_app_campaigns).",
      "title": "Campaign Id"
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
      "description": "Scope to one ad set (from get_meta_app_adsets).",
      "title": "Ad Group Id"
    },
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze (default 30, 1-365).",
      "title": "Lookback Days",
      "type": "integer"
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
      "description": "Start date YYYY-MM-DD.",
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
      "description": "End date YYYY-MM-DD.",
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
  "title": "GetMetaAppCreativesInput",
  "type": "object"
}
```

</details>

<a id="get_meta_app_summary"></a>

## `get_meta_app_summary`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants their mobile-APP-promotion (AEO / App Installs / OUTCOME_APP_PROMOTION) performance — INSTALLS and COST PER INSTALL (CPI). Keywords: "CPI", "cost per install", "how many installs", "app installs", "install cost", "AEO performance", "mobile game/app campaign performance", "UA performance", "cost per registration/purchase in-app".

The account headline for app campaigns: total installs, CPI (cost per install) graded against the account's OWN goal or 90-day average (never an invented benchmark — abstains honestly if there's no goal/history), and the in-app-event FUNNEL cost ladder (install → activate → registration → add-to-wishlist → checkout → level → purchase) with the cost per event. This is the fast entry point — then drill into per-campaign / ad-set / creative install cost.

Reads cached nightly metrics (never calls Meta live). When to use: "What's my CPI?", "How are my app install campaigns doing?", "Cost per install this month?", "Show my install funnel / cost per in-app event".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for the app-promotion (AEO) account summary: installs, CPI, funnel.",
  "properties": {
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze (default 30, 1-365).",
      "title": "Lookback Days",
      "type": "integer"
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
  "title": "GetMetaAppSummaryInput",
  "type": "object"
}
```

</details>

<a id="get_meta_audience_insights"></a>

## `get_meta_audience_insights`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks about audience demographics, which placements perform best, device breakdown, or targeting optimization for Meta ads.

This tool provides audience and placement analysis for Meta campaigns.

Returns:
- Age group performance (18-24, 25-34, 35-44, 45-54, 55-64, 65+)
- Gender performance breakdown
- Placement breakdown (Facebook Feed, Instagram Feed, Stories, Reels, Messenger)
- Device breakdown (Mobile, Desktop, Tablet)
- Best performing audience segments
- Targeting recommendations

When to use this tool:
- "What age group performs best for my Meta ads?"
- "Should I target men or women?"
- "Which placements should I use?"
- "Do my Instagram Stories ads perform well?"
- "Mobile vs desktop performance on Facebook?"

Parameters:
- lookback_days: 7, 14, 30 (default), 60, or 90 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- breakdown_type: 'age', 'gender', 'placement', 'device', or 'all' (default)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 1-3 seconds (cached database query)
Data source: Cached database (aggregate metrics only - detailed breakdown requires live API)

Common insights:
- Meta audiences typically skew mobile (70-85%)
- Instagram tends to perform better with 18-34 age groups
- Facebook Feed often has highest reach but Stories may have better engagement
- Reels placement growing rapidly in 2024-2025

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta audience and placement insights",
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
      "description": "Type of breakdown: 'age', 'gender', 'placement', 'device', or 'all' (default). Use 'all' for comprehensive audience analysis.",
      "title": "Breakdown Type",
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
  "title": "MetaAudienceInsightsInput",
  "type": "object"
}
```

</details>

<a id="get_meta_campaign_details"></a>

## `get_meta_campaign_details`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see detailed information about a specific Meta campaign, including its full structure (ad sets, ads, targeting, budgets).

This tool retrieves comprehensive details about a single campaign. With `include_hierarchy=true`, it shows the complete campaign tree: Campaign - Ad Sets - Ads.

Returns:
- Campaign settings (name, status, objective, budget, bid strategy, schedule)
- Performance summary (impressions, clicks, spend, reach, CTR, CPC)
- Ads Manager URL
- When include_hierarchy=true: Full structure with all ad sets and their ads, targeting details, hierarchy stats

When to use this tool:
- "Show me details for campaign [ID]"
- "What's the structure of my campaign?"
- "How many ad sets and ads does this campaign have?"
- "What targeting is set on my campaign?"
- "Show me the full campaign hierarchy"
- After `list_meta_campaigns` when user wants to drill into a specific campaign

Parameters:
- campaign_id: The Meta Campaign ID (required)
- include_hierarchy: Include ad sets and ads (default: false, set true for full view)

Execution time: 3-10 seconds (longer with hierarchy due to multiple API calls)
Data source: Meta Marketing API (live)

Workflow:
1. Use `list_meta_campaigns` to find campaign IDs
2. Use `get_meta_campaign_details` with `include_hierarchy=true` to see everything
3. Use `update_meta_ad_set` or `update_meta_ad` to make changes to specific items

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting detailed campaign information",
  "properties": {
    "campaign_id": {
      "description": "The Meta Campaign ID to get details for (required)",
      "title": "Campaign Id",
      "type": "string"
    },
    "include_hierarchy": {
      "default": false,
      "description": "Include full hierarchy with ad sets and ads (default: false). Set to true to see the complete campaign structure.",
      "title": "Include Hierarchy",
      "type": "boolean"
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
      "description": "Start of the performance window (YYYY-MM-DD). Use with end_date to report on a specific flight. When no window is given, established campaigns default to the last 7 days and brand-new campaigns default to their run so far (creation date through today).",
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
      "description": "End of the performance window (YYYY-MM-DD). Use with start_date.",
      "title": "End Date"
    },
    "date_preset": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Preset performance window instead of start_date/end_date: 'last_7d', 'last_14d', 'last_30d', 'last_90d', 'maximum' (lifetime-to-date). When omitted, established campaigns default to last 7 days and campaigns created in the last 7 days default to their run so far (so today's delivery is visible).",
      "title": "Date Preset"
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
    "campaign_id"
  ],
  "title": "GetMetaCampaignDetailsInput",
  "type": "object"
}
```

</details>

<a id="get_meta_campaign_performance"></a>

## `get_meta_campaign_performance`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks about Meta/Facebook/Instagram ad performance, campaign metrics, ROAS, spend analysis, or wants to understand how their Meta ads are performing.

This tool retrieves comprehensive campaign performance metrics from Meta Ads.

Returns:
- Account summary (total spend, impressions, reach, conversions, ROAS)
- Campaign breakdown with status and objectives
- Top performing campaigns by ROAS
- Meta-specific metrics (reach, frequency, reach/impressions ratio)
- Optimization recommendations

When to use this tool:
- "How are my Meta ads performing?"
- "What's my Facebook campaign ROAS?"
- "Show me Instagram ad performance"
- "Which Meta campaigns are doing best?"
- "Analyze my Meta ad spend"

Parameters:
- lookback_days: 7, 14, 30 (default), 60, or 90 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- include_recommendations: true (default) or false
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 1-3 seconds (cached database query)
Data source: campaign_daily_metrics table (updated nightly)

Note: Unlike Google Ads, Meta does not have keyword or search term data. Meta uses interest-based targeting.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta campaign performance analysis",
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
    "include_recommendations": {
      "default": true,
      "description": "Include optimization recommendations. Default is true.",
      "title": "Include Recommendations",
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
  "title": "MetaCampaignPerformanceInput",
  "type": "object"
}
```

</details>

<a id="get_meta_lead_form_submissions"></a>

## `get_meta_lead_form_submissions`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see lead submissions, lead data, or leads collected from a Meta lead form.

Retrieves individual lead submissions for a specific lead form, including contact details and associated ad/campaign information.

When to use this tool:
- "Show me the leads from form X"
- "Get my lead form submissions"
- "Download my Meta leads"
- "Show lead data from my campaign"
- "How many leads did I get?"

Returns per lead:
- Submission timestamp
- Field data (name, email, phone, etc. — varies by form)
- Source: organic or paid (with campaign name and ad name)
- Lead ID

Parameters:
- form_id: Lead form ID (required — get from list_meta_lead_forms)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts
- limit: Maximum leads to return (default: 100)

Permission: Requires 'leads_retrieval' scope. If the user gets a permission error, they need to disconnect and reconnect their Meta account to grant the updated permissions.

Execution time: 2-5 seconds
Data source: Meta Marketing API (live)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for retrieving lead form submissions.",
  "properties": {
    "form_id": {
      "description": "Lead form ID (required). Get available form IDs from list_meta_lead_forms tool.",
      "title": "Form Id",
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
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of lead submissions to return (default: 100)",
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "form_id"
  ],
  "title": "MetaLeadFormSubmissionsInput",
  "type": "object"
}
```

</details>

<a id="get_meta_pixel_stats"></a>

## `get_meta_pixel_stats`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to set up RETARGETING catalog ads, or check whether a pixel is firing product events.

Returns pixel health (last fired time, availability) and recent event breakdown. Use to confirm ViewContent / AddToCart / Purchase are firing before building a retargeting catalog campaign; if they aren't, recommend prospecting instead.

When to use:
- Before a retargeting catalog ad
- "Is my pixel working?", "what events is my pixel getting?"

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for checking pixel health and which events are firing.",
  "properties": {
    "pixel_id": {
      "description": "Meta Pixel ID (required). Get it from list_meta_pixels.",
      "title": "Pixel Id",
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
      "description": "Meta ad account ID. If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "pixel_id"
  ],
  "title": "GetMetaPixelStatsInput",
  "type": "object"
}
```

</details>

<a id="get_meta_product_performance"></a>

## `get_meta_product_performance`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to drill into ONE specific catalog product's performance over time — its daily spend/ROAS trend and full funnel (views → carts → checkouts → purchases). Get the product_id from analyze_meta_catalog_performance first.

When to use: "How is product X doing?", "Show me the trend for this SKU", "What's the funnel for this product?"

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for drilling into a single catalog product's daily trend + funnel.",
  "properties": {
    "product_id": {
      "description": "The Meta product ID to drill into (from analyze_meta_catalog_performance).",
      "title": "Product Id",
      "type": "string"
    },
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze (default 30).",
      "title": "Lookback Days",
      "type": "integer"
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
      "description": "Start date YYYY-MM-DD.",
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
      "description": "End date YYYY-MM-DD.",
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
  "required": [
    "product_id"
  ],
  "title": "GetMetaProductPerformanceInput",
  "type": "object"
}
```

</details>

<a id="get_negative_keyword_list"></a>

## `get_negative_keyword_list`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Show the keywords inside one shared negative keyword list.

⚠️ READ-ONLY. Safe to call repeatedly.

Lists the negative keywords (text + match type) in a specific shared list. Paged
and filterable (`query`, `sort_by`, `offset`/`limit`) for large lists.

**Parameters:** shared_set_id (required — from list_negative_keyword_lists).
**Use when:** "what's in my negative keyword list?", "show the keywords in list X".

<details>
<summary>Full input schema</summary>

```json
{
  "description": "View the keywords inside one shared negative keyword list (paged).",
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
      "description": "Free-text filter on the keyword text.",
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
      "description": "Sort field: text (default) or match_type.",
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
      "default": "asc",
      "description": "'asc' (default) or 'desc'.",
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
      "description": "Row offset for paging (0-based). Default 0.",
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
      "description": "Rows per page (1-200). Default 100.",
      "title": "Limit"
    }
  },
  "required": [
    "shared_set_id"
  ],
  "title": "GetNegativeKeywordListInput",
  "type": "object"
}
```

</details>

<a id="get_placement_performance"></a>

## `get_placement_performance`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Per-PLACEMENT performance WITH conversions — where your ads actually ran (websites, YouTube channels/videos, apps) and what each placement cost and produced.

This tool retrieves READ-ONLY data via 1 live GAQL query (cached 5 min in Redis). Safe to call multiple times.

**Why this tool:** `get_display_placements` shows only the placements you manually targeted (config, no metrics). `get_campaign_performance` stops at ad-group granularity. This is the ONLY tool that shows WHERE Display / Demand Gen / Video / Smart ads actually delivered — including automatic placements Google chose — with cost AND conversions per placement. It's the data behind the Google Ads UI "Where ads showed" / Content → Placements report.

**Returns one row per placement** (or per domain/channel when group_view=true):
- Identity: `placement_type` (WEBSITE / YOUTUBE_CHANNEL / YOUTUBE_VIDEO / MOBILE_APPLICATION / …), `display_name`, `target_url` (the site / channel / app), `campaign_name`, `ad_group_name` (detail view)
- Metrics for the date range: `impressions`, `clicks`, `ctr`, `cost`, `conversions`, `conversion_value`, `all_conversions`, `cpc`, `cpa`, `roas`
- `totals` block + `pagination` (page / total_pages / has_more)

**These reports are huge** (a Demand Gen account can have 150,000+ placements). Filter SERVER-SIDE so you don't pull everything:
- `min_cost` — only placements that spent at least this much (account currency)
- `min_impressions` — only placements above an impression floor
- `zero_conversions_only` — only placements with ZERO conversions (spent money, no conversions). Pair with `min_cost` to find wasted spend to exclude.
- `placement_type` — restrict to WEBSITE / YOUTUBE_CHANNEL / etc.
- `order_by` — cost | conversions | impressions | clicks
- `group_view=true` — roll up per domain/channel for fewer rows

**Pagination:** results are paged. Check `pagination.has_more` in the response — if true, call again with `page` incremented (page=2, page=3, …) to get the next set of placements. Continue until has_more is false.

**Coverage:** Display, Demand Gen, Video, Smart campaigns (any campaign that runs on the Display/YouTube network). Search campaigns have no placement rows.

**These numbers are the account's own measured data — this tool renders NO verdicts, invents no "good/bad" thresholds, and applies no baseline.** It shows the placements and their metrics so you (and the user) can decide. `zero_conversions_only` is a factual filter, not a judgement.

**Parameters:**
- customer_id: Optional (uses connected account if omitted)
- lookback_days: 7, 30, 60, 90, 120 (default 30). Ignored when both start_date and end_date set.
- start_date / end_date: YYYY-MM-DD (override lookback_days when both provided)
- campaign_id: Optional — scope to one campaign
- placement_type / group_view / min_cost / min_impressions / zero_conversions_only / order_by: filters above
- page / page_size: pagination (page_size default 50, max 200)

**Execution time:** 1-4 seconds (1 GAQL query, then cached 5 min)

**Use this tool when:**
- User asks "where did my ads show?", "which websites / YouTube channels / apps converted?", "where is Display/Demand Gen wasting money?"
- User wants to find placements with spend but no conversions to exclude them
- User wants per-placement cost / conversions / CPA to optimize Display or Demand Gen

**Tip:** Find waste with `zero_conversions_only=true` + `min_cost`, then exclude it with `add_placement_exclusions`.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for get_placement_performance tool (placement-level perf + conversions).",
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
      "description": "Number of days to analyze (7, 30, 60, 90, 120). Default 30. Ignored when both start_date and end_date are provided.",
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
      "description": "Optional. Scope to a single campaign (from list_campaigns). Omit for account-wide placement breakdown.",
      "title": "Campaign Id"
    },
    "placement_type": {
      "default": "ALL",
      "description": "Filter by placement type: ALL | WEBSITE | MOBILE_APPLICATION | MOBILE_APP_CATEGORY | YOUTUBE_VIDEO | YOUTUBE_CHANNEL | GOOGLE_PRODUCTS. Default ALL.",
      "title": "Placement Type",
      "type": "string"
    },
    "group_view": {
      "default": false,
      "description": "False (default) = one row per exact placement (detail_placement_view). True = rolled up per domain / channel (group_placement_view) for fewer rows.",
      "title": "Group View",
      "type": "boolean"
    },
    "min_cost": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Only return placements that spent at least this much (in the account's currency). Use to hide low-spend noise (these reports can have 150k+ rows).",
      "title": "Min Cost"
    },
    "min_impressions": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Only return placements with at least this many impressions. Defaults to >0 (placements that actually served) when omitted.",
      "title": "Min Impressions"
    },
    "zero_conversions_only": {
      "default": false,
      "description": "True = only placements with ZERO conversions in the window (spent money, produced no conversions). Pair with min_cost to find wasted spend to exclude.",
      "title": "Zero Conversions Only",
      "type": "boolean"
    },
    "order_by": {
      "default": "cost",
      "description": "Sort placements by: cost | conversions | impressions | clicks (descending). Default cost.",
      "title": "Order By",
      "type": "string"
    },
    "page": {
      "default": 1,
      "description": "Page number (1-based). The response's pagination.has_more tells you whether to call again with page+1 for the next set of placements.",
      "title": "Page",
      "type": "integer"
    },
    "page_size": {
      "default": 50,
      "description": "Placements per page (default 50, max 200).",
      "title": "Page Size",
      "type": "integer"
    }
  },
  "title": "PlacementPerformanceInput",
  "type": "object"
}
```

</details>

<a id="get_pmax_asset_groups"></a>

## `get_pmax_asset_groups`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List all asset groups on a Performance Max campaign.

Shows per group: ID, name, status, **ad_strength** (Google's creative rating),
**primary_status + reasons** (why a group is/isn't serving), final URLs and
display paths. This is the read-back tool for the other asset-group tools.

**Use when:**
- "Why isn't my PMax campaign serving?" → check primary_status_reasons
- "How strong are my asset groups?" → ad_strength per group
- Getting asset_group_id for update/remove/add-image calls

**Parameters:**
- campaign_id: The PMax campaign ID (REQUIRED — get from list_campaigns)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 1-3 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing asset groups on a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
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
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "GetPMaxAssetGroupsInput",
  "type": "object"
}
```

</details>

<a id="get_pmax_asset_performance"></a>

## `get_pmax_asset_performance`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read Google's own per-asset performance_label for every image in a PMax campaign, plus asset-group-level rollup metrics.

PMax does not expose per-image CTR / conversions on Google's side — Google
instead publishes its own ML grade per asset: BEST / GOOD / LOW / LEARNING /
PENDING. This tool surfaces that label directly, and adds a derived
`recommended_action`:

- LOW → REPLACE
- LEARNING / PENDING → WAIT
- GOOD / BEST → KEEP
- UNKNOWN / UNSPECIFIED → REVIEW

Per-group metrics (impressions, clicks, conversions, cost_micros, CTR, CVR)
are rolled up for the requested date range. Labels themselves are not
date-scoped on Google's API; they reflect Google's current grade.

**Use when:**
- Identifying which assets to swap during a monthly creative refresh
- Sanity-checking that newly added assets have left LEARNING
- Reporting on PMax creative health per asset group

**Parameters:**
- campaign_id: The PMax campaign ID
- asset_group_id: optional — scope to one group
- date_range / start_date+end_date: window for the group-level metrics
- min_label_severity: optional filter (LOW / GOOD / BEST)

**Execution time:** 2-5 seconds (two GAQL queries)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for reading per-asset performance_label + per-group\nrollup metrics for a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "asset_group_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional — scope to one asset group.",
      "title": "Asset Group Id"
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
      "default": "LAST_90_DAYS",
      "description": "One of LAST_7_DAYS, LAST_14_DAYS, LAST_30_DAYS, LAST_90_DAYS. Ignored when both start_date and end_date are set.",
      "title": "Date Range"
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
      "description": "YYYY-MM-DD. Use together with end_date to override date_range.",
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
      "description": "YYYY-MM-DD. Use together with start_date to override date_range.",
      "title": "End Date"
    },
    "min_label_severity": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional filter. One of LOW, GOOD, BEST. LOW returns only LOW assets; GOOD returns LOW+GOOD; BEST returns LOW+GOOD+BEST. LEARNING/PENDING/UNKNOWN are excluded by this filter (they are returned only when no filter is set).",
      "title": "Min Label Severity"
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
    "campaign_id"
  ],
  "title": "GetPMaxAssetPerformanceInput",
  "type": "object"
}
```

</details>

<a id="get_pmax_audience_signals"></a>

## `get_pmax_audience_signals`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Get current audience signals for a Performance Max campaign.

Returns audience signal resource names and associated audience resource references.

**Use when:**
- User wants to see what audience signals are on their PMax campaign
- Before adding new signals
- To get resource_name for removal

**Parameters:**
- campaign_id: The PMax campaign ID

**Execution time:** 1-2 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting audience signals from a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Google Ads campaign ID (numeric). Example: '21854471508'",
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
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "GetPMaxAudienceSignalsInput",
  "type": "object"
}
```

</details>

<a id="get_pmax_conversion_goals"></a>

## `get_pmax_conversion_goals`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read a campaign's campaign-specific conversion goals (read-only).

Lists each conversion goal's category (e.g. PURCHASE, ADD_TO_CART), origin, and
whether it is **biddable** (i.e. the campaign optimizes toward it). Use this to
verify, for example, that a Performance Max campaign is set to purchase-only
bidding before launch — PURCHASE should be the only biddable goal.

**Parameters:**
- campaign_id: the campaign ID

**Execution time:** 1-3 seconds (single GAQL read). Read-only — changes nothing.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for reading a campaign's conversion goals (read-only).",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (numeric). Example: '24249158821'",
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
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "GetPMaxConversionGoalsInput",
  "type": "object"
}
```

</details>

<a id="get_pmax_search_themes"></a>

## `get_pmax_search_themes`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Get current search themes for a Performance Max campaign.

Returns each search theme's text and approval_status (APPROVED, LIMITED, DISAPPROVED, UNDER_REVIEW).

**Use when:**
- User wants to see what search themes are set on their PMax campaign
- Before adding new themes (to check current count — max 50)
- To verify theme approval status after adding

**Parameters:**
- campaign_id: The PMax campaign ID (get from list_campaigns)

**Execution time:** 1-2 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting search themes from a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Google Ads campaign ID (numeric). Example: '21854471508'",
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
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "GetPMaxSearchThemesInput",
  "type": "object"
}
```

</details>

<a id="get_product_groups"></a>

## `get_product_groups`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read a Shopping ad group's product-partition (listing-group) tree.

Shows how the ad group's products are subdivided for bidding. Returns each node: criterion_id,
parent_id, node_type (SUBDIVISION branch / UNIT leaf), the dimension it represents, its bid, and
whether it's excluded. An empty tree means the ad group serves ALL products at the ad-group bid.

**Required:** ad_group_id (a Shopping ad group).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read a Shopping ad group's product-partition (listing-group) tree.",
  "properties": {
    "ad_group_id": {
      "description": "The Shopping ad group ID (from get_campaign_structure).",
      "title": "Ad Group Id",
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
    "ad_group_id"
  ],
  "title": "GetProductGroupsInput",
  "type": "object"
}
```

</details>

<a id="get_reach_frequency"></a>

## `get_reach_frequency`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Reach & frequency — how many UNIQUE users your campaigns reached, and the average number of times each person saw your ads.

This tool retrieves READ-ONLY data via 1 live GAQL query (cached 5 min in Redis). Safe to call multiple times.

**Why this tool:** `get_campaign_performance` reports impressions but not unique reach. This is the only tool that returns `unique_users` (de-duplicated people reached) and `average_impression_frequency_per_user` (the "Avg. impr. freq. / user" column in the Google Ads UI) — the direct signal for creative-fatigue and rotation decisions on YouTube / Demand Gen / Video campaigns, instead of proxying frequency from CPM/CTR trends.

**Returns one row per campaign** (sorted by impressions):
- `campaign_id`, `campaign_name`, `campaign_type`, `status`
- `impressions`, `unique_users`, `avg_impression_frequency_per_user`

**Google constraints (surfaced honestly, not bugs):**
- Reach metrics are **campaign-level only** — Google REJECTS them at the ad-group level, so this tool cannot break reach down by ad group.
- Reach is populated for reach-eligible campaign types (Demand Gen, Video/YouTube, Performance Max, Display). Search campaigns typically report 0 unique users.
- Google reports unique reach only for a **trailing ~92-day window**; a longer window silently returns zeros, so the lookback is clamped to 92 days (the tool tells you when it clamped).
- `unique_users` is de-duplicated over the window and is **NOT summed across campaigns** (the same person can be reached by more than one campaign).

**These are the account's own measured numbers — the tool renders NO verdict and invents no "healthy frequency" threshold.** Whether a given frequency is too high depends on the campaign and goal; the tool reports the number and leaves the call to you.

**Parameters:**
- customer_id: Optional (uses connected account if omitted)
- lookback_days: 7, 30, 60, 90 (clamped to ≤92). Ignored when both start_date and end_date set.
- start_date / end_date: YYYY-MM-DD (override lookback_days when both provided; clamped to last 92 days)
- campaign_id: Optional — scope to one campaign

**Execution time:** 1-3 seconds (1 GAQL query, then cached 5 min)

**Use this tool when:**
- User asks "what's my reach / frequency?", "how many unique users did I reach?", "how often is each person seeing my ad?"
- User is deciding whether to rotate/refresh creative on a YouTube or Demand Gen campaign (frequency is the fatigue signal)
- User wants unique reach instead of raw impressions

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for get_reach_frequency tool (unique users + avg frequency).",
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
      "description": "Number of days to analyze (7, 30, 60, 90). Clamped to Google's ~92-day reach limit. Default 30. Ignored when both start_date and end_date are provided.",
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
      "description": "Optional. Scope to a single campaign (from list_campaigns). Omit for all campaigns with reach data.",
      "title": "Campaign Id"
    }
  },
  "title": "ReachFrequencyInput",
  "type": "object"
}
```

</details>

<a id="get_shopping_settings"></a>

## `get_shopping_settings`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read a Shopping campaign's Merchant Center settings.

Returns the shopping_setting that binds the campaign to Merchant Center: merchant_id, feed_label,
campaign_priority (0-2), enable_local, disable_product_feed. Use get_campaign_structure for the ad
groups / ads / budget / bidding / network; this tool is specifically for the Merchant-Center binding.

**Required:** campaign_id (a Shopping campaign — from list_campaigns).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read a Shopping campaign's Merchant Center settings.",
  "properties": {
    "campaign_id": {
      "description": "The Shopping campaign ID (from list_campaigns).",
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
      "description": "Google Ads customer ID. Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "GetShoppingSettingsInput",
  "type": "object"
}
```

</details>

<a id="get_tool_schema"></a>

## `get_tool_schema`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Get the exact, authoritative signature (name, parameters, types, required fields, allowed values) for one or more tools by name. Call this after `search_tools` and BEFORE calling a tool, so you send correct arguments and never guess. The schema returned is the live tool definition — always current. This is a TOP-LEVEL tool like `search_tools`: call it DIRECTLY by name when it is in your tool list, e.g. get_tool_schema({"tool_names": ["pause_meta_campaign"]}). If your client does not list it, call it through any platform router instead (e.g. google_ads(action="execute", tool_name="get_tool_schema", arguments={"tool_names": [...]})) — same result.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "tool_names": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        {
          "type": "string"
        }
      ],
      "description": "Exact tool name(s) to fetch the full signature (inputSchema) for — from search_tools results. Accepts a list, a single string, or the `tool_name` key.",
      "title": "Tool Names"
    },
    "tool_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Alias for tool_names — a single tool name is also accepted here.",
      "title": "Tool Name"
    }
  },
  "title": "GetToolSchemaInput",
  "type": "object"
}
```

</details>

<a id="get_usage_status"></a>

## `get_usage_status`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Get your current tool-call usage for the billing period.

**Returns:**
- Current usage (calls used / limit) — monthly limit or annual pool
- Subscription tier (Free, Plus, Pro, Enterprise) and billing period (monthly / annual)
- When the quota or annual pool resets
- For annual subscribers, the pooled yearly allowance and annual reset date

On hosts that support interactive widgets it renders a usage meter.

**Use this tool when:**
- User asks "how many calls do I have left?"
- User asks about their subscription or quota
- User wants to check their usage

READ-ONLY and safe to call anytime.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting usage status with quota widget",
  "properties": {},
  "title": "UsageStatusInput",
  "type": "object"
}
```

</details>

<a id="google_analytics"></a>

## `google_analytics`

Scope: **supporting** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read Google Analytics 4 reports and metadata for the user's connected GA4 properties.

**Use action="list_tools" first** to discover available actions and their parameters.
Then use action="execute" with the specific tool_name and arguments.

**When to use:**
- Website / app traffic, sessions, users, page views, bounce rate, engagement
- Conversions, conversion events, key events, goal completions
- Audience demographics, geography, device breakdown
- Traffic sources (organic, paid, referral, social, direct)
- Comparing ad spend (from `google_ads` / `meta_ads`) to actual site outcomes
- "How is my website performing?", "show GA4 conversions", "what's my bounce rate"

If the user hasn't connected Google Analytics, this tool returns a friendly
message asking them to open Settings → Connections to authorize the connection.

**Picking a property (do NOT guess):** a connected account often has many GA4
properties. If you call a report action without a `property` and more than one
exists, this tool returns the labelled list and asks which to use — relay it and
let the user pick one, a few, or all. Do NOT invent or assume a property id. If
they say "all", warn first that it means one report call per property (which uses
that many tool calls), then confirm before running them.

**Example — list actions:**
action: "list_tools"

**Example — run a GA4 report** (use `google_analytics-run-report-in-ga4` with
`property: "properties/<id>"`; get the id from `google_analytics-list-property-options`):
action: "execute"
tool_name: "google_analytics-run-report-in-ga4"
arguments: {"property": "properties/493035312", "startDate": "7daysAgo", "endDate": "today", "metrics": ["sessions", "totalUsers"]}


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "action": {
      "description": "'list_tools': discover available actions for this app. 'execute': run a specific action by name.",
      "title": "Action",
      "type": "string"
    },
    "tool_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Name of the action to execute (required when action='execute'). Get exact names from action='list_tools' first.",
      "title": "Tool Name"
    },
    "arguments": {
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
      "description": "Arguments object passed to the action (required when action='execute').",
      "title": "Arguments"
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
      "description": "Which connected account to use (the account id, e.g. apn_…). Only needed when you have MULTIPLE accounts connected for this app — the tool will tell you the ids to choose from. Omit if you have just one connected account.",
      "title": "Account Id"
    }
  },
  "required": [
    "action"
  ],
  "title": "_IntegrationsRouterInput",
  "type": "object"
}
```

</details>

<a id="google_search_console"></a>

## `google_search_console`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read organic-search performance for the user's verified sites, and submit URLs for re-indexing.

**Use action="list_tools" first** to discover available actions and their parameters.
Then use action="execute" with the specific tool_name and arguments.

**When to use:**
- Organic search performance — clicks, impressions, CTR, average position
- Which search queries bring traffic, and which pages rank for them
- Breakdowns by query, page, country, device, or date
- Comparing PAID search (`google_ads`) against ORGANIC search
- "What keywords am I ranking for?", "why did organic traffic drop?", "which pages lost impressions?"
- Asking Google to re-crawl a page after publishing or updating it

If the user hasn't connected Search Console, this tool returns a friendly message
asking them to open Settings → Connections to authorize the connection.

**Picking a site (do NOT guess):** a connected account may have several verified
sites. If you call a site action without a `siteUrl` and more than one exists,
this tool returns the labelled list of sites and asks which to use — relay it and
let the user pick. Get the list any time with `google_search_console-list-sites`.

**⚠️ Side effects & confirmation:** `google_search_console-submit-url-for-indexing` is a WRITE — it notifies Google that a URL was updated or deleted. Confirm the exact URL with the user before submitting. The performance action is read-only.

**Example — list actions:**
action: "list_tools"

**Example — top queries last 28 days:**
action: "execute"
tool_name: "google_search_console-retrieve-site-performance-data"
arguments: {"siteUrl": "https://example.com/", "startDate": "2026-07-16", "endDate": "2026-08-12", "dimensions": ["query"], "rowLimit": 25}


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "action": {
      "description": "'list_tools': discover available actions for this app. 'execute': run a specific action by name.",
      "title": "Action",
      "type": "string"
    },
    "tool_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Name of the action to execute (required when action='execute'). Get exact names from action='list_tools' first.",
      "title": "Tool Name"
    },
    "arguments": {
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
      "description": "Arguments object passed to the action (required when action='execute').",
      "title": "Arguments"
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
      "description": "Which connected account to use (the account id, e.g. apn_…). Only needed when you have MULTIPLE accounts connected for this app — the tool will tell you the ids to choose from. Omit if you have just one connected account.",
      "title": "Account Id"
    }
  },
  "required": [
    "action"
  ],
  "title": "_IntegrationsRouterInput",
  "type": "object"
}
```

</details>

<a id="google_tag_manager"></a>

## `google_tag_manager`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read and manage tags and variables in the user's Google Tag Manager containers.

**Use action="list_tools" first** to discover available actions and their parameters.
Then use action="execute" with the specific tool_name and arguments.

**When to use:**
- Which tags (conversion pixels, analytics, remarketing) are on their site
- Whether a specific pixel/tag exists and is configured correctly
- Diagnosing why a conversion pixel isn't firing — read the tag config
- Creating or updating a tag or a GTM variable
- "Is my Meta pixel installed?", "list my GTM tags", "why isn't my conversion tracking firing"

If the user hasn't connected Google Tag Manager, this tool returns a friendly message
asking them to open Settings → Connections to authorize the connection.

**Picking account → container → workspace (do NOT guess):** GTM is a hierarchy.
If you call an action without `accountId`, `containerId` or `workspaceId` and more
than one option exists at that level, this tool returns the labelled list for the
missing level and asks which to use — relay it and let the user pick, one level at
a time. Never assume an id, especially for a write: a tag written to the wrong
container silently breaks the customer's live tracking.

**⚠️ Side effects & confirmation:** create-tag, update-tag and update-variable WRITE to a live container that fires the customer's tracking on their real website — a wrong edit can silently break conversion tracking site-wide. Confirm the exact change before any write; prefer the read actions (get-tag, get-tags) for diagnostics.

**Example — list actions:**
action: "list_tools"

**Example — list tags in a container:**
action: "execute"
tool_name: "google_tag_manager-get-tags"
arguments: {"accountId": "6000000000", "containerId": "12345678", "workspaceId": "3"}


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "action": {
      "description": "'list_tools': discover available actions for this app. 'execute': run a specific action by name.",
      "title": "Action",
      "type": "string"
    },
    "tool_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Name of the action to execute (required when action='execute'). Get exact names from action='list_tools' first.",
      "title": "Tool Name"
    },
    "arguments": {
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
      "description": "Arguments object passed to the action (required when action='execute').",
      "title": "Arguments"
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
      "description": "Which connected account to use (the account id, e.g. apn_…). Only needed when you have MULTIPLE accounts connected for this app — the tool will tell you the ids to choose from. Omit if you have just one connected account.",
      "title": "Account Id"
    }
  },
  "required": [
    "action"
  ],
  "title": "_IntegrationsRouterInput",
  "type": "object"
}
```

</details>

<a id="help_user_upload"></a>

## `help_user_upload`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Show user instructions for uploading images to postimages.org for Performance Max campaigns.

⚠️ CALL THIS FIRST when user wants to create a PMax campaign!

**YOUR ROLE**: Image Upload Guide

**WHEN TO USE**:
- User says "create PMax campaign" or similar
- Before asking for image uploads
- Anytime user needs help uploading images

**WHAT THIS DOES**:
- Returns clear, step-by-step instructions
- Tells user to upload to postimages.org
- Explains how to get Direct links (not share pages)
- Shows example URL format

**DO NOT**:
- Ask user to upload via ChatGPT's paperclip (won't work with size limits!)
- Request base64 data (too large!)
- Skip this step (user needs clear guidance)

**AFTER THIS**:
- User uploads to postimages.org
- User pastes Direct links in chat
- You call validate_and_prepare_assets with those URLs

**Execution Time**: <1 second (just returns text)
**Authentication**: Not required

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for help_user_upload tool (no parameters needed).",
  "properties": {},
  "title": "HelpUserUploadInput",
  "type": "object"
}
```

</details>

<a id="infer_business_profile"></a>

## `infer_business_profile`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Automatically infer business profile from campaign data using AI analysis.

⚠️ IMPORTANT: This tool ANALYZES data but may SAVE a profile if confidence is high.

🎯 **What This Tool Does (Performance Agent - Phase 1 Feature 5):**
- Analyzes campaign names, keywords, and ad copy
- Uses Claude AI to classify business type
- Infers business vertical, size, goals, and audience
- Returns confidence level (high, medium, low)
- Auto-saves if confidence is HIGH, asks confirmation for LOW

**Inference Process:**
1. Collects campaign names and keywords from Google Ads
2. Analyzes patterns (B2B vs B2C, product vs service)
3. Uses AI to classify business vertical
4. Estimates business size from ad spend
5. Identifies primary goals from campaign types

**Confidence Levels:**
- **HIGH** (≥0.8): Auto-saves profile, high certainty
- **MEDIUM** (0.5-0.8): Saves profile, reasonable certainty
- **LOW** (<0.5): Returns suggestion, asks user to confirm

**Parameters:**
- **force_save**: Set to true to save even low-confidence profiles
- **customer_id**: Optional (uses connected account if omitted)

**Returns:**
- Inferred business profile (vertical, size, goal, audience)
- Confidence level and reasoning
- Whether profile was saved or needs confirmation
- Suggested confirmation prompt for low-confidence results

**Use this tool when:**
- User doesn't have a business profile set
- User asks "analyze my business"
- You need business context but none exists
- After user connects a new Google Ads account

**Example Flow:**
1. Call `get_business_profile` - returns no profile
2. Call `infer_business_profile` - analyzes campaigns
3. If HIGH confidence: Profile saved automatically
4. If LOW confidence: Ask user to confirm with suggested prompt

**Execution time:** 3-8 seconds (AI analysis + optional save)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for inferring business profile from campaign data",
  "properties": {
    "force_save": {
      "default": false,
      "description": "If true, save the profile even if confidence is low. Default is false (requires user confirmation for low-confidence profiles).",
      "title": "Force Save",
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
    }
  },
  "title": "BusinessProfileInferInput",
  "type": "object"
}
```

</details>

<a id="klaviyo"></a>

## `klaviyo`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read and act on the user's Klaviyo (email + SMS marketing) account.

**Use action="list_tools" first** to discover available actions and their parameters.
Then use action="execute" with the specific tool_name and arguments.

**When to use:**
- Klaviyo lists, segments, profiles, subscribers
- Email campaign performance (opens, clicks, conversions, revenue)
- Flows (welcome series, abandoned cart, post-purchase)
- Adding profiles or events, triggering flows
- "Show my Klaviyo campaign stats", "add a contact to list X", "what flows do I have"

If the user hasn't connected Klaviyo, this tool returns a friendly message
asking them to open Settings → Connections to authorize the connection.

**⚠️ Side effects & confirmation:** Write operations change a live Klaviyo account — adding profiles or events writes contact PII, and triggering a flow can send real email/SMS to subscribers. These take effect immediately; confirm before writing.

**Example — list actions:**
action: "list_tools"

**Example — add a profile:**
action: "execute"
tool_name: "klaviyo-add-profile-to-list"
arguments: {"listId": "abc123", "email": "jane@example.com"}


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "action": {
      "description": "'list_tools': discover available actions for this app. 'execute': run a specific action by name.",
      "title": "Action",
      "type": "string"
    },
    "tool_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Name of the action to execute (required when action='execute'). Get exact names from action='list_tools' first.",
      "title": "Tool Name"
    },
    "arguments": {
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
      "description": "Arguments object passed to the action (required when action='execute').",
      "title": "Arguments"
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
      "description": "Which connected account to use (the account id, e.g. apn_…). Only needed when you have MULTIPLE accounts connected for this app — the tool will tell you the ids to choose from. Omit if you have just one connected account.",
      "title": "Account Id"
    }
  },
  "required": [
    "action"
  ],
  "title": "_IntegrationsRouterInput",
  "type": "object"
}
```

</details>

<a id="link_merchant_center"></a>

## `link_merchant_center`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Link a Merchant Center account to this Google Ads account.

This is the prerequisite for Shopping campaigns — the product feed lives in Merchant
Center, and the link lets Google Ads serve those products. If the same Google login
administers both accounts the link is created directly; otherwise Google creates a
pending invitation that must be accepted on the Merchant Center side.

**Required:** merchant_center_id (the numeric ID shown in Merchant Center).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Link a Merchant Center account to this Google Ads account (required before creating Shopping campaigns).",
  "properties": {
    "merchant_center_id": {
      "description": "The Merchant Center account ID to link (the numeric ID shown in Merchant Center).",
      "title": "Merchant Center Id",
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
    "merchant_center_id"
  ],
  "title": "LinkMerchantCenterInput",
  "type": "object"
}
```

</details>

