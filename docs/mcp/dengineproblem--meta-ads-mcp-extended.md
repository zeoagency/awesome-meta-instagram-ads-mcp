# dengineproblem/meta-ads-mcp-extended

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/dengineproblem/meta-ads-mcp-extended) · [Machine-readable snapshot](../../catalog/dengineproblem--meta-ads-mcp-extended.json)

Complete registered tool snapshot. **59 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`e6f1517bca0b`](https://github.com/dengineproblem/meta-ads-mcp-extended/tree/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b). Method: `runtime-tools-list`.

- 59-tool union with optional registrations enabled; default configuration exposes 53. Optional tools are labeled below.
- generate_report is an upgrade stub, not reporting functionality. Some payloads are JSON-encoded strings exactly as registered.

## Tools

- [batch_request](#batch_request)
- [create_ad](#create_ad)
- [create_ad_creative](#create_ad_creative)
- [create_adset](#create_adset)
- [create_budget_schedule](#create_budget_schedule)
- [create_campaign](#create_campaign)
- [create_instagram_carousel](#create_instagram_carousel)
- [create_leadform_carousel](#create_leadform_carousel)
- [create_lookalike_audience](#create_lookalike_audience)
- [create_video_creative](#create_video_creative)
- [create_website_carousel](#create_website_carousel)
- [create_whatsapp_carousel](#create_whatsapp_carousel)
- [duplicate_ad](#duplicate_ad)
- [duplicate_adset](#duplicate_adset)
- [duplicate_campaign](#duplicate_campaign)
- [duplicate_creative](#duplicate_creative)
- [estimate_audience_size](#estimate_audience_size)
- [expand_to_stories](#expand_to_stories)
- [fetch](#fetch)
- [generate_creative_image](#generate_creative_image)
- [generate_report](#generate_report)
- [get_account_info](#get_account_info)
- [get_account_pages](#get_account_pages)
- [get_ad_accounts](#get_ad_accounts)
- [get_ad_creatives](#get_ad_creatives)
- [get_ad_details](#get_ad_details)
- [get_ad_image](#get_ad_image)
- [get_ads](#get_ads)
- [get_adset_details](#get_adset_details)
- [get_adsets](#get_adsets)
- [get_campaign_details](#get_campaign_details)
- [get_campaigns](#get_campaigns)
- [get_custom_audiences](#get_custom_audiences)
- [get_insights](#get_insights)
- [get_interest_suggestions](#get_interest_suggestions)
- [get_login_link](#get_login_link)
- [get_video_status](#get_video_status)
- [pause_ad](#pause_ad)
- [pause_adset](#pause_adset)
- [pause_campaign](#pause_campaign)
- [resume_ad](#resume_ad)
- [resume_adset](#resume_adset)
- [resume_campaign](#resume_campaign)
- [save_ad_image_locally](#save_ad_image_locally)
- [search](#search)
- [search_ads_archive](#search_ads_archive)
- [search_behaviors](#search_behaviors)
- [search_demographics](#search_demographics)
- [search_geo_locations](#search_geo_locations)
- [search_interests](#search_interests)
- [search_pages_by_name](#search_pages_by_name)
- [send_capi_event](#send_capi_event)
- [update_ad](#update_ad)
- [update_ad_creative](#update_ad_creative)
- [update_adset](#update_adset)
- [update_campaign](#update_campaign)
- [upload_ad_image](#upload_ad_image)
- [upload_video](#upload_video)
- [upscale_to_4k](#upscale_to_4k)

<a id="batch_request"></a>

## `batch_request`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/batch.py#L111)


    Execute multiple Graph API requests in a single call.

    This is highly efficient for operations like:
    - Getting insights for multiple campaigns/adsets/ads
    - Updating multiple objects at once
    - Bulk reading object details

    The batch API automatically handles:
    - Splitting requests into chunks of 50 (Meta API limit)
    - Retry with exponential backoff on rate limits
    - Parsing individual responses

    Args:
        access_token: Meta API access token
        requests: List of request objects, each containing:
            - method (str): HTTP method - "GET", "POST", or "DELETE"
            - relative_url (str): API endpoint path (e.g., "123456789/insights")
            - body (str, optional): URL-encoded body for POST requests
                                   (e.g., "status=PAUSED&name=New+Name")

    Returns:
        JSON response with results array containing success/error for each request

    Example:
        batch_request(
            access_token="...",
            requests=[
                {"method": "GET", "relative_url": "act_123/campaigns?fields=id,name"},
                {"method": "GET", "relative_url": "act_123/adsets?fields=id,name"},
                {"method": "POST", "relative_url": "123456789", "body": "status=PAUSED"}
            ]
        )
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "access_token": {
      "title": "Access Token",
      "type": "string"
    },
    "requests": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Requests",
      "type": "array"
    }
  },
  "required": [
    "access_token",
    "requests"
  ],
  "title": "batch_requestArguments",
  "type": "object"
}
```

</details>

<a id="create_ad"></a>

## `create_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L91)


    Create a new ad with an existing creative.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        name: Ad name
        adset_id: Ad set ID where this ad will be placed
        creative_id: ID of an existing creative to use
        status: Initial ad status (default: ACTIVE)
        bid_amount: Optional bid amount in account currency (in cents)
        tracking_specs: Optional tracking specifications (e.g., for pixel events).
                      Example: [{"action.type":"offsite_conversion","fb_pixel":["YOUR_PIXEL_ID"]}]
        access_token: Meta API access token (optional - will use cached token if not provided)

    Note:
        Dynamic Creative creatives require the parent ad set to have `is_dynamic_creative=true`.
        Otherwise, ad creation will fail with error_subcode 1885998.
    

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
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "creative_id": {
      "title": "Creative Id",
      "type": "string"
    },
    "status": {
      "default": "ACTIVE",
      "title": "Status",
      "type": "string"
    },
    "bid_amount": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Bid Amount"
    },
    "tracking_specs": {
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
      "title": "Tracking Specs"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "account_id",
    "name",
    "adset_id",
    "creative_id"
  ],
  "title": "create_adArguments",
  "type": "object"
}
```

</details>

<a id="create_ad_creative"></a>

## `create_ad_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L802)


    Create a new ad creative using an uploaded image hash.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        image_hash: Hash of the uploaded image
        access_token: Meta API access token (optional - will use cached token if not provided)
        name: Creative name
        page_id: Facebook Page ID to be used for the ad
        link_url: Destination URL for the ad
        message: Ad copy/text
        headline: Single headline for simple ads (cannot be used with headlines)
        headlines: List of headlines for dynamic creative testing (cannot be used with headline)
        description: Single description for simple ads (cannot be used with descriptions)
        descriptions: List of descriptions for dynamic creative testing (cannot be used with description)
        dynamic_creative_spec: Dynamic creative optimization settings
        call_to_action_type: Call to action button type (e.g., 'LEARN_MORE', 'SIGN_UP', 'SHOP_NOW', 'WHATSAPP_MESSAGE')
        lead_gen_form_id: Lead generation form ID for lead generation campaigns. Required when using
                         lead generation CTAs like 'SIGN_UP', 'GET_OFFER', 'SUBSCRIBE', etc.
        instagram_actor_id: Optional Instagram account ID for Instagram placements
        whatsapp_phone_number: WhatsApp phone number without + (e.g., '77077707066') for WHATSAPP_MESSAGE CTA
        client_question: Pre-filled message user sends to WhatsApp (for WHATSAPP_MESSAGE campaigns)
        url_tags: UTM parameters to append to destination URL (e.g., 'utm_source=facebook&utm_medium=cpc')
        instagram_username: Instagram username (without @) for auto-generating Instagram profile URL as link_url

    Returns:
        JSON response with created creative details
    

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
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
    },
    "link_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Link Url"
    },
    "message": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Message"
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
      "title": "Headlines"
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
      "title": "Descriptions"
    },
    "dynamic_creative_spec": {
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
      "title": "Dynamic Creative Spec"
    },
    "call_to_action_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Call To Action Type"
    },
    "lead_gen_form_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lead Gen Form Id"
    },
    "instagram_actor_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram Actor Id"
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
      "title": "Whatsapp Phone Number"
    },
    "client_question": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Client Question"
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
      "title": "Url Tags"
    },
    "instagram_username": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram Username"
    }
  },
  "required": [
    "account_id",
    "image_hash"
  ],
  "title": "create_ad_creativeArguments",
  "type": "object"
}
```

</details>

<a id="create_adset"></a>

## `create_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/adsets.py#L109)


    Create a new ad set in a Meta Ads account.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        campaign_id: Meta Ads campaign ID this ad set belongs to
        name: Ad set name
        optimization_goal: Conversion optimization goal. Values:
                          - 'OFFSITE_CONVERSIONS': Site Leads (pixel-based) or WhatsApp Conversions
                          - 'LEAD_GENERATION': Lead Forms (instant forms)
                          - 'CONVERSATIONS': WhatsApp/Messenger chat
                          - 'LINK_CLICKS': Instagram Traffic (with page_id) or Website Traffic
                          - 'APP_INSTALLS': Mobile app campaigns
        billing_event: How you're charged (e.g., 'IMPRESSIONS', 'LINK_CLICKS')
        status: Initial ad set status (default: ACTIVE)
        daily_budget: Daily budget in account currency (in cents)
        lifetime_budget: Lifetime budget in account currency (in cents)
        targeting: Targeting specifications including age, location, interests, etc.
                  Use targeting_automation.advantage_audience=1 for automatic audience finding
        bid_amount: Bid amount in account currency (in cents)
        bid_strategy: Bid strategy (e.g., 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP')
        start_time: Start time in ISO 8601 format (e.g., '2023-12-01T12:00:00-0800')
        end_time: End time in ISO 8601 format
        dsa_beneficiary: DSA beneficiary (person/organization benefiting from ads) for European compliance
        promoted_object: Configuration for campaigns with conversion tracking.
                        For APP_INSTALLS: {"application_id": "...", "object_store_url": "..."}
                        For OFFSITE_CONVERSIONS (Site Leads): {"pixel_id": "...", "custom_event_type": "LEAD"}
                        For OFFSITE_CONVERSIONS (WhatsApp Conv): {"pixel_id": "...", "custom_event_type": "...", "page_id": "..."}
                        For LINK_CLICKS (Instagram Traffic): {"page_id": "..."} (no link = Instagram profile)
                        For LEAD_GENERATION: {"page_id": "..."}
        destination_type: Where users are directed. Auto-set based on optimization_goal if not provided.
                          - 'WEBSITE': Site Leads (OFFSITE_CONVERSIONS)
                          - 'ON_AD': Lead Forms (LEAD_GENERATION)
                          - 'WHATSAPP': WhatsApp campaigns (CONVERSATIONS or WhatsApp Conversions)
                          - 'INSTAGRAM_PROFILE': Instagram traffic
                          - 'APP_STORE', 'DEEPLINK': Mobile app campaigns
        is_dynamic_creative: Enable Dynamic Creative for this ad set.
        validate_only: If True, validate parameters and return preview without creating ad set (dry-run mode).
        access_token: Meta API access token (optional - will use cached token if not provided)
    

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
      "title": "Billing Event",
      "type": "string"
    },
    "status": {
      "default": "ACTIVE",
      "title": "Status",
      "type": "string"
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "integer"
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
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lifetime Budget"
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
      "title": "Targeting"
    },
    "bid_amount": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
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
      "title": "Bid Strategy"
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
      "title": "Dsa Beneficiary"
    },
    "promoted_object": {
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
      "title": "Promoted Object"
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
      "title": "Destination Type"
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
      "title": "Is Dynamic Creative"
    },
    "validate_only": {
      "default": false,
      "title": "Validate Only",
      "type": "boolean"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "account_id",
    "campaign_id",
    "name",
    "optimization_goal",
    "billing_event"
  ],
  "title": "create_adsetArguments",
  "type": "object"
}
```

</details>

<a id="create_budget_schedule"></a>

## `create_budget_schedule`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/budget_schedules.py#L13)


    Create a budget schedule for a Meta Ads campaign.

    Allows scheduling budget increases based on anticipated high-demand periods.
    The times should be provided as Unix timestamps.
    
    Args:
        campaign_id: Meta Ads campaign ID.
        budget_value: Amount of budget increase. Interpreted based on budget_value_type.
        budget_value_type: Type of budget value - "ABSOLUTE" or "MULTIPLIER".
        time_start: Unix timestamp for when the high demand period should start.
        time_end: Unix timestamp for when the high demand period should end.
        access_token: Meta API access token (optional - will use cached token if not provided).
        
    Returns:
        A JSON string containing the ID of the created budget schedule or an error message.
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "budget_value": {
      "title": "Budget Value",
      "type": "integer"
    },
    "budget_value_type": {
      "title": "Budget Value Type",
      "type": "string"
    },
    "time_start": {
      "title": "Time Start",
      "type": "integer"
    },
    "time_end": {
      "title": "Time End",
      "type": "integer"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "campaign_id",
    "budget_value",
    "budget_value_type",
    "time_start",
    "time_end"
  ],
  "title": "create_budget_scheduleArguments",
  "type": "object"
}
```

</details>

<a id="create_campaign"></a>

## `create_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/campaigns.py#L116)


    Create a new campaign in a Meta Ads account.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        name: Campaign name
        objective: Campaign objective (ODAX, outcome-based). Must be one of:
                   OUTCOME_AWARENESS, OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT,
                   OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_APP_PROMOTION.
                   Note: Legacy objectives like BRAND_AWARENESS, LINK_CLICKS,
                   CONVERSIONS, APP_INSTALLS, etc. are not valid for new
                   campaigns and will cause a 400 error. Use the outcome-based
                   values above (e.g., BRAND_AWARENESS → OUTCOME_AWARENESS).
        access_token: Meta API access token (optional - will use cached token if not provided)
        status: Initial campaign status (default: PAUSED)
        special_ad_categories: List of special ad categories if applicable
        daily_budget: Daily budget in account currency (in cents) as a string (only used if use_adset_level_budgets=False)
        lifetime_budget: Lifetime budget in account currency (in cents) as a string (only used if use_adset_level_budgets=False)
        buying_type: Buying type (e.g., 'AUCTION')
        bid_strategy: Bid strategy. Must be one of: 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'.
        bid_cap: Bid cap in account currency (in cents) as a string
        spend_cap: Spending limit for the campaign in account currency (in cents) as a string
        campaign_budget_optimization: Whether to enable campaign budget optimization (only used if use_adset_level_budgets=False)
        ab_test_control_setups: Settings for A/B testing (e.g., [{"name":"Creative A", "ad_format":"SINGLE_IMAGE"}])
        use_adset_level_budgets: If True, budgets will be set at the ad set level instead of campaign level (default: False)
    

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
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "status": {
      "default": "PAUSED",
      "title": "Status",
      "type": "string"
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
      "title": "Special Ad Categories"
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "integer"
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
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lifetime Budget"
    },
    "buying_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Buying Type"
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
      "title": "Bid Strategy"
    },
    "bid_cap": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Bid Cap"
    },
    "spend_cap": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Spend Cap"
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
      "default": null,
      "title": "Campaign Budget Optimization"
    },
    "ab_test_control_setups": {
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
      "title": "Ab Test Control Setups"
    },
    "use_adset_level_budgets": {
      "default": false,
      "title": "Use Adset Level Budgets",
      "type": "boolean"
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

<a id="create_instagram_carousel"></a>

## `create_instagram_carousel`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/carousel.py#L188)


    Create an Instagram carousel creative for engagement/traffic campaigns.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        cards: List of carousel cards. Each card should have:
            - image_hash (str): Hash of uploaded image
            - text (str): Card headline/name (max 50 chars)
            - link (str, optional): Card-specific destination URL
        page_id: Facebook Page ID associated with the ad
        instagram_id: Instagram account ID
        instagram_username: Instagram username (without @)
        message: Primary text/caption for the ad
        access_token: Meta API access token (optional)
        name: Creative name (auto-generated if not provided)

    Returns:
        JSON response with created creative ID
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "cards": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Cards",
      "type": "array"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "instagram_id": {
      "title": "Instagram Id",
      "type": "string"
    },
    "instagram_username": {
      "title": "Instagram Username",
      "type": "string"
    },
    "message": {
      "title": "Message",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
    "cards",
    "page_id",
    "instagram_id",
    "instagram_username",
    "message"
  ],
  "title": "create_instagram_carouselArguments",
  "type": "object"
}
```

</details>

<a id="create_leadform_carousel"></a>

## `create_leadform_carousel`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/carousel.py#L400)


    Create a lead generation carousel creative with instant form.

    When users click, they see a pre-filled lead form without leaving Facebook/Instagram.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        cards: List of carousel cards. Each card should have:
            - image_hash (str): Hash of uploaded image
            - text (str): Card headline/name (max 50 chars)
        page_id: Facebook Page ID associated with the ad
        message: Primary text/caption for the ad
        lead_form_id: ID of the lead generation form (created in Meta Business Suite)
        access_token: Meta API access token (optional)
        instagram_id: Instagram account ID for Instagram placements
        call_to_action: CTA button type. Common for lead gen: SIGN_UP, SUBSCRIBE,
                       GET_QUOTE, LEARN_MORE, APPLY_NOW, GET_OFFER
        name: Creative name (auto-generated if not provided)

    Returns:
        JSON response with created creative ID
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "cards": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Cards",
      "type": "array"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "message": {
      "title": "Message",
      "type": "string"
    },
    "lead_form_id": {
      "title": "Lead Form Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "instagram_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram Id"
    },
    "call_to_action": {
      "default": "SIGN_UP",
      "title": "Call To Action",
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
    "cards",
    "page_id",
    "message",
    "lead_form_id"
  ],
  "title": "create_leadform_carouselArguments",
  "type": "object"
}
```

</details>

<a id="create_lookalike_audience"></a>

## `create_lookalike_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/audiences.py#L13)


    Create a Lookalike Audience based on a seed Custom Audience.

    Lookalike Audiences help you reach new people who are similar to your
    existing customers or engaged users.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        seed_audience_id: ID of the source Custom Audience to base the lookalike on
                         (e.g., Instagram Engagers, Website Visitors, Customer List)
        country: Country code for the lookalike audience (e.g., 'US', 'KZ', 'RU', 'GB')
        access_token: Meta API access token (optional - will use cached token if not provided)
        ratio: Size of the lookalike audience as a percentage of the country's population.
               Valid range: 0.01 to 0.10 (1% to 10%). Default: 0.03 (3%)
               Smaller ratios = more similar to seed, larger = broader reach
        name: Optional custom name for the audience. If not provided, will auto-generate
              a name like "LAL 3% US - 2024-01-15"

    Returns:
        JSON response with the created audience ID and details

    Example:
        create_lookalike_audience(
            account_id="act_123456789",
            seed_audience_id="23842588888640185",
            country="US",
            ratio=0.03
        )
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "seed_audience_id": {
      "title": "Seed Audience Id",
      "type": "string"
    },
    "country": {
      "title": "Country",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "ratio": {
      "default": 0.03,
      "title": "Ratio",
      "type": "number"
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
    "seed_audience_id",
    "country"
  ],
  "title": "create_lookalike_audienceArguments",
  "type": "object"
}
```

</details>

<a id="create_video_creative"></a>

## `create_video_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L1061)


    Create a video ad creative for WhatsApp, Instagram, Website, or Lead Form campaigns.

    This function creates video creatives using object_story_spec with video_data structure.
    It supports multiple campaign types based on call_to_action_type:

    - WHATSAPP_MESSAGE: Click-to-WhatsApp campaigns (requires whatsapp_phone_number, client_question)
    - LEARN_MORE: Instagram/Website traffic or Lead Form campaigns
    - SIGN_UP: Website conversion campaigns

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        video_id: ID of the uploaded video (from upload_video)
        page_id: Facebook Page ID to be used for the ad
        access_token: Meta API access token (optional - will use cached token if not provided)
        name: Creative name (auto-generated if not provided)
        message: Ad copy/text shown above the video
        call_to_action_type: CTA button type. Common values:
            - 'WHATSAPP_MESSAGE' for Click-to-WhatsApp
            - 'LEARN_MORE' for traffic/lead gen campaigns
            - 'SIGN_UP' for website conversions
        link_url: Destination URL (for LEARN_MORE/SIGN_UP campaigns)
        whatsapp_phone_number: WhatsApp number without + (e.g., '77077707066') for WHATSAPP_MESSAGE
        client_question: Pre-filled message user sends to WhatsApp (for WHATSAPP_MESSAGE)
        lead_gen_form_id: Lead form ID for lead generation campaigns
        instagram_actor_id: Instagram account ID for Instagram placements
        thumbnail_hash: Optional image hash for video thumbnail
        thumbnail_url: Optional image URL for video thumbnail (auto-fetched from video if not provided)
        url_tags: UTM parameters to append to destination URL (e.g., 'utm_source=facebook&utm_medium=cpc')
        instagram_username: Instagram username (without @) for auto-generating Instagram profile URL as link_url

    Returns:
        JSON response with created creative ID and details

    Example (WhatsApp):
        create_video_creative(
            account_id="act_123456789",
            video_id="987654321",
            page_id="123456789",
            message="Напишите нам, чтобы узнать подробности",
            call_to_action_type="WHATSAPP_MESSAGE",
            whatsapp_phone_number="77077707066",
            client_question="Здравствуйте! Хочу узнать об этом подробнее."
        )

    Example (Lead Form):
        create_video_creative(
            account_id="act_123456789",
            video_id="987654321",
            page_id="123456789",
            message="Оставьте заявку",
            call_to_action_type="LEARN_MORE",
            lead_gen_form_id="123456789"
        )
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "video_id": {
      "title": "Video Id",
      "type": "string"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
    "message": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Message"
    },
    "call_to_action_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Call To Action Type"
    },
    "link_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Link Url"
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
      "title": "Whatsapp Phone Number"
    },
    "client_question": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Client Question"
    },
    "lead_gen_form_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lead Gen Form Id"
    },
    "instagram_actor_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram Actor Id"
    },
    "thumbnail_hash": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Thumbnail Hash"
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
      "title": "Thumbnail Url"
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
      "title": "Url Tags"
    },
    "instagram_username": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram Username"
    }
  },
  "required": [
    "account_id",
    "video_id",
    "page_id"
  ],
  "title": "create_video_creativeArguments",
  "type": "object"
}
```

</details>

<a id="create_website_carousel"></a>

## `create_website_carousel`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/carousel.py#L280)


    Create a website traffic carousel creative.

    Drives users to your website with multiple product/service cards.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        cards: List of carousel cards. Each card should have:
            - image_hash (str): Hash of uploaded image
            - text (str): Card headline/name (max 50 chars)
            - link (str, optional): Card-specific destination URL
            - description (str, optional): Card description
        page_id: Facebook Page ID associated with the ad
        message: Primary text/caption for the ad
        site_url: Main website URL (used as default for cards without specific links)
        access_token: Meta API access token (optional)
        instagram_id: Instagram account ID for Instagram placements
        utm: UTM parameters to append to URLs (e.g., "utm_source=facebook&utm_medium=cpc")
        call_to_action: CTA button type. Options: LEARN_MORE, SHOP_NOW, SIGN_UP,
                       BOOK_TRAVEL, CONTACT_US, DOWNLOAD, GET_OFFER, etc.
        name: Creative name (auto-generated if not provided)

    Returns:
        JSON response with created creative ID
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "cards": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Cards",
      "type": "array"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "message": {
      "title": "Message",
      "type": "string"
    },
    "site_url": {
      "title": "Site Url",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "instagram_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram Id"
    },
    "utm": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Utm"
    },
    "call_to_action": {
      "default": "LEARN_MORE",
      "title": "Call To Action",
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
    "cards",
    "page_id",
    "message",
    "site_url"
  ],
  "title": "create_website_carouselArguments",
  "type": "object"
}
```

</details>

<a id="create_whatsapp_carousel"></a>

## `create_whatsapp_carousel`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/carousel.py#L44)


    Create a WhatsApp Click-to-WhatsApp (CTWA) carousel creative.

    This creative type drives users to start a WhatsApp conversation
    with your business after clicking on the ad.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        cards: List of carousel cards. Each card should have:
            - image_hash (str): Hash of uploaded image
            - text (str): Card headline/name (max 50 chars)
            - link (str, optional): Card-specific link
        page_id: Facebook Page ID associated with the ad
        message: Primary text/caption for the ad
        client_question: Pre-filled message that user will send to WhatsApp
        access_token: Meta API access token (optional)
        instagram_id: Instagram account ID for Instagram placements
        whatsapp_phone: WhatsApp business phone number (format: +1234567890)
        name: Creative name (auto-generated if not provided)

    Returns:
        JSON response with created creative ID

    Example:
        create_whatsapp_carousel(
            account_id="act_123456789",
            cards=[
                {"image_hash": "abc123", "text": "Product 1"},
                {"image_hash": "def456", "text": "Product 2"}
            ],
            page_id="123456789",
            message="Check out our products!",
            client_question="Hi, I'm interested in your products"
        )
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "cards": {
      "items": {
        "additionalProperties": true,
        "type": "object"
      },
      "title": "Cards",
      "type": "array"
    },
    "page_id": {
      "title": "Page Id",
      "type": "string"
    },
    "message": {
      "title": "Message",
      "type": "string"
    },
    "client_question": {
      "title": "Client Question",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "instagram_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Instagram Id"
    },
    "whatsapp_phone": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Whatsapp Phone"
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
    "cards",
    "page_id",
    "message",
    "client_question"
  ],
  "title": "create_whatsapp_carouselArguments",
  "type": "object"
}
```

</details>

<a id="duplicate_ad"></a>

## `duplicate_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/duplication.py#L105)


        Duplicate a Meta Ads ad.

        Recommended: Use this to run robust experiments.
        
        Args:
            ad_id: Meta Ads ad ID to duplicate
            target_adset_id: Ad set ID to move the duplicated ad to (optional)
            name_suffix: Suffix to add to the duplicated ad name
            duplicate_creative: Whether to duplicate the ad creative
            new_creative_name: Override name for the duplicated creative
            new_status: Status for the new ad (ACTIVE or PAUSED)
        

Availability: Opt-in META_ADS_ENABLE_DUPLICATION.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "target_adset_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Target Adset Id"
    },
    "name_suffix": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": " - Copy",
      "title": "Name Suffix"
    },
    "duplicate_creative": {
      "default": true,
      "title": "Duplicate Creative",
      "type": "boolean"
    },
    "new_creative_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Creative Name"
    },
    "new_status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "PAUSED",
      "title": "New Status"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "duplicate_adArguments",
  "type": "object"
}
```

</details>

<a id="duplicate_adset"></a>

## `duplicate_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/duplication.py#L62)


        Duplicate a Meta Ads ad set with its ads.

        Recommended: Use this to run robust experiments.
        
        Args:
            adset_id: Meta Ads ad set ID to duplicate
            target_campaign_id: Campaign ID to move the duplicated ad set to (optional)
            name_suffix: Suffix to add to the duplicated ad set name
            include_ads: Whether to duplicate ads within the ad set
            include_creatives: Whether to duplicate ad creatives
            new_daily_budget: Override the daily budget for the new ad set
            new_targeting: Override targeting settings for the new ad set
            new_status: Status for the new ad set (ACTIVE or PAUSED)
        

Availability: Opt-in META_ADS_ENABLE_DUPLICATION.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "target_campaign_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Target Campaign Id"
    },
    "name_suffix": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": " - Copy",
      "title": "Name Suffix"
    },
    "include_ads": {
      "default": true,
      "title": "Include Ads",
      "type": "boolean"
    },
    "include_creatives": {
      "default": true,
      "title": "Include Creatives",
      "type": "boolean"
    },
    "new_daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Daily Budget"
    },
    "new_targeting": {
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
      "title": "New Targeting"
    },
    "new_status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "PAUSED",
      "title": "New Status"
    }
  },
  "required": [
    "adset_id"
  ],
  "title": "duplicate_adsetArguments",
  "type": "object"
}
```

</details>

<a id="duplicate_campaign"></a>

## `duplicate_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/duplication.py#L19)


        Duplicate a Meta Ads campaign with all its ad sets and ads.

        Recommended: Use this to run robust experiments.
        
        Args:
            campaign_id: Meta Ads campaign ID to duplicate
            name_suffix: Suffix to add to the duplicated campaign name
            include_ad_sets: Whether to duplicate ad sets within the campaign
            include_ads: Whether to duplicate ads within ad sets
            include_creatives: Whether to duplicate ad creatives
            copy_schedule: Whether to copy the campaign schedule
            new_daily_budget: Override the daily budget for the new campaign
            new_status: Status for the new campaign (ACTIVE or PAUSED)
        

Availability: Opt-in META_ADS_ENABLE_DUPLICATION.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "name_suffix": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": " - Copy",
      "title": "Name Suffix"
    },
    "include_ad_sets": {
      "default": true,
      "title": "Include Ad Sets",
      "type": "boolean"
    },
    "include_ads": {
      "default": true,
      "title": "Include Ads",
      "type": "boolean"
    },
    "include_creatives": {
      "default": true,
      "title": "Include Creatives",
      "type": "boolean"
    },
    "copy_schedule": {
      "default": false,
      "title": "Copy Schedule",
      "type": "boolean"
    },
    "new_daily_budget": {
      "anyOf": [
        {
          "type": "number"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Daily Budget"
    },
    "new_status": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "PAUSED",
      "title": "New Status"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "duplicate_campaignArguments",
  "type": "object"
}
```

</details>

<a id="duplicate_creative"></a>

## `duplicate_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/duplication.py#L142)


        Duplicate a Meta Ads creative.

        Recommended: Use this to run robust experiments.
        
        Args:
            creative_id: Meta Ads creative ID to duplicate
            name_suffix: Suffix to add to the duplicated creative name
            new_primary_text: Override the primary text for the new creative
            new_headline: Override the headline for the new creative
            new_description: Override the description for the new creative
            new_cta_type: Override the call-to-action type for the new creative
            new_destination_url: Override the destination URL for the new creative
        

Availability: Opt-in META_ADS_ENABLE_DUPLICATION.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "creative_id": {
      "title": "Creative Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "name_suffix": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": " - Copy",
      "title": "Name Suffix"
    },
    "new_primary_text": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Primary Text"
    },
    "new_headline": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Headline"
    },
    "new_description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Description"
    },
    "new_cta_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Cta Type"
    },
    "new_destination_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Destination Url"
    }
  },
  "required": [
    "creative_id"
  ],
  "title": "duplicate_creativeArguments",
  "type": "object"
}
```

</details>

<a id="estimate_audience_size"></a>

## `estimate_audience_size`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/targeting.py#L70)


    Estimate audience size for targeting specifications using Meta's delivery_estimate API.
    
    This function provides comprehensive audience estimation for complex targeting combinations
    including demographics, geography, interests, and behaviors. It also maintains backwards
    compatibility for simple interest validation.
    
    Args:
        access_token: Meta API access token (optional - will use cached token if not provided)
        account_id: Meta Ads account ID (format: act_XXXXXXXXX) - required for comprehensive estimation
        targeting: Complete targeting specification including demographics, geography, interests, etc.
                  Example: {
                      "age_min": 25,
                      "age_max": 65,
                      "geo_locations": {"countries": ["PL"]},
                      "flexible_spec": [
                          {"interests": [{"id": "6003371567474"}]},
                          {"interests": [{"id": "6003462346642"}]}
                      ]
                  }
        optimization_goal: Optimization goal for estimation (default: "REACH"). 
                          Options: "REACH", "LINK_CLICKS", "IMPRESSIONS", "CONVERSIONS", etc.
        interest_list: [DEPRECATED - for backwards compatibility] List of interest names to validate
        interest_fbid_list: [DEPRECATED - for backwards compatibility] List of interest IDs to validate
    
    Returns:
        JSON string with audience estimation results including estimated_audience_size,
        reach_estimate, and targeting validation
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
      "title": "Targeting"
    },
    "optimization_goal": {
      "default": "REACH",
      "title": "Optimization Goal",
      "type": "string"
    },
    "interest_list": {
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
      "title": "Interest List"
    },
    "interest_fbid_list": {
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
      "title": "Interest Fbid List"
    }
  },
  "title": "estimate_audience_sizeArguments",
  "type": "object"
}
```

</details>

<a id="expand_to_stories"></a>

## `expand_to_stories`

Scope: **supporting** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/creative_generation.py#L192)


    Expand a 4:5 image to 9:16 Stories format via seamless outpainting.

    The original image content stays in the center while the background
    is extended upward and downward seamlessly.

    Args:
        image_path: Path to the 4:5 source image
        output_path: Optional path for the output (default: {original}_stories.png)
        upscale_4k: If True, generate in 4K resolution (2160x3840)

    Returns:
        JSON with file_path to expanded 9:16 image

    Example:
        expand_to_stories(image_path="/path/to/creative_20240115_143022.png", upscale_4k=True)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "image_path": {
      "title": "Image Path",
      "type": "string"
    },
    "output_path": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Output Path"
    },
    "upscale_4k": {
      "default": false,
      "title": "Upscale 4K",
      "type": "boolean"
    }
  },
  "required": [
    "image_path"
  ],
  "title": "expand_to_storiesArguments",
  "type": "object"
}
```

</details>

<a id="fetch"></a>

## `fetch`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/openai_deep_research.py#L367)


    Fetch complete record data by ID.
    It retrieves the full data for a specific record identified by its ID.
    
    Args:
        id: The record ID to fetch (format: "type:id", e.g., "account:act_123456")
        
    Returns:
        JSON response with complete record data including id, title, text, and metadata
        
    Example Usage:
        fetch(id="account:act_123456789")
        fetch(id="campaign:23842588888640185")
        fetch(id="ad:23842614006130185")
        fetch(id="page:123456789")
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "id": {
      "title": "Id",
      "type": "string"
    }
  },
  "required": [
    "id"
  ],
  "title": "fetchArguments",
  "type": "object"
}
```

</details>

<a id="generate_creative_image"></a>

## `generate_creative_image`

Scope: **supporting** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/creative_generation.py#L64)


    Generate a 4:5 Instagram creative image with text overlay via Gemini.

    Args:
        prompt: Style prompt (colors, mood, objects, background)
        offer: Main headline (6-12 words)
        bullets: 3 bullet points separated by newlines
        profits: Benefit/bonus text
        cta: Call-to-action text (default: "Узнать больше")
        reference_image_path: Optional path to reference image for style
        output_dir: Optional output directory (default: current working directory)

    Returns:
        JSON with file_path to generated image

    Example:
        generate_creative_image(
            prompt="Современный минималистичный дизайн, синий градиент",
            offer="Похудей на 10 кг за месяц",
            bullets="• Без диет\n• Без тренировок\n• Результат за 30 дней",
            profits="Первая консультация бесплатно",
            cta="Записаться"
        )
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "prompt": {
      "title": "Prompt",
      "type": "string"
    },
    "offer": {
      "title": "Offer",
      "type": "string"
    },
    "bullets": {
      "title": "Bullets",
      "type": "string"
    },
    "profits": {
      "title": "Profits",
      "type": "string"
    },
    "cta": {
      "default": "Узнать больше",
      "title": "Cta",
      "type": "string"
    },
    "reference_image_path": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Reference Image Path"
    },
    "output_dir": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Output Dir"
    }
  },
  "required": [
    "prompt",
    "offer",
    "bullets",
    "profits"
  ],
  "title": "generate_creative_imageArguments",
  "type": "object"
}
```

</details>

<a id="generate_report"></a>

## `generate_report`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/reports.py#L15)


        Generate comprehensive Meta Ads performance reports.

        **This is a premium feature available with Pipeboard Pro.**
        
        Args:
            account_id: Meta Ads account ID (format: act_XXXXXXXXX)
            access_token: Meta API access token (optional - will use cached token if not provided)
            report_type: Type of report to generate (account, campaign, comparison)
            time_range: Time period for the report (e.g., 'last_30d', 'last_7d', 'this_month')
            campaign_ids: Specific campaign IDs (required for campaign/comparison reports)
            export_format: Output format for the report (pdf, json, html)
            report_name: Custom name for the report (auto-generated if not provided)
            include_sections: Specific sections to include in the report
            breakdowns: Audience breakdown dimensions (age, gender, country, etc.)
            comparison_period: Time period for comparison analysis
        

Availability: Opt-in META_ADS_ENABLE_REPORTS; implementation only returns a premium upgrade message.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "report_type": {
      "default": "account",
      "title": "Report Type",
      "type": "string"
    },
    "time_range": {
      "default": "last_30d",
      "title": "Time Range",
      "type": "string"
    },
    "campaign_ids": {
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
      "title": "Campaign Ids"
    },
    "export_format": {
      "default": "pdf",
      "title": "Export Format",
      "type": "string"
    },
    "report_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Report Name"
    },
    "include_sections": {
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
      "title": "Include Sections"
    },
    "breakdowns": {
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
      "title": "Breakdowns"
    },
    "comparison_period": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Comparison Period"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "generate_reportArguments",
  "type": "object"
}
```

</details>

<a id="get_account_info"></a>

## `get_account_info`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/accounts.py#L33)


    Get detailed information about a specific ad account.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L1620)


    Get pages associated with a Meta Ads account.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
    
    Returns:
        JSON response with pages associated with the account
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/accounts.py#L11)


    Get ad accounts accessible by a user.
    
    Args:
        access_token: Meta API access token (optional - will use cached token if not provided)
        user_id: Meta user ID or "me" for the current user
        limit: Maximum number of accounts to return (default: 200)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "user_id": {
      "default": "me",
      "title": "User Id",
      "type": "string"
    },
    "limit": {
      "default": 200,
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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L163)


    Get creative details for a specific ad. Best if combined with get_ad_image to get the full image.
    
    Args:
        ad_id: Meta Ads ad ID
        access_token: Meta API access token (optional - will use cached token if not provided)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "get_ad_creativesArguments",
  "type": "object"
}
```

</details>

<a id="get_ad_details"></a>

## `get_ad_details`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L68)


    Get detailed information about a specific ad.
    
    Args:
        ad_id: Meta Ads ad ID
        access_token: Meta API access token (optional - will use cached token if not provided)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L191)


    Get, download, and visualize a Meta ad image in one step. Useful to see the image in the LLM.
    
    Args:
        ad_id: Meta Ads ad ID
        access_token: Meta API access token (optional - will use cached token if not provided)
    
    Returns:
        The ad image ready for direct visual analysis
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "get_ad_imageArguments",
  "type": "object"
}
```

