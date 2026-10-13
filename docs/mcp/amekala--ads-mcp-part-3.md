# amekala/ads-mcp — tools 71–105

[All tools](amekala--ads-mcp.md) · [Tool index](../tool-index.md)

<a id="create_youtube_campaign"></a>

## `create_youtube_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

🔄 LONG-RUNNING TOOL: Creates a YouTube Video campaign using Google Ads Demand Gen format with YouTube-only placements. Emits MCP progress updates during authentication and campaign creation (typically 10-20 seconds). Progress stages: validate → commit.

⚠️ CRITICAL WARNING ⚠️
- Call this tool ONLY ONCE per campaign
- Creates REAL campaigns that cost REAL money
- Do NOT retry automatically if errors occur
- Report errors to user instead of retrying

⚠️ CRITICAL PREREQUISITE:
- MUST validate the YouTube video first using validate_video tool
- Video must be public or unlisted on YouTube (NOT private)

🎬 **YouTube Campaign Placements:**
✅ YouTube In-Feed (appears in search results & related videos)
✅ YouTube In-Stream (plays before/during/after videos)
✅ YouTube Shorts (appears in Shorts feed)
❌ Gmail (disabled for YouTube campaigns)
❌ Discover (disabled for YouTube campaigns)
❌ Display (disabled for YouTube campaigns)

📋 **YOUR CRITICAL ROLE: Campaign Strategist & Text Creator**

**STEP 1: Validate Video First**

Before calling this tool:
1. Get user's YouTube video URL or ID
2. Call validate_video tool with platform="pmax" to verify it
3. Confirm video is accessible (public or unlisted)

🔴 **STEP 1.5: MANDATORY — Discover Existing Assets**
BEFORE proceeding, you MUST call discover_existing_assets to check for existing image/logo assets:
1. Call: discover_existing_assets(asset_types=["image", "logo"], target_domain="<user's domain>")
2. Present findings to the user:
   - Show all available logos and images with dimensions
   - Show count of assets found per type
3. Ask the user:
   "I found [N] existing assets in your account. Would you like to:
   A) Reuse an existing logo (saves time, consistent branding)
   B) Upload a new logo image
   C) Upload a new logo from URL"
4. Based on answer:
   - Reuse → Use logo_asset_id from discovered assets
   - Upload new → Use validate_and_prepare_assets with logos_square → asset_bundle_id
5. 🚫 NEVER skip this step — even if the user didn't mention assets

**STEP 2: Collect Campaign Details from User**

YOU MUST collect these from the user (ask if not provided):

**REQUIRED Fields:**
1. **Campaign Name** - Descriptive and unique
2. **Daily Budget** - Minimum $15/day (recommended $50+)
3. **YouTube Video ID** - 11-character video ID (validated in Step 1)
4. **Final URL** - Landing page (must match verified domain)
5. **Business Name** - Max 25 characters

**STEP 3: Generate High-Quality Ad Copy**

**🚨 BEFORE GENERATING TEXT - READ CHARACTER LIMITS 🚨**

**Headlines (1-5 required):**
- **STRICT LIMIT: 40 characters maximum per headline**
- Count characters BEFORE calling this tool!
- Examples:
  - "Shop Premium Watches Today" (26 chars) ✅
  - "Free Worldwide Shipping Now" (27 chars) ✅

**Descriptions (1-5 required):**
- **STRICT LIMIT: 90 characters maximum per description**
- Count characters BEFORE calling this tool!
- Examples:
  - "Shop authentic luxury timepieces with expert curation and free worldwide shipping." (82 chars) ✅

**Long Headlines (optional, 1-5):**
- **STRICT LIMIT: 90 characters maximum per long headline**
- Falls back to regular headlines if not provided

**⚠️ WILL BE REJECTED IF YOU EXCEED LIMITS - NO RETRIES!**

**LOGO (REQUIRED - one of two options):**
- **Option A** (existing logo): logo_asset_id from discover_existing_assets — use this if the account already has logo images
- **Option B** (new upload): asset_bundle_id from validate_and_prepare_assets — use this if the account has NO existing logos (e.g., Search-only accounts)

**Workflow:**
1. First try discover_existing_assets to find existing logos
2. If logos found → use logo_asset_id
3. If NO logos found → ask user for a logo image URL, run validate_and_prepare_assets with logos_square, then use the returned asset_bundle_id

**OPTIONAL Fields (use defaults if not provided):**
- call_to_action: Default "LEARN_MORE". Options: SHOP_NOW, SIGN_UP, SUBSCRIBE, DOWNLOAD, BOOK_NOW, CONTACT_US, GET_QUOTE, APPLY_NOW, WATCH_NOW, ORDER_NOW, BUY_NOW, SEE_MORE, START_NOW, VISIT_SITE, REGISTER
- target_locations: Defaults to ["United States"]
- target_languages: Defaults to ["en"]
- additional_video_ids: Up to 4 more videos (5 total max)
- bidding_strategy: MAXIMIZE_CLICKS (default), MAXIMIZE_CONVERSIONS (needs conversion tracking), TARGET_CPA
- target_cpa: Required only for TARGET_CPA bidding

**STEP 4: Call create_youtube_campaign**

After you have ALL details:
- Validate character counts yourself BEFORE calling
- Call create_youtube_campaign with complete payload
- Wait for response (may take 10-20 seconds)

**STEP 5: Handle Response**

**If SUCCESS:**
- Show campaign ID, name, budget, status
- Explain YouTube-only placements (In-Feed, In-Stream, Shorts)
- Explain campaign starts PAUSED for safety
- Provide next steps (review, activate, monitor)

**If FAILURE:**
- Show error message clearly
- Do NOT retry automatically
- Guide user to fix the issue

**Example Conversation Flow:**

User: "I want to run YouTube ads for my product"

You: "I'd be happy to help create a YouTube video campaign! First, can you share your YouTube video URL so I can validate it?"

