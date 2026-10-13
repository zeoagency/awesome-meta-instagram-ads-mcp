# amekala/ads-mcp — tools 141–175

[All tools](amekala--ads-mcp.md) · [Tool index](../tool-index.md)

<a id="list_call_assets"></a>

## `list_call_assets`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List every phone (CALL) asset on a campaign, with status and resource names.

Use this to inspect call assets before adding one (so you don't create a
duplicate), or to find the asset/link to pause or remove.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED). Get from list_campaigns.
- customer_id: Optional Google Ads customer ID

**Returns:** each call asset's phone_number, country_code, status
(ENABLED/PAUSED), asset_resource_name, and campaign_asset_resource_name.

**Execution time:** 1-2 seconds (read-only)

**Example:**
User: "What phone numbers are on this campaign?"
Agent: list_call_assets(campaign_id="19850524478")

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing CALL assets (phone extensions) on a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (numeric). Get from list_campaigns.",
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
  "title": "ListCallAssetsInput",
  "type": "object"
}
```

</details>

<a id="list_campaign_extensions"></a>

## `list_campaign_extensions`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List all campaign-level assets for a campaign: sitelinks, callouts, structured snippets, call assets, business names, and images.

Returns a summary of every asset type configured on the campaign, each with
its status (ENABLED/PAUSED) and resource name.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED). Get from list_campaigns.
- customer_id: Optional Google Ads customer ID

**Returns:**
- Sitelinks, Callouts, Structured Snippets
- Call assets (phone number + country + status)
- Business names
- Images (field type + status)

**Execution time:** 1-2 seconds (read-only)

**When to use:**
- User asks "what extensions/assets do I have?"
- BEFORE adding an asset — check what already exists (avoids duplicates)
- Auditing campaign setup / finding a duplicate to clean up

**Example:**
User: "Show me the extensions on my campaign"
Agent:
1. Uses list_campaigns to get campaign_id
2. Uses list_campaign_extensions to see all assets

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing all extensions on a campaign.\n\nReturns all sitelinks, callouts, and structured snippets for the campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to list extensions for. Get from list_campaigns.",
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
  "title": "ListCampaignExtensionsInput",
  "type": "object"
}
```

</details>

<a id="list_campaigns"></a>

## `list_campaigns`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List all Google Ads campaigns for the connected account.

⚠️ CRITICAL: Call this tool BEFORE creating new campaigns to ask the user:
"Would you like to create a new campaign or update an existing one?"

This tool retrieves READ-ONLY data. Safe to call multiple times.

**Returns:**
- List of all campaigns with IDs, names, status, type, budget
- 30-day performance metrics for each campaign (impressions, clicks, cost, conversions)
- Total campaign count

**Parameters:**
- status_filter: ENABLED, PAUSED, or ALL (optional, default: ALL)
- campaign_type: SEARCH, PERFORMANCE_MAX (or PMAX), DISPLAY, SHOPPING, VIDEO, DEMAND_GEN, APP, or ALL (optional, default: ALL)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-5 seconds (direct Google Ads API call)

**Campaign Management Guidelines:**

BEFORE Starting Any Campaign Work:
1. ALWAYS use `list_campaigns` first
2. Ask user: "Would you like to create a new campaign or update an existing one?"
3. If updating, use `get_campaign_structure` to see full details

User Intent Mapping:
| User Says | Agent Action |
|-----------|--------------|
| "Create a campaign for X" | List existing first, then ask create vs update |
| "Change the budget" | Get structure, then use update tools |
| "Add more keywords" | Get structure, then add keywords |
| "Update my ads" | Get structure, then update ad content |
| "Pause the campaign" | Use pause_campaign tool |

**Use this tool to:**
- View all existing campaigns before creating new ones
- Find campaign IDs for update operations
- Get a quick overview of account structure
- Identify active vs paused campaigns

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing campaigns",
  "properties": {
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
      "description": "Filter by status: ENABLED, PAUSED, or ALL (default: ALL)",
      "title": "Status Filter"
    },
    "campaign_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by type: SEARCH, PERFORMANCE_MAX (or PMAX), DISPLAY, SHOPPING, VIDEO, DEMAND_GEN, APP, or ALL (default: ALL)",
      "title": "Campaign Type"
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
  "title": "ListCampaignsInput",
  "type": "object"
}
```

</details>

<a id="list_conversion_actions"></a>

## `list_conversion_actions`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List conversion actions for the connected Google Ads account with full per-action metadata.

This tool retrieves READ-ONLY data. Safe to call multiple times.

**Returns for each conversion action:**
- id, name, resource_name
- category (PURCHASE, SUBMIT_LEAD_FORM, SIGNUP, ADD_TO_CART, BEGIN_CHECKOUT, BOOK_APPOINTMENT, etc.)
- status (ENABLED, REMOVED, HIDDEN)
- type (WEBPAGE, UPLOAD_CLICKS, GOOGLE_ANALYTICS_4, FIREBASE_*, etc.)
- counting_type (ONE_PER_CLICK or MANY_PER_CLICK)
- primary_for_goal (true if this action is primary for its category goal)
- include_in_conversions_metric (true if it counts in Smart Bidding "Conversions")
- click_through_lookback_window_days, view_through_lookback_window_days
- value_settings: default_value, default_currency_code, always_use_default_value
- attribution_model (GOOGLE_ADS_LAST_CLICK, DATA_DRIVEN, etc.)

**Parameters:**
- customer_id: Optional Google Ads customer ID (uses primary if omitted)
- status_filter: 'ENABLED' (default — matches Google Ads UI active list), 'all' (include HIDDEN), or 'primary' (only primary_for_goal=true)
- include_removed: false by default (matches Google Ads UI). Set true to include status=REMOVED for full audit.

**Execution time:** 1-3 seconds (single GAQL query, cached 1 hour in Redis)

**Use this tool when:**
- User asks for conversion setup, conversion action list, or conversion tracking audit beyond a health-score summary
- User wants per-action category, counting mode, or value settings to reason about ROAS / TARGET_ROAS bidding
- User wants to see secondary or non-primary actions that audit_conversion_tracking truncates
- Before any per-conversion-action analysis (downstream tools may need the action IDs)

**Tip:** For accounts with many actions (100+), `status_filter='primary'` returns just the goal-primary actions used by Smart Bidding — usually the most relevant subset.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for list_conversion_actions tool.",
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
    "status_filter": {
      "default": "ENABLED",
      "description": "Filter actions by status: 'ENABLED' (default, matches Google Ads UI active list), 'all' (every action including HIDDEN/UNKNOWN), or 'primary' (only actions where primary_for_goal=true).",
      "title": "Status Filter",
      "type": "string"
    },
    "include_removed": {
      "default": false,
      "description": "If true, include conversion actions with status=REMOVED. Default false matches Google Ads UI.",
      "title": "Include Removed",
      "type": "boolean"
    }
  },
  "title": "ListConversionActionsInput",
  "type": "object"
}
```

