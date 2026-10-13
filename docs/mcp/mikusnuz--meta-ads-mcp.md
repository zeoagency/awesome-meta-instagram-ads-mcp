# mikusnuz/meta-ads-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/mikusnuz/meta-ads-mcp) · [Machine-readable snapshot](../../catalog/mikusnuz--meta-ads-mcp.json)

Complete registered tool snapshot. **134 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`e6bec2599e43`](https://github.com/mikusnuz/meta-ads-mcp/tree/e6bec2599e4394b355d553b38db41495aa24c910). Method: `runtime-tools-list`.

- Some structured payloads are registered as JSON strings; these remain strings in the schemas.

## Tools

- [add_business_user](#add_business_user)
- [add_to_block_list](#add_to_block_list)
- [add_users_to_audience](#add_users_to_audience)
- [batch_products](#batch_products)
- [copy_ad](#copy_ad)
- [copy_adset](#copy_adset)
- [copy_campaign](#copy_campaign)
- [create_ad](#create_ad)
- [create_adset](#create_adset)
- [create_async_report](#create_async_report)
- [create_block_list](#create_block_list)
- [create_budget_schedule](#create_budget_schedule)
- [create_campaign](#create_campaign)
- [create_canvas](#create_canvas)
- [create_catalog](#create_catalog)
- [create_creative](#create_creative)
- [create_custom_audience](#create_custom_audience)
- [create_dynamic_creative](#create_dynamic_creative)
- [create_experiment](#create_experiment)
- [create_feed](#create_feed)
- [create_lead_form](#create_lead_form)
- [create_lookalike_audience](#create_lookalike_audience)
- [create_offline_event_set](#create_offline_event_set)
- [create_product_set](#create_product_set)
- [create_rf_prediction](#create_rf_prediction)
- [create_rule](#create_rule)
- [create_system_user](#create_system_user)
- [debug_token](#debug_token)
- [delete_ad](#delete_ad)
- [delete_adset](#delete_adset)
- [delete_audience](#delete_audience)
- [delete_block_list](#delete_block_list)
- [delete_budget_schedule](#delete_budget_schedule)
- [delete_campaign](#delete_campaign)
- [delete_canvas](#delete_canvas)
- [delete_image](#delete_image)
- [delete_rf_prediction](#delete_rf_prediction)
- [delete_rule](#delete_rule)
- [delete_video](#delete_video)
- [exchange_token](#exchange_token)
- [generate_preview](#generate_preview)
- [get_account_activities](#get_account_activities)
- [get_account_insights](#get_account_insights)
- [get_ad](#get_ad)
- [get_ad_account](#get_ad_account)
- [get_ad_insights](#get_ad_insights)
- [get_ad_preview](#get_ad_preview)
- [get_adset](#get_adset)
- [get_adset_ads](#get_adset_ads)
- [get_adset_insights](#get_adset_insights)
- [get_adset_leads](#get_adset_leads)
- [get_adset_targeting_sentence](#get_adset_targeting_sentence)
- [get_async_report](#get_async_report)
- [get_audience](#get_audience)
- [get_audience_health](#get_audience_health)
- [get_batch_status](#get_batch_status)
- [get_business](#get_business)
- [get_campaign](#get_campaign)
- [get_campaign_ads](#get_campaign_ads)
- [get_campaign_adsets](#get_campaign_adsets)
- [get_campaign_insights](#get_campaign_insights)
- [get_campaign_leads](#get_campaign_leads)
- [get_canvas](#get_canvas)
- [get_catalog](#get_catalog)
- [get_creative](#get_creative)
- [get_delivery_estimate](#get_delivery_estimate)
- [get_experiment](#get_experiment)
- [get_experiment_results](#get_experiment_results)
- [get_feed_uploads](#get_feed_uploads)
- [get_form_leads](#get_form_leads)
- [get_image](#get_image)
- [get_lead](#get_lead)
- [get_lead_form](#get_lead_form)
- [get_product](#get_product)
- [get_product_set](#get_product_set)
- [get_reach_estimate](#get_reach_estimate)
- [get_rf_prediction](#get_rf_prediction)
- [get_rule](#get_rule)
- [get_saved_audience](#get_saved_audience)
- [get_targeting_suggestions](#get_targeting_suggestions)
- [get_video](#get_video)
- [list_account_users](#list_account_users)
- [list_ad_accounts](#list_ad_accounts)
- [list_ads](#list_ads)
- [list_adsets](#list_adsets)
- [list_block_lists](#list_block_lists)
- [list_budget_schedules](#list_budget_schedules)
- [list_business_ad_accounts](#list_business_ad_accounts)
- [list_business_instagram_accounts](#list_business_instagram_accounts)
- [list_business_pages](#list_business_pages)
- [list_business_users](#list_business_users)
- [list_businesses](#list_businesses)
- [list_campaigns](#list_campaigns)
- [list_canvases](#list_canvases)
- [list_catalogs](#list_catalogs)
- [list_creatives](#list_creatives)
- [list_custom_audiences](#list_custom_audiences)
- [list_experiments](#list_experiments)
- [list_feeds](#list_feeds)
- [list_images](#list_images)
- [list_lead_forms](#list_lead_forms)
- [list_offline_event_sets](#list_offline_event_sets)
- [list_product_sets](#list_product_sets)
- [list_products](#list_products)
- [list_rf_predictions](#list_rf_predictions)
- [list_rules](#list_rules)
- [list_saved_audiences](#list_saved_audiences)
- [list_system_users](#list_system_users)
- [list_videos](#list_videos)
- [refresh_token](#refresh_token)
- [remove_business_user](#remove_business_user)
- [remove_from_block_list](#remove_from_block_list)
- [remove_users_from_audience](#remove_users_from_audience)
- [search_ad_library](#search_ad_library)
- [search_locations](#search_locations)
- [search_targeting](#search_targeting)
- [search_targeting_map](#search_targeting_map)
- [send_conversion_event](#send_conversion_event)
- [send_offline_event](#send_offline_event)
- [update_ad](#update_ad)
- [update_ad_account](#update_ad_account)
- [update_adset](#update_adset)
- [update_audience](#update_audience)
- [update_budget_schedule](#update_budget_schedule)
- [update_campaign](#update_campaign)
- [update_catalog](#update_catalog)
- [update_creative](#update_creative)
- [update_experiment](#update_experiment)
- [update_product](#update_product)
- [update_product_set](#update_product_set)
- [update_rule](#update_rule)
- [upload_feed](#upload_feed)
- [upload_image](#upload_image)
- [upload_video](#upload_video)

<a id="add_business_user"></a>

## `add_business_user`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L108)

Add a user to the configured business by email. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "email": {
      "type": "string",
      "description": "Email address of the user to add"
    },
    "role": {
      "type": "string",
      "enum": [
        "ADMIN",
        "EMPLOYEE"
      ],
      "description": "Role for the new user"
    }
  },
  "required": [
    "email",
    "role"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="add_to_block_list"></a>

## `add_to_block_list`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/brand_safety.ts#L50)

Add publisher URLs to an existing block list.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "list_id": {
      "type": "string",
      "description": "Block list ID"
    },
    "urls": {
      "type": "string",
      "description": "JSON array of URLs to block (e.g. '[\"example.com\",\"bad-site.com\"]')"
    }
  },
  "required": [
    "list_id",
    "urls"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="add_users_to_audience"></a>

## `add_users_to_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L128)

Add users to a custom audience. Payload must be a JSON string containing hashed user data with a schema array defining the data types (e.g. EMAIL, PHONE, FN, LN).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "Audience ID"
    },
    "payload": {
      "type": "string",
      "description": "JSON string: {schema: ['EMAIL','PHONE',...], data: [['hash1','hash2',...], ...]}. All PII must be SHA-256 hashed."
    }
  },
  "required": [
    "audience_id",
    "payload"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="batch_products"></a>

## `batch_products`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L220)

Batch create, update, or delete products in a catalog. Supports up to 5,000 items per request. Update operations support upsert.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "requests": {
      "type": "string",
      "description": "JSON array of batch requests. Each: {method: 'CREATE'|'UPDATE'|'DELETE', retailer_id: string, data?: {name, description, price, url, image_url, availability, ...}}"
    },
    "allow_upsert": {
      "type": "boolean",
      "default": false,
      "description": "Allow UPDATE to create items if they don't exist (default false)"
    }
  },
  "required": [
    "catalog_id",
    "requests"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="copy_ad"></a>

## `copy_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L124)

Copy an existing ad. Creates a duplicate within the same or different ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Source ad ID to copy"
    },
    "adset_id": {
      "type": "string",
      "description": "Target ad set ID. If omitted, copies to same ad set"
    },
    "name": {
      "type": "string",
      "description": "Name for the copied ad"
    },
    "status": {
      "type": "string",
      "default": "PAUSED",
      "description": "Status for copied ad (default PAUSED)"
    }
  },
  "required": [
    "ad_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="copy_adset"></a>

## `copy_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L149)

Copy an existing ad set. Creates a duplicate within the same or different campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Source ad set ID to copy"
    },
    "campaign_id": {
      "type": "string",
      "description": "Target campaign ID. If omitted, copies to same campaign"
    },
    "name": {
      "type": "string",
      "description": "Name for the copied ad set"
    },
    "status": {
      "type": "string",
      "default": "PAUSED",
      "description": "Status for copied ad set (default PAUSED)"
    },
    "deep_copy": {
      "type": "boolean",
      "default": true,
      "description": "Copy ads within the ad set (default true)"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="copy_campaign"></a>

## `copy_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L154)

Copy an existing campaign. Creates a duplicate with optional name override. Copies structure including ad sets and ads.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Source campaign ID to copy"
    },
    "name": {
      "type": "string",
      "description": "Name for the copied campaign. Defaults to 'Copy of <original>'"
    },
    "status": {
      "type": "string",
      "default": "PAUSED",
      "description": "Status for copied campaign (default PAUSED)"
    },
    "deep_copy": {
      "type": "boolean",
      "default": true,
      "description": "Copy ad sets and ads within the campaign (default true)"
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_ad"></a>

## `create_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L57)

Create a new ad. Requires name, adset_id, and creative (JSON object_story_spec). Defaults to PAUSED status.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Ad name"
    },
    "adset_id": {
      "type": "string",
      "description": "Parent ad set ID"
    },
    "creative": {
      "type": "string",
      "description": "JSON string of creative spec (object_story_spec with page_id, link_data/photo_data/video_data). Note: as of v26.0, a creative with applink_treatment=web_only can no longer be attached to an ad in a campaign using Website and App conversion locations — use automatic destination selection or a compatible manual destination instead."
    },
    "status": {
      "type": "string",
      "default": "PAUSED",
      "description": "Ad status (default PAUSED)"
    },
    "tracking_specs": {
      "type": "string",
      "description": "JSON string of tracking specs array"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the ad in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "adset_id",
    "creative"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_adset"></a>

## `create_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L55)

Create a new ad set. Requires name, campaign_id, budget, optimization_goal, billing_event, and targeting. Defaults to PAUSED status.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Ad set name"
    },
    "campaign_id": {
      "type": "string",
      "description": "Parent campaign ID"
    },
    "daily_budget": {
      "type": "string",
      "description": "Daily budget in currency cents (e.g. '5000' = $50.00)"
    },
    "lifetime_budget": {
      "type": "string",
      "description": "Lifetime budget in currency cents"
    },
    "optimization_goal": {
      "type": "string",
      "description": "Optimization goal: NONE, APP_INSTALLS, AD_RECALL_LIFT, ENGAGED_USERS, EVENT_RESPONSES, IMPRESSIONS, LEAD_GENERATION, QUALITY_LEAD, LINK_CLICKS, OFFSITE_CONVERSIONS, PAGE_LIKES, POST_ENGAGEMENT, QUALITY_CALL, REACH, LANDING_PAGE_VIEWS, VISIT_INSTAGRAM_PROFILE, ENGAGED_PAGE_VIEWS, VALUE, THRUPLAY, DERIVED_EVENTS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, CONVERSATIONS, IN_APP_VALUE, MESSAGING_PURCHASE_CONVERSION, MESSAGING_DEEP_CONVERSATION_AND_FOLLOW, SUBSCRIBERS, REMINDERS_SET, MEANINGFUL_CALL_ATTEMPT, PROFILE_VISIT, PROFILE_AND_PAGE_ENGAGEMENT, ADVERTISER_SILOED_VALUE, AUTOMATIC_OBJECTIVE, MESSAGING_APPOINTMENT_CONVERSION"
    },
    "billing_event": {
      "type": "string",
      "description": "Billing event: APP_INSTALLS, CLICKS, IMPRESSIONS, LINK_CLICKS, NONE, OFFER_CLAIMS, PAGE_LIKES, POST_ENGAGEMENT, THRUPLAY, PURCHASE, LISTING_INTERACTION"
    },
    "bid_strategy": {
      "type": "string",
      "description": "Bid strategy: LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS"
    },
    "targeting": {
      "type": "string",
      "description": "JSON string of targeting spec (age_min, age_max, genders, geo_locations, interests, etc.). Advantage+ Audience automation and other flags go inside this object too, e.g. targeting_automation: {\"advantage_audience\":1}. As of v26.0, ad sets in the Housing, Employment, or Financial Products and Services (HEC-F) special ad categories with relaxable (non-broad) targeting must explicitly set targeting.targeting_automation.advantage_audience to 1 or 0 — omitting it now returns ADS_TARGETING__REQUIRE_EXPLICIT_ADVANTAGE_AUDIENCE_FLAG. Not required for broad/default audience setups. Also note: as of Marketing API v26.0, the Instagram Explore Feed placement was removed (explicitly specifying it in publisher_platforms/instagram_positions now returns an error) and the 'story' value in messenger_positions is silently dropped."
    },
    "promoted_object": {
      "type": "string",
      "description": "JSON string of the promoted_object spec. Required for many objectives, e.g. OUTCOME_SALES needs {\"pixel_id\":\"...\",\"custom_event_type\":\"PURCHASE\"}, OUTCOME_APP_PROMOTION needs {\"application_id\":\"...\",\"object_store_url\":\"...\"}, OUTCOME_ENGAGEMENT page-like ads need {\"page_id\":\"...\"}. Omitting it when the objective requires one causes ad set creation to fail."
    },
    "start_time": {
      "type": "string",
      "description": "Start time (ISO 8601)"
    },
    "end_time": {
      "type": "string",
      "description": "End time (ISO 8601)"
    },
    "status": {
      "type": "string",
      "default": "PAUSED",
      "description": "Ad set status (default PAUSED)"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the ad set in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "campaign_id",
    "optimization_goal",
    "billing_event",
    "targeting"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_async_report"></a>

## `create_async_report`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/insights.ts#L93)

Create an async insight report for large data queries. Returns a report_run_id to poll with get_async_report.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "default": "impressions,clicks,spend,reach,frequency,cpc,cpm,ctr,actions,cost_per_action_type",
      "description": "Comma-separated insight fields"
    },
    "breakdowns": {
      "type": "string",
      "description": "Breakdown dimensions: age,gender,country,region,publisher_platform,platform_position,device_platform,comscore_market (replaces dma). Some accounts must opt in in Ads Manager for impression_device, hourly_stats_aggregated_by_audience_time_zone, and frequency_value; empty results do not necessarily mean zero performance."
    },
    "date_preset": {
      "type": "string",
      "description": "Lowercase date preset, for example: today, yesterday, last_7d, last_14d, last_30d, this_month, last_month, this_quarter, last_quarter, this_year, last_year"
    },
    "time_range": {
      "type": "string",
      "description": "JSON string {since,until} in YYYY-MM-DD format"
    },
    "time_increment": {
      "type": "string",
      "description": "Time granularity: all_days, 1, 7, monthly"
    },
    "filtering": {
      "type": "string",
      "description": "JSON string for filtering"
    },
    "level": {
      "type": "string",
      "description": "Aggregation level: campaign, adset, ad"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_block_list"></a>

## `create_block_list`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/brand_safety.ts#L31)

Create a new publisher block list for the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Name for the block list"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the block list in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_budget_schedule"></a>

## `create_budget_schedule`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/budget.ts#L36)

Create a budget schedule on a campaign or ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "parent_id": {
      "type": "string",
      "minLength": 1,
      "description": "Campaign or ad set ID that will own the budget schedule"
    },
    "parent_type": {
      "type": "string",
      "enum": [
        "campaign",
        "adset"
      ],
      "default": "campaign",
      "description": "Type of parent object"
    },
    "budget_value": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "Unsigned value interpreted according to budget_value_type (ABSOLUTE uses currency minor units)"
    },
    "budget_value_type": {
      "type": "string",
      "enum": [
        "ABSOLUTE",
        "MULTIPLIER"
      ],
      "description": "How budget_value is applied"
    },
    "time_start": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "Schedule start time as a Unix timestamp"
    },
    "time_end": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "Schedule end time as a Unix timestamp"
    }
  },
  "required": [
    "parent_id",
    "budget_value",
    "budget_value_type",
    "time_start",
    "time_end"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_campaign"></a>

## `create_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L57)

Create a new ad campaign. Defaults to PAUSED status. Requires name and objective. Budget can be set at campaign or ad set level.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Campaign name"
    },
    "objective": {
      "type": "string",
      "enum": [
        "OUTCOME_AWARENESS",
        "OUTCOME_ENGAGEMENT",
        "OUTCOME_LEADS",
        "OUTCOME_SALES",
        "OUTCOME_TRAFFIC",
        "OUTCOME_APP_PROMOTION"
      ],
      "description": "Campaign objective"
    },
    "status": {
      "type": "string",
      "default": "PAUSED",
      "description": "Campaign status (default PAUSED)"
    },
    "daily_budget": {
      "type": "string",
      "description": "Daily budget in account currency cents (e.g. '5000' = $50.00)"
    },
    "lifetime_budget": {
      "type": "string",
      "description": "Lifetime budget in account currency cents"
    },
    "special_ad_categories": {
      "type": "string",
      "description": "JSON array of special ad categories: HOUSING, EMPLOYMENT, FINANCIAL_PRODUCTS_SERVICES, ISSUES_ELECTIONS_POLITICS, NONE. This field is required by Meta on every campaign — pass '[]' or '[\"NONE\"]' if none apply. CREDIT was renamed to FINANCIAL_PRODUCTS_SERVICES; the old name is no longer accepted."
    },
    "special_ad_category_country": {
      "type": "string",
      "description": "JSON array of ISO 3166-1 alpha-2 country codes, e.g. '[\"US\"]'. Required for ISSUES_ELECTIONS_POLITICS (which also requires authorization to run ads in those countries). For HOUSING, EMPLOYMENT, and FINANCIAL_PRODUCTS_SERVICES it is optional and defaults to the ad account's listed tax country if omitted."
    },
    "start_time": {
      "type": "string",
      "description": "Campaign start time (ISO 8601 format)"
    },
    "stop_time": {
      "type": "string",
      "description": "Campaign stop time (ISO 8601 format)"
    },
    "bid_strategy": {
      "type": "string",
      "description": "Bid strategy: LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS. Meta defaults new campaigns to LOWEST_COST_WITH_BID_CAP, which requires a bid_amount on every ad set — pass LOWEST_COST_WITHOUT_CAP to avoid that."
    },
    "spend_cap": {
      "type": "string",
      "description": "Lifetime spend cap for the campaign, in account currency cents. Once set it cannot be removed, only raised or reset — pass '0' to reset/clear it."
    },
    "is_adset_budget_sharing_enabled": {
      "type": "boolean",
      "description": "Whether ad sets under this campaign can share budget with each other. Required on some newer ad accounts — omitting it can cause campaign creation to fail with 'Must specify True or False in is_adset_budget_sharing_enabled'."
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the campaign in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "objective"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_canvas"></a>

## `create_canvas`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/canvas.ts#L51)

Create a new Instant Experience (Canvas) on a Facebook Page. Requires page_id and body_elements JSON array defining the canvas layout.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "page_id": {
      "type": "string",
      "description": "Facebook Page ID to create the canvas on"
    },
    "body_elements": {
      "type": "string",
      "description": "JSON array of canvas body elements (buttons, carousels, photos, videos, text, etc.)"
    },
    "name": {
      "type": "string",
      "description": "Canvas name"
    }
  },
  "required": [
    "page_id",
    "body_elements"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_catalog"></a>

## `create_catalog`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L45)

Create a new product catalog for the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Catalog name"
    },
    "vertical": {
      "type": "string",
      "description": "Catalog vertical: commerce, hotels, flights, destinations, home_listings, vehicles"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the catalog in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_creative"></a>

## `create_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/creatives.ts#L66)

Create a new ad creative with object_story_spec. The spec defines the ad content (link, photo, or video) and the associated Facebook Page. Notes for v26.0: poll_spec and the poll type under interactive_components_spec are no longer supported and will be rejected. If the advertiser has a shop, eligible creatives now default to destination_spec.destination_type=WEBSITE_AND_SHOP — set it to WEBSITE_AND_SHOP_OPT_OUT to opt out.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Creative name"
    },
    "object_story_spec": {
      "type": "string",
      "description": "JSON string of object_story_spec (page_id, link_data/photo_data/video_data). Use the separate wamo_whatsapp_identity_spec parameter for WhatsApp Status ads."
    },
    "url_tags": {
      "type": "string",
      "description": "URL tags to append to all links"
    },
    "asset_feed_spec": {
      "type": "string",
      "description": "JSON string of asset_feed_spec for dynamic creative"
    },
    "destination_spec": {
      "type": "string",
      "description": "JSON object controlling the destination; set destination_type=WEBSITE_AND_SHOP_OPT_OUT to opt out of the v26 Shops default"
    },
    "wamo_whatsapp_identity_spec": {
      "type": "string",
      "description": "JSON object with wamo_whatsapp_identity_id or whatsapp_phone_number for WhatsApp Status ads; sent at the creative's top level"
    },
    "degrees_of_freedom_spec": {
      "type": "string",
      "description": "JSON object for Advantage+ creative controls, including creative_features_spec.image_animation, video_filtering, and video_uncrop"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the creative in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "object_story_spec"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_custom_audience"></a>

## `create_custom_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L51)

Create a new custom audience. Subtype determines the audience source (CUSTOM, WEBSITE, APP, OFFLINE_CONVERSION, LOOKALIKE, ENGAGEMENT, etc.).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Audience name"
    },
    "subtype": {
      "type": "string",
      "enum": [
        "CUSTOM",
        "WEBSITE",
        "APP",
        "OFFLINE_CONVERSION",
        "CLAIM",
        "PARTNER",
        "MANAGED",
        "VIDEO",
        "LOOKALIKE",
        "ENGAGEMENT",
        "BAG_OF_ACCOUNTS",
        "STUDY_RULE_AUDIENCE",
        "FOX"
      ],
      "description": "Audience subtype"
    },
    "description": {
      "type": "string",
      "description": "Audience description"
    },
    "customer_file_source": {
      "type": "string",
      "description": "Source of customer file: USER_PROVIDED_ONLY, PARTNER_PROVIDED_ONLY, BOTH_USER_AND_PARTNER_PROVIDED"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the audience in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "subtype"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_dynamic_creative"></a>

## `create_dynamic_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/creatives.ts#L122)

Create a dynamic creative with asset_feed_spec. Meta automatically combines different images, videos, titles, bodies, and CTAs to find the best performing combinations.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Creative name"
    },
    "asset_feed_spec": {
      "type": "string",
      "description": "JSON string of asset_feed_spec with arrays: images (hash), videos (video_id), bodies (text), titles (text), descriptions (text), call_to_action_types"
    },
    "object_story_spec": {
      "type": "string",
      "description": "JSON object containing the associated page_id and optional instagram_user_id"
    },
    "destination_spec": {
      "type": "string",
      "description": "JSON object controlling the destination; set destination_type=WEBSITE_AND_SHOP_OPT_OUT to opt out of the v26 Shops default"
    },
    "wamo_whatsapp_identity_spec": {
      "type": "string",
      "description": "JSON object with wamo_whatsapp_identity_id or whatsapp_phone_number for WhatsApp Status ads; sent at the creative's top level"
    },
    "degrees_of_freedom_spec": {
      "type": "string",
      "description": "JSON object for Advantage+ creative controls, including creative_features_spec.image_animation, video_filtering, and video_uncrop"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the creative in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "asset_feed_spec"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_experiment"></a>

## `create_experiment`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/experiments.ts#L27)

Create a new A/B test experiment (ad study).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Experiment name"
    },
    "description": {
      "type": "string",
      "description": "Experiment description"
    },
    "start_time": {
      "type": "string",
      "description": "Start time in ISO 8601 or Unix timestamp"
    },
    "end_time": {
      "type": "string",
      "description": "End time in ISO 8601 or Unix timestamp"
    },
    "type": {
      "type": "string",
      "description": "Study type"
    },
    "cells": {
      "type": "string",
      "description": "JSON array of test cells: [{name, campaign_id}]"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the experiment in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "start_time",
    "end_time",
    "cells"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_feed"></a>

## `create_feed`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/feeds.ts#L27)

Create a new product feed for a catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "name": {
      "type": "string",
      "description": "Feed name"
    },
    "schedule": {
      "type": "string",
      "description": "JSON string for feed schedule configuration"
    },
    "file_url": {
      "type": "string",
      "description": "URL of the feed file"
    }
  },
  "required": [
    "catalog_id",
    "name"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_lead_form"></a>

## `create_lead_form`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/leads.ts#L65)

Create a new lead generation form on a Facebook Page. Requires pages_manage_ads permission.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "page_id": {
      "type": "string",
      "description": "Facebook Page ID"
    },
    "name": {
      "type": "string",
      "description": "Lead form name"
    },
    "questions": {
      "type": "string",
      "description": "JSON array of questions. Each: {key: string, type: 'CUSTOM'|'EMAIL'|'PHONE'|'FULL_NAME'|'CITY'|'STATE'|'COUNTRY'|'ZIP'|'JOB_TITLE'|'COMPANY_NAME', label?: string}"
    },
    "privacy_policy_url": {
      "type": "string",
      "description": "URL to privacy policy"
    },
    "follow_up_action_url": {
      "type": "string",
      "description": "URL to redirect after submission"
    },
    "thank_you_page": {
      "type": "string",
      "description": "JSON object: {title: string, body: string, button_text?: string, button_type?: 'VIEW_WEBSITE'|'DOWNLOAD'}"
    }
  },
  "required": [
    "page_id",
    "name",
    "questions",
    "privacy_policy_url"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_lookalike_audience"></a>

## `create_lookalike_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L164)

Create a lookalike audience based on an existing custom audience. Ratio (1-10) determines how closely the new audience resembles the source.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Lookalike audience name"
    },
    "origin_audience_id": {
      "type": "string",
      "description": "Source custom audience ID"
    },
    "lookalike_spec": {
      "type": "string",
      "description": "JSON string: {country: 'US', ratio: 0.01-0.10} where ratio is the lookalike percentage (1%-10%)"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the audience in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "origin_audience_id",
    "lookalike_spec"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_offline_event_set"></a>

## `create_offline_event_set`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/conversions.ts#L67)

Create a new offline conversion data set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Event set name"
    },
    "description": {
      "type": "string",
      "description": "Event set description"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the event set in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_product_set"></a>

## `create_product_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L102)

Create a new product set within a catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "name": {
      "type": "string",
      "description": "Product set name"
    },
    "filter": {
      "type": "string",
      "description": "JSON string of filter rules for the product set"
    }
  },
  "required": [
    "catalog_id",
    "name"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_rf_prediction"></a>

## `create_rf_prediction`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/reach_frequency.ts#L31)

Create a new reach & frequency prediction. Provide targeting spec as JSON string, budget in cents, and scheduling info.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "target_spec": {
      "type": "string",
      "description": "JSON string of targeting specification"
    },
    "start_time": {
      "type": "string",
      "description": "Prediction start time (ISO 8601 or Unix timestamp)"
    },
    "stop_time": {
      "type": "string",
      "description": "Prediction stop time (ISO 8601 or Unix timestamp)"
    },
    "budget": {
      "type": "number",
      "description": "Budget in account currency cents"
    },
    "frequency_cap": {
      "type": "number",
      "description": "Maximum frequency cap per user"
    },
    "destination_id": {
      "type": "string",
      "description": "Destination ID (e.g. Facebook Page ID)"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the prediction in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "target_spec",
    "start_time",
    "stop_time",
    "budget",
    "frequency_cap",
    "destination_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_rule"></a>

## `create_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/rules.ts#L45)

Create a new automated rule for the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Rule name"
    },
    "evaluation_spec": {
      "type": "string",
      "description": "JSON string defining rule conditions"
    },
    "execution_spec": {
      "type": "string",
      "description": "JSON string defining rule actions"
    },
    "schedule_spec": {
      "type": "string",
      "description": "JSON string defining rule schedule"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to create the rule in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "name",
    "evaluation_spec",
    "execution_spec"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_system_user"></a>

## `create_system_user`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L243)

Create a new system user in the configured business. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Name for the system user"
    },
    "role": {
      "type": "string",
      "enum": [
        "ADMIN",
        "EMPLOYEE"
      ],
      "description": "Role for the system user"
    }
  },
  "required": [
    "name",
    "role"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="debug_token"></a>

## `debug_token`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/auth.ts#L41)

Debug an access token to inspect its properties, permissions, expiration, and validity. Requires META_APP_ID and META_APP_SECRET.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "input_token": {
      "type": "string",
      "description": "Access token to debug/inspect"
    }
  },
  "required": [
    "input_token"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_ad"></a>

## `delete_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L107)

Delete an ad. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Ad ID to delete"
    }
  },
  "required": [
    "ad_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_adset"></a>

## `delete_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L132)

Delete an ad set. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad set ID to delete"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_audience"></a>

## `delete_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L111)

Delete a custom audience. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "Audience ID to delete"
    }
  },
  "required": [
    "audience_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_block_list"></a>

## `delete_block_list`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/brand_safety.ts#L87)

Delete a publisher block list. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "list_id": {
      "type": "string",
      "description": "Block list ID to delete"
    }
  },
  "required": [
    "list_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_budget_schedule"></a>

## `delete_budget_schedule`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/budget.ts#L103)

Delete a budget schedule. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "schedule_id": {
      "type": "string",
      "description": "Budget schedule ID to delete"
    }
  },
  "required": [
    "schedule_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_campaign"></a>

## `delete_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L137)

Delete a campaign. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Campaign ID to delete"
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_canvas"></a>

## `delete_canvas`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/canvas.ts#L72)

Delete an Instant Experience (Canvas). This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "canvas_id": {
      "type": "string",
      "description": "Canvas ID to delete"
    }
  },
  "required": [
    "canvas_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_image"></a>

## `delete_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/images.ts#L85)

Delete an ad image by hash. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "hash": {
      "type": "string",
      "description": "Image hash to delete"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID the image belongs to (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "hash"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_rf_prediction"></a>

## `delete_rf_prediction`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/reach_frequency.ts#L82)

Delete a reach & frequency prediction. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "prediction_id": {
      "type": "string",
      "description": "Prediction ID to delete"
    }
  },
  "required": [
    "prediction_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_rule"></a>

## `delete_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/rules.ts#L88)

Delete an automated rule.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "rule_id": {
      "type": "string",
      "description": "Rule ID"
    }
  },
  "required": [
    "rule_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_video"></a>

## `delete_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/videos.ts#L89)

Delete an ad video. This action is irreversible.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "video_id": {
      "type": "string",
      "description": "Video ID to delete"
    }
  },
  "required": [
    "video_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="exchange_token"></a>

## `exchange_token`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/auth.ts#L7)

Exchange a short-lived access token for a long-lived token. Requires META_APP_ID and META_APP_SECRET to be configured.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "short_lived_token": {
      "type": "string",
      "description": "Short-lived access token to exchange"
    }
  },
  "required": [
    "short_lived_token"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="generate_preview"></a>

## `generate_preview`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/creatives.ts#L145)

Generate an ad preview without needing an existing ad. Provide creative spec directly to see how it would look.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_format": {
      "type": "string",
      "description": "Ad format: DESKTOP_FEED_STANDARD, MOBILE_FEED_STANDARD, INSTAGRAM_STANDARD, INSTAGRAM_STORY, RIGHT_COLUMN_STANDARD, etc."
    },
    "creative": {
      "type": "string",
      "description": "JSON string of creative spec: {object_story_spec: {...}} or {object_story_id: '...'}"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to generate the preview in (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "ad_format",
    "creative"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_account_activities"></a>

## `get_account_activities`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/account.ts#L74)

Get activity log for the ad account. Shows changes made to campaigns, ad sets, ads, etc.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_account_insights"></a>

## `get_account_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/insights.ts#L21)

Get performance insights for the ad account. Returns metrics like impressions, clicks, spend, reach, etc.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "default": "impressions,clicks,spend,reach,frequency,cpc,cpm,ctr,actions,cost_per_action_type",
      "description": "Comma-separated insight fields"
    },
    "breakdowns": {
      "type": "string",
      "description": "Breakdown dimensions: age,gender,country,region,publisher_platform,platform_position,device_platform,comscore_market (replaces dma). Some accounts must opt in in Ads Manager for impression_device, hourly_stats_aggregated_by_audience_time_zone, and frequency_value; empty results do not necessarily mean zero performance."
    },
    "date_preset": {
      "type": "string",
      "description": "Lowercase date preset, for example: today, yesterday, last_7d, last_14d, last_30d, this_month, last_month, this_quarter, last_quarter, this_year, last_year"
    },
    "time_range": {
      "type": "string",
      "description": "JSON string {since,until} in YYYY-MM-DD format"
    },
    "time_increment": {
      "type": "string",
      "description": "Time granularity: all_days, 1, 7, monthly"
    },
    "filtering": {
      "type": "string",
      "description": "JSON string for filtering"
    },
    "level": {
      "type": "string",
      "description": "Aggregation level: campaign, adset, ad"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad"></a>

## `get_ad`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L37)

Get details of a specific ad by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Ad ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "ad_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_account"></a>

## `get_ad_account`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/account.ts#L7)

Get details of the configured ad account including status, balance, currency, timezone, and spend info.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "default": "id,name,account_status,balance,currency,timezone_name,amount_spent,business_name,business_city,business_country_code,owner,min_campaign_group_spend_cap",
      "description": "Comma-separated fields to return"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_insights"></a>

## `get_ad_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/insights.ts#L75)

Get performance insights for a specific ad.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Ad ID"
    },
    "fields": {
      "type": "string",
      "default": "impressions,clicks,spend,reach,frequency,cpc,cpm,ctr,actions,cost_per_action_type",
      "description": "Comma-separated insight fields"
    },
    "breakdowns": {
      "type": "string",
      "description": "Breakdown dimensions: age,gender,country,region,publisher_platform,platform_position,device_platform,comscore_market (replaces dma). Some accounts must opt in in Ads Manager for impression_device, hourly_stats_aggregated_by_audience_time_zone, and frequency_value; empty results do not necessarily mean zero performance."
    },
    "date_preset": {
      "type": "string",
      "description": "Lowercase date preset, for example: today, yesterday, last_7d, last_14d, last_30d, this_month, last_month, this_quarter, last_quarter, this_year, last_year"
    },
    "time_range": {
      "type": "string",
      "description": "JSON string {since,until} in YYYY-MM-DD format"
    },
    "time_increment": {
      "type": "string",
      "description": "Time granularity: all_days, 1, 7, monthly"
    },
    "filtering": {
      "type": "string",
      "description": "JSON string for filtering"
    },
    "level": {
      "type": "string",
      "description": "Aggregation level: campaign, adset, ad"
    }
  },
  "required": [
    "ad_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_preview"></a>

## `get_ad_preview`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L148)

Get a preview of an ad in a specific format. Returns HTML iframe for rendering.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Ad ID"
    },
    "ad_format": {
      "type": "string",
      "description": "Ad format: DESKTOP_FEED_STANDARD, MOBILE_FEED_STANDARD, INSTAGRAM_STANDARD, INSTAGRAM_STORY, RIGHT_COLUMN_STANDARD, etc."
    }
  },
  "required": [
    "ad_id",
    "ad_format"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_adset"></a>

## `get_adset`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L35)

Get details of a specific ad set by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad set ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_adset_ads"></a>

## `get_adset_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L192)

Get all ads belonging to a specific ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad set ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_adset_insights"></a>

## `get_adset_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/insights.ts#L57)

Get performance insights for a specific ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad Set ID"
    },
    "fields": {
      "type": "string",
      "default": "impressions,clicks,spend,reach,frequency,cpc,cpm,ctr,actions,cost_per_action_type",
      "description": "Comma-separated insight fields"
    },
    "breakdowns": {
      "type": "string",
      "description": "Breakdown dimensions: age,gender,country,region,publisher_platform,platform_position,device_platform,comscore_market (replaces dma). Some accounts must opt in in Ads Manager for impression_device, hourly_stats_aggregated_by_audience_time_zone, and frequency_value; empty results do not necessarily mean zero performance."
    },
    "date_preset": {
      "type": "string",
      "description": "Lowercase date preset, for example: today, yesterday, last_7d, last_14d, last_30d, this_month, last_month, this_quarter, last_quarter, this_year, last_year"
    },
    "time_range": {
      "type": "string",
      "description": "JSON string {since,until} in YYYY-MM-DD format"
    },
    "time_increment": {
      "type": "string",
      "description": "Time granularity: all_days, 1, 7, monthly"
    },
    "filtering": {
      "type": "string",
      "description": "JSON string for filtering"
    },
    "level": {
      "type": "string",
      "description": "Aggregation level: campaign, adset, ad"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_adset_leads"></a>

## `get_adset_leads`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L216)

Get leads generated by a specific ad set. Requires leads_retrieval permission.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad set ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_adset_targeting_sentence"></a>

## `get_adset_targeting_sentence`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L175)

Get human-readable targeting description for an ad set. Converts targeting spec into readable sentences.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad set ID"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_async_report"></a>

## `get_async_report`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/insights.ts#L114)

Check status and retrieve results of an async insight report.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "report_run_id": {
      "type": "string",
      "description": "Report run ID from create_async_report"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated insight fields to return once the job completes"
    },
    "include_results": {
      "type": "boolean",
      "default": true,
      "description": "Fetch /{report_run_id}/insights when the job is complete"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 100,
      "description": "Maximum result rows per page"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for the result page"
    }
  },
  "required": [
    "report_run_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_audience"></a>

## `get_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L31)

Get details of a specific custom audience by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "Audience ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "audience_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_audience_health"></a>

## `get_audience_health`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L190)

Get health status and delivery readiness of a custom audience. Shows match rate, size, and operation status.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "Custom audience ID"
    }
  },
  "required": [
    "audience_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_batch_status"></a>

## `get_batch_status`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L244)

Check the status of a catalog batch operation.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "handle": {
      "type": "string",
      "description": "Batch handle returned from batch_products"
    }
  },
  "required": [
    "catalog_id",
    "handle"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_business"></a>

## `get_business`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L30)

Get details of a specific business by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "business_id": {
      "type": "string",
      "description": "Business ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "business_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign"></a>

## `get_campaign`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L37)

Get details of a specific campaign by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Campaign ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign_ads"></a>

## `get_campaign_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L202)

Get all ads belonging to a specific campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Campaign ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign_adsets"></a>

## `get_campaign_adsets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L178)

Get all ad sets belonging to a specific campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Campaign ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign_insights"></a>

## `get_campaign_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/insights.ts#L39)

Get performance insights for a specific campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Campaign ID"
    },
    "fields": {
      "type": "string",
      "default": "impressions,clicks,spend,reach,frequency,cpc,cpm,ctr,actions,cost_per_action_type",
      "description": "Comma-separated insight fields"
    },
    "breakdowns": {
      "type": "string",
      "description": "Breakdown dimensions: age,gender,country,region,publisher_platform,platform_position,device_platform,comscore_market (replaces dma). Some accounts must opt in in Ads Manager for impression_device, hourly_stats_aggregated_by_audience_time_zone, and frequency_value; empty results do not necessarily mean zero performance."
    },
    "date_preset": {
      "type": "string",
      "description": "Lowercase date preset, for example: today, yesterday, last_7d, last_14d, last_30d, this_month, last_month, this_quarter, last_quarter, this_year, last_year"
    },
    "time_range": {
      "type": "string",
      "description": "JSON string {since,until} in YYYY-MM-DD format"
    },
    "time_increment": {
      "type": "string",
      "description": "Time granularity: all_days, 1, 7, monthly"
    },
    "filtering": {
      "type": "string",
      "description": "JSON string for filtering"
    },
    "level": {
      "type": "string",
      "description": "Aggregation level: campaign, adset, ad"
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign_leads"></a>

## `get_campaign_leads`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L226)

Get leads generated by a specific campaign. Requires leads_retrieval permission.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Campaign ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_canvas"></a>

## `get_canvas`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/canvas.ts#L31)

Get details of a specific Instant Experience (Canvas) by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "canvas_id": {
      "type": "string",
      "description": "Canvas ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "canvas_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_catalog"></a>

## `get_catalog`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L27)

Get details of a specific product catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "catalog_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_creative"></a>

## `get_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/creatives.ts#L46)

Get details of a specific ad creative by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "creative_id": {
      "type": "string",
      "description": "Creative ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "creative_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_delivery_estimate"></a>

## `get_delivery_estimate`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L166)

Get delivery estimate for an ad set, including estimated daily reach. Note: the delivery_estimate edge exists on the ad set (and ad account) node, not on individual ads. Also note: as of v26.0, the daily_outcomes_curve, budget_guardrail, and estimate_dau fields are no longer returned (removed with no replacement).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad Set ID"
    },
    "optimization_goal": {
      "type": "string",
      "description": "Optimization goal to estimate for"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_experiment"></a>

## `get_experiment`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/experiments.ts#L50)

Get details of a specific experiment (ad study).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "experiment_id": {
      "type": "string",
      "description": "Experiment (ad study) ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "experiment_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_experiment_results"></a>

## `get_experiment_results`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/experiments.ts#L87)

Get results/cells of an experiment (ad study).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "experiment_id": {
      "type": "string",
      "description": "Experiment (ad study) ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "experiment_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_feed_uploads"></a>

## `get_feed_uploads`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/feeds.ts#L65)

Get upload history for a product feed.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "feed_id": {
      "type": "string",
      "description": "Product feed ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "feed_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_form_leads"></a>

## `get_form_leads`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/leads.ts#L7)

Get leads submitted through a lead generation form.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "form_id": {
      "type": "string",
      "description": "Lead form ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "form_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_image"></a>

## `get_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/images.ts#L65)

Get details of a specific ad image by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "image_id": {
      "type": "string",
      "description": "Image ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "image_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_lead"></a>

## `get_lead`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/leads.ts#L27)

Get details of a specific lead by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "lead_id": {
      "type": "string",
      "description": "Lead ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "lead_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_lead_form"></a>

## `get_lead_form`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/leads.ts#L94)

Get details of a specific lead generation form.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "form_id": {
      "type": "string",
      "description": "Lead form ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "form_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_product"></a>

## `get_product`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L179)

Get details of a specific product.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_id": {
      "type": "string",
      "description": "Product ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "product_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_product_set"></a>

## `get_product_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L121)

Get details of a specific product set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "set_id": {
      "type": "string",
      "description": "Product set ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "set_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_reach_estimate"></a>

## `get_reach_estimate`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/targeting.ts#L70)

Get estimated audience reach for a given targeting specification. Useful for planning campaigns before creating them.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "targeting_spec": {
      "type": "string",
      "description": "JSON string of targeting spec (same format as ad set targeting)"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "targeting_spec"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_rf_prediction"></a>

## `get_rf_prediction`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/reach_frequency.ts#L62)

Get details of a specific reach & frequency prediction by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "prediction_id": {
      "type": "string",
      "description": "Prediction ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "prediction_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_rule"></a>

## `get_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/rules.ts#L27)

Get details of a specific automated rule.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "rule_id": {
      "type": "string",
      "description": "Rule ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "rule_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_saved_audience"></a>

## `get_saved_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L233)

Get details of a specific saved audience by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "Saved audience ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "audience_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_targeting_suggestions"></a>

## `get_targeting_suggestions`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/targeting.ts#L88)

Get targeting suggestions based on existing targeting criteria. Meta suggests related interests, behaviors, and demographics.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "targeting_list": {
      "type": "string",
      "description": "JSON string of current targeting criteria to get suggestions for"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "targeting_list"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_video"></a>

## `get_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/videos.ts#L69)

Get details of a specific ad video by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "video_id": {
      "type": "string",
      "description": "Video ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    }
  },
  "required": [
    "video_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_account_users"></a>

## `list_account_users`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/account.ts#L98)

List users who have access to the ad account with their roles and permissions.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_ad_accounts"></a>

## `list_ad_accounts`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/account.ts#L27)

List all ad accounts accessible by the current user. Returns paginated results.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_ads"></a>

## `list_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L7)

List ads in the ad account. Optionally filter by campaign, ad set, or status.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Filter by campaign ID"
    },
    "adset_id": {
      "type": "string",
      "description": "Filter by ad set ID"
    },
    "status": {
      "type": "string",
      "description": "Filter by status: ACTIVE, PAUSED, DELETED, ARCHIVED"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_adsets"></a>

## `list_adsets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L7)

List ad sets in the ad account. Optionally filter by campaign or status.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Filter by campaign ID"
    },
    "status": {
      "type": "string",
      "description": "Filter by status: ACTIVE, PAUSED, DELETED, ARCHIVED"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_block_lists"></a>

## `list_block_lists`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/brand_safety.ts#L7)

List publisher block lists for the ad account. Returns paginated results.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_budget_schedules"></a>

## `list_budget_schedules`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/budget.ts#L8)

List budget schedules attached to a campaign or ad set. Returns paginated results.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "parent_id": {
      "type": "string",
      "minLength": 1,
      "description": "Campaign or ad set ID that owns the budget schedules"
    },
    "parent_type": {
      "type": "string",
      "enum": [
        "campaign",
        "adset"
      ],
      "default": "campaign",
      "description": "Type of parent object"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "parent_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_business_ad_accounts"></a>

## `list_business_ad_accounts`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L50)

List ad accounts owned by the configured business. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_business_instagram_accounts"></a>

## `list_business_instagram_accounts`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L185)

List Instagram accounts owned by the configured business. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_business_pages"></a>

## `list_business_pages`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L156)

List Facebook Pages owned by the configured business. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_business_users"></a>

## `list_business_users`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L79)

List users of the configured business. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_businesses"></a>

## `list_businesses`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L7)

List all businesses accessible by the current user. Returns paginated results.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_campaigns"></a>

## `list_campaigns`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L7)

List campaigns in the ad account. Supports filtering by status and objective. Returns paginated results.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Filter by status: ACTIVE, PAUSED, DELETED, ARCHIVED"
    },
    "objective": {
      "type": "string",
      "description": "Filter by objective: OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "before": {
      "type": "string",
      "description": "Pagination cursor for previous page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_canvases"></a>

## `list_canvases`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/canvas.ts#L7)

List Instant Experience (Canvas) creatives in the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_catalogs"></a>

## `list_catalogs`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L7)

List product catalogs for the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_creatives"></a>

## `list_creatives`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/creatives.ts#L22)

List ad creatives in the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_custom_audiences"></a>

## `list_custom_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L7)

List custom audiences in the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_experiments"></a>

## `list_experiments`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/experiments.ts#L7)

List A/B test experiments (ad studies) for the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_feeds"></a>

## `list_feeds`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/feeds.ts#L7)

List product feeds for a catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "catalog_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_images"></a>

## `list_images`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/images.ts#L9)

List ad images uploaded to the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_lead_forms"></a>

## `list_lead_forms`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/leads.ts#L45)

List lead generation forms for a Facebook Page.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "page_id": {
      "type": "string",
      "description": "Facebook Page ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "page_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_offline_event_sets"></a>

## `list_offline_event_sets`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/conversions.ts#L47)

List offline conversion data sets for the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_product_sets"></a>

## `list_product_sets`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L82)

List product sets within a catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "required": [
    "catalog_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_products"></a>

## `list_products`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L158)

List products within a catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "filter": {
      "type": "string",
      "description": "JSON string of filter rules"
    }
  },
  "required": [
    "catalog_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_rf_predictions"></a>

## `list_rf_predictions`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/reach_frequency.ts#L7)

List reach & frequency predictions for the ad account. Returns paginated results.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_rules"></a>

## `list_rules`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/rules.ts#L7)

List automated rules for the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results to return"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_saved_audiences"></a>

## `list_saved_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L209)

List saved audiences in the ad account. Saved audiences are reusable targeting presets.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_system_users"></a>

## `list_system_users`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L214)

List system users of the configured business. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_videos"></a>

## `list_videos`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/videos.ts#L9)

List ad videos uploaded to the ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="refresh_token"></a>

## `refresh_token`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/auth.ts#L24)

Extend a valid long-lived user access token through Meta's documented token exchange flow. Requires META_APP_ID and META_APP_SECRET.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "long_lived_token": {
      "type": "string",
      "description": "Long-lived access token to refresh"
    }
  },
  "required": [
    "long_lived_token"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="remove_business_user"></a>

## `remove_business_user`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/business.ts#L133)

Remove a user from the configured business. Requires META_BUSINESS_ID env var.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "user_id": {
      "type": "string",
      "description": "User ID to remove from the business"
    }
  },
  "required": [
    "user_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="remove_from_block_list"></a>

## `remove_from_block_list`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/brand_safety.ts#L69)

Remove publisher URLs from an existing block list.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "list_id": {
      "type": "string",
      "description": "Block list ID"
    },
    "urls": {
      "type": "string",
      "description": "JSON array of URLs to remove (e.g. '[\"example.com\"]')"
    }
  },
  "required": [
    "list_id",
    "urls"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="remove_users_from_audience"></a>

## `remove_users_from_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L146)

Remove users from a custom audience. Payload format is the same as add_users_to_audience.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "Audience ID"
    },
    "payload": {
      "type": "string",
      "description": "JSON string: {schema: ['EMAIL','PHONE',...], data: [['hash1','hash2',...], ...]}. All PII must be SHA-256 hashed."
    }
  },
  "required": [
    "audience_id",
    "payload"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="search_ad_library"></a>

## `search_ad_library`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ad_library.ts#L7)

Search the Meta Ad Library for ads. Allows searching by keywords, countries, and ad type. Useful for competitive research and transparency.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "search_terms": {
      "type": "string",
      "description": "Keywords to search for in ads"
    },
    "ad_reached_countries": {
      "type": "string",
      "description": "Comma-separated country codes where ads were shown (e.g. 'US,GB,KR')"
    },
    "ad_type": {
      "type": "string",
      "description": "Ad type filter: ALL, POLITICAL_AND_ISSUE_ADS, HOUSING_ADS, etc."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated fields to return"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "after": {
      "type": "string",
      "description": "Pagination cursor for next page"
    },
    "order_by": {
      "type": "string",
      "description": "Sort order for results"
    }
  },
  "required": [
    "search_terms",
    "ad_reached_countries"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="search_locations"></a>

## `search_locations`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/targeting.ts#L30)

Search for geographic locations (countries, regions, cities, zip codes) for ad targeting.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "Search query (e.g. 'New York', 'California', 'United States')"
    },
    "location_types": {
      "type": "string",
      "description": "Comma-separated location types: country, region, city, zip, geo_market, electoral_district"
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    }
  },
  "required": [
    "q"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="search_targeting"></a>

## `search_targeting`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/targeting.ts#L7)

Search for targeting options (interests, behaviors, demographics, etc.) by keyword. Use this to find valid targeting IDs for ad set targeting specs.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "Search query (e.g. 'fitness', 'technology', 'cooking')"
    },
    "type": {
      "type": "string",
      "description": "Targeting type filter: adinterest, adgeolocation, adeducationschool, adeducationmajor, adworkemployer, adworkposition, adlocale, etc."
    },
    "limit": {
      "type": "number",
      "default": 25,
      "description": "Number of results (default 25)"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "q"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="search_targeting_map"></a>

## `search_targeting_map`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/targeting.ts#L52)

Map targeting IDs to their full details (names, types, paths). Useful for resolving IDs obtained from other endpoints.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "targeting_list": {
      "type": "string",
      "description": "JSON array of targeting IDs to look up"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to query (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "required": [
    "targeting_list"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="send_conversion_event"></a>

## `send_conversion_event`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/conversions.ts#L8)

Send a server-side conversion event via the Conversions API (pixel).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "events": {
      "type": "string",
      "description": "JSON array of events: [{event_name, event_time, user_data, custom_data, action_source}]"
    },
    "test_event_code": {
      "type": "string",
      "description": "Events Manager test code; use to verify delivery as test events"
    }
  },
  "required": [
    "events"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="send_offline_event"></a>

## `send_offline_event`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/conversions.ts#L27)

Send offline conversion events through the Conversions API to a dataset. Store events must use action_source=physical_store.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "event_set_id": {
      "type": "string",
      "description": "Dataset ID for offline events (legacy parameter name retained)"
    },
    "events": {
      "type": "string",
      "description": "JSON array of offline events"
    },
    "test_event_code": {
      "type": "string",
      "description": "Events Manager test code; use to verify delivery as test events"
    }
  },
  "required": [
    "event_set_id",
    "events"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_ad"></a>

## `update_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/ads.ts#L81)

Update an existing ad. Only provided fields will be modified.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "Ad ID to update"
    },
    "name": {
      "type": "string",
      "description": "New ad name"
    },
    "status": {
      "type": "string",
      "description": "New status: ACTIVE, PAUSED, DELETED, ARCHIVED"
    },
    "creative": {
      "type": "string",
      "description": "New creative spec as JSON string"
    },
    "tracking_specs": {
      "type": "string",
      "description": "New tracking specs as JSON string"
    }
  },
  "required": [
    "ad_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_ad_account"></a>

## `update_ad_account`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/account.ts#L50)

Update the configured ad account settings. Only provided fields will be modified.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "New account name"
    },
    "timezone_name": {
      "type": "string",
      "description": "New timezone (e.g. 'America/New_York')"
    },
    "spend_cap": {
      "type": "string",
      "description": "Account spend cap in currency cents (e.g. '100000' = $1000.00)"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to update (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_adset"></a>

## `update_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/adsets.ts#L98)

Update an existing ad set. Only provided fields will be modified.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "Ad set ID to update"
    },
    "name": {
      "type": "string",
      "description": "New ad set name"
    },
    "status": {
      "type": "string",
      "description": "New status: ACTIVE, PAUSED, DELETED, ARCHIVED"
    },
    "daily_budget": {
      "type": "string",
      "description": "New daily budget in currency cents"
    },
    "lifetime_budget": {
      "type": "string",
      "description": "New lifetime budget in currency cents"
    },
    "targeting": {
      "type": "string",
      "description": "New targeting spec as JSON string. Advantage+ Audience automation flags go inside this object, e.g. targeting_automation: {\"advantage_audience\":1} — required for HEC-F (Housing/Employment/Financial Products and Services) ad sets with relaxable, non-broad targeting as of v26.0. Note: the Instagram Explore Feed placement was removed in Marketing API v26.0 — requests that explicitly include it now return an error."
    },
    "start_time": {
      "type": "string",
      "description": "New start time (ISO 8601)"
    },
    "end_time": {
      "type": "string",
      "description": "New end time (ISO 8601)"
    },
    "bid_amount": {
      "type": "string",
      "description": "New bid amount in currency cents"
    }
  },
  "required": [
    "adset_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_audience"></a>

## `update_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/audiences.ts#L89)

Update an existing custom audience. Only provided fields will be modified.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "Audience ID to update"
    },
    "name": {
      "type": "string",
      "description": "New audience name"
    },
    "description": {
      "type": "string",
      "description": "New audience description"
    }
  },
  "required": [
    "audience_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_budget_schedule"></a>

## `update_budget_schedule`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/budget.ts#L70)

Update an existing budget schedule. Only provided fields will be modified.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "schedule_id": {
      "type": "string",
      "description": "Budget schedule ID to update"
    },
    "budget_value": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "New unsigned value interpreted according to budget_value_type"
    },
    "budget_value_type": {
      "type": "string",
      "enum": [
        "ABSOLUTE",
        "MULTIPLIER"
      ],
      "description": "How budget_value is applied"
    },
    "time_start": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "New start time as a Unix timestamp"
    },
    "time_end": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "description": "New end time as a Unix timestamp"
    }
  },
  "required": [
    "schedule_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_campaign"></a>

## `update_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/campaigns.ts#L103)

Update an existing campaign. Only provided fields will be modified.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "Campaign ID to update"
    },
    "name": {
      "type": "string",
      "description": "New campaign name"
    },
    "status": {
      "type": "string",
      "description": "New status: ACTIVE, PAUSED, DELETED, ARCHIVED"
    },
    "daily_budget": {
      "type": "string",
      "description": "New daily budget in currency cents"
    },
    "lifetime_budget": {
      "type": "string",
      "description": "New lifetime budget in currency cents"
    },
    "start_time": {
      "type": "string",
      "description": "New start time (ISO 8601)"
    },
    "stop_time": {
      "type": "string",
      "description": "New stop time (ISO 8601)"
    },
    "bid_strategy": {
      "type": "string",
      "description": "New bid strategy: LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS"
    },
    "spend_cap": {
      "type": "string",
      "description": "Lifetime spend cap for the campaign, in account currency cents. Once set it cannot be removed, only raised or reset — pass '0' to reset/clear it."
    }
  },
  "required": [
    "campaign_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_catalog"></a>

## `update_catalog`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L64)

Update an existing product catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "catalog_id": {
      "type": "string",
      "description": "Product catalog ID"
    },
    "name": {
      "type": "string",
      "description": "New catalog name"
    }
  },
  "required": [
    "catalog_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_creative"></a>

## `update_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/creatives.ts#L100)

Update an existing ad creative. Only name and url_tags can be modified after creation.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "creative_id": {
      "type": "string",
      "description": "Creative ID to update"
    },
    "name": {
      "type": "string",
      "description": "New creative name"
    },
    "url_tags": {
      "type": "string",
      "description": "New URL tags"
    }
  },
  "required": [
    "creative_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_experiment"></a>

## `update_experiment`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/experiments.ts#L68)

Update an existing experiment (ad study).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "experiment_id": {
      "type": "string",
      "description": "Experiment (ad study) ID"
    },
    "name": {
      "type": "string",
      "description": "New experiment name"
    },
    "description": {
      "type": "string",
      "description": "New experiment description"
    }
  },
  "required": [
    "experiment_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_product"></a>

## `update_product`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L197)

Update an existing product in a catalog.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "product_id": {
      "type": "string",
      "description": "Product ID"
    },
    "name": {
      "type": "string",
      "description": "Product name"
    },
    "description": {
      "type": "string",
      "description": "Product description"
    },
    "price": {
      "type": "string",
      "description": "Product price (e.g. '9.99 USD')"
    },
    "url": {
      "type": "string",
      "description": "Product URL"
    },
    "image_url": {
      "type": "string",
      "description": "Product image URL"
    },
    "availability": {
      "type": "string",
      "description": "Product availability: in stock, out of stock, etc."
    }
  },
  "required": [
    "product_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_product_set"></a>

## `update_product_set`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/catalogs.ts#L139)

Update an existing product set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "set_id": {
      "type": "string",
      "description": "Product set ID"
    },
    "name": {
      "type": "string",
      "description": "New product set name"
    },
    "filter": {
      "type": "string",
      "description": "JSON string of updated filter rules"
    }
  },
  "required": [
    "set_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_rule"></a>

## `update_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/rules.ts#L66)

Update an existing automated rule.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "rule_id": {
      "type": "string",
      "description": "Rule ID"
    },
    "name": {
      "type": "string",
      "description": "New rule name"
    },
    "evaluation_spec": {
      "type": "string",
      "description": "JSON string defining updated rule conditions"
    },
    "execution_spec": {
      "type": "string",
      "description": "JSON string defining updated rule actions"
    },
    "schedule_spec": {
      "type": "string",
      "description": "JSON string defining updated rule schedule"
    },
    "status": {
      "type": "string",
      "description": "Rule status: ENABLED, DISABLED"
    }
  },
  "required": [
    "rule_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="upload_feed"></a>

## `upload_feed`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/feeds.ts#L47)

Upload/trigger a feed file upload for a product feed.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "feed_id": {
      "type": "string",
      "description": "Product feed ID"
    },
    "url": {
      "type": "string",
      "description": "URL of the feed file to upload"
    }
  },
  "required": [
    "feed_id",
    "url"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="upload_image"></a>

## `upload_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/images.ts#L33)

Upload an ad image from a public URL or a local file. Returns image hash for use in ad creatives. Note: fetching from a URL requires the app to have Meta's URL-fetch capability — if that fails with an OAuthException 'Application does not have the capability to make this API call', use file_path to upload the raw bytes instead, which does not require that capability.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "description": "Public URL of the image to upload"
    },
    "file_path": {
      "type": "string",
      "description": "Local filesystem path of the image to upload. Sent as base64-encoded bytes, bypassing Meta's URL-fetch capability requirement."
    },
    "name": {
      "type": "string",
      "description": "Name to assign to the uploaded image. Defaults to the file_path basename when uploading a local file."
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to upload into (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="upload_video"></a>

## `upload_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/mikusnuz/meta-ads-mcp/blob/e6bec2599e4394b355d553b38db41495aa24c910/src/tools/videos.ts#L33)

Upload an ad video from a public URL or a local file. Returns video ID for use in ad creatives.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "file_url": {
      "type": "string",
      "description": "Public URL of the video to upload"
    },
    "file_path": {
      "type": "string",
      "description": "Local filesystem path of the video to upload. Sent as multipart/form-data, bypassing the need for a publicly reachable URL."
    },
    "title": {
      "type": "string",
      "description": "Video title"
    },
    "description": {
      "type": "string",
      "description": "Video description"
    },
    "account_id": {
      "type": "string",
      "description": "Ad account ID to upload into (e.g. 'act_123' or '123'). Falls back to META_AD_ACCOUNT_ID env var if omitted."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

