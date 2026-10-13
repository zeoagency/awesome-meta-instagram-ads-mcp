# brandu-mos/konquest-meta-ads-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/brandu-mos/konquest-meta-ads-mcp) · [Machine-readable snapshot](../../catalog/brandu-mos--konquest-meta-ads-mcp.json)

Complete registered tool snapshot. **57 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`762c224b060b`](https://github.com/brandu-mos/konquest-meta-ads-mcp/tree/762c224b060b233b66fb9af8a2f3865303ed757b). Method: `runtime-tools-list`.

- Complete public open-core inventory. Private premium modules are absent and excluded.

## Tools

- [bulk_rename_objects](#bulk_rename_objects)
- [check_token_status](#check_token_status)
- [create_ad_creative](#create_ad_creative)
- [create_ad_from_manifest](#create_ad_from_manifest)
- [create_adset](#create_adset)
- [create_campaign](#create_campaign)
- [create_multi_asset_ad](#create_multi_asset_ad)
- [create_product_set](#create_product_set)
- [delete_campaign_structure](#delete_campaign_structure)
- [diagnose_pixel_on_site](#diagnose_pixel_on_site)
- [discover_all_accounts](#discover_all_accounts)
- [duplicate_adset](#duplicate_adset)
- [duplicate_campaign](#duplicate_campaign)
- [estimate_audience_size](#estimate_audience_size)
- [generate_names](#generate_names)
- [get_account_info](#get_account_info)
- [get_account_pages](#get_account_pages)
- [get_ad_accounts](#get_ad_accounts)
- [get_ad_creatives](#get_ad_creatives)
- [get_ad_details](#get_ad_details)
- [get_ad_image](#get_ad_image)
- [get_ads](#get_ads)
- [get_adset_details](#get_adset_details)
- [get_adsets](#get_adsets)
- [get_bulk_insights](#get_bulk_insights)
- [get_campaign_details](#get_campaign_details)
- [get_campaigns](#get_campaigns)
- [get_catalog_info](#get_catalog_info)
- [get_catalog_products](#get_catalog_products)
- [get_creative_details](#get_creative_details)
- [get_event_stats](#get_event_stats)
- [get_insights](#get_insights)
- [get_instagram_identities](#get_instagram_identities)
- [get_interest_suggestions](#get_interest_suggestions)
- [get_pixel_events](#get_pixel_events)
- [get_pixel_info](#get_pixel_info)
- [get_product_sets](#get_product_sets)
- [list_custom_audiences](#list_custom_audiences)
- [poll_video_processing](#poll_video_processing)
- [read_client_vault](#read_client_vault)
- [resolve_page_identity](#resolve_page_identity)
- [run_setup_check](#run_setup_check)
- [run_tracking_diagnostic](#run_tracking_diagnostic)
- [search_behaviors](#search_behaviors)
- [search_demographics](#search_demographics)
- [search_geo_locations](#search_geo_locations)
- [search_interests](#search_interests)
- [send_test_event](#send_test_event)
- [update_ad](#update_ad)
- [update_ad_creative](#update_ad_creative)
- [update_adset](#update_adset)
- [update_campaign](#update_campaign)
- [update_product_set](#update_product_set)
- [upload_ad_image](#upload_ad_image)
- [upload_video_asset](#upload_video_asset)
- [upload_video_resumable](#upload_video_resumable)
- [validate_catalog_connections](#validate_catalog_connections)

<a id="bulk_rename_objects"></a>

## `bulk_rename_objects`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ops.py#L129)


Rename multiple Meta Ads objects in one call.

Args:
    renames_json: JSON array of rename specs:
        [{object_id: '...', new_name: '...', object_type: 'campaign|adset|ad'}, ...]


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "renames_json": {
      "title": "Renames Json",
      "type": "string"
    }
  },
  "required": [
    "renames_json"
  ],
  "title": "bulk_rename_objectsArguments",
  "type": "object"
}
```

</details>

<a id="check_token_status"></a>

## `check_token_status`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/accounts.py#L22)


Check Meta API token health, permissions, and rate limit status.

Returns token validity, granted permissions, missing permissions,
and current rate limit usage percentage.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {},
  "title": "check_token_statusArguments",
  "type": "object"
}
```

</details>

<a id="create_ad_creative"></a>

## `create_ad_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/creatives.py#L381)


Create a standalone single-image ad creative.

Returns creative_id for use in ad creation (create_ad_from_manifest)
or ad update (update_ad creative swap).

Requires a Facebook Page ID. Instagram identity is auto-resolved
from the page - if unavailable, creative is created for Facebook only.

Single-image creatives only in v1. For video, carousel, or dynamic
creatives, use create_multi_asset_ad.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    page_id: Facebook Page ID for the creative.
    image_hash: Image hash from upload_ad_image.
    link_url: CTA destination URL.
    primary_text: Main ad copy text (the "message").
    headline: Optional headline (appears below image).
    description: Optional description text.
    cta_type: Call-to-action type. Default 'LEARN_MORE'.
        Valid: LEARN_MORE, SHOP_NOW, SIGN_UP, SUBSCRIBE, CONTACT_US,
        GET_OFFER, BOOK_TRAVEL, DOWNLOAD, APPLY_NOW, WATCH_MORE,
        GET_QUOTE, SEND_MESSAGE, ORDER_NOW, NO_BUTTON.
    name: Optional creative name. Subject to naming enforcement.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "image_hash": {
      "title": "Image Hash",
      "type": "string"
    },
    "link_url": {
      "title": "Link Url",
      "type": "string"
    },
    "primary_text": {
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
      "title": "Description"
    },
    "cta_type": {
      "default": "LEARN_MORE",
      "title": "Cta Type",
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
      "title": "Name"
    }
  },
  "required": [
    "account_id",
    "page_id",
    "image_hash",
    "link_url",
    "primary_text"
  ],
  "title": "create_ad_creativeArguments",
  "type": "object"
}
```

</details>

<a id="create_ad_from_manifest"></a>

## `create_ad_from_manifest`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ads.py#L333)


Create an ad from a manifest entry (always PAUSED, manifest-driven, no exceptions).

Loads the manifest entry, detects creative mode, resolves identity,
checks for duplicates, validates pre-write, creates the ad,
and verifies post-write.

INSTAGRAM GATE: Enforced via placement_mode parameter.
- full_meta (default): requires IG identity, BLOCKS if unavailable
- facebook_only: explicit FB-only, no IG placements
- instagram_only: requires IG identity, BLOCKS if unavailable

For video ads: provide meta_video_id from upload_video_asset + poll_video_processing.
The video must be in 'ready' state before calling this tool.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    adset_id: Target ad set ID.
    logical_creative_id: ID of the creative entry in the manifest (e.g., 'lc_example_brand_001').
    manifest_json: JSON string containing the manifest or a single creative entry.
        Must include the logical_creative_id entry with variants, CTA, etc.
    ad_name: Name for the ad. Greek text validated.
    page_id: Facebook Page ID for the ad identity.
    destination_url: Primary destination URL for the ad CTA.
    primary_text: Primary text / message body. Required for manual mode, optional for auto/hybrid.
    cta_type: Call to action type (default 'SHOP_NOW'). See VALID_CTA_TYPES.
    headline: Optional headline text. Auto-generated if copy_mode='auto' and not provided.
    description: Optional description text. Auto-generated if copy_mode='auto' and not provided.
    instagram_user_id: Optional IG user ID. If not provided, attempts resolution from account.
    destination_url_override: If set, overrides manifest URL. Logged explicitly.
    cta_override: If set, overrides manifest CTA. Logged explicitly.
    primary_text_override: If set, overrides manifest primary text. Logged explicitly.
    headline_override: If set, overrides manifest headline. Logged explicitly.
    copy_mode: 'manual' (default), 'auto' (generate from vault), 'hybrid' (fill gaps).
    angle_name: Marketing angle for auto/hybrid copy generation.
    icp_name: Target ICP for auto/hybrid copy generation.
    funnel_stage: 'tofu', 'mofu', 'bofu' for copy tone/structure.
    dry_run: If true, runs all validation but does not create the ad. Returns what would be created.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "logical_creative_id": {
      "title": "Logical Creative Id",
      "type": "string"
    },
    "manifest_json": {
      "title": "Manifest Json",
      "type": "string"
    },
    "ad_name": {
      "title": "Ad Name",
      "type": "string"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "destination_url": {
      "title": "Destination Url",
      "type": "string"
    },
    "primary_text": {
      "default": "",
      "title": "Primary Text",
      "type": "string"
    },
    "cta_type": {
      "default": "SHOP_NOW",
      "title": "Cta Type",
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
      "title": "Description"
    },
    "instagram_user_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram User Id"
    },
    "meta_video_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Meta Video Id"
    },
    "destination_url_override": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Destination Url Override"
    },
    "cta_override": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Cta Override"
    },
    "primary_text_override": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Primary Text Override"
    },
    "headline_override": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Headline Override"
    },
    "copy_mode": {
      "default": "manual",
      "title": "Copy Mode",
      "type": "string"
    },
    "angle_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Angle Name"
    },
    "icp_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Icp Name"
    },
    "funnel_stage": {
      "default": "tofu",
      "title": "Funnel Stage",
      "type": "string"
    },
    "dry_run": {
      "default": false,
      "title": "Dry Run",
      "type": "boolean"
    },
    "placement_mode": {
      "default": "full_meta",
      "title": "Placement Mode",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "adset_id",
    "logical_creative_id",
    "manifest_json",
    "ad_name",
    "page_id",
    "destination_url"
  ],
  "title": "create_ad_from_manifestArguments",
  "type": "object"
}
```

</details>

<a id="create_adset"></a>

## `create_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/adsets.py#L226)


Create a new ad set (always PAUSED, no exceptions).

Runs Advantage+ audience enforcement, parent campaign inspection, ABO/CBO
enforcement, ICP signal mapping, narrowing detection, pre-write validation,
creates the ad set, and verifies post-write.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    campaign_id: Parent campaign ID. Must be PAUSED or ACTIVE.
    name: Ad set name. Greek text validated.
    optimization_goal: e.g. 'OFFSITE_CONVERSIONS', 'LINK_CLICKS', 'LEAD_GENERATION', 'REACH'.
        Must be compatible with parent campaign objective.
    billing_event: Usually 'IMPRESSIONS'. Also: 'LINK_CLICKS', 'THRUPLAY'.
    daily_budget: Daily budget in EUR (e.g., 15.00). Required for ABO campaigns. Omit for CBO.
    lifetime_budget: Lifetime budget in EUR. Alternative to daily_budget. Requires end_time.
    targeting_json: JSON string of targeting spec. Advantage+ mode uses signals as suggestions.
        Example: '{"geo_locations":{"countries":["GR"]},"age_min":25,"age_max":55}'
    promoted_object_json: JSON string of promoted object. Required for OUTCOME_SALES/LEADS.
        Example: '{"pixel_id":"123456789012345","custom_event_type":"PURCHASE"}'
    start_time: ISO 8601 start time. Optional (defaults to immediately when activated).
    end_time: ISO 8601 end time. Required if using lifetime_budget.
    audience_mode: 'advantage_plus' (default, recommended), 'manual', 'broad',
        'existing_audience', 'restricted' (disables Advantage+).
    icp_name: ICP name from concept selection for signal derivation.
    icp_signals_json: Pre-built ICP signals JSON with interests/behaviors/demographics.
    experiment_type: If 'strict_audience_test', allows Advantage+ OFF.
    explicit_tracking_mode: Operator-declared tracking mode override.
        'instant_form', 'messaging', 'page_engagement' allow writes without pixel.
        If not set, system infers intended flow and enforces pixel for website paths.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "type": "string"
    },
    "optimization_goal": {
      "title": "Optimization Goal",
      "type": "string"
    },
    "billing_event": {
      "default": "IMPRESSIONS",
      "title": "Billing Event",
      "type": "string"
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
      "title": "Lifetime Budget"
    },
    "targeting_json": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Targeting Json"
    },
    "promoted_object_json": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Promoted Object Json"
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
      "title": "End Time"
    },
    "audience_mode": {
      "default": "advantage_plus",
      "title": "Audience Mode",
      "type": "string"
    },
    "icp_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Icp Name"
    },
    "icp_signals_json": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Icp Signals Json"
    },
    "experiment_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Experiment Type"
    },
    "explicit_tracking_mode": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Explicit Tracking Mode"
    },
    "naming_audience_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Naming Audience Type"
    },
    "naming_age_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Naming Age Range"
    },
    "naming_geo": {
      "default": "GR",
      "title": "Naming Geo",
      "type": "string"
    },
    "naming_exclusion_flag": {
      "default": "None",
      "title": "Naming Exclusion Flag",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "campaign_id",
    "name",
    "optimization_goal"
  ],
  "title": "create_adsetArguments",
  "type": "object"
}
```

</details>

<a id="create_campaign"></a>

## `create_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/campaigns.py#L191)


Create a new campaign (always PAUSED, no exceptions).

Runs naming enforcement, pre-write validation, creates the campaign,
verifies post-write, and logs the mutation.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    name: Campaign name following convention: Objective | Product | Funnel | BudgetModel.
        If not following convention, provide product/funnel/budget_model for auto-correction.
    objective: Must be an outcome-based objective:
        OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS,
        OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION.
    special_ad_categories: Comma-separated special categories if applicable.
    product: Product/offer name for naming convention (e.g., 'Consulting', 'VitC').
    funnel: Funnel stage for naming: TOFU, MOFU, BOFU, RT.
    budget_model: ABO or CBO for naming convention.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "type": "string"
    },
    "objective": {
      "title": "Objective",
      "type": "string"
    },
    "special_ad_categories": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Special Ad Categories"
    },
    "product": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Product"
    },
    "funnel": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Funnel"
    },
    "budget_model": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Budget Model"
    }
  },
  "required": [
    "account_id",
    "name",
    "objective"
  ],
  "title": "create_campaignArguments",
  "type": "object"
}
```

</details>

<a id="create_multi_asset_ad"></a>

## `create_multi_asset_ad`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ad_builder.py#L154)


Create an ad with enforced identity, multi-asset support, and verification.

Supports two asset modes (not mixed):
- VIDEO: If 9:16 and/or 1:1 videos provided, creates ONE ad with
  asset_feed_spec and placement mapping. Single video = simple mode.
- STATIC IMAGE: If 2+ of image_1x1_hash/image_4x5_hash/image_9x16_hash
  provided, creates ONE ad with asset_feed_spec and placement mapping.
  Single image hash not accepted here - use create_ad_creative instead.

Mixed video + image is blocked. Provide one type only.

INSTAGRAM GATE: Enforced via placement_mode.
- full_meta (default): requires IG identity, BLOCKS if unavailable
- facebook_only: explicit FB-only, no IG placements
- instagram_only: requires IG identity, BLOCKS if unavailable

Args:
    account_id: Ad account ID.
    adset_id: Target ad set ID.
    page_id: Facebook Page ID.
    ad_name: Ad name.
    primary_text: Main ad copy. Required for manual, auto-generated for auto/hybrid.
    headline: Headline text. Auto-generated for auto/hybrid if empty.
    destination_url: CTA destination URL.
    cta_type: CTA type (default LEARN_MORE).
    video_9x16_id: Vertical video ID (for Stories/Reels).
    video_1x1_id: Square video ID (for Feed).
    description: Optional description.
    copy_mode: 'manual' (default), 'auto' (generate from vault), 'hybrid'.
    angle_name: Marketing angle for auto/hybrid copy generation.
    icp_name: Target ICP for auto/hybrid copy generation.
    funnel_stage: 'tofu', 'mofu', 'bofu' for copy structure.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "ad_name": {
      "title": "Ad Name",
      "type": "string"
    },
    "primary_text": {
      "default": "",
      "title": "Primary Text",
      "type": "string"
    },
    "headline": {
      "default": "",
      "title": "Headline",
      "type": "string"
    },
    "destination_url": {
      "default": "",
      "title": "Destination Url",
      "type": "string"
    },
    "cta_type": {
      "default": "LEARN_MORE",
      "title": "Cta Type",
      "type": "string"
    },
    "video_9x16_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Video 9X16 Id"
    },
    "video_1x1_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Video 1X1 Id"
    },
    "image_1x1_hash": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Image 1X1 Hash"
    },
    "image_4x5_hash": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Image 4X5 Hash"
    },
    "image_9x16_hash": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Image 9X16 Hash"
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
      "title": "Description"
    },
    "copy_mode": {
      "default": "manual",
      "title": "Copy Mode",
      "type": "string"
    },
    "angle_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Angle Name"
    },
    "icp_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Icp Name"
    },
    "funnel_stage": {
      "default": "tofu",
      "title": "Funnel Stage",
      "type": "string"
    },
    "placement_mode": {
      "default": "full_meta",
      "title": "Placement Mode",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "adset_id",
    "page_id",
    "ad_name"
  ],
  "title": "create_multi_asset_adArguments",
  "type": "object"
}
```

</details>

<a id="create_product_set"></a>

## `create_product_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/catalogs.py#L468)


Create a product set with filter rules for DPA targeting.

Args:
    catalog_id: Product catalog ID.
    name: Product set name.
    filter_json: JSON string of filter rules.
        Example: '{"product_type":{"i_contains":"shoes"}}'


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "catalog_id": {
      "title": "Catalog Id",
      "type": "string"
    },
    "name": {
      "title": "Name",
      "type": "string"
    },
    "filter_json": {
      "title": "Filter Json",
      "type": "string"
    }
  },
  "required": [
    "catalog_id",
    "name",
    "filter_json"
  ],
  "title": "create_product_setArguments",
  "type": "object"
}
```

</details>

<a id="delete_campaign_structure"></a>

## `delete_campaign_structure`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ops.py#L169)


Delete entire campaign structure (ads -> adsets -> campaigns) in correct order.

Args:
    account_id: Ad account ID.
    campaign_ids_json: JSON array of campaign IDs to delete. If not provided with
        delete_all_active=True, deletes all non-deleted campaigns.
    delete_all_active: If True and no campaign_ids, targets all campaigns.
    confirm: Must be True to actually delete. False = dry run showing what would be deleted.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "campaign_ids_json": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Campaign Ids Json"
    },
    "delete_all_active": {
      "default": false,
      "title": "Delete All Active",
      "type": "boolean"
    },
    "confirm": {
      "default": false,
      "title": "Confirm",
      "type": "boolean"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "delete_campaign_structureArguments",
  "type": "object"
}
```

</details>

<a id="diagnose_pixel_on_site"></a>

## `diagnose_pixel_on_site`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ops.py#L270)


Diagnose pixel installation on a website via headless browser check.

Checks: pixel script presence, consent/cookie blocking, Lead event setup,
Complianz/cookie banner status.

Requires browser MCP (Puppeteer) to be available.

Args:
    url: Website URL to check.
    pixel_id: Optional specific pixel ID to look for.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "url": {
      "title": "Url",
      "type": "string"
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
      "title": "Pixel Id"
    }
  },
  "required": [
    "url"
  ],
  "title": "diagnose_pixel_on_siteArguments",
  "type": "object"
}
```

</details>

<a id="discover_all_accounts"></a>

## `discover_all_accounts`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/accounts.py#L227)


Discover all ad accounts, their pages, pixels, and Instagram accounts.

Used to generate or update the account registry (config/accounts.yaml).
Returns a comprehensive mapping of all accessible assets.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {},
  "title": "discover_all_accountsArguments",
  "type": "object"
}
```

</details>

<a id="duplicate_adset"></a>

## `duplicate_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/duplication.py#L506)


Duplicate a single ad set into a target campaign within the same account.

All created objects are PAUSED. Does not duplicate child ads.
Same-account only.

Args:
    adset_id: Source ad set ID to duplicate.
    target_campaign_id: Campaign to place the duplicated ad set in.
    account_id: Ad account ID (must match source).
    name_suffix: Appended to source name (default " - Copy").
    budget_override: Override budget in EUR. If None, copies source budget.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "target_campaign_id": {
      "title": "Target Campaign Id",
      "type": "string"
    },
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "name_suffix": {
      "default": " - Copy",
      "title": "Name Suffix",
      "type": "string"
    },
    "budget_override": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Budget Override"
    }
  },
  "required": [
    "adset_id",
    "target_campaign_id",
    "account_id"
  ],
  "title": "duplicate_adsetArguments",
  "type": "object"
}
```

</details>

<a id="duplicate_campaign"></a>

## `duplicate_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/duplication.py#L39)


Duplicate a campaign (and optionally its child ad sets and ads) within the same account.

All created objects are PAUSED. When include_ads=True, ads are duplicated
with their existing creative references (creatives are reused, not copied).

Same-account only. Cross-account duplication is not supported.

Args:
    campaign_id: Source campaign ID to duplicate.
    account_id: Ad account ID. Must match the source campaign's account.
    name_suffix: Appended to source names (default " - Copy").
        Must result in valid names per naming convention.
    include_adsets: Whether to duplicate child ad sets (default True).
    adset_budget_override: Override all duplicated ad set budgets (EUR).
        Only applies to ABO campaigns. If None, copies source budgets.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "name_suffix": {
      "default": " - Copy",
      "title": "Name Suffix",
      "type": "string"
    },
    "include_adsets": {
      "default": true,
      "title": "Include Adsets",
      "type": "boolean"
    },
    "include_ads": {
      "default": false,
      "title": "Include Ads",
      "type": "boolean"
    },
    "adset_budget_override": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Adset Budget Override"
    }
  },
  "required": [
    "campaign_id",
    "account_id"
  ],
  "title": "duplicate_campaignArguments",
  "type": "object"
}
```

</details>

<a id="estimate_audience_size"></a>

## `estimate_audience_size`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/targeting.py#L336)


Estimate audience reach for a targeting specification.

Returns estimated daily reach (lower/upper bounds) for the given
targeting spec on the specified account.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    targeting_json: JSON string of targeting spec.
        Example: '{"geo_locations":{"countries":["GR"]},"age_min":25,"age_max":55}'


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "targeting_json": {
      "title": "Targeting Json",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "targeting_json"
  ],
  "title": "estimate_audience_sizeArguments",
  "type": "object"
}
```

</details>

<a id="generate_names"></a>

## `generate_names`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/naming.py#L146)


Generate correctly named Meta Ads object following naming convention.

Convention (learned from ExampleBrand):
- Campaign: Objective | Product | Funnel | BudgetModel
- Ad Set: AudienceType | AgeRange | Geo | ExclusionFlag
- Ad: Hook | Format | Version

Args:
    object_type: 'campaign', 'adset', or 'ad'.
    objective: For campaigns: Sales, Traffic, Leads, Awareness, Engagement.
    product: For campaigns: product/offer name (client-specific).
    funnel: For campaigns: TOFU, MOFU, BOFU, RT.
    budget_model: For campaigns: ABO, CBO.
    audience_type: For ad sets: Broad, Broad-Interest, RT-WV-30d, etc.
    age_range: For ad sets: 24-55, 18-45, All.
    geo: Country code (default GR).
    exclusion_flag: For ad sets: Adv, ExPurch, None.
    hook: For ads: concept name in kebab-case (e.g., Employee-Blame).
    format_code: For ads: REEL, VID, IMG, REEL+FEED.
    version: For ads: V1, V2, V3.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "object_type": {
      "title": "Object Type",
      "type": "string"
    },
    "objective": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Objective"
    },
    "product": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Product"
    },
    "funnel": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Funnel"
    },
    "budget_model": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Budget Model"
    },
    "audience_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Audience Type"
    },
    "age_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Age Range"
    },
    "geo": {
      "default": "GR",
      "title": "Geo",
      "type": "string"
    },
    "exclusion_flag": {
      "default": "None",
      "title": "Exclusion Flag",
      "type": "string"
    },
    "hook": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Hook"
    },
    "format_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Format Code"
    },
    "version": {
      "default": "V1",
      "title": "Version",
      "type": "string"
    }
  },
  "required": [
    "object_type"
  ],
  "title": "generate_namesArguments",
  "type": "object"
}
```

</details>

<a id="get_account_info"></a>

## `get_account_info`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/accounts.py#L100)


Get detailed information about a specific ad account.

Returns account configuration, status, spend data, pixel info,
and connected assets.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_account_infoArguments",
  "type": "object"
}
```

</details>

<a id="get_account_pages"></a>

## `get_account_pages`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/accounts.py#L155)


List Facebook Pages available for ads on a specific ad account.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_account_pagesArguments",
  "type": "object"
}
```

</details>

<a id="get_ad_accounts"></a>

## `get_ad_accounts`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/accounts.py#L33)


List all ad accounts accessible to the authenticated user.

Returns account IDs, names, statuses, currencies, and timezones
for all accounts in your business portfolio.

Args:
    limit: Maximum number of accounts to return (default 50).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "get_ad_accountsArguments",
  "type": "object"
}
```

</details>

<a id="get_ad_creatives"></a>

## `get_ad_creatives`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/creatives.py#L210)


List ad creatives for an account or specific ad, with image hash resolution.

Args:
    account_id: Ad account ID (e.g., 'act_123456789'). Used for image hash resolution.
    ad_id: Optional ad ID. If provided, returns the creative for that specific ad.
    limit: Max results when listing account creatives (default 50).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
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
      "title": "Ad Id"
    },
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_ad_creativesArguments",
  "type": "object"
}
```

</details>

<a id="get_ad_details"></a>

## `get_ad_details`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ads.py#L294)


Get detailed ad information including creative reference,
tracking specs, conversion specs, issues, and recommendations.

Args:
    ad_id: Ad ID (numeric string).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "get_ad_detailsArguments",
  "type": "object"
}
```

</details>

<a id="get_ad_image"></a>

## `get_ad_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/images.py#L177)


Retrieve metadata and URL for an uploaded ad image by hash.

Returns the image URL, dimensions, name, and other metadata.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    image_hash: Image hash from upload_ad_image.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "image_hash": {
      "title": "Image Hash",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "image_hash"
  ],
  "title": "get_ad_imageArguments",
  "type": "object"
}
```

</details>

<a id="get_ads"></a>

## `get_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ads.py#L226)


List ads for an account, campaign, or ad set.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    campaign_id: Optional - filter ads by campaign.
    adset_id: Optional - filter ads by ad set (takes precedence over campaign_id).
    status_filter: Filter by effective_status: 'ACTIVE', 'PAUSED', 'ARCHIVED', or 'ALL'.
    limit: Maximum results per page (default 50).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
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
      "title": "Campaign Id"
    },
    "adset_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Adset Id"
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
      "default": null,
      "title": "Status Filter"
    },
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_adsArguments",
  "type": "object"
}
```

</details>

<a id="get_adset_details"></a>

## `get_adset_details`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/adsets.py#L156)


Get detailed ad set information including targeting, optimization,
learning stage, frequency caps, and attribution settings.

Args:
    adset_id: Ad set ID (numeric string).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    }
  },
  "required": [
    "adset_id"
  ],
  "title": "get_adset_detailsArguments",
  "type": "object"
}
```

</details>

<a id="get_adsets"></a>

## `get_adsets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/adsets.py#L70)


List ad sets for an account or filtered by campaign.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    campaign_id: Optional campaign ID to filter ad sets for that campaign only.
    status_filter: Filter by effective_status: 'ACTIVE', 'PAUSED', 'ARCHIVED', or 'ALL'.
    limit: Maximum results per page (default 50).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
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
      "default": null,
      "title": "Status Filter"
    },
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_adsetsArguments",
  "type": "object"
}
```

</details>

<a id="get_bulk_insights"></a>

## `get_bulk_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/insights.py#L472)


Get performance insights across all accessible ad accounts in one call.

Aggregates spend, impressions, clicks, conversions, ROAS across accounts.
Uses accounts from the Meta API (not accounts.yaml).

Args:
    time_range: 'today', 'yesterday', 'last_3d', 'last_7d', 'last_14d', 'last_30d'.
    level: 'account' (one row per account). Campaign-level bulk is not supported.
    limit_accounts: Max accounts to query (default 20).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "time_range": {
      "default": "last_7d",
      "title": "Time Range",
      "type": "string"
    },
    "level": {
      "default": "account",
      "title": "Level",
      "type": "string"
    },
    "limit_accounts": {
      "default": 20,
      "title": "Limit Accounts",
      "type": "integer"
    }
  },
  "title": "get_bulk_insightsArguments",
  "type": "object"
}
```

</details>

<a id="get_campaign_details"></a>

## `get_campaign_details`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/campaigns.py#L145)


Get detailed information about a specific campaign including
budget, objective, bid strategy, special categories, and issues.

Args:
    campaign_id: Campaign ID (numeric string).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "get_campaign_detailsArguments",
  "type": "object"
}
```

</details>

<a id="get_campaigns"></a>

## `get_campaigns`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/campaigns.py#L57)


List campaigns for an ad account with status and budget info.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    status_filter: Filter by effective_status: 'ACTIVE', 'PAUSED', 'ARCHIVED', or 'ALL'.
        If not set, returns all campaigns.
    limit: Maximum results per page (default 50, max 100).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
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
      "default": null,
      "title": "Status Filter"
    },
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_campaignsArguments",
  "type": "object"
}
```

</details>

<a id="get_catalog_info"></a>

## `get_catalog_info`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/catalogs.py#L28)


Get catalog details including product count, vertical, name,
and connected event sources (pixels).

Args:
    catalog_id: Product catalog ID (numeric string).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "catalog_id": {
      "title": "Catalog Id",
      "type": "string"
    }
  },
  "required": [
    "catalog_id"
  ],
  "title": "get_catalog_infoArguments",
  "type": "object"
}
```

</details>

<a id="get_catalog_products"></a>

## `get_catalog_products`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/catalogs.py#L85)


List products in a catalog with price, availability, review status, and URLs.

Args:
    catalog_id: Product catalog ID.
    limit: Max products to return (default 25, max 100).
    filter_availability: Optional filter: 'in stock', 'out of stock', 'discontinued'.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "catalog_id": {
      "title": "Catalog Id",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    },
    "filter_availability": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Filter Availability"
    }
  },
  "required": [
    "catalog_id"
  ],
  "title": "get_catalog_productsArguments",
  "type": "object"
}
```

</details>

<a id="get_creative_details"></a>

## `get_creative_details`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/creatives.py#L294)


Get full creative details including mode classification, media URLs,
object_story_spec, asset_feed_spec, and degrees_of_freedom_spec.

Args:
    creative_id: Creative ID (numeric string).
    account_id: Optional account ID for image hash resolution. If not provided,
        image hashes will not be resolved to URLs.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "creative_id": {
      "title": "Creative Id",
      "type": "string"
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
    }
  },
  "required": [
    "creative_id"
  ],
  "title": "get_creative_detailsArguments",
  "type": "object"
}
```

</details>

<a id="get_event_stats"></a>

## `get_event_stats`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/pixels.py#L260)


Get event statistics with archetype-aware diagnostic analysis.

Checks event coverage, parameter completeness, diagnostic flags,
and classifies overall tracking health.

Args:
    pixel_id: Pixel ID (numeric string).
    archetype: Account archetype for requirement matching:
        'ecommerce', 'lead_gen', 'awareness', 'traffic', 'hybrid', 'messages'.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "pixel_id": {
      "title": "Pixel Id",
      "type": "string"
    },
    "archetype": {
      "default": "hybrid",
      "title": "Archetype",
      "type": "string"
    }
  },
  "required": [
    "pixel_id"
  ],
  "title": "get_event_statsArguments",
  "type": "object"
}
```

</details>

<a id="get_insights"></a>

## `get_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/insights.py#L326)