</details>

<a id="get_ads"></a>

## `get_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L23)


    Get ads for a Meta Ads account with optional filtering.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of ads to return (default: 10)
        campaign_id: Optional campaign ID to filter by
        adset_id: Optional ad set ID to filter by
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "limit": {
      "default": 10,
      "title": "Limit",
      "type": "integer"
    },
    "campaign_id": {
      "default": "",
      "title": "Campaign Id",
      "type": "string"
    },
    "adset_id": {
      "default": "",
      "title": "Adset Id",
      "type": "string"
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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/adsets.py#L73)


    Get detailed information about a specific ad set.
    
    Args:
        adset_id: Meta Ads ad set ID
        access_token: Meta API access token (optional - will use cached token if not provided)
    
    Example:
        To call this function through MCP, pass the adset_id as the first argument:
        {
            "args": "YOUR_ADSET_ID"
        }
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/adsets.py#L35)


    Get ad sets for a Meta Ads account with optional filtering by campaign.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of ad sets to return (default: 10)
        campaign_id: Optional campaign ID to filter by
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "limit": {
      "default": 10,
      "title": "Limit",
      "type": "integer"
    },
    "campaign_id": {
      "default": "",
      "title": "Campaign Id",
      "type": "string"
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

<a id="get_campaign_details"></a>

## `get_campaign_details`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/campaigns.py#L89)


    Get detailed information about a specific campaign.

    Note: This function requests a specific set of fields ('id,name,objective,status,...'). 
    The Meta API offers many other fields for campaigns (e.g., 'effective_status', 'source_campaign_id', etc.) 
    that could be added to the 'fields' parameter in the code if needed.
    
    Args:
        campaign_id: Meta Ads campaign ID
        access_token: Meta API access token (optional - will use cached token if not provided)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/campaigns.py#L12)


    Get campaigns for a Meta Ads account with optional filtering.
    
    Note: By default, the Meta API returns a subset of available fields. 
    Other fields like 'effective_status', 'special_ad_categories', 
    'lifetime_budget', 'spend_cap', 'budget_remaining', 'promoted_object', 
    'source_campaign_id', etc., might be available but require specifying them
    in the API call (currently not exposed by this tool's parameters).
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of campaigns to return (default: 10)
        status_filter: Filter by effective status (e.g., 'ACTIVE', 'PAUSED', 'ARCHIVED').
                       Maps to the 'effective_status' API parameter, which expects an array
                       (this function handles the required JSON formatting). Leave empty for all statuses.
        objective_filter: Filter by campaign objective(s). Can be a single objective string or a list of objectives.
                         Valid objectives: 'OUTCOME_AWARENESS', 'OUTCOME_TRAFFIC', 'OUTCOME_ENGAGEMENT',
                         'OUTCOME_LEADS', 'OUTCOME_SALES', 'OUTCOME_APP_PROMOTION'.
                         Examples: 'OUTCOME_LEADS' or ['OUTCOME_LEADS', 'OUTCOME_SALES'].
                         Leave empty for all objectives.
        after: Pagination cursor to get the next set of results
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "limit": {
      "default": 10,
      "title": "Limit",
      "type": "integer"
    },
    "status_filter": {
      "default": "",
      "title": "Status Filter",
      "type": "string"
    },
    "objective_filter": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      ],
      "default": "",
      "title": "Objective Filter"
    },
    "after": {
      "default": "",
      "title": "After",
      "type": "string"
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

<a id="get_custom_audiences"></a>

## `get_custom_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/audiences.py#L109)


    Get list of Custom Audiences for an ad account.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of audiences to return (default: 25)

    Returns:
        JSON response with list of custom audiences including id, name, subtype,
        approximate_count (audience size), and delivery_status
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "get_custom_audiencesArguments",
  "type": "object"
}
```

</details>

<a id="get_insights"></a>

## `get_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/insights.py#L14)


    Get performance insights for a campaign, ad set, ad or account.
    
    Args:
        object_id: ID of the campaign, ad set, ad or account
        access_token: Meta API access token (optional - will use cached token if not provided)
        time_range: Either a preset time range string or a dictionary with "since" and "until" dates in YYYY-MM-DD format
                   Preset options: today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, 
                   last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, 
                   last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year
                   Dictionary example: {"since":"2023-01-01","until":"2023-01-31"}
        breakdown: Optional breakdown dimension. Valid values include:
                   Demographic: age, gender, country, region, dma
                   Platform/Device: device_platform, platform_position, publisher_platform, impression_device
                   Creative Assets: ad_format_asset, body_asset, call_to_action_asset, description_asset, 
                                  image_asset, link_url_asset, title_asset, video_asset, media_asset_url,
                                  media_creator, media_destination_url, media_format, media_origin_url,
                                  media_text_content, media_type, creative_relaxation_asset_type,
                                  flexible_format_asset_type, gen_ai_asset_type
                   Campaign/Ad Attributes: breakdown_ad_objective, breakdown_reporting_ad_id, app_id, product_id
                   Conversion Tracking: coarse_conversion_value, conversion_destination, standard_event_content_type,
                                       signal_source_bucket, is_conversion_id_modeled, fidelity_type, redownload
                   Time-based: hourly_stats_aggregated_by_advertiser_time_zone, 
                              hourly_stats_aggregated_by_audience_time_zone, frequency_value
                   Extensions/Landing: ad_extension_domain, ad_extension_url, landing_destination, 
                                      mdsa_landing_destination
                   Attribution: sot_attribution_model_type, sot_attribution_window, sot_channel, 
                               sot_event_type, sot_source
                   Mobile/SKAN: skan_campaign_id, skan_conversion_id, skan_version, postback_sequence_index
                   CRM/Business: crm_advertiser_l12_territory_ids, crm_advertiser_subvertical_id,
                                crm_advertiser_vertical_id, crm_ult_advertiser_id, user_persona_id, user_persona_name
                   Advanced: hsid, is_auto_advance, is_rendered_as_delayed_skip_ad, mmm, place_page_id,
                            marketing_messages_btn_name, impression_view_time_advertiser_hour_v2, comscore_market,
                            comscore_market_code
        level: Level of aggregation (ad, adset, campaign, account)
        limit: Maximum number of results to return per page (default: 25, Meta API allows much higher values)
        after: Pagination cursor to get the next set of results. Use the 'after' cursor from previous response's paging.next field.
        action_attribution_windows: Optional list of attribution windows (e.g., ["1d_click", "7d_click", "1d_view"]).
                   When specified, actions include additional fields for each window. The 'value' field always shows 7d_click.
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "object_id": {
      "title": "Object Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "time_range": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "additionalProperties": {
            "type": "string"
          },
          "type": "object"
        }
      ],
      "default": "maximum",
      "title": "Time Range"
    },
    "breakdown": {
      "default": "",
      "title": "Breakdown",
      "type": "string"
    },
    "level": {
      "default": "ad",
      "title": "Level",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    },
    "after": {
      "default": "",
      "title": "After",
      "type": "string"
    },
    "action_attribution_windows": {
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
      "title": "Action Attribution Windows"
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

<a id="get_interest_suggestions"></a>

## `get_interest_suggestions`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/targeting.py#L41)


    Get interest suggestions based on existing interests.
    
    Args:
        interest_list: List of interest names to get suggestions for (e.g., ["Basketball", "Soccer"])
        access_token: Meta API access token (optional - will use cached token if not provided)  
        limit: Maximum number of suggestions to return (default: 25)
    
    Returns:
        JSON string containing suggested interests with id, name, audience_size, and description fields
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "interest_list": {
      "items": {
        "type": "string"
      },
      "title": "Interest List",
      "type": "array"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "limit": {
      "default": 25,
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

<a id="get_login_link"></a>

## `get_login_link`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/authentication.py#L42)


    Get a clickable login link for Meta Ads authentication.
    
    NOTE: This method should only be used if you're using your own Facebook app.
    If using Pipeboard authentication (recommended), set the PIPEBOARD_API_TOKEN
    environment variable instead (token obtainable via https://pipeboard.co).
    
    Args:
        access_token: Meta API access token (optional - will use cached token if not provided)
    
    Returns:
        A clickable resource link for Meta authentication
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "title": "get_login_linkArguments",
  "type": "object"
}
```

</details>

<a id="get_video_status"></a>

## `get_video_status`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/video_upload.py#L346)


    Get the processing status of an uploaded video.

    After uploading, Meta processes (encodes) the video. This can take
    several minutes depending on video length and resolution.

    A video must be fully processed before it can be used in ad creatives.

    Args:
        video_id: Meta video ID (returned from upload_video)
        access_token: Meta API access token (optional)

    Returns:
        JSON response with:
        - id: Video ID
        - status: Processing status object containing:
            - video_status: "ready", "processing", "error"
            - processing_progress: 0-100 percentage
        - title: Video title
        - length: Duration in seconds
        - source: Video source URL (when ready)

    Status values:
        - "processing": Video is being encoded
        - "ready": Video is ready to use in ads
        - "error": Processing failed

    Example:
        get_video_status(video_id="123456789")
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "video_id": {
      "title": "Video Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "video_id"
  ],
  "title": "get_video_statusArguments",
  "type": "object"
}
```

</details>

<a id="pause_ad"></a>

## `pause_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/status_control.py#L144)


    Pause an ad by setting its status to PAUSED.

    When paused, the ad stops delivering immediately.
    The ad can be resumed later with resume_ad.

    Args:
        ad_id: Meta Ads ad ID
        access_token: Meta API access token (optional - will use cached token if not provided)

    Returns:
        JSON response with success status: {"success": true} or error details
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "pause_adArguments",
  "type": "object"
}
```

</details>

<a id="pause_adset"></a>

## `pause_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/status_control.py#L106)


    Pause an ad set by setting its status to PAUSED.

    When paused, all ads within the ad set stop delivering.
    The ad set can be resumed later with resume_adset.

    Args:
        adset_id: Meta Ads ad set ID
        access_token: Meta API access token (optional - will use cached token if not provided)

    Returns:
        JSON response with success status: {"success": true} or error details
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "adset_id"
  ],
  "title": "pause_adsetArguments",
  "type": "object"
}
```

</details>

<a id="pause_campaign"></a>

## `pause_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/status_control.py#L68)


    Pause a campaign by setting its status to PAUSED.

    When paused, all ads within the campaign stop delivering.
    The campaign can be resumed later with resume_campaign.

    Args:
        campaign_id: Meta Ads campaign ID
        access_token: Meta API access token (optional - will use cached token if not provided)

    Returns:
        JSON response with success status: {"success": true} or error details
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