[User provides: https://youtu.be/eIZtladpm6c]

[Call validate_video with video_url_or_id="eIZtladpm6c", platform="pmax"]

You: "Your video is validated and ready! Now I need a few details:
1. Campaign name?
2. Daily budget? (minimum $15, recommended $50+)
3. Landing page URL?
4. Business name?

I'll create compelling headlines and descriptions for your YouTube ads."

[User provides details]

[Call create_youtube_campaign with all details]

**Video Specifications:**
- Must be on YouTube (public or unlisted, NOT private)
- Minimum 10 seconds duration recommended
- Maximum 5 videos per campaign (1 primary + 4 additional)
- Validated via validate_video tool before campaign creation

**Bidding Options:**
- MAXIMIZE_CLICKS: Best for most campaigns (default, works without conversion tracking)
- MAXIMIZE_CONVERSIONS: Best when conversion tracking is set up on the account
- TARGET_CPA: Best when you know your target cost per acquisition (requires conversion tracking)

**Campaign Creation Best Practices:**
1. Always validate video first with validate_video tool
2. 🔴 MANDATORY: Run discover_existing_assets to find logos/images — present results to user, ask if they want to reuse or upload new
3. If reuse → use logo_asset_id; if upload new → validate_and_prepare_assets → asset_bundle_id
4. Confirm budget with user ($15/day minimum)
5. Create compelling, benefit-focused ad copy
6. Campaign starts PAUSED - explain this to user
7. This costs real money - be transparent
8. 🔴 AFTER campaign creation: Add extensions (sitelinks, callouts, structured snippets) — see STEP 6 below

**STEP 6: MANDATORY — Add Extensions After Creation**
After the campaign is successfully created, you MUST:
1. Crawl the user's website to gather relevant page links, features, and service categories
2. Add sitelinks: at least 4 links to key pages (add_sitelinks tool)
3. Add callout extensions: 4-6 business highlights (add_callout_extensions tool)
4. Add structured snippets: categorized features (add_structured_snippets tool)
5. Verify with list_campaign_extensions to confirm all extensions are attached
Extensions are FREE and increase ad visibility by 15-25%. NEVER skip this step.

**Execution Time:** 10-20 seconds (direct backend API call)

**Authentication:** Required (MCP OAuth 2.1)

**CRITICAL REMINDERS:**
- Campaign starts PAUSED for user safety
- This costs real money - be transparent with user
- Never retry on failure - report error to user
- Always validate video BEFORE creating campaign

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for create_youtube_campaign tool.\n\nCreates a YouTube Video campaign using Google Ads Demand Gen format\nwith YouTube-only channel controls (In-Feed, In-Stream, Shorts).\nGmail, Discover, and Display placements are disabled.",
  "properties": {
    "campaign_name": {
      "description": "Campaign name (e.g., 'YouTube Summer Promo 2025')",
      "title": "Campaign Name",
      "type": "string"
    },
    "budget_daily": {
      "description": "Daily budget in the account's native currency. IMPORTANT: Do NOT convert currencies — pass the user's amount as-is. Example: if user says '₹1000/day', pass 1000 (not a USD conversion). The Google Ads API interprets this in the account's currency automatically. Google recommends minimum ~$20/day USD equivalent for YouTube/Demand Gen campaigns.",
      "minimum": 1.0,
      "title": "Budget Daily",
      "type": "number"
    },
    "youtube_video_id": {
      "description": "Primary YouTube video ID (exactly 11 characters). Must be validated first using validate_video tool. Example: 'dQw4w9WgXcQ'",
      "title": "Youtube Video Id",
      "type": "string"
    },
    "final_url": {
      "description": "Landing page URL where users go after clicking the ad. **REQUIRED — ask the user for their website URL before calling this tool. Do NOT guess.** Must be HTTPS, reachable, and match the verified domain on the Google Ads account. Example: 'https://example.com/product'.",
      "title": "Final Url",
      "type": "string"
    },
    "business_name": {
      "description": "Business name, max 25 characters. Example: 'Luxury Watch Co'",
      "maxLength": 25,
      "title": "Business Name",
      "type": "string"
    },
    "headlines": {
      "description": "MUST BE JSON ARRAY: 1-5 headlines, each EXACTLY 40 characters maximum. Commas ARE allowed within headlines. Example: [\"Shop Premium Watches Today\", \"Free Shipping\"]. COUNT CHARACTERS! ANY over 40 will be REJECTED!",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Headlines",
      "type": "array"
    },
    "descriptions": {
      "description": "MUST BE JSON ARRAY: 1-5 descriptions, each EXACTLY 90 characters maximum. Commas ARE allowed within descriptions. Example: [\"Shop authentic luxury timepieces with expert curation and free shipping.\"]. COUNT CHARACTERS BEFORE CALLING - ANY over 90 will be REJECTED!",
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
      "description": "MUST BE JSON ARRAY: Optional 1-5 long headlines, each EXACTLY 90 characters maximum. Falls back to regular headlines if not provided. Example: [\"Premium Swiss Watches - Certified Authentic, Free Worldwide Shipping\"]. COUNT CHARACTERS! ANY over 90 will be REJECTED!",
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
      "default": "LEARN_MORE",
      "description": "Call-to-action button label. Options: LEARN_MORE (default), SHOP_NOW, SIGN_UP, SUBSCRIBE, DOWNLOAD, BOOK_NOW, CONTACT_US, GET_QUOTE, APPLY_NOW, WATCH_NOW, ORDER_NOW, BUY_NOW, SEE_MORE, START_NOW, VISIT_SITE, REGISTER",
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
      "description": "Optional: Language targets as ISO codes (e.g., ['en', 'es']). Defaults to English.",
      "title": "Target Languages"
    },
    "additional_video_ids": {
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
      "description": "Optional: Up to 4 additional YouTube video IDs (max 5 total including primary). Each must be exactly 11 characters. Example: ['abc123xyz00', 'def456uvw00']",
      "title": "Additional Video Ids"
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
      "description": "Bidding strategy: MAXIMIZE_CLICKS (default, works without conversion tracking), MAXIMIZE_CONVERSIONS (requires conversion tracking), or TARGET_CPA (requires target_cpa). TARGET_CPA requires target_cpa parameter.",
      "title": "Bidding Strategy"
    },
    "target_cpa": {
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
      "description": "Target CPA in USD (only required when bidding_strategy='TARGET_CPA'). Example: 25.0 means target $25 per conversion.",
      "title": "Target Cpa"
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
      "description": "Logo image asset ID (1:1 square aspect ratio) from discover_existing_assets. Either this OR asset_bundle_id is required. Example: '123456789'",
      "title": "Logo Asset Id"
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
      "description": "Asset bundle ID (UUID) from validate_and_prepare_assets. Use this when the account has no existing logo images. The bundle must contain a square logo (logos_square). Either this OR logo_asset_id is required. Example: '7df76fef-9d1f-4218-8bfb-3173f6de9622'",
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
    "youtube_video_id",
    "final_url",
    "business_name",
    "headlines",
    "descriptions"
  ],
  "title": "CreateYouTubeCampaignInput",
  "type": "object"
}
```

</details>

<a id="detect_meta_catalog_waste"></a>

## `detect_meta_catalog_waste`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to find and recover WASTED catalog spend at the PRODUCT level. Keywords: "which products waste money", "recover spend", "stop wasting budget", "SKUs that don't convert", "products below break-even".

Detects recoverable spend: SKUs spending with ZERO conversions + SKUs converting BELOW break-even (1.0x ROAS). Returns the account recoverable-spend total and a prioritized, severity-ranked SKU action list. Carries the same guards as the campaign-level wasted-spend tool: never "pause" a SKU that still converts (says reduce/tighten instead), respects minimum spend, and softens copy when conversion tracking looks incomplete.

Reads cached nightly product metrics (never calls Meta live). When to use: "Which products are wasting my budget?", "How much catalog spend can I recover?"

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for the product-level recoverable-spend (waste) detector.",
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
  "title": "DetectMetaCatalogWasteInput",
  "type": "object"
}
```

</details>

<a id="detect_meta_creative_fatigue"></a>

## `detect_meta_creative_fatigue`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks about creative fatigue, ad refresh timing, frequency management, declining CTR, when to replace ads, or audience exhaustion on Meta/Facebook/Instagram.

This tool analyzes all Meta Ads creatives for fatigue indicators using frequency-CTR correlation analysis and provides a fatigue score (0-100) for each ad.

Returns:
- Fatigue score (0-100) for each ad based on weighted factors
- Severely fatigued ads (score ≥80) - immediate action required
- At-risk ads (score 50-79) - plan refresh within 7-14 days
- Healthy ads count
- Daily spend being wasted on fatigued creatives
- Projected monthly waste
- Refresh schedule recommendations
- Contributing factors for each fatigued ad

When to use this tool:
- "Are any of my Meta/Facebook/Instagram ads fatigued?"
- "When should I refresh my creatives?"
- "Why is my CTR declining?"
- "Which ads have high frequency?"
- "How much am I wasting on fatigued ads?"
- "What's my ad refresh schedule?"
- "Are my retargeting ads showing too often?"

Parameters:
- lookback_days: 7, 14, 30 (default), 60, or 90 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- frequency_threshold_cold: 2.0-8.0 (default: 4.0) - threshold for cold traffic audiences
- frequency_threshold_retargeting: 4.0-10.0 (default: 7.0) - threshold for retargeting audiences
- ctr_decline_threshold: 0.10-0.50 (default: 0.20 = 20%) - CTR decline to flag as fatigued
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 2-5 seconds (cached database query with analysis)
Data source: meta_ad_creative_metrics table (ad-level daily metrics with frequency, CTR, video completion)

Fatigue Score Calculation:
The fatigue score (0-100) is calculated using weighted factors:
- Frequency (40%): impressions/reach ratio vs threshold
- CTR Decline (35%): % drop in CTR vs previous period
- Days Running (25%): creative age vs optimal refresh timing

Severity Levels:
- 🔴 Score ≥80: Severely fatigued - PAUSE immediately and replace
- 🟡 Score 50-79: At risk - prepare replacement within 7-14 days
- ✅ Score <50: Healthy - continue monitoring

Best practices:
- Cold traffic: Refresh creatives when frequency reaches 3-4x
- Retargeting: Can tolerate higher frequency (up to 6-7x)
- Create 3-5 variations per ad set for automatic rotation
- Monitor weekly for frequency and CTR trends

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta creative fatigue detection analysis",
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
    "frequency_threshold_cold": {
      "default": 4.0,
      "description": "Frequency threshold for cold traffic audiences (2.0-8.0). Default is 4.0 - ads showing to cold audiences more than 4x are considered fatigued.",
      "title": "Frequency Threshold Cold",
      "type": "number"
    },
    "frequency_threshold_retargeting": {
      "default": 7.0,
      "description": "Frequency threshold for retargeting audiences (4.0-10.0). Default is 7.0 - retargeting audiences can tolerate higher frequency.",
      "title": "Frequency Threshold Retargeting",
      "type": "number"
    },
    "ctr_decline_threshold": {
      "default": 0.2,
      "description": "CTR decline threshold to flag as fatigued (0.10-0.50 = 10%-50%). Default is 0.20 (20% decline).",
      "title": "Ctr Decline Threshold",
      "type": "number"
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
  "title": "MetaCreativeFatigueInput",
  "type": "object"
}
```

</details>

<a id="diagnose_funnel"></a>

## `diagnose_funnel`

Scope: **supporting** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

DIAGNOSE why a user's ads aren't producing sales/leads — the ordered root-cause check that tells them WHICH part of their funnel is broken and what to do about it.

**Call this when the user asks:**
- "why aren't my ads selling / working / converting?", "I'm not getting any sales", "my ads aren't performing", "what's wrong with my account?", "what would you do to increase sales?", "I'm losing money on ads"
- any open-ended "something is wrong and I don't know what" question

**How it differs from the performance tools:** those DESCRIBE the numbers for one platform. This walks the whole chain in ORDER — is conversion tracking real → should there even be revenue → is there traffic → is it converting → (we can't see the landing page) → where is the money going — and STOPS at the first broken step, reporting the rest as 'not assessed' rather than 'fine'. That ordering is the point: a broken pixel makes every number below it meaningless, and advice about bids or budgets would be guesswork until it's fixed.

**Inputs (all optional):** `platform` and `account_id` to narrow to one account; `lookback_days` (14-90, default 60). With no arguments it checks every connected account and leads with the worst one — call it bare.

⛔ It ABSTAINS honestly: if the account has too little data, or the numbers can't be verified, it says so and says what would unlock an answer, rather than guessing. It never invents benchmarks or promises outcomes.

If the funnel is healthy and the user wants budget advice, follow up with generate_media_plan. Renders an interactive widget; the text carries the same diagnosis.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "All optional — the question is already fully specified by the tool itself.",
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
      "title": "Account Id"
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
      "default": null,
      "title": "Lookback Days"
    }
  },
  "title": "DiagnoseFunnelInput",
  "type": "object"
}
```

</details>

<a id="diagnose_meta_catalog_funnel"></a>

## `diagnose_meta_catalog_funnel`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to know WHERE in the catalog shopping funnel they're losing shoppers. Keywords: "funnel", "drop-off", "people add to cart but don't buy", "abandoned carts", "why aren't products converting", "checkout drop".

Reports the catalog funnel (product view → add to cart → checkout → purchase) per product and account-wide, from cached nightly metrics. For each product and the account it computes the stage-to-stage drop-off RATES and states, as a MEASURED FACT, the stage with the largest drop (e.g. "82% of carts didn't reach checkout"). It does NOT label a drop "severe" or assert a diagnosed cause — it offers COMMON REASONS to check at that stage (creative/feed at view→cart; price/shipping at cart→checkout; payment/checkout friction or pixel firing at checkout→purchase) as guidance, not a verdict.

Reads cached nightly product metrics (never calls Meta live). When to use: "Where are shoppers dropping off in my catalog funnel?", "Why am I getting carts but fewer sales?"

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for the catalog funnel drop-off diagnostic.",
  "properties": {
    "lookback_days": {
      "default": 30,
      "description": "Days to analyze: 7, 30, 60, 90, or 120 (default 30).",
      "title": "Lookback Days",
      "type": "integer"
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
      "description": "Optional product set ID to scope the diagnostic to one set.",
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
  "title": "DiagnoseMetaCatalogFunnelInput",
  "type": "object"
}
```

</details>

<a id="discover_existing_assets"></a>

## `discover_existing_assets`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

🔍 Discover existing assets in the Google Ads account (images, sitelinks, callouts, structured snippets).

**Phase 0: Asset Discovery** - Read-only tool, safe to call anytime.

🔴 **MANDATORY WORKFLOW - ALWAYS DO THIS FIRST:**

BEFORE creating ANY Performance Max campaign, you MUST:
1. Call this tool: discover_existing_assets(target_domain="<user's domain>")
2. Show the user what was found (images, sitelinks)
3. Ask: "Would you like to reuse these assets or upload new ones?"
4. Based on answer:
   - Reuse → Use existing_image_ids in create_pmax_campaign
   - Upload new → Use validate_and_prepare_assets → asset_bundle_id
   - Mix both → Use both parameters (hybrid mode)

🚫 **NEVER create PMAX without discovering assets first** (unless user explicitly says "skip discovery, upload new")

**What This Tool Does:**
- Queries Google Ads Asset Library for existing validated assets
- Returns campaign-validated assets FIRST, then the rest of the asset library
- Includes downloadable image URLs (full-size, from Google's CDN)

📄 **Paginated:** results come in pages of 50 per asset type. The response
footer states whether more pages exist; if it does, call again with page=2
(then 3, …) until it reports all assets have been returned. The full inventory
is the pages combined, so page 1 alone is not the complete list.

**2-Tier Smart Discovery:**

**Tier 1: Campaign-Validated Assets (High Confidence)** ✅
- Assets currently attached to ENABLED, PAUSED, or REMOVED campaigns
- These have been validated by Google and won't fail
- Includes domain filtering for sitelinks
- Best option for reuse

**Tier 2: No Validated Assets (Ask User)** ⚠️
- Account has no suitable assets in campaigns
- Recommends uploading fresh assets or website research
- Safer than using orphaned assets from library

**Parameters:**
- target_domain: Optional domain to filter sitelinks (e.g., "rooterhero.com")
  - **CRITICAL for multi-domain accounts!** Google rejects wrong-domain sitelinks
  - **Extract the base domain** from campaign URL (just the domain part)
  - Examples: "https://www.rooterhero.com/services" → "rooterhero.com", "sahaayak.life" → "sahaayak.life"
  - Only sitelinks matching this domain will be returned
  - Prevents Google API errors for domain mismatches

**Returns:**
- images: List of validated images (landscape, square, portrait, logos)
- sitelinks: List of validated sitelinks (filtered by domain if provided)
- callouts: List of validated callouts
- structured_snippets: List of validated structured snippets
- recommendation: Smart guidance on whether to reuse or upload new

**Example ChatGPT Flow:**

User: "Create a campaign for rooterhero.com" (or "https://www.rooterhero.com/services")

Step 1: Extract base domain → "rooterhero.com"
Step 2: Call discover_existing_assets(target_domain="rooterhero.com")

If Tier 1 (validated assets found):
  ChatGPT: "I found 8 sitelinks and 11 images from your previous Rooter Hero campaigns.
            These were validated by Google. Would you like to reuse them, or upload fresh assets?"

  User: "Reuse them" → Use those assets in Phase 1
  User: "Upload new" → Follow current upload flow

If Tier 2 (no validated assets):
  ChatGPT: "No validated assets found for rooterhero.com in your campaigns.
            Options:
            1. Upload fresh images/sitelinks
            2. Let me research rooterhero.com and suggest sitelinks
            3. Create campaign without extensions"

**When to Call:**
- BEFORE creating Search campaigns (to discover sitelinks, callouts, snippets)
- BEFORE creating PMAX campaigns (to discover images)
- When user asks "What assets do I have?"
- When user wants to reuse existing assets

**When NOT to Call:**
- User explicitly says "I'll upload new images"
- User wants to create minimal campaign without extensions

**Execution Time:** 1-3 seconds (read-only query)

**Authentication:** Required (MCP OAuth 2.1)

**Note:** This is Phase 0 - discovery only. Phase 1 will enable reusing discovered assets in campaigns.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "target_domain": {
      "type": "string",
      "description": "Optional domain to filter sitelinks. **Extract the base domain from the campaign URL.** Examples: 'https://www.rooterhero.com/services' → 'rooterhero.com', 'sahaayak.life' → 'sahaayak.life'. Only sitelinks matching this domain will be returned. Critical: Google rejects wrong-domain sitelinks."
    },
    "asset_types": {
      "type": "array",
      "description": "Asset types to discover. Default: all types.",
      "items": {
        "type": "string",
        "enum": [
          "images",
          "sitelinks",
          "callouts",
          "structured_snippets"
        ]
      },
      "default": [
        "images",
        "sitelinks",
        "callouts",
        "structured_snippets"
      ]
    },
    "customer_id": {
      "type": "string",
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status."
    },
    "page": {
      "type": "integer",
      "description": "Page number (1-based, 50 assets per type per page). The response tells you if more pages exist — KEEP CALLING with page=2, 3, ... until it says ALL assets have been returned. Accumulate results across pages; do NOT assume page 1 is everything.",
      "default": 1,
      "minimum": 1
    }
  }
}
```

</details>

<a id="discover_meta_assets"></a>

## `discover_meta_assets`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to browse existing images and videos in their Meta Ad Library for reuse in new campaigns.

This tool retrieves existing images and videos that have been uploaded to Meta's Ad Library, allowing users to reuse them in new campaigns without uploading again.

Returns:
- List of existing images with their hashes (dimensions, created timestamps)
- List of existing videos with their IDs (title, duration, created timestamps)
- Instructions for using assets in campaigns

When to use this tool:
- "Show me my existing Meta ad images"
- "What videos do I already have in Meta?"
- "I want to reuse an existing image/video for my campaign"
- "List my Facebook ad library assets"
- Before uploading new assets - check if they already exist

Parameters:
- ad_account_id: Required for multi-account users. Get from list_connected_accounts
- asset_type: 'all' (default), 'image', or 'video' - filters which asset types are returned
- limit: Max assets to return (default 50, max 100)

Execution time: 2-5 seconds
Data source: Meta Ad Library API (live)

Workflow:
1. Use `discover_meta_assets` to find existing images and/or videos
2. Copy the `image_hash` (images) or `video_id` (videos) of the asset you want to reuse
3. Use that value with `create_meta_image_campaign` (`existing_image_hash`) or `create_meta_video_campaign` (`existing_video_id`)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for discovering existing Meta ad images and videos",
  "properties": {
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
    "asset_type": {
      "default": "all",
      "description": "Which asset types to return: 'all' (default — images and videos), 'image' (image hashes only), or 'video' (video IDs only).",
      "title": "Asset Type",
      "type": "string"
    },
    "limit": {
      "default": 50,
      "description": "Maximum number of assets to return (default 50, max 100)",
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "DiscoverMetaAssetsInput",
  "type": "object"
}
```

</details>

<a id="duplicate_meta_campaign"></a>

## `duplicate_meta_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to duplicate/copy an existing Meta campaign with all its ad sets, ads, and settings.

IMPORTANT: This creates a NEW real campaign in Meta Ads. The duplicate starts in PAUSED status by default for review.

This tool copies the entire campaign structure including:
- Campaign settings (objective, budget strategy)
- All ad sets (targeting, budgets, schedules, promoted_object)
- All ads (creatives, text, CTAs, app_link_spec deep links)

App Campaigns (OUTCOME_APP_PROMOTION) — preserved on duplicate:
- ad-set promoted_object (application_id + object_store_url + custom_event_type)
- creative app_link_spec (deep_link_url_ios / deep_link_url_android)
- creative asset_feed_spec.link_urls.ios_url / android_url (DCO ads)
After duplicating an app campaign, run get_meta_campaign_details on the
new campaign ID to verify the 'App Campaign:' section shows the same
app_id, store URL, and event type as the original.

Returns:
- Original and new campaign IDs
- New campaign status
- Ads Manager URL for the new campaign
- Next steps for review and activation

When to use this tool:
- "Duplicate my campaign"
- "Copy campaign [ID]"
- "Create a copy of this campaign"
- "I want to A/B test with a copy of my campaign"
- "Clone my campaign with different targeting"

Parameters:
- campaign_id: The Meta Campaign ID to duplicate (required)
- new_name: Name for the new campaign (optional, defaults to original + " - Copy")
- status: Status for new campaign — 'PAUSED' (default, recommended) or 'ACTIVE'

Execution time: 10-30 seconds (depends on campaign size)
Creates: New real campaign in Meta Ads

Common use cases:
1. A/B Testing: Duplicate, then modify targeting or creative on the copy
2. Seasonal variants: Copy a proven campaign, update copy and dates
3. New market expansion: Duplicate, change location targeting
4. Budget testing: Copy, change budget levels

Workflow:
1. Use `list_meta_campaigns` to find the campaign ID
2. Use `duplicate_meta_campaign` to create the copy
3. Use `update_meta_campaign` or `update_meta_ad_set` to modify the copy
4. Use `resume_meta_campaign` when ready to launch

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for duplicating a Meta campaign",
  "properties": {
    "campaign_id": {
      "description": "The Meta Campaign ID to duplicate (required)",
      "title": "Campaign Id",
      "type": "string"
    },
    "new_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Name for the new campaign (optional - defaults to original name + ' - Copy')",
      "title": "New Name"
    },
    "status": {
      "default": "PAUSED",
      "description": "Status for the new campaign: 'PAUSED' (default, recommended for review) or 'ACTIVE'",
      "title": "Status",
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
    "campaign_id"
  ],
  "title": "DuplicateMetaCampaignInput",
  "type": "object"
}
```

</details>

<a id="explain_meta_anomaly"></a>

## `explain_meta_anomaly`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks why Meta/Facebook/Instagram performance dropped or changed, what happened to their ROAS/CTR/CPM, or wants to understand why a metric changed during a specific period.

This tool analyzes why a specific metric changed during a specified period by comparing it to historical baselines and identifying contributing factors. It detects Meta-specific causes including creative fatigue, audience saturation, placement mix shifts, and auction competition.

Returns:
- Current metric value vs historical averages (30/60/90-day)
- Deviation percentages from baselines
- Contributing factors ranked by estimated impact
- Factor explanations with details
- Similar historical periods with comparable changes
- Assessment of anomaly severity (CRITICAL/WARNING/MINOR/NORMAL)
- Specific recommendations based on detected factors
- Quick actionable items

When to use this tool:
- "Why did my Meta ROAS drop?"
- "What happened to my Facebook CTR this week?"
- "Why is my Instagram CPM so high?"
- "Explain my Meta performance change"
- "My conversions dropped last week - why?"
- "Why did my frequency spike?"
- "What caused my ROAS to decline 40%?"
- "Diagnose my Meta performance problem"

Parameters:
- metric: Required - 'roas', 'ctr', 'cpc', 'cpm', 'conversions', 'conversion_rate', 'frequency', or 'reach'
- period_start: Required - Start date (YYYY-MM-DD format)
- period_end: Required - End date (YYYY-MM-DD format, must be ≤30 days from start)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 3-8 seconds (statistical analysis across multiple periods)
Data source: campaign_daily_metrics + meta_placement_daily_metrics + meta_ad_creative_metrics tables

Contributing Factors Detected:
- CPM Change: Auction competition fluctuations (holidays, competitor activity)
- CTR Change: Creative performance (fatigue, messaging, targeting)
- Conversion Rate Change: Landing page or offer issues
- Frequency Change: Audience saturation (Meta-specific)
- Creative Fatigue: High frequency + declining CTR (Meta-specific)
- Placement Mix Change: Shift in placement distribution (Meta-specific)
- Campaign Changes: Paused/new campaigns affecting overall performance

Severity Levels:
- 🔴 CRITICAL (≥40% deviation): Immediate action required
- 🟡 WARNING (25-40% deviation): Review recommended
- 🟢 MINOR (15-25% deviation): Monitor situation
- ✅ NORMAL (<15% deviation): Within normal variation

Similar Historical Periods:
Finds past periods with comparable deviations to provide context (e.g., "similar drop occurred during Black Friday 2024")

Best for:
- Diagnosing sudden performance drops
- Understanding seasonal patterns
- Identifying actionable causes vs. external factors
- Prioritizing optimization efforts

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta anomaly explanation analysis",
  "properties": {
    "metric": {
      "default": "ctr",
      "description": "Metric to analyze: 'roas', 'ctr', 'cpc', 'cpm', 'conversions', 'conversion_rate', 'frequency', or 'reach'. Default: 'ctr'",
      "title": "Metric",
      "type": "string"
    },
    "period_start": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Start date of anomaly period (ISO format: YYYY-MM-DD). Defaults to 7 days ago.",
      "title": "Period Start"
    },
    "period_end": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "End date of anomaly period (ISO format: YYYY-MM-DD). Defaults to yesterday. Period must be ≤30 days.",
      "title": "Period End"
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
    "raw_data": {
      "default": false,
      "description": "If true, return ONLY raw metrics as a JSON code block (no severity labels, suggested bids/budgets, industry benchmarks, or optimization recommendations). Use when you run your own attribution model or want to minimize token usage.",
      "title": "Raw Data",
      "type": "boolean"
    }
  },
  "title": "MetaAnomalyExplainInput",
  "type": "object"
}
```

</details>

<a id="explain_performance_anomaly"></a>

## `explain_performance_anomaly`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Explain why a performance metric changed using statistical analysis and historical context.

⚠️ IMPORTANT: This tool retrieves READ-ONLY data. Safe to call multiple times. Uses statistical analysis only (no ML models).

🎯 **What This Tool Does (Performance Agent - Phase 1 Feature 4):**
- Explains why metrics changed (ROAS, CTR, CPC, conversions, conversion rate)
- Compares current period to historical averages (30/60/90-day)
- Identifies contributing factors with severity levels
- Detects campaign changes (paused, new, budget changes)
- Finds similar historical periods (seasonality detection)
- Provides actionable recommendations to address issues

**Returns comprehensive anomaly explanation:**
- Current metric value vs historical averages
- Deviation percentages (how much it changed)
- Contributing factors:
  - CPC changes (>15% = auction competition shifts)
  - Conversion rate changes (>10% = landing page/seasonality issues)
  - Campaign changes (paused high-performers, new campaigns, budget changes)
  - Day-of-week patterns (weekend vs weekday effects)
- Similar historical periods for context
- Assessment (normal variation vs requires action)
- Specific recommendations to fix the issue

🔍 **How Anomaly Detection Works:**

**Historical Comparison:**
- Compares current period to 30/60/90-day averages
- ±15% deviation considered "normal variation"
- >15% deviation flagged as requiring attention

**Contributing Factor Detection:**
1. **CPC Changes** (>15% threshold)
   - Increased CPC = auction competition increased
   - Decreased CPC = auction competition decreased or bid adjustments

2. **Conversion Rate Changes** (>10% threshold)
   - Decreased = landing page issues, seasonality, audience quality
   - Increased = landing page improved, better targeting

3. **Campaign Changes:**
   - Paused high-performers (ROAS > 3.0x) = lost revenue driver
   - New campaigns (>$1K spend) = learning phase affecting overall performance
   - Budget changes (>20%) = delivery and auction participation affected

4. **Day-of-Week Patterns:**
   - Weekend-heavy periods often show different performance
   - Normal for B2C (higher weekend conversion)
   - Normal for B2B (lower weekend conversion)

5. **Seasonality Detection:**
   - Finds similar historical periods (±10% metric value)
   - Helps identify if drop is seasonal vs real issue

**Parameters:**
- metric: 'roas', 'ctr', 'cpc', 'conversions', 'conversion_rate' (REQUIRED)
- period_start: Start date in YYYY-MM-DD format (REQUIRED)
- period_end: End date in YYYY-MM-DD format (REQUIRED, max 30 days period)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-4 seconds (statistical analysis + database queries)
**Data source:** campaign_daily_metrics table (updated nightly, 120-day retention)
**Analysis method:** Statistical comparison (no ML models)
**Trigger:** Reactive (user asks "why?"), not proactive alerts

**Use this tool when:**
- User asks "why did my ROAS drop?"
- User asks "why did my CTR increase?"
- User notices unexpected metric changes
- User wants to understand performance fluctuations
- After seeing performance changes in dashboards



<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for performance anomaly explanation",
  "properties": {
    "metric": {
      "description": "Metric to explain: 'roas' (Return on Ad Spend), 'ctr' (Click-Through Rate), 'cpc' (Cost Per Click), 'conversions', or 'conversion_rate'",
      "title": "Metric",
      "type": "string"
    },
    "period_start": {
      "description": "Start date of the anomaly period (ISO format: YYYY-MM-DD, e.g., '2025-01-15')",
      "title": "Period Start",
      "type": "string"
    },
    "period_end": {
      "description": "End date of the anomaly period (ISO format: YYYY-MM-DD, e.g., '2025-01-21'). Maximum 30 days between start and end.",
      "title": "Period End",
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
    "raw_data": {
      "default": false,
      "description": "If true, return ONLY raw metrics as a JSON code block (no severity labels, suggested bids/budgets, industry benchmarks, or optimization recommendations). Use when you run your own attribution model or want to minimize token usage.",
      "title": "Raw Data",
      "type": "boolean"
    }
  },
  "required": [
    "metric",
    "period_start",
    "period_end"
  ],
  "title": "AnomalyExplanationInput",
  "type": "object"
}
```

</details>

<a id="get_ad_creative"></a>

## `get_ad_creative`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read/export the creative composition of existing ads — videos, images (downloadable URLs), and all text.

This tool retrieves READ-ONLY data via 2 live GAQL queries (cached 15 min in Redis). Safe to call multiple times.

**Why this tool:** `get_campaign_structure` shows ads but not what they're made of. This tool returns the full creative payload of any existing ad so you can audit, archive, or rebuild winners into other formats.

**Returns per ad:**
- Identity: `ad_id`, `ad_name`, `ad_type`, `status`, `ad_strength`, ad group + campaign context
- **Videos:** YouTube `video_id` + `watch_url` + `thumbnail_url` + title per video asset
- **Images:** direct downloadable `url` (Google CDN) + `width`/`height` + `mime_type` + `role` (marketing / square_marketing / portrait_marketing / logo / square_logo)
- **Text:** `headlines[]`, `long_headlines[]`, `descriptions[]`, `business_name`, `call_to_actions[]`
- **Carousel ads:** per-card headline + CTA + card images (resolved to URLs)
- `final_urls`, `display_url`; RSA `path1`/`path2`; RDA colors

**Supported ad types (v1):** DEMAND_GEN_VIDEO_RESPONSIVE_AD, DEMAND_GEN_MULTI_ASSET_AD, DEMAND_GEN_CAROUSEL_AD, RESPONSIVE_SEARCH_AD, RESPONSIVE_DISPLAY_AD. PMax creative lives in asset groups (no per-ad rows) — not covered; use list_pmax_asset_group_images.

**Known API limits (not bugs):** video files are NOT downloadable via the Google Ads API (YouTube watch URL is the canonical reference); per-video orientation (landscape/square/portrait) is not exposed by the API.

**Parameters:**
- customer_id: Optional (uses connected account if omitted)
- ad_id: single ad — OR ad_group_id — OR campaign_id (bulk). At least one required.
- status_filter: 'all' (default — includes paused, useful for archiving) | 'enabled'
- limit: max ads (default 50, max 100)

**Execution time:** 2-5 seconds (2 GAQL queries, then cached 15 min)

**Use this tool when:**
- User asks "what's in this ad?", "download/export my creatives", "which video/image does this ad use?"
- After get_ad_performance identified a winner/loser and the user wants to see or reuse its creative
- User wants to rebuild a winning ad in another format or audit live creatives

**Tip:** Pair with `get_ad_performance` — performance tells you WHICH ad wins, this tells you WHAT it's made of.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for get_ad_creative tool (issue #646 Gap 2).",
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
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    },
    "ad_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "A single ad ID to export (from get_ad_performance or get_campaign_structure).",
      "title": "Ad Id"
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
      "description": "Export all ads in this ad group.",
      "title": "Ad Group Id"
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
      "description": "Bulk: export all ads in this campaign (from list_campaigns).",
      "title": "Campaign Id"
    },
    "status_filter": {
      "default": "all",
      "description": "'all' (default — every non-REMOVED ad, paused included for archiving) or 'enabled' (only ENABLED ads).",
      "title": "Status Filter",
      "type": "string"
    },
    "limit": {
      "default": 50,
      "description": "Max ads returned (default 50, max 100).",
      "title": "Limit",
      "type": "integer"
    },
    "raw_data": {
      "default": false,
      "description": "Return the full raw JSON payload instead of formatted markdown.",
      "title": "Raw Data",
      "type": "boolean"
    }
  },
  "title": "AdCreativeInput",
  "type": "object"
}
```

</details>

<a id="get_ad_group_audiences"></a>

## `get_ad_group_audiences`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read audience targeting on an ad group.

Returns the user lists, in-market / affinity, and custom audiences currently attached,
with bid modifiers and whether each is a negative (exclusion).

**Required:** ad_group_id (from get_campaign_structure).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read audience targeting (user lists, in-market, affinity, custom) on an ad group.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID (from get_campaign_structure).",
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
  "title": "GetAdGroupAudiencesInput",
  "type": "object"
}
```

</details>

<a id="get_ad_group_demographics"></a>

## `get_ad_group_demographics`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read demographic targeting on an ad group (Search, Display, etc.).

Returns the age ranges, genders, and income ranges currently targeted/excluded,
with any bid modifiers. Use before update_ad_group_demographics.

**Required:** ad_group_id (from get_campaign_structure).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read demographic targeting (age/gender/income/parental) on an ad group.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID (from get_campaign_structure).",
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
  "title": "GetAdGroupDemographicsInput",
  "type": "object"
}
```

</details>

<a id="get_ad_group_device_bid_modifiers"></a>

## `get_ad_group_device_bid_modifiers`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read the device (MOBILE/TABLET/DESKTOP) bid modifiers on an ad group.

Search ad groups carry implicit MOBILE/DESKTOP/TABLET rows that read back at 1.0×
(no adjustment) until you set a real modifier via set_ad_group_device_bid_modifiers.
So a device shown at "1.0× (no adjustment)" simply hasn't been bid up or down yet.

**Required:** ad_group_id (from get_campaign_structure).

Read-only, safe to call anytime. Pair with set_ad_group_device_bid_modifiers to adjust.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read the device (MOBILE/TABLET/DESKTOP) bid modifiers on an ad group.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID (from get_campaign_structure).",
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
  "title": "GetAdGroupDeviceBidModifiersInput",
  "type": "object"
}
```

</details>

<a id="get_ad_group_settings"></a>

## `get_ad_group_settings`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read every editable setting on ANY ad group (Search, Display, PMax, Demand Gen, YouTube).

Returns id, name, status, type, cpc/cpm bids, target_cpa/target_roas, ad_rotation_mode,
targeting_setting (audience OBSERVATION vs TARGETING), URL templates, and parent campaign.

Use this before update_ad_group_settings so you know the current values.

**Required:** ad_group_id (from get_campaign_structure).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read every editable setting on ANY ad group (any channel).",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID (from get_campaign_structure).",
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
  "title": "GetAdGroupSettingsInput",
  "type": "object"
}
```