Get performance insights for any Meta Ads object (account, campaign, ad set, or ad).

Returns normalized metrics with objective-aware extraction: purchases/ROAS for ecommerce,
leads/CPL for lead_gen, reach/frequency for awareness.

Args:
    object_id: Account ID (act_XXX), campaign ID, ad set ID, or ad ID.
    time_range: Date preset ('last_7d', 'last_30d', 'this_month', etc.)
        or explicit range 'YYYY-MM-DD,YYYY-MM-DD'.
    breakdowns: Comma-separated breakdown dimensions (e.g. 'age,gender').
        Supported: age, gender, country, region, impression_device,
        platform_position, publisher_platform, device_platform, product_id.
    level: Aggregation level when querying account/campaign: 'campaign', 'adset', 'ad'.
        Omit for object-level insights.
    archetype: Account archetype for metric selection: 'ecommerce', 'lead_gen',
        'awareness', 'traffic', 'hybrid', 'messages'. Default 'hybrid' (all metrics).
    compact: If true, return a compact operator-friendly summary alongside raw data.
    limit: Max rows for breakdown or level queries (default 50).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "object_id": {
      "title": "Object Id",
      "type": "string"
    },
    "time_range": {
      "default": "last_7d",
      "title": "Time Range",
      "type": "string"
    },
    "breakdowns": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Breakdowns"
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
      "title": "Level"
    },
    "archetype": {
      "default": "hybrid",
      "title": "Archetype",
      "type": "string"
    },
    "compact": {
      "default": true,
      "title": "Compact",
      "type": "boolean"
    },
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "object_id"
  ],
  "title": "get_insightsArguments",
  "type": "object"
}
```

</details>

<a id="get_instagram_identities"></a>

## `get_instagram_identities`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/accounts.py#L186)


List Instagram accounts available for ads on a specific ad account.

Returns instagram_user_id (the canonical identifier) for each account.
This is the first step in the Instagram identity resolution ladder.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_instagram_identitiesArguments",
  "type": "object"
}
```

