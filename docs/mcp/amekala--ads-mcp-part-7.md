# amekala/ads-mcp — tools 211–241

[All tools](amekala--ads-mcp.md) · [Tool index](../tool-index.md)

<a id="update_ad_content"></a>

## `update_ad_content`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Combined update for ad content (RSA, RDA, or DemandGen video-responsive / multi-asset) in a single API call with combined field mask.

Backend auto-detects ad type and applies the right proto branch.

**Parameters:**
- ad_id (REQUIRED), ad_group_id (REQUIRED)
- headlines: Optional — RSA 3-15 (max 30 chars) / RDA 1-5 (max 30 chars) / DemandGen 1-5 (max 40 chars)
- descriptions: Optional — RSA 2-4 / RDA 1-5 / DemandGen 1-5, each max 90 chars
- long_headline: Optional — RDA only (single string, max 90 chars). Rejected for RSA and DemandGen
  (DemandGen uses long_headlineS, plural — not editable via this tool).
- final_urls: Optional — landing page URLs (all types)
- final_mobile_urls: Optional — mobile-specific landing URLs (all types). Send [] to clear.
- tracking_url_template: Optional — per-ad tracking template, e.g. "{lpurl}?utm_source=google" (all types). Send "" to clear.
- customer_id: Optional

At least one of headlines, descriptions, long_headline, final_urls, final_mobile_urls, or tracking_url_template is required.

**Execution time:** 2-4 seconds.

**Example (RDA ad):** Update headlines + long_headline + descriptions in one call.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for combined ad content update (RSA, RDA, or DemandGen).\n\nBackend auto-detects ad type and applies the right proto branch.\n`long_headline` is only valid for RDA — rejected for RSA and DemandGen\n(DemandGen uses long_headlineS, plural — not editable via this tool).",
  "properties": {
    "ad_id": {
      "description": "The ad ID to update. Get from get_campaign_structure.",
      "title": "Ad Id",
      "type": "string"
    },
    "ad_group_id": {
      "description": "The ad group ID the ad belongs to. Get from get_campaign_structure.",
      "title": "Ad Group Id",
      "type": "string"
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
      "description": "Optional: headlines (RSA 3-15 max 30 chars / RDA 1-5 max 30 chars / DemandGen 1-5 max 40 chars).",
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
      "description": "Optional: descriptions (RSA 2-4 / RDA 1-5 / DemandGen 1-5, each max 90 chars).",
      "title": "Descriptions"
    },
    "long_headline": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: long headline text, max 90 chars. RDA only — rejected for RSA and DemandGen.",
      "title": "Long Headline"
    },
    "final_urls": {
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
      "description": "Optional: Landing page URLs.",
      "title": "Final Urls"
    },
    "final_mobile_urls": {
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
      "description": "Optional: mobile-specific landing URLs (all ad types). Send [] to clear existing mobile URLs; omit to leave unchanged.",
      "title": "Final Mobile Urls"
    },
    "tracking_url_template": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: per-ad tracking URL template, e.g. '{lpurl}?utm_source=google' (all ad types). Send \"\" to clear; omit to leave unchanged.",
      "title": "Tracking Url Template"
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
    "ad_id",
    "ad_group_id"
  ],
  "title": "UpdateAdContentInput",
  "type": "object"
}
```

</details>

<a id="update_ad_descriptions"></a>

## `update_ad_descriptions`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update descriptions for a Responsive Search Ad (RSA), Responsive Display Ad (RDA), OR a DemandGen ad (video-responsive / multi-asset).

Backend auto-detects ad type; per-type count bounds:
- RSA: 2-4 descriptions
- RDA: 1-5 descriptions
- DemandGen (video-responsive / multi-asset): 1-5 descriptions

Each description is max 90 characters (all types).

**Parameters:**
- ad_id (REQUIRED), ad_group_id (REQUIRED), descriptions (REQUIRED)
- customer_id (optional)

**Description Rules:**
- Should expand on headlines and include specific details + CTAs
- Formula: [Value Prop]. [Specific Detail]. [CTA].

**Execution time:** 2-4 seconds.

**WARNING:** Updated ads go through Google's review process.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating ad descriptions (RSA, RDA, or DemandGen).\n\nThe backend auto-detects ad type and enforces per-type count bounds:\n- RSA: 2-4 descriptions\n- RDA: 1-5 descriptions\n- DemandGen (video-responsive / multi-asset): 1-5 descriptions",
  "properties": {
    "ad_id": {
      "description": "The ad ID to update. Get from get_campaign_structure.",
      "title": "Ad Id",
      "type": "string"
    },
    "ad_group_id": {
      "description": "The ad group ID the ad belongs to. Get from get_campaign_structure.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "descriptions": {
      "description": "Descriptions (max 90 characters each). RSA requires 2-4; RDA requires 1-5; DemandGen requires 1-5.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Descriptions",
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
    }
  },
  "required": [
    "ad_id",
    "ad_group_id",
    "descriptions"
  ],
  "title": "UpdateAdDescriptionsInput",
  "type": "object"
}
```

</details>

<a id="update_ad_group_demographics"></a>

## `update_ad_group_demographics`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Set demographic TARGETING on an ad group (exclude-the-inverse).

You list which age_ranges / genders / income_ranges to TARGET. Google achieves this
by EXCLUDING every value you did NOT list, so be explicit about the full set you want.

**Valid values:**
- age_ranges: AGE_RANGE_18_24, _25_34, _35_44, _45_54, _55_64, _65_UP, AGE_RANGE_UNDETERMINED
- genders: MALE, FEMALE, UNDETERMINED
- income_ranges: INCOME_RANGE_0_50, _50_60, _60_70, _70_80, _80_90, _90_UP, INCOME_RANGE_UNDETERMINED

**IMPORTANT:** Confirm with the user before narrowing demographics — excludes are live.

**Required:** ad_group_id + at least one dimension.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Set demographic TARGETING on an ad group (exclude-the-inverse pattern).\n\nYou list which age_ranges / genders / income_ranges to TARGET; Google achieves\nthis by EXCLUDING every value you did NOT list. Sending an empty list for a\ndimension leaves that dimension untargeted (all values eligible).",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID to update.",
      "title": "Ad Group Id",
      "type": "string"
    },
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
      "description": "Age ranges to TARGET. Valid: AGE_RANGE_18_24, AGE_RANGE_25_34, AGE_RANGE_35_44, AGE_RANGE_45_54, AGE_RANGE_55_64, AGE_RANGE_65_UP, AGE_RANGE_UNDETERMINED.",
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
      "description": "Genders to TARGET. Valid: MALE, FEMALE, UNDETERMINED.",
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
      "description": "Income ranges to TARGET. Valid: INCOME_RANGE_0_50, INCOME_RANGE_50_60, INCOME_RANGE_60_70, INCOME_RANGE_70_80, INCOME_RANGE_80_90, INCOME_RANGE_90_UP, INCOME_RANGE_UNDETERMINED.",
      "title": "Income Ranges"
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
  "title": "UpdateAdGroupDemographicsInput",
  "type": "object"
}
```

</details>

<a id="update_ad_group_settings"></a>

## `update_ad_group_settings`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update any combination of settings on ANY ad group (any channel).

**Can update (all optional — only what you set changes):**
- name, status (ENABLED/PAUSED)
- cpc_bid_micros, cpm_bid_micros, target_cpa_micros, target_roas (fraction, e.g. 4.0=400%)
- ad_rotation_mode (OPTIMIZE / ROTATE_FOREVER)
- final_url_suffix, tracking_url_template
- audience_targeting_mode (OBSERVATION vs TARGETING)

**IMPORTANT:** Confirm with the user before changing bids or status.
Call get_ad_group_settings first to see current values.

**Required:** ad_group_id + at least one field to change.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Update any combination of editable settings on ANY ad group (any channel).\n\nEvery field is optional; only the ones you set are changed.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID to update.",
      "title": "Ad Group Id",
      "type": "string"
    },
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
      "description": "New ad group name.",
      "title": "Name"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ENABLED | PAUSED (use remove_ad_group to soft-delete).",
      "title": "Status"
    },
    "cpc_bid_micros": {
      "anyOf": [
        {
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Max CPC bid in micros.",
      "title": "Cpc Bid Micros"
    },
    "cpm_bid_micros": {
      "anyOf": [
        {
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CPM bid in micros.",
      "title": "Cpm Bid Micros"
    },
    "target_cpa_micros": {
      "anyOf": [
        {
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Ad-group target CPA in micros.",
      "title": "Target Cpa Micros"
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
      "description": "Ad-group target ROAS as a fraction (e.g. 4.0 = 400%). NOT micros.",
      "title": "Target Roas"
    },
    "ad_rotation_mode": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "OPTIMIZE | ROTATE_FOREVER.",
      "title": "Ad Rotation Mode"
    },
    "final_url_suffix": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Final URL suffix.",
      "title": "Final Url Suffix"
    },
    "tracking_url_template": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Tracking URL template.",
      "title": "Tracking Url Template"
    },
    "audience_targeting_mode": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "OBSERVATION (bid-only) vs TARGETING (restrict) for audiences on this ad group.",
      "title": "Audience Targeting Mode"
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
  "title": "UpdateAdGroupSettingsInput",
  "type": "object"
}
```

</details>

<a id="update_ad_headlines"></a>

## `update_ad_headlines`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update headlines for a Responsive Search Ad (RSA), Responsive Display Ad (RDA), OR a DemandGen ad (video-responsive / multi-asset).

The backend auto-detects the ad type and enforces per-type count + character bounds:
- RSA (Search): 3-15 headlines, max 30 chars each
- RDA (Display): 1-5 headlines, max 30 chars each
- DemandGen (video-responsive / multi-asset): 1-5 headlines, max 40 chars each

**MANDATORY WORKFLOW:**
1. Call `get_campaign_structure` or `get_ad_creative` to find ad_id and ad_group_id
2. Review current headlines
3. Prepare new headlines:
   - RSA — 3-15 headlines. Follow the category system (Category A: What It Is,
     Category B: Benefits, Category C: Pain/Proof/CTA). Headlines must work in ANY combination.
   - RDA — 1-5 short headlines (max 30 chars each). You'll also likely want to update
     the `long_headline` via `update_ad_content` (RDA only, max 90 chars).
   - DemandGen — 1-5 headlines (max 40 chars each). This replaces the ad's short headlines;
     it does NOT touch long_headlines/descriptions.
4. Validate (char limit per type above, no "!" marks, no unverified superlatives like "Best", "#1")
5. Get user approval
6. Call this tool with ad_id, ad_group_id, headlines

**Parameters:**
- ad_id (REQUIRED), ad_group_id (REQUIRED), headlines (REQUIRED)
- customer_id (optional)

**Execution time:** 2-4 seconds.

