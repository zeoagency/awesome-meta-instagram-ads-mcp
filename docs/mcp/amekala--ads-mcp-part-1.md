# amekala/ads-mcp — tools 1–35

[All tools](amekala--ads-mcp.md) · [Tool index](../tool-index.md)

<a id="add_ad_group_audiences"></a>

## `add_ad_group_audiences`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add audience targeting to an ad group.

⚠️ Use `search_audiences` FIRST to find real audience IDs — NEVER fabricate IDs
(wrong IDs target unrelated audiences and waste budget).

**Accepts:** in_market_audiences, affinity_audiences, custom_audiences, user_lists.

**Required:** ad_group_id + at least one audience list.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Add audience targeting to an ad group.\n\nUse search_audiences to find real audience IDs — NEVER fabricate them.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID to add audiences to.",
      "title": "Ad Group Id",
      "type": "string"
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
      "description": "In-market audience IDs (from search_audiences).",
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
      "description": "Affinity audience IDs (from search_audiences).",
      "title": "Affinity Audiences"
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
      "description": "Custom audience IDs (from search_audiences).",
      "title": "Custom Audiences"
    },
    "user_lists": {
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
      "description": "Remarketing/user-list resource names or IDs.",
      "title": "User Lists"
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
  "title": "AddAdGroupAudiencesInput",
  "type": "object"
}
```

</details>

<a id="add_app_ad_asset"></a>

## `add_app_ad_asset`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add an image or video asset to an existing App (Universal App / UAC) ad.

App ads are largely automated, but you can supply extra image/video creative that Google
mixes into the ads. This tool appends one asset to the app ad (existing assets are kept).

**Parameters:**
- ad_id (REQUIRED), ad_group_id (REQUIRED) — the App ad. Get from get_campaign_structure / get_ad_creative.
- asset_type (REQUIRED): 'image' or 'video'.
- image (asset_type=image): image_url (public http(s) URL or data:image/...;base64,... to UPLOAD)
  OR image_asset (an existing customers/<cid>/assets/<id> resource name).
- video (asset_type=video): youtube_video_id (a YouTube video id).
- customer_id: Optional.

Works on all App sub-types (install / engagement / pre-registration).

**Execution time:** 2-6 seconds (upload + mutate).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding an image or video asset to an App (UAC) ad.",
  "properties": {
    "ad_id": {
      "description": "The App ad ID. Get from get_campaign_structure / get_ad_creative.",
      "title": "Ad Id",
      "type": "string"
    },
    "ad_group_id": {
      "description": "The ad group the App ad belongs to.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "asset_type": {
      "description": "'image' or 'video'.",
      "title": "Asset Type",
      "type": "string"
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
      "description": "For asset_type=image: a public http(s) URL OR a data:image/...;base64,... URI to UPLOAD a new image asset. (Alternatively pass image_asset to reference an existing one.)",
      "title": "Image Url"
    },
    "image_asset": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For asset_type=image: an EXISTING image asset resource name (customers/<cid>/assets/<id>) to link instead of uploading.",
      "title": "Image Asset"
    },
    "youtube_video_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For asset_type=video: a YouTube video id (e.g. 'w0qzUDSXP0o'). A YouTube video asset is created and linked.",
      "title": "Youtube Video Id"
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
    "asset_type"
  ],
  "title": "AddAppAdAssetInput",
  "type": "object"
}
```

</details>

<a id="add_asset_group_listing_filter"></a>

## `add_asset_group_listing_filter`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Subdivide a retail Performance Max asset group's products — include or exclude a partition.

Splits products by dimension_type=value (e.g. product_brand=Nike, product_type=Shoes). exclude=true
makes the partition UNIT_EXCLUDED (those products won't serve from this asset group); otherwise it's
UNIT_INCLUDED. Retail PMax has NO per-node bids (bidding is fully automated). The "everything else"
sibling is created automatically.

FIRST call on an unpartitioned asset group subdivides the root. To split an EXISTING partition
further, pass parent_filter_id (from get_asset_group_listing_filters).

**Required:** asset_group_id, dimension_type, value. Optional: level (type/category), index
(custom_attribute), exclude, parent_filter_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Subdivide a retail-PMax asset group's products — include or exclude a partition (no bids; PMax auto-bids).",
  "properties": {
    "asset_group_id": {
      "description": "The retail-PMax asset group ID.",
      "title": "Asset Group Id",
      "type": "string"
    },
    "dimension_type": {
      "description": "What to split products by: product_brand | product_type | product_item_id | product_category | product_condition | product_channel | product_custom_attribute.",
      "title": "Dimension Type",
      "type": "string"
    },
    "value": {
      "description": "The dimension value for this partition (e.g. 'Nike', 'Shoes', 'NEW').",
      "title": "Value",
      "type": "string"
    },
    "level": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For product_type / product_category: LEVEL1..LEVEL5 (default LEVEL1).",
      "title": "Level"
    },
    "index": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For product_custom_attribute: INDEX0..INDEX4 (default INDEX0).",
      "title": "Index"
    },
    "exclude": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Exclude this partition from serving (UNIT_EXCLUDED). Retail PMax has no per-node bids.",
      "title": "Exclude"
    },
    "parent_filter_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "To split an EXISTING partition further, the UNIT filter_id to subdivide (from get_asset_group_listing_filters). Omit for the first subdivision.",
      "title": "Parent Filter Id"
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
    "asset_group_id",
    "dimension_type",
    "value"
  ],
  "title": "AddAssetGroupListingFilterInput",
  "type": "object"
}
```

</details>

<a id="add_business_name_asset"></a>

## `add_business_name_asset`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a BUSINESS_NAME asset to a Search campaign.

The business name shows in Search ads next to the URL. It is a brand
identifier, not promotional copy. Max 25 characters.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED — get from list_campaigns)
- business_name: The display name (max 25 chars)
- customer_id: Optional (uses connected account if omitted)

**Behavior:**
Creates a new TextAsset in the Asset Library and links it to the campaign
with field_type=BUSINESS_NAME. Existing business name assets on the campaign
are not removed — call this once per campaign or unlink the previous asset
first if you want a clean swap.

**Execution time:** 2-4 seconds

**Example:**
User: "Set the business name on campaign 23847465076 to 'Refresh Wellington'"
Agent: add_business_name_asset(campaign_id="23847465076", business_name="Refresh Wellington")

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding a BUSINESS_NAME asset to a Search campaign.\n\nThe business name shows next to the URL in Search ads. Each campaign\ntypically has ONE — running this tool a second time appends a new asset\nwithout removing the previous one. Use `get_campaign_structure` to see\nthe current business name asset and unlink the old one if needed.\n\nMax length: 25 characters (Google enforces).",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (numeric). Get from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "business_name": {
      "description": "The business name to display next to ad URLs. Max 25 characters. Examples: 'Refresh Wellington', 'Acme Inc'. Avoid promotional language — this is your brand identifier, not ad copy.",
      "title": "Business Name",
      "type": "string"
    },
    "force": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Optional (default false). Idempotent by default: if the same business name is already on the campaign it is NOT added again. Set force=true only to intentionally add a duplicate.",
      "title": "Force"
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
    "business_name"
  ],
  "title": "AddBusinessNameAssetInput",
  "type": "object"
}
```

</details>

<a id="add_call_asset"></a>

## `add_call_asset`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a phone call asset to a campaign.

Call assets show a tap-to-call button on mobile and a visible phone number
on desktop. They attach at campaign level via CampaignAssetService.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED)
- phone_number: digits or formatted ("929-478-4835", "+1 929 478 4835")
- country_code: 2-letter ISO ("US", "GB", "IN", "AU")
- call_conversion_action: Optional. Full resource name of a
  CallConversionAction (`customers/<cid>/conversionActions/<id>`) to count
  calls as conversions. Omit to skip call-conversion tracking.
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-4 seconds

**Example:**
User: "Add 929-478-4835 (US) as a call asset on campaign 23847465076"
Agent: add_call_asset(campaign_id="23847465076", phone_number="929-478-4835", country_code="US")

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding a CALL asset (phone number extension) to a campaign.\n\nCall assets render a tap-to-call button in Search ads on mobile and a\nvisible phone number on desktop. They attach at campaign level via\nCampaignAssetService (the same level as callouts/sitelinks).\n\nFor call-conversion tracking, pass `call_conversion_action` with the\nfull resource name of a CallConversionAction. Without it, calls clicked\nfrom this asset are NOT counted as conversions.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (numeric). Get from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "phone_number": {
      "description": "Phone number to display. Plain digits or with separators are both accepted: '9294784835', '929-478-4835', '+1 929 478 4835'. Google normalizes the number using country_code.",
      "title": "Phone Number",
      "type": "string"
    },
    "country_code": {
      "description": "2-letter ISO country code. 'US', 'GB', 'IN', 'AU', etc. Must match the country the phone number is registered to.",
      "title": "Country Code",
      "type": "string"
    },
    "call_conversion_action": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional. Full resource name of a CallConversionAction (`customers/<cid>/conversionActions/<id>`) to count calls as conversions. Omit to skip call-conversion tracking on this asset.",
      "title": "Call Conversion Action"
    },
    "force": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Optional (default false). By default this tool is idempotent: if the same phone number is already on the campaign it is NOT added again (returns the existing one). Set force=true only if you intentionally want a second identical number on the campaign.",
      "title": "Force"
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
    "phone_number",
    "country_code"
  ],
  "title": "AddCallAssetInput",
  "type": "object"
}
```

</details>

<a id="add_callout_extensions"></a>

## `add_callout_extensions`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add callout extensions to a campaign.

Callouts are short, non-clickable highlights that appear below your ad.
They communicate quick trust signals and differentiators.

**IMPORTANT RULES (from google-ads-creative-guidelines.md):**
- Max 25 characters each
- 4-8 callouts recommended
- Should NOT be CTAs (no "click", "buy", "order", "call")
- Should NOT end with periods

**GOOD EXAMPLES:**
- "Free Shipping"
- "24/7 Support"
- "No Code Required"
- "30 Second Setup"
- "Award Winning"

**BAD EXAMPLES (will be rejected):**
- "Click Now" (CTA word)
- "Buy Today" (CTA word)
- "Free Shipping." (ends with period)

**Parameters:**
- campaign_id: The campaign ID (REQUIRED). Get from list_campaigns.
- callouts: List of callout text strings (REQUIRED). Each max 25 chars.
- customer_id: Optional Google Ads customer ID

**Execution time:** 2-5 seconds

**When to use:**
- User wants to add callouts/highlights to their campaign
- User asks about extensions or ad enhancements
- After creating a campaign, suggest adding callouts

**Example:**
User: "Add some callouts to my campaign"
Agent:
1. Uses list_campaigns to get campaign_id
2. Uses add_callout_extensions with relevant callouts

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding callout extensions to a campaign.\n\nCallouts are short, non-clickable highlights that appear below your ad.\nThey communicate quick trust signals and differentiators.\n\nGOOD EXAMPLES: \"Free Shipping\", \"24/7 Support\", \"No Code Required\", \"30 Second Setup\"\nDISCOURAGED (will warn, not reject): \"Click Now\", \"Buy Today\" — these\nread as CTAs and are weaker as callouts.\n\nFrom google-ads-creative-guidelines.md:\n- Max 25 characters each (anything longer is smart-truncated)\n- 4-8 callouts recommended\n- Avoid CTA-style wording (\"click\", \"buy\", \"order\", \"call\") — callouts\n  describe features, not actions. We emit a warning but still ship the\n  callout. Substring-style words like \"Buying Tips\" are accepted.\n- Should NOT end with periods (trailing period is auto-stripped)",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to add callouts to. Get from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "callouts": {
      "description": "List of callout text strings. Each max 25 characters. Example: ['Free Shipping', '24/7 Support', 'No Code Required']",
      "items": {
        "type": "string"
      },
      "title": "Callouts",
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
      "description": "Optional. Pin callouts to a SPECIFIC ad group instead of the whole campaign. Use when the campaign has themed ad groups and you want different callouts per theme. Per Google's specificity rules, ad-group callouts override campaign-level callouts for that ad group. Get ad group IDs from get_campaign_structure or list_ad_groups.",
      "title": "Ad Group Id"
    }
  },
  "required": [
    "campaign_id",
    "callouts"
  ],
  "title": "AddCalloutExtensionsInput",
  "type": "object"
}
```