</details>

<a id="list_google_languages"></a>

## `list_google_languages`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List Google Ads language constants. Returns the catalog of valid language resource names for `target_languages` in campaign creation tools.

**WHEN TO USE:**
Call this BEFORE campaign creation whenever the user requests a language that isn't obviously ISO-2 (e.g., user says "Brazilian Portuguese", "Swiss German", "Simplified Chinese"). Returns the correct `languageConstants/<id>` + the ISO code Google expects.

Campaign creation tools accept ISO codes (e.g., 'en', 'pt-BR'), numeric IDs (1000), or full resource names (`languageConstants/1000`) — but the catalog here is authoritative.

**INPUT:** optional `search` substring (searches both name and code), optional `only_targetable` (default true — excludes non-targetable legacy codes).

**Execution time:** instant after first call. Redis-cached 24 hours.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for list_google_languages.",
  "properties": {
    "search": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional case-insensitive substring filter over language name or code (e.g., 'portuguese', 'pt', 'spanish').",
      "title": "Search"
    },
    "only_targetable": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": true,
      "description": "Filter to languages that can be targeted in campaigns. Default true.",
      "title": "Only Targetable"
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
  "title": "ListGoogleLanguagesInput",
  "type": "object"
}
```

</details>

<a id="list_labels"></a>

## `list_labels`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List the account's labels (for organizing and reporting on campaigns).

Returns each label's id, name, and description. Use the id with add_campaign_label to
tag a campaign, or with create_label to make a new one first.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "List the account's labels.",
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
  "title": "ListLabelsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_ad_sets"></a>

## `list_meta_ad_sets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see the ad sets within a specific Meta campaign, including their targeting, budgets, and optimization settings.

This tool retrieves ad sets for a given campaign with their status, budget, optimization goal, and billing event.

Returns:
- Ad set list with name, ID, status, budget, optimization goal, billing event
- Next step guidance for editing ad sets or viewing ads

When to use this tool:
- "Show me the ad sets in campaign [ID]"
- "What ad sets are running in my campaign?"
- "List the ad groups for this campaign"
- "Which ad sets are active/paused?"
- Before using `update_meta_ad_set` when user doesn't know the ad set ID

Parameters:
- campaign_id: Campaign ID to list ad sets for (required)
- status: Filter by status (optional)
- limit: Max ad sets to return (default: 100)
- ad_account_id: Optional

Execution time: 2-5 seconds
Data source: Meta Marketing API (live)

Workflow:
1. Use `list_meta_campaigns` to find campaign IDs
2. Use `list_meta_ad_sets` with campaign_id to see ad sets
3. Use `update_meta_ad_set` to edit targeting, budget, or placements
4. Use `list_meta_ads` with ad_set_id to see individual ads

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing Meta ad sets",
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
      "description": "Filter ad sets to a specific campaign ID (optional - if not provided, lists all ad sets in the account)",
      "title": "Campaign Id"
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
      "description": "Filter by status: comma-separated values like 'ACTIVE,PAUSED'",
      "title": "Status"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of ad sets to return (default: 100)",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "ListMetaAdSetsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_ads"></a>

## `list_meta_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see the individual ads within a specific Meta ad set, including their status and creative information.

This tool retrieves ads for a given ad set with their name, status, and creative ID.

Returns:
- Ad list with name, ID, status, creative ID
- Next step guidance for editing ads

When to use this tool:
- "Show me the ads in ad set [ID]"
- "What ads are running in this ad set?"
- "List the individual ads"
- "Which ads are active/paused?"
- Before using `update_meta_ad` when user doesn't know the ad ID

Parameters:
- ad_set_id: Ad Set ID to list ads for (required for direct listing)
- campaign_id: Campaign ID (will guide user to use ad_set_id)
- status: Filter by status (optional)
- limit: Max ads to return (default: 100)

Execution time: 2-5 seconds
Data source: Meta Marketing API (live)

Workflow:
1. Use `list_meta_ad_sets` to find ad set IDs
2. Use `list_meta_ads` with ad_set_id to see ads
3. Use `update_meta_ad` to pause/resume or swap creative