**WARNING:** Updated ads go through Google's review process (24-48 hours).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating ad headlines (RSA, RDA, or DemandGen).\n\nThe backend auto-detects ad type and enforces per-type count + char bounds:\n- RSA (Responsive Search Ad): 3-15 headlines, max 30 chars each\n- RDA (Responsive Display Ad): 1-5 headlines, max 30 chars each\n- DemandGen (video-responsive / multi-asset): 1-5 headlines, max 40 chars each",
  "properties": {
    "ad_id": {
      "description": "The ad ID to update. Get from get_campaign_structure (look in ad_groups -> ads section).",
      "title": "Ad Id",
      "type": "string"
    },
    "ad_group_id": {
      "description": "The ad group ID the ad belongs to. Get from get_campaign_structure.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "headlines": {
      "description": "Headlines. RSA requires 3-15 (max 30 chars each); RDA requires 1-5 (max 30 chars); DemandGen requires 1-5 (max 40 chars). Headlines should work well in any combination. Avoid exclamation marks and unverified superlatives (Best, #1, etc.).",
      "items": {
        "type": "string"
      },
      "maxItems": 15,
      "minItems": 1,
      "title": "Headlines",
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
    }
  },
  "required": [
    "ad_id",
    "ad_group_id",
    "headlines"
  ],
  "title": "UpdateAdHeadlinesInput",
  "type": "object"
}
```

</details>

<a id="update_bid_strategy"></a>

## `update_bid_strategy`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Change campaign bidding strategy.

**Available Strategies:**
- MAXIMIZE_CLICKS: Get as many clicks as possible within budget (optional cpc_bid_ceiling = max CPC cap)
- MAXIMIZE_CONVERSIONS: Get as many conversions as possible
- TARGET_CPA: Set a target cost per acquisition (requires target_cpa)
- TARGET_ROAS: Set a target return on ad spend (requires target_roas)
- TARGET_IMPRESSION_SHARE: Bid to appear for a target share of auctions at a chosen page position (requires impression_share_location + impression_share_target_percent)

**Parameters:**
- campaign_id: The campaign ID (REQUIRED)
- strategy: one of the strategies above (REQUIRED)
- target_cpa: Required if strategy is TARGET_CPA. In dollars, e.g., 25.00 for $25 CPA
- target_roas: Required if strategy is TARGET_ROAS. Multiplier, e.g., 4.0 for 400% ROAS
- impression_share_location: Required if strategy is TARGET_IMPRESSION_SHARE. ABSOLUTE_TOP_OF_PAGE, TOP_OF_PAGE, or ANYWHERE_ON_PAGE
- impression_share_target_percent: Required if strategy is TARGET_IMPRESSION_SHARE. 1-100, e.g., 80 for 80%
- cpc_bid_ceiling: Max CPC cap. Used with MAXIMIZE_CLICKS or TARGET_IMPRESSION_SHARE. In the ACCOUNT'S currency (not cents, not USD; for 8.00 send 8). Optional — omit to keep an existing ceiling; STRONGLY recommended on TARGET_IMPRESSION_SHARE. Not accepted on other strategies
- customer_id: Optional (uses connected account if omitted)

**IMPORTANT:**
- TARGET_CPA requires conversion tracking to be set up
- TARGET_ROAS requires conversion value tracking
- TARGET_IMPRESSION_SHARE is for visibility goals (Search/Display); set cpc_bid_ceiling so bids don't run away chasing the target
- This changes the bidding on a LIVE campaign immediately — review the values (especially the CPC ceiling and target %) before moving on
- The response shows the ceiling READ BACK from Google ("Max CPC ceiling: …"); if it says "not set", the cap did not save — do not tell the user it did. `list_campaigns` / `get_campaign_structure` also report the ceiling
- Changing strategy may take 1-2 weeks to stabilize performance
- Confirm with user before changing

**Execution time:** 2-4 seconds

**Examples:**
User: "I want to target $30 CPA"
Agent: Uses update_bid_strategy with strategy=TARGET_CPA, target_cpa=30.00

User: "Target absolute top of page, 80% impression share, max CPC $4"
Agent: Uses update_bid_strategy with strategy=TARGET_IMPRESSION_SHARE, impression_share_location=ABSOLUTE_TOP_OF_PAGE, impression_share_target_percent=80, cpc_bid_ceiling=4.00

User: "Maximize clicks but never pay more than CA$8 a click"
Agent: Uses update_bid_strategy with strategy=MAXIMIZE_CLICKS, cpc_bid_ceiling=8 (account currency is CAD, so 8 means CA$8.00)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating campaign bidding strategy",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to update. Use list_campaigns first to get available campaign IDs.",
      "title": "Campaign Id",
      "type": "string"
    },
    "strategy": {
      "description": "Bidding strategy: MAXIMIZE_CLICKS, MAXIMIZE_CONVERSIONS, MAXIMIZE_CONVERSION_VALUE, TARGET_CPA, TARGET_ROAS, or TARGET_IMPRESSION_SHARE",
      "title": "Strategy",
      "type": "string"
    },
    "target_cpa": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target CPA in dollars (required if strategy is TARGET_CPA). Example: 25.00 for $25 CPA",
      "title": "Target Cpa"
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
      "description": "Target ROAS multiplier (required if strategy is TARGET_ROAS). Example: 4.0 for 400% ROAS",
      "title": "Target Roas"
    },
    "impression_share_location": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Required for TARGET_IMPRESSION_SHARE. Where on the page to target: ABSOLUTE_TOP_OF_PAGE (very top / first ad), TOP_OF_PAGE (above results), or ANYWHERE_ON_PAGE.",
      "title": "Impression Share Location"
    },
    "impression_share_target_percent": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Required for TARGET_IMPRESSION_SHARE. Impression-share target as a percent 1-100 (e.g. 80 for 80% impression share).",
      "title": "Impression Share Target Percent"
    },
    "cpc_bid_ceiling": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Max CPC bid ceiling. Used with MAXIMIZE_CLICKS (caps what Maximize Clicks may pay per click) or TARGET_IMPRESSION_SHARE (caps bids chasing the impression-share target). In the ACCOUNT'S OWN CURRENCY as a decimal — NOT cents, NOT USD. For an 8.00 ceiling send 8, not 8000000. Optional; omit it to leave an existing ceiling unchanged. Rejected on other strategies (they have no max-CPC field). The response echoes the ceiling read back from Google so you can confirm it saved.",
      "title": "Cpc Bid Ceiling"
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
    "campaign_id",
    "strategy"
  ],
  "title": "UpdateBidStrategyInput",
  "type": "object"
}
```

</details>

<a id="update_campaign"></a>

## `update_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update an existing campaign's settings.

**Can update:**
- name: Campaign name
- status: ENABLED or PAUSED
- budget_amount: Daily budget in dollars
- target_search_network: Search Partners toggle (Search campaigns)
- target_content_network: Display Network expansion (Search campaigns)
- language_codes: Replace language targeting (e.g. ["en"] for English-only). As of Sept 2026 this no longer applies to SEARCH campaigns (Google matches on ad language); still honored for Performance Max. A safe no-op on Search — nothing changes and you get a note explaining why.
- locations_to_add: Append locations to geo targeting (free text or geoTargetConstants/<id>)
- locations_to_remove: Remove locations by criterion resource name (get from get_campaign_targeting)
- audience_targeting_mode: OBSERVATION vs TARGETING for audience signals
- ai_max_enabled: Google AI Max toggle on Search campaigns

**IMPORTANT:**
- Confirm with user BEFORE making changes
- Use list_campaigns first to get campaign_id
- At least one update field is required
- For locations_to_remove, you MUST call get_campaign_targeting first to obtain the criterion resource names — free-text location names will not work for removal.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED - get from list_campaigns)
- name: New campaign name (optional)
- status: ENABLED or PAUSED (optional)
- budget_amount: Daily budget in dollars, e.g., 50.00 for $50/day (optional)
- target_search_network / target_content_network: bools (optional)
- language_codes: list[str] (optional, REPLACES current set)
- locations_to_add / locations_to_remove: list[str] (optional)
- audience_targeting_mode: OBSERVATION | TARGETING (optional)
- ai_max_enabled: bool (optional)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-6 seconds depending on number of targeting changes

**Example:**
User: "Increase the budget to $100/day and target English-only"
Agent:
1. Uses list_campaigns to find the campaign
2. Confirms: "I'll update 'Summer Sale' budget to $100/day and set language to English-only. Proceed?"
3. Uses update_campaign(campaign_id=..., budget_amount=100.00, language_codes=["en"])

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating campaign settings",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to update. Use list_campaigns first to get available campaign IDs.",
      "title": "Campaign Id",
      "type": "string"
    },
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
      "description": "New campaign name (optional)",
      "title": "Name"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New status: ENABLED or PAUSED (optional)",
      "title": "Status"
    },
    "budget_amount": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New daily budget in dollars, e.g., 50.00 for $50/day (optional)",
      "title": "Budget Amount"
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
      "description": "Search Partners network toggle. Default OFF on new campaigns. Search Partners traffic typically has 30–50% lower conversion rates than google.com search — only enable when explicitly requested. Pass true to enable, false to disable.",
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
      "description": "Display Network expansion for Search campaigns. Default OFF on new campaigns. Display traffic has very different user intent — only enable when explicitly requested. Pass true to enable, false to disable.",
      "title": "Target Content Network"
    },
    "language_codes": {
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
      "description": "REPLACE the campaign's language targeting with this list. ISO-639-1 codes (`en`, `es`, `fr`, `de`, `pt`, `it`, `nl`, `ja`, `zh`, `ko`, `ru`, `ar`, `hi`, `tr`, `pl`, `id`, `th`, `vi`, `sv`, `fi`, `da`, `no`, `cs`, `el`, `he`, `hu`, `ro`, `sk`, `uk`, `bg`, `bn`, `ml`, `ta`, `te`, `mr`, `ur`, `fa`, `ms`, `tl`, `lt`, `lv`, `et`, `sl`, `hr`, `sr`, `ca`, `is`) or `languageConstants/<id>` resource names from `list_google_languages`. Pass `[\"en\"]` for English-only targeting. Sending this REPLACES the campaign's existing language criteria — pass the full intended list. NOTE: as of Sept 2026 Google removed campaign-level language targeting for SEARCH campaigns — Search ads now match on the language of the ad itself, so this setting no longer applies to Search (it is still honored for Performance Max on YouTube/Display/Discover/Gmail). Sending it on a Search campaign is a safe no-op: nothing is changed and you'll get a note back explaining why.",
      "title": "Language Codes"
    },
    "locations_to_add": {
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
      "description": "Locations to ADD to the campaign's geo targeting. Accepts free-text (`'Miami, FL'`, `'United States'`) OR `geoTargetConstants/<id>` resource names from `resolve_google_locations`. New criteria are appended — existing targets are untouched. To remove existing targets, use `locations_to_remove`.",
      "title": "Locations To Add"
    },
    "locations_to_remove": {
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
      "description": "Locations to REMOVE from the campaign's geo targeting. Each entry must be a criterion resource name in the form `customers/<cid>/campaignCriteria/<campaign_id>~<criterion_id>`. Call `get_campaign_targeting` first to get the exact resource names for currently-targeted locations.",
      "title": "Locations To Remove"
    },
    "audience_targeting_mode": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign-level audience targeting mode for AUDIENCE dimension: `OBSERVATION` (audience signals only inform reporting and bid adjustments — ads still serve to non-audience users) or `TARGETING` (ads ONLY serve to users in the listed audience segments). OBSERVATION is the default and matches the SOP for most Search campaigns. Switching to TARGETING narrows reach significantly — confirm with user.",
      "title": "Audience Targeting Mode"
    },
    "ai_max_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Ads AI Max toggle on Search campaigns. AI Max uses Google's AI to expand match types and rewrite ads beyond what the advertiser specified. SOPs that require exact-match-only or fixed ad copy should keep this OFF. Pass `false` to disable, `true` to enable. Only affects Search campaigns — ignored on PMax/Display.",
      "title": "Ai Max Enabled"
    },
    "target_partner_search_network": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Search Partner Network toggle. Available only to select Google partner accounts — Google rejects it on non-partner accounts. Pass true/false.",
      "title": "Target Partner Search Network"
    },
    "target_youtube": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "YouTube network toggle (whether ads serve on YouTube). Applies to campaign types that support YouTube delivery. Pass true/false.",
      "title": "Target Youtube"
    },
    "target_google_tv_network": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google TV network toggle. Applies to campaign types that support Google TV. Pass true/false.",
      "title": "Target Google Tv Network"
    },
    "url_expansion_opt_out": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Final URL expansion opt-out (Performance Max / Search). true = ads only send traffic to your exact final URLs; false = Google may expand to other relevant landing pages on your site (the default). Pass true/false.",
      "title": "Url Expansion Opt Out"
    },
    "tracking_url_template": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign-level tracking URL template — a click-measurement/redirect URL (e.g. a third-party click tracker) with ValueTrack params like `{lpurl}?utm_source=google&utm_campaign={campaignid}`. Applies to all ads in the campaign. Pass an empty string \"\" to CLEAR it.",
      "title": "Tracking Url Template"
    },
    "final_url_suffix": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign-level final URL suffix — query params appended to the landing-page URL for tracking (e.g. `utm_source=google&utm_medium=cpc`). Does NOT redirect. Pass an empty string \"\" to CLEAR it.",
      "title": "Final Url Suffix"
    },
    "url_custom_parameters": {
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
      "description": "Campaign-level custom URL parameters — a list of {\"key\",\"value\"} objects usable as `{_key}` in the tracking template (e.g. `[{\"key\":\"season\",\"value\":\"summer\"}]` → `{_season}`). REPLACES the full set; pass `[]` to clear. Keys are lowercase alphanumeric, no braces.",
      "title": "Url Custom Parameters"
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
  "title": "UpdateCampaignInput",
  "type": "object"
}
```

</details>

<a id="update_campaign_dates"></a>

## `update_campaign_dates`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Set a campaign's start and/or end date. Works on ANY campaign type (Search, PMax, Demand Gen, Display).

Dates are 'YYYY-MM-DD'. Pass either or both. Setting an end_date stops the campaign
after that day; omit end_date to leave it open-ended. Use get_campaign_dates to see
current values first.

**Required:** campaign_id + at least one of start_date / end_date.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Set a campaign's start and/or end date. Works on ANY campaign type.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
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
      "description": "Campaign start date, 'YYYY-MM-DD'. Can't be in the past for a not-yet-started campaign.",
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
      "description": "Campaign end date, 'YYYY-MM-DD'. Omit to leave open-ended. Must be after start_date.",
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
      "description": "Google Ads customer ID. Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "UpdateCampaignDatesInput",
  "type": "object"
}
```