</details>

<a id="add_campaign_label"></a>

## `add_campaign_label`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Attach an existing label to a campaign.

Get the label_id from list_labels (or create_label first). This tags the campaign for
filtering and reporting; it does not change delivery.

**Required:** campaign_id + label_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Attach an existing label to a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "label_id": {
      "description": "The label ID to attach (from list_labels or create_label).",
      "title": "Label Id",
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
    "campaign_id",
    "label_id"
  ],
  "title": "AddCampaignLabelInput",
  "type": "object"
}
```

</details>

<a id="add_campaign_proximity"></a>

## `add_campaign_proximity`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add proximity (radius) targeting to a campaign — target everyone within N miles/km of an address.

**When to use:**
- "Target people within 10 miles of downtown San Francisco"
- Local businesses wanting a radius around a store, not a whole city/state

**Different from city/state targeting:** for country/state/city/postal geo_target_constant
targeting, use `update_campaign` (locations_to_add) instead. Proximity is a RADIUS around a point.

**Each proximity needs:**
- radius + radius_units (MILES | KILOMETERS)
- an address: any of city_name, province_name/province_code, postal_code, country_code, street_address
- optional bid_modifier (1.2 = +20%)

**Required:** campaign_id + 1+ proximities.

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "_ProximityCircle": {
      "description": "One proximity (radius) circle around an address.",
      "properties": {
        "radius": {
          "description": "Radius length (e.g. 10). Units set by radius_units.",
          "exclusiveMinimum": 0,
          "title": "Radius",
          "type": "number"
        },
        "radius_units": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": "MILES",
          "description": "MILES or KILOMETERS.",
          "title": "Radius Units"
        },
        "country_code": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "2-letter country code, e.g. 'US'.",
          "title": "Country Code"
        },
        "province_code": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "State/province code, e.g. 'US-CA'.",
          "title": "Province Code"
        },
        "province_name": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "State/province name, e.g. 'California'.",
          "title": "Province Name"
        },
        "city_name": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "City, e.g. 'San Francisco'.",
          "title": "City Name"
        },
        "postal_code": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Postal/ZIP code.",
          "title": "Postal Code"
        },
        "street_address": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Street address.",
          "title": "Street Address"
        },
        "bid_modifier": {
          "anyOf": [
            {
              "maximum": 10.0,
              "minimum": 0.1,
              "type": "number"
            },
            {
              "type": "null"
            }
          ],
          "default": null,
          "description": "Optional bid adjustment (1.2 = +20%, 0.8 = -20%).",
          "title": "Bid Modifier"
        }
      },
      "required": [
        "radius"
      ],
      "title": "_ProximityCircle",
      "type": "object"
    }
  },
  "description": "Add proximity (radius) targeting circles to a Search campaign.\n\nA proximity targets everyone within a radius of an address — e.g. '10 miles\naround San Francisco, CA'. This is DIFFERENT from city/state targeting\n(use update_campaign locations_to_add for geo_target_constant targeting).",
  "properties": {
    "campaign_id": {
      "description": "Campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "proximities": {
      "description": "1+ proximity circles. Each: radius + radius_units + an address (city/state/postal/country/street) + optional bid_modifier.",
      "items": {
        "$ref": "#/$defs/_ProximityCircle"
      },
      "minItems": 1,
      "title": "Proximities",
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
    "proximities"
  ],
  "title": "AddCampaignProximityInput",
  "type": "object"
}
```

</details>

<a id="add_demandgen_ad"></a>

## `add_demandgen_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a new Demand Gen ad (image or video) to an EXISTING Demand Gen ad group.

Use this to add MORE ads to an ad group you already have — e.g. test a second creative, or add a video ad alongside an image ad. It does NOT create an ad group or change targeting; get the ad_group_id from get_campaign_structure (it must be a DEMAND_GEN ad group).

**Formats:**
- **multi_asset** (default) — image ad: marketing_images (landscape 1.91:1), square_marketing_images (1:1), portrait_marketing_images (4:5), logo. Google mixes them.
- **video_responsive** — video ad: youtube_video_ids (1-5) + logo. long_headlines recommended.

**Creative bounds (Demand Gen):** headlines 1-5 (max 40 chars), descriptions 1-5 (max 90 chars), business_name max 25, long_headlines max 90 chars.

**Assets:** provide NEW images via marketing_images/etc. as [{"url": "...", "name": "..."}], OR reuse existing asset resource names via existing_images, OR a logo by logo_asset_id (from discover_existing_assets). Videos are referenced by youtube_video_ids.

**Parameters:**
- ad_group_id (REQUIRED) — existing DEMAND_GEN ad group
- ad_format, final_url (REQUIRED), business_name (REQUIRED), headlines (REQUIRED), descriptions (REQUIRED)
- long_headlines, call_to_action, image/video/logo sources (optional per format)

The ad is created ENABLED; delivery is still gated by the ad group + campaign status.

**Execution time:** 10-20 seconds (assets are uploaded then the ad is created in one atomic mutate).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for add_demandgen_ad tool.\n\nAdds a new Demand Gen ad (multi_asset image ad or video_responsive) to an\nEXISTING Demand Gen ad group. Unlike add_demandgen_ad_group, this does NOT\ncreate an ad group or set targeting — it only adds creative to an ad group\nthat already exists (get its ID from get_campaign_structure).",
  "properties": {
    "ad_group_id": {
      "description": "The EXISTING Demand Gen ad group ID to add the ad to. Get from get_campaign_structure (must be a DEMAND_GEN ad group).",
      "title": "Ad Group Id",
      "type": "string"
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
      "description": "Ad format: 'multi_asset' (image ads, default) or 'video_responsive' (video ads).",
      "title": "Ad Format"
    },
    "final_url": {
      "description": "Landing page URL where users go after clicking the ad. **REQUIRED — ask the user for their website URL before calling this tool. Do NOT guess.** Must be HTTPS and reachable. Example: 'https://example.com/product'.",
      "title": "Final Url",
      "type": "string"
    },
    "business_name": {
      "description": "Business name, max 25 characters.",
      "maxLength": 25,
      "title": "Business Name",
      "type": "string"
    },
    "headlines": {
      "description": "MUST BE JSON ARRAY: 1-5 headlines, each max 40 characters.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Headlines",
      "type": "array"
    },
    "descriptions": {
      "description": "MUST BE JSON ARRAY: 1-5 descriptions, each max 90 characters.",
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
      "description": "Optional 1-5 long headlines, max 90 chars each. Used by video_responsive format.",
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
      "description": "CTA label: LEARN_MORE, SHOP_NOW, SIGN_UP, SUBSCRIBE, DOWNLOAD, BOOK_NOW, etc.",
      "title": "Call To Action"
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
      "description": "Landscape images (1.91:1) as [{\"url\": \"...\", \"name\": \"img1\"}].",
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
      "description": "Square images (1:1) as [{\"url\": \"...\", \"name\": \"img1\"}].",
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
      "description": "Portrait images (4:5) as [{\"url\": \"...\", \"name\": \"img1\"}].",
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
      "description": "Existing image asset resource names to reuse. Keys: marketing_images_landscape, marketing_images_square, marketing_images_portrait, logos_square.",
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
      "description": "YouTube video IDs for video_responsive format. 1-5 videos.",
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
      "description": "New logo images as [{\"url\": \"...\", \"name\": \"logo1\"}].",
      "title": "Logo Images"
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
    "final_url",
    "business_name",
    "headlines",
    "descriptions"
  ],
  "title": "AddDemandGenAdInput",
  "type": "object"
}
```

</details>

<a id="add_demandgen_ad_group"></a>

## `add_demandgen_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a new ad group with targeting and ads to an EXISTING Demand Gen campaign.

Use this after create_demandgen_campaign to add additional ad groups. Each ad group can have:
- **Different location targeting** (e.g., US cities vs India cities vs UAE cities)
- **Different audience targeting** (e.g., marketing pros vs tech founders vs agency owners)
- **Same or different ad creative** (headlines, descriptions, images, videos)

**Reuse Existing Audiences:**
To attach an existing audience (from Google Ads UI or a previous campaign), pass:
- audience_segments.existing_audience_id: numeric audience ID
- audience_segments.existing_audience_resource_name: full resource name

**Create New Audiences:**
To create a new audience from interest segments:
- audience_segments.in_market_audience_ids: [80517, 80520]
- audience_segments.affinity_audience_ids: [92948]
Use search_audiences to find segment IDs.

**Parameters:**
- campaign_id: Demand Gen campaign ID (from create_demandgen_campaign or list_campaigns)
- ad_group_name: Descriptive name
- Same creative fields as create_demandgen_campaign (headlines, descriptions, images, etc.)
- target_locations: Location targeting specific to this ad group
- audience_segments: Audience targeting specific to this ad group