</details>

<a id="get_ad_performance"></a>

## `get_ad_performance`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Per-AD performance breakdown — one row per ad, with individual metrics.

This tool retrieves READ-ONLY data via 1 live GAQL query (cached 5 min in Redis). Safe to call multiple times.

**Why this tool:** `get_campaign_performance` stops at ad-group granularity. When an ad group contains several live ads, this is the only tool that shows which creative is winning so you can pause losers and scale winners.

**Returns one row per ad:**
- Identity: `ad_id`, `ad_name`, `ad_group_id`, `ad_group_name`, `campaign_id`, `campaign_name`
- State: `ad_type` (e.g. DEMAND_GEN_VIDEO_RESPONSIVE_AD, DEMAND_GEN_MULTI_ASSET_AD, RESPONSIVE_SEARCH_AD), `status`, `ad_strength`, `is_live` (ad + ad group + campaign all ENABLED)
- Metrics for the date range: `impressions`, `clicks`, `ctr`, `cost`, `conversions`, `conversion_value`, `cpc`, `cpa`, `roas`, `video_views`, `video_view_rate` (video ads)
- `totals` block + explicit truncation info (`total_ads_matched` vs `returned`)

**Coverage:** Search, Display, Demand Gen, YouTube campaigns. NOT PMax — PMax has no per-ad rows (asset-group model); use `get_pmax_asset_performance` instead.