</details>

<a id="update_campaign_frequency_caps"></a>

## `update_campaign_frequency_caps`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Set a campaign's frequency caps — limit how often a user sees the ads. Works on ANY campaign type.

This REPLACES the full set of caps (send the complete desired list; pass [] to remove
all caps). Each cap: {level: CAMPAIGN|AD_GROUP|AD_GROUP_AD, event_type: IMPRESSION|VIDEO_VIEW,
time_unit: DAY|WEEK|MONTH, time_length: 1-365, cap: >=1}. Use get_campaign_frequency_caps first.

Example — cap at 3 impressions per user per day:
[{"level":"CAMPAIGN","event_type":"IMPRESSION","time_unit":"DAY","time_length":1,"cap":3}]

**Required:** campaign_id + frequency_caps (list).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "REPLACE a campaign's frequency caps (limit how often a user sees ads). Works on ANY type.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "frequency_caps": {
      "description": "The COMPLETE new list of caps (this REPLACES all existing caps; pass [] to clear). Each cap is an object: {level: CAMPAIGN|AD_GROUP|AD_GROUP_AD, event_type: IMPRESSION|VIDEO_VIEW, time_unit: DAY|WEEK|MONTH, time_length: int 1-365, cap: int >=1}. Example — 3 impressions/user/day: [{\"level\":\"CAMPAIGN\",\"event_type\":\"IMPRESSION\",\"time_unit\":\"DAY\",\"time_length\":1,\"cap\":3}].",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Frequency Caps",
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
      "description": "Google Ads customer ID. Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id",
    "frequency_caps"
  ],
  "title": "UpdateCampaignFrequencyCapsInput",
  "type": "object"
}
```

</details>

<a id="update_conversion_action"></a>

## `update_conversion_action`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update an EXISTING conversion action (change its name, category, status, value, counting, lookback windows, primary flag, whether it counts in Conversions, or attribution model).

Only the fields you pass change — everything else stays as-is. It never removes a conversion action (to pause it, set status=PAUSED, which is reversible).

**Parameters:**
- conversion_action_id: The conversion action to update (REQUIRED). Get it from list_conversion_actions or audit_conversion_tracking.
- Any of: name, category, status (ENABLED/PAUSED), value (+ currency_code, always_use_default_value), counting_type, click_through_lookback_window_days, view_through_lookback_window_days, include_in_conversions_metric, primary_for_goal, attribution_model.
- customer_id: Optional.

**Common uses:**
- "Set the payment-calculator conversion to secondary" → primary_for_goal=false
- "Stop counting Get Directions in Conversions" → include_in_conversions_metric=false
- "Assign $250 to the Lead Submit conversion" → value=250
- "Pause the old duplicate conversion" → status=PAUSED

**Execution time:** 2-4 seconds. Confirm changes with the user first — this changes a live conversion setup.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating an EXISTING conversion action (field-mask).\n\nEvery field except conversion_action_id is optional — only the fields you\nprovide are changed; the rest are left as-is. Reversible for status. Never\nremoves the action.",
  "properties": {
    "conversion_action_id": {
      "description": "The conversion action ID to update. Get it from list_conversion_actions or audit_conversion_tracking.",
      "title": "Conversion Action Id",
      "type": "string"
    },
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
      "description": "New display name.",
      "title": "Name"
    },
    "category": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New category: PURCHASE, SIGNUP, ADD_TO_CART, BEGIN_CHECKOUT, SUBMIT_LEAD_FORM, BOOK_APPOINTMENT, REQUEST_QUOTE, GET_DIRECTIONS, ENGAGEMENT, CONTACT, PHONE_CALL_LEAD, OUTBOUND_CLICK, QUALIFIED_LEAD, CONVERTED_LEAD, DOWNLOAD, PAGE_VIEW, SUBSCRIBE_PAID, IMPORTED_LEAD, STORE_VISIT, STORE_SALE, DEFAULT.",
      "title": "Category"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New status: ENABLED or PAUSED. (This tool never removes a conversion action.)",
      "title": "Status"
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
      "description": "New default conversion value in the ACCOUNT'S currency as a decimal (not cents, not USD). E.g. 50 for 50/lead.",
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
      "description": "3-letter currency code for the value (USD, EUR, ...).",
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
      "default": null,
      "description": "If True, every conversion is worth `value` regardless of what the tag sends. Requires value > 0.",
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
      "default": null,
      "description": "ONE_PER_CLICK (lead-gen) or MANY_PER_CLICK (e-commerce).",
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
      "default": null,
      "description": "1-30.",
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
      "default": null,
      "description": "1-30.",
      "title": "View Through Lookback Window Days"
    },
    "include_in_conversions_metric": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Whether this action counts in the 'Conversions' metric Smart Bidding optimizes toward. NOTE: this can't be changed via the API on an existing action — it's derived from the action's category/goal (and, for GA4-imported conversions, set in Google Analytics). Passing it only produces guidance to change it in the Google Ads UI / GA4; it won't be modified here.",
      "title": "Include In Conversions Metric"
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
      "default": null,
      "description": "Whether this is a primary conversion action for its goal.",
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
      "default": null,
      "description": "Attribution model: GOOGLE_ADS_LAST_CLICK, GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN, GOOGLE_SEARCH_ATTRIBUTION_LINEAR, GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY, GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED, GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK, EXTERNAL.",
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
    "conversion_action_id"
  ],
  "title": "UpdateConversionActionInput",
  "type": "object"
}
```

</details>

<a id="update_demandgen_channel_controls"></a>

## `update_demandgen_channel_controls`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Turn Demand Gen (or YouTube) delivery channels on or off for an ad group.

The 6 channels: youtube_in_stream, youtube_in_feed, youtube_shorts, discover, gmail,
display. Pass only the channels you want to change — the rest keep their current value
(this is a merge, not a replace). At least one channel must stay enabled.

Example: set youtube_shorts=false to stop delivering on Shorts while leaving the rest on.

**Required:** ad_group_id + at least one channel toggle. Only works on Demand Gen ad groups.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Toggle Demand Gen delivery channels on an ad group. Only channels you pass are\nchanged; the rest keep their current value. At least one must stay enabled.",
  "properties": {
    "ad_group_id": {
      "description": "Demand Gen ad group ID (from get_campaign_structure).",
      "title": "Ad Group Id",
      "type": "string"
    },
    "youtube_in_stream": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "YouTube in-stream (skippable/non-skippable) placements.",
      "title": "Youtube In Stream"
    },
    "youtube_in_feed": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "YouTube in-feed (browse/search) placements.",
      "title": "Youtube In Feed"
    },
    "youtube_shorts": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "YouTube Shorts placements.",
      "title": "Youtube Shorts"
    },
    "discover": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Discover feed placements.",
      "title": "Discover"
    },
    "gmail": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Gmail Promotions/Social tab placements.",
      "title": "Gmail"
    },
    "display": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Google Display Network placements.",
      "title": "Display"
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
  "title": "UpdateDemandGenChannelControlsInput",
  "type": "object"
}
```

</details>

<a id="update_display_ad_creative"></a>

## `update_display_ad_creative`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Edit any combination of CREATIVE fields on a Responsive Display Ad.

Complements `update_ad_content` (which handles headlines / descriptions / long_headline / final_urls). This tool handles EVERYTHING ELSE on the RDA.

**Text fields:**
- `business_name` (max 25)
- `main_color` / `accent_color` (hex e.g. '#FFAABB')
- `allow_flexible_color` (bool)
- `price_prefix` (max 10)
- `promo_text` (max 20)
- `call_to_action` (enum label like SHOP_NOW, LEARN_MORE, or free-form ≤30 chars)
- `format_setting` (ALL_FORMATS | NATIVE | NON_NATIVE)

**Image + video fields** (REPLACE the entire list when provided — you may supply both URL objects to upload AND existing asset resource names to reuse; they're merged):
- `marketing_images`: landscape 1.91:1 URLs to upload
- `square_marketing_images`: square 1:1 URLs
- `logo_images`: landscape 4:1 logos
- `square_logo_images`: square 1:1 logos
- `youtube_video_ids`: list of YouTube IDs
- `existing_*_images`: reuse existing asset resource names (from discover_existing_assets)

**Workflow tip** — to add images WITHOUT replacing: first call `get_campaign_structure` or `discover_existing_assets` to get the current resource names, then pass them as `existing_*_images` AND your new ones as `marketing_images`. The service merges them.

**At least one field must be provided.** Any omitted field is not touched.

**Execution time:** 4-10 seconds (includes image uploads if any).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for update_display_ad_creative — all creative fields on a RDA.\n\nAt least one of the creative fields must be provided.\nAny field omitted is not touched.\n\nImage/video fields REPLACE the entire list when provided (both sources\naccept URL objects for new uploads AND resource names for existing assets).",
  "properties": {
    "ad_group_id": {
      "description": "Parent ad group ID.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "ad_id": {
      "description": "RDA (AdGroupAd) ID to update.",
      "title": "Ad Id",
      "type": "string"
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
      "description": "Business name, max 25 chars.",
      "title": "Business Name"
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
      "description": "Hex color like '#RRGGBB' or '#RGB'.",
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
      "description": "Hex color.",
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
      "default": null,
      "description": "Let Google pick optimal colors.",
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
      "description": "Max 10 chars, e.g. 'from'.",
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
      "description": "Max 20 chars, e.g. 'Up to 50% off'.",
      "title": "Promo Text"
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
      "description": "CTA label (SHOP_NOW, LEARN_MORE, etc.) OR free-form ≤30 chars.",
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
      "description": "ALL_FORMATS | NATIVE | NON_NATIVE.",
      "title": "Format Setting"
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
      "description": "Landscape images (1.91:1) to UPLOAD: [{url,name?},...]. Uploads + replaces list.",
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
      "title": "Square Logo Images"
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
      "description": "YouTube video IDs (replace entire video list).",
      "title": "Youtube Video Ids"
    },
    "existing_marketing_images": {
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
      "description": "Reuse existing image asset resource names.",
      "title": "Existing Marketing Images"
    },
    "existing_square_marketing_images": {
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
      "title": "Existing Square Marketing Images"
    },
    "existing_logo_images": {
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
      "title": "Existing Logo Images"
    },
    "existing_square_logo_images": {
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
      "title": "Existing Square Logo Images"
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
      "description": "UUID from `validate_and_prepare_assets`. Pre-validated images auto-replace the ad's image lists. Recommended over passing direct URLs.",
      "title": "Asset Bundle Id"
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
    "ad_group_id",
    "ad_id"
  ],
  "title": "UpdateDisplayAdCreativeInput",
  "type": "object"
}
```

</details>

<a id="update_display_ad_group"></a>

## `update_display_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update one or more editable settings on a Display ad group in a single API call.

At least one of the following must be provided. Any field omitted is not touched.

**Fields:**
- `name`: New ad group name (string)
- `status`: ENABLED | PAUSED | REMOVED (REMOVED is a soft-delete — use `remove_display_ad_group` for clarity)
- `cpc_bid`: Max CPC in account currency (MANUAL_CPC campaigns)
- `cpm_bid`: Max viewable CPM in account currency (MANUAL_CPM campaigns)
- `ad_rotation_mode`: OPTIMIZE (Google picks best ad) | ROTATE_FOREVER (even rotation)
- `optimized_targeting_enabled`: Let Google expand targeting beyond your chosen audiences

Note: `exclude_demographic_expansion` is Search-only and not editable on Display.