**Execution time:** 10-20 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for add_demandgen_ad_group tool.\n\nAdds a new ad group with targeting and ads to an existing Demand Gen campaign.\nEach ad group can have its own location targeting, audience targeting, and creative.",
  "properties": {
    "campaign_id": {
      "description": "The Demand Gen campaign ID to add the ad group to. Get from list_campaigns or get_campaign_structure.",
      "title": "Campaign Id",
      "type": "string"
    },
    "ad_group_name": {
      "description": "Name for the new ad group (e.g., 'US Metro - Marketing Pros')",
      "title": "Ad Group Name",
      "type": "string"
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
      "description": "Ad format: 'multi_asset' (image ads, default), 'video_responsive' (video ads).",
      "title": "Ad Format"
    },
    "final_url": {
      "description": "Landing page URL where users go after clicking the ad. **REQUIRED — ask the user for their website URL before calling this tool. Do NOT guess.** Must be HTTPS and reachable. Example: 'https://example.com/product'.",
      "title": "Final Url",
      "type": "string"
    },
    "business_name": {
      "description": "Business name, max 25 characters.",
      "maxLength": 25,
      "title": "Business Name",
      "type": "string"
    },
    "headlines": {
      "description": "MUST BE JSON ARRAY: 1-5 headlines, each max 40 characters.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Headlines",
      "type": "array"
    },
    "descriptions": {
      "description": "MUST BE JSON ARRAY: 1-5 descriptions, each max 90 characters.",
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
      "description": "Optional 1-5 long headlines, max 90 chars each. For video_responsive format.",
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
      "description": "CTA label: LEARN_MORE, SHOP_NOW, SIGN_UP, SUBSCRIBE, DOWNLOAD, BOOK_NOW, etc.",
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
      "description": "Geographic targets for THIS ad group (e.g., ['New York', 'Bangalore']). Each ad group can target different locations.",
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
      "description": "Language targets as ISO codes (e.g., ['en']). Defaults to English.",
      "title": "Target Languages"
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
      "description": "Optional channel controls for this ad group.",
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
      "description": "Landscape images (1.91:1) as [{\"url\": \"...\", \"name\": \"img1\"}].",
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
      "description": "Square images (1:1) as [{\"url\": \"...\", \"name\": \"img1\"}].",
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
      "description": "Portrait images (4:5) as [{\"url\": \"...\", \"name\": \"img1\"}].",
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
      "description": "Existing image asset resource names to reuse. Keys: marketing_images_landscape, marketing_images_square, marketing_images_portrait, logos_square.",
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
      "description": "YouTube video IDs for video_responsive format. 1-5 videos.",
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
      "description": "New logo images as [{\"url\": \"...\", \"name\": \"logo1\"}].",
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
      "description": "Asset bundle ID from validate_and_prepare_assets.",
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
      "description": "Audience targeting for THIS ad group. CRITICAL: Only use segment IDs returned by search_audiences tool. NEVER fabricate or guess IDs -- wrong IDs target unrelated audiences and waste budget. If search_audiences returns no results, skip audience_segments entirely. To REUSE an existing audience: {'existing_audience_id': 12345} or {'existing_audience_resource_name': 'customers/123/audiences/456'}. To CREATE new: {'in_market_audience_ids': [80463], 'affinity_audience_ids': [92913], 'custom_audience_ids': ['customers/123/customAudiences/456']}. Use search_audiences to find segment IDs.",
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
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "campaign_id",
    "ad_group_name",
    "final_url",
    "business_name",
    "headlines",
    "descriptions"
  ],
  "title": "AddDemandGenAdGroupInput",
  "type": "object"
}
```

</details>

<a id="add_display_ad"></a>

## `add_display_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add another Responsive Display Ad (RDA) to an EXISTING Display ad group.

**When to use:**
- User wants to A/B test multiple creatives in the same ad group
- User asks to "add another ad" to an existing Display ad group

**Required:**
- ad_group_id
- headlines (1-5 @ 30ch), long_headline (1 @ 90ch), descriptions (1-5 @ 90ch), business_name (≤25ch), final_url
- At least one landscape AND one square marketing image (new or via existing_images)

**Character limits (strict):**
- Headlines: MAX 30 chars each
- Long headline: MAX 90 chars
- Descriptions: MAX 90 chars each
- Business name: MAX 25 chars

**Execution time:** 4-8 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for add_display_ad tool.\n\nAdds another Responsive Display Ad to an existing Display ad group.",
  "properties": {
    "ad_group_id": {
      "description": "Existing Display ad group ID.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "final_url": {
      "description": "Landing page URL (https).",
      "title": "Final Url",
      "type": "string"
    },
    "business_name": {
      "description": "Business name, max 25 chars.",
      "maxLength": 25,
      "title": "Business Name",
      "type": "string"
    },
    "headlines": {
      "description": "JSON ARRAY: 1-5 short headlines, each MAX 30 characters.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Headlines",
      "type": "array"
    },
    "long_headline": {
      "description": "Exactly 1 long headline, max 90 characters.",
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
      "description": "Landscape images (1.91:1).",
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
      "description": "Square images (1:1).",
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
      "description": "UUID from `validate_and_prepare_assets`. Pre-validated images get auto-mapped. Recommended.",
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
      "title": "Youtube Video Ids"
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
      "title": "Promo Text"
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
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id",
    "final_url",
    "business_name",
    "headlines",
    "long_headline",
    "descriptions"
  ],
  "title": "AddDisplayAdInput",
  "type": "object"
}
```

</details>

<a id="add_display_ad_group"></a>

## `add_display_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a new DISPLAY_STANDARD ad group (with its own targeting + a Responsive Display Ad) to an EXISTING Display campaign.

**When to use:**
- User wants another ad group inside a Display campaign (different targeting + different creative)
- User asks to "add an ad group to my Display campaign"

**Each ad group can have:**
- Its own audience_segments, topics, managed_placements, display_keywords, demographics
- Its own responsive display ad (creative + assets)
- Optional manual CPC/CPM bid (inherits campaign bidding otherwise)

**Required:**
- campaign_id (Display campaign from list_campaigns)
- ad_group_name
- Full RDA payload: headlines (1-5 @ 30ch), long_headline (1 @ 90ch), descriptions (1-5 @ 90ch), business_name (≤25ch), final_url
- At least one landscape AND one square marketing image (new URL or reuse via existing_images)

**Execution time:** 8-15 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for add_display_ad_group tool.\n\nAdds a new DISPLAY_STANDARD ad group (with its own targeting + a Responsive Display Ad)\nto an existing Display campaign.",
  "properties": {
    "campaign_id": {
      "description": "Existing Display campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "ad_group_name": {
      "description": "Name for the new ad group.",
      "title": "Ad Group Name",
      "type": "string"
    },
    "final_url": {
      "description": "Landing page URL (https).",
      "title": "Final Url",
      "type": "string"
    },
    "business_name": {
      "description": "Business name, max 25 chars.",
      "maxLength": 25,
      "title": "Business Name",
      "type": "string"
    },
    "headlines": {
      "description": "JSON ARRAY: 1-5 short headlines, each MAX 30 characters.",
      "items": {
        "type": "string"
      },
      "maxItems": 5,
      "minItems": 1,
      "title": "Headlines",
      "type": "array"
    },
    "long_headline": {
      "description": "Exactly 1 long headline, max 90 characters.",
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
      "description": "Landscape images (1.91:1). Required unless reusing via existing_images.",
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
      "description": "Square images (1:1). Required unless reusing via existing_images.",
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
      "description": "Optional square logos (1:1). Up to 5.",
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
      "description": "UUID from `validate_and_prepare_assets`. Pre-validated images get auto-mapped into this ad group's image fields. Recommended.",
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
      "description": "Optional YouTube video IDs (0-5).",
      "title": "Youtube Video Ids"
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
      "description": "Audience targeting. Keys: user_interests, custom_audiences, user_lists, combined_audiences. Use search_audiences — NEVER fabricate IDs.",
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
      "description": "Topic IDs or 'topicConstants/<id>' resource names.",
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
      "description": "Managed placements. List of {type, value}: type in ('website','mobile_app','youtube_channel','youtube_video').",
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
      "description": "Contextual display keywords. List of {text, negative?}.",
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
      "description": "Demographic targeting (exclude-the-inverse). Keys: age_ranges, genders, parental_statuses, income_ranges.",
      "title": "Demographics"
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
      "description": "Carry through campaign bidding (MANUAL_CPC/MANUAL_CPM needs cpc_bid/cpm_bid).",
      "title": "Bidding Strategy"
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
      "description": "Required for MANUAL_CPC.",
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
      "description": "Required for MANUAL_CPM.",
      "title": "Cpm Bid"
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
      "description": "CTA label.",
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
      "description": "ALL_FORMATS / NATIVE / NON_NATIVE.",
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
      "description": "Hex color.",
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
      "default": true,
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
      "title": "Promo Text"
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
    "ad_group_name",
    "final_url",
    "business_name",
    "headlines",
    "long_headline",
    "descriptions"
  ],
  "title": "AddDisplayAdGroupInput",
  "type": "object"
}
```

</details>

<a id="add_display_audiences"></a>

## `add_display_audiences`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add audience targeting to a Display ad group.

**audience_segments** keys:
- `user_interests` — list of affinity/in-market category IDs (from `search_audiences`)
- `custom_audiences` — list of resource names like `"customers/123/customAudiences/456"`
- `user_lists` — list of remarketing list resource names like `"customers/123/userLists/789"`
- `combined_audiences` — list of combined audience resource names

**CRITICAL:** Only use IDs returned by `search_audiences`. NEVER fabricate — wrong IDs waste budget on unrelated audiences.

**Example:**
```
audience_segments: {
  "user_interests": ["80517", "80520"],
  "user_lists": ["customers/123/userLists/111"]
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
    "audience_segments": {
      "additionalProperties": true,
      "description": "Object of audience lists to ADD to the ad group.\nInclude keys: user_interests (affinity/in-market IDs), custom_audiences (resource names), user_lists (resource names), combined_audiences (resource names).\nExclude keys (#559 — build NEGATIVE criteria): user_list_exclusions, user_interest_exclusions, custom_audience_exclusions, combined_audience_exclusions.\nShape-tolerant: a flat top-level list, a list of {user_list: rn} objects, and synonym keys are all accepted and normalized.\nUse search_audiences to get valid IDs — NEVER fabricate. Example: {'user_lists': ['customers/123/userLists/456'], 'user_list_exclusions': ['customers/123/userLists/789']}",
      "title": "Audience Segments",
      "type": "object"
    }
  },
  "required": [
    "ad_group_id",
    "audience_segments"
  ],
  "title": "AddDisplayAudiencesInput",
  "type": "object"
}
```

</details>

<a id="add_display_keywords"></a>

## `add_display_keywords`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add contextual display keywords to a Display ad group.

Display keywords are ALWAYS BROAD-match (Google ignores match_type for Display). Each keyword tells Google what context to show ads in — NOT what users are searching.

**Example:**
```
display_keywords: [
  {"text": "running shoes"},
  {"text": "cheap knockoff", "negative": true}
]
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
    "display_keywords": {
      "description": "List of {text, negative?} items. Display keywords are always BROAD-match.",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Display Keywords",
      "type": "array"
    }
  },
  "required": [
    "ad_group_id",
    "display_keywords"
  ],
  "title": "AddDisplayKeywordsInput",
  "type": "object"
}
```

</details>

<a id="add_display_placements"></a>

## `add_display_placements`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add managed placements (websites, mobile apps, YouTube channels, YouTube videos) to a Display ad group.

**Placement types:**
- `website` — value is a domain or URL (e.g., "nytimes.com")
- `mobile_app` — value is an app ID in format "mobileapp::1-com.example.app"
- `youtube_channel` — value is a channel ID (e.g., "UCxxxxx")
- `youtube_video` — value is a video ID (e.g., "dQw4w9WgXcQ")

**Example:**
```
placements: [
  {"type":"website","value":"nytimes.com"},
  {"type":"youtube_video","value":"dQw4w9WgXcQ"}
]
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
    "placements": {
      "description": "List of {type, value} placements. type in ('website','mobile_app','youtube_channel','youtube_video').",
      "items": {
        "additionalProperties": {
          "type": "string"
        },
        "type": "object"
      },
      "title": "Placements",
      "type": "array"
    }
  },
  "required": [
    "ad_group_id",
    "placements"
  ],
  "title": "AddDisplayPlacementsInput",
  "type": "object"
}
```

</details>

<a id="add_display_topics"></a>

## `add_display_topics`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add topic targeting to a Display ad group.

**topics** is a list of topic IDs or `topicConstants/<id>` resource names.
Example: `["topicConstants/1017", "1020"]` (the bare form gets auto-prefixed).

Topic IDs are published by Google at https://developers.google.com/google-ads/api/data/codes-formats#verticals

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
    "topics": {
      "description": "List of topic IDs or 'topicConstants/<id>' resource names.",
      "items": {
        "type": "string"
      },
      "title": "Topics",
      "type": "array"
    }
  },
  "required": [
    "ad_group_id",
    "topics"
  ],
  "title": "AddDisplayTopicsInput",
  "type": "object"
}
```