**Row filter:** REMOVED ads excluded. Paused ads are included only if they actually served in the window (so per-ad numbers still roll up to ad-group totals without zero-row noise).

**Parameters:**
- customer_id: Optional (uses connected account if omitted)
- lookback_days: 7, 30, 60, 90, 120 (default 30). Ignored when both start_date and end_date set.
- start_date / end_date: YYYY-MM-DD (override lookback_days when both provided)
- campaign_id: Optional — scope to one campaign
- ad_group_id: Optional — scope to one ad group
- limit: Max ads returned, cost-desc (default 100, max 500)

**Execution time:** 1-3 seconds (1 GAQL query, then cached 5 min)

**Use this tool when:**
- User asks "which ad/creative is performing best?" or "which video is winning?"
- User wants to pause losing creatives or scale winning ones (follow with pause_ad)
- User needs per-ad CTR / CPA / ROAS / video view rate inside an ad group
- After get_campaign_performance shows an ad group worth drilling into

**Tip:** Pair with `get_ad_creative` to see WHAT each winning/losing ad is made of (videos, images, headlines).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for get_ad_performance tool (issue #646 Gap 1).",
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
      "description": "Optional. Scope to a single campaign (from list_campaigns). Omit for account-wide per-ad breakdown.",
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
      "description": "Optional. Scope to a single ad group (from get_campaign_structure).",
      "title": "Ad Group Id"
    },
    "limit": {
      "default": 100,
      "description": "Max ads returned, sorted by cost desc (default 100, max 500). Response flags truncation explicitly via total_ads_matched/returned.",
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "AdPerformanceInput",
  "type": "object"
}
```

</details>

<a id="get_ad_policy_violations"></a>

## `get_ad_policy_violations`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read policy review/approval state for ads. Surfaces the exact reason an ad was disapproved or limited.

**When to use:**
- User says "my ad got disapproved, why?"
- User says "my campaign isn't serving — is there a policy issue?"
- Routine pre-launch check for newly created ads

**Returns per ad:**
- approval_status: APPROVED, APPROVED_LIMITED, DISAPPROVED, AREA_OF_INTEREST_ONLY, UNSPECIFIED
- review_status: REVIEW_IN_PROGRESS, REVIEWED, UNDER_APPEAL, ELIGIBLE_MAY_SERVE
- topic_entries: list of specific policy topics violated, each with:
  - topic: human-readable policy name (e.g. "Healthcare and medicines")
  - type: PROHIBITED, LIMITED, FULLY_LIMITED, DESCRIPTIVE, BROADENING, AREA_OF_INTEREST_ONLY
  - evidences: text snippets, URLs, language codes that triggered the flag
  - constraints: countries / certifications affected

**Filters (provide at least one of ad_id / ad_group_id / campaign_id):**
- ad_id: most precise; use when investigating one specific ad
- ad_group_id: every ad in this ad group
- campaign_id: every ad in this campaign
- status_filter (default DISAPPROVED_OR_LIMITED): DISAPPROVED, LIMITED, DISAPPROVED_OR_LIMITED, or ALL

**Limitations:**
- Returns up to 500 ads per call
- REMOVED ads are excluded
- Asset-level violations (image disapprovals) are reported on the parent ad
- New ads in REVIEW_IN_PROGRESS won't show topic_entries yet — wait for review

**Example:**
User: "Why isn't my ad serving in the lead-gen campaign?"
Agent:
1. Calls list_campaigns to find campaign_id
2. Calls get_ad_policy_violations(campaign_id=X, status_filter='DISAPPROVED_OR_LIMITED')
3. If results: shows topic, type, and evidence for each — explains what to fix
4. If empty: "All ads are approved. The non-serving issue is elsewhere (budget, bidding, targeting)."


<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for reading ad policy review state.\n\nAt least one of ad_id, ad_group_id, or campaign_id must be set so we don't\nreturn a customer-wide flood. ad_id is most precise.",
  "properties": {
    "ad_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Specific ad ID to check. Most precise; use this when investigating one disapproved ad.",
      "title": "Ad Id"
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
      "description": "Filter to all ads in this ad group.",
      "title": "Ad Group Id"
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
      "description": "Filter to all ads in this campaign.",
      "title": "Campaign Id"
    },
    "status_filter": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "DISAPPROVED_OR_LIMITED",
      "description": "Approval-status filter: DISAPPROVED_OR_LIMITED (default — only ads with policy issues), DISAPPROVED, LIMITED, or ALL (every ad regardless of approval state).",
      "title": "Status Filter"
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
  "title": "GetAdPolicyViolationsInput",
  "type": "object"
}
```