**Execution time:** 2-4 seconds.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for update_display_ad_group. At least one field must be set.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID.",
      "title": "Ad Group Id",
      "type": "string"
    },
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
      "description": "New ad group name.",
      "title": "Name"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ENABLED | PAUSED | REMOVED.",
      "title": "Status"
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
      "description": "New max CPC bid in account currency (MANUAL_CPC campaigns).",
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
      "description": "New max viewable CPM bid in account currency (MANUAL_CPM campaigns).",
      "title": "Cpm Bid"
    },
    "ad_rotation_mode": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "OPTIMIZE (Google chooses best ad) or ROTATE_FOREVER (even rotation).",
      "title": "Ad Rotation Mode"
    },
    "optimized_targeting_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Enable Google's optimized targeting expansion. Default Google behavior varies.",
      "title": "Optimized Targeting Enabled"
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
  "title": "UpdateDisplayAdGroupInput",
  "type": "object"
}
```

</details>

<a id="update_display_campaign_schedule"></a>

## `update_display_campaign_schedule`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update a Display campaign's start_date and/or end_date.

Pass either or both dates as 'YYYY-MM-DD' (or compact 'YYYYMMDD'). You must provide at least one.

Notes:
- Google does NOT support un-setting start/end dates via the API. To effectively
  run "forever", set end_date to a far-future date (e.g., 2099-12-31).
- Updating start_date after the campaign has already started is a no-op.

**Execution time:** 2-4 seconds.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for update_display_campaign_schedule.",
  "properties": {
    "campaign_id": {
      "description": "Display campaign ID.",
      "title": "Campaign Id",
      "type": "string"
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
      "description": "New start date, 'YYYY-MM-DD' (or compact 'YYYYMMDD'). Omit to leave unchanged.",
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
      "description": "New end date, 'YYYY-MM-DD'. Omit to leave unchanged.",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "UpdateDisplayCampaignScheduleInput",
  "type": "object"
}
```

</details>

<a id="update_display_demographics"></a>

## `update_display_demographics`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update demographic targeting on a Display ad group via the exclude-the-inverse pattern.

This tool adds NEGATIVE criteria for every demographic value NOT in your target list. It does NOT remove prior negative criteria — use `remove_display_criteria` if you want to clear old exclusions first.

**Input keys** (all optional — only groups you pass are modified):
- `age_ranges`: subset of `AGE_RANGE_18_24, AGE_RANGE_25_34, AGE_RANGE_35_44, AGE_RANGE_45_54, AGE_RANGE_55_64, AGE_RANGE_65_UP, AGE_RANGE_UNDETERMINED`
- `genders`: subset of `MALE, FEMALE, UNDETERMINED`
- `parental_statuses`: subset of `PARENT, NOT_A_PARENT, UNDETERMINED`
- `income_ranges`: subset of `INCOME_RANGE_0_50, INCOME_RANGE_50_60, INCOME_RANGE_60_70, INCOME_RANGE_70_80, INCOME_RANGE_80_90, INCOME_RANGE_90_UP, INCOME_RANGE_UNDETERMINED`

**Example — target women aged 25-44 only:**
```
demographics: {
  "age_ranges": ["AGE_RANGE_25_34","AGE_RANGE_35_44"],
  "genders": ["FEMALE"]
}
```

**Execution time:** 2-5 seconds.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_group_id": {
      "description": "Target Display ad group ID.",
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
    },
    "demographics": {
      "additionalProperties": {
        "items": {
          "type": "string"
        },
        "type": "array"
      },
      "description": "Keys: age_ranges (AGE_RANGE_18_24..AGE_RANGE_65_UP, AGE_RANGE_UNDETERMINED), genders (MALE, FEMALE, UNDETERMINED), parental_statuses (PARENT, NOT_A_PARENT, UNDETERMINED), income_ranges (INCOME_RANGE_0_50..INCOME_RANGE_90_UP, INCOME_RANGE_UNDETERMINED). Google targets via exclude-the-inverse: we add NEGATIVE criteria for everything NOT listed.",
      "title": "Demographics",
      "type": "object"
    }
  },
  "required": [
    "ad_group_id",
    "demographics"
  ],
  "title": "UpdateDisplayDemographicsInput",
  "type": "object"
}
```

</details>

<a id="update_display_frequency_caps"></a>

## `update_display_frequency_caps`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

REPLACE all frequency caps on a Display campaign.

Google requires sending the full desired set each time — partial updates are not supported. Pass [] to remove ALL caps.

**Each entry:**
- `level`: CAMPAIGN | AD_GROUP | AD_GROUP_AD
- `event_type`: IMPRESSION | VIDEO_VIEW
- `time_unit`: DAY | WEEK | MONTH
- `time_length`: 1-365 (number of time_unit periods)
- `cap`: ≥ 1 (max events per user in that window)

**Examples:**
- 3 impressions/day: `[{level:CAMPAIGN, event_type:IMPRESSION, time_unit:DAY, time_length:1, cap:3}]`
- 10 impressions/week + 2/day: two entries in the list
- Clear all caps: `[]`

**Execution time:** 2-5 seconds.

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "DisplayFrequencyCapEntry": {
      "description": "Shape of a single frequency cap entry.",
      "properties": {
        "level": {
          "description": "CAMPAIGN | AD_GROUP | AD_GROUP_AD",
          "title": "Level",
          "type": "string"
        },
        "event_type": {
          "description": "IMPRESSION | VIDEO_VIEW",
          "title": "Event Type",
          "type": "string"
        },
        "time_unit": {
          "description": "DAY | WEEK | MONTH",
          "title": "Time Unit",
          "type": "string"
        },
        "time_length": {
          "description": "Number of time_unit periods (1-365).",
          "maximum": 365,
          "minimum": 1,
          "title": "Time Length",
          "type": "integer"
        },
        "cap": {
          "description": "Max events per user in the time window.",
          "minimum": 1,
          "title": "Cap",
          "type": "integer"
        }
      },
      "required": [
        "level",
        "event_type",
        "time_unit",
        "time_length",
        "cap"
      ],
      "title": "DisplayFrequencyCapEntry",
      "type": "object"
    }
  },
  "description": "Input for update_display_frequency_caps — REPLACES all caps on the campaign.",
  "properties": {
    "campaign_id": {
      "description": "Display campaign ID.",
      "title": "Campaign Id",
      "type": "string"
    },
    "frequency_caps": {
      "description": "New set of frequency caps to apply. Pass [] to clear ALL caps. Google requires you to send the complete desired set each time.",
      "items": {
        "$ref": "#/$defs/DisplayFrequencyCapEntry"
      },
      "title": "Frequency Caps",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id",
    "frequency_caps"
  ],
  "title": "UpdateDisplayFrequencyCapsInput",
  "type": "object"
}
```

</details>

<a id="update_keyword"></a>

## `update_keyword`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update keyword bid or status.

**Parameters:**
- keyword_id: The keyword to update (REQUIRED - get from get_campaign_structure)
- ad_group_id: The ad group containing the keyword (REQUIRED)
- cpc_bid_micros: New bid in micros (1 USD = 1,000,000). Example: 2500000 = $2.50
- status: ENABLED or PAUSED
- customer_id: Optional

**Can update:**
- Bid amount (cpc_bid_micros)
- Status (ENABLED/PAUSED)

**CANNOT update (immutable):**
- Keyword text
- Match type

**Execution time:** 2-3 seconds

**Example:**
User: "Increase the bid on 'running shoes' to $3"
Agent:
1. Uses get_campaign_structure to find the keyword_id
2. Uses update_keyword with cpc_bid_micros=3000000

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating a keyword",
  "properties": {
    "keyword_id": {
      "description": "The keyword ID to update. Use get_campaign_structure to find this.",
      "title": "Keyword Id",
      "type": "string"
    },
    "ad_group_id": {
      "description": "The ad group ID the keyword belongs to.",
      "title": "Ad Group Id",
      "type": "string"
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
      "description": "New bid in micros (1 USD = 1,000,000 micros). Example: 2500000 for $2.50",
      "title": "Cpc Bid Micros"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New status: ENABLED or PAUSED",
      "title": "Status"
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
    "keyword_id",
    "ad_group_id"
  ],
  "title": "UpdateKeywordInput",
  "type": "object"
}
```

</details>

<a id="update_location_targeting"></a>

## `update_location_targeting`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Change a campaign's location-targeting MODE without recreating the campaign.

This is the "Presence vs Presence-or-Interest" toggle. It controls *who* sees ads inside the campaign's existing location list — it does NOT change the location list itself (use targeting tools for that).

**Modes:**
- PRESENCE (recommended for performance): People physically in or regularly in the targeted locations
- PRESENCE_OR_INTEREST (Google's default): People in OR interested in the locations (broader; can waste budget on out-of-area users)
- SEARCH_INTEREST: People searching for the location (Search campaigns only)

**When to use:**
- Customer says "my ads are showing to people not in my target area" → switch to PRESENCE
- Local-only business (medical, restaurants, services) → PRESENCE
- Brand-awareness or interest-based reach → keep PRESENCE_OR_INTEREST

**Channel-type rules (auto-enforced):**
- Display: rejects negative=PRESENCE_OR_INTEREST. Tool auto-defaults negative to PRESENCE if omitted.
- Display: rejects positive=SEARCH_INTEREST.
- Search/PMax: all combinations supported.

**Parameters:**
- campaign_id: Campaign to update (REQUIRED)
- positive_geo_target_type: PRESENCE, PRESENCE_OR_INTEREST, or SEARCH_INTEREST (REQUIRED)
- negative_geo_target_type: PRESENCE or PRESENCE_OR_INTEREST (OPTIONAL — leave existing untouched if omitted, except Display where we force PRESENCE)

**Example:**
User: "My Display campaign is showing to people not in my city, fix it."
Agent:
1. Confirms: "I'll switch the location targeting to 'People physically in your locations' (PRESENCE). Proceed?"
2. Calls update_location_targeting(campaign_id, positive_geo_target_type='PRESENCE')

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating campaign location-targeting MODE.\n\nThis controls *who* sees ads inside the campaign's location list:\n- PRESENCE: People physically in the location (recommended for performance)\n- PRESENCE_OR_INTEREST: People in OR interested in the location (default; broader)\n- SEARCH_INTEREST: People searching for the location (Search-only; rejected on Display)\n\nDistinct from add_display_locations / update_campaign_location_targeting,\nwhich manage the *list* of targeted geo IDs. This tool only flips the mode.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to update. Use list_campaigns first to get available campaign IDs.",
      "title": "Campaign Id",
      "type": "string"
    },
    "positive_geo_target_type": {
      "description": "Location targeting mode for inclusions: PRESENCE (physically in), PRESENCE_OR_INTEREST (in or interested in), or SEARCH_INTEREST (searching for; Search campaigns only). For most performance campaigns, PRESENCE is recommended over the default PRESENCE_OR_INTEREST.",
      "title": "Positive Geo Target Type",
      "type": "string"
    },
    "negative_geo_target_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional. Mode for location *exclusions*: PRESENCE (physically in) or PRESENCE_OR_INTEREST (in or interested in). Display campaigns only accept PRESENCE; if omitted on a Display campaign we force PRESENCE.",
      "title": "Negative Geo Target Type"
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
    "campaign_id",
    "positive_geo_target_type"
  ],
  "title": "UpdateLocationTargetingInput",
  "type": "object"
}
```

</details>

<a id="update_meta_ad"></a>

## `update_meta_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to update an individual Meta ad — pause/resume it, rename it, or swap its creative.

IMPORTANT: This tool modifies REAL ads in Meta Ads Manager. Changes take effect immediately.

Returns:
- Confirmation of updates applied
- Summary of changes
- Ads Manager URL for the ad

When to use this tool:
- "Pause this ad"
- "Resume ad [ID]"
- "Rename this ad"
- "Swap the creative on this ad"
- "Change the image on this ad" (via creative swap)
- "Turn off the underperforming ad"

Parameters:
- ad_id: The Meta Ad ID to update (required)
- status: ACTIVE, PAUSED, DELETED, ARCHIVED (optional)
- name: New ad name (optional)
- creative_id: New creative ID for creative swap (optional)

At least one update field must be provided.

Execution time: 2-5 seconds
Modifies: Real ad in Meta Ads

Workflow for creative swap:
1. Use `discover_meta_assets` to find existing images/creatives
2. Get the creative ID you want to use
3. Use `update_meta_ad` with `creative_id` to swap