</details>

<a id="get_interest_suggestions"></a>

## `get_interest_suggestions`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/targeting.py#L222)


Get related interest suggestions from seed interests.

Accepts a comma-separated list of interest IDs or names and returns
Meta's suggested related interests for targeting expansion.

Args:
    interest_list: Comma-separated interest IDs (numeric) or interest names.
        Example IDs: '6003139266461,6003017845981'
        Example names: 'yoga,meditation'
    limit: Max suggestions to return (default 20).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "interest_list": {
      "title": "Interest List",
      "type": "string"
    },
    "limit": {
      "default": 20,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "interest_list"
  ],
  "title": "get_interest_suggestionsArguments",
  "type": "object"
}
```

</details>

<a id="get_pixel_events"></a>

## `get_pixel_events`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/pixels.py#L212)


Get events received by a pixel in the last 24 hours,
broken down by event type and hourly counts.

Args:
    pixel_id: Pixel ID (numeric string).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "pixel_id": {
      "title": "Pixel Id",
      "type": "string"
    }
  },
  "required": [
    "pixel_id"
  ],
  "title": "get_pixel_eventsArguments",
  "type": "object"
}
```

</details>

<a id="get_pixel_info"></a>

## `get_pixel_info`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/pixels.py#L186)


Get pixel status, connections, last fired time, and availability.