</details>

<a id="get_asset_group_listing_filters"></a>

## `get_asset_group_listing_filters`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read a retail Performance Max asset group's product listing-filter tree.

Retail PMax (a PMax campaign linked to a Merchant Center account) can partition which products
each asset group promotes. Returns each filter node: filter_id, parent_id, node_type (SUBDIVISION /
UNIT_INCLUDED / UNIT_EXCLUDED), the dimension it represents, and whether it's excluded. An empty
tree means the asset group promotes ALL feed products.

**Required:** asset_group_id (a retail-PMax asset group, from get_pmax_asset_groups).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read a retail Performance Max asset group's product listing-filter tree.",
  "properties": {
    "asset_group_id": {
      "description": "The retail-PMax asset group ID (from get_pmax_asset_groups).",
      "title": "Asset Group Id",
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
    "asset_group_id"
  ],
  "title": "GetAssetGroupListingFiltersInput",
  "type": "object"
}
```

</details>

<a id="get_benchmark_context"></a>

## `get_benchmark_context`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Get industry benchmark context for AI-powered recommendations.

⚠️ IMPORTANT: This tool retrieves READ-ONLY data. Safe to call multiple times.

🎯 **What This Tool Does (Performance Agent - Phase 1 Feature 5):**
- Generates contextual benchmark data for the user's business
- Combines business profile with industry benchmarks
- Provides recommended ROAS targets based on vertical
- Returns formatted context for AI prompts

**Returns benchmark context:**
- Business vertical and size context
- Industry-specific ROAS benchmarks (typical, good, excellent)
- CTR benchmarks by industry
- CPC expectations for the vertical
- Seasonality considerations
- Custom recommendations based on profile

**Industry Benchmarks Included:**
| Vertical | Typical ROAS | Good ROAS | Excellent ROAS |
|----------|--------------|-----------|----------------|
| Retail | 4.0x | 6.0x | 8.0x |
| Services | 3.0x | 5.0x | 7.0x |
| Technology | 3.5x | 5.5x | 8.0x |
| Healthcare | 2.5x | 4.0x | 6.0x |
| Finance | 5.0x | 8.0x | 12.0x |
| Education | 2.0x | 3.5x | 5.0x |

**Parameters:**
- **include_recommendations**: Include performance recommendations (default: true)
- **customer_id**: Optional (uses connected account if omitted)

**Use this tool when:**
- Before providing performance analysis
- When comparing user's metrics to industry standards
- User asks "how am I doing compared to others?"
- You need context for optimization recommendations

**Integration with Other Tools:**
Call this BEFORE or AFTER these tools for enhanced recommendations:
- `analyze_wasted_spend` - Contextualize waste against industry norms
- `optimize_budget_allocation` - Use industry-appropriate ROAS targets
- `get_campaign_performance` - Compare metrics to benchmarks
- `explain_performance_anomaly` - Understand if changes are industry-wide

**Execution time:** 1-2 seconds (profile lookup + benchmark calculation)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting benchmark context for AI prompts",
  "properties": {
    "include_recommendations": {
      "default": true,
      "description": "Include performance recommendations based on benchmarks (default: true)",
      "title": "Include Recommendations",
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
  "title": "BenchmarkContextInput",
  "type": "object"
}
```