<a id="resume_ad"></a>

## `resume_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/status_control.py#L163)


    Resume a paused ad by setting its status to ACTIVE.

    When resumed, the ad will start delivering again
    (subject to its ad set's and campaign's status).

    Args:
        ad_id: Meta Ads ad ID
        access_token: Meta API access token (optional - will use cached token if not provided)

    Returns:
        JSON response with success status: {"success": true} or error details
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "resume_adArguments",
  "type": "object"
}
```

</details>

<a id="resume_adset"></a>

## `resume_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/status_control.py#L125)


    Resume a paused ad set by setting its status to ACTIVE.

    When resumed, ads within the ad set will start delivering again
    (subject to their own status and the campaign's status).

    Args:
        adset_id: Meta Ads ad set ID
        access_token: Meta API access token (optional - will use cached token if not provided)

    Returns:
        JSON response with success status: {"success": true} or error details
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "adset_id"
  ],
  "title": "resume_adsetArguments",
  "type": "object"
}
```

</details>

<a id="resume_campaign"></a>

## `resume_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/status_control.py#L87)


    Resume a paused campaign by setting its status to ACTIVE.

    When resumed, ads within the campaign will start delivering again
    (subject to their own status and the status of their ad sets).

    Args:
        campaign_id: Meta Ads campaign ID
        access_token: Meta API access token (optional - will use cached token if not provided)

    Returns:
        JSON response with success status: {"success": true} or error details
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "campaign_id"
  ],
  "title": "resume_campaignArguments",
  "type": "object"
}
```

</details>

<a id="save_ad_image_locally"></a>

## `save_ad_image_locally`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L394)


        Get, download, and save a Meta ad image locally, returning the file path.
        
        Args:
            ad_id: Meta Ads ad ID
            access_token: Meta API access token (optional - will use cached token if not provided)
            output_dir: Directory to save the image file (default: 'ad_images')
        
        Returns:
            The file path to the saved image, or an error message string.
        

Availability: Opt-in META_ADS_ENABLE_SAVE_AD_IMAGE_LOCALLY.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "title": "Ad Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "output_dir": {
      "default": "ad_images",
      "title": "Output Dir",
      "type": "string"
    }
  },
  "required": [
    "ad_id"
  ],
  "title": "save_ad_image_locallyArguments",
  "type": "object"
}
```

