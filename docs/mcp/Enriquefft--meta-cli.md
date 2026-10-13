# Enriquefft/meta-cli

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/Enriquefft/meta-cli) · [Machine-readable snapshot](../../catalog/Enriquefft--meta-cli.json)

Complete registered tool snapshot. **11 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`9d1dc234223c`](https://github.com/Enriquefft/meta-cli/tree/9d1dc234223ca97bd9f8d605450fb1070961d753). Method: `runtime-tools-list`.

- The CLI exposes these tools through meta serve. Handler-only defaults and validation are not invented as schema constraints.

## Tools

- [meta_auth_status](#meta_auth_status)
- [meta_create_ad](#meta_create_ad)
- [meta_create_adset](#meta_create_adset)
- [meta_create_campaign](#meta_create_campaign)
- [meta_create_creative](#meta_create_creative)
- [meta_list_accounts](#meta_list_accounts)
- [meta_list_pages](#meta_list_pages)
- [meta_search_targeting](#meta_search_targeting)
- [meta_upload_image](#meta_upload_image)
- [meta_upload_video](#meta_upload_video)
- [meta_video_status](#meta_video_status)

<a id="meta_auth_status"></a>

## `meta_auth_status`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L21)

Verify the current access token is valid and show granted permissions.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {},
  "required": [],
  "type": "object"
}
```

</details>

<a id="meta_create_ad"></a>

## `meta_create_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L262)

Create a new ad by linking a creative to an ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "description": "The ad account ID",
      "type": "string"
    },
    "adset_id": {
      "description": "Ad set ID to place this ad in",
      "type": "string"
    },
    "creative_id": {
      "description": "Creative ID to use for this ad",
      "type": "string"
    },
    "name": {
      "description": "Ad name",
      "type": "string"
    },
    "status": {
      "default": "PAUSED",
      "description": "Initial ad status",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "name",
    "adset_id",
    "creative_id"
  ],
  "type": "object"
}
```

</details>

<a id="meta_create_adset"></a>

## `meta_create_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L125)

Create a new ad set under a campaign, defining targeting, scheduling, and budget.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "description": "The ad account ID",
      "type": "string"
    },
    "advantage_audience": {
      "description": "Enable Advantage+ audience expansion (default: false, uses explicit targeting)",
      "type": "boolean"
    },
    "age_max": {
      "default": 65,
      "description": "Maximum age",
      "type": "number"
    },
    "age_min": {
      "default": 18,
      "description": "Minimum age",
      "type": "number"
    },
    "behaviors": {
      "description": "Behavior IDs for targeting (use meta_search_targeting with type 'behaviors' to find IDs)",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "bid_amount": {
      "description": "Bid amount in dollars",
      "type": "number"
    },
    "billing_event": {
      "description": "Billing event (default: IMPRESSIONS)",
      "type": "string"
    },
    "campaign_id": {
      "description": "Parent campaign ID",
      "type": "string"
    },
    "countries": {
      "description": "Target countries (ISO country codes)",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "custom_audiences": {
      "description": "Custom audience IDs from the ad account",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "custom_event_type": {
      "description": "Custom event type for the pixel",
      "type": "string"
    },
    "daily_budget": {
      "description": "Daily budget in dollars",
      "type": "number"
    },
    "end_time": {
      "description": "Ad set end time (ISO 8601)",
      "type": "string"
    },
    "excluded_countries": {
      "description": "Countries to exclude from targeting",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "genders": {
      "description": "Target genders (1=male, 2=female). Default: [1,2]",
      "items": {
        "type": "number"
      },
      "type": "array"
    },
    "interests": {
      "description": "Interest IDs for targeting (use meta_search_targeting with type 'interests' to find IDs)",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "lifetime_budget": {
      "description": "Lifetime budget in dollars",
      "type": "number"
    },
    "name": {
      "description": "Ad set name",
      "type": "string"
    },
    "optimization_goal": {
      "description": "Optimization goal for the ad set",
      "type": "string"
    },
    "pixel_id": {
      "description": "Facebook Pixel ID for conversion tracking",
      "type": "string"
    },
    "publisher_platforms": {
      "description": "Publisher platforms (facebook, instagram, audience_network, messenger)",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "start_time": {
      "description": "Ad set start time (ISO 8601)",
      "type": "string"
    },
    "status": {
      "default": "PAUSED",
      "description": "Initial ad set status",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "name",
    "campaign_id",
    "optimization_goal",
    "countries"
  ],
  "type": "object"
}
```

</details>

<a id="meta_create_campaign"></a>

## `meta_create_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L88)

Create a new advertising campaign under the specified ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "description": "The ad account ID",
      "type": "string"
    },
    "bid_strategy": {
      "default": "LOWEST_COST_WITHOUT_CAP",
      "description": "Bid strategy",
      "type": "string"
    },
    "daily_budget": {
      "description": "Daily budget in dollars (e.g. 50.00 = $50). Mutually exclusive with lifetime_budget; at least one is required.",
      "type": "number"
    },
    "lifetime_budget": {
      "description": "Lifetime budget in dollars (e.g. 500.00 = $500). Mutually exclusive with daily_budget; at least one is required.",
      "type": "number"
    },
    "name": {
      "description": "Campaign name",
      "type": "string"
    },
    "objective": {
      "description": "Campaign objective",
      "enum": [
        "OUTCOME_SALES",
        "OUTCOME_TRAFFIC",
        "OUTCOME_ENGAGEMENT",
        "OUTCOME_AWARENESS",
        "OUTCOME_LEADS",
        "OUTCOME_APP_PROMOTION"
      ],
      "type": "string"
    },
    "special_ad_category": {
      "default": "NONE",
      "description": "Special ad category",
      "type": "string"
    },
    "status": {
      "default": "PAUSED",
      "description": "Initial campaign status",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "name",
    "objective"
  ],
  "type": "object"
}
```

</details>

<a id="meta_create_creative"></a>

## `meta_create_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L215)

Create an ad creative with video/image, text, and call-to-action. For video creatives, the video's auto-generated thumbnail is resolved automatically — pass image_hash or image_url only if you want a custom thumbnail.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "description": "The ad account ID",
      "type": "string"
    },
    "cta": {
      "default": "SHOP_NOW",
      "description": "Call-to-action button type",
      "type": "string"
    },
    "description": {
      "description": "Ad description",
      "type": "string"
    },
    "headline": {
      "description": "Ad headline",
      "type": "string"
    },
    "image_hash": {
      "description": "Optional. Hash of a previously uploaded image to use as a custom thumbnail. Omit for video creatives to let meta-cli auto-resolve the video's default thumbnail.",
      "type": "string"
    },
    "image_url": {
      "description": "Optional. URL of an image to use as a custom thumbnail. Omit for video creatives to let meta-cli auto-resolve the video's default thumbnail.",
      "type": "string"
    },
    "instagram_account_id": {
      "description": "Instagram account ID for Instagram placement",
      "type": "string"
    },
    "link": {
      "description": "Destination URL",
      "type": "string"
    },
    "message": {
      "description": "Ad copy / body text",
      "type": "string"
    },
    "name": {
      "description": "Creative name",
      "type": "string"
    },
    "page_id": {
      "description": "Facebook Page ID",
      "type": "string"
    },
    "video_id": {
      "description": "Video ID from meta_upload_video",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "page_id",
    "message",
    "link"
  ],
  "type": "object"
}
```

</details>

<a id="meta_list_accounts"></a>

## `meta_list_accounts`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L27)

List ad accounts accessible by the authenticated user.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "limit": {
      "default": 25,
      "description": "Maximum number of accounts to return",
      "type": "number"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

<a id="meta_list_pages"></a>

## `meta_list_pages`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L37)

List Facebook Pages managed by the authenticated user.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "limit": {
      "default": 25,
      "description": "Maximum number of pages to return",
      "type": "number"
    }
  },
  "required": [],
  "type": "object"
}
```

</details>

<a id="meta_search_targeting"></a>

## `meta_search_targeting`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L288)

Search for targeting options (interests, behaviors, demographics, etc.).

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "description": "The ad account ID",
      "type": "string"
    },
    "limit": {
      "default": 25,
      "description": "Maximum number of results",
      "type": "number"
    },
    "query": {
      "description": "Search query string",
      "type": "string"
    },
    "type": {
      "description": "Type of targeting to search",
      "enum": [
        "interests",
        "behaviors",
        "demographics",
        "education_schools",
        "education_majors",
        "work_employers",
        "work_positions"
      ],
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "type",
    "query"
  ],
  "type": "object"
}
```

</details>

<a id="meta_upload_image"></a>

## `meta_upload_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L64)

Upload an image file to an ad account for use in ad creatives (including as a video creative thumbnail).

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "description": "The ad account ID",
      "type": "string"
    },
    "file_path": {
      "description": "Local file path to the image file",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "file_path"
  ],
  "type": "object"
}
```

</details>

<a id="meta_upload_video"></a>

## `meta_upload_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L47)

Upload a video file to an ad account for use in ad creatives.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "account_id": {
      "description": "The ad account ID",
      "type": "string"
    },
    "file_path": {
      "description": "Local file path to the video file",
      "type": "string"
    },
    "title": {
      "description": "Optional title for the video",
      "type": "string"
    }
  },
  "required": [
    "account_id",
    "file_path"
  ],
  "type": "object"
}
```

</details>

<a id="meta_video_status"></a>

## `meta_video_status`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/Enriquefft/meta-cli/blob/9d1dc234223ca97bd9f8d605450fb1070961d753/internal/mcp/tools.go#L78)

Check the encoding status of an uploaded video. Wait until status is 'ready' before using in creatives.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "video_id": {
      "description": "The video ID returned from meta_upload_video",
      "type": "string"
    }
  },
  "required": [
    "video_id"
  ],
  "type": "object"
}
```

</details>