</details>

<a id="add_keywords"></a>

## `add_keywords`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add keywords to an existing ad group.

⚠️ **CRITICAL: Run `research_keywords` BEFORE using this tool!**

**MANDATORY WORKFLOW:**
1. Call `get_campaign_structure` to get ad_group_id and see existing keywords
2. Call `research_keywords` with business context to get quality keyword suggestions
3. Show keyword suggestions to user with CPC, search volume, intent level
4. Get user approval on which keywords to add
5. ONLY THEN call this tool with approved keywords

**Why research first?**
- Ensures keywords have real search volume
- Shows CPC costs so user understands budget impact
- Provides HIGH/MEDIUM/LOW intent classification
- Prevents adding low-quality or irrelevant keywords

**Requires:**
- ad_group_id: Get from get_campaign_structure (REQUIRED)
- keywords: List of keywords to add (from research_keywords results)

**Each keyword needs:**
- text: The keyword phrase (e.g., "buy running shoes online")
- match_type: EXACT, PHRASE, or BROAD (default: BROAD)
- cpc_bid_micros: Optional bid override (1 USD = 1,000,000 micros)

**Match Type Guide:**
- BROAD: Ads show for related searches (widest reach) - Google's 2025 recommendation
- PHRASE: Ads show when query contains keyword phrase
- EXACT: Ads show only for exact query or close variants

**IMPORTANT:**
- Keyword text and match_type CANNOT be changed after creation
- To "change" a keyword, remove the old one and add a new one
- Get ad_group_id from get_campaign_structure first

**Execution time:** 2-4 seconds

**Example Workflow:**
User: "Add more keywords to my plumbing campaign"

Agent Steps:
1. Call get_campaign_structure → get ad_group_id, see existing keywords
2. Call research_keywords with business_description="plumbing services"
3. Show user: "I found these keyword suggestions from Keyword Planner:
   - emergency plumber near me (HIGH intent, $45 CPC, 12K searches/mo)
   - 24 hour plumber (HIGH intent, $38 CPC, 8K searches/mo)
   Which would you like to add?"
4. User selects keywords
5. Call add_keywords with selected keywords

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding keywords to an ad group",
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID to add keywords to. Use get_campaign_structure first to find ad_group_id.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "keywords": {
      "description": "List of keywords to add. Each keyword: {text, match_type (EXACT/PHRASE/BROAD), cpc_bid_micros (optional)}",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Keywords",
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
    "ad_group_id",
    "keywords"
  ],
  "title": "AddKeywordsInput",
  "type": "object"
}
```

</details>

<a id="add_meta_ad"></a>

## `add_meta_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to add another ad/creative variation to an EXISTING ad set.

DO NOT USE to create a new campaign. For new campaigns:
- Video campaign - `create_meta_video_campaign`
- Image campaign - `create_meta_image_campaign`
- Carousel campaign - `create_meta_carousel_campaign`

Common scenarios:
- A/B test ad copy: Different headlines, primary text, or CTAs for the same audience
- A/B test creatives: Different images or videos for the same audience
- Format testing within one audience: Image vs video ad in the same ad set
- Dynamic Creative (DCO): Multiple images + text variations in one ad — Meta auto-optimizes

KEY DISTINCTION — add_meta_ad vs add_meta_ad_set:
- Same audience, different creative/copy - use THIS tool (add_meta_ad)
- Different audience/targeting - use `add_meta_ad_set` instead (creates a new ad set)

Ads in the same ad set SHARE: targeting, budget, schedule, pixel tracking.
Each ad has its OWN: creative (image/video/carousel), headline, primary text, CTA, landing page.

IMPORTANT: You need an ad_set_id from a previously created ad set. Use `list_meta_ad_sets` first if you don't have the ad_set_id.

Supports all 3 ad types + Dynamic Creative:
- `image`: Different image + copy variation
- `video`: Different video + copy variation
- `carousel`: Different card set + copy variation
- **Dynamic Creative (DCO)**: Pass `image_urls` (2-10 images), `headlines` (up to 5), `primary_texts` (up to 5), `descriptions` (up to 5). Meta tests ALL combinations and optimizes delivery automatically.

Dynamic Creative Optimization (DCO) workflow:
1. Create ad set with `is_dynamic_creative=true` via `add_meta_ad_set`
2. Call this tool with `image_urls` (list of 2-10 image URLs), plus optional `headlines`, `primary_texts`, `descriptions` arrays
3. Meta will test all image × headline × text combinations and optimize
4. DCO ad sets support only 1 ad — if the ad set already has is_dynamic_creative enabled, this tool auto-detects it
Note: Cannot mix image_urls (DCO) with image_url (single image) or placement-specific images.

