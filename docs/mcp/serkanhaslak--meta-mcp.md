# serkanhaslak/meta-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/serkanhaslak/meta-mcp) · [Machine-readable snapshot](../../catalog/serkanhaslak--meta-mcp.json)

Complete registered tool snapshot. **77 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`66898db8ef4d`](https://github.com/serkanhaslak/meta-mcp/tree/66898db8ef4daf015dfeb5197950b52807263e22). Method: `runtime-tools-list`.

- JSON-encoded payload parameters remain strings. Prose defaults and options are not invented as schema constraints.

## Tools

- [add_audience_users](#add_audience_users)
- [batch_request](#batch_request)
- [copy_ad](#copy_ad)
- [copy_adset](#copy_adset)
- [copy_campaign](#copy_campaign)
- [create_ad](#create_ad)
- [create_ad_label](#create_ad_label)
- [create_ad_rule](#create_ad_rule)
- [create_adset](#create_adset)
- [create_async_report](#create_async_report)
- [create_budget_schedule](#create_budget_schedule)
- [create_campaign](#create_campaign)
- [create_creative](#create_creative)
- [create_custom_audience](#create_custom_audience)
- [create_custom_conversion](#create_custom_conversion)
- [create_lookalike_audience](#create_lookalike_audience)
- [create_saved_audience](#create_saved_audience)
- [delete_ad](#delete_ad)
- [delete_ad_label](#delete_ad_label)
- [delete_ad_rule](#delete_ad_rule)
- [delete_adset](#delete_adset)
- [delete_audience](#delete_audience)
- [delete_campaign](#delete_campaign)
- [delete_creative](#delete_creative)
- [delete_custom_conversion](#delete_custom_conversion)
- [delete_image](#delete_image)
- [delete_saved_audience](#delete_saved_audience)
- [generate_ad_preview](#generate_ad_preview)
- [get_account_activities](#get_account_activities)
- [get_account_info](#get_account_info)
- [get_account_insights](#get_account_insights)
- [get_account_pages](#get_account_pages)
- [get_ad](#get_ad)
- [get_ad_accounts](#get_ad_accounts)
- [get_ad_previews](#get_ad_previews)
- [get_ad_rule](#get_ad_rule)
- [get_adset](#get_adset)
- [get_budget_schedules](#get_budget_schedules)
- [get_campaign](#get_campaign)
- [get_creative](#get_creative)
- [get_custom_conversion](#get_custom_conversion)
- [get_delivery_estimate](#get_delivery_estimate)
- [get_insights](#get_insights)
- [get_lead_forms](#get_lead_forms)
- [get_leads](#get_leads)
- [get_pixel](#get_pixel)
- [get_reach_estimate](#get_reach_estimate)
- [get_targeting_sentence](#get_targeting_sentence)
- [get_targeting_suggestions](#get_targeting_suggestions)
- [get_video](#get_video)
- [get_video_thumbnails](#get_video_thumbnails)
- [list_ad_labels](#list_ad_labels)
- [list_ad_rules](#list_ad_rules)
- [list_ads](#list_ads)
- [list_adsets](#list_adsets)
- [list_campaigns](#list_campaigns)
- [list_creatives](#list_creatives)
- [list_custom_audiences](#list_custom_audiences)
- [list_custom_conversions](#list_custom_conversions)
- [list_images](#list_images)
- [list_pixels](#list_pixels)
- [list_saved_audiences](#list_saved_audiences)
- [list_videos](#list_videos)
- [remove_audience_users](#remove_audience_users)
- [search_behaviors](#search_behaviors)
- [search_demographics](#search_demographics)
- [search_geo_locations](#search_geo_locations)
- [search_interests](#search_interests)
- [send_conversion_event](#send_conversion_event)
- [update_ad](#update_ad)
- [update_ad_rule](#update_ad_rule)
- [update_adset](#update_adset)
- [update_campaign](#update_campaign)
- [update_creative](#update_creative)
- [upload_image](#upload_image)
- [upload_video](#upload_video)
- [validate_targeting](#validate_targeting)

<a id="add_audience_users"></a>

## `add_audience_users`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/audiences.ts#L98)

Add users to an existing custom audience by uploading hashed PII data. All personally identifiable information (emails, phone numbers, etc.) MUST be SHA256 hashed before sending. The payload defines the schema (types of data) and the corresponding data rows. Meta will match the hashed data against their user database to populate the audience.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "The ID of the custom audience to add users to. Get this from list_custom_audiences or create_custom_audience."
    },
    "payload": {
      "type": "string",
      "description": "JSON string containing the user data payload. Must include \"schema\" (array of PII types) and \"data\" (array of arrays with hashed values). All PII values must be lowercase and SHA256 hashed. Example: {\"schema\":[\"EMAIL\",\"PHONE\"],\"data\":[[\"a1b2c3...hash...\",\"d4e5f6...hash...\"],[\"g7h8i9...hash...\",\"j0k1l2...hash...\"]]}. Valid schema types: EMAIL, PHONE, FN (first name), LN (last name), GEN (gender), DOB (date of birth YYYYMMDD), CT (city), ST (state), ZIP, COUNTRY, MADID (mobile advertiser ID), EXTERN_ID (external ID)."
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

<a id="batch_request"></a>

## `batch_request`

Scope: **supporting** · Capability: **automation** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/batch.ts#L7)

Execute multiple Meta API calls in a single HTTP request using the Batch API. Supports up to 50 sub-requests per call. Each sub-request can be a GET, POST, or DELETE with its own endpoint and parameters. Responses are returned in the same order as requests. Use this to efficiently fetch data from multiple objects (e.g. get insights for 10 campaigns at once) or perform bulk operations (e.g. pause multiple ad sets).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "requests": {
      "type": "string",
      "description": "JSON string containing an array of sub-request objects. Each object must have: \"method\" (GET, POST, or DELETE), \"relative_url\" (API endpoint path with query params, e.g. \"123456/insights?fields=impressions,spend&date_preset=last_7d\"). Optional: \"body\" (URL-encoded form data for POST requests, e.g. \"status=PAUSED&name=Updated+Name\"). Maximum 50 sub-requests. Example: [{\"method\":\"GET\",\"relative_url\":\"act_123/campaigns?fields=id,name\"},{\"method\":\"GET\",\"relative_url\":\"act_123/adsets?fields=id,name\"}]"
    }
  },
  "required": [
    "requests"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="copy_ad"></a>

## `copy_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/copies.ts#L101)

Create a copy of an existing ad using the Meta Copies API. Optionally copy it into a different ad set by providing adset_id. The copy is created in PAUSED status by default to allow creative review before launching. Returns the ID of the newly created ad.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "The ID of the source ad to copy (e.g. \"123456789\"). The ad must exist and be accessible in your ad account."
    },
    "rename_options": {
      "type": "string",
      "description": "JSON string controlling how the copied ad is renamed. Keys: \"rename_strategy\" (DEEP_RENAME or NO_RENAME), \"rename_prefix\" (prepended to the name), \"rename_suffix\" (appended to the name). Example: {\"rename_strategy\":\"DEEP_RENAME\",\"rename_prefix\":\"V2 - \"}."
    },
    "status_option": {
      "type": "string",
      "description": "Status for the copied ad. Valid values: \"PAUSED\" (copy is created paused regardless of source status), \"INHERITED\" (copy inherits the source ad's status). Defaults to PAUSED if not specified."
    },
    "adset_id": {
      "type": "string",
      "description": "The ID of the target ad set to copy the ad into (e.g. \"123456789\"). If not provided, the ad is copied within the same ad set. Useful for testing the same creative across different audiences or moving winning ads to new ad sets."
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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/copies.ts#L51)

Create a copy of an existing ad set using the Meta Copies API. Optionally copy it into a different campaign by providing campaign_id. Set deep_copy to "true" to also duplicate all ads within the ad set. The copy is created in PAUSED status by default. Returns the ID of the newly created ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "The ID of the source ad set to copy (e.g. \"123456789\"). The ad set must exist and be accessible in your ad account."
    },
    "rename_options": {
      "type": "string",
      "description": "JSON string controlling how the copied ad set (and its ads if deep_copy) are renamed. Keys: \"rename_strategy\" (DEEP_RENAME to rename all levels, NO_RENAME to keep original names), \"rename_prefix\" (prepended to the name), \"rename_suffix\" (appended to the name). Example: {\"rename_strategy\":\"DEEP_RENAME\",\"rename_prefix\":\"Test - \"}."
    },
    "status_option": {
      "type": "string",
      "description": "Status for the copied ad set. Valid values: \"PAUSED\" (copy is created paused regardless of source status), \"INHERITED\" (copy inherits the source ad set's status). Defaults to PAUSED if not specified."
    },
    "campaign_id": {
      "type": "string",
      "description": "The ID of the target campaign to copy the ad set into (e.g. \"123456789\"). If not provided, the ad set is copied within the same campaign. Useful for reorganizing ad sets across campaigns or duplicating winning ad sets into new campaigns."
    },
    "deep_copy": {
      "type": "string",
      "description": "Whether to deep-copy the ad set including all its ads. Pass \"true\" to copy the ad set with all ads, \"false\" to copy only the ad set shell. Defaults to \"false\". Deep copy is useful for duplicating a complete ad set for audience testing."
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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/copies.ts#L8)

Create a copy of an existing campaign using the Meta Copies API. By default only the campaign shell is copied. Set deep_copy to "true" to also duplicate all ad sets and ads within the campaign. The copy is created in PAUSED status by default to allow review before launching. Returns the ID of the newly created campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "The ID of the source campaign to copy (e.g. \"123456789\"). The campaign must exist and be accessible in your ad account."
    },
    "rename_options": {
      "type": "string",
      "description": "JSON string controlling how the copied campaign (and its children if deep_copy) are renamed. Keys: \"rename_strategy\" (DEEP_RENAME to rename all levels, NO_RENAME to keep original names), \"rename_prefix\" (prepended to the name), \"rename_suffix\" (appended to the name). Example: {\"rename_strategy\":\"DEEP_RENAME\",\"rename_prefix\":\"Copy of \",\"rename_suffix\":\" - Q2\"}. Defaults to Meta's standard behavior (prepends \"Copy of\")."
    },
    "status_option": {
      "type": "string",
      "description": "Status for the copied campaign. Valid values: \"PAUSED\" (copy is created paused regardless of source status — recommended for review), \"INHERITED\" (copy inherits the source campaign's status). Defaults to PAUSED if not specified."
    },
    "deep_copy": {
      "type": "string",
      "description": "Whether to deep-copy the entire campaign structure including all ad sets and ads. Pass \"true\" to copy everything, \"false\" to copy only the campaign shell. Defaults to \"false\". Deep copy is useful for duplicating a full campaign for A/B testing or seasonal relaunches."
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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/ads.ts#L76)

Create a new ad within an ad set. An ad combines a creative (image/video/carousel) with an ad set (targeting and budget). The creative parameter accepts either a reference to an existing creative by ID or an inline creative spec as a JSON string.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (with or without \"act_\" prefix). Falls back to the default account if omitted."
    },
    "name": {
      "type": "string",
      "description": "Name of the ad."
    },
    "adset_id": {
      "type": "string",
      "description": "The ID of the ad set this ad belongs to."
    },
    "creative": {
      "type": "string",
      "description": "JSON string specifying the ad creative. Use {\"creative_id\":\"<id>\"} to reference an existing creative, or provide an inline spec like {\"title\":\"My Ad\",\"body\":\"Ad text\",\"image_hash\":\"abc123\",\"link_url\":\"https://example.com\",\"object_story_spec\":{...}}."
    },
    "status": {
      "type": "string",
      "description": "Initial status of the ad. Values: ACTIVE, PAUSED. Default is PAUSED if omitted."
    },
    "tracking_specs": {
      "type": "string",
      "description": "JSON string of tracking specs array. Defines conversion tracking for the ad. Example: '[{\"action.type\":[\"offsite_conversion\"],\"fb_pixel\":[\"123456789\"]}]'."
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

<a id="create_ad_label"></a>

## `create_ad_label`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/labels.ts#L36)

Create a new ad label in an ad account. Ad labels are reusable tags for organizing campaigns, ad sets, and ads. After creating a label, you can attach it to ad objects via their update endpoints. Use descriptive names that reflect your organizational scheme (e.g. "Holiday 2024", "A/B Test - Creative V2", "High Priority"). Returns the new label ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "Name of the ad label. Must be unique within the ad account. Use a descriptive, consistent naming convention (e.g. \"Campaign Type: Retargeting\", \"Region: EMEA\")."
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

<a id="create_ad_rule"></a>

## `create_ad_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/rules.ts#L36)

Create a new automated rule for an ad account. Rules automatically monitor your campaigns, ad sets, or ads and take actions when specified conditions are met — such as pausing under-performing ads, increasing budgets for high-performers, or sending notifications when spend thresholds are reached. The rule is defined by an evaluation spec (when and what to check), an execution spec (what action to take), and an optional schedule spec (how often to run).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "Name of the automated rule. Use a descriptive name for easy identification (e.g. \"Pause ads with CPA > $50\", \"Increase budget for ROAS > 3x\")."
    },
    "evaluation_spec": {
      "type": "string",
      "description": "JSON string defining when and what to evaluate. Must include \"evaluation_type\" (SCHEDULE for periodic checks, TRIGGER for event-based) and \"filters\" (array of condition objects). Each filter has \"field\" (metric name like \"spent\", \"cost_per_action_type\", \"impressions\"), \"value\" (threshold), \"operator\" (GREATER_THAN, LESS_THAN, EQUAL, NOT_EQUAL, IN_RANGE, NOT_IN_RANGE), and \"type\" (data type: \"int\", \"float\", \"string\"). For TRIGGER type, also include \"trigger\" with \"type\" (STATS_CHANGE for metric changes, METADATA_CREATION for new entity creation). Example: {\"evaluation_type\":\"SCHEDULE\",\"filters\":[{\"field\":\"spent\",\"value\":100,\"operator\":\"GREATER_THAN\",\"type\":\"int\"}]}"
    },
    "execution_spec": {
      "type": "string",
      "description": "JSON string defining what action to take when conditions are met. Must include \"execution_type\" (PAUSE, UNPAUSE, CHANGE_BUDGET, CHANGE_BID, ROTATE, NOTIFICATION) and optionally \"execution_options\" (array of action details). For budget/bid changes, each option has \"field\" (e.g. \"daily_budget\", \"lifetime_budget\", \"bid_amount\"), \"value\" (amount or percentage), and \"operator\" (SET, INCREASE_BY, DECREASE_BY, INCREASE_BY_PERCENTAGE, DECREASE_BY_PERCENTAGE). Example: {\"execution_type\":\"CHANGE_BUDGET\",\"execution_options\":[{\"field\":\"daily_budget\",\"value\":5000,\"operator\":\"INCREASE_BY_PERCENTAGE\"}]}"
    },
    "schedule_spec": {
      "type": "string",
      "description": "JSON string defining how often the rule runs. Includes \"schedule_type\" (DAILY, HOURLY, SEMI_HOURLY) and optionally \"schedule\" (array of time window objects with \"days\" as 0-6 for Sun-Sat, \"start_minute\" and \"end_minute\" as minutes from midnight 0-1439). Example: {\"schedule_type\":\"DAILY\",\"schedule\":[{\"days\":[0,1,2,3,4,5,6],\"start_minute\":0,\"end_minute\":1439}]} for every day all day."
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

<a id="create_adset"></a>

## `create_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/adsets.ts#L76)

Create a new ad set within a campaign. An ad set defines the audience targeting, budget, schedule, optimization goal, and billing event. The targeting parameter accepts a JSON string matching the Meta Targeting Spec (geo_locations, age_min, age_max, genders, interests, behaviors, custom_audiences, etc.).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (with or without \"act_\" prefix). Falls back to the default account if omitted."
    },
    "name": {
      "type": "string",
      "description": "Name of the ad set."
    },
    "campaign_id": {
      "type": "string",
      "description": "The ID of the parent campaign this ad set belongs to."
    },
    "targeting": {
      "type": "string",
      "description": "JSON string of the targeting spec object. Example: '{\"geo_locations\":{\"countries\":[\"US\"]},\"age_min\":18,\"age_max\":65,\"genders\":[1]}'."
    },
    "billing_event": {
      "type": "string",
      "description": "The event that triggers billing. Common values: IMPRESSIONS, LINK_CLICKS, POST_ENGAGEMENT, PAGE_LIKES, VIDEO_VIEWS, APP_INSTALLS, THRUPLAY."
    },
    "optimization_goal": {
      "type": "string",
      "description": "What the ad delivery is optimized for. Common values: REACH, IMPRESSIONS, LINK_CLICKS, LANDING_PAGE_VIEWS, POST_ENGAGEMENT, VIDEO_VIEWS, LEAD_GENERATION, CONVERSIONS, VALUE, APP_INSTALLS, OFFSITE_CONVERSIONS."
    },
    "bid_amount": {
      "type": "number",
      "description": "Bid amount in cents (integer) for the ad set. E.g. 500 = $5.00. Required for some bid strategies."
    },
    "daily_budget": {
      "type": "number",
      "description": "Daily budget in cents (integer). E.g. 2000 = $20.00. Either daily_budget or lifetime_budget is typically required."
    },
    "lifetime_budget": {
      "type": "number",
      "description": "Lifetime budget in cents (integer). E.g. 100000 = $1000.00. Either daily_budget or lifetime_budget is typically required."
    },
    "start_time": {
      "type": "string",
      "description": "Start time in ISO 8601 format, e.g. \"2025-06-01T00:00:00-0400\". Required if lifetime_budget is set."
    },
    "end_time": {
      "type": "string",
      "description": "End time in ISO 8601 format, e.g. \"2025-06-30T23:59:59-0400\". Required if lifetime_budget is set."
    },
    "status": {
      "type": "string",
      "description": "Initial status of the ad set. Values: ACTIVE, PAUSED. Default is PAUSED if omitted."
    },
    "promoted_object": {
      "type": "string",
      "description": "JSON string of the promoted object. Required for certain optimization goals. Example: '{\"page_id\":\"123456789\"}' or '{\"pixel_id\":\"123\",\"custom_event_type\":\"PURCHASE\"}'."
    }
  },
  "required": [
    "name",
    "campaign_id",
    "targeting",
    "billing_event",
    "optimization_goal"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_async_report"></a>

## `create_async_report`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/insights.ts#L153)

Create an asynchronous insights report for a campaign, ad set, ad, or account. Use this for large or complex queries that may time out with synchronous get_insights. Returns a report_run_id that you can poll using get_insights with the report run ID to check completion status and retrieve results. Async reports support an additional time_increment parameter for daily/weekly/monthly breakdowns.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "object_id": {
      "type": "string",
      "description": "The ID of the campaign, ad set, ad, or ad account (act_XXX) to generate the report for."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of metrics to include in the report. Defaults to impressions,clicks,spend,cpc,cpm,ctr,actions. See Meta Ads Insights API docs for the full list of available fields."
    },
    "time_range": {
      "type": "string",
      "description": "JSON string specifying a custom date range. Format: {\"since\":\"YYYY-MM-DD\",\"until\":\"YYYY-MM-DD\"}. Example: {\"since\":\"2024-01-01\",\"until\":\"2024-03-31\"}. Cannot be used together with date_preset."
    },
    "date_preset": {
      "type": "string",
      "description": "Predefined date range. Valid values: today, yesterday, this_month, last_month, this_quarter, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year. Cannot be used together with time_range."
    },
    "breakdowns": {
      "type": "string",
      "description": "Comma-separated list of breakdowns. Common values: age, gender, country, region, publisher_platform, platform_position, device_platform."
    },
    "level": {
      "type": "string",
      "description": "Aggregation level. Valid values: campaign, adset, ad. Determines the granularity of the returned rows."
    },
    "filtering": {
      "type": "string",
      "description": "JSON string of filters. Format: [{\"field\":\"<field>\",\"operator\":\"<op>\",\"value\":\"<val>\"}]."
    },
    "time_increment": {
      "type": "string",
      "description": "How to break down results over time. Use \"1\" for daily, \"7\" for weekly, \"monthly\" for monthly, or \"all_days\" for the entire period as a single row. This is especially useful for trend analysis over a date range."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of result rows to return per page (default 25, max 100)."
    }
  },
  "required": [
    "object_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_budget_schedule"></a>

## `create_budget_schedule`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/budget-schedules.ts#L34)

Create a budget schedule for a campaign or ad set. Budget schedules let you define time-bound budget overrides — for example, doubling your budget during a product launch weekend or setting a fixed high budget for a flash sale. You can define up to 50 schedule periods per campaign or ad set. The parent object must use a lifetime budget for ABSOLUTE schedules or a daily budget for MULTIPLIER schedules.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "object_id": {
      "type": "string",
      "description": "The campaign or ad set ID to attach the budget schedule to (e.g. \"123456789\"). The object must already exist and have an appropriate budget type set."
    },
    "budget_schedule_spec": {
      "type": "string",
      "description": "JSON string containing an array of schedule period objects. Each object defines a time window and budget override. Maximum 50 periods per object. Required fields per period: \"time_start\" (ISO 8601 datetime, e.g. \"2025-06-01T00:00:00+0000\"), \"time_end\" (ISO 8601 datetime, e.g. \"2025-06-07T23:59:59+0000\"), \"budget_value\" (string amount in account currency cents for ABSOLUTE, or multiplier like \"1.5\" for 50% increase), \"budget_value_type\" (\"ABSOLUTE\" for a fixed budget amount during the period, or \"MULTIPLIER\" for a relative increase over the base daily budget — e.g. \"2.0\" means 2x the normal daily budget). Example: [{\"time_start\":\"2025-06-01T00:00:00+0000\",\"time_end\":\"2025-06-07T23:59:59+0000\",\"budget_value\":\"10000\",\"budget_value_type\":\"ABSOLUTE\"}]"
    }
  },
  "required": [
    "object_id",
    "budget_schedule_spec"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_campaign"></a>

## `create_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/campaigns.ts#L77)

Create a new campaign in the specified ad account. Requires at minimum a name and objective. The campaign is created in PAUSED status by default so you can configure ad sets and ads before launching. Returns the new campaign ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "The name of the campaign."
    },
    "objective": {
      "type": "string",
      "description": "Campaign objective. Valid values: OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_TRAFFIC, OUTCOME_APP_PROMOTION."
    },
    "status": {
      "type": "string",
      "description": "Initial campaign status. Defaults to PAUSED. Valid values: ACTIVE, PAUSED."
    },
    "special_ad_categories": {
      "type": "string",
      "description": "JSON array of special ad categories. Required by Meta -- pass \"[]\" if none apply. Valid values: NONE, EMPLOYMENT, HOUSING, CREDIT, ISSUES_ELECTIONS_POLITICS. Example: [\"CREDIT\"]."
    },
    "daily_budget": {
      "type": "string",
      "description": "Daily budget in account currency cents (e.g. \"5000\" for $50.00 USD). Mutually exclusive with lifetime_budget."
    },
    "lifetime_budget": {
      "type": "string",
      "description": "Lifetime budget in account currency cents (e.g. \"100000\" for $1000.00 USD). Mutually exclusive with daily_budget. Requires stop_time on ad sets."
    },
    "bid_strategy": {
      "type": "string",
      "description": "Bid strategy for the campaign. Valid values: LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS."
    },
    "buying_type": {
      "type": "string",
      "description": "Buying type. Defaults to AUCTION. Valid values: AUCTION, RESERVED."
    },
    "is_campaign_budget_optimization": {
      "type": "string",
      "description": "Enable Advantage Campaign Budget (formerly CBO). Set to \"true\" to let Meta automatically distribute budget across ad sets. When enabled, budget is set at campaign level and Meta optimizes distribution."
    },
    "smart_promotion_type": {
      "type": "string",
      "description": "For Advantage+ campaigns. Valid values: GUIDED_CREATION. Enables Meta automation features for audience, placement, and creative optimization."
    },
    "special_ad_category_country": {
      "type": "string",
      "description": "JSON array of country codes for special ad category enforcement. Required when special_ad_categories includes EMPLOYMENT, HOUSING, or CREDIT. Example: [\"US\",\"CA\"]."
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

<a id="create_creative"></a>

## `create_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/creatives.ts#L63)

Create a new ad creative in the specified ad account. The creative defines the visual and textual content of an ad, including images, videos, text, links, and call-to-action buttons. After creation, associate the creative with an ad using the ads tools.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "A descriptive name for the creative. Used for internal identification in the Ads Manager."
    },
    "object_story_spec": {
      "type": "string",
      "description": "JSON string defining the creative content. Must include \"page_id\" and one of: \"link_data\" (for link/image ads with fields like link, message, name, description, image_hash, call_to_action), \"video_data\" (for video ads with video_id, title, message, thumbnail_url, call_to_action), or \"photo_data\" (for photo post ads with image_hash, caption). Example: {\"page_id\":\"123\",\"link_data\":{\"link\":\"https://example.com\",\"message\":\"Check this out\",\"image_hash\":\"abc123\",\"call_to_action\":{\"type\":\"LEARN_MORE\"}}}"
    },
    "asset_feed_spec": {
      "type": "string",
      "description": "JSON string for Dynamic Creative assets. Provide multiple text/image/video variations and Meta will automatically test combinations. Structure: {\"images\":[{\"hash\":\"...\"}],\"bodies\":[{\"text\":\"...\"}],\"titles\":[{\"text\":\"...\"}],\"descriptions\":[{\"text\":\"...\"}],\"call_to_action_types\":[\"LEARN_MORE\"]}. Only used with Dynamic Creative ad sets."
    },
    "url_tags": {
      "type": "string",
      "description": "URL query parameters appended to all links in the creative for tracking. Example: \"utm_source=facebook&utm_medium=cpc&utm_campaign=spring_sale\". Do not include the leading \"?\"."
    },
    "degrees_of_freedom_spec": {
      "type": "string",
      "description": "JSON string to enable Meta Generative AI creative features (text generation, image expansion, background generation). Example: {\"creative_features_spec\":{\"standard_enhancements\":{\"enroll_status\":\"OPT_IN\"}}} to enable all AI enhancements. Use \"OPT_OUT\" to disable specific features."
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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/audiences.ts#L43)

Create a new custom audience in an ad account. Custom audiences let you target ads to a specific set of people based on customer data, website activity, app activity, or engagement. After creation, you can populate the audience using add_audience_users or set up rules for automatic population.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "Name of the custom audience. Must be unique within the ad account. Use a descriptive name for easy identification (e.g. \"High-Value Purchasers Q1 2024\")."
    },
    "subtype": {
      "type": "string",
      "description": "Type of custom audience to create. Valid values: CUSTOM (uploaded customer list), WEBSITE (based on pixel events), APP (based on app events), OFFLINE (offline conversions), ENGAGEMENT (people who engaged with your content on Meta)."
    },
    "description": {
      "type": "string",
      "description": "Description of the audience for internal reference. Not shown to users."
    },
    "customer_file_source": {
      "type": "string",
      "description": "Source of customer data for CUSTOM subtype audiences. Valid values: USER_PROVIDED_ONLY (data collected directly from customers), PARTNER_PROVIDED_ONLY (data from partners), BOTH_USER_AND_PARTNER_PROVIDED (mix of both sources)."
    },
    "rule": {
      "type": "string",
      "description": "JSON string defining audience rules for WEBSITE or APP subtypes. Example for website visitors in last 30 days: {\"inclusions\":{\"operator\":\"or\",\"rules\":[{\"event_sources\":[{\"id\":\"<pixel_id>\",\"type\":\"pixel\"}],\"retention_seconds\":2592000,\"filter\":{\"operator\":\"and\",\"filters\":[{\"field\":\"url\",\"operator\":\"i_contains\",\"value\":\"\"}]}}]}}"
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

<a id="create_custom_conversion"></a>

## `create_custom_conversion`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/custom-conversions.ts#L36)

Create a new custom conversion for an ad account. Custom conversions define URL-based rules that refine when a standard pixel event counts as a conversion. For example, you can create a custom conversion that only fires a "Purchase" event when the page URL contains "/checkout/success". This lets you optimize ad delivery and track conversions for specific pages or funnels without adding extra pixel event code. The conversion is associated with a specific pixel and event type.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "Name of the custom conversion. Use a descriptive name that identifies the conversion action and page (e.g. \"Purchase - Thank You Page\", \"Lead - Contact Form Submitted\"). Must be unique within the ad account."
    },
    "pixel_id": {
      "type": "string",
      "description": "The Meta Pixel ID to base this custom conversion on. The pixel must be installed on the website where the conversion occurs. Use list_pixels to find available pixel IDs. Example: \"123456789012345\"."
    },
    "custom_event_type": {
      "type": "string",
      "description": "The standard pixel event type this custom conversion is based on. The custom conversion will only fire when this event type occurs AND the URL rule matches. Valid values: \"PURCHASE\", \"LEAD\", \"COMPLETE_REGISTRATION\", \"ADD_TO_CART\", \"INITIATED_CHECKOUT\", \"SEARCH\", \"VIEW_CONTENT\", \"CONTACT\", \"OTHER\". Use \"OTHER\" for custom events or general page views."
    },
    "rule": {
      "type": "string",
      "description": "JSON string defining the URL matching rule for this custom conversion. The rule determines which page URLs trigger the conversion. Common patterns: URL contains — {\"and\":[{\"url\":{\"i_contains\":\"thank-you\"}}]}, URL equals — {\"and\":[{\"url\":{\"eq\":\"https://example.com/success\"}}]}, URL regex — {\"and\":[{\"url\":{\"regex\":\"checkout\\/confirm\"}}]}, Multiple conditions — {\"and\":[{\"url\":{\"i_contains\":\"purchase\"}},{\"url\":{\"i_not_contains\":\"cancel\"}}]}. The \"i_contains\" operator is case-insensitive."
    },
    "default_conversion_value": {
      "type": "number",
      "description": "Default monetary value assigned to each conversion event. Used for ROAS (Return on Ad Spend) calculations when no dynamic value is passed with the pixel event. Example: 49.99 for a product that typically costs $49.99. Set to 0 or omit if conversions have varying values sent via the pixel."
    }
  },
  "required": [
    "name",
    "pixel_id",
    "custom_event_type",
    "rule"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_lookalike_audience"></a>

## `create_lookalike_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/audiences.ts#L150)

Create a lookalike audience based on an existing custom audience. Lookalike audiences find new people who share similar characteristics with your source audience. The ratio controls audience size vs. similarity — smaller ratios (e.g. 0.01 = top 1%) are more similar to your source, while larger ratios (e.g. 0.10 = top 10%) reach more people but with less similarity.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "Name for the lookalike audience. Use a descriptive name including the source and ratio (e.g. \"LAL - High-Value Customers - US 1%\")."
    },
    "origin_audience_id": {
      "type": "string",
      "description": "The ID of the source custom audience to base the lookalike on. The source audience should have at least 100 people from a single country for best results. Get this from list_custom_audiences."
    },
    "lookalike_spec": {
      "type": "string",
      "description": "JSON string defining the lookalike configuration. Must include \"country\" (ISO country code) and \"ratio\" (0.01 to 0.20, where 0.01 = top 1% most similar). Example: {\"country\":\"US\",\"ratio\":0.01} for top 1% in the US. For multi-country: {\"country\":\"US,GB\",\"ratio\":0.05}. You can also specify \"starting_ratio\" and \"ratio\" for a range (e.g. {\"country\":\"US\",\"starting_ratio\":0.03,\"ratio\":0.06} for 3-6% band)."
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

<a id="create_saved_audience"></a>

## `create_saved_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/saved-audiences.ts#L36)

Create a new saved audience in an ad account. Saved audiences store a reusable targeting specification — including demographics, interests, behaviors, and geo-targeting — so you can quickly apply the same targeting to multiple ad sets without re-entering it each time. The targeting parameter uses the same format as ad set targeting.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "name": {
      "type": "string",
      "description": "Name for the saved audience. Must be unique within the ad account. Use a descriptive name for easy identification (e.g. \"TR Males 25-44 Finance Interest\")."
    },
    "targeting": {
      "type": "string",
      "description": "JSON string of the targeting spec — same format used in ad set targeting. Must include at least geo_locations. Example: {\"geo_locations\":{\"countries\":[\"TR\"]},\"age_min\":25,\"age_max\":44,\"genders\":[1],\"interests\":[{\"id\":\"6003139266461\",\"name\":\"Finance\"}]}. Use search_interests, search_geo_locations, search_behaviors, and search_demographics tools to discover valid targeting values."
    },
    "description": {
      "type": "string",
      "description": "Description of the saved audience for internal reference. Useful for documenting the intent or campaign context for this targeting configuration."
    }
  },
  "required": [
    "name",
    "targeting"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_ad"></a>

## `delete_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/ads.ts#L171)

Delete an ad by its ID. This action is irreversible. Consider updating the status to ARCHIVED instead if you may need to reference it later.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "The ID of the ad to delete."
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

<a id="delete_ad_label"></a>

## `delete_ad_label`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/labels.ts#L60)

Permanently delete an ad label. This action cannot be undone. The label will be removed from all campaigns, ad sets, and ads it was attached to. Those ad objects will continue to function normally — only the label association is removed.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "label_id": {
      "type": "string",
      "description": "The ad label ID to delete (e.g. \"123456789\"). Get this from list_ad_labels. WARNING: This action is irreversible and will detach the label from all associated ad objects."
    }
  },
  "required": [
    "label_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_ad_rule"></a>

## `delete_ad_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/rules.ts#L182)

Permanently delete an automated rule. This action cannot be undone. The rule will immediately stop evaluating and executing. Any campaigns, ad sets, or ads that were being monitored by this rule will no longer be automatically managed — make sure you have alternative monitoring in place.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "rule_id": {
      "type": "string",
      "description": "The automated rule ID to delete (e.g. \"123456789\"). Get this from list_ad_rules. WARNING: This action is irreversible."
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

<a id="delete_adset"></a>

## `delete_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/adsets.ts#L259)

Delete an ad set by its ID. This action is irreversible. The ad set and all its ads will be deleted. Consider updating the status to ARCHIVED instead if you may need to reference it later.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "The ID of the ad set to delete."
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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/audiences.ts#L189)

Permanently delete a custom audience. This action cannot be undone. Any ad sets currently targeting this audience will stop delivering. Make sure to update or pause affected ad sets before deleting an audience.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "The ID of the custom audience to delete. Get this from list_custom_audiences. WARNING: This action is irreversible."
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

<a id="delete_campaign"></a>

## `delete_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/campaigns.ts#L231)

Delete a campaign by its ID. This sets the campaign status to DELETED. Deleted campaigns can still be viewed but cannot be reactivated. All ad sets and ads under the campaign will also stop delivering.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "The campaign ID to delete (e.g. \"123456789\")."
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

<a id="delete_creative"></a>

## `delete_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/creatives.ts#L152)

Delete an ad creative by its ID. This is a permanent action. The creative must not be actively used by any running ads. If the creative is in use, pause or delete the associated ads first.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "creative_id": {
      "type": "string",
      "description": "The ID of the ad creative to delete."
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

<a id="delete_custom_conversion"></a>

## `delete_custom_conversion`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/custom-conversions.ts#L120)

Permanently delete a custom conversion. This action cannot be undone. Any ad sets optimizing for this custom conversion will lose their optimization target, which may affect delivery. Any historical reporting data associated with this custom conversion will also become inaccessible. Make sure to update affected ad sets to use a different optimization event before deleting.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "custom_conversion_id": {
      "type": "string",
      "description": "The ID of the custom conversion to delete. Use list_custom_conversions to find the ID. WARNING: This action is irreversible and will affect any ad sets optimizing for this conversion."
    }
  },
  "required": [
    "custom_conversion_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_image"></a>

## `delete_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/images.ts#L93)

Delete an image from the ad account's image library by its hash. This is a permanent action. The image must not be actively used by any running ad creatives. If the image is in use, update or delete the associated creatives first.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "hash": {
      "type": "string",
      "description": "The hash of the image to delete. You can find image hashes using the list_images tool."
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

<a id="delete_saved_audience"></a>

## `delete_saved_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/saved-audiences.ts#L80)

Permanently delete a saved audience by its ID. This removes the reusable targeting spec from the ad account. Existing ad sets that were created using this saved audience are NOT affected — they retain their own copy of the targeting. This action cannot be undone.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "saved_audience_id": {
      "type": "string",
      "description": "The ID of the saved audience to delete. Get this from list_saved_audiences. WARNING: This action is irreversible."
    }
  },
  "required": [
    "saved_audience_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="generate_ad_preview"></a>

## `generate_ad_preview`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/previews.ts#L41)

Generate an ad preview from a creative specification without creating a persistent creative object. This is useful for previewing ad designs during the creative development process — you can iterate on the object_story_spec and see rendered output before committing to a final creative. Returns iframe-ready HTML showing how the ad would look in the specified placement.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "creative": {
      "type": "string",
      "description": "JSON string of the creative specification object. Must contain an \"object_story_spec\" with \"page_id\" and one of: \"link_data\" (for link/image ads), \"video_data\" (for video ads), or \"photo_data\" (for photo ads). Example: {\"object_story_spec\":{\"page_id\":\"123456\",\"link_data\":{\"link\":\"https://example.com\",\"message\":\"Check this out!\",\"image_hash\":\"abc123\",\"call_to_action\":{\"type\":\"LEARN_MORE\"}}}}"
    },
    "ad_format": {
      "type": "string",
      "enum": [
        "DESKTOP_FEED_STANDARD",
        "MOBILE_FEED_STANDARD",
        "INSTAGRAM_STANDARD",
        "INSTAGRAM_STORY",
        "INSTAGRAM_REELS",
        "RIGHT_COLUMN",
        "MARKETPLACE_MOBILE",
        "AUDIENCE_NETWORK_INSTREAM_VIDEO"
      ],
      "description": "The ad placement format to render the preview for. Each format simulates how the ad appears in that specific placement: DESKTOP_FEED_STANDARD (Facebook desktop News Feed), MOBILE_FEED_STANDARD (Facebook mobile News Feed), INSTAGRAM_STANDARD (Instagram feed post), INSTAGRAM_STORY (Instagram Stories full-screen), INSTAGRAM_REELS (Instagram Reels), RIGHT_COLUMN (Facebook right-hand column), MARKETPLACE_MOBILE (Facebook Marketplace on mobile), AUDIENCE_NETWORK_INSTREAM_VIDEO (in-stream video on Audience Network partner apps)."
    }
  },
  "required": [
    "creative",
    "ad_format"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_account_activities"></a>

## `get_account_activities`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/activities.ts#L9)

Retrieve the activity log (audit trail) for an ad account. Returns a chronological record of changes made to the account and its objects — campaigns, ad sets, ads, audiences, budgets, targeting, and more. Each activity entry includes who made the change, what was changed, and when. Use this to audit recent modifications, investigate unexpected performance shifts, track team member actions, or review changes before/after a specific date.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "since": {
      "type": "string",
      "description": "Unix timestamp (seconds since epoch) for the start of the time range. Only activities on or after this time are returned. Example: \"1700000000\" for Nov 14 2023. Use together with \"until\" to define a precise window."
    },
    "until": {
      "type": "string",
      "description": "Unix timestamp (seconds since epoch) for the end of the time range. Only activities on or before this time are returned. Example: \"1700086400\". Use together with \"since\" to define a precise window."
    },
    "uid": {
      "type": "string",
      "description": "Filter activities by the Facebook user ID of the actor who performed the action. Use this to see only changes made by a specific team member or API integration."
    },
    "category": {
      "type": "string",
      "enum": [
        "ACCOUNT",
        "AD",
        "AD_SET",
        "CAMPAIGN",
        "AUDIENCE",
        "BID",
        "BUDGET",
        "TARGETING"
      ],
      "description": "Filter activities by category to narrow down to a specific object type or action domain. ACCOUNT: account-level settings changes. AD: ad creation, edits, status changes. AD_SET: ad set configuration changes. CAMPAIGN: campaign-level changes. AUDIENCE: custom/lookalike audience modifications. BID: bid strategy and amount changes. BUDGET: budget amount and schedule changes. TARGETING: targeting specification changes."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return for each activity entry. Defaults to \"event_type,event_time,actor_name,actor_id,object_id,object_type,extra_data,translated_event_type\". Other available fields include date_time_in_timezone, application_name. See Meta API docs for all available Activity fields."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of activity entries to return per page (default 25, max 100). Use pagination cursors in the response to fetch additional pages."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_account_info"></a>

## `get_account_info`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/account.ts#L43)

Get detailed information about a specific ad account including its status, spending limits, currency, timezone, business info, and funding source. Useful for verifying account configuration before creating campaigns.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,account_id,account_status,age,currency,timezone_name,timezone_offset_hours_utc,business_name,business_city,business_country_code,spend_cap,amount_spent,balance,owner,funding_source_details,disable_reason,created_time. See Meta API docs for all available AdAccount fields."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_account_insights"></a>

## `get_account_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/insights.ts#L92)

Get aggregated performance insights for an entire ad account. Returns account-level metrics like total impressions, clicks, spend, CTR, CPC, and CPM across all campaigns. Supports the same breakdowns, date ranges, and filters as get_insights but scoped to the whole account. Use this for high-level reporting and account performance overview.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of metrics to return. Defaults to impressions,clicks,spend,cpc,cpm,ctr,actions. Common fields: impressions, clicks, spend, cpc, cpm, ctr, reach, frequency, actions, cost_per_action_type, conversions, cost_per_conversion. See Meta Ads Insights API docs for the full list."
    },
    "time_range": {
      "type": "string",
      "description": "JSON string specifying a custom date range. Format: {\"since\":\"YYYY-MM-DD\",\"until\":\"YYYY-MM-DD\"}. Example: {\"since\":\"2024-01-01\",\"until\":\"2024-01-31\"}. Cannot be used together with date_preset."
    },
    "date_preset": {
      "type": "string",
      "description": "Predefined date range instead of a custom time_range. Valid values: today, yesterday, this_month, last_month, this_quarter, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year. Cannot be used together with time_range."
    },
    "breakdowns": {
      "type": "string",
      "description": "Comma-separated list of breakdowns to segment results. Common values: age, gender, country, region, dma, impression_device, publisher_platform, platform_position, device_platform. Example: \"age,gender\" to see results broken down by age and gender."
    },
    "level": {
      "type": "string",
      "description": "Aggregation level for the results. Valid values: campaign, adset, ad. Use level=campaign to see per-campaign breakdown within the account."
    },
    "filtering": {
      "type": "string",
      "description": "JSON string of filters to apply to results. Format: [{\"field\":\"<field>\",\"operator\":\"<op>\",\"value\":\"<val>\"}]. Operators: EQUAL, NOT_EQUAL, GREATER_THAN, LESS_THAN, IN, NOT_IN, CONTAIN, NOT_CONTAIN."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of result rows to return per page (default 25, max 100)."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_account_pages"></a>

## `get_account_pages`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/account.ts#L69)

List Facebook Pages managed by the current user/token. Pages are required when creating ad creatives (for page-backed ads) or working with lead generation forms. Returns page IDs, names, access tokens, and categories.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,access_token,category,followers_count,fan_count. See Meta API docs for all available Page fields."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of pages to return per page (default 25, max 100)."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad"></a>

## `get_ad`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/ads.ts#L56)

Get detailed information about a single ad by its ID. Returns the full ad configuration including its creative reference, tracking specs, conversion specs, and delivery status.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "The ID of the ad to retrieve."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to: id,name,adset_id,campaign_id,status,effective_status,creative,tracking_specs,conversion_specs,created_time,updated_time,preview_shareable_link"
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

<a id="get_ad_accounts"></a>

## `get_ad_accounts`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/account.ts#L8)

List all ad accounts accessible by the current access token. Returns account IDs, names, statuses, and other metadata. Use this to discover which ad accounts you can manage before performing operations on a specific account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,account_id,account_status,currency,timezone_name,business_name. See Meta API docs for all available AdAccount fields."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of ad accounts to return per page (default 25, max 100)."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_previews"></a>

## `get_ad_previews`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/previews.ts#L8)

Get rendered HTML preview(s) of an existing ad creative. Returns an iframe-ready HTML snippet that shows how the creative looks in the specified ad format/placement. Use this to visually verify a creative before it goes live or to share previews with stakeholders for approval.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "creative_id": {
      "type": "string",
      "description": "The ID of the ad creative to preview. You can obtain this from list_creatives or get_creative."
    },
    "ad_format": {
      "type": "string",
      "enum": [
        "DESKTOP_FEED_STANDARD",
        "MOBILE_FEED_STANDARD",
        "INSTAGRAM_STANDARD",
        "INSTAGRAM_STORY",
        "INSTAGRAM_REELS",
        "RIGHT_COLUMN",
        "MARKETPLACE_MOBILE",
        "AUDIENCE_NETWORK_INSTREAM_VIDEO"
      ],
      "description": "The ad placement format to render the preview for. Each format simulates how the ad appears in that specific placement: DESKTOP_FEED_STANDARD (Facebook desktop News Feed), MOBILE_FEED_STANDARD (Facebook mobile News Feed), INSTAGRAM_STANDARD (Instagram feed post), INSTAGRAM_STORY (Instagram Stories full-screen), INSTAGRAM_REELS (Instagram Reels), RIGHT_COLUMN (Facebook right-hand column), MARKETPLACE_MOBILE (Facebook Marketplace on mobile), AUDIENCE_NETWORK_INSTREAM_VIDEO (in-stream video on Audience Network partner apps)."
    }
  },
  "required": [
    "creative_id",
    "ad_format"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_rule"></a>

## `get_ad_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/rules.ts#L95)

Get detailed information about a specific automated rule by its ID. Returns the full rule configuration including evaluation conditions, execution actions, schedule, and current status. Use this to inspect a rule before updating or to verify it was created correctly.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "rule_id": {
      "type": "string",
      "description": "The automated rule ID to retrieve (e.g. \"123456789\"). Get this from list_ad_rules."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,status,evaluation_spec,execution_spec,schedule_spec,created_time,updated_time. See Meta API docs for all available AdRule fields."
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

<a id="get_adset"></a>

## `get_adset`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/adsets.ts#L56)

Get detailed information about a single ad set by its ID. Returns the full ad set configuration including targeting spec, budget, schedule, optimization goal, and delivery status.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "The ID of the ad set to retrieve."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to: id,name,campaign_id,status,effective_status,daily_budget,lifetime_budget,budget_remaining,bid_amount,bid_strategy,billing_event,optimization_goal,targeting,promoted_object,start_time,end_time,created_time,updated_time"
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

<a id="get_budget_schedules"></a>

## `get_budget_schedules`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/budget-schedules.ts#L9)

Get budget schedules for a campaign or ad set. Budget schedules allow you to automatically increase or set specific budgets for defined time periods (e.g. boost spend during a flash sale weekend). Returns schedule IDs, budget values, time windows, recurrence settings, and statuses.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "object_id": {
      "type": "string",
      "description": "The campaign or ad set ID to retrieve budget schedules for (e.g. \"123456789\"). Budget schedules can be attached to either campaigns or ad sets."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to \"id,budget_value,budget_value_type,time_start,time_end,recurrence_type,status\". Available fields include: id, budget_value (the budget amount in account currency cents or multiplier value), budget_value_type (ABSOLUTE or MULTIPLIER), time_start (ISO 8601 start time), time_end (ISO 8601 end time), recurrence_type (NONE for one-time or WEEKLY for recurring), status (ACTIVE, PAUSED, etc.)."
    }
  },
  "required": [
    "object_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign"></a>

## `get_campaign`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/campaigns.ts#L55)

Get detailed information about a specific campaign by its ID. Returns the full campaign configuration including objective, status, budget, bid strategy, and special ad categories.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "The campaign ID to retrieve (e.g. \"123456789\")."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,objective,status,effective_status,daily_budget,lifetime_budget,budget_remaining,buying_type,bid_strategy,special_ad_categories,spend_cap,start_time,stop_time,created_time,updated_time. See Meta API docs for all available Campaign fields."
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

<a id="get_creative"></a>

## `get_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/creatives.ts#L41)

Get detailed information about a specific ad creative by its ID. Returns the full creative configuration including object story spec, image/video references, URL tags, and asset feed spec. Use this to inspect a creative before cloning or modifying it.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "creative_id": {
      "type": "string",
      "description": "The ID of the ad creative to retrieve."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to: id,name,status,object_story_spec,thumbnail_url,image_url,url_tags,asset_feed_spec,body,title,link_url,call_to_action_type. See Meta API docs for all available AdCreative fields."
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

<a id="get_custom_conversion"></a>

## `get_custom_conversion`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/custom-conversions.ts#L95)

Get detailed information about a specific custom conversion including its URL rule, associated pixel, event type, default value, and firing history. Use this to inspect a custom conversion configuration, verify its rule is matching correctly, or check when it last fired. The last_fired_time field is particularly useful for debugging whether the conversion is actively tracking.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "custom_conversion_id": {
      "type": "string",
      "description": "The ID of the custom conversion to retrieve. Use list_custom_conversions to find available IDs. Example: \"123456789012345\"."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,pixel,custom_event_type,rule,default_conversion_value,creation_time,last_fired_time,first_fired_time,is_archived,account_id,description,event_source_type. See Meta API docs for all available CustomConversion fields."
    }
  },
  "required": [
    "custom_conversion_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_delivery_estimate"></a>

## `get_delivery_estimate`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/account.ts#L109)

Get a delivery estimate for a given targeting specification and optimization goal. Returns estimated daily reach, impressions, and other delivery metrics. Use this to evaluate audience size and expected performance before creating ad sets.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "targeting_spec": {
      "type": "string",
      "description": "JSON string of the targeting specification object. Must include at least geo_locations. Example: {\"geo_locations\":{\"countries\":[\"US\"]},\"age_min\":25,\"age_max\":45,\"genders\":[1]}"
    },
    "optimization_goal": {
      "type": "string",
      "description": "The optimization goal for the delivery estimate. Common values: REACH, IMPRESSIONS, LINK_CLICKS, LANDING_PAGE_VIEWS, OFFSITE_CONVERSIONS, LEAD_GENERATION, APP_INSTALLS, VIDEO_VIEWS."
    }
  },
  "required": [
    "targeting_spec",
    "optimization_goal"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_insights"></a>

## `get_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/insights.ts#L33)

Get performance insights (metrics) for a specific campaign, ad set, or ad. Returns metrics like impressions, clicks, spend, CTR, CPC, CPM, and conversion actions. You can break down results by time, demographics, placement, and more. Use this for detailed performance analysis of individual ad objects.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "object_id": {
      "type": "string",
      "description": "The ID of the campaign, ad set, or ad to get insights for. You can get these IDs from list_campaigns, list_adsets, or list_ads."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of metrics to return. Defaults to impressions,clicks,spend,cpc,cpm,ctr,actions. Common fields: impressions, clicks, spend, cpc, cpm, ctr, reach, frequency, actions, cost_per_action_type, conversions, cost_per_conversion, video_p25_watched_actions, video_p50_watched_actions, video_p75_watched_actions, video_p100_watched_actions. See Meta Ads Insights API docs for the full list."
    },
    "time_range": {
      "type": "string",
      "description": "JSON string specifying a custom date range. Format: {\"since\":\"YYYY-MM-DD\",\"until\":\"YYYY-MM-DD\"}. Example: {\"since\":\"2024-01-01\",\"until\":\"2024-01-31\"}. Cannot be used together with date_preset."
    },
    "date_preset": {
      "type": "string",
      "description": "Predefined date range instead of a custom time_range. Valid values: today, yesterday, this_month, last_month, this_quarter, last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year. Cannot be used together with time_range."
    },
    "breakdowns": {
      "type": "string",
      "description": "Comma-separated list of breakdowns to segment results. Common values: age, gender, country, region, dma, impression_device, publisher_platform, platform_position, device_platform. Example: \"age,gender\" to see results broken down by age and gender. Some breakdowns cannot be combined — see Meta API docs for valid combinations."
    },
    "level": {
      "type": "string",
      "description": "Aggregation level for the results. Valid values: campaign, adset, ad. When querying a campaign, use level=adset to see per-adset breakdown, or level=ad for per-ad breakdown."
    },
    "filtering": {
      "type": "string",
      "description": "JSON string of filters to apply to results. Format: [{\"field\":\"<field>\",\"operator\":\"<op>\",\"value\":\"<val>\"}]. Operators: EQUAL, NOT_EQUAL, GREATER_THAN, LESS_THAN, IN, NOT_IN, CONTAIN, NOT_CONTAIN. Example: [{\"field\":\"action_type\",\"operator\":\"IN\",\"value\":[\"link_click\",\"post_engagement\"]}]"
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of result rows to return per page (default 25, max 100). Use pagination for large result sets."
    }
  },
  "required": [
    "object_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_lead_forms"></a>

## `get_lead_forms`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/leadgen.ts#L9)

List lead generation forms for a Facebook Page. Returns form IDs, names, statuses, creation times, and lead counts. Lead forms are used with Lead Generation campaign objectives to collect user information (name, email, phone, etc.) directly within Facebook/Instagram ads.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "page_id": {
      "type": "string",
      "description": "Facebook Page ID that owns the lead forms. Use get_account_pages to find your page IDs. Example: \"123456789\"."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,status,created_time,leads_count. Other available fields include: locale, page, qualifiers_enabled, question_page_custom_headline, questions, thank_you_page."
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

<a id="get_leads"></a>

## `get_leads`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/leadgen.ts#L34)

Retrieve leads collected from a specific lead generation form. Returns lead IDs, submission timestamps, and field data (name, email, phone, etc.) as submitted by users. Use this to export or process leads from your Lead Generation campaigns. Requires leads_retrieval permission on the Page access token.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "form_id": {
      "type": "string",
      "description": "Lead form ID to retrieve leads from. Use get_lead_forms to find form IDs. Example: \"987654321\"."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return per lead. Defaults to id,created_time,field_data. Other available fields include: ad_id, ad_name, adset_id, adset_name, campaign_id, campaign_name, form_id, platform, retailer_item_id."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of leads to return per page (default 25, max 100). Use pagination cursors in the response to retrieve additional pages."
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

<a id="get_pixel"></a>

## `get_pixel`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/pixel.ts#L34)

Get detailed information about a specific Meta Pixel (dataset) including its configuration, code snippet, owner, and firing status. Use this to inspect pixel setup, retrieve the pixel base code for installation, or check when events were last received.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "pixel_id": {
      "type": "string",
      "description": "Meta Pixel ID to retrieve details for. Use list_pixels to find pixel IDs. Example: \"123456789012345\"."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,code,creation_time,last_fired_time,owner_ad_account,owner_business,data_use_setting,is_unavailable,automatic_matching_fields. See Meta API docs for all available AdsPixel fields."
    }
  },
  "required": [
    "pixel_id"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_reach_estimate"></a>

## `get_reach_estimate`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/reach-estimate.ts#L8)

Get an estimated audience reach and daily outcomes for a given targeting specification. This is the same data shown in the "Audience Definition" gauge in Meta Ads Manager when setting up ad set targeting. Returns estimated daily reach, impressions, and the total addressable audience size. Use this to evaluate targeting options before creating ad sets — for example, to compare audience sizes across different interest combinations, check if a geo+demographic combination is too narrow, or estimate potential reach for budget planning. The targeting_spec format is identical to what you would use when creating an ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "targeting_spec": {
      "type": "string",
      "description": "JSON string of the targeting specification to estimate reach for. Uses the same format as ad set targeting. Example — target 25-45 year old women in Turkey interested in finance: {\"geo_locations\":{\"countries\":[\"TR\"]},\"age_min\":25,\"age_max\":45,\"genders\":[2],\"interests\":[{\"id\":\"6003139266461\",\"name\":\"Finance\"}]}. You can include any valid targeting fields: geo_locations (countries, regions, cities, zips), age_min/age_max (13-65, where 65 means 65+), genders (1=male, 2=female), interests, behaviors, custom_audiences, excluded_custom_audiences, publisher_platforms, device_platforms, flexible_spec (OR logic), exclusions. Use search_interests, search_behaviors, and search_geo_locations to find valid targeting IDs."
    },
    "optimize_for": {
      "type": "string",
      "description": "The optimization goal that affects the estimated outcomes. This changes which daily estimates are returned (e.g. estimated clicks vs. impressions). Valid values: \"NONE\" (no optimization, raw reach), \"IMPRESSIONS\" (maximize impressions), \"REACH\" (maximize unique reach), \"LINK_CLICKS\" (maximize clicks to destination), \"OFFSITE_CONVERSIONS\" (maximize conversions), \"LANDING_PAGE_VIEWS\" (maximize page views), \"POST_ENGAGEMENT\" (maximize post engagement), \"THRUPLAY\" (maximize video views), \"LEAD_GENERATION\" (maximize leads), \"APP_INSTALLS\" (maximize installs), \"VALUE\" (maximize purchase value). Defaults to NONE if not specified."
    },
    "currency": {
      "type": "string",
      "description": "Three-letter ISO 4217 currency code for cost estimates in the response. Examples: \"USD\", \"EUR\", \"GBP\", \"TRY\" (Turkish Lira), \"BRL\". If not specified, uses the ad account default currency."
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

<a id="get_targeting_sentence"></a>

## `get_targeting_sentence`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/targeting-utils.ts#L68)

Convert a targeting specification into a human-readable sentence. Returns a natural-language description of who the targeting will reach — for example, "People aged 25-45 in United States who like Finance and are interested in Investing". This is useful for reviewing targeting configurations at a glance, generating reports, or confirming that the targeting spec matches your intent before creating an ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "targeting_spec": {
      "type": "string",
      "description": "JSON string of the full targeting specification to describe. This should be the same format used in ad set targeting_spec. Example: {\"geo_locations\":{\"countries\":[\"US\",\"GB\"]},\"age_min\":18,\"age_max\":65,\"interests\":[{\"id\":\"6003139266461\",\"name\":\"Yoga\"}],\"behaviors\":[{\"id\":\"6002714895372\",\"name\":\"Frequent Travelers\"}]}. The API converts all targeting parameters (location, demographics, interests, behaviors, custom audiences, etc.) into readable sentence lines."
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

<a id="get_targeting_suggestions"></a>

## `get_targeting_suggestions`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/targeting-utils.ts#L8)

Get targeting suggestions based on a list of existing interest or behavior IDs. Returns similar and related targeting options that you can add to expand your audience. Useful for discovering new targeting ideas — for example, if you are targeting "Running" and "Marathon", this endpoint might suggest "Trail Running", "5K Races", or "Athletic Apparel". Use the returned IDs in ad set targeting_spec.interests or targeting_spec.behaviors.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "targeting_list": {
      "type": "string",
      "description": "JSON string containing an array of targeting objects to get suggestions for. Each object must have \"id\" (the interest or behavior ID) and \"type\" (either \"interests\" or \"behaviors\"). Example: [{\"id\":\"6003139266461\",\"type\":\"interests\"},{\"id\":\"6003020834693\",\"type\":\"interests\"}]. You can obtain these IDs from search_interests, search_behaviors, or from an existing ad set's targeting_spec."
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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/videos.ts#L115)

Get detailed information about a specific video by its ID. Returns the full video metadata including title, description, duration, source URL, encoding status, and available thumbnails. Use this to check video processing status or retrieve details before creating video ad creatives.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "video_id": {
      "type": "string",
      "description": "The ID of the video to retrieve."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,title,description,length,source,created_time,updated_time,status,thumbnails,permalink_url,embeddable,format. See Meta API docs for all available AdVideo fields."
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

<a id="get_video_thumbnails"></a>

## `get_video_thumbnails`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/videos.ts#L140)

Get available thumbnails for a specific video. Returns a list of thumbnail images at various sizes that can be used when creating video ad creatives. Each thumbnail includes its URI, width, height, and whether it is the preferred thumbnail.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "video_id": {
      "type": "string",
      "description": "The ID of the video to retrieve thumbnails for."
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

<a id="list_ad_labels"></a>

## `list_ad_labels`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/labels.ts#L9)

List all ad labels for an ad account. Ad labels are tags you can attach to campaigns, ad sets, and ads for organization and filtering. Use labels to group related objects (e.g. "Q1 Promo", "Brand Awareness", "Retargeting") and then filter by label in list endpoints. Returns label IDs, names, and timestamps.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,created_time,updated_time. See Meta API docs for all available AdLabel fields."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_ad_rules"></a>

## `list_ad_rules`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/rules.ts#L9)

List all automated rules for an ad account. Automated rules let you monitor campaigns, ad sets, and ads and take actions (pause, adjust budget, notify) when conditions are met. Returns rule names, statuses, evaluation specs, execution specs, and schedules.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,status,evaluation_spec,execution_spec,schedule_spec,created_time,updated_time. See Meta API docs for all available AdRule fields."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_ads"></a>

## `list_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/ads.ts#L8)

List ads for an ad account. Returns ads with their creative references, status, and tracking configuration. Supports filtering by effective status, ad set, campaign, and custom field selection.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (with or without \"act_\" prefix). Falls back to the default account if omitted."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to: id,name,adset_id,campaign_id,status,effective_status,creative,tracking_specs,conversion_specs,created_time,updated_time,preview_shareable_link"
    },
    "filtering": {
      "type": "string",
      "description": "JSON array of filter objects, e.g. [{\"field\":\"adset_id\",\"operator\":\"EQUAL\",\"value\":\"123\"}]. Supports fields like name, adset_id, campaign_id, and more."
    },
    "effective_status": {
      "type": "string",
      "description": "Comma-separated effective statuses to filter by, e.g. \"ACTIVE,PAUSED\". Valid values: ACTIVE, PAUSED, DELETED, ARCHIVED, IN_PROCESS, WITH_ISSUES, CAMPAIGN_PAUSED, ADSET_PAUSED, DISAPPROVED, PENDING_REVIEW, PREAPPROVED."
    },
    "limit": {
      "type": "number",
      "description": "Maximum number of ads to return per page (1-100). Default is 25."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_adsets"></a>

## `list_adsets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/adsets.ts#L8)

List ad sets for an ad account. Returns ad sets with their configuration including targeting, budget, schedule, and optimization settings. Supports filtering by effective status and custom field selection.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (with or without \"act_\" prefix). Falls back to the default account if omitted."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to: id,name,campaign_id,status,effective_status,daily_budget,lifetime_budget,budget_remaining,bid_amount,bid_strategy,billing_event,optimization_goal,targeting,promoted_object,start_time,end_time,created_time,updated_time"
    },
    "filtering": {
      "type": "string",
      "description": "JSON array of filter objects, e.g. [{\"field\":\"name\",\"operator\":\"CONTAIN\",\"value\":\"Brand\"}]. Supports fields like name, campaign_id, and more."
    },
    "effective_status": {
      "type": "string",
      "description": "Comma-separated effective statuses to filter by, e.g. \"ACTIVE,PAUSED\". Valid values: ACTIVE, PAUSED, DELETED, ARCHIVED, IN_PROCESS, WITH_ISSUES, CAMPAIGN_PAUSED, DISAPPROVED, PENDING_REVIEW, PREAPPROVED."
    },
    "limit": {
      "type": "number",
      "description": "Maximum number of ad sets to return per page (1-100). Default is 25."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_campaigns"></a>

## `list_campaigns`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/campaigns.ts#L8)

List campaigns for an ad account with optional filtering by status. Returns campaign IDs, names, objectives, statuses, budgets, and other configuration. Supports pagination via limit parameter.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,objective,status,effective_status,daily_budget,lifetime_budget,budget_remaining,buying_type,bid_strategy,special_ad_categories,created_time,updated_time. See Meta API docs for all available Campaign fields."
    },
    "effective_status": {
      "type": "string",
      "description": "JSON array of effective statuses to filter by. Example: [\"ACTIVE\",\"PAUSED\"]. Valid values: ACTIVE, PAUSED, DELETED, ARCHIVED, IN_PROCESS, WITH_ISSUES, CAMPAIGN_PAUSED, DISAPPROVED."
    },
    "filtering": {
      "type": "string",
      "description": "JSON array of filter objects. Each object has field, operator, and value. Example: [{\"field\":\"name\",\"operator\":\"CONTAIN\",\"value\":\"Spring\"}]. Operators: EQUAL, NOT_EQUAL, GREATER_THAN, LESS_THAN, CONTAIN, NOT_CONTAIN, IN, NOT_IN."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of campaigns to return per page (default 25, max 100)."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_creatives"></a>

## `list_creatives`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/creatives.ts#L8)

List ad creatives for an ad account. Returns creative IDs, names, object story specs, and other configuration. Use this to browse existing creatives before associating them with ads or to audit creative assets in the account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to: id,name,status,object_story_spec,thumbnail_url,image_url,url_tags,asset_feed_spec. See Meta API docs for all available AdCreative fields."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of creatives to return per page (default 25, max 100)."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_custom_audiences"></a>

## `list_custom_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/audiences.ts#L9)

List all custom audiences for an ad account. Returns audience IDs, names, subtypes, approximate sizes, and delivery status. Use this to discover existing audiences before creating new ones or to find audience IDs for use in ad set targeting.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,subtype,description,approximate_count,delivery_status,operation_status,time_created,time_updated. See Meta API docs for all available CustomAudience fields."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of audiences to return per page (default 25, max 100)."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_custom_conversions"></a>

## `list_custom_conversions`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/custom-conversions.ts#L9)

List all custom conversions for an ad account. Custom conversions let you track and optimize for specific URL-based conversion events without modifying your pixel code. They work by applying URL rules to standard pixel events — for example, tracking a "Purchase" event only when the URL contains "/thank-you". Returns conversion IDs, names, rules, associated pixels, and firing status. Use this to audit existing custom conversions or find IDs for reporting and optimization.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,pixel,custom_event_type,rule,default_conversion_value,creation_time,last_fired_time,is_archived. Other available fields include: account_id, aggregation_rule, business, data_sources, description, event_source_type, first_fired_time, is_unavailable, offline_conversion_data_set, retention_days."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_images"></a>

## `list_images`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/images.ts#L55)

List images in the ad account's image library. Optionally filter by specific image hashes to retrieve details for known images. Returns image metadata including hash, name, URL, dimensions, and creation time. Use this to find image hashes needed for creating ad creatives.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,hash,name,url,url_128,width,height,created_time,status. See Meta API docs for all available AdImage fields."
    },
    "hashes": {
      "type": "string",
      "description": "Comma-separated list of image hashes to filter by. Only images matching these hashes will be returned. Use this to look up specific images you already know the hash for."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_pixels"></a>

## `list_pixels`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/pixel.ts#L8)

List all Meta Pixels (datasets) associated with an ad account. Returns pixel IDs, names, creation times, and last fired times. Pixels are used for website event tracking, conversion optimization, and building custom audiences from website visitors. You need the pixel ID to send server-side conversion events via the Conversions API.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,code,creation_time,last_fired_time. Other available fields include: owner_ad_account, owner_business, data_use_setting, is_unavailable, automatic_matching_fields."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_saved_audiences"></a>

## `list_saved_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/saved-audiences.ts#L9)

List all saved audiences for an ad account. Saved audiences are reusable targeting specs (demographics, interests, behaviors, locations) that can be applied to ad sets. Returns audience names, targeting details, approximate reach, and run status. Use this to discover existing saved audiences before creating new ones or to review targeting configurations.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,name,description,targeting,approximate_count,run_status,sentence_lines. See Meta API docs for all available SavedAudience fields."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_videos"></a>

## `list_videos`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/videos.ts#L81)

List videos in the ad account's video library. Returns video metadata including IDs, titles, thumbnails, duration, and upload status. Use this to find video IDs needed for creating video ad creatives.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "fields": {
      "type": "string",
      "description": "Comma-separated list of fields to return. Defaults to id,title,description,length,created_time,updated_time,status,thumbnails,permalink_url. See Meta API docs for all available AdVideo fields."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of videos to return per page (default 25, max 100)."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="remove_audience_users"></a>

## `remove_audience_users`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/audiences.ts#L124)

Remove users from an existing custom audience by providing hashed PII data. The payload format is identical to add_audience_users — all PII values must be lowercase and SHA256 hashed. Meta will match and remove the specified users from the audience.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "audience_id": {
      "type": "string",
      "description": "The ID of the custom audience to remove users from. Get this from list_custom_audiences."
    },
    "payload": {
      "type": "string",
      "description": "JSON string containing the user data payload. Must include \"schema\" (array of PII types) and \"data\" (array of arrays with hashed values). All PII values must be lowercase and SHA256 hashed. Format is identical to add_audience_users. Example: {\"schema\":[\"EMAIL\"],\"data\":[[\"a1b2c3...hash...\"]]}"
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

<a id="search_behaviors"></a>

## `search_behaviors`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/targeting.ts#L33)

Search for behavior-based targeting options. Returns behavior IDs, names, audience sizes, and descriptions. Behaviors represent user actions and purchase patterns (e.g. "frequent travelers", "small business owners", "engaged shoppers"). Use these in ad set targeting_spec.behaviors.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "Search query string to find matching behaviors. Examples: \"travel\", \"business owner\", \"mobile\". The API matches against behavior names and descriptions."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of results to return (default 25, max 1000)."
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

<a id="search_demographics"></a>

## `search_demographics`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/targeting.ts#L93)

Search for demographic targeting options including education level, job titles, relationship status, life events, and more. Returns demographic IDs, names, audience sizes, and paths. Use these in ad set targeting_spec for refined audience demographic filtering.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "Search query string to find matching demographics. Examples: \"college\", \"married\", \"new job\", \"engineer\". Matches against demographic names and descriptions."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of results to return (default 25, max 1000)."
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

<a id="search_geo_locations"></a>

## `search_geo_locations`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/targeting.ts#L60)

Search for geographic targeting locations including countries, regions, cities, zip codes, DMAs, and electoral districts. Returns location keys, names, country codes, and population data. Use these in ad set targeting_spec.geo_locations to define where ads will be shown.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "Search query string to find matching locations. Examples: \"New York\", \"Turkey\", \"90210\", \"London\". Matches against location names and codes."
    },
    "location_types": {
      "type": "string",
      "description": "Comma-separated list of location types to search. Valid types: country, region, city, zip, geo_market, electoral_district. If omitted, all types are searched. Example: \"city,region\" to only return cities and regions."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of results to return (default 25, max 1000)."
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

<a id="search_interests"></a>

## `search_interests`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/targeting.ts#L7)

Search for interest-based targeting options. Returns interest IDs, names, audience sizes, and paths that can be used in ad set targeting_spec.interests. Use this to discover targetable interests for building audience segments (e.g. "yoga", "photography", "electric vehicles").

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "q": {
      "type": "string",
      "description": "Search query string to find matching interests. Examples: \"yoga\", \"digital marketing\", \"Tesla\". The API matches against interest names and related terms."
    },
    "limit": {
      "type": "string",
      "description": "Maximum number of results to return (default 25, max 1000). Use higher values for broad queries to see all available options."
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

<a id="send_conversion_event"></a>

## `send_conversion_event`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/conversions.ts#L7)

Send a server-side conversion event to the Meta Conversions API via a pixel. This is used for tracking offline conversions, server-side events, and CRM data. Events are attributed to ad clicks/views using user_data matching. Always hash PII (email, phone, name) with SHA-256 before sending. Use test_event_code during development to validate events in Events Manager without affecting production data.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "pixel_id": {
      "type": "string",
      "description": "Meta Pixel ID to send the event to. Use list_pixels to find pixel IDs. Example: \"123456789012345\"."
    },
    "event_name": {
      "type": "string",
      "description": "Standard or custom event name. Standard events: Purchase, Lead, CompleteRegistration, ViewContent, AddToCart, AddToWishlist, InitiateCheckout, AddPaymentInfo, Search, Contact, FindLocation, Schedule, StartTrial, SubmitApplication, Subscribe, CustomizeProduct, Donate. Custom events: any string (e.g. \"PremiumSignup\")."
    },
    "event_time": {
      "type": "string",
      "description": "Unix timestamp (seconds) when the event occurred. Must be within the last 7 days. Example: \"1700000000\". Use Math.floor(Date.now()/1000) for current time."
    },
    "action_source": {
      "type": "string",
      "description": "Where the event originated. Values: \"website\" (browser/pixel), \"app\" (mobile app), \"email\" (email click), \"phone_call\" (call center), \"chat\" (messaging), \"physical_store\" (in-store), \"system_generated\" (automated), \"other\"."
    },
    "user_data": {
      "type": "string",
      "description": "JSON string of user matching parameters. All PII values (em, ph, fn, ln, ct, st, zp, country) MUST be SHA-256 hashed before sending. Example: {\"em\":[\"a1b2c3...hash\"],\"ph\":[\"d4e5f6...hash\"],\"client_ip_address\":\"1.2.3.4\",\"client_user_agent\":\"Mozilla/5.0...\",\"fbc\":\"fb.1.123.456\",\"fbp\":\"fb.1.123.789\",\"external_id\":[\"user123\"]}. Keys: em=email, ph=phone, fn=first_name, ln=last_name, ct=city, st=state, zp=zip, country=country, external_id=your_user_id, fbc=click_id_cookie, fbp=browser_id_cookie."
    },
    "custom_data": {
      "type": "string",
      "description": "JSON string of event-specific data. Example: {\"value\":99.99,\"currency\":\"USD\",\"content_name\":\"Premium Plan\",\"content_ids\":[\"SKU123\"],\"content_type\":\"product\",\"order_id\":\"ORD-456\"}. For Purchase events, value and currency are required for ROAS reporting."
    },
    "event_source_url": {
      "type": "string",
      "description": "The URL where the event occurred. Required for website action_source. Example: \"https://example.com/checkout/thank-you\"."
    },
    "event_id": {
      "type": "string",
      "description": "Unique event ID for deduplication. If both browser pixel and server send the same event, use the same event_id to prevent double-counting. Example: \"event_abc123\"."
    },
    "test_event_code": {
      "type": "string",
      "description": "Test event code from Events Manager > Test Events tab. When provided, events appear in the Test Events panel instead of being processed as real events. Example: \"TEST12345\". Remove for production."
    }
  },
  "required": [
    "pixel_id",
    "event_name",
    "event_time",
    "action_source",
    "user_data"
  ],
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_ad"></a>

## `update_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/ads.ts#L127)

Update an existing ad. Allows modifying the name, status, creative, and tracking specs. Only the fields you provide will be updated; omitted fields remain unchanged.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "description": "The ID of the ad to update."
    },
    "name": {
      "type": "string",
      "description": "New name for the ad."
    },
    "status": {
      "type": "string",
      "description": "Updated status. Values: ACTIVE, PAUSED, DELETED, ARCHIVED."
    },
    "creative": {
      "type": "string",
      "description": "JSON string specifying the updated creative. Use {\"creative_id\":\"<id>\"} to swap to a different creative, or provide an inline spec."
    },
    "tracking_specs": {
      "type": "string",
      "description": "JSON string of updated tracking specs array."
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

<a id="update_ad_rule"></a>

## `update_ad_rule`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/rules.ts#L118)

Update an existing automated rule. You can modify the name, evaluation conditions, execution actions, schedule, or enable/disable the rule. Only the fields you provide will be updated; others remain unchanged. Use this to adjust thresholds, change actions, or pause rules temporarily.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "rule_id": {
      "type": "string",
      "description": "The automated rule ID to update (e.g. \"123456789\"). Get this from list_ad_rules."
    },
    "name": {
      "type": "string",
      "description": "New name for the automated rule."
    },
    "evaluation_spec": {
      "type": "string",
      "description": "Updated JSON string defining when and what to evaluate. Same format as create_ad_rule. Include \"evaluation_type\" and \"filters\" array. Example: {\"evaluation_type\":\"SCHEDULE\",\"filters\":[{\"field\":\"spent\",\"value\":200,\"operator\":\"GREATER_THAN\",\"type\":\"int\"}]}"
    },
    "execution_spec": {
      "type": "string",
      "description": "Updated JSON string defining what action to take. Same format as create_ad_rule. Include \"execution_type\" and optionally \"execution_options\". Example: {\"execution_type\":\"PAUSE\"}"
    },
    "schedule_spec": {
      "type": "string",
      "description": "Updated JSON string defining how often the rule runs. Same format as create_ad_rule. Include \"schedule_type\" and optionally \"schedule\" array."
    },
    "status": {
      "type": "string",
      "description": "New rule status. Valid values: ENABLED (rule is active and will execute), DISABLED (rule is paused and will not execute)."
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

<a id="update_adset"></a>

## `update_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/adsets.ts#L178)

Update an existing ad set. Allows modifying the name, targeting, budget, schedule, optimization, and status. Only the fields you provide will be updated; omitted fields remain unchanged.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "adset_id": {
      "type": "string",
      "description": "The ID of the ad set to update."
    },
    "name": {
      "type": "string",
      "description": "New name for the ad set."
    },
    "targeting": {
      "type": "string",
      "description": "JSON string of the updated targeting spec. Replaces the entire targeting spec. Example: '{\"geo_locations\":{\"countries\":[\"US\",\"CA\"]},\"age_min\":25}'."
    },
    "billing_event": {
      "type": "string",
      "description": "Updated billing event. Common values: IMPRESSIONS, LINK_CLICKS, POST_ENGAGEMENT."
    },
    "optimization_goal": {
      "type": "string",
      "description": "Updated optimization goal. Common values: REACH, LINK_CLICKS, CONVERSIONS, VALUE."
    },
    "bid_amount": {
      "type": "number",
      "description": "Updated bid amount in cents (integer)."
    },
    "daily_budget": {
      "type": "number",
      "description": "Updated daily budget in cents (integer)."
    },
    "lifetime_budget": {
      "type": "number",
      "description": "Updated lifetime budget in cents (integer)."
    },
    "start_time": {
      "type": "string",
      "description": "Updated start time in ISO 8601 format."
    },
    "end_time": {
      "type": "string",
      "description": "Updated end time in ISO 8601 format."
    },
    "status": {
      "type": "string",
      "description": "Updated status. Values: ACTIVE, PAUSED, DELETED, ARCHIVED."
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

<a id="update_campaign"></a>

## `update_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/campaigns.ts#L184)

Update an existing campaign. You can modify the name, status, budget, and bid strategy. Only the fields you provide will be updated; others remain unchanged. Use this to pause/activate campaigns or adjust budgets.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "description": "The campaign ID to update (e.g. \"123456789\")."
    },
    "name": {
      "type": "string",
      "description": "New name for the campaign."
    },
    "status": {
      "type": "string",
      "description": "New campaign status. Valid values: ACTIVE, PAUSED, DELETED, ARCHIVED."
    },
    "daily_budget": {
      "type": "string",
      "description": "New daily budget in account currency cents (e.g. \"5000\" for $50.00 USD). Mutually exclusive with lifetime_budget."
    },
    "lifetime_budget": {
      "type": "string",
      "description": "New lifetime budget in account currency cents (e.g. \"100000\" for $1000.00 USD). Mutually exclusive with daily_budget."
    },
    "bid_strategy": {
      "type": "string",
      "description": "New bid strategy. Valid values: LOWEST_COST_WITHOUT_CAP, LOWEST_COST_WITH_BID_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS."
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

<a id="update_creative"></a>

## `update_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/creatives.ts#L117)

Update an existing ad creative. Only the provided fields will be modified; omitted fields remain unchanged. Note: not all fields are updatable after creation -- name, url_tags, and object_story_spec are the most commonly updated fields.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "creative_id": {
      "type": "string",
      "description": "The ID of the ad creative to update."
    },
    "name": {
      "type": "string",
      "description": "Updated name for the creative."
    },
    "object_story_spec": {
      "type": "string",
      "description": "Updated JSON string defining the creative content. Same structure as create_creative: must include \"page_id\" and one of \"link_data\", \"video_data\", or \"photo_data\"."
    },
    "url_tags": {
      "type": "string",
      "description": "Updated URL query parameters appended to all links in the creative for tracking. Example: \"utm_source=facebook&utm_medium=cpc\". Do not include the leading \"?\"."
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

<a id="upload_image"></a>

## `upload_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/images.ts#L9)

Upload an image to the ad account's image library for use in ad creatives. Supports two upload methods: provide base64-encoded image data via "bytes", or a publicly accessible URL via "url" (Meta will download the image). Returns the image hash needed for creating ad creatives. Supported formats: JPG, PNG, BMP, TIFF, GIF (non-animated). Max size: 30MB.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "bytes": {
      "type": "string",
      "description": "Base64-encoded image data. Use this method when you have the image content available directly. Provide either \"bytes\" or \"url\", not both."
    },
    "url": {
      "type": "string",
      "description": "Publicly accessible URL of the image. Meta will download the image from this URL. Use this method for images already hosted online. Provide either \"bytes\" or \"url\", not both."
    },
    "name": {
      "type": "string",
      "description": "Optional name for the image. If not provided, Meta will auto-generate a name."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="upload_video"></a>

## `upload_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/videos.ts#L9)

Upload a video to the ad account's video library for use in ad creatives. Supports three upload methods: "file_url" (recommended for large files — Meta downloads directly from a public URL), "source" (base64-encoded video data for small files under 10MB), or "file_path" (local filesystem path — server reads and uploads via multipart). Provide exactly one upload method. Supported formats: MP4, MOV, AVI, and others. Max size varies by method (file_url supports up to 4GB).

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "file_url": {
      "type": "string",
      "description": "Publicly accessible URL of the video file. Meta will download the video directly. Recommended for large files as it avoids transferring data through the server. Provide exactly one of: file_url, source, or file_path."
    },
    "source": {
      "type": "string",
      "description": "Base64-encoded video data. Best for small files under 10MB. Provide exactly one of: file_url, source, or file_path."
    },
    "file_path": {
      "type": "string",
      "description": "Absolute path to a video file on the local filesystem. The server will read the file and upload it via multipart form data. Provide exactly one of: file_url, source, or file_path."
    },
    "title": {
      "type": "string",
      "description": "Title for the video. Displayed in the video library and can be used in ad creatives."
    },
    "description": {
      "type": "string",
      "description": "Description for the video. Stored as metadata in the video library."
    }
  },
  "additionalProperties": false,
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="validate_targeting"></a>

## `validate_targeting`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/serkanhaslak/meta-mcp/blob/66898db8ef4daf015dfeb5197950b52807263e22/src/tools/targeting-utils.ts#L38)

Validate a targeting specification before using it in an ad set. Checks whether the targeting spec is well-formed and deliverable — for example, it verifies that interest IDs exist, geo-locations are valid, age ranges are acceptable, and the overall combination is not too narrow. Returns validation status and detailed error messages for any issues found. Always validate targeting specs before creating or updating ad sets to catch problems early.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "description": "Ad account ID (e.g. \"123456789\" or \"act_123456789\"). Falls back to the default account from META_AD_ACCOUNT_ID env var if not provided."
    },
    "targeting_spec": {
      "type": "string",
      "description": "JSON string of the full targeting specification to validate. This should be the same format used in ad set targeting_spec. Must include at least geo_locations. Example: {\"geo_locations\":{\"countries\":[\"US\"]},\"age_min\":25,\"age_max\":45,\"interests\":[{\"id\":\"6003139266461\",\"name\":\"Yoga\"}],\"genders\":[1]}. The API will check all fields for validity, supported values, and deliverability."
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