Args:
    pixel_id: Pixel ID (numeric string).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "pixel_id": {
      "title": "Pixel Id",
      "type": "string"
    }
  },
  "required": [
    "pixel_id"
  ],
  "title": "get_pixel_infoArguments",
  "type": "object"
}
```

</details>

<a id="get_product_sets"></a>

## `get_product_sets`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/catalogs.py#L169)


List product sets in a catalog with product counts and filter rules.

Args:
    catalog_id: Product catalog ID.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "catalog_id": {
      "title": "Catalog Id",
      "type": "string"
    }
  },
  "required": [
    "catalog_id"
  ],
  "title": "get_product_setsArguments",
  "type": "object"
}
```

</details>

<a id="list_custom_audiences"></a>

## `list_custom_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/audiences.py#L152)


List custom audiences for an ad account with type classification,
size estimates, delivery status, and diagnostic warnings.

Flags audiences that are unusable, too small, too broad, stale, or errored.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    limit: Max audiences to return (default 50).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "limit": {
      "default": 50,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "list_custom_audiencesArguments",
  "type": "object"
}
```

</details>

<a id="poll_video_processing"></a>

## `poll_video_processing`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/video.py#L227)


Poll video processing status until ready, failed, or max attempts reached.

Args:
    video_id: Meta video ID from upload_video_asset.
    max_attempts: Maximum poll attempts (default 30 = 5 minutes at 10s interval).
    poll_interval_seconds: Seconds between polls (default 10).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "video_id": {
      "title": "Video Id",
      "type": "string"
    },
    "max_attempts": {
      "default": 30,
      "title": "Max Attempts",
      "type": "integer"
    },
    "poll_interval_seconds": {
      "default": 10,
      "title": "Poll Interval Seconds",
      "type": "integer"
    }
  },
  "required": [
    "video_id"
  ],
  "title": "poll_video_processingArguments",
  "type": "object"
}
```