Workflow for pausing underperformers:
1. Use `analyze_meta_ad_performance` to identify underperforming ads
2. Use `list_meta_ads` to get ad IDs
3. Use `update_meta_ad` with `status=PAUSED`

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating a Meta ad.\n\nSupported fields: status, name, creative_id.\n\nNOT supported here: primary_text, headline, description, call_to_action_type.\nMeta does not allow editing creative text fields in-place. To change ad copy or CTA,\ncreate a new ad with the updated text using add_meta_ad, then pause the old ad.",
  "properties": {
    "ad_id": {
      "description": "**REQUIRED.** The Meta Ad ID to update. If you don't have it, call `list_meta_ads` first. You MUST also provide at least one update field (status, name, or creative_id) — do NOT call this tool with only an ad_id and no changes. Note: ad copy (primary_text, headline, CTA) cannot be edited in-place. To change those, use add_meta_ad to create a new ad, then pause the old one.",
      "title": "Ad Id",
      "type": "string"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New status: 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'",
      "title": "Status"
    },
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
      "description": "New ad name",
      "title": "Name"
    },
    "creative_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New creative ID for creative swap. Use this to replace the ad's creative with an existing creative.",
      "title": "Creative Id"
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
      "description": "URL parameters (e.g. 'utm_source=meta&utm_campaign=2026q2') applied to the ad. Set on the Ad object directly — no creative swap needed. Leading '?' stripped.",
      "title": "Url Tags"
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
      "description": "Update Meta's multi-advertiser ad format enrollment on this ad's creative. Set false to opt out, true to opt in. Triggers a creative swap (the existing creative is cloned with the new contextual_multi_ads setting and the ad's creative_id is swapped). May reset Meta's learning phase for ~3-7 days.",
      "title": "Multi Advertiser"
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
    "ad_id"
  ],
  "title": "UpdateMetaAdInput",
  "type": "object"
}
```

</details>

<a id="update_meta_ad_set"></a>

## `update_meta_ad_set`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to edit an existing Meta ad set's targeting, budget, bid, placements, schedule, or optimization settings.

IMPORTANT: This tool modifies REAL ad sets in Meta Ads Manager. Changes take effect immediately.

This is the primary tool for:
- Changing audience targeting (age, gender, interests, locations)
- Excluding placements (e.g., remove Audience Network)
- Adjusting budgets at the ad set level
- Changing bid amounts
- Pausing/resuming specific ad sets
- Modifying optimization goals

Returns:
- Confirmation of updates applied
- Summary of all changes made
- Ads Manager URL for the ad set

When to use this tool:
- "Change the targeting on my ad set"
- "Exclude Audience Network from placements"
- "Update the budget on this ad set to $50/day"
- "Pause this ad set"
- "Change the age range to 25-45"
- "Add interest targeting for fitness"
- "Exclude custom audience from this ad set"
- "Change bid to $5"
- "Update the optimization goal"

Parameters:
- ad_set_id: The Meta Ad Set ID to update (required)
- status: ACTIVE, PAUSED, DELETED, ARCHIVED (optional)
- name: New ad set name (optional)
- daily_budget: New daily budget in the account's own currency, NOT cents, NOT USD (for 20/day send 20, not 2000; optional, min 1). DO NOT use for CBO campaigns.
- lifetime_budget: New lifetime budget in the account's own currency, NOT cents, NOT USD (optional). DO NOT use for CBO campaigns.
- daily_min_spend_target: CBO only — minimum daily spend for this ad set (use INSTEAD of daily_budget)
- daily_spend_cap: CBO only — maximum daily spend cap for this ad set (use INSTEAD of daily_budget)
- lifetime_min_spend_target: CBO only — minimum lifetime spend (for lifetime budget CBO)
- lifetime_spend_cap: CBO only — maximum lifetime spend cap (for lifetime budget CBO)
- bid_amount: New bid amount in the account's own currency, NOT cents, NOT USD (for a 2.50 bid send 2.5, not 250) (optional)
- targeting: New targeting spec as JSON (optional) — for placements, audiences, demographics
- start_time: New start time ISO format (optional)
- end_time: New end time ISO format (optional)
- optimization_goal: REACH, LINK_CLICKS, LANDING_PAGE_VIEWS, OFFSITE_CONVERSIONS, VALUE, etc. (optional)

**CBO (Advantage Campaign Budget) campaigns:**
For ad sets under CBO campaigns, do NOT set daily_budget or lifetime_budget.
Use daily_min_spend_target / daily_spend_cap to control spend distribution.
Setting daily_budget on a CBO ad set will cause Meta to reject with an error.

At least one update field must be provided.

Targeting Spec Examples:

*Exclude Audience Network:*
```json
{
  "publisher_platforms": ["facebook", "instagram"],
  "facebook_positions": ["feed", "stories", "reels"],
  "instagram_positions": ["stream", "story", "reels"]
}
```

*Change age and gender:*
```json
{
  "age_min": 25,
  "age_max": 45,
  "genders": [1]
}
```
(genders: 1=male, 2=female, omit for all)

*Add interest targeting:*
```json
{
  "flexible_spec": [{"interests": [{"id": "6003139266461", "name": "Fitness"}]}]
}
```

*Exclude custom audience:*
```json
{
  "excluded_custom_audiences": [{"id": "AUDIENCE_ID"}]
}
```

Execution time: 2-5 seconds
Modifies: Real ad set in Meta Ads

Workflow:
1. Use `list_meta_ad_sets` or `get_meta_campaign_details` to find the ad set ID
2. Use `update_meta_ad_set` with the changes you want to make
3. Verify changes in Ads Manager

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating a Meta ad set",
  "properties": {
    "ad_set_id": {
      "description": "**REQUIRED.** The Meta Ad Set ID to update. If you don't have it, call `list_meta_ad_sets` first. You MUST also provide at least one update field (status, name, daily_budget, etc.) — do NOT call this tool with only an ad_set_id and no changes.",
      "title": "Ad Set Id",
      "type": "string"
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
      "description": "Click-to-WhatsApp ad sets only. Change WHICH WhatsApp number receives the conversations, as displayed on the Page (e.g. '+55 51 99999-0000'). Use this when a WhatsApp campaign is routing to the wrong number. The ad set's other destination settings (the linked Page) are preserved.",
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
      "description": "Click-to-WhatsApp ad sets only. Alternative to whatsapp_phone_number: the WhatsApp Business phone-number ID from Meta Business Settings. Names the same destination — pass either one, not both.",
      "title": "Whatsapp Phone Number Id"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New status: 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED'",
      "title": "Status"
    },
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
      "description": "New ad set name",
      "title": "Name"
    },
    "daily_budget": {
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
      "description": "New daily budget in the ad account's OWN CURRENCY as a decimal — NOT cents, and NOT converted to USD. For 20/day send 20, not 2000 (the tool converts to Meta's internal unit for you; sending cents books a 100x budget).",
      "title": "Daily Budget"
    },
    "lifetime_budget": {
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
      "description": "New lifetime budget in the ad account's OWN CURRENCY as a decimal — NOT cents, and NOT converted to USD. For a 500 total send 500, not 50000.",
      "title": "Lifetime Budget"
    },
    "bid_amount": {
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
      "description": "New bid amount in the ad account's OWN CURRENCY as a decimal — NOT cents, and NOT converted to USD. For a 2.50 bid send 2.5, not 250.",
      "title": "Bid Amount"
    },
    "targeting": {
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
      "description": "New targeting specification as a JSON object. Use this for placement exclusions, audience exclusions, age/gender changes, and interest targeting updates. For LOCATION changes prefer the `locations` / `location_types` params below — they build Meta's geo_locations correctly (city keys + radius + reach mode) and merge onto the ad set's existing targeting so the rest isn't wiped.",
      "title": "Targeting"
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
      "description": "Replace the ad set's location targeting. Country codes (['US','BR']) or location objects from search_meta_targeting ([{'key':'2344821','type':'city','radius':20,'distance_unit':'kilometer'}]). ALWAYS include the 'type' field on each object (city/region/zip/place) — a key with no type is treated as a country code and rejected by Meta. Merged onto current targeting (other targeting is preserved).",
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
      "description": "DEPRECATED — do not set. Meta removed the location-targeting reach-mode ('people living in' / 'recently in' / 'travelling in'); all ad sets now reach 'people living in or recently in' the selected locations, and sending any location_types value now makes Meta reject the ad set. Leave unset; any value is ignored. If an existing ad set is blocked at publish for a removed location option, edit its locations (pass `locations`) to re-save the audience.",
      "title": "Location Types"
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
      "description": "EU Digital Services Act beneficiary (advertiser's business/legal name). REQUIRED by Meta when the ad set targets any EU/EEA country. Set this if a campaign-create or targeting update failed with 'No advertiser indicated' / DSA beneficiary required. Example: 'Acme Inc'.",
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
      "description": "EU DSA payor — the entity paying. Optional; defaults to dsa_beneficiary.",
      "title": "Dsa Payor"
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
      "description": "Advantage+ Audience on/off. Toggle Meta's AI audience expansion without replacing the rest of the ad set's targeting. When provided, merges into targeting.targeting_automation.advantage_audience (0/1). Pass True to enable, False to disable. Leave unset to keep existing value.",
      "title": "Advantage Audience"
    },
    "start_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New start time in ISO format YYYY-MM-DDTHH:MM:SS",
      "title": "Start Time"
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
      "description": "New end time in ISO format YYYY-MM-DDTHH:MM:SS",
      "title": "End Time"
    },
    "optimization_goal": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New optimization goal. Web/general values: REACH, IMPRESSIONS, LINK_CLICKS, LANDING_PAGE_VIEWS, OFFSITE_CONVERSIONS, VALUE, POST_ENGAGEMENT, LEAD_GENERATION. App-campaign values (only valid when parent campaign objective=OUTCOME_APP_PROMOTION): APP_INSTALLS (default), APP_INSTALLS_AND_OFFSITE_CONVERSIONS (combined goal), OFFSITE_CONVERSIONS (in-app events), IN_APP_VALUE (value optimization for in-app events), VALUE.",
      "title": "Optimization Goal"
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
      "description": "Update the Facebook App ID on the ad-set promoted_object. Numeric only — NOT iOS bundle ID or Android package name. Use to swap the promoted app on an existing OUTCOME_APP_PROMOTION ad set (e.g. relaunching with a new app version that has a different FB App ID).",
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
      "description": "Update the App Store / Play Store URL on the ad-set promoted_object. Examples: 'https://apps.apple.com/us/app/example/id123456789' or 'https://play.google.com/store/apps/details?id=com.example'. The ad set's OS targeting is realigned to match automatically.",
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
      "description": "Operating system to target: 'iOS' or 'Android'. Usually OMIT — when you change app_store_url the OS targeting is realigned automatically. Set this only to deliberately override that.",
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
      "description": "Update the in-app event type for OUTCOME_APP_PROMOTION optimization. Pass 'APP_INSTALLS' to revert to install optimization (clears custom_event_type so Meta uses optimization_goal). Pass a specific event (PURCHASE, LEVEL_ACHIEVED, COMPLETE_REGISTRATION, START_TRIAL, etc.) to optimize for in-app actions. Requires Meta SDK to fire the event from the app.",
      "title": "App Event Type"
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
      "description": "Minimum daily spend target in account currency for CBO campaigns. Use this instead of daily_budget when the campaign uses Advantage Campaign Budget. Set to 0 to remove the minimum.",
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
      "description": "Maximum daily spend cap in account currency for CBO campaigns. Use this instead of daily_budget when the campaign uses Advantage Campaign Budget. Set to 0 to remove the cap.",
      "title": "Daily Spend Cap"
    },
    "lifetime_min_spend_target": {
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
      "description": "Minimum lifetime spend target in account currency for CBO campaigns with lifetime budget.",
      "title": "Lifetime Min Spend Target"
    },
    "lifetime_spend_cap": {
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
      "description": "Maximum lifetime spend cap in account currency for CBO campaigns with lifetime budget.",
      "title": "Lifetime Spend Cap"
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
      "description": "Ad-set-level URL parameters (e.g. 'utm_source=meta&utm_medium=cpc'). Applied to every ad in this ad set. Leading '?' stripped.",
      "title": "Url Tags"
    }
  },
  "required": [
    "ad_set_id"
  ],
  "title": "UpdateMetaAdSetInput",
  "type": "object"
}
```

</details>

<a id="update_meta_campaign"></a>

## `update_meta_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to update an existing Meta campaign's status, budget, name, or schedule.

IMPORTANT: This tool modifies REAL campaigns in Meta Ads Manager. Changes take effect immediately.