</details>

<a id="search"></a>

## `search`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/openai_deep_research.py#L312)


    Search through Meta Ads data and return matching record IDs.
    It searches across ad accounts, campaigns, ads, pages, and businesses to find relevant records
    based on the provided query.
    
    Args:
        query: Search query string to find relevant Meta Ads records
        access_token: Meta API access token (optional - will use cached token if not provided)
        
    Returns:
        JSON response with list of matching record IDs
        
    Example Usage:
        search(query="active campaigns")
        search(query="account spending")
        search(query="facebook ads performance")
        search(query="facebook pages")
        search(query="user businesses")
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    }
  },
  "required": [
    "query"
  ],
  "title": "searchArguments",
  "type": "object"
}
```

</details>

<a id="search_ads_archive"></a>

## `search_ads_archive`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads_library.py#L16)


        Search the Facebook Ads Library archive.

        Args:
            search_terms: The search query for ads.
            ad_reached_countries: List of country codes (e.g., ["US", "GB"]).
            access_token: Meta API access token (optional - will use cached token if not provided).
            ad_type: Type of ads to search for (e.g., POLITICAL_AND_ISSUE_ADS, HOUSING_ADS, ALL).
            limit: Maximum number of ads to return.
            fields: Comma-separated string of fields to retrieve for each ad.

        Example Usage via curl equivalent:
            curl -G \
            -d "search_terms='california'" \
            -d "ad_type=POLITICAL_AND_ISSUE_ADS" \
            -d "ad_reached_countries=['US']" \
            -d "fields=ad_snapshot_url,spend" \
            -d "access_token=<ACCESS_TOKEN>" \
            "https://graph.facebook.com/<API_VERSION>/ads_archive"
        

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "search_terms": {
      "title": "Search Terms",
      "type": "string"
    },
    "ad_reached_countries": {
      "items": {
        "type": "string"
      },
      "title": "Ad Reached Countries",
      "type": "array"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "ad_type": {
      "default": "ALL",
      "title": "Ad Type",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "title": "Limit",
      "type": "integer"
    },
    "fields": {
      "default": "ad_creation_time,ad_creative_body,ad_creative_link_caption,ad_creative_link_description,ad_creative_link_title,ad_delivery_start_time,ad_delivery_stop_time,ad_snapshot_url,currency,demographic_distribution,funding_entity,impressions,page_id,page_name,publisher_platform,region_distribution,spend",
      "title": "Fields",
      "type": "string"
    }
  },
  "required": [
    "search_terms",
    "ad_reached_countries"
  ],
  "title": "search_ads_archiveArguments",
  "type": "object"
}
```