</details>

<a id="read_client_vault"></a>

## `read_client_vault`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/vault_reader.py#L128)


Read all client intelligence from the Obsidian vault for ad operations.

Auto-resolves: brand voice, ICPs, angles, objections, profile IDs.
If critical files are missing, returns explicit blockers.

Args:
    account_id: Ad account ID. Resolved to client slug via registry.
    include_context: If True, also reads campaign history, assets, constraints.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "include_context": {
      "default": false,
      "title": "Include Context",
      "type": "boolean"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "read_client_vaultArguments",
  "type": "object"
}
```

</details>

<a id="resolve_page_identity"></a>

## `resolve_page_identity`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ops.py#L365)


Resolve full identity for a Facebook Page: page details + Instagram business account.

Uses the 3-step IG resolution ladder (registry -> promote_pages -> ad account).
Falls back to direct page query if account_id not provided.

Args:
    page_id: Facebook Page ID.
    account_id: Optional ad account ID for improved IG resolution.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "account_id": {
      "default": null,
      "title": "Account Id",
      "type": "string"
    }
  },
  "required": [
    "page_id"
  ],
  "title": "resolve_page_identityArguments",
  "type": "object"
}
```

</details>

<a id="run_setup_check"></a>

## `run_setup_check`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/setup.py#L20)