Standard workflow:
1. Get ad_set_id from prior campaign creation or `list_meta_ad_sets`
2. Write variant ad copy (different headline/primary_text/image)
3. Call this tool with ad_set_id + new creative + copy

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding a new ad to an existing ad set",
  "properties": {
    "ad_set_id": {
      "description": "**REQUIRED.** The Meta Ad Set ID to add the ad to. If you don't have it, call `list_meta_ad_sets` first. Example: '120209876543210'.",
      "title": "Ad Set Id",
      "type": "string"
    },
    "ad_type": {
      "description": "**REQUIRED.** Type of ad: 'image', 'video', or 'carousel'. Must match the creative source you're providing — image needs image_url/hash/bundle, video needs video_url/existing_video_id, carousel needs cards.",
      "title": "Ad Type",
      "type": "string"
    },
    "auto_copy_creative": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "When True and `existing_image_hash` (or carousel card image_hash) belongs to a DIFFERENT connected Meta account than `ad_account_id`, the image is automatically copied to the target account and the new hash is used in the ad. Default False = pre-validation blocks with an actionable error. ⚠️ **ASK THE USER FIRST.** Auto-copy creates a new image asset in the target Meta account. On accounts with many creatives (e.g. a library of seasonal images), running auto-copy can be wasteful and surprising. Only set this flag after the user explicitly confirms they want the asset copied. Does not apply to videos (`existing_video_id` mismatches still require manual handling).",
      "title": "Auto Copy Creative"
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
      "description": "Image URL (for image type)",
      "title": "Image Url"
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
      "description": "Existing Meta image hash. For image ads, this is the image itself. For video ads, doubles as the video thumbnail (used when Meta's auto-generated thumbnail edge stays empty after upload, which happens for 10-30s on freshly uploaded videos).",
      "title": "Existing Image Hash"
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
      "description": "Asset bundle ID",
      "title": "Asset Bundle Id"
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
      "description": "Image URL for Stories/Reels (9:16, recommended 1080x1920px). Uses asset_feed_spec for placement-specific creatives.",
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
      "description": "Image URL for Right Column (1.91:1, recommended 1200x628px). Uses asset_feed_spec for placement-specific creatives.",
      "title": "Right Column Image Url"
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
      "description": "Video URL (for video type)",
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
      "description": "Existing video ID",
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
      "description": "Custom thumbnail URL",
      "title": "Thumbnail Url"
    },
    "placement_specific_videos": {
      "anyOf": [
        {
          "additionalProperties": {
            "type": "string"
          },
          "type": "object"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Map of placement name → video URL or existing Meta video ID. Keys: 'feed' (1:1 or 16:9 horizontal), 'stories_reels' (9:16 vertical), 'right_column' (1.91:1). Values: public MP4 URL or existing video ID. Backend uploads each, resolves thumbnails, builds asset_feed_spec.videos[] + asset_customization_rules[] mapping each video to its placement. Mutually exclusive with video_url / existing_video_id. ad_type='video' only.",
      "title": "Placement Specific Videos"
    },
    "cards": {
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
      "description": "Carousel cards (2-10). Each card MUST have: `headline` and ONE of `existing_image_hash` (preferred — use the hash from `discover_meta_assets`) OR `image_url` (will upload). `image_hash` is accepted as an alias for `existing_image_hash`. Per-card `landing_page_url` is optional — falls back to the carousel-level `landing_page_url` if omitted. Video-only cards (`video_id` / `existing_video_id` without an image source) are NOT supported; use `create_meta_video_campaign` for video ads. Optional per-card keys: `description` (≤20 chars), `call_to_action`.",
      "title": "Cards"
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
      "description": "Primary ad text (max 2200 chars, recommended 125). Provide EITHER this (single) OR `primary_texts` (a 2-5 item list for dynamic creative). One of the two is REQUIRED. Ask the user before calling. Supports emojis and line breaks. ⚠️ If the user gives you 2+ primary text variations, put ALL of them in `primary_texts` (one Dynamic-Creative ad) — do not pick one for this field.",
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
      "description": "Headline (max 255 chars, recommended 40). If the user gives you 2+ headline variations, use the `headlines` array instead of this single field.",
      "title": "Headline"
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
      "description": "Description (max 255 chars, recommended 30). For 2+ description variations use the `descriptions` array instead.",
      "title": "Description"
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
      "description": "Optional display URL (caption) shown in the ad instead of the full landing page URL (e.g. 'brand.com'). Must match or redirect to the landing_page_url domain. NOT supported for ad_type='video'.",
      "title": "Display Link"
    },
    "image_urls": {
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
      "description": "List of image URLs for multi-image Dynamic Creative (2-10). Meta automatically tests all combinations and optimizes delivery. Only valid with ad_type='image'. Mutually exclusive with image_url/existing_image_hash/story_image_url.",
      "title": "Image Urls"
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
      "description": "List of headline variations (2-5). **USE THIS whenever the user gives you 2+ headlines** — one ad, Meta tests the combinations (Dynamic Creative); do not pick one into the singular headline field. Works with image_urls (multi-image DCO) OR on a single image/video. Not supported for carousel — use per-card cards[].headline.",
      "title": "Headlines"
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
      "description": "List of primary text variations (2-5). **USE THIS whenever the user gives you 2+ primary texts** — one ad, Meta tests the combinations (Dynamic Creative); do not pick one into the singular primary_text field. Works with image_urls (multi-image DCO) OR on a single image/video. Not supported for carousel.",
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
      "description": "List of description variations (up to 5). Works with image_urls (multi-image DCO) OR on a single image/video (multi-text A/B testing without DCO). Not supported for carousel — use per-card cards[].description.",
      "title": "Descriptions"
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
      "description": "Lead form ID for OUTCOME_LEADS campaigns. If not provided, auto-fetched from the ad set's campaign.",
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
      "description": "Custom name for the ad. Also accepts 'name' as alias.",
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
      "description": "Set to false to opt out of Meta's multi-advertiser ad format at the creative level. Default (None) = Meta's default behavior (enrolled).",
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
      "description": "URL parameters (e.g. 'utm_source=meta&utm_medium=cpc&utm_campaign=...') appended to the landing-page URL on every click. Use for UTM tracking. Leading '?' is stripped automatically. Set at the creative level — applies to every click on this ad.",
      "title": "Url Tags"
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
      "description": "Master switch for Meta's Advantage+ Creative AI enhancements. Set False to opt OUT of ALL granular enhancements at once. Leave None or True to keep Meta's defaults.",
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
      "description": "List of granular Advantage+ Creative features to opt OUT of individually. 'standard_enhancements' rejected (deprecated in Meta API v22, breaks duplicate_campaign).",
      "title": "Disabled Creative Features"
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
      "description": "Optional iOS deep link to open a specific app screen (e.g. 'myapp://product/123'). Only takes effect when the parent ad set's campaign is OUTCOME_APP_PROMOTION.",
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
      "description": "Optional Android deep link (e.g. 'myapp://product/123' or 'intent://...'). Only takes effect when the parent ad set's campaign is OUTCOME_APP_PROMOTION.",
      "title": "Deep Link Url Android"
    }
  },
  "required": [
    "ad_set_id",
    "ad_type",
    "landing_page_url"
  ],
  "title": "AddMetaAdInput",
  "type": "object"
}
```

</details>

<a id="add_meta_ad_set"></a>

## `add_meta_ad_set`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to add a new ad set to an EXISTING campaign.

Common scenarios:
- Audience testing: Same ad format, different targeting/interests per ad set (e.g., "4 ad sets with different interests")
- Multi-format: Different ad types (image + video + carousel) under one campaign
- Budget split: Same creative, different budgets per audience segment
- Scaling: Adding new audiences/markets to an existing campaign
WhatsApp campaigns (destination_type='WHATSAPP'): if the customer's Page has more than one
WhatsApp number, ASK WHICH ONE should receive conversations and pass whatsapp_phone_number.
Leave it out and Meta picks a number itself, which may not be the one they expect.
- Geographic split: Same ad, different locations per ad set
- Dynamic Creative (DCO): Set is_dynamic_creative=true, then use add_meta_ad with image_urls/headlines/primary_texts

CRITICAL: Each `create_meta_*_campaign` creates a NEW campaign.
To add more ad sets to the SAME campaign, you MUST use this tool.
NEVER call create_meta_*_campaign again for the same campaign.

IMPORTANT: You need a campaign_id from a previously created campaign. Use `get_meta_campaign_details` first if you don't have the campaign_id.

Supports all 3 ad types:
- `image`: Provide image_url, existing_image_hash, or asset_bundle_id
- `video`: Provide video_url or existing_video_id
- `carousel`: Provide cards array (2-10 cards)

Dynamic Creative Optimization (DCO):
- Set `is_dynamic_creative=true` when creating the ad set
- Then use `add_meta_ad` with `image_urls` (2-10), `headlines` (up to 5), `primary_texts` (up to 5) to add a DCO ad
- Meta automatically tests all asset combinations and optimizes delivery
- DCO ad sets support only 1 ad — one ad with multiple asset variations

Each ad set has INDEPENDENT: targeting, budget, schedule, pixel/conversion tracking.
Shared from campaign: objective, campaign name.

**CBO (Advantage Campaign Budget) campaigns:**
If the campaign uses CBO (campaign_budget_optimization=true when created), you MUST:
- Set `campaign_budget_optimization: true` on this tool call
- Do NOT set `budget_daily` (budget is managed at campaign level)
- Optionally set `daily_min_spend_target` and `daily_spend_cap` to control spend distribution
If the campaign does NOT use CBO, `budget_daily` is required as usual.

Workflow:
1. Create initial campaign with `create_meta_*_campaign` - get campaign_id
2. Call this tool with the campaign_id for each additional ad set
3. Use `add_meta_ad` to add more ad copies/creatives within any ad set

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding a new ad set to an existing campaign",
  "properties": {
    "campaign_id": {
      "description": "The Meta Campaign ID to add the ad set to (required). Get this from a prior create_meta_*_campaign call or get_meta_campaign_details.",
      "title": "Campaign Id",
      "type": "string"
    },
    "ad_type": {
      "description": "Type of ad: 'image', 'video', or 'carousel'",
      "title": "Ad Type",
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
      "description": "Daily budget for this ad set in the ad account's OWN CURRENCY as a decimal — NOT cents, and NOT converted to USD. For 20/day send 20, not 2000. Required for non-CBO campaigns. Do NOT set for CBO campaigns — budget is managed at campaign level. Use daily_min_spend_target/daily_spend_cap instead.",
      "title": "Budget Daily"
    },
    "campaign_budget_optimization": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Set to true if the parent campaign uses Advantage Campaign Budget (CBO). When true, budget_daily is not required and bid_strategy is skipped on the ad set.",
      "title": "Campaign Budget Optimization"
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
      "description": "CBO only: minimum daily spend for this ad set in account currency.",
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
      "description": "CBO only: maximum daily spend cap for this ad set in account currency.",
      "title": "Daily Spend Cap"
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
      "description": "Public URL of image to use (for image ad_type)",
      "title": "Image Url"
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
      "description": "Existing Meta image hash (for image ad_type)",
      "title": "Existing Image Hash"
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
      "description": "Asset bundle ID from validate_and_prepare_meta_assets (for image ad_type)",
      "title": "Asset Bundle Id"
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
      "description": "Public URL of video to upload (for video ad_type)",
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
      "description": "Existing Meta video ID (for video ad_type)",
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
      "description": "Custom thumbnail URL for video",
      "title": "Thumbnail Url"
    },
    "cards": {
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
      "description": "Carousel cards (2-10). Each: {image_url, headline, landing_page_url, description?, call_to_action?}",
      "title": "Cards"
    },
    "primary_text": {
      "description": "**REQUIRED.** Primary ad text (max 2200 chars, recommended 125). Ask the user for it before calling. Supports emojis and line breaks.",
      "maxLength": 2200,
      "title": "Primary Text",
      "type": "string"
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
      "description": "Headline (max 255 chars, recommended 40)",
      "title": "Headline"
    },
    "landing_page_url": {
      "description": "**REQUIRED.** Landing page URL (HTTPS). Ask the user for it before calling.",
      "title": "Landing Page Url",
      "type": "string"
    },
    "call_to_action": {
      "default": "LEARN_MORE",
      "description": "CTA button: LEARN_MORE, SHOP_NOW, SIGN_UP, etc.",
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
      "description": "Description (max 255 chars, recommended 30)",
      "title": "Description"
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
      "description": "Optional display URL (caption) shown in the ad instead of the full landing page URL (e.g. 'brand.com'). Must match or redirect to the landing_page_url domain. NOT supported for ad_type='video'.",
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
      "description": "Advantage+ Audience on/off. When True, interests/behaviors/custom_audiences are treated as suggestions and Meta expands delivery beyond them. When False/None, strict filter behavior. Incompatible with special ad categories.",
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
      "description": "Master switch for Meta's Advantage+ Creative AI enhancements. Set False to opt OUT of ALL granular enhancements at once. Leave None or True to keep Meta's defaults.",
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
      "description": "List of granular Advantage+ Creative features to opt OUT of individually (image_auto_crop, enhance_cta, text_optimizations, etc.). 'standard_enhancements' rejected — Meta deprecated it in v22 and it breaks duplicate_campaign (error_subcode 3858504).",
      "title": "Disabled Creative Features"
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
      "description": "Location targeting. Country codes (['US']) or location objects from search_meta_targeting ([{'key': '2421836', 'type': 'city', 'radius': 25, 'distance_unit': 'mile'}]). ALWAYS include the 'type' field (city/region/zip/place) on each object — a key with no type is treated as a country code and rejected by Meta. For ~dozens of cities each with a radius, pass one object per city. Default: ['US']",
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
      "maximum": 65,
      "minimum": 18,
      "title": "Age Min",
      "type": "integer"
    },
    "age_max": {
      "default": 65,
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
      "title": "Behaviors"
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
      "title": "Excluded Custom Audiences"
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
      "description": "Lead form ID for OUTCOME_LEADS campaigns. If not provided, auto-fetched from existing campaign ads.",
      "title": "Lead Form Id"
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
      "description": "Meta Pixel ID for conversion tracking",
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
      "description": "Meta Pixel Standard Event to optimize for. Options: PURCHASE, LEAD, COMPLETE_REGISTRATION, ADD_TO_CART, INITIATED_CHECKOUT, ADD_PAYMENT_INFO, SEARCH, CONTENT_VIEW, OTHER. Use OTHER with custom_conversion_id for custom-conversion rules, or with custom_event_str for arbitrary pixel events. NOTE: LANDING_PAGE_VIEWS / LINK_CLICKS / IMPRESSIONS / REACH are `optimization_goal` values, not pixel events — do not set those here.",
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
      "description": "Custom conversion ID for optimizing towards a specific custom conversion. When provided, pixel_event_name is ignored — Meta infers the event type from the custom conversion.",
      "title": "Custom Conversion Id"
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
      "description": "Custom name for the ad set",
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
      "description": "Custom name for the ad created inside the ad set",
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
    "multi_share_optimized": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": true,
      "description": "For carousel: optimize card order",
      "title": "Multi Share Optimized"
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
      "description": "Lifetime budget for this ad set in the ad account's OWN CURRENCY as a decimal (NOT cents, NOT USD; minimum 1). Mutually exclusive with budget_daily. Requires end_time to be set. Cannot be used with CBO campaigns.",
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
      "description": "End date/time for this ad set in ISO format (e.g., 2026-04-30T23:59:59). Required when using budget_lifetime. Optional with budget_daily.",
      "title": "End Time"
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
      "description": "Set to false to opt out of Meta's multi-advertiser ad format at the creative level. When false, sets contextual_multi_ads.enroll_status=OPT_OUT on the ad creative. Default (None) = Meta's default behavior (enrolled).",
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
      "description": "Which platforms to run on: ['facebook', 'instagram', 'audience_network', 'messenger']. Only listed platforms are included. Default: automatic (all).",
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
      "description": "Facebook placements: feed, right_hand_column, story, facebook_reels, marketplace, search, etc. Only listed positions are included.",
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
      "description": "Instagram placements: stream (feed), story, reels, explore, explore_home, ig_search, profile_feed. Only listed positions are included.",
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
      "description": "Facebook App ID (numeric). Required when adding an ad set to an OUTCOME_APP_PROMOTION campaign. NOT the iOS bundle ID or Android package name.",
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
      "description": "App Store / Play Store URL. Required when adding an ad set to an OUTCOME_APP_PROMOTION campaign. The ad set's OS targeting is set from this URL automatically (override with user_os).",
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
      "description": "Operating system to target: 'iOS' or 'Android'. Usually OMIT — derived from app_store_url. Meta REJECTS an ad set whose OS targeting disagrees with the promoted app's platform ('Mobile Targeting Mismatch').",
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
      "description": "Optional in-app event to optimize for (PURCHASE, LEVEL_ACHIEVED, COMPLETE_REGISTRATION, etc.). Defaults to APP_INSTALLS when omitted.",
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
      "description": "Optional iOS deep link (e.g. 'myapp://product/123').",
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
      "description": "Optional Android deep link (e.g. 'myapp://product/123').",
      "title": "Deep Link Url Android"
    },
    "is_dynamic_creative": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Set to true to enable Dynamic Creative Optimization on this ad set. Meta will test combinations of images, headlines, and text to find the best performer. Only 1 ad is allowed per DCO ad set. Use with add_meta_ad's image_urls/headlines/primary_texts fields.",
      "title": "Is Dynamic Creative"
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
      "description": "Override the ad set destination type. Set to 'WEBSITE' for OUTCOME_LEADS campaigns that track conversions on your website via Meta Pixel instead of using Meta's built-in lead form. Set to 'WHATSAPP' for a WhatsApp-native (Click-to-WhatsApp) ad set — requires the parent campaign objective to be OUTCOME_ENGAGEMENT (or OUTCOME_LEADS) and facebook_page_id. Options: WEBSITE, ON_AD, WEBSITE_AND_ON_AD, WHATSAPP.",
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
      "description": "For destination_type='WHATSAPP' only. The greeting shown when the WhatsApp chat opens from the ad. Ignored for non-WhatsApp ad sets.",
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
      "description": "For destination_type='WHATSAPP' only. Quick-reply prompt buttons shown when the WhatsApp chat opens (e.g. ['See pricing', 'Book a visit']). Ignored for non-WhatsApp ad sets.",
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
      "description": "EU Digital Services Act beneficiary — the entity (usually the advertiser's business/legal name) that benefits from this ad. REQUIRED by Meta when the ad set targets any EU/EEA country (e.g. Spain, Germany, France). Ignored for non-EU targeting. Example: 'Acme Inc'.",
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
      "description": "EU DSA payor — the entity paying for the ad. Optional; defaults to dsa_beneficiary when omitted. Only needed if the payor differs from the beneficiary.",
      "title": "Dsa Payor"
    }
  },
  "required": [
    "campaign_id",
    "ad_type",
    "primary_text",
    "landing_page_url"
  ],
  "title": "AddMetaAdSetInput",
  "type": "object"
}
```