Alternative: Use `get_meta_campaign_details` with `include_hierarchy=true` to see the full campaign tree at once.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing Meta ads",
  "properties": {
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
      "description": "Filter ads to a specific ad set ID",
      "title": "Ad Set Id"
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
      "description": "Filter ads to a specific campaign ID",
      "title": "Campaign Id"
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
      "description": "Filter by status: comma-separated values like 'ACTIVE,PAUSED'",
      "title": "Status"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of ads to return (default: 100)",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "ListMetaAdsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_campaigns"></a>

## `list_meta_campaigns`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see their existing Meta/Facebook/Instagram campaigns, browse campaign structure, or find a campaign ID.

This tool retrieves all campaigns in the connected Meta ad account with their status, objective, budget, and creation date.

Returns:
- Campaign list with name, ID, status, objective, budget
- Status summary (how many ACTIVE, PAUSED, etc.)
- Next step guidance for drilling into campaign details

When to use this tool:
- "Show me my Meta campaigns"
- "List my Facebook ad campaigns"
- "What campaigns do I have running?"
- "Which campaigns are active?"
- "Find my campaign for [product/brand]"
- "I need to find a campaign ID"
- Before using update/pause/resume tools when user doesn't know the campaign ID

Parameters:
- status: Filter by status (comma-separated: 'ACTIVE', 'PAUSED', 'DELETED', 'ARCHIVED')
- effective_status: Filter by effective status (includes inherited states like 'CAMPAIGN_PAUSED')
- objective: Filter by objective (OUTCOME_TRAFFIC, OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_AWARENESS)
- limit: Max campaigns to return (default: 100)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 2-5 seconds
Data source: Meta Marketing API (live)

Workflow:
1. Use `list_meta_campaigns` to find campaigns
2. Use `get_meta_campaign_details` with a campaign ID to see full structure
3. Use `update_meta_campaign` or `update_meta_ad_set` to make changes

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing Meta campaigns",
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
      "description": "Filter by status: comma-separated values like 'ACTIVE,PAUSED'. Options: ACTIVE, PAUSED, DELETED, ARCHIVED",
      "title": "Status"
    },
    "effective_status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Filter by effective status: comma-separated values. Options: ACTIVE, PAUSED, DELETED, ARCHIVED, IN_PROCESS, WITH_ISSUES, CAMPAIGN_PAUSED",
      "title": "Effective Status"
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
      "description": "Filter by campaign objective: OUTCOME_TRAFFIC, OUTCOME_SALES, OUTCOME_LEADS, OUTCOME_AWARENESS, OUTCOME_ENGAGEMENT",
      "title": "Objective"
    },
    "limit": {
      "default": 100,
      "description": "Maximum number of campaigns to return (default: 100, max: 500)",
      "maximum": 500,
      "minimum": 1,
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "ListMetaCampaignsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_catalogs"></a>

## `list_meta_catalogs`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to browse product catalogs for catalog / dynamic product ads (DPA / Advantage+ Catalog), or before creating a catalog campaign.

Returns all product catalogs attached to the business behind the ad account (id, name, product_count, vertical).

Workflow:
1. Call this to discover catalogs
2. Pass a catalog ID to list_meta_product_sets / list_meta_products / create_meta_product_set

When to use:
- "Show my product catalogs", "list my Shopify catalog"
- Before creating a catalog / dynamic product / Advantage+ Catalog ad

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing product catalogs attached to the business.",
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
      "description": "Meta ad account ID (e.g., 'act_123456'). If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "title": "ListMetaCatalogsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_custom_audiences"></a>

## `list_meta_custom_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to browse, list, or select Custom Audiences for targeting — DB lists, lookalike audiences, remarketing segments, website visitors, engagement audiences.

Returns all Custom Audiences for the ad account with ID, name, type (subtype), approximate size, and delivery status.

Workflow:
1. Call this tool to discover available custom audiences
2. Use audience IDs with campaign creation tools via `custom_audiences` parameter
3. Optionally use `excluded_custom_audiences` to exclude specific audiences

When to use:
- Before creating campaigns that need custom audience targeting
- When user asks "which audiences do I have?" or "show me my lookalike audiences"
- When setting up remarketing or DB-list campaigns

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing custom audiences in a Meta ad account",
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
    }
  },
  "title": "ListMetaCustomAudiencesInput",
  "type": "object"
}
```

</details>

<a id="list_meta_instagram_accounts"></a>

## `list_meta_instagram_accounts`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to run ads on Instagram, asks about Instagram accounts, or you need to find the instagram_account_id before campaign creation.

Returns Instagram accounts that are:
1. Authorized for ads on the ad account (from Business Manager)
2. Linked to Facebook Pages (from Page settings)

Workflow:
1. Call this tool to discover available Instagram accounts
2. Use the Instagram account ID with campaign creation tools via `instagram_account_id` parameter

When to use:
- Before any campaign creation to enable Instagram placements
- When user asks "which Instagram accounts can I use?"
- When an Instagram association fails and user needs to find the right account

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing Instagram accounts authorized for ads",
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
      "description": "Meta ad account ID (e.g., 'act_123456'). If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "title": "ListMetaInstagramAccountsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_lead_forms"></a>

## `list_meta_lead_forms`

Scope: **meta-ads** · Capability: **leads** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see their Meta lead generation forms, list lead forms, or find a lead form ID.

Lists all lead generation forms for a Facebook Page associated with the ad account.

When to use this tool:
- "Show me my Meta lead forms"
- "List my Facebook lead generation forms"
- "What lead forms do I have?"
- "Find my lead form ID"
- "Show lead forms for my page"

Returns per form:
- Form name, status (ACTIVE/ARCHIVED), leads count
- Creation date
- Form questions (field names and types)
- Form ID (needed for get_meta_lead_form_submissions and campaign creation with lead_form_id)

Parameters:
- page_id: Facebook Page ID (optional — auto-resolved from ad account if not provided)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts
- limit: Maximum forms to return (default: 50)

Note: Lead forms belong to Facebook Pages, not ad accounts. If you don't have the page_id, just omit it and the tool will auto-resolve from the ad account's promotable pages.

Permission: Requires 'leads_retrieval' scope. If the user gets a permission error, they need to disconnect and reconnect their Meta account to grant the updated permissions.

Execution time: 2-5 seconds
Data source: Meta Marketing API (live)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing Meta lead generation forms.",
  "properties": {
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
      "description": "Facebook Page ID that owns the lead forms. If not provided, auto-resolves from the ad account's promotable pages.",
      "title": "Page Id"
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
      "default": 50,
      "description": "Maximum number of lead forms to return (default: 50)",
      "title": "Limit",
      "type": "integer"
    }
  },
  "title": "MetaLeadFormsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_pages"></a>

## `list_meta_pages`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to know which Facebook Page an ad will run from, or a create/add tool reported the account has 2+ Pages and you need to pick one.

Returns every Facebook Page that can run ads on the ad account (id + name + any linked Instagram account).

Workflow:
1. Call this tool to discover the account's promotable Pages.
2. Pass the chosen page's id to any Meta create/add tool via the `facebook_page_id` parameter.

When to use:
- When a create/add tool returns `needs_page_disambiguation` (the account has 2+ Pages and Meta has no default).
- When the user asks "which Facebook Page will this run from?" or wants a specific Page.
- Before creating a campaign on an account you know has multiple Pages, to choose deliberately rather than let it ask.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing Facebook Pages that can run ads on the ad account.",
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
      "description": "Meta ad account ID (e.g., 'act_123456'). If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "title": "ListMetaPagesInput",
  "type": "object"
}
```