Check MCP setup readiness and return structured results.

Validates token, permissions, account access, pages, Instagram identity,
pixels, and local configuration. Returns pass/warn/fail for each check
with exact fix instructions for failures.

Read-only. Does not modify any configuration or Meta settings.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {},
  "title": "run_setup_checkArguments",
  "type": "object"
}
```

</details>

<a id="run_tracking_diagnostic"></a>

## `run_tracking_diagnostic`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/pixels.py#L437)


Run comprehensive tracking diagnostic for an ad account.

Checks all connected pixels, event coverage, parameter completeness,
and Meta diagnostic flags. Returns archetype-aware health classification
with severity-ranked issues and fix suggestions.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    archetype: Account archetype for requirement matching.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "archetype": {
      "default": "hybrid",
      "title": "Archetype",
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "run_tracking_diagnosticArguments",
  "type": "object"
}
```

</details>

<a id="search_behaviors"></a>

## `search_behaviors`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/targeting.py#L99)


Search or list behavior-based targeting options.

If query is provided, filters by keyword. Otherwise returns all behaviors.

Args:
    query: Optional search term (e.g., 'travel', 'small business').
    limit: Max results (default 30).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
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
      "title": "Query"
    },
    "limit": {
      "default": 30,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "search_behaviorsArguments",
  "type": "object"
}
```

</details>

<a id="search_demographics"></a>

## `search_demographics`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/targeting.py#L278)


Search or list demographic targeting options.

Returns demographic categories: life events, education, work,
financial, relationship, home ownership, parental status, etc.

If query is provided, filters by keyword. Otherwise returns all demographics.

Args:
    query: Optional search term (e.g., 'homeowner', 'new job', 'university').
    limit: Max results (default 30).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
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
      "title": "Query"
    },
    "limit": {
      "default": 30,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "search_demographicsArguments",
  "type": "object"
}
```