</details>

<a id="add_meta_catalog_ad"></a>

## `add_meta_catalog_ad`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to add ANOTHER catalog ad to an existing catalog ad set — e.g. to test multiple creatives (different copy, CTA, or product set on the creative) within one ad set. Adds the ad PAUSED.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Add ANOTHER catalog ad (its own copy/CTA/product-set-on-creative/landing) to an\nEXISTING catalog ad set — for testing multiple creatives in one ad set.",
  "properties": {
    "ad_set_id": {
      "description": "The existing catalog ad set ID to add the ad to.",
      "title": "Ad Set Id",
      "type": "string"
    },
    "product_set_id": {
      "description": "Product set for this ad's creative (required).",
      "title": "Product Set Id",
      "type": "string"
    },
    "primary_text": {
      "description": "Primary ad text.",
      "title": "Primary Text",
      "type": "string"
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
      "description": "Headline (defaults to {{product.name}}).",
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
      "description": "Description (defaults to {{product.current_price}}).",
      "title": "Description"
    },
    "call_to_action": {
      "default": "SHOP_NOW",
      "description": "CTA button type.",
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
      "description": "Storefront URL (derived from the catalog if omitted).",
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
      "description": "Instagram account ID (auto-detected).",
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
      "description": "Custom ad name.",
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
      "description": "Meta ad account ID. Auto-detected if omitted.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "ad_set_id",
    "product_set_id",
    "primary_text"
  ],
  "title": "AddMetaCatalogAdInput",
  "type": "object"
}
```

</details>

<a id="add_meta_catalog_ad_set"></a>

## `add_meta_catalog_ad_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to add ANOTHER ad set to an existing Advantage+ Catalog campaign — e.g. one campaign running multiple strategies in parallel: ad set A = prospecting, ad set B = viewed-not-purchased retargeting, ad set C = a different product set or budget. Each catalog ad set independently controls its product set, audience strategy, budget, targeting, and retention window. The catalog is inherited from the parent campaign.

Use this AFTER create_meta_catalog_campaign to layer on more ad sets. Adds the ad set + its first catalog ad, PAUSED.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Add a NEW catalog ad set (+ its first ad) to an EXISTING catalog campaign.\nEach ad set independently controls its product set, audience, budget and targeting\n— e.g. one campaign with ad set A = prospecting, ad set B = viewed-not-purchased\nretargeting, ad set C = a different product set. The catalog is inherited from the\nparent campaign.",
  "properties": {
    "campaign_id": {
      "description": "The existing Advantage+ Catalog campaign ID to add the ad set to. Get it from create_meta_catalog_campaign or list_meta_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "product_set_id": {
      "description": "Product set this ad set promotes (required). From list_meta_product_sets.",
      "title": "Product Set Id",
      "type": "string"
    },
    "primary_text": {
      "description": "Primary ad text for this ad set's first ad.",
      "title": "Primary Text",
      "type": "string"
    },
    "audience_type": {
      "default": "prospecting",
      "description": "'prospecting' (broad) or 'retargeting' (pixel product audience). Retargeting REQUIRES pixel_id.",
      "title": "Audience Type",
      "type": "string"
    },
    "destination_type": {
      "default": "WEBSITE",
      "description": "'WEBSITE' (default) or 'FACEBOOK' (on-Facebook Shop).",
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
      "description": "Daily budget for THIS ad set in the account's own currency as a decimal — NOT cents, NOT USD (for 20/day send 20, not 2000). Provide unless the campaign uses CBO.",
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
      "description": "Lifetime budget for this ad set in the account's own currency as a decimal — NOT cents, NOT USD (requires end_time).",
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
      "description": "Meta ad account ID. Auto-detected if omitted.",
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
      "description": "Headline (defaults to {{product.name}}).",
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
      "description": "Description (defaults to {{product.current_price}}).",
      "title": "Description"
    },
    "call_to_action": {
      "default": "SHOP_NOW",
      "description": "CTA button type.",
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
      "description": "Storefront URL (derived from the catalog if omitted).",
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
      "description": "Instagram account ID (auto-detected).",
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
      "description": "Pixel ID. REQUIRED for retargeting.",
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
      "description": "Conversion event (default PURCHASE).",
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
      "description": "viewed_not_purchased | carted_not_purchased | all_engaged_not_purchased | cross_sell_purchasers | custom.",
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
      "description": "Retargeting lookback window (days).",
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
      "description": "Country codes (default ['US']).",
      "title": "Locations"
    },
    "age_min": {
      "default": 18,
      "description": "Min age.",
      "title": "Age Min",
      "type": "integer"
    },
    "age_max": {
      "default": 65,
      "description": "Max age.",
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
      "description": "['male']/['female']/omit.",
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
      "description": "Interest targeting specs.",
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
      "description": "Behavior targeting specs.",
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
      "description": "Custom audience IDs to include.",
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
      "description": "Advantage+ Audience expansion.",
      "title": "Advantage Audience"
    },
    "campaign_budget_optimization": {
      "default": false,
      "description": "Set true if the parent campaign uses CBO (then omit budget_daily).",
      "title": "Campaign Budget Optimization",
      "type": "boolean"
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
    "campaign_id",
    "product_set_id",
    "primary_text"
  ],
  "title": "AddMetaCatalogAdSetInput",
  "type": "object"
}
```

</details>

<a id="add_negative_keywords"></a>

## `add_negative_keywords`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add negative keywords to a campaign.

Negative keywords prevent your ads from showing for certain searches.
They help save budget by avoiding irrelevant clicks.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED - get from list_campaigns)
- keywords: List of negative keywords to add
- customer_id: Optional

**Each keyword needs:**
- text: The keyword phrase (e.g., "free", "cheap", "diy")
- match_type: EXACT, PHRASE, or BROAD (default: BROAD)

**Campaign-level vs Ad Group-level:**
This adds negative keywords at CAMPAIGN level, affecting ALL ad groups.

**Common negative keywords:**
- "free", "cheap", "discount" (for premium brands)
- "jobs", "salary", "careers" (for product companies)
- "diy", "how to", "tutorial" (for service providers)

**Execution time:** 2-4 seconds

**Example:**
User: "Block searches containing 'free' and 'cheap'"
Agent: Uses add_negative_keywords with campaign_id and keywords list

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding negative keywords to a campaign",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to add negative keywords to. Use list_campaigns first.",
      "title": "Campaign Id",
      "type": "string"
    },
    "keywords": {
      "description": "List of negative keywords. Each: {text, match_type (EXACT/PHRASE/BROAD)}. These prevent ads from showing for unwanted searches.",
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Keywords",
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
    "campaign_id",
    "keywords"
  ],
  "title": "AddNegativeKeywordsInput",
  "type": "object"
}
```

</details>

<a id="add_negative_keywords_to_list"></a>

## `add_negative_keywords_to_list`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add negative keywords to a SHARED negative keyword list.

Adds negatives to a reusable list (SharedSet), so every campaign the list is
attached to blocks those searches at once — no need to repeat per campaign.

**Parameters:**
- shared_set_id (required — from list_negative_keyword_lists)
- keywords (required): each {text, match_type} — match_type EXACT, PHRASE, or BROAD (default BROAD)

**Use when:** "add these negatives to my shared list", "block 'free', 'cheap' across
all my campaigns via the list".

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "_NegKeywordItem": {
      "properties": {
        "text": {
          "description": "The negative keyword phrase.",
          "title": "Text",
          "type": "string"
        },
        "match_type": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": "BROAD",
          "description": "EXACT, PHRASE, or BROAD (default BROAD).",
          "title": "Match Type"
        }
      },
      "required": [
        "text"
      ],
      "title": "_NegKeywordItem",
      "type": "object"
    }
  },
  "description": "Add negative keywords to a shared list.",
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
    "keywords": {
      "description": "Negative keywords to add, each {text, match_type}. match_type EXACT/PHRASE/BROAD (default BROAD).",
      "items": {
        "$ref": "#/$defs/_NegKeywordItem"
      },
      "title": "Keywords",
      "type": "array"
    }
  },
  "required": [
    "shared_set_id",
    "keywords"
  ],
  "title": "AddNegativeKeywordsToListInput",
  "type": "object"
}
```

</details>

<a id="add_placement_exclusions"></a>

## `add_placement_exclusions`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Exclude placements — add negative placement criteria so your ads STOP serving on specific websites, YouTube channels/videos, or apps. This is the write side that closes the optimization loop after `get_placement_performance` finds wasted or off-target placements.

**What it does:** adds NEGATIVE placement criteria at the campaign level (applies to all ad groups) OR a single ad-group level. It is non-destructive — it does NOT pause or delete any campaign, ad group, ad, or existing targeting; it only prevents future serving on the placements you list. (To undo, the negative criterion can be removed later.)

**Scope — provide exactly ONE:**
- `campaign_id` — exclude across the whole campaign (all ad groups)
- `ad_group_id` — exclude only within that ad group

**Placements** — a list of `{type, value}`:
- `WEBSITE` → value = domain/url (e.g. `msn.com`)
- `YOUTUBE_CHANNEL` → value = channel id
- `YOUTUBE_VIDEO` → value = video id
- `MOBILE_APPLICATION` → value = app id

Typically you take the `target_url` / `display_name` of placements that `get_placement_performance` shows with spend but zero conversions, and pass them here.

**Returns:** which placements were `added` (with their criterion resource names) and which were `skipped` (invalid type/empty value), plus counts. Invalid rows are reported, never silently dropped.

**Parameters:**
- customer_id: Optional (uses connected account if omitted)
- campaign_id OR ad_group_id: exactly one (required)
- placements: list of {type, value} (required)

**Use this tool when:**
- User wants to exclude wasteful placements found via `get_placement_performance`
- User says "block ads on <site>", "exclude this channel/app", "stop showing on these placements"

**Tip:** Pair with `get_placement_performance` (`zero_conversions_only=true` + `min_cost`) to find the waste, then exclude it here in the same workflow.

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "PlacementExclusionItem": {
      "description": "One placement to exclude.",
      "properties": {
        "type": {
          "description": "Placement type: WEBSITE | YOUTUBE_CHANNEL | YOUTUBE_VIDEO | MOBILE_APPLICATION.",
          "title": "Type",
          "type": "string"
        },
        "value": {
          "description": "The identifier: WEBSITE=domain/url (e.g. 'msn.com'); YOUTUBE_CHANNEL=channel id; YOUTUBE_VIDEO=video id; MOBILE_APPLICATION=app id.",
          "title": "Value",
          "type": "string"
        }
      },
      "required": [
        "type",
        "value"
      ],
      "title": "PlacementExclusionItem",
      "type": "object"
    }
  },
  "description": "Input schema for add_placement_exclusions tool (negative placement criteria).",
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
      "description": "Exclude at CAMPAIGN level (applies to all ad groups). Use this OR ad_group_id, not both.",
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
      "description": "Exclude at AD-GROUP level (only that ad group). Use this OR campaign_id, not both.",
      "title": "Ad Group Id"
    },
    "placements": {
      "description": "Placements to exclude. Each is {type, value}. Typically sourced from get_placement_performance (e.g. placements with spend but zero conversions).",
      "items": {
        "$ref": "#/$defs/PlacementExclusionItem"
      },
      "title": "Placements",
      "type": "array"
    },
    "raw_data": {
      "default": false,
      "description": "Return the raw JSON result instead of the formatted summary.",
      "title": "Raw Data",
      "type": "boolean"
    }
  },
  "required": [
    "placements"
  ],
  "title": "AddPlacementExclusionsInput",
  "type": "object"
}
```