Returns:
- Confirmation of updates applied
- Updated campaign details
- Ads Manager URL

When to use this tool:
- "Update my Meta campaign budget"
- "Change my Facebook campaign name"
- "Pause my Instagram campaign"
- "Resume my paused campaign"
- "Set a new budget for campaign X"
- "Change the end date for my campaign"

Parameters:
- campaign_id: The Meta Campaign ID to update (required)
- status: New status - 'ACTIVE', 'PAUSED' (optional)
- name: New campaign name (optional)
- daily_budget: New daily budget in the account's own currency, NOT cents, NOT USD (for 20/day send 20, not 2000) (optional)
- lifetime_budget: New lifetime budget in the account's own currency, NOT cents, NOT USD (optional)
- start_time: New start time in ISO format (optional)
- stop_time: New stop time in ISO format (optional)
- bid_strategy: Campaign bidding strategy (optional) — 'LOWEST_COST_WITHOUT_CAP',
  'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', or 'LOWEST_COST_WITH_MIN_ROAS'.
  The capped strategies need a bid cap on the ad sets (`bid_amount` via
  update_meta_ad_set) — set that first or Meta rejects the change.

At least one update field must be provided.

Execution time: 2-5 seconds
Modifies: Real campaign in Meta Ads

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating a Meta campaign",
  "properties": {
    "campaign_id": {
      "description": "**REQUIRED.** The Meta Campaign ID to update. If you don't have it, call `list_meta_campaigns` first. You MUST also provide at least one update field (status, name, daily_budget, lifetime_budget, start_time, stop_time, or bid_strategy) — do NOT call this tool with only a campaign_id and no changes. Note: objective cannot be changed after creation; targeting and optimization_goal live at the ad set level (use `update_meta_ad_set`).",
      "title": "Campaign Id",
      "type": "string"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New status: 'ACTIVE', 'PAUSED' (optional)",
      "title": "Status"
    },
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
      "description": "New campaign name (optional)",
      "title": "Name"
    },
    "daily_budget": {
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
      "description": "New daily budget in the ad account's OWN CURRENCY as a decimal — NOT cents, and NOT converted to USD. For 20/day send 20, not 2000 (the tool converts to Meta's internal unit for you; sending cents books a 100x budget).",
      "title": "Daily Budget"
    },
    "lifetime_budget": {
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
      "description": "New lifetime budget in the ad account's OWN CURRENCY as a decimal — NOT cents, and NOT converted to USD. For a 500 total send 500, not 50000.",
      "title": "Lifetime Budget"
    },
    "start_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New start time in ISO format YYYY-MM-DDTHH:MM:SS (optional)",
      "title": "Start Time"
    },
    "stop_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New stop time in ISO format YYYY-MM-DDTHH:MM:SS (optional)",
      "title": "Stop Time"
    },
    "bid_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign bidding strategy (optional). One of: 'LOWEST_COST_WITHOUT_CAP' (automatic bidding, Meta's default), 'LOWEST_COST_WITH_BID_CAP' (manual bid cap), 'COST_CAP' (target cost per result), 'LOWEST_COST_WITH_MIN_ROAS' (ROAS floor). NOTE: the capped strategies need a bid cap on the ad sets — set `bid_amount` via update_meta_ad_set first. Bid strategy applies at the campaign level for CBO campaigns; ABO campaigns carry it on the ad set.",
      "title": "Bid Strategy"
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
  "title": "UpdateMetaCampaignInput",
  "type": "object"
}
```

</details>

<a id="update_meta_catalog_ad"></a>

## `update_meta_catalog_ad`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to edit/change an existing catalog AD — rename, pause/activate, swap to another creative, or change the copy/headline/description/CTA/landing/product-set (Meta rebuilds the creative since creatives are immutable). Only the fields you pass change.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "DEEP update of a catalog AD — rename/pause, swap to an existing creative, or\nchange the copy/CTA/product-set/landing (Meta rebuilds the creative).",
  "properties": {
    "ad_id": {
      "description": "The catalog ad ID to update (required).",
      "title": "Ad Id",
      "type": "string"
    },
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
      "description": "New ad name.",
      "title": "Name"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ACTIVE, PAUSED, or ARCHIVED.",
      "title": "Status"
    },
    "creative_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Swap to an existing creative ID (no rebuild).",
      "title": "Creative Id"
    },
    "primary_text": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "New primary text (rebuilds the creative).",
      "title": "Primary Text"
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
      "description": "New headline (rebuilds the creative).",
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
      "description": "New description (rebuilds the creative).",
      "title": "Description"
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
      "description": "New CTA button type (rebuilds the creative).",
      "title": "Call To Action"
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
      "description": "New storefront URL (rebuilds the creative).",
      "title": "Landing Page Url"
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
      "description": "Product set for the rebuilt creative (required when rebuilding).",
      "title": "Product Set Id"
    },
    "product_catalog_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Catalog ID (used to derive a storefront link when rebuilding without landing_page_url).",
      "title": "Product Catalog Id"
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
      "description": "UTM-style URL parameters (rebuilds the creative).",
      "title": "Url Tags"
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
      "description": "Facebook Page ID (auto-detected if rebuilding the creative). If the account has 2+ Pages, pass the one you want; call list_meta_pages to see options.",
      "title": "Facebook Page Id"
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
      "description": "Meta ad account ID. Auto-detected if omitted.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "UpdateMetaCatalogAdInput",
  "type": "object"
}
```

</details>

<a id="update_meta_catalog_ad_set"></a>

## `update_meta_catalog_ad_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to edit/change an existing catalog AD SET — deep control: budget, bid amount/strategy, optimization goal, full targeting (geo/age/gender/interests/behaviors/custom audiences/placements), schedule/dayparting, frequency caps, attribution, destination. PLUS catalog-specific: swap the product set, change the conversion event, or change the RETARGETING window/events (rebuilds the product audience). Only the fields you pass change.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "DEEP update of a catalog AD SET — every Meta-editable lever plus catalog-aware\nchanges (swap product set, change retention window / events for retargeting, change\nthe conversion event). Only the fields you pass are changed.",
  "properties": {
    "ad_set_id": {
      "description": "The catalog ad set ID to update (required).",
      "title": "Ad Set Id",
      "type": "string"
    },
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
      "description": "New ad set name.",
      "title": "Name"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ACTIVE, PAUSED, or ARCHIVED.",
      "title": "Status"
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Daily budget in the account's own currency as a decimal — NOT cents, NOT USD (for 20/day send 20, not 2000).",
      "title": "Daily Budget"
    },
    "lifetime_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime budget in the account's own currency as a decimal — NOT cents, NOT USD (can't switch budget type after creation).",
      "title": "Lifetime Budget"
    },
    "bid_amount": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Bid amount in the account's own currency as a decimal — NOT cents, NOT USD (for bid-cap/cost-cap strategies).",
      "title": "Bid Amount"
    },
    "bid_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, LOWEST_COST_WITH_MIN_ROAS, COST_CAP.",
      "title": "Bid Strategy"
    },
    "daily_min_spend_target": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO: min daily spend for this ad set, in the account's own currency as a decimal — NOT cents, NOT USD.",
      "title": "Daily Min Spend Target"
    },
    "daily_spend_cap": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO: max daily spend for this ad set, in the account's own currency as a decimal — NOT cents, NOT USD.",
      "title": "Daily Spend Cap"
    },
    "lifetime_min_spend_target": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO: min lifetime spend for this ad set, in the account's own currency as a decimal — NOT cents, NOT USD.",
      "title": "Lifetime Min Spend Target"
    },
    "lifetime_spend_cap": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO: max lifetime spend for this ad set, in the account's own currency as a decimal — NOT cents, NOT USD.",
      "title": "Lifetime Spend Cap"
    },
    "pacing_type": {
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
      "description": "e.g. ['standard'].",
      "title": "Pacing Type"
    },
    "optimization_goal": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "OFFSITE_CONVERSIONS (default for catalog sales), VALUE (ROAS), LINK_CLICKS, LANDING_PAGE_VIEWS, etc.",
      "title": "Optimization Goal"
    },
    "billing_event": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "IMPRESSIONS (default) or LINK_CLICKS.",
      "title": "Billing Event"
    },
    "attribution_spec": {
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
      "description": "Conversion attribution windows.",
      "title": "Attribution Spec"
    },
    "start_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Ad set start time (ISO 8601).",
      "title": "Start Time"
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
      "description": "Ad set end time (ISO 8601).",
      "title": "End Time"
    },
    "adset_schedule": {
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
      "description": "Dayparting schedule (list of day/hour windows).",
      "title": "Adset Schedule"
    },
    "frequency_control_specs": {
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
      "description": "Frequency caps.",
      "title": "Frequency Control Specs"
    },
    "targeting": {
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
      "description": "Full Meta targeting spec to REPLACE current targeting (geo_locations, age_min/max, genders, interests, behaviors, custom_audiences, excluded_custom_audiences, publisher_platforms, etc.).",
      "title": "Targeting"
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
      "description": "WEBSITE or FACEBOOK.",
      "title": "Destination Type"
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
      "description": "Swap the product set this ad set promotes.",
      "title": "Product Set Id"
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
      "description": "Change/set the pixel in the promoted object.",
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
      "description": "Change the conversion event (custom_event_type), e.g. PURCHASE, ADD_TO_CART.",
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
      "description": "Rebuild the retargeting audience: viewed_not_purchased | carted_not_purchased | all_engaged_not_purchased | cross_sell_purchasers | custom.",
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
      "description": "Change the retargeting lookback window (days).",
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
      "description": "custom preset: pixel events to include.",
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
      "description": "custom preset: pixel events to exclude.",
      "title": "Exclude Events"
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
      "description": "EU DSA beneficiary.",
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
      "description": "EU DSA payor.",
      "title": "Dsa Payor"
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
      "description": "Meta ad account ID. Auto-detected if omitted.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "ad_set_id"
  ],
  "title": "UpdateMetaCatalogAdSetInput",
  "type": "object"
}
```

</details>

<a id="update_meta_catalog_campaign"></a>

## `update_meta_catalog_campaign`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to edit/change an existing Advantage+ Catalog CAMPAIGN — rename, pause/activate/archive, change budget (CBO), spend cap, bid strategy, schedule, special ad categories, or swap the catalog. Only the fields you pass are changed.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "DEEP update of an Advantage+ Catalog CAMPAIGN — every Meta-editable lever.\nOnly the fields you pass are changed; the rest stay as-is.",
  "properties": {
    "campaign_id": {
      "description": "The catalog campaign ID to update (required).",
      "title": "Campaign Id",
      "type": "string"
    },
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
      "description": "New campaign name.",
      "title": "Name"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ACTIVE, PAUSED, or ARCHIVED.",
      "title": "Status"
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO daily budget in the account's own currency as a decimal — NOT cents, NOT USD (e.g. 50.0).",
      "title": "Daily Budget"
    },
    "lifetime_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "CBO lifetime budget in the account's own currency as a decimal — NOT cents, NOT USD.",
      "title": "Lifetime Budget"
    },
    "spend_cap": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Lifetime spend cap in the ad account's OWN CURRENCY as a decimal — NOT cents, NOT USD (Meta minimum applies, e.g. 100).",
      "title": "Spend Cap"
    },
    "bid_strategy": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, LOWEST_COST_WITH_MIN_ROAS, or COST_CAP.",
      "title": "Bid Strategy"
    },
    "pacing_type": {
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
      "description": "e.g. ['standard'] or ['no_pacing'].",
      "title": "Pacing Type"
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
      "description": "HOUSING/EMPLOYMENT/CREDIT/etc.",
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
    "start_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign start time (ISO 8601).",
      "title": "Start Time"
    },
    "stop_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Campaign stop time (ISO 8601).",
      "title": "Stop Time"
    },
    "is_adset_budget_sharing_enabled": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Advantage campaign budget sharing across ad sets.",
      "title": "Is Adset Budget Sharing Enabled"
    },
    "product_catalog_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Swap the catalog this campaign advertises (replaces the campaign's catalog).",
      "title": "Product Catalog Id"
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
      "description": "Meta ad account ID. Auto-detected if omitted.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "UpdateMetaCatalogCampaignInput",
  "type": "object"
}
```

</details>

<a id="update_pmax_asset_group"></a>

## `update_pmax_asset_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update settings of an existing PMax asset group.