</details>

<a id="search_geo_locations"></a>

## `search_geo_locations`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/targeting.py#L154)


Search geographic locations for ad targeting.

Args:
    query: Location search term (e.g., 'Greece', 'Athens', 'Crete').
    location_type: Type of location: 'country', 'region', 'city', 'zip',
        'geo_market', 'electoral_district'. Default 'country'.
    limit: Max results (default 10).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "location_type": {
      "default": "country",
      "title": "Location Type",
      "type": "string"
    },
    "limit": {
      "default": 10,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "search_geo_locationsArguments",
  "type": "object"
}
```

</details>

<a id="search_interests"></a>

## `search_interests`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/targeting.py#L38)


Search for interest-based targeting options.

Returns matching interests with audience size estimates, topic category, and path.

Args:
    query: Search term (e.g., 'yoga', 'hospitality', 'skincare').
    limit: Max results (default 20).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "limit": {
      "default": 20,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "query"
  ],
  "title": "search_interestsArguments",
  "type": "object"
}
```

</details>

<a id="send_test_event"></a>

## `send_test_event`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/pixels.py#L359)


Send a test event via the Conversions API Test Events endpoint.

Args:
    pixel_id: Pixel ID (numeric string).
    event_name: Event name to send (default 'PageView').
    test_event_code: Test event code from Events Manager.
        If not provided, generates a temporary one.
    custom_data: Optional JSON string of custom_data params
        (e.g., '{"value": 10.00, "currency": "EUR"}').


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "pixel_id": {
      "title": "Pixel Id",
      "type": "string"
    },
    "event_name": {
      "default": "PageView",
      "title": "Event Name",
      "type": "string"
    },
    "test_event_code": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Test Event Code"
    },
    "custom_data": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Custom Data"
    }
  },
  "required": [
    "pixel_id"
  ],
  "title": "send_test_eventArguments",
  "type": "object"
}
```

</details>

<a id="update_ad"></a>

## `update_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ads.py#L942)


Update an existing ad. Supervised write - validates before applying.

Takes a pre-write snapshot for rollback, validates the update payload,
applies via Meta API, and verifies post-write state.

Note on creative_id: Swaps the creative attached to this ad. The new creative
must already exist (created via create_multi_asset_ad or the Meta UI).
This does NOT create a new creative - it re-points the ad to an existing one.

Args:
    ad_id: Ad ID to update.
    name: New ad name. Subject to naming enforcement.
    status: New status. Allowed: 'PAUSED', 'ACTIVE', 'ARCHIVED'.
        Activating requires confirmation-level validation.
    creative_id: ID of an existing creative to attach to this ad.
        Format: numeric string (e.g., '120239290442460377').


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
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
      "title": "Creative Id"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "update_adArguments",
  "type": "object"
}
```

</details>

<a id="update_ad_creative"></a>

## `update_ad_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/creatives.py#L597)


Update an existing ad creative's name.

IMPORTANT: Meta API does NOT allow changing copy, headline, CTA, or link URL
on existing creatives. Creative content is immutable after creation.

To change ad copy: create a NEW creative with create_ad_creative, then swap
it on the ad with update_ad(creative_id=new_creative_id).

Args:
    creative_id: Creative ID to update.
    name: New creative name.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "creative_id": {
      "title": "Creative Id",
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
      "title": "Name"
    }
  },
  "required": [
    "creative_id"
  ],
  "title": "update_ad_creativeArguments",
  "type": "object"
}
```

</details>

<a id="update_adset"></a>

## `update_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/adsets.py#L861)


Update an existing ad set. Supervised write - validates before applying.

Takes a pre-write snapshot for rollback, validates the update payload,
applies via Meta API, and verifies post-write state.