</details>

<a id="add_pmax_asset_group"></a>

## `add_pmax_asset_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a NEW asset group to an EXISTING Performance Max campaign.

Takes the same asset-group shape as create_pmax_campaign and builds the group
atomically (assets + links + search themes + audience signals in one call).
The new group is created **PAUSED** — enable it with update_pmax_asset_group.

**Required in asset_group:** name, final_urls, headlines (3-15),
descriptions (2-5), business_name, logo_images, marketing_images (landscape),
square_marketing_images. Google rejects groups missing required asset types.

**Optional:** long_headlines, portrait_marketing_images, youtube_video_ids,
search_themes (auto-derived from headlines if omitted), audience_signals.

**Parameters:**
- campaign_id: The PMax campaign ID (REQUIRED)
- asset_group: The group config object (REQUIRED — see shape above)
- auto_truncate: Auto-fix text over character limits (default: true)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 10-30 seconds (uploads images, atomic mutate)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding a NEW asset group to an EXISTING PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "asset_group": {
      "additionalProperties": true,
      "description": "Asset group config — SAME shape as one create_pmax_campaign asset_groups[] entry. Required keys: name, final_urls (list), headlines (3-15), descriptions (2-5), business_name, logo_images ([{url,name?}]), marketing_images (landscape 1.91:1), square_marketing_images (1:1). Optional: long_headlines (1-5), portrait_marketing_images, youtube_video_ids, search_themes (auto-derived from headlines if omitted), audience_signals ({in_market_audience_ids, affinity_audience_ids, custom_audience_ids, user_list_ids}), existing_images (reuse Asset Library images by resource name: {marketing_images_landscape, marketing_images_square, logos_square} — from discover_existing_assets).",
      "title": "Asset Group",
      "type": "object"
    },
    "auto_truncate": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": true,
      "description": "Auto-truncate text that exceeds Google character limits instead of rejecting (default: true).",
      "title": "Auto Truncate"
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
    "asset_group"
  ],
  "title": "AddPMaxAssetGroupInput",
  "type": "object"
}
```

</details>

<a id="add_pmax_asset_group_asset"></a>

## `add_pmax_asset_group_asset`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add ONE text or video asset to a Performance Max asset group.

Text slots (pass `text`): HEADLINE (≤30 chars), LONG_HEADLINE (≤90),
DESCRIPTION (≤90), BUSINESS_NAME (≤25). Video (pass `youtube_video_id`):
YOUTUBE_VIDEO. Over-limit text is auto-truncated. Per-group maxima are
enforced (15 headlines / 5 long headlines / 5 descriptions / 1 business name
/ 5 videos) — you'll get a clear error if the slot is full.

**Use when:**
- "Add a headline 'Summer Sale' to the PMax group" → field_type=HEADLINE, text=...
- "Attach this YouTube video to the asset group" → field_type=YOUTUBE_VIDEO, youtube_video_id=...

**Parameters:**
- campaign_id: The PMax campaign ID (REQUIRED)
- field_type: The slot (REQUIRED — see list above)
- text: For text slots (REQUIRED for those)
- youtube_video_id: For YOUTUBE_VIDEO (REQUIRED for that)
- asset_group_id: Required if the campaign has 2+ groups
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-5 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding a text/video asset to a PMax asset group.",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "field_type": {
      "description": "Asset slot: HEADLINE (max 30 chars), LONG_HEADLINE (max 90), DESCRIPTION (max 90), BUSINESS_NAME (max 25), or YOUTUBE_VIDEO. Use add_pmax_asset_group_image for images.",
      "title": "Field Type",
      "type": "string"
    },
    "text": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "The text — REQUIRED for HEADLINE/LONG_HEADLINE/DESCRIPTION/BUSINESS_NAME. Over-limit text is truncated.",
      "title": "Text"
    },
    "youtube_video_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "The YouTube video ID (11 chars) — REQUIRED for YOUTUBE_VIDEO. e.g. 'dQw4w9WgXcQ'.",
      "title": "Youtube Video Id"
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
      "description": "Required when the campaign has more than one asset group. Get IDs from get_pmax_asset_groups.",
      "title": "Asset Group Id"
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
    "field_type"
  ],
  "title": "AddPMaxAssetGroupAssetInput",
  "type": "object"
}
```

</details>

<a id="add_pmax_asset_group_image"></a>

## `add_pmax_asset_group_image`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Upload a new image and link it to a PMax asset group.

Accepts http(s) URLs OR base64 data URIs (`data:image/...;base64,...`).
Per-group caps are enforced BEFORE upload: 20 marketing images per group
(across MARKETING_IMAGE / SQUARE_MARKETING_IMAGE / PORTRAIT_MARKETING_IMAGE /
TALL_PORTRAIT_MARKETING_IMAGE), 5 of each logo type (LOGO / LANDSCAPE_LOGO /
BUSINESS_LOGO).

If the campaign has exactly one asset group, `asset_group_id` is optional —
otherwise it is required. Image bytes are uploaded only after cap validation
passes, so a doomed call doesn't burn bandwidth.

**Parameters:**
- campaign_id: The PMax campaign ID
- image_url: http(s) URL or `data:image/...;base64,...` URI
- field_type: which PMax image slot to fill (see list of accepted values)
- asset_group_id: required for multi-group campaigns
- asset_name: optional display name in the Asset Library

**Execution time:** 3-8 seconds (image fetch + Google Ads mutate)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for uploading + linking an image to a PMax asset group.",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "image_url": {
      "description": "Image to upload. Either a public http(s) URL OR a base64 data URI (`data:image/png;base64,...`). Plain base64 without the data-URI prefix is NOT accepted — wrap it as `data:image/...;base64,...`.",
      "title": "Image Url",
      "type": "string"
    },
    "field_type": {
      "description": "PMax image slot. One of: MARKETING_IMAGE, SQUARE_MARKETING_IMAGE, PORTRAIT_MARKETING_IMAGE, TALL_PORTRAIT_MARKETING_IMAGE, LOGO, LANDSCAPE_LOGO, BUSINESS_LOGO. Per-group caps: 20 marketing images total (across the 4 marketing types), 5 of each logo type.",
      "title": "Field Type",
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
      "description": "Required when the campaign has more than one asset group. Auto-resolved when there is exactly one.",
      "title": "Asset Group Id"
    },
    "asset_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display name for the new asset in the Google Ads Asset Library.",
      "title": "Asset Name"
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
    "image_url",
    "field_type"
  ],
  "title": "AddPMaxAssetGroupImageInput",
  "type": "object"
}
```

</details>

<a id="add_pmax_audience_signal"></a>

## `add_pmax_audience_signal`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add an audience signal to an existing Performance Max campaign.

Audience signals hint Google AI about who your ideal customers are.
Uses in-market segments (actively researching), affinity segments (long-term interests),
and custom audiences (remarketing lists, customer match).

Use search_audiences tool first to discover relevant audience segment IDs.

**Parameters:**
- campaign_id: The PMax campaign ID
- audience_config: Dict with segment IDs

**Execution time:** 2-5 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding an audience signal to a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Google Ads campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
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
      "description": "Audience configuration with segment IDs. CRITICAL: Only use IDs returned by search_audiences tool. NEVER fabricate or guess IDs -- wrong IDs target unrelated audiences. Canonical keys: 'in_market_audience_ids' (List[int]), 'affinity_audience_ids' (List[int]), 'custom_audience_ids' (List[str] customAudiences resource names), 'user_list_ids' (List[str] userLists resource names from search_audiences custom results), 'audience_name' (str). Example: {'in_market_audience_ids': [80432, 80210], 'user_list_ids': ['customers/123/userLists/456'], 'audience_name': 'SaaS Buyers'}. Input is shape-tolerant (#559): synonyms 'user_interests'/'in_market_audiences', 'remarketing_lists'/'user_lists', and 'name'/'signal_name' are accepted, as are flat (no wrapper) and nested 'segments' shapes — they are normalized for you.",
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
    "campaign_id"
  ],
  "title": "AddPMaxAudienceSignalInput",
  "type": "object"
}
```

</details>

<a id="add_pmax_campaign_logo"></a>

## `add_pmax_campaign_logo`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Link a square LOGO as a campaign-level asset to an existing Performance Max campaign.

Performance Max campaigns with **Brand Guidelines enabled** require at least one
square LOGO and a BUSINESS_NAME linked at the CAMPAIGN level (as CampaignAssets,
NOT asset-group assets). Until both exist, Google rejects any attempt to complete
an asset group with "require at least one square logo to be linked as a
CampaignAsset" / "must link business name and logo assets as CampaignAssets".
This tool satisfies that requirement — the asset-group image tools cannot, because
they link at the asset-group level.

Provide the logo by EITHER:
- `asset_id` — the numeric ID of an EXISTING approved image asset in the account's
  library (preferred; no re-upload), or
- `image_url` — a public http(s) URL or `data:image/...;base64,...` URI to create
  a new square logo image.

Optionally pass `business_name` (max 25 chars) to link the BUSINESS_NAME asset in
the same call. Idempotent: already-linked assets are skipped (pass `force=true` to
add another). A non-square logo produces a warning (Google requires 1:1).

**Parameters:**
- campaign_id: the Performance Max campaign ID
- asset_id OR image_url: the logo source (exactly one)
- business_name: optional, also link the business name
- asset_name / force: optional