</details>

<a id="list_meta_pixels"></a>

## `list_meta_pixels`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants conversion tracking, asks about Meta Pixels, or before creating OUTCOME_SALES campaigns.

Returns all Meta Pixels for the ad account with their status and last fired time.

Workflow:
1. Call this tool to discover available pixels
2. Use the pixel ID with campaign creation tools via `pixel_id` parameter
3. Optionally specify `pixel_event_name` (default: PURCHASE)

When to use:
- Before creating OUTCOME_SALES campaigns (pixel_id is required for conversion tracking)
- When user asks "which pixels do I have?"
- When setting up conversion tracking for campaigns

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing Meta Pixels",
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
      "description": "Meta ad account ID (e.g., 'act_123456'). If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "title": "ListMetaPixelsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_product_sets"></a>

## `list_meta_product_sets`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to see the product sets (groupings) inside a catalog, to choose which products a catalog ad should advertise.

Returns product sets (id, name, product_count) for a catalog. The default 'All Products' set always exists.

When to use:
- "What product sets do I have?", "show the groups in my catalog"
- After list_meta_catalogs, before creating a catalog ad

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing product sets within a catalog.",
  "properties": {
    "catalog_id": {
      "description": "Product catalog ID (required). Get it from list_meta_catalogs.",
      "title": "Catalog Id",
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
    "catalog_id"
  ],
  "title": "ListMetaProductSetsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_products"></a>

## `list_meta_products`

Scope: **meta-ads** · Capability: **catalogs** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to inspect the individual products in a catalog or product set (to confirm what will be advertised).

Returns products (SKU/retailer_id, name, price, availability). Optionally scoped to a product set.

When to use:
- "What products are in my catalog?", "show items in the Footwear set"
- To verify products before running a catalog ad

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing products in a catalog or product set.",
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
      "description": "Optional product set ID to scope products. Get it from list_meta_product_sets.",
      "title": "Product Set Id"
    },
    "limit": {
      "default": 50,
      "description": "Maximum number of products to return (default 50, max 100).",
      "title": "Limit",
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
      "description": "Meta ad account ID. If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "required": [
    "catalog_id"
  ],
  "title": "ListMetaProductsInput",
  "type": "object"
}
```

</details>

<a id="list_meta_promotable_apps"></a>

## `list_meta_promotable_apps`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to run a Meta app-install / app-promotion campaign, or asks which mobile apps they can advertise.

Returns the apps this ad account is allowed to promote, each with its numeric Facebook App ID and the App Store / Google Play URLs Meta already holds.

ALWAYS call this BEFORE creating an OUTCOME_APP_PROMOTION campaign. The `app_id` Meta requires is the numeric FACEBOOK App ID — NOT an iOS bundle ID (com.example.app) or Android package name. Customers routinely guess it wrong and the campaign fails.

Workflow:
1. Call this tool to discover promotable apps
2. Pass the returned `app_id` + matching `app_store_url` to a campaign creation tool with objective OUTCOME_APP_PROMOTION
3. OS targeting is derived from the store URL automatically — Meta rejects an ad set whose OS targeting disagrees with the promoted app

When to use:
- Before ANY app campaign creation (app_id + app_store_url are both required)
- When the user asks "which apps can I advertise?"
- When an app campaign failed with a promoted-object, app-setup, or "Mobile Targeting Mismatch" error

Apps that have no App Store / Google Play listing are returned separately with an explanation — Meta cannot run an app campaign for a web-only or canvas app.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing apps this ad account can promote (#977).",
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
      "description": "Meta ad account ID (e.g., 'act_123456'). If not provided, uses the connected account.",
      "title": "Ad Account Id"
    }
  },
  "title": "ListMetaPromotableAppsInput",
  "type": "object"
}
```

</details>

<a id="list_negative_keyword_lists"></a>

## `list_negative_keyword_lists`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List the account's SHARED negative keyword lists.

⚠️ READ-ONLY. Safe to call repeatedly.

A shared negative keyword list (Google "negative keyword list" / SharedSet) is a
reusable set of negative keywords you can attach to many campaigns at once —
unlike `add_negative_keywords` which adds negatives to ONE campaign only. This
lists each list with its keyword count and how many campaigns it's attached to.

**Use when:** "show my negative keyword lists", "what shared negative lists do I
have?", before adding to or attaching a list.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "List the account's shared negative keyword lists.",
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
  "title": "ListNegativeKeywordListsInput",
  "type": "object"
}
```

</details>

<a id="list_pmax_asset_group_assets"></a>

## `list_pmax_asset_group_assets`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List the TEXT and VIDEO assets on a Performance Max campaign's asset groups.

Complements list_pmax_asset_group_images (which covers images). Shows per
group: headlines, long headlines, descriptions, business name, and YouTube
videos — each with its field_type, status, performance_label, and the
`asset_group_asset_resource_name` to pass to remove_pmax_asset_group_asset.

**Parameters:**
- campaign_id: The PMax campaign ID (REQUIRED)
- asset_group_id: Optional — scope to one group
- field_types: Optional list to filter (e.g. ["HEADLINE"])
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 1-3 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing text/video assets on PMax asset groups.",
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
    "field_types": {
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
      "description": "Optional filter, any of HEADLINE, LONG_HEADLINE, DESCRIPTION, BUSINESS_NAME, YOUTUBE_VIDEO. Omit for all.",
      "title": "Field Types"
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
  "title": "ListPMaxAssetGroupAssetsInput",
  "type": "object"
}
```