</details>

<a id="get_business_profile"></a>

## `get_business_profile`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Get the user's business profile for contextual recommendations.

⚠️ IMPORTANT: This tool retrieves READ-ONLY data. Safe to call multiple times.

🎯 **What This Tool Does (Performance Agent - Phase 1 Feature 5):**
- Retrieves the user's saved business profile
- Returns business vertical, size, goals, target audience
- Provides context for more relevant recommendations
- Shows profile source (user-set, inferred, or none)

**Returns business context:**
- Business vertical (retail, services, technology, etc.)
- Business size (small, medium, large)
- Primary goal (leads, sales, awareness, traffic)
- Target audience description
- Geographic focus (local, regional, national, international)
- Seasonality patterns
- Profile confidence level

**Use this tool when:**
- You need business context for recommendations
- Before providing industry-specific advice
- User asks "what type of business am I?"
- You want to personalize optimization suggestions

**If no profile exists:**
- Use `infer_business_profile` to automatically detect from campaign data
- Or ask user to provide business details via `save_business_profile`

**Execution time:** 1-2 seconds (database lookup)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting business profile",
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
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "title": "BusinessProfileInput",
  "type": "object"
}
```

</details>

<a id="get_campaign_dates"></a>

## `get_campaign_dates`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read a campaign's start and end dates.

Returns start_date and end_date (YYYY-MM-DD). An end_date far in the future (e.g.
2037-12-30) or empty means the campaign has no scheduled end. Works on any campaign type.

**Required:** campaign_id (from list_campaigns).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read a campaign's start/end dates.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (from list_campaigns).",
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
  "title": "GetCampaignDatesInput",
  "type": "object"
}
```

