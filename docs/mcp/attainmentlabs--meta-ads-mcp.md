# attainmentlabs/meta-ads-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/attainmentlabs/meta-ads-mcp) · [Machine-readable snapshot](../../catalog/attainmentlabs--meta-ads-mcp.json)

Complete registered tool snapshot. **13 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`82d29b127c12`](https://github.com/attainmentlabs/meta-ads-mcp/tree/82d29b127c129d12489a46ec4b7e39443114aea1). Method: `runtime-tools-list`.

- Unconstrained array items and prose-only options remain as upstream exposes them; no additional parameter constraints are inferred.

## Tools

- [activate_campaign](#activate_campaign)
- [bulk_update_campaign_status](#bulk_update_campaign_status)
- [create_meta_campaign](#create_meta_campaign)
- [delete_campaign](#delete_campaign)
- [get_ad_account_summary](#get_ad_account_summary)
- [get_campaign_status](#get_campaign_status)
- [get_meta_insights](#get_meta_insights)
- [list_ad_sets](#list_ad_sets)
- [list_ads](#list_ads)
- [list_campaigns](#list_campaigns)
- [pause_campaign](#pause_campaign)
- [update_daily_budget](#update_daily_budget)
- [upload_ad_image](#upload_ad_image)

<a id="activate_campaign"></a>

## `activate_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L752)

Activate (unpause) a Meta campaign. This will resume ad spending.

The campaign must have a valid payment method and approved creatives.
Set confirm=True after reviewing the campaign in Ads Manager.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "confirm": {
      "default": false,
      "title": "Confirm",
      "type": "boolean"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "activate_campaignArguments",
  "type": "object"
}
```

</details>

<a id="bulk_update_campaign_status"></a>

## `bulk_update_campaign_status`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L630)

Bulk pause, activate, or delete campaigns.

status must be PAUSED, ACTIVE, or DELETED. dry_run defaults to True.
Set dry_run=False and confirm=True after reviewing the campaign IDs.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_ids": {
      "items": {},
      "title": "Campaign Ids",
      "type": "array"
    },
    "status": {
      "title": "Status",
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "title": "Dry Run",
      "type": "boolean"
    },
    "confirm": {
      "default": false,
      "title": "Confirm",
      "type": "boolean"
    }
  },
  "required": [
    "campaign_ids",
    "status"
  ],
  "title": "bulk_update_campaign_statusArguments",
  "type": "object"
}
```

</details>

<a id="create_meta_campaign"></a>

## `create_meta_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L358)

Create a complete Meta ad campaign: campaign, ad set, creatives, and ads.

Each item in `ads` is a dict with:
  - name (str): ad name
  - image_path (str): absolute path to image file on disk
  - primary_text (str): ad body copy
  - headline (str): ad headline
  - link (str): destination URL
  - cta (str, optional): call-to-action button, default "LEARN_MORE"
  - description (str, optional): ad description text

daily_budget_cents: budget in cents. 1000 = $10/day, 3000 = $30/day.

dry_run: when True (default), simulates all API calls without spending money.
Set dry_run=False to actually deploy. All campaigns start as PAUSED regardless.
confirm: required when dry_run=False. This is the approval gate.

Valid objectives: OUTCOME_TRAFFIC, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT,
OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_APP_PROMOTION

Valid CTAs: LEARN_MORE, SIGN_UP, DOWNLOAD, SHOP_NOW, BOOK_NOW, GET_OFFER,
SUBSCRIBE, CONTACT_US, APPLY_NOW, WATCH_MORE, INSTALL_MOBILE_APP


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_name": {
      "title": "Campaign Name",
      "type": "string"
    },
    "ad_set_name": {
      "title": "Ad Set Name",
      "type": "string"
    },
    "objective": {
      "default": "OUTCOME_TRAFFIC",
      "title": "Objective",
      "type": "string"
    },
    "countries": {
      "default": [
        "US"
      ],
      "items": {},
      "title": "Countries",
      "type": "array"
    },
    "age_min": {
      "default": 18,
      "title": "Age Min",
      "type": "integer"
    },
    "age_max": {
      "default": 65,
      "title": "Age Max",
      "type": "integer"
    },
    "daily_budget_cents": {
      "default": 1000,
      "title": "Daily Budget Cents",
      "type": "integer"
    },
    "optimization_goal": {
      "default": "LINK_CLICKS",
      "title": "Optimization Goal",
      "type": "string"
    },
    "ads": {
      "default": [],
      "items": {},
      "title": "Ads",
      "type": "array"
    },
    "dry_run": {
      "default": true,
      "title": "Dry Run",
      "type": "boolean"
    },
    "confirm": {
      "default": false,
      "title": "Confirm",
      "type": "boolean"
    }
  },
  "required": [
    "campaign_name",
    "ad_set_name"
  ],
  "title": "create_meta_campaignArguments",
  "type": "object"
}
```

</details>

<a id="delete_campaign"></a>

## `delete_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L770)

Permanently delete a Meta campaign. This cannot be undone.

Set confirm=True after reviewing the campaign ID.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "confirm": {
      "default": false,
      "title": "Confirm",
      "type": "boolean"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "delete_campaignArguments",
  "type": "object"
}
```

</details>

<a id="get_ad_account_summary"></a>

## `get_ad_account_summary`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L484)

Get the configured Meta ad account summary.

Read-only. Use this before campaign work to confirm the connected account,
currency, timezone, spend, balance, and account status.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {},
  "title": "get_ad_account_summaryArguments",
  "type": "object"
}
```

</details>

<a id="get_campaign_status"></a>

## `get_campaign_status`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L702)

Get the status of a Meta campaign including its ad sets and ads.

Returns campaign name, status, objective, and lists of ad sets and ads
with their statuses and budgets.


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
  "title": "get_campaign_statusArguments",
  "type": "object"
}
```

</details>

<a id="get_meta_insights"></a>

## `get_meta_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L538)

Get Meta Ads performance insights.

Read-only. object_id can be an ad account, campaign, ad set, or ad ID.
Leave object_id blank to use the configured ad account. Use level for
account breakdowns such as campaign, adset, or ad.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "object_id": {
      "default": "",
      "title": "Object Id",
      "type": "string"
    },
    "level": {
      "default": "",
      "title": "Level",
      "type": "string"
    },
    "date_preset": {
      "default": "last_7d",
      "title": "Date Preset",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "get_meta_insightsArguments",
  "type": "object"
}
```

</details>

<a id="list_ad_sets"></a>

## `list_ad_sets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L516)

List recent ad sets in the configured Meta ad account.

Read-only. Use this to find ad set IDs before budget or status changes.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "list_ad_setsArguments",
  "type": "object"
}
```

</details>

<a id="list_ads"></a>

## `list_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L527)

List recent ads in the configured Meta ad account.

Read-only. Use this to find ad IDs and inspect delivery status.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "list_adsArguments",
  "type": "object"
}
```

</details>

<a id="list_campaigns"></a>

## `list_campaigns`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L504)

List recent campaigns in the configured Meta ad account.

Read-only. Use this to find campaign IDs before status, insights, budget,
pause, activate, or bulk operations.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "list_campaignsArguments",
  "type": "object"
}
```

</details>

<a id="pause_campaign"></a>

## `pause_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L742)

Pause a live Meta campaign. Safe to call on already-paused campaigns.

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
  "title": "pause_campaignArguments",
  "type": "object"
}
```

</details>

<a id="update_daily_budget"></a>

## `update_daily_budget`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L591)

Update daily budget for a campaign or ad set.

dry_run defaults to True. Set dry_run=False and confirm=True after review.
If META_ADS_MAX_DAILY_BUDGET_CENTS is set, the budget cannot exceed it.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "object_id": {
      "title": "Object Id",
      "type": "string"
    },
    "daily_budget_cents": {
      "title": "Daily Budget Cents",
      "type": "integer"
    },
    "dry_run": {
      "default": true,
      "title": "Dry Run",
      "type": "boolean"
    },
    "confirm": {
      "default": false,
      "title": "Confirm",
      "type": "boolean"
    }
  },
  "required": [
    "object_id",
    "daily_budget_cents"
  ],
  "title": "update_daily_budgetArguments",
  "type": "object"
}
```

</details>

<a id="upload_ad_image"></a>

## `upload_ad_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/attainmentlabs/meta-ads-mcp/blob/82d29b127c129d12489a46ec4b7e39443114aea1/meta_ads_mcp/server.py#L568)

Upload an image to the configured Meta ad account.

dry_run defaults to True. Set dry_run=False and confirm=True to upload.
Returns an image hash that can be used in ad creatives.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "image_path": {
      "title": "Image Path",
      "type": "string"
    },
    "dry_run": {
      "default": true,
      "title": "Dry Run",
      "type": "boolean"
    },
    "confirm": {
      "default": false,
      "title": "Confirm",
      "type": "boolean"
    }
  },
  "required": [
    "image_path"
  ],
  "title": "upload_ad_imageArguments",
  "type": "object"
}
```

</details>