</details>

<a id="list_pmax_asset_group_images"></a>

## `list_pmax_asset_group_images`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

List image assets linked to Performance Max asset groups, grouped by asset_group_id.

Returns image URL, dimensions, field_type, status, performance_label, and the
`asset_group_asset_resource_name` you can pass straight back to
`remove_pmax_asset_group_image`.

**Use when:**
- Auditing what creative is actually serving on a PMax campaign
- Capturing resource names before a remove
- Confirming `add_pmax_asset_group_image` succeeded

**Parameters:**
- campaign_id: The PMax campaign ID
- asset_group_id: Optional — scope to one group

**Execution time:** 1-3 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for listing images linked to PMax asset groups.",
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
      "description": "Optional — scope to one asset group. Omit to list every group in the campaign.",
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
    "campaign_id"
  ],
  "title": "ListPMaxAssetGroupImagesInput",
  "type": "object"
}
```

</details>

<a id="optimize_budget_allocation"></a>

## `optimize_budget_allocation`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Optimize budget allocation across campaigns using linear programming to maximize conversions.

⚠️ IMPORTANT: This tool retrieves READ-ONLY optimization recommendations. Safe to call multiple times. Does NOT automatically change budgets.

🎯 **What This Tool Does (Performance Agent - Phase 1):**
- Uses linear programming to optimize budget distribution
- Maximizes total conversions while respecting constraints
- Provides current vs optimized allocation comparison
- Categorizes campaigns into actions: PAUSE/SCALE/REDUCE/MAINTAIN
- Shows expected conversion lift from optimization
- Generates specific recommendations with budget amounts

**Returns detailed optimization plan:**
- Current allocation (what you have now)
- Optimized allocation (what you should have)
- Expected conversion lift (absolute and percentage)
- Campaign-by-campaign actions with reasoning
- Budget change amounts and percentages
- Specific implementation recommendations

**Optimization Algorithm:**
Uses scipy linear programming with constraints:
1. Sum of budgets = total_budget (you don't overspend)
2. Only campaigns with ROAS >= target get significant budget
3. Min budget per campaign >= min_daily_budget (or $0 to pause)
4. Max change per campaign <= ±max_change_percentage (avoid drastic shifts)

**Target ROAS Resolution (3-tier priority):**
1. User override (if target_roas parameter provided)
2. Account goals table (user-set or API-pulled)
3. 90-day historical average ROAS
4. Default to 1.0x (breakeven) if no data

**Configuration Parameters:**
- **total_budget**: Total monthly budget to allocate (REQUIRED)
- **lookback_days**: 7, 30, 60, 90, or 120 days (default: 30)
- **start_date**: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- **end_date**: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
- **target_roas**: Optional override (e.g., 3.0 for 3.0x)
- **max_change_percentage**: 0.0-1.0 (default: 0.5 = ±50%)
  * 0.3 = Conservative (±30% change, minimal disruption)
  * 0.5 = Balanced (±50% change, standard optimization)
  * 0.7 = Aggressive (±70% change, fast scaling)
- **min_daily_budget**: Minimum $ per campaign (default: $5.00, or $0.00 to allow pausing)
- **customer_id**: Optional (uses connected account if omitted)

**Execution time:** 1-5 seconds (depends on campaign count)
**Data source:** campaign_daily_metrics table (updated nightly)

**Use this tool when:**
- User wants to optimize budget allocation
- User asks "how should I allocate my budget?"
- User wants to maximize conversions with current spend
- User wants data-driven budget recommendations
- After running wasted spend analysis (natural next step)



<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for budget allocation optimization",
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
    "total_budget": {
      "description": "Total monthly budget to allocate across campaigns (e.g., 15000.00 for $15K/month)",
      "title": "Total Budget",
      "type": "number"
    },
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze for historical performance (7, 30, 60, 90, or 120 days). Default is 30 days.",
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
    "max_change_percentage": {
      "default": 0.5,
      "description": "Maximum budget change per campaign as a percentage (0.0-1.0). Default 0.5 = ±50%. Use 0.3 for conservative, 0.7 for aggressive.",
      "title": "Max Change Percentage",
      "type": "number"
    },
    "min_daily_budget": {
      "default": 5.0,
      "description": "Minimum daily budget per campaign in dollars. Default is $5.00. Set to 0.0 to allow complete pausing of underperformers.",
      "title": "Min Daily Budget",
      "type": "number"
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
    "total_budget"
  ],
  "title": "BudgetOptimizationInput",
  "type": "object"
}
```

</details>

<a id="optimize_meta_budget"></a>

## `optimize_meta_budget`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks about Meta/Facebook/Instagram budget optimization, reallocating ad spend, maximizing conversions with their budget, or wants data-driven budget recommendations.

This tool uses linear programming (scipy.optimize) to find the optimal budget allocation across Meta Ads campaigns or ad sets to maximize conversions while respecting constraints.

Returns:
- Optimal budget allocation for each campaign/ad set
- Expected conversion lift from reallocation
- Campaigns to scale up (high ROAS performers)
- Campaigns to reduce (below target ROAS)
- Campaigns to consider pausing (ROAS < 1.0)
- Actionable recommendations
- CBO (Campaign Budget Optimization) notes