**Execution time:** 2-6 seconds (asset resolve/upload + Google Ads mutate)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for linking a LOGO CampaignAsset to an existing PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Performance Max campaign ID (numeric). Example: '24249158821'",
      "title": "Campaign Id",
      "type": "string"
    },
    "asset_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "The numeric ID (or full resource name) of an EXISTING approved IMAGE asset in the account's library to link as the square logo. Preferred when the logo is already uploaded (no re-upload). Get IDs from discover_existing_assets / list_pmax_asset_group_images.",
      "title": "Asset Id"
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
      "description": "Alternative to asset_id: a public http(s) URL OR a 'data:image/...;base64,...' URI to create/upsert a NEW square logo image. Provide EITHER asset_id OR image_url, not both.",
      "title": "Image Url"
    },
    "asset_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display name for a newly created logo asset.",
      "title": "Asset Name"
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
      "description": "Optional: also link a BUSINESS_NAME CampaignAsset (max 25 chars) in the same call. Brand-Guidelines PMax campaigns require BOTH a square logo and a business name at the campaign level.",
      "title": "Business Name"
    },
    "force": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "If true, link even when an identical logo is already linked (default skips duplicates).",
      "title": "Force"
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
  "title": "AddPMaxCampaignLogoInput",
  "type": "object"
}
```

</details>

<a id="add_pmax_search_themes"></a>

## `add_pmax_search_themes`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add search themes to an existing Performance Max campaign.

Search themes hint Google AI about what customers search for. Max 50 per asset group.
NOT keywords — no match types, no bids, no quality scores.

**Best practices:**
- Derive from keyword research results, business profile, or user input
- Keep themes specific but not too narrow (2-5 words ideal)
- Avoid generic themes like "buy stuff" or overly specific ones like "buy red nike air max 97 size 12"

**Parameters:**
- campaign_id: The PMax campaign ID
- search_themes: List of theme strings to add

**Execution time:** 2-5 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for adding search themes to a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Google Ads campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "search_themes": {
      "description": "List of search themes to add. Max 50 total per asset group. NOT keywords — these are hints for Google AI about what customers search. Example: ['AI ad management', 'automate google ads']",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Search Themes",
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
    "campaign_id",
    "search_themes"
  ],
  "title": "AddPMaxSearchThemesInput",
  "type": "object"
}
```

</details>

<a id="add_product_group"></a>

## `add_product_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Subdivide a Shopping ad group's products by a dimension — set a bid for a partition or exclude it.

Splits products by `dimension_type`=`value` (e.g. product_brand=Nike, product_type=Shoes with
level=LEVEL1, product_item_id=SKU123, product_condition=NEW). Creates a biddable partition
(bid_micros) OR an excluded one (exclude=true) — plus the required "everything else" sibling
automatically.

FIRST call on a serve-all ad group subdivides the root. To split an EXISTING partition further,
pass parent_criterion_id (the UNIT to subdivide, from get_product_groups).

**Required:** ad_group_id, dimension_type, value. Optional: level (for type/category), index (for
custom_attribute), bid_micros OR exclude, parent_criterion_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Subdivide a Shopping ad group's products by a dimension (add a biddable or excluded partition).",
  "properties": {
    "ad_group_id": {
      "description": "The Shopping ad group ID.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "dimension_type": {
      "description": "What to split products by: product_brand | product_type | product_item_id | product_category | product_condition | product_channel | product_custom_attribute.",
      "title": "Dimension Type",
      "type": "string"
    },
    "value": {
      "description": "The dimension value for this partition, e.g. 'Nike' (brand), 'Shoes' (type), 'SKU123' (item_id), 'NEW' (condition), 'ONLINE' (channel), a category_id (category).",
      "title": "Value",
      "type": "string"
    },
    "level": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For product_type / product_category only: the level LEVEL1..LEVEL5 (default LEVEL1).",
      "title": "Level"
    },
    "index": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "For product_custom_attribute only: INDEX0..INDEX4.",
      "title": "Index"
    },
    "bid_micros": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Max CPC for this partition in micros (biddable UNIT). Omit if exclude=true.",
      "title": "Bid Micros"
    },
    "exclude": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Exclude this partition from serving (no bid). Mutually exclusive with bid_micros.",
      "title": "Exclude"
    },
    "parent_criterion_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "To split an EXISTING partition further, the UNIT criterion_id to subdivide (from get_product_groups). Omit for the first subdivision of a serve-all ad group.",
      "title": "Parent Criterion Id"
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
    "dimension_type",
    "value"
  ],
  "title": "AddProductGroupInput",
  "type": "object"
}
```

</details>

<a id="add_search_ad_group"></a>

## `add_search_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a new ad group to an EXISTING Search campaign.

**When to use:**
- User wants another themed ad group inside a Search campaign
- User asks to "add an ad group to my Search campaign"

**Each ad group can optionally be seeded with:**
- keywords (plain text — run research_keywords first)
- a Responsive Search Ad (headlines 3-15 @30ch + descriptions 2-4 @90ch + final_url)
- an optional manual CPC bid (inherits campaign bidding otherwise)

**Required:** campaign_id (Search campaign from list_campaigns), ad_group_name.

**Execution time:** 5-15 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Add a new SEARCH_STANDARD ad group to an existing Search campaign.\n\nOptionally seeds the ad group with keywords, a Responsive Search Ad\n(headlines + descriptions), sitelinks, and demographics — all in one call.",
  "properties": {
    "campaign_id": {
      "description": "Existing Search campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "ad_group_name": {
      "description": "Name for the new ad group.",
      "title": "Ad Group Name",
      "type": "string"
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
      "description": "Optional max CPC bid in micros (1_000_000 = 1 unit of account currency). Only used when the campaign bidding strategy allows a manual/ad-group bid.",
      "title": "Cpc Bid Micros"
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
      "description": "Optional ad-group target CPA in micros.",
      "title": "Target Cpa Micros"
    },
    "keywords": {
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
      "description": "Optional keywords to seed the ad group (plain text). Run research_keywords first for ideas.",
      "title": "Keywords"
    },
    "headlines": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "maxItems": 15,
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional RSA headlines to create an ad in this group (each ≤30 chars). Requires descriptions + final_url too. ⚠️ Provide 10+ real headlines: Google pads to 10 and any shortfall is filled with generic 'Default Headline N' placeholders that go LIVE. Aim for 10-15.",
      "title": "Headlines"
    },
    "descriptions": {
      "anyOf": [
        {
          "items": {
            "type": "string"
          },
          "maxItems": 4,
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional RSA descriptions (each ≤90 chars). Requires headlines + final_url too. ⚠️ Provide 4 real descriptions: shortfalls are padded with generic 'Default Description N' placeholders that go LIVE. Aim for 4.",
      "title": "Descriptions"
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
      "description": "Landing page URL for the seeded RSA (required if headlines set).",
      "title": "Final Url"
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
    "ad_group_name"
  ],
  "title": "AddSearchAdGroupInput",
  "type": "object"
}
```

</details>

<a id="add_search_campaign_image"></a>

## `add_search_campaign_image`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Upload + link an image asset at the SEARCH campaign level.

For PMax campaigns use `add_pmax_asset_group_image` instead (PMax links at
asset-group level). This tool is for Search campaigns where image assets
attach at campaign level via CampaignAssetService.

Valid `field_type` values (Search campaigns only):
- AD_IMAGE       — promotional image extension (used by default; always works)
- BUSINESS_LOGO  — brand logo (requires an identity-verified advertiser)

The MARKETING_IMAGE family and LOGO/LANDSCAPE_LOGO are Performance Max / asset-group
image types — Google REJECTS them on a Search campaign. For those, use
`add_pmax_asset_group_image` on a PMax campaign instead.

**Parameters:**
- campaign_id: The Search campaign ID
- image_url: http(s) URL OR `data:image/...;base64,...` URI
- field_type: AD_IMAGE (default) or BUSINESS_LOGO — omit to use AD_IMAGE
- asset_name: optional display name in the Asset Library
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 3-8 seconds (image fetch + Google Ads mutate)

**Example:**
User: "Upload this image (https://...) to campaign 23847465076"
Agent: add_search_campaign_image(campaign_id="23847465076", image_url="https://...")  # defaults to AD_IMAGE

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for uploading + linking an image asset at the SEARCH campaign level.\n\nFor PMax campaigns, use `add_pmax_asset_group_image` (asset-group scoped).\nSearch campaigns attach images at campaign level via CampaignAssetService.\n\nValid `field_type` values (Search campaigns):\n  - AD_IMAGE       — image extension (the default; always works)\n  - BUSINESS_LOGO  — brand logo (requires an identity-verified advertiser)\nThe MARKETING_IMAGE family and LOGO/LANDSCAPE_LOGO are PMax/asset-group types\nand are NOT valid on Search — use add_pmax_asset_group_image for those.",
  "properties": {
    "campaign_id": {
      "description": "The Search campaign ID (numeric). Get from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "image_url": {
      "description": "Image to upload. Either a public http(s) URL OR a base64 data URI (`data:image/png;base64,...`). Plain base64 without the data-URI prefix is NOT accepted.",
      "title": "Image Url",
      "type": "string"
    },
    "field_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Asset slot — one of: AD_IMAGE, BUSINESS_LOGO. Omit to use AD_IMAGE (a promotional image extension; always works). BUSINESS_LOGO = a brand logo (needs an identity-verified advertiser). For PMax MARKETING_IMAGE/LOGO assets use add_pmax_asset_group_image.",
      "title": "Field Type"
    },
    "asset_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional display name for the asset in the Google Ads Asset Library (visible in the UI; doesn't affect rendering).",
      "title": "Asset Name"
    },
    "force": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": false,
      "description": "Optional (default false). Idempotent by default: if this exact image is already linked to the campaign under this field_type it is NOT linked again. Set force=true to add a duplicate link.",
      "title": "Force"
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
    "image_url"
  ],
  "title": "AddSearchCampaignImageInput",
  "type": "object"
}
```

</details>

<a id="add_shopping_ad_group"></a>

## `add_shopping_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add a new ad group to an existing Standard Shopping campaign.

Creates a SHOPPING_PRODUCT_ADS ad group plus its product ad(s). Use this to structure a Shopping
campaign into multiple ad groups (e.g. one per product category) after it's created — each ad group
can then get its own product-partition tree via add_product_group and its own CPC bid.

To edit/pause/remove an ad group afterward, use the channel-neutral tools update_ad_group_settings /
pause_ad_group / resume_ad_group / remove_ad_group (they work on Shopping ad groups).

**Required:** campaign_id (a Shopping campaign). Optional: name, cpc_bid_micros, num_product_ads.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Add a new ad group to an existing Standard Shopping campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Shopping campaign ID to add the ad group to (from list_campaigns).",
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
      "description": "Default max CPC for this ad group in micros (1,000,000 = 1 currency unit).",
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
      "description": "Number of product ads to create in the ad group (default 1).",
      "title": "Num Product Ads"
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
  "title": "AddShoppingAdGroupInput",
  "type": "object"
}
```

</details>

<a id="add_shopping_product_ad"></a>

## `add_shopping_product_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add product ad(s) to an existing Shopping ad group.

A Shopping product ad is a marker that lets the ad group serve products from the linked Merchant
Center feed (it has no creative — the products come from the feed). Most ad groups need only one.
Use this if an ad group has no product ad (so it can't serve) or you want extras.

To LIST an ad group's ads use get_campaign_structure; to REMOVE one use remove_ad.

**Required:** ad_group_id (a Shopping ad group). Optional: count (default 1).

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Add product ad(s) to an existing Shopping ad group.",
  "properties": {
    "ad_group_id": {
      "description": "The Shopping ad group ID (from get_campaign_structure).",
      "title": "Ad Group Id",
      "type": "string"
    },
    "count": {
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
      "description": "How many product ads to add (default 1). Product ads are markers — products come from the feed.",
      "title": "Count"
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
  "title": "AddShoppingProductAdInput",
  "type": "object"
}
```

</details>