Per-field isolation: only the fields you pass change. Supported fields:
- **status**: ENABLED / PAUSED (pause a group without touching the campaign)
- **name**: rename the group
- **final_urls / final_mobile_urls**: replace the landing page URL list
- **path1 / path2**: display URL paths (empty string clears)

**Use when:**
- "Pause the summer asset group" → status=PAUSED
- "Point the sale group at the new landing page" → final_urls

**Parameters:**
- campaign_id: The PMax campaign ID (REQUIRED)
- asset_group_id: Required if the campaign has 2+ groups (from get_pmax_asset_groups)
- name / status / final_urls / final_mobile_urls / path1 / path2: at least one
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-4 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating an asset group's settings.",
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
      "description": "Required when the campaign has more than one asset group. Auto-resolved when there is exactly one. Get IDs from get_pmax_asset_groups.",
      "title": "Asset Group Id"
    },
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
      "description": "New asset group name.",
      "title": "Name"
    },
    "status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "ENABLED or PAUSED. Use remove_pmax_asset_group to remove.",
      "title": "Status"
    },
    "final_urls": {
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
      "description": "Replacement landing page URL list (replaces the whole list).",
      "title": "Final Urls"
    },
    "final_mobile_urls": {
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
      "description": "Replacement mobile landing page URL list.",
      "title": "Final Mobile Urls"
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
      "description": "Display URL path segment 1 (max 15 chars). Pass empty string to clear.",
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
      "description": "Display URL path segment 2 (max 15 chars, requires path1). Pass empty string to clear.",
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
    "campaign_id"
  ],
  "title": "UpdatePMaxAssetGroupInput",
  "type": "object"
}
```

</details>

<a id="update_pmax_audience_signal"></a>

## `update_pmax_audience_signal`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Update the segment composition of an existing PMax audience IN PLACE (#325).

USE THIS INSTEAD OF REMOVE + ADD when you want to change which audiences
are in a signal — for example, to merge in a new Customer Match list while
keeping existing in-market interests. Updating in place avoids the
"audience with this name already exists" error that comes from removing a
signal and re-adding under the same name.

**Workflow:**
1. Call get_pmax_audience_signals → returns signals with their `audience`
   resource names AND current `composition`
2. Build a new audience_config dict with the FULL desired composition
   (this REPLACES, not merges — copy the current composition then add or
   remove segments as needed)
3. Call this tool with the audience_resource_name + new audience_config

**Parameters:**
- audience_resource_name: from get_pmax_audience_signals (the `audience`
  field on each signal — NOT the signal's own resource_name)
- audience_config: same shape as add_pmax_audience_signal

**Execution time:** 2-5 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for updating an existing PMax audience IN PLACE (#325).\n\nUse this instead of remove + add when you want to change segment\ncomposition without dealing with the 'audience name already exists'\nerror that comes from re-creating an audience under the same name.\n\nCommon pattern: load current composition with get_pmax_audience_signals,\nadd or remove segment IDs as needed, pass the merged list here.",
  "properties": {
    "audience_resource_name": {
      "description": "The audience resource name to update. Get from get_pmax_audience_signals — it's the `audience` field on each signal (NOT the signal's own resource_name). Example: 'customers/1234567890/audiences/12345'",
      "title": "Audience Resource Name",
      "type": "string"
    },
    "audience_config": {
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
      "description": "REPLACES the audience's segment composition. Same shape as add_pmax_audience_signal: keys 'in_market_audience_ids' (List[int]), 'affinity_audience_ids' (List[int]), 'custom_audience_ids' (List[str]), 'user_list_ids' (List[str]). Shape-tolerant (#559): synonym keys, flat, and nested 'segments' shapes are normalized for you. To MERGE rather than replace, fetch the current composition from get_pmax_audience_signals first and combine with the new segments. Example: {'in_market_audience_ids': [80432, 80210], 'user_list_ids': ['customers/123/userLists/456']}",
      "title": "Audience Config"
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
    "audience_resource_name"
  ],
  "title": "UpdatePMaxAudienceSignalInput",
  "type": "object"
}
```

</details>

<a id="update_product_group"></a>

## `update_product_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Change the max CPC bid on a biddable product-group (UNIT) node.

Get the criterion_id from get_product_groups. Only biddable UNIT leaves have a bid (SUBDIVISION
branches and excluded nodes do not).

**Required:** ad_group_id, criterion_id, bid_micros.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Change the bid on a biddable product-group (UNIT) node.",
  "properties": {
    "ad_group_id": {
      "description": "The Shopping ad group ID.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "criterion_id": {
      "description": "The product-group criterion ID (from get_product_groups).",
      "title": "Criterion Id",
      "type": "string"
    },
    "bid_micros": {
      "description": "New max CPC in micros (1,000,000 = 1 currency unit).",
      "title": "Bid Micros",
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
      "description": "Google Ads customer ID. Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id",
    "criterion_id",
    "bid_micros"
  ],
  "title": "UpdateProductGroupInput",
  "type": "object"
}
```

</details>

<a id="validate_and_prepare_assets"></a>

## `validate_and_prepare_assets`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

🔄 LONG-RUNNING TOOL — **GOOGLE ADS ONLY**.

⚠️ **WRONG TOOL FOR OTHER PLATFORMS.** Each platform has its own asset validator
because the image specs (aspect ratios, sizes, allowed formats) differ:

  • Google Ads      → use `validate_and_prepare_assets` (this tool)
  • Meta Ads        → use `validate_and_prepare_meta_assets`
  • LinkedIn Ads    → use `validate_and_prepare_linkedin_assets`
  • TikTok Ads      → use `validate_and_prepare_tiktok_assets`

If the user is building for Meta/LinkedIn/TikTok, STOP and call the matching
platform-specific tool instead. Calling this Google tool with non-Google images
will fail validation because the field shapes (`marketing_images_landscape`,
`square_marketing_images`, `logo_images`) are Google-Ads-specific.

This tool validates multiple images from URLs for Google Performance Max /
Display campaigns. Emits MCP progress updates while downloading and validating
5-10 images (typically 5-15 seconds). Progress stages: download → validate → commit.

⚠️ CRITICAL: This tool accepts IMAGE URLS (from postimages.org), NOT base64 or file paths!

📋 **YOUR CRITICAL ROLE: URL Validator & Categorizer**

**STEP 1: Call help_user_upload First**

Before anything else:
- Call help_user_upload() to show upload instructions
- User will upload to postimages.org and paste Direct links
- User provides links like: https://i.postimg.cc/ABC123/image.jpg

**STEP 2: Categorize URLs by Examining Images**

When user pastes URLs, YOU MUST:
1. **Request to view each image** (you can see images from URLs)
2. **Calculate aspect ratio** for each: width / height
3. **Categorize based on ratio**:
   - Landscape (1.8-2.0): ~1.91:1 like 1200×628px
   - Square (0.95-1.05): ~1:1 like 1200×1200px
   - Portrait (0.75-0.85): ~0.8:1 like 960×1200px
   - Logo: Small images or very wide (4:1)
4. **Verify minimum requirements**:
   - At least 1 landscape
   - At least 1 square (non-logo)
   - At least 1 logo
5. If missing types, ask user to upload more

2. **Tell them what images they need:**
   - **REQUIRED:**
     - At least 1 landscape image (1.91:1 ratio, like 1200×628px or 600×314px)
     - At least 1 square image (1:1 ratio, like 1200×1200px or 300×300px)
     - At least 1 square logo (1:1 ratio, min 128×128px, recommended 1200×1200px)
   - **OPTIONAL:**
     - Portrait images (4:5 ratio, like 960×1200px or 400×600px)
     - Landscape logos (4:1 ratio, like 1200×300px or 512×128px)

3. **Provide OS-specific help if user asks how to check/resize images:**
   - **Mac users:**
     - "Right-click image → Get Info → shows dimensions"
     - "Use Preview app → Tools → Adjust Size to resize"
     - "Recommended free tool: GIMP (gimp.org) for precise aspect ratio control"

   - **Windows users:**
     - "Right-click image → Properties → Details tab → shows dimensions"
     - "Use Paint → Resize → maintain aspect ratio checkbox"
     - "Recommended free tool: GIMP (gimp.org) or Paint.NET"

   - **Online tools (any OS):**
     - "Canva.com (free, easy templates for exact sizes)"
     - "Photopea.com (free Photoshop alternative)"
     - "ResizePixel.com (quick resize tool)"

4. **CRITICAL: Read, Examine, and Categorize Images BEFORE Calling This Tool:**

   **Step 4a: READ FILE CONTENTS (REQUIRED!)**
   - When user uploads images, ChatGPT stores them as files with paths like `/mnt/data/image.png`
   - **YOU MUST READ EACH FILE** to get the actual image data
   - **DO NOT** send file paths or FILE:file_xxx references to this tool
   - **DO NOT** send data URIs with FILE: references like `data:image/png;base64,FILE:file_xxx`
   - **YOU MUST** read the file contents using your file reading capabilities
   - Convert file contents to base64 string
   - Send actual base64 encoded data (the binary image bytes encoded as base64)

   **Step 4b: EXAMINE AND CATEGORIZE**
   - **USE EXTENDED THINKING** to analyze each image
   - When you read the image file, you can see its dimensions
   - Calculate aspect ratio: width / height
   - Categorize based on aspect ratio:
     * **Landscape** (1.80-2.00 ratio): ~1.91:1 images like 1200×628px
     * **Square** (0.95-1.05 ratio): ~1:1 images like 1200×1200px
     * **Portrait** (0.75-0.85 ratio): ~0.8:1 (4:5) images like 960×1200px
     * **Logo Square** (0.95-1.05 ratio + small size <500px): Small square logos
     * **Logo Landscape** (3.80-4.20 ratio): ~4:1 images like 1200×300px

   **Step 4c: VERIFY MINIMUM REQUIREMENTS**
   - Count images in each category
   - **REQUIRED MINIMUM**:
     * At least 1 landscape image
     * At least 1 square image (non-logo)
     * At least 1 logo (square or landscape)
   - If missing ANY required type:
     * Tell user: "You need at least 1 landscape, 1 square, and 1 logo image"
     * Ask user to upload missing types
     * DO NOT call this tool yet

**STEP 2: Call This Tool with ACTUAL Base64 Data**

⚠️ **CRITICAL - Data Format**:
```python
# ❌ WRONG - DO NOT SEND:
"data:image/png;base64,FILE:file_xxx"  # File reference - will fail!
"/mnt/data/image.png"  # File path - will fail!