When to use this tool:
- "How should I allocate my Meta budget?"
- "Optimize my Facebook ad spend for conversions"
- "Which Instagram campaigns should I increase budget?"
- "Reallocate my $5000 Meta budget"
- "Maximize conversions with my current spend"
- "What's the optimal budget split across campaigns?"

Parameters:
- total_budget: **REQUIRED.** Total budget to allocate across campaigns/ad sets in the account's own currency as a decimal — NOT cents, NOT USD (e.g., 5000.00). Must be > 0 — this is the pool that gets redistributed. Without it the tool has nothing to optimize and returns a validation error.
- lookback_days: 7, 14, 30 (default), 60, or 90 days for analysis
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- target_roas: Optional override (default: from account goals or 2.0x)
- max_change_percentage: Max budget change per item (default: 0.5 = 50%)
- min_daily_budget: Minimum budget per item (default: 5.00)
- optimization_level: 'campaign' (default) or 'ad_set'
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 2-5 seconds (cached database query + optimization)
Data source: campaign_daily_metrics + ad_group_daily_metrics tables

Key concepts:
- Linear Programming: Mathematical optimization to maximize objective (conversions) subject to constraints
- Efficiency Score: Conversions per dollar spent - used to prioritize allocation
- Max Change Constraint: Prevents dramatic shifts (e.g., ±50% max from current)
- Target ROAS: 3-tier resolution: account_goals - 90-day historical - default 2.0x

Meta-specific considerations:
- CBO campaigns: Budget set at campaign level, Meta distributes to ad sets
- ABO campaigns: Budget set at ad set level, more granular control
- Learning Phase: New campaigns need 50+ conversions before optimization

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta budget allocation optimization",
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
    "total_budget": {
      "description": "**REQUIRED.** Total monthly budget to allocate across campaigns, in the ad account's OWN CURRENCY as a decimal — NOT cents, NOT USD (e.g. 5000.00). This is the pool that gets redistributed across your campaigns or ad sets. Must be > 0. Do NOT call this tool without total_budget — there's nothing to optimize. If you want a recommendation based on existing spend, fetch current campaign spend via get_meta_campaign_performance first, sum it, and pass that as total_budget.",
      "exclusiveMinimum": 0,
      "title": "Total Budget",
      "type": "number"
    },
    "lookback_days": {
      "default": 30,
      "description": "Number of days to analyze for historical performance (7, 30, 60, 90, or 120 days). Default is 30 days.",
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
      "description": "Optional target ROAS override (e.g., 2.0 for 2.0x ROAS). If not provided, will use account goals or historical average.",
      "title": "Target Roas"
    },
    "max_change_percentage": {
      "default": 0.5,
      "description": "Maximum allowed budget change per campaign as decimal (0.3 for ±30%, 0.5 for ±50%, 0.7 for ±70%). Default is 0.5.",
      "title": "Max Change Percentage",
      "type": "number"
    },
    "min_daily_budget": {
      "default": 5.0,
      "description": "Minimum daily budget per campaign in the ad account's OWN CURRENCY as a decimal — NOT cents, NOT USD. Default is 5.00.",
      "title": "Min Daily Budget",
      "type": "number"
    },
    "optimization_level": {
      "default": "campaign",
      "description": "Level of optimization: 'campaign' (default) or 'ad_set'. Note: Ad set optimization may not apply to CBO-enabled campaigns.",
      "title": "Optimization Level",
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
    "total_budget"
  ],
  "title": "MetaBudgetOptimizeInput",
  "type": "object"
}
```

</details>

<a id="optimize_meta_placements"></a>

## `optimize_meta_placements`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User asks about Meta/Facebook/Instagram placement performance, which placements work best, Feed vs Stories vs Reels, should they use Audience Network, or wants placement optimization recommendations.

This tool analyzes placement-level performance (Feed, Stories, Reels, Audience Network, Messenger, etc.) and provides optimization recommendations including budget reallocation suggestions.

Returns:
- Placement ROAS ranking (sorted by performance)
- Placements categorized as SCALE/MAINTAIN/REDUCE/EXCLUDE
- Budget reallocation recommendations between placements
- Expected ROAS improvement from optimization
- Optimal placement mix for campaign objective
- Savings from excluding underperforming placements
- Actionable recommendations and quick actions

When to use this tool:
- "Which Meta placements should I use?"
- "Should I exclude Audience Network?"
- "Instagram Stories vs Reels - which is better?"
- "Feed vs Stories performance comparison"
- "Where should I allocate my Meta ad budget?"
- "Which placements are wasting money?"
- "What's the optimal placement mix for conversions?"
- "Facebook Marketplace performance?"

Parameters:
- lookback_days: 7, 14, 30 (default), 60, or 90 days
- date_range: preset alternative to lookback_days / start_date / end_date. One of: 'last_7_days', 'last_14_days', 'last_30_days', 'last_60_days', 'last_90_days'. (Both 'last_30_days' and 'last_30d' / 'last_month' aliases accepted.)
- start_date: Optional start date (YYYY-MM-DD). Overrides lookback_days when used with end_date.
- end_date: Optional end date (YYYY-MM-DD). Overrides lookback_days when used with start_date.
⚠️ DATE CLARIFICATION: If the user's date request is vague or ambiguous (e.g., "March to June" without a year, "last quarter", "recently", "a few months ago"), ask the user to specify exact dates before calling this tool. Do not assume or guess dates.
- objective: 'conversions' (default), 'traffic', or 'awareness' - for optimal mix recommendations
- target_roas: Optional override (default: from account goals or 2.0x)
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 2-5 seconds (cached database query with analysis)
Data source: meta_placement_daily_metrics table (placement-level daily metrics)

ROAS Thresholds for Recommendations:
- ✅ SCALE (ROAS ≥3.0x): Increase budget by 20-30%
- ➖ MAINTAIN (ROAS 1.5-3.0x): Keep current budget
- ⚠️ REDUCE (ROAS 1.0-1.5x): Reduce budget by 30-50%
- 🔴 EXCLUDE (ROAS <1.0x): Remove from campaigns

Meta Placements Analyzed:
- Facebook: Feed, Stories, Reels, Marketplace, Search Results
- Instagram: Feed, Stories, Reels, Explore
- Messenger: Inbox, Stories
- Audience Network: All placements

Common Insights:
- Audience Network often has lowest ROAS for conversion campaigns - consider excluding
- Instagram Feed and Reels typically have highest conversion rates
- Stories are great for awareness but may have lower conversion rates
- Facebook Marketplace can be effective for e-commerce

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta placement optimization analysis",
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
    "objective": {
      "default": "conversions",
      "description": "Campaign objective for optimal placement mix recommendations: 'conversions' (default), 'traffic', or 'awareness'.",
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
  "title": "MetaPlacementOptimizeInput",
  "type": "object"
}
```