</details>

<a id="search_behaviors"></a>

## `search_behaviors`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/targeting.py#L456)


    Get all available behavior targeting options.
    
    Args:
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of results to return (default: 50)
    
    Returns:
        JSON string containing behavior targeting options with id, name, audience_size bounds, path, and description
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "limit": {
      "default": 50,
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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/targeting.py#L481)


    Get demographic targeting options.
    
    Args:
        access_token: Meta API access token (optional - will use cached token if not provided)
        demographic_class: Type of demographics to retrieve. Options: 'demographics', 'life_events', 
                          'industries', 'income', 'family_statuses', 'user_device', 'user_os' (default: 'demographics')
        limit: Maximum number of results to return (default: 50)
    
    Returns:
        JSON string containing demographic targeting options with id, name, audience_size bounds, path, and description
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "demographic_class": {
      "default": "demographics",
      "title": "Demographic Class",
      "type": "string"
    },
    "limit": {
      "default": 50,
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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/targeting.py#L508)


    Search for geographic targeting locations.
    
    Args:
        query: Search term for locations (e.g., "New York", "California", "Japan")
        access_token: Meta API access token (optional - will use cached token if not provided)
        location_types: Types of locations to search. Options: ['country', 'region', 'city', 'zip', 
                       'geo_market', 'electoral_district']. If not specified, searches all types.
        limit: Maximum number of results to return (default: 25)
    
    Returns:
        JSON string containing location data with key, name, type, and geographic hierarchy information
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
      "title": "Location Types"
    },
    "limit": {
      "default": 25,
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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/targeting.py#L12)


    Search for interest targeting options by keyword.
    
    Args:
        query: Search term for interests (e.g., "baseball", "cooking", "travel")
        access_token: Meta API access token (optional - will use cached token if not provided)
        limit: Maximum number of results to return (default: 25)
    
    Returns:
        JSON string containing interest data with id, name, audience_size, and path fields
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "query": {
      "title": "Query",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "limit": {
      "default": 25,
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

<a id="search_pages_by_name"></a>

## `search_pages_by_name`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L1597)


    Search for pages by name within an account.
    
    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        search_term: Search term to find pages by name (optional - returns all pages if not provided)
    
    Returns:
        JSON response with matching pages
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "search_term": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Search Term"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "search_pages_by_nameArguments",
  "type": "object"
}
```

</details>

<a id="send_capi_event"></a>

## `send_capi_event`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/capi.py#L201)


    Send a conversion event to Meta Conversions API (CAPI).

    CAPI allows you to send web, app, and offline events directly to Meta
    for improved ad targeting and measurement. Events sent via CAPI are
    matched with events from the browser pixel for deduplication.

    At least one of phone or email is required for user matching.

    Args:
        pixel_id: Facebook Pixel ID (dataset ID)
        event_name: Standard event name. Common values:
            - ViewContent: User viewed a product/content
            - CompleteRegistration: User completed registration
            - Purchase: User made a purchase
            - Lead: User submitted a lead form
            - AddToCart: User added item to cart
            - InitiateCheckout: User started checkout
        access_token: Meta API access token (optional - will use cached token if not provided)
        phone: User's phone number (will be hashed with SHA256)
        email: User's email address (will be hashed with SHA256)
        client_ip_address: User's IP address (improves matching)
        client_user_agent: User's browser user agent (improves matching)
        fbc: Facebook click ID cookie (_fbc)
        fbp: Facebook browser ID cookie (_fbp)
        external_id: Your internal user ID (will be hashed)
        event_source_url: URL where the event occurred
        action_source: Where the event originated. Values: website, app, email,
                      phone_call, chat, physical_store, system_generated, other
        custom_data: Additional event data like currency, value, content_ids, etc.
            Example: {"currency": "USD", "value": 99.99, "content_ids": ["SKU123"]}
        event_id: Unique event ID for deduplication. If not provided, one will be generated.

    Returns:
        JSON response with events_received count and fbtrace_id

    Example:
        send_capi_event(
            pixel_id="123456789",
            event_name="Purchase",
            phone="+1234567890",
            email="user@example.com",
            custom_data={"currency": "USD", "value": 99.99}
        )
    

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
      "title": "Event Name",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "phone": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Phone"
    },
    "email": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Email"
    },
    "client_ip_address": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Client Ip Address"
    },
    "client_user_agent": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Client User Agent"
    },
    "fbc": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Fbc"
    },
    "fbp": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Fbp"
    },
    "external_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "External Id"
    },
    "event_source_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Event Source Url"
    },
    "action_source": {
      "default": "website",
      "title": "Action Source",
      "type": "string"
    },
    "custom_data": {
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
      "title": "Custom Data"
    },
    "event_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Event Id"
    }
  },
  "required": [
    "pixel_id",
    "event_name"
  ],
  "title": "send_capi_eventArguments",
  "type": "object"
}
```

</details>

<a id="update_ad"></a>

## `update_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L520)


    Update an ad with new settings.
    
    Args:
        ad_id: Meta Ads ad ID
        status: Update ad status (ACTIVE, PAUSED, etc.)
        bid_amount: Bid amount in account currency (in cents for USD)
        tracking_specs: Optional tracking specifications (e.g., for pixel events).
        creative_id: ID of the creative to associate with this ad (changes the ad's image/content)
        access_token: Meta API access token (optional - will use cached token if not provided)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
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
      "title": "Status"
    },
    "bid_amount": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Bid Amount"
    },
    "tracking_specs": {
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
      "title": "Tracking Specs"
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
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L1278)


    Update an existing ad creative with new content or settings.
    
    Args:
        creative_id: Meta Ads creative ID to update
        access_token: Meta API access token (optional - will use cached token if not provided)
        name: New creative name
        message: New ad copy/text
        headline: Single headline for simple ads (cannot be used with headlines)
        headlines: New list of headlines for dynamic creative testing (cannot be used with headline)
        description: Single description for simple ads (cannot be used with descriptions)
        descriptions: New list of descriptions for dynamic creative testing (cannot be used with description)
        dynamic_creative_spec: New dynamic creative optimization settings
        call_to_action_type: New call to action button type
        lead_gen_form_id: Lead generation form ID for lead generation campaigns. Required when using
                         lead generation CTAs like 'SIGN_UP', 'GET_OFFER', 'SUBSCRIBE', etc.
    
    Returns:
        JSON response with updated creative details
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "creative_id": {
      "title": "Creative Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
    "message": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Message"
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
      "title": "Headlines"
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
      "title": "Descriptions"
    },
    "dynamic_creative_spec": {
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
      "title": "Dynamic Creative Spec"
    },
    "call_to_action_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Call To Action Type"
    },
    "lead_gen_form_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lead Gen Form Id"
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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/adsets.py#L414)


    Update an ad set with new settings including frequency caps and budgets.
    
    Args:
        adset_id: Meta Ads ad set ID
        frequency_control_specs: List of frequency control specifications 
                                 (e.g. [{"event": "IMPRESSIONS", "interval_days": 7, "max_frequency": 3}])
        bid_strategy: Bid strategy (e.g., 'LOWEST_COST_WITH_BID_CAP')
        bid_amount: Bid amount in account currency (in cents for USD)
        status: Update ad set status (ACTIVE, PAUSED, etc.)
        targeting: Complete targeting specifications (will replace existing targeting)
                  (e.g. {"targeting_automation":{"advantage_audience":1}, "geo_locations": {"countries": ["US"]}})
        optimization_goal: Conversion optimization goal (e.g., 'LINK_CLICKS', 'CONVERSIONS', 'APP_INSTALLS', etc.)
        daily_budget: Daily budget in account currency (in cents) as a string
        lifetime_budget: Lifetime budget in account currency (in cents) as a string
        is_dynamic_creative: Enable/disable Dynamic Creative for this ad set.
        access_token: Meta API access token (optional - will use cached token if not provided)
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "adset_id": {
      "title": "Adset Id",
      "type": "string"
    },
    "frequency_control_specs": {
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
      "title": "Frequency Control Specs"
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
      "title": "Bid Strategy"
    },
    "bid_amount": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Bid Amount"
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
      "title": "Targeting"
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
      "title": "Optimization Goal"
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "integer"
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
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lifetime Budget"
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
      "title": "Is Dynamic Creative"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/campaigns.py#L234)


    Update an existing campaign in a Meta Ads account.

    Args:
        campaign_id: Meta Ads campaign ID
        access_token: Meta API access token (optional - will use cached token if not provided)
        name: New campaign name
        status: New campaign status (e.g., 'ACTIVE', 'PAUSED')
        special_ad_categories: List of special ad categories if applicable
        daily_budget: New daily budget in account currency (in cents) as a string. 
                     Set to empty string "" to remove the daily budget.
        lifetime_budget: New lifetime budget in account currency (in cents) as a string.
                        Set to empty string "" to remove the lifetime budget.
        bid_strategy: New bid strategy
        bid_cap: New bid cap in account currency (in cents) as a string
        spend_cap: New spending limit for the campaign in account currency (in cents) as a string
        campaign_budget_optimization: Enable/disable campaign budget optimization
        objective: New campaign objective (Note: May not always be updatable)
        use_adset_level_budgets: If True, removes campaign-level budgets to switch to ad set level budgets
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "campaign_id": {
      "title": "Campaign Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
      "title": "Special Ad Categories"
    },
    "daily_budget": {
      "anyOf": [
        {
          "type": "integer"
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
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lifetime Budget"
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
      "title": "Bid Strategy"
    },
    "bid_cap": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Bid Cap"
    },
    "spend_cap": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Spend Cap"
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
      "default": null,
      "title": "Campaign Budget Optimization"
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
    "use_adset_level_budgets": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Use Adset Level Budgets"
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

<a id="upload_ad_image"></a>

## `upload_ad_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/ads.py#L567)


    Upload an image to use in Meta Ads creatives.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        access_token: Meta API access token (optional - will use cached token if not provided)
        file: Data URL or raw base64 string of the image (e.g., "data:image/png;base64,iVBORw0KG...")
        image_url: Direct URL to an image to fetch and upload
        file_path: Local file path to an image (e.g., "/path/to/image.png")
        name: Optional name for the image (default: filename)

    Returns:
        JSON response with image details including hash for creative creation
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
    },
    "file": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "File"
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
      "title": "Image Url"
    },
    "file_path": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "File Path"
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
    "account_id"
  ],
  "title": "upload_ad_imageArguments",
  "type": "object"
}
```

</details>

<a id="upload_video"></a>

## `upload_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/video_upload.py#L256)


    Upload a video to Meta Ads for use in ad creatives.

    Automatically uses chunked upload for files >= 50MB, simple upload for smaller files.
    Supports videos up to 4GB.

    After upload, the video will be processed (encoded) by Meta. Use get_video_status
    to check when processing is complete before using in ads.

    Args:
        account_id: Meta Ads account ID (format: act_XXXXXXXXX)
        file_path: Absolute path to the video file on disk
        access_token: Meta API access token (optional - will use cached token if not provided)
        title: Optional title for the video

    Returns:
        JSON response with:
        - id: Video ID to use in creatives
        - upload_method: "simple" or "chunked"

    Supported formats: MP4, MOV, AVI, MKV, WEBM
    Recommended: MP4 with H.264 codec

    Example:
        upload_video(
            account_id="act_123456789",
            file_path="/path/to/video.mp4",
            title="My Product Ad"
        )
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "title": "Account Id",
      "type": "string"
    },
    "file_path": {
      "title": "File Path",
      "type": "string"
    },
    "access_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Access Token"
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
    }
  },
  "required": [
    "account_id",
    "file_path"
  ],
  "title": "upload_videoArguments",
  "type": "object"
}
```

</details>

<a id="upscale_to_4k"></a>

## `upscale_to_4k`

Scope: **supporting** · Capability: **creatives** · [Definition](https://github.com/dengineproblem/meta-ads-mcp-extended/blob/e6f1517bca0b0689b9160e8fea4e7cba9f8c849b/meta_ads_mcp/core/creative_generation.py#L334)


    Upscale an image to 4K resolution via Gemini.

    Takes an existing image and generates a 4K version preserving
    all details, composition and style.

    Args:
        image_path: Path to the source image
        aspect_ratio: Target aspect ratio - "9:16", "4:5", or "1:1" (default: "9:16")
        output_path: Optional path for the output (default: {original}_4k.png)

    Returns:
        JSON with file_path to 4K image

    Example:
        upscale_to_4k(image_path="/path/to/creative.png", aspect_ratio="9:16")
    

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "image_path": {
      "title": "Image Path",
      "type": "string"
    },
    "aspect_ratio": {
      "default": "9:16",
      "title": "Aspect Ratio",
      "type": "string"
    },
    "output_path": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Output Path"
    }
  },
  "required": [
    "image_path"
  ],
  "title": "upscale_to_4kArguments",
  "type": "object"
}
```

</details>