# ✅ CORRECT - SEND THIS:
"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..."  # Actual base64 encoded image bytes
# OR just the base64 string without prefix:
"iVBORw0KGgoAAAANSUhEUgAA..."  # Also works
```

**How to get actual base64**:
1. Read the uploaded file from its path
2. Get the file contents (binary data)
3. Encode to base64 string
4. Pass to this tool

**Example**:
- User uploads `image.png`
- ChatGPT stores as `/mnt/data/image123.png`
- You read the file → get binary PNG data
- You encode to base64 → get "iVBORw0K..."
- You send to tool: `marketing_images_landscape: ["iVBORw0K..."]`

**IMPORTANT**:
- The tool needs ACTUAL image data to validate dimensions and aspect ratios
- File references cannot be validated
- You must convert files to base64 before calling this tool

**Image Requirements (Google Ads PMax specs):**

| Type | Aspect Ratio | Min Size | Recommended | Max File Size |
|------|--------------|----------|-------------|---------------|
| Landscape | 1.91:1 | 600×314px | 1200×628px | 5MB |
| Square | 1:1 | 300×300px | 1200×1200px | 5MB |
| Portrait | 4:5 (0.8:1) | 400×600px | 960×1200px | 5MB |
| Logo Square | 1:1 | 128×128px | 1200×1200px | 5MB |
| Logo Landscape | 4:1 | 512×128px | 1200×300px | 5MB |

- **Tolerance:** ±2% aspect ratio deviation allowed
- **Formats:** JPEG, PNG, WEBP only

**STEP 3: Pre-Flight Checks (BEFORE Calling Tool)**

**Check #1: Count Images**
- Count how many images you categorized in each type
- **REQUIRED MINIMUM**:
  * 1+ landscape images
  * 1+ square images (non-logo)
  * 1+ logo images
- If missing ANY required type:
  * "I see you uploaded [N] images, but I need at least 1 landscape, 1 square, and 1 logo."
  * "Please upload [missing type] image(s)."
  * DO NOT call this tool yet
  * Wait for user to upload more images

**Check #2: Verify Categorization**
- Use extended thinking to double-check your categorization
- Example thinking:
  * "Image 1: 1200×628 = 1.91 ratio → landscape ✓"
  * "Image 2: 1200×1200 = 1.0 ratio, large size → square marketing image ✓"
  * "Image 3: 200×200 = 1.0 ratio, small size → logo ✓"
- If uncertain about categorization, explain to user and ask for clarification

**STEP 4: Handle Validation Results**

**If validation FAILS:**
- Show the user the EXACT error message from this tool
- Explain what the error means in simple terms
- Provide step-by-step instructions to fix:
  - How to check current dimensions
  - What the correct dimensions should be
  - How to resize the image
  - How to re-upload

**If validation SUCCEEDS:**
- Celebrate! ✅
- Show the asset_bundle_id to the user
- Tell them the bundle is valid for 1 hour
- Move to collecting campaign text details (name, headlines, etc.)
- DO NOT call create_pmax_campaign until you have ALL text details

**Returns:**
- SUCCESS: asset_bundle_id (UUID) + summary of validated images
- FAILURE: Specific error for the first invalid image + instructions to fix

**Common Validation Errors & How to Help:**

1. **Wrong aspect ratio**
   - Error: "Expected 1.91:1, got 2.0:1"
   - Help: "Your image is slightly too wide. Crop it to 1200×628px exactly."

2. **Image too small**
   - Error: "Minimum size is 600×314px, got 500×250px"
   - Help: "Use a higher resolution image or upscale this one."

3. **File too large**
   - Error: "File too large. Maximum 5 MB, got 6.2 MB"
   - Help: "Compress the image using an online tool or save as JPEG with lower quality."

4. **Wrong format**
   - Error: "Unsupported format 'BMP'"
   - Help: "Convert to JPEG or PNG format."

**Example User Flow:**

User: "I want to create a PMax campaign"
You: "Great! Let's start by uploading your images. You'll need:
- At least 1 landscape image (1200×628px recommended)
- At least 1 square image (1200×1200px recommended)
- At least 1 square logo (1200×1200px recommended)

Click the paperclip icon (📎) to attach your images."

[User uploads images]

You: "Perfect! I can see your images. Let me validate them..."
[Call validate_and_prepare_assets]

**Execution Time:** 1-3 seconds (fast validation)

**Authentication:** NOT required for this tool (validation only)

**REMEMBER:**
- Be extremely patient and helpful with image validation
- Provide clear, actionable instructions for fixing errors
- Never proceed to create_pmax_campaign without a valid asset_bundle_id
- The bundle expires in 1 hour - if expired, re-validate images

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for validate_and_prepare_assets tool - NOW ACCEPTS URLs!",
  "properties": {
    "marketing_images_landscape": {
      "description": "Landscape image URLs (1.91:1 ratio, min 600×314px). Direct HTTPS links from postimages.org ending in .jpg/.png/.webp. Minimum 1 required.",
      "items": {
        "type": "string"
      },
      "title": "Marketing Images Landscape",
      "type": "array"
    },
    "marketing_images_square": {
      "description": "Square image URLs (1:1 ratio, min 300×300px). Direct HTTPS links ending in .jpg/.png/.webp. Minimum 1 required.",
      "items": {
        "type": "string"
      },
      "title": "Marketing Images Square",
      "type": "array"
    },
    "marketing_images_portrait": {
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
      "description": "Portrait image URLs (4:5 ratio = 0.8:1, min 400×600px). Direct HTTPS links. Optional.",
      "title": "Marketing Images Portrait"
    },
    "logos_square": {
      "description": "Square logo URLs (1:1 ratio, min 128×128px). Direct HTTPS links. Minimum 1 required.",
      "items": {
        "type": "string"
      },
      "title": "Logos Square",
      "type": "array"
    },
    "logos_landscape": {
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
      "description": "Landscape logo URLs (4:1 ratio, min 512×128px). Direct HTTPS links. Optional.",
      "title": "Logos Landscape"
    }
  },
  "required": [
    "marketing_images_landscape",
    "marketing_images_square",
    "logos_square"
  ],
  "title": "ValidateAssetsInput",
  "type": "object"
}
```

</details>

<a id="validate_and_prepare_meta_assets"></a>

## `validate_and_prepare_meta_assets`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://mcp.adspirer.com/api/v1/tools)

**META ADS ONLY.** Validates and uploads images for Meta (Facebook/Instagram) campaigns.

⚠️ **WRONG TOOL FOR OTHER PLATFORMS.** Each ad platform has its own validator
because image specs differ:

  • Meta Ads (this tool)  → 1080×1080 carousel, 1200×628 feed, etc.
  • Google Ads            → use `validate_and_prepare_assets`
  • LinkedIn Ads          → use `validate_and_prepare_linkedin_assets`
  • TikTok Ads            → use `validate_and_prepare_tiktok_assets`

This tool validates image URLs against Meta's specifications and uploads them to get image hashes needed for campaign creation. It stores validated assets in a temporary bundle (60-minute TTL).

Returns:
- Validation results (pass/fail per image)
- Image hashes for successfully uploaded images
- Asset bundle ID for use in campaign creation
- Placement compatibility information

When to use this tool:
- "Upload this image for my Meta campaign"
- "Validate my product images for Facebook ads"
- "Prepare images for Instagram ads"
- User provides image URLs and wants to create a campaign

Parameters:
- image_urls: List of public URLs to validate and upload (1-10 images)
- placement: Target placement - 'feed' (default), 'stories_reels', or 'carousel'
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 5-15 seconds (depends on image count and size)
Data source: Meta Ad Image Upload API

Image Requirements:
| Placement | Aspect Ratio | Min Dimensions | Max Size |
|-----------|-------------|----------------|----------|
| Feed | 1:1 or 4:5 | 600x600 | 30MB |
| Stories/Reels | 9:16 | 500x888 | 30MB |
| Carousel | 1:1 | 1080x1080 | 30MB |

Workflow:
1. Use `validate_and_prepare_meta_assets` with image URLs
2. If successful, receive an `asset_bundle_id`
3. Use that bundle_id with `create_meta_image_campaign`

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for validating and uploading Meta ad images",
  "properties": {
    "image_urls": {
      "description": "**REQUIRED.** List of public image URLs to validate and upload (max 10). Ask the user for the image URLs before calling this tool — do NOT call with an empty payload. Images will be validated and uploaded to Meta to get image hashes you can reference in campaign creation.",
      "items": {
        "type": "string"
      },
      "title": "Image Urls",
      "type": "array"
    },
    "placement": {
      "default": "feed",
      "description": "Target placement: 'feed' (default), 'stories_reels', or 'carousel'",
      "title": "Placement",
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
      "description": "Meta Ad Account ID (optional)",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "image_urls"
  ],
  "title": "ValidateAndPrepareMetaAssetsInput",
  "type": "object"
}
```

</details>

<a id="validate_catalog_readiness"></a>

## `validate_catalog_readiness`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to create Advantage+ Catalog / Dynamic Product Ads, or asks "is my catalog ready for ads?". Run this PRE-FLIGHT before setting up a catalog campaign.

Aggregates the real signals that decide whether dynamic product ads will actually deliver:
- Catalog exists and has products
- Product set (if given) is non-empty
- Sampled products have images (catalog ads render the product image — no image = no render)
- Feed health (last-upload errors), best-effort
- If a pixel_id is given: classifies RETARGETING readiness (needs ViewContent/AddToCart) vs PROSPECTING-only

Returns an overall verdict (ready / ready_with_warnings / not_ready), explicit blockers, warnings, and a recommended audience strategy. Always prefer this before catalog campaign creation so we never launch a dead retargeting campaign.

When to use:
- "Create a catalog ad", "set up dynamic product ads", "advantage+ catalog"
- "Is my product catalog ready to advertise?"

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for the catalog-ads pre-flight readiness check.",
  "properties": {
    "catalog_id": {
      "description": "Product catalog ID (required). Get it from list_meta_catalogs.",
      "title": "Catalog Id",
      "type": "string"
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
      "description": "Optional product set ID to scope the readiness check. Get it from list_meta_product_sets. Defaults to the whole catalog.",
      "title": "Product Set Id"
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
      "description": "Optional Meta Pixel ID. If provided, the check classifies RETARGETING readiness (needs ViewContent/AddToCart events) vs PROSPECTING-only. Get it from list_meta_pixels.",
      "title": "Pixel Id"
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
    "catalog_id"
  ],
  "title": "ValidateCatalogReadinessInput",
  "type": "object"
}
```

</details>

<a id="validate_video"></a>

## `validate_video`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Validate video for ad campaigns (unified tool for all platforms).

⚠️ IMPORTANT: This is a READ-ONLY validation tool. Safe to call multiple times.

🎯 **What This Tool Does:**
- Validates videos for Google Ads PMAX or TikTok campaigns
- For PMAX: Validates YouTube video (privacy, duration, embeddable)
- For TikTok: Validates public video URL is accessible
- Returns metadata (title, duration, privacy, thumbnail)

**DOES NOT upload videos** - user must already have video uploaded:
- PMAX: Video must be on YouTube (public or unlisted)
- TikTok: Video must be on public hosting (Google Drive, Vimeo, etc.)

**Parameters:**
- video_url_or_id (required): YouTube URL/ID (PMAX) or public video URL (TikTok)
- platform (required): 'pmax' or 'tiktok'

**For PMAX:**
Accepts YouTube formats:
- Full URL: https://youtube.com/watch?v=dQw4w9WgXcQ
- Short URL: https://youtu.be/dQw4w9WgXcQ
- Shorts: https://youtube.com/shorts/dQw4w9WgXcQ
- Direct ID: dQw4w9WgXcQ (11 characters)

Validates:
- Video exists and is accessible
- Privacy is Public or Unlisted (NOT Private)
- Embeddable is enabled
- Duration ≥10 seconds (PMAX requirement)

Returns:
- Video title
- Duration
- Privacy status
- Thumbnail URL
- Video ID

**For TikTok:**
Accepts public video file URLs:
- Google Drive: https://drive.google.com/file/d/ABC123/view
- Vimeo: https://vimeo.com/video/123456
- Dropbox: https://dropbox.com/s/abc/video.mp4
- Any publicly accessible video URL

Validates:
- URL is accessible (HTTP 200)
- Content-Type is video/* (when available)

Returns:
- URL validation status
- Content-Type
- File size (if available)

**Execution Time:** 1-3 seconds (YouTube Data API call or HTTP request)

**When to Use:**
- BEFORE creating a campaign with videos
- To verify video meets platform requirements
- To get video metadata (title, duration)

**Example Usage:**

```
User: "I want to use this YouTube video in my PMAX campaign: dQw4w9WgXcQ"
YOU: [Call validate_video with video_url_or_id="dQw4w9WgXcQ", platform="pmax"]
Response: Video validated, title="Product Demo", duration=45s, ready for use
```

```
User: "Can I use this video for TikTok ads: https://drive.google.com/file/d/ABC/view"
YOU: [Call validate_video with video_url_or_id="https://drive...", platform="tiktok"]
Response: URL validated, accessible, ready for campaign
```

**Error Handling:**
- Private videos: Clear error asking user to change privacy to Public/Unlisted
- Short videos (<10s for PMAX): Error with duration requirement
- Invalid URLs: Error with accessibility details
- Not embeddable: Error asking user to enable embedding

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for unified video validation",
  "properties": {
    "video_url_or_id": {
      "description": "YouTube video URL/ID (for PMAX) OR public video file URL (for TikTok). Examples: 'dQw4w9WgXcQ' (YouTube ID), 'https://youtube.com/watch?v=dQw4w9WgXcQ' (YouTube URL), 'https://youtu.be/dQw4w9WgXcQ' (YouTube short URL), 'https://drive.google.com/file/d/ABC123/view' (Google Drive video), 'https://vimeo.com/video/123456' (Vimeo video)",
      "title": "Video Url Or Id",
      "type": "string"
    },
    "platform": {
      "description": "Target platform: 'pmax' or 'tiktok'. Determines validation rules and requirements. 'pmax' = Google Ads Performance Max (requires YouTube video). 'tiktok' = TikTok Ads (requires public video URL).",
      "title": "Platform",
      "type": "string"
    }
  },
  "required": [
    "video_url_or_id",
    "platform"
  ],
  "title": "ValidateVideoInput",
  "type": "object"
}
```

</details>