</details>

<a id="get_campaign_frequency_caps"></a>

## `get_campaign_frequency_caps`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read a campaign's frequency caps (how often a user can see the ads).

Returns the list of caps, each with level, event_type, time_unit, time_length, and cap.
An empty list means no frequency capping is configured. Works on any campaign type.

**Required:** campaign_id (from list_campaigns).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read a campaign's frequency caps.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (from list_campaigns).",
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
  "title": "GetCampaignFrequencyCapsInput",
  "type": "object"
}
```

</details>

<a id="get_campaign_labels"></a>

## `get_campaign_labels`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List the labels currently attached to a campaign.

Returns each attached label's id, name, and description. Use remove_campaign_label with
a label id to detach it.

**Required:** campaign_id (from list_campaigns).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "List labels attached to a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (from list_campaigns).",
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
  "title": "GetCampaignLabelsInput",
  "type": "object"
}
```

</details>

<a id="get_campaign_performance"></a>

## `get_campaign_performance`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Analyze Google Ads campaign performance with comprehensive insights and recommendations.

⚠️ IMPORTANT: This tool retrieves READ-ONLY data. Safe to call multiple times.

**Returns detailed analysis:**
- Campaign structure and ad group organization
- Keyword performance with quality scores and match types
- Ad group performance breakdown
- Performance metrics (CTR, conversions, CPC, cost, ROAS)
- Optimization recommendations with actionable insights
- Performance trends (last 7 days)

**Parameters:**
- lookback_days: 7, 30, 60, 90, or 120 days (default: 30)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- customer_id: Optional (uses connected account if omitted)
- campaign_id: Optional. When provided, scopes the analysis to a single campaign (all metrics, ad groups, keywords, and trends reflect that campaign only). Omit for account-wide analysis. Use `list_campaigns` first to find the campaign ID.

**Execution time:** 2-5 seconds (direct backend API call)
**Data source:** Cached database (updated nightly via metrics collection)

**Use this tool to:**
- Review current campaign performance
- Identify optimization opportunities
- Get data-driven recommendations
- Analyze keyword and ad effectiveness
- Understand what's working and what needs improvement



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
      "description": "Number of days to analyze (7, 30, 60, or 90 days). Default is 30 days.",
      "title": "Lookback Days",
      "type": "integer"
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
      "description": "Optional Google Ads campaign ID to filter analysis to a single campaign. When provided, all metrics, ad-group, keyword, and trend data are scoped to this campaign only. Omit for account-wide analysis across all campaigns.",
      "title": "Campaign Id"
    }
  },
  "title": "PerformanceAnalysisInput",
  "type": "object"
}
```

</details>

<a id="get_campaign_structure"></a>

## `get_campaign_structure`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Get campaign structure with ad groups, keywords, ads, and extensions. Supports pagination for large campaigns.

This tool retrieves READ-ONLY data. Safe to call multiple times.

**Returns campaign hierarchy (paginated by ad groups):**
- Campaign details (name, status, budget, bidding strategy)
- Ad groups with their settings (paginated — default 5 per page)
- Keywords per ad group (including match types, bids, status)
- Ads per ad group (including RSA headlines/descriptions, ad strength)
- Negative keywords per ad group
- Campaign-level extensions and negative keywords (on page 1 only)
- Pagination metadata (page, total_pages, has_more)
- Summary counts (total ad groups, keywords, ads across ALL pages)

**Parameters:**
- campaign_id: The campaign ID (REQUIRED - get from list_campaigns)
- customer_id: Optional (uses connected account if omitted)
- page: Page number, 1-based (default: 1)
- page_size: Ad groups per page, 1-50 (default: 5)
- ad_group_id: Optional — fetch only this single ad group (bypasses pagination)
- include: What detail per ad group: 'all' (default), 'summary' (counts only), 'keywords', 'ads'

**⚡ PAGINATION CONTRACT (IMPORTANT FOR AI AGENTS):**
- The response includes `pagination.has_more` — if true, you MUST call again with `page` incremented
- Continue calling until `has_more` is false
- Then consolidate all pages and present the complete campaign structure to the user
- The `summary` section is always included and shows total counts across ALL ad groups (not just the current page)
- Extensions and campaign-level negative keywords are only returned on page 1
- Use `ad_group_id` to drill into a single ad group when the user asks about a specific one
- Use `include='summary'` for a quick overview without nested keyword/ad data

**Execution time:** 3-8 seconds per page (multiple API queries)

**Use this tool when:**
- User wants to update an existing campaign
- User wants to see current keywords/ads
- User wants to add extensions to existing campaign
- User says "show me what's in this campaign"
- Before making any updates to a campaign

**Important IDs returned:**
- campaign.id - For campaign-level updates (budget, status)
- ad_groups[].id - For adding keywords/ads
- keywords[].id - For keyword updates (status, bids)
- ads[].id - For ad content updates

**Example flow:**
1. User: "I want to update my campaign"
2. Agent: Uses list_campaigns to show all campaigns
3. User: Selects campaign "Summer Sale 2025"
4. Agent: Uses get_campaign_structure with that campaign_id
5. If has_more=true, agent calls again with page=2, page=3, etc.
6. Agent: Shows consolidated structure and asks what to update
7. User: "Change the headlines"
8. Agent: Uses update_ad_headlines with the ad_id from structure

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting campaign structure with pagination",
  "properties": {
    "campaign_id": {
      "description": "The single campaign ID to get structure for. Use list_campaigns first to get available campaign IDs. This tool returns ONE campaign at a time — to inspect several, call it once per campaign_id (there is no campaign_ids / campaign_name_filter parameter).",
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
      "description": "Page number (1-based). Use to paginate through large campaigns. Default: 1",
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
      "default": 5,
      "description": "Number of ad groups per page (1-50). Default: 5",
      "title": "Page Size"
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
      "description": "Optional: Fetch only this specific ad group's details (bypasses pagination)",
      "title": "Ad Group Id"
    },
    "include": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "all",
      "description": "What to include per ad group: 'all' (default), 'summary' (counts only, no nested data), 'keywords' (keywords only), 'ads' (ads only)",
      "title": "Include"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "GetCampaignStructureInput",
  "type": "object"
}
```

</details>

<a id="get_campaign_targeting"></a>

## `get_campaign_targeting`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Full targeting view for a Google Ads campaign — locations, languages, demographics, audiences, devices, ad schedule, topics, placements, keywords, AND negative variants of each.