</details>

<a id="pause_ad"></a>

## `pause_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Pause an ad to stop it from showing.

This is REVERSIBLE using resume_ad.

**Parameters:**
- ad_id: The ad ID to pause (REQUIRED)
- ad_group_id: The ad group ID (REQUIRED)
- customer_id: Optional

**Execution time:** 1-2 seconds

**When to use:**
- User says "pause this ad", "stop this ad"
- User wants to A/B test by pausing one ad
- Ad is underperforming and needs a break
- Making changes before re-enabling

**Example:**
User: "Pause my underperforming ad"
Agent:
1. Uses get_campaign_structure to find ad_id and ad_group_id
2. Uses pause_ad to stop the ad

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for pausing an ad",
  "properties": {
    "ad_id": {
      "description": "The ad ID to pause. Get from get_campaign_structure.",
      "title": "Ad Id",
      "type": "string"
    },
    "ad_group_id": {
      "description": "The ad group ID the ad belongs to. Get from get_campaign_structure.",
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
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_id",
    "ad_group_id"
  ],
  "title": "PauseAdInput",
  "type": "object"
}
```

</details>

<a id="pause_ad_group"></a>

## `pause_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Pause an ad group so none of its ads serve.

Works on ad groups of any channel — Search, Display, PMax, Demand Gen, YouTube.
This is REVERSIBLE using resume_ad_group.

**Parameters:**
- ad_group_id: The ad group ID to pause (REQUIRED)
- customer_id: Optional

**Execution time:** 1-2 seconds

**When to use:**
- User wants to pause an entire ad group while keeping its sibling ad groups running
- New build SOPs that require ad groups to start PAUSED until launch (PMax/Search SOPs)
- Temporarily silencing a themed ad group without removing it

**Note:**
This is the ad-group-level counterpart to `pause_ad` (ad-level) and `pause_campaign`
(campaign-level). Unlike `update_display_ad_group`, this works for Search ad groups too.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for pausing an ad group (any channel including Search).",
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID to pause. Get from get_campaign_structure or list_ad_groups. Works on Search, Display, PMax, Demand Gen, and YouTube ad groups — unlike update_display_ad_group, which is Display-only.",
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
      "description": "Google Ads customer ID. Required for multi-account users. Get from get_connections_status.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id"
  ],
  "title": "PauseAdGroupInput",
  "type": "object"
}
```

</details>

<a id="pause_campaign"></a>

## `pause_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Quickly pause a running campaign.

Pausing a campaign stops all ads from showing immediately.
This is REVERSIBLE using resume_campaign.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED - get from list_campaigns)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 1-2 seconds

**Returns:**
- Campaign name
- Before status (e.g., ENABLED)
- After status (PAUSED)
- Confirmation message

**When to use:**
- User says "pause the campaign", "stop the ads", "turn it off"
- User wants to temporarily stop spending
- User needs to make changes before ads continue

**Example:**
User: "Pause my summer sale campaign"
Agent: Uses pause_campaign with the campaign_id

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for pausing a campaign",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to pause. Use list_campaigns first to get available campaign IDs.",
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
  "title": "PauseCampaignInput",
  "type": "object"
}
```

</details>

<a id="pause_meta_campaign"></a>

## `pause_meta_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to pause a running Meta campaign.

IMPORTANT: Pausing a campaign stops all ad delivery immediately. No more budget will be spent until resumed.

Returns:
- Confirmation that campaign is paused
- Campaign details
- Ads Manager URL

When to use this tool:
- "Pause my Meta campaign"
- "Stop my Facebook ads"
- "Pause campaign 123456"
- "Turn off my Instagram campaign"

Parameters:
- campaign_id: The Meta Campaign ID to pause (required)

Execution time: 2-5 seconds
Effect: Campaign status changes to PAUSED immediately

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for pausing a Meta campaign",
  "properties": {
    "campaign_id": {
      "description": "The Meta Campaign ID to pause (required)",
      "title": "Campaign Id",
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
  "title": "PauseMetaCampaignInput",
  "type": "object"
}
```

</details>

<a id="remove_ad"></a>

## `remove_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove (soft-delete) an ad — sets status=REMOVED.

⚠️ **This is PERMANENT.** REMOVED ads cannot be re-enabled. To temporarily stop an ad,
use pause_ad instead.

Works on ads of any channel.

**Required:** ad_group_id + ad_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Soft-delete ANY ad (status=REMOVED). Irreversible.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID that contains the ad.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "ad_id": {
      "description": "Ad ID to remove (from get_ad_creative / get_campaign_structure).",
      "title": "Ad Id",
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
    "ad_group_id",
    "ad_id"
  ],
  "title": "RemoveAdInput",
  "type": "object"
}
```

</details>

<a id="remove_ad_group"></a>

## `remove_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove (soft-delete) an ad group — sets status=REMOVED.

⚠️ **This is PERMANENT.** Google has no hard delete and REMOVED ad groups cannot be
re-enabled. To temporarily stop an ad group, use pause_ad_group instead.

Works on ad groups of any channel (Search, Display, PMax, Demand Gen, YouTube).