Note on budgets: ABO/CBO rules are enforced. If the parent campaign uses CBO
(has campaign-level budget), ad set budget updates are blocked. Budget updates
are only allowed for ABO ad sets (parent campaign has no budget).

Note on targeting: targeting_json must be a valid Meta targeting spec JSON object.
Partial updates are supported - Meta merges provided fields with existing targeting.
To clear a field, set it explicitly to null in the JSON.

Args:
    adset_id: Ad set ID to update.
    name: New ad set name. Subject to naming enforcement.
    status: New status. Allowed: 'PAUSED', 'ACTIVE', 'ARCHIVED'.
        Activating requires confirmation-level validation.
    daily_budget: New daily budget in currency units (e.g., 15.0 for EUR 15).
        Only allowed for ABO ad sets. Mutually exclusive with lifetime_budget.
    lifetime_budget: New lifetime budget in currency units.
        Only allowed for ABO ad sets. Mutually exclusive with daily_budget.
    targeting_json: JSON string of targeting spec to apply.
        Example: '{"geo_locations":{"countries":["GR"]},"age_min":25,"age_max":55}'
    start_time: New start time (ISO 8601 format).
    end_time: New end time (ISO 8601 format).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
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
      "title": "Lifetime Budget"
    },
    "targeting_json": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Targeting Json"
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
      "title": "End Time"
    }
  },
  "required": [
    "adset_id"
  ],
  "title": "update_adsetArguments",
  "type": "object"
}
```

</details>

<a id="update_campaign"></a>

## `update_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/campaigns.py#L473)


Update an existing campaign. Supervised write - validates before applying.

Takes a pre-write snapshot for rollback, validates the update payload,
applies via Meta API, and verifies post-write state.

Args:
    campaign_id: Campaign ID to update.
    name: New campaign name. Subject to naming enforcement.
    daily_budget: New daily budget in currency units (e.g., 50.0 for EUR 50).
        Mutually exclusive with lifetime_budget.
    lifetime_budget: New lifetime budget in currency units.
        Mutually exclusive with daily_budget.
    status: New status. Allowed: 'PAUSED', 'ACTIVE', 'ARCHIVED'.
        Activating requires confirmation-level validation.
    start_time: New start time (ISO 8601 format).
    end_time: New end time / stop_time (ISO 8601 format).
    special_ad_categories: Comma-separated categories or empty string to clear.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
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
      "title": "Name"
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
      "title": "Lifetime Budget"
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
      "title": "Status"
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
      "title": "End Time"
    },
    "special_ad_categories": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Special Ad Categories"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "update_campaignArguments",
  "type": "object"
}
```

</details>

<a id="update_product_set"></a>

## `update_product_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/catalogs.py#L518)


Update a product set name or filter rules.

Args:
    product_set_id: Product set ID to update.
    name: New name.
    filter_json: New filter rules as JSON string.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "product_set_id": {
      "title": "Product Set Id",
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
      "title": "Name"
    },
    "filter_json": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Filter Json"
    }
  },
  "required": [
    "product_set_id"
  ],
  "title": "update_product_setArguments",
  "type": "object"
}
```

</details>

<a id="upload_ad_image"></a>

## `upload_ad_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/images.py#L21)


Upload an image from URL into Meta ad images library.

Downloads the image from the provided URL, then uploads it to Meta
via multipart form upload. Returns the image hash needed for creative
creation (create_ad_creative, create_multi_asset_ad) and ad building.

Supported formats: JPG, PNG. Max size: 30MB.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    image_url: Public URL of the image to upload.
    name: Optional name for the image in the library.
        Defaults to filename from URL.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "image_url": {
      "title": "Image Url",
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
      "title": "Name"
    }
  },
  "required": [
    "account_id",
    "image_url"
  ],
  "title": "upload_ad_imageArguments",
  "type": "object"
}
```

</details>

<a id="upload_video_asset"></a>

## `upload_video_asset`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/video.py#L82)


Upload a local video file to a Meta ad account.

Validates the file, uploads via simple upload (for files < 1GB),
and returns the meta_video_id for use in ad creation.
The video enters processing after upload - use poll_video_processing
to check when it's ready.

Args:
    account_id: Ad account ID (e.g., 'act_123456789').
    video_path: Local filesystem path to the video file (.mp4 or .mov).
    title: Optional title for the video in Meta.
    description: Optional description.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "video_path": {
      "title": "Video Path",
      "type": "string"
    },
    "title": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Title"
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
      "title": "Description"
    }
  },
  "required": [
    "account_id",
    "video_path"
  ],
  "title": "upload_video_assetArguments",
  "type": "object"
}
```

</details>

<a id="upload_video_resumable"></a>

## `upload_video_resumable`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/ops.py#L29)


Upload a video file using resumable upload (supports files >100MB up to 4GB).

Use this for large files that fail with upload_video_asset.
Automatically chunks the file and uploads sequentially.

Args:
    account_id: Ad account ID.
    video_path: Local path to .mp4 or .mov file.
    title: Optional title (defaults to filename).
    chunk_size_mb: Chunk size in MB (default 20).


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "video_path": {
      "title": "Video Path",
      "type": "string"
    },
    "title": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Title"
    },
    "chunk_size_mb": {
      "default": 20,
      "title": "Chunk Size Mb",
      "type": "integer"
    }
  },
  "required": [
    "account_id",
    "video_path"
  ],
  "title": "upload_video_resumableArguments",
  "type": "object"
}
```

</details>

<a id="validate_catalog_connections"></a>

## `validate_catalog_connections`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/brandu-mos/konquest-meta-ads-mcp/blob/762c224b060b233b66fb9af8a2f3865303ed757b/meta_ads_mcp/core/catalogs.py#L203)


Validate the catalog-pixel-account-page connection chain
and run diagnostic health assessment.

For DPA (Dynamic Product Ads) to work, the full chain must be connected:
Catalog -> Pixel -> Ad Account -> Page

Args:
    catalog_id: Product catalog ID.
    account_id: Optional ad account ID to verify connection.
    pixel_id: Optional pixel ID to verify catalog-pixel link.
    page_id: Optional page ID to verify catalog-page link.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "catalog_id": {
      "title": "Catalog Id",
      "type": "string"
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
      "title": "Pixel Id"
    },
    "page_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Page Id"
    }
  },
  "required": [
    "catalog_id"
  ],
  "title": "validate_catalog_connectionsArguments",
  "type": "object"
}
```

</details>