This tool retrieves READ-ONLY data via 2 GAQL queries (cached 15 min in Redis). Safe to call multiple times.

**Returns sections (only the ones with data are rendered):**
- 📍 **Locations** — geo target constants + bid modifiers
- 🌐 **Languages** — language constants
- 👥 **Demographics** — gender, age range, parental status, income range (campaign or ad-group level, with bid modifiers)
- 🎯 **Audiences** — user lists (remarketing), user interests (in-market/affinity), custom audiences, combined audiences, AUDIENCE resource
- 📱 **Devices** — device type + bid modifier
- ⏰ **Ad Schedule** — day of week + hour window + bid modifier
- 📺 **Topics** — topic constants (Display)
- 🌐 **Placements** — managed placement URLs (Display)
- 🔑 **Keywords** — keyword text + match type
- 🚫 **Negatives** — exclusion list across the same dimensions

**Parameters:**
- campaign_id: The campaign ID (REQUIRED — get from list_campaigns)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-5 seconds (2 GAQL queries, then cached 15 min)

**Use this tool when:**
- User asks "what is this campaign targeting?" — covers ALL targeting axes
- User asks "what audiences/demographics/devices does this campaign target?"
- User wants ad schedule, placement, or topic exclusions
- Before recommending targeting changes
- To audit targeting setup post-creation

**Out of scope (tracked separately):**
- PMax `asset_group_signals` (different resource)
- Customer-level negative criterion lists (account-wide negatives)
- Shared negative keyword lists (separate resource)
- 3rd-party brand safety / IVT services

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for getting campaign location targeting",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to get location targeting for. Use list_campaigns first.",
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
  "title": "GetCampaignTargetingInput",
  "type": "object"
}
```

</details>

<a id="get_campaign_tracking"></a>

## `get_campaign_tracking`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read a campaign's URL tracking settings.

Returns the campaign-level `tracking_url_template` (click-measurement/redirect URL),
`final_url_suffix` (query params appended to the landing page), and
`url_custom_parameters` (the {key,value} params usable as `{_key}` in the template).

Use this to see or verify what `update_campaign` set. Reads/writes of these tracking
fields are campaign-level and apply to all ads in the campaign.

**Required:** campaign_id (from list_campaigns).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read a campaign's URL tracking settings (read-back for update_campaign tracking fields).",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to read tracking settings for (from list_campaigns).",
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
  "title": "GetCampaignTrackingInput",
  "type": "object"
}
```

</details>

<a id="get_connections_status"></a>

## `get_connections_status`

Scope: **supporting** · Capability: **accounts** · [Definition](https://mcp.adspirer.com/api/v1/tools)

View connected ad accounts and OAuth connections.

Shows all connected ad platforms (Google Ads, TikTok Ads, Meta Ads, LinkedIn Ads) with:
- Connection status and account details
- Primary account indicator
- Option to switch primary account
- Quick links to connect new platforms

Use this tool when user asks about:
- "how many accounts do I have" / "how many ad accounts"
- "what accounts are connected" / "connected accounts"
- "which account am I using" / "current account"
- "show my connections" / "list my accounts"
- "connection status" / "account status"
- "what platforms do I have connected"
- Account count, account list, or connection overview

Do not use for:
- Discovering campaigns, ads, or keywords (use discover_existing_assets)
- Performance data or metrics (use performance tools)
- Creating or managing campaigns

This is specifically for OAuth connections and account management.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for get_connections_status tool - no required params",
  "properties": {},
  "title": "ConnectionsStatusInput",
  "type": "object"
}
```

</details>

<a id="get_conversion_action_performance"></a>

## `get_conversion_action_performance`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Per-conversion-action performance breakdown.

This tool retrieves READ-ONLY data via 2 live GAQL queries (cached 5 min in Redis). Safe to call multiple times.

**Returns:**
- `totals` — account or campaign aggregate: cost, conversions, conversion_value, CPA, ROAS, clicks, impressions
- `breakdown` — per-conversion-action rows: conversions, conversion_value, all_conversions, all_conversions_value, avg_value_per_conversion, share_of_conversions, share_of_value
- `note` — explains why per-action CPA/ROAS are NOT computed

**Important — what this tool does NOT do:**
Per-action CPA and ROAS are NOT shown. Google Ads rejects `cost_micros` when segmenting by `conversion_action` because cost is shared across all actions a click can produce. We do NOT prorate cost per action — that would fabricate data. Account/campaign-level CPA + ROAS appear in `totals`. Use `share_of_conversions` and `share_of_value` to see relative contribution per action.

**Parameters:**
- customer_id: Optional (uses connected account if omitted)
- lookback_days: 7, 30, 60, 90, 120 (default 30). Ignored when both start_date and end_date set.
- start_date / end_date: YYYY-MM-DD (override lookback_days when both provided)
- campaign_id: Optional. Scopes the breakdown to a single campaign.

**Execution time:** 2-5 seconds (2 GAQL queries, then cached 5 min)

**Use this tool when:**
- User asks "which conversion action drove the most conversions / value?"
- User wants per-action breakdown for accounts with multiple conversion actions (e.g., lead vs purchase)
- User wants to see relative contribution of each action to total conversions/value
- After `list_conversion_actions` to map IDs to performance

**Tip:** Use this AFTER `list_conversion_actions` so you know action names/IDs/categories. For a single campaign: pass `campaign_id` from `list_campaigns`.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for get_conversion_action_performance tool.",
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
      "description": "Optional. Scope the breakdown to a single campaign. Omit for account-wide breakdown.",
      "title": "Campaign Id"
    }
  },
  "title": "ConversionActionPerformanceInput",
  "type": "object"
}
```

</details>

<a id="get_demandgen_audiences"></a>

## `get_demandgen_audiences`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read the grouped audience targeting on a Demand Gen (or YouTube) ad group.

Demand Gen ad groups use ONE grouped audience (a named audience built from segments),
not individual audience criteria. This shows the audience name and its segments.

Use this before replace_demandgen_audiences to see what's currently targeted.

**Required:** ad_group_id (from get_campaign_structure). Only works on Demand Gen ad groups.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read the grouped audience attached to a Demand Gen ad group.",
  "properties": {
    "ad_group_id": {
      "description": "Demand Gen ad group ID (from get_campaign_structure).",
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
  "title": "GetDemandGenAudiencesInput",
  "type": "object"
}
```

</details>

<a id="get_demandgen_channel_controls"></a>

## `get_demandgen_channel_controls`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read which delivery channels are enabled on a Demand Gen (or YouTube) ad group.

Demand Gen ad groups deliver across 6 channels: youtube_in_stream, youtube_in_feed,
youtube_shorts, discover, gmail, display. This shows the on/off state of each.

Use this before update_demandgen_channel_controls so you know the current state.

**Required:** ad_group_id (from get_campaign_structure). Only works on Demand Gen ad groups.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Read the 6 Demand Gen delivery-channel toggles for an ad group.",
  "properties": {
    "ad_group_id": {
      "description": "Demand Gen ad group ID (from get_campaign_structure).",
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
  "title": "GetDemandGenChannelControlsInput",
  "type": "object"
}
```

</details>

<a id="get_display_ad_group_settings"></a>

## `get_display_ad_group_settings`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read every editable setting on a Display ad group.

Returns: id, name, status, type (DISPLAY_STANDARD), campaign resource, current cpc_bid + cpm_bid (both in account currency AND micros), ad_rotation_mode, optimized_targeting_enabled, exclude_demographic_expansion.

**Use this before update_display_ad_group** so you can show the user the current state and ask for which fields to change.

**Execution time:** 1-3 seconds (read-only).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for get_display_ad_group_settings.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID.",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id"
  ],
  "title": "GetDisplayAdGroupSettingsInput",
  "type": "object"
}
```

</details>

<a id="get_display_audiences"></a>

## `get_display_audiences`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List audience targeting on a Display campaign's ad groups.

Returns entries with type ∈ {USER_LIST, CUSTOM_AUDIENCE, USER_INTEREST, COMBINED_AUDIENCE}.

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

<a id="get_display_demographics"></a>

## `get_display_demographics`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List demographic targeting (age, gender, parental status, income) on a Display campaign's ad groups.

Each entry has a `negative` flag — Google targets via exclude-the-inverse: to target MALE only, everything else is listed as negative criteria.

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

<a id="get_display_frequency_caps"></a>

## `get_display_frequency_caps`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Read the frequency caps currently configured on a Display campaign.

Returns a list of `{level, event_type, time_unit, time_length, cap}` entries.

**Execution time:** 1-3 seconds (read-only).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for get_display_frequency_caps.",
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
  "title": "GetDisplayFrequencyCapsInput",
  "type": "object"
}
```

</details>