**Required:** ad_group_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Soft-delete ANY ad group (status=REMOVED). Irreversible.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID to remove.",
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
  "title": "RemoveAdGroupInput",
  "type": "object"
}
```

</details>

<a id="remove_app_ad_asset"></a>

## `remove_app_ad_asset`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove an image or video asset from an App (UAC) ad.

**Parameters:**
- ad_id (REQUIRED), ad_group_id (REQUIRED).
- asset_type (REQUIRED): 'image' or 'video'.
- asset_resource_name (customers/<cid>/assets/<id>) OR asset_id (numeric) — which asset to drop.
  Get the app ad's current assets from get_ad_creative.
- customer_id: Optional.

**Execution time:** 2-4 seconds.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing an image or video asset from an App (UAC) ad.",
  "properties": {
    "ad_id": {
      "description": "The App ad ID.",
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
    "asset_resource_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "The asset resource name to remove (customers/<cid>/assets/<id>). Provide this OR asset_id. Get current assets from get_ad_creative.",
      "title": "Asset Resource Name"
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
      "description": "The numeric asset id to remove (alternative to asset_resource_name).",
      "title": "Asset Id"
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
  "title": "RemoveAppAdAssetInput",
  "type": "object"
}
```

</details>

<a id="remove_asset_group_listing_filter"></a>

## `remove_asset_group_listing_filter`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove a listing-filter node (and its whole subtree) from a retail-PMax asset group.

Get the filter_id from get_asset_group_listing_filters. Removing a subdivision removes everything
under it. Remove the root to return the asset group to promoting ALL feed products.

**Required:** asset_group_id, filter_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Remove a listing-filter node (and its subtree) from a retail-PMax asset group.",
  "properties": {
    "asset_group_id": {
      "description": "The retail-PMax asset group ID.",
      "title": "Asset Group Id",
      "type": "string"
    },
    "filter_id": {
      "description": "The listing-filter ID to remove (from get_asset_group_listing_filters).",
      "title": "Filter Id",
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
    "asset_group_id",
    "filter_id"
  ],
  "title": "RemoveAssetGroupListingFilterInput",
  "type": "object"
}
```

</details>

<a id="remove_call_assets"></a>

## `remove_call_assets`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove (unlink) phone (CALL) assets from a campaign.

Unlinks the CampaignAsset from THIS campaign only — the underlying asset stays
in the Asset Library and can be re-linked elsewhere. Use to clean up a
duplicate phone number.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED)
- asset_ids: Optional list of asset IDs / resource_names to unlink (get from
  list_call_assets). OMIT to unlink ALL call assets on the campaign.
- customer_id: Optional Google Ads customer ID

**Execution time:** 2-4 seconds

**Example:**
User: "Remove the duplicate phone number from this campaign"
Agent:
1. list_call_assets(campaign_id="19850524478") to get the asset IDs
2. remove_call_assets(campaign_id="19850524478", asset_ids=["411113414834"])

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing (unlinking) CALL assets from a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to remove call assets from. Use list_call_assets first to see what's there.",
      "title": "Campaign Id",
      "type": "string"
    },
    "asset_ids": {
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
      "description": "Optional list of asset IDs (or full resource_names) to unlink. Get IDs from list_call_assets. If omitted, ALL call assets on this campaign are unlinked (the underlying asset stays in the library).",
      "title": "Asset Ids"
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
  "title": "RemoveCallAssetsInput",
  "type": "object"
}
```

</details>

<a id="remove_callouts"></a>

## `remove_callouts`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove callout extensions from a campaign.

Unlinks callouts from THIS campaign. The underlying Asset stays in your account and can be re-linked elsewhere.

**Why this matters:**
- Old callouts containing words like "Doctor Reviewed" / "Medical" / "Clinical" can flag a campaign for policy issues
- Stale promotional callouts (e.g. "Summer Sale 2024") look bad to users
- Must remove old callouts before fresh ones take their place

**Parameters:**
- campaign_id: Campaign whose callouts to remove (REQUIRED)
- asset_ids: Optional list of asset IDs (or full resource_names) to remove specifically. Get IDs from `list_campaign_extensions`. If omitted, ALL callouts on this campaign are removed.
- customer_id: Optional (uses connected account if omitted)

**Workflow:**
1. Call `list_campaign_extensions(campaign_id)` to see what's currently linked
2. Identify which callouts to remove by their asset_id or text
3. Call this tool with those asset_ids (or omit to clear ALL)
4. Use `add_callout_extensions` to add fresh ones if needed

**Example:**
User: "Remove all my callouts and add new ones"
Agent:
1. Confirms: "I'll remove all 4 current callouts and let you add new ones. Proceed?"
2. Calls remove_callouts(campaign_id) — clears all
3. Then add_callout_extensions with new list

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing callout extensions from a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to remove callouts from. Use list_campaigns first to find campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "asset_ids": {
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
      "description": "Optional list of asset IDs (or full resource_names) to remove. Get IDs from list_campaign_extensions. If omitted, ALL callouts linked to this campaign are removed.",
      "title": "Asset Ids"
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
  "title": "RemoveCalloutsInput",
  "type": "object"
}
```

</details>

<a id="remove_campaign"></a>

## `remove_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Permanently remove (delete) a campaign — sets its status to REMOVED.

⚠️ This is PERMANENT and CANNOT be undone (a removed campaign cannot be re-enabled — use
pause_campaign if you only want to stop it temporarily). All of the campaign's ad groups and ads
are removed with it.

**Required:** campaign_id (from list_campaigns).

**When to use:** the user explicitly wants to delete / get rid of / permanently remove a campaign.
For "stop"/"turn off"/"pause", use pause_campaign instead.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing (permanently deleting) a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to remove. Use list_campaigns first to get available campaign IDs.",
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
  "title": "RemoveCampaignInput",
  "type": "object"
}
```

</details>

