# brijr/meta-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/brijr/meta-mcp) · [Machine-readable snapshot](../../catalog/brijr--meta-mcp.json)

Complete registered tool snapshot. **39 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`664b20617a6a`](https://github.com/brijr/meta-mcp/tree/664b20617a6aee529ff31f8093e85fca7db4b7be). Method: `registered-source`.

- Exact registered Zod definitions converted through the MCP SDK; this is a source snapshot, not an enumeration of a hosted deployment.

## Tools

- [bulk_create_ads](#bulk_create_ads)
- [bulk_update_status](#bulk_update_status)
- [clone_campaign_structure](#clone_campaign_structure)
- [compare_ads](#compare_ads)
- [create_ad](#create_ad)
- [create_ad_creative](#create_ad_creative)
- [create_ad_set](#create_ad_set)
- [create_campaign](#create_campaign)
- [create_custom_audience](#create_custom_audience)
- [create_lookalike_audience](#create_lookalike_audience)
- [delete_ad_set](#delete_ad_set)
- [delete_campaign](#delete_campaign)
- [duplicate_ad_set](#duplicate_ad_set)
- [get_ad](#get_ad)
- [get_ad_accounts](#get_ad_accounts)
- [get_ad_metrics](#get_ad_metrics)
- [get_ad_preview](#get_ad_preview)
- [get_ad_set](#get_ad_set)
- [get_adset_metrics](#get_adset_metrics)
- [get_audience_size](#get_audience_size)
- [get_campaign](#get_campaign)
- [get_campaign_metrics](#get_campaign_metrics)
- [get_conversion_data](#get_conversion_data)
- [get_custom_conversions](#get_custom_conversions)
- [get_insights](#get_insights)
- [get_pages](#get_pages)
- [get_pixels](#get_pixels)
- [get_targeting_options](#get_targeting_options)
- [get_video_status](#get_video_status)
- [list_ad_sets](#list_ad_sets)
- [list_ads](#list_ads)
- [list_audiences](#list_audiences)
- [list_campaigns](#list_campaigns)
- [update_ad](#update_ad)
- [update_ad_set](#update_ad_set)
- [update_campaign](#update_campaign)
- [upload_image](#upload_image)
- [upload_video](#upload_video)
- [validate_account](#validate_account)

<a id="bulk_create_ads"></a>

## `bulk_create_ads`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/batch/bulk_create_ads.ts#L29)

Create multiple Meta ads in a single tool call.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "ads": {
      "minItems": 1,
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "creative_id": {
            "type": "string",
            "minLength": 1,
            "description": "Meta object ID."
          },
          "creative_spec": {
            "type": "object",
            "propertyNames": {
              "type": "string"
            },
            "additionalProperties": {}
          },
          "page_id": {
            "type": "string",
            "minLength": 1,
            "description": "Meta object ID."
          },
          "message": {
            "type": "string"
          },
          "headline": {
            "type": "string"
          },
          "link": {
            "type": "string"
          },
          "image_hash": {
            "type": "string"
          },
          "call_to_action": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "meta_overrides": {
            "type": "object",
            "propertyNames": {
              "type": "string"
            },
            "additionalProperties": {}
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": {}
      }
    }
  },
  "required": [
    "ad_set_id",
    "ads"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="bulk_update_status"></a>

## `bulk_update_status`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/batch/bulk_update_status.ts#L12)

Update status for many Meta objects at once.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "object_ids": {
      "minItems": 1,
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "description": "Meta object ID."
      }
    },
    "status": {
      "type": "string"
    }
  },
  "required": [
    "object_ids",
    "status"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="clone_campaign_structure"></a>

## `clone_campaign_structure`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/batch/clone_campaign_structure.ts#L11)

Deep-clone a campaign with its ad sets and ads.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "campaign_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="compare_ads"></a>

## `compare_ads`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/insights/compare_ads.ts#L13)

Compare metrics across multiple Meta ads.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_ids": {
      "minItems": 1,
      "type": "array",
      "items": {
        "type": "string",
        "minLength": 1,
        "description": "Meta object ID."
      }
    },
    "metrics": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "date_range": {
      "type": "object",
      "properties": {
        "since": {
          "type": "string",
          "description": "Start date in YYYY-MM-DD format."
        },
        "until": {
          "type": "string",
          "description": "End date in YYYY-MM-DD format."
        }
      },
      "required": [
        "since",
        "until"
      ]
    }
  },
  "required": [
    "ad_ids"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_ad"></a>

## `create_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/create_ad.ts#L18)

Create a Meta ad under an ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "creative_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "name": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "ad_set_id",
    "creative_id",
    "name"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_ad_creative"></a>

## `create_ad_creative`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/create_ad_creative.ts#L23)

Create a Meta ad creative.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "name": {
      "type": "string"
    },
    "page_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "message": {
      "type": "string"
    },
    "headline": {
      "type": "string"
    },
    "link": {
      "type": "string"
    },
    "image_hash": {
      "type": "string"
    },
    "call_to_action": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "account_id",
    "name"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_ad_set"></a>

## `create_ad_set`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/ad-sets/create_ad_set.ts#L39)

Create a Meta ad set under a campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "name": {
      "type": "string"
    },
    "targeting": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    },
    "optimization_goal": {
      "type": "string",
      "description": "Meta optimization goal, e.g. LINK_CLICKS, LANDING_PAGE_VIEWS, OFFSITE_CONVERSIONS, REACH, IMPRESSIONS, LEAD_GENERATION, THRUPLAY. Must be compatible with billing_event and the campaign objective."
    },
    "billing_event": {
      "type": "string",
      "description": "How you are charged, e.g. IMPRESSIONS, LINK_CLICKS, THRUPLAY. Must be a valid pairing for optimization_goal (e.g. OFFSITE_CONVERSIONS bills on IMPRESSIONS; LINK_CLICKS optimization can bill on LINK_CLICKS or IMPRESSIONS)."
    },
    "promoted_object": {
      "description": "Required for conversion/lead objectives (e.g. OUTCOME_LEADS, OUTCOME_SALES). Example: { pixel_id, custom_event_type: 'PURCHASE' } or { page_id }.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {}
    },
    "budget": {
      "type": "object",
      "properties": {
        "amount_minor": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "currency": {
          "type": "string",
          "minLength": 3,
          "maxLength": 3
        },
        "period": {
          "type": "string",
          "enum": [
            "daily",
            "lifetime"
          ]
        }
      },
      "required": [
        "amount_minor",
        "currency",
        "period"
      ]
    },
    "schedule": {
      "type": "object",
      "properties": {
        "start_time": {
          "type": "string",
          "description": "ISO 8601 timestamp."
        },
        "end_time": {
          "description": "ISO 8601 timestamp.",
          "type": "string"
        }
      },
      "required": [
        "start_time"
      ]
    },
    "status": {
      "type": "string"
    },
    "bid_amount": {
      "type": "integer",
      "minimum": -9007199254740991,
      "maximum": 9007199254740991
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "campaign_id",
    "name",
    "targeting",
    "optimization_goal",
    "billing_event",
    "budget"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_campaign"></a>

## `create_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/campaigns/create_campaign.ts#L27)

Create a Meta campaign on an ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "name": {
      "type": "string"
    },
    "objective": {
      "type": "string"
    },
    "buying_type": {
      "type": "string"
    },
    "special_ad_categories": {
      "default": [],
      "description": "Required by Meta on every campaign. Pass [] when no special ad category applies, or values like HOUSING, EMPLOYMENT, CREDIT, ISSUES_ELECTIONS_POLITICS, FINANCIAL_PRODUCTS_SERVICES, ONLINE_GAMBLING_AND_GAMING.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "status": {
      "type": "string"
    },
    "budget": {
      "type": "object",
      "properties": {
        "amount_minor": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "currency": {
          "type": "string",
          "minLength": 3,
          "maxLength": 3
        },
        "period": {
          "type": "string",
          "enum": [
            "daily",
            "lifetime"
          ]
        }
      },
      "required": [
        "amount_minor",
        "currency",
        "period"
      ]
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "account_id",
    "name",
    "objective"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_custom_audience"></a>

## `create_custom_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/audiences/create_custom_audience.ts#L19)

Create a Meta custom audience.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "name": {
      "type": "string"
    },
    "source_type": {
      "type": "string"
    },
    "config": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "account_id",
    "name",
    "source_type",
    "config"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="create_lookalike_audience"></a>

## `create_lookalike_audience`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/audiences/create_lookalike_audience.ts#L16)

Create a Meta lookalike audience.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "source_audience_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "country": {
      "type": "string",
      "minLength": 2,
      "maxLength": 2
    },
    "ratio": {
      "type": "number",
      "exclusiveMinimum": 0,
      "maximum": 0.2
    },
    "name": {
      "type": "string"
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "account_id",
    "source_audience_id",
    "country",
    "ratio"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_ad_set"></a>

## `delete_ad_set`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/ad-sets/delete_ad_set.ts#L10)

Delete a Meta ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "ad_set_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="delete_campaign"></a>

## `delete_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/campaigns/delete_campaign.ts#L10)

Delete or archive a Meta campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "campaign_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="duplicate_ad_set"></a>

## `duplicate_ad_set`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/ad-sets/duplicate_ad_set.ts#L11)

Clone an existing ad set with optional overrides.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "ad_set_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad"></a>

## `get_ad`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/get_ad.ts#L10)

Get a Meta ad by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "ad_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_accounts"></a>

## `get_ad_accounts`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/account/get_ad_accounts.ts#L10)

List accessible Meta ad accounts for the connected workspace.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 500
    },
    "after": {
      "type": "string"
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_metrics"></a>

## `get_ad_metrics`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/insights/get_ad_metrics.ts#L11)

Get key metrics for a Meta ad.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "date_range": {
      "type": "object",
      "properties": {
        "since": {
          "type": "string",
          "description": "Start date in YYYY-MM-DD format."
        },
        "until": {
          "type": "string",
          "description": "End date in YYYY-MM-DD format."
        }
      },
      "required": [
        "since",
        "until"
      ]
    }
  },
  "required": [
    "ad_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_preview"></a>

## `get_ad_preview`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/get_ad_preview.ts#L12)

Generate ad previews for a creative and placement format.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "creative_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "ad_format": {
      "type": "string"
    }
  },
  "required": [
    "creative_id",
    "ad_format"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_ad_set"></a>

## `get_ad_set`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/ad-sets/get_ad_set.ts#L10)

Get a Meta ad set by ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "ad_set_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_adset_metrics"></a>

## `get_adset_metrics`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/insights/get_adset_metrics.ts#L11)

Get key metrics for a Meta ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "date_range": {
      "type": "object",
      "properties": {
        "since": {
          "type": "string",
          "description": "Start date in YYYY-MM-DD format."
        },
        "until": {
          "type": "string",
          "description": "End date in YYYY-MM-DD format."
        }
      },
      "required": [
        "since",
        "until"
      ]
    }
  },
  "required": [
    "ad_set_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_audience_size"></a>

## `get_audience_size`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/audiences/get_audience_size.ts#L14)

Estimate audience size for a Meta targeting specification.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "targeting": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "account_id",
    "targeting"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign"></a>

## `get_campaign`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/campaigns/get_campaign.ts#L10)

Get campaign details by campaign ID.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "campaign_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_campaign_metrics"></a>

## `get_campaign_metrics`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/insights/get_campaign_metrics.ts#L11)

Get key metrics for a Meta campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "date_range": {
      "type": "object",
      "properties": {
        "since": {
          "type": "string",
          "description": "Start date in YYYY-MM-DD format."
        },
        "until": {
          "type": "string",
          "description": "End date in YYYY-MM-DD format."
        }
      },
      "required": [
        "since",
        "until"
      ]
    }
  },
  "required": [
    "campaign_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_conversion_data"></a>

## `get_conversion_data`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/insights/get_conversion_data.ts#L13)

Get conversion-focused insight rows for a Meta object.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "object_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "level": {
      "type": "string"
    },
    "date_range": {
      "type": "object",
      "properties": {
        "since": {
          "type": "string",
          "description": "Start date in YYYY-MM-DD format."
        },
        "until": {
          "type": "string",
          "description": "End date in YYYY-MM-DD format."
        }
      },
      "required": [
        "since",
        "until"
      ]
    }
  },
  "required": [
    "object_id",
    "level"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_custom_conversions"></a>

## `get_custom_conversions`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/account/get_custom_conversions.ts#L11)

List custom conversions for an ad account or a specific pixel.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "pixel_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_insights"></a>

## `get_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/insights/get_insights.ts#L15)

Pull Meta performance insights for a campaign, ad set, or ad.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "object_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "level": {
      "type": "string"
    },
    "metrics": {
      "minItems": 1,
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "date_range": {
      "type": "object",
      "properties": {
        "since": {
          "type": "string",
          "description": "Start date in YYYY-MM-DD format."
        },
        "until": {
          "type": "string",
          "description": "End date in YYYY-MM-DD format."
        }
      },
      "required": [
        "since",
        "until"
      ]
    },
    "breakdowns": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "object_id",
    "level",
    "metrics"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_pages"></a>

## `get_pages`

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/account/get_pages.ts#L12)

List Facebook Pages that can be used with the connected Meta identity.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "include_all_pages": {
      "type": "boolean"
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_pixels"></a>

## `get_pixels`

Scope: **meta-ads** · Capability: **tracking** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/account/get_pixels.ts#L10)

List Meta Pixels available on an ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_targeting_options"></a>

## `get_targeting_options`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/audiences/get_targeting_options.ts#L12)

Search Meta targeting options such as interests and demographics.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 100
    }
  },
  "required": [
    "query"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="get_video_status"></a>

## `get_video_status`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/get_video_status.ts#L10)

Get processing status for a Meta video asset.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "video_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "video_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_ad_sets"></a>

## `list_ad_sets`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/ad-sets/list_ad_sets.ts#L13)

List ad sets under a campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "status": {
      "type": "string"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 500
    },
    "after": {
      "type": "string"
    }
  },
  "required": [
    "campaign_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_ads"></a>

## `list_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/list_ads.ts#L14)

List ads under an ad set or campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "status": {
      "type": "string"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 500
    },
    "after": {
      "type": "string"
    }
  },
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_audiences"></a>

## `list_audiences`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/audiences/list_audiences.ts#L13)

List custom and saved Meta audiences.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "type": {
      "type": "string"
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 500
    },
    "after": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="list_campaigns"></a>

## `list_campaigns`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/campaigns/list_campaigns.ts#L19)

List campaigns on an ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "status": {
      "type": "string"
    },
    "objective": {
      "type": "string"
    },
    "date_range": {
      "type": "object",
      "properties": {
        "since": {
          "type": "string",
          "description": "Start date in YYYY-MM-DD format."
        },
        "until": {
          "type": "string",
          "description": "End date in YYYY-MM-DD format."
        }
      },
      "required": [
        "since",
        "until"
      ]
    },
    "limit": {
      "type": "integer",
      "exclusiveMinimum": 0,
      "maximum": 500
    },
    "after": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_ad"></a>

## `update_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/update_ad.ts#L18)

Update a Meta ad.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "status": {
      "type": "string"
    },
    "creative_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "name": {
      "type": "string"
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "ad_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_ad_set"></a>

## `update_ad_set`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/ad-sets/update_ad_set.ts#L30)

Update a Meta ad set.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "ad_set_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "targeting": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    },
    "budget": {
      "type": "object",
      "properties": {
        "amount_minor": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "currency": {
          "type": "string",
          "minLength": 3,
          "maxLength": 3
        },
        "period": {
          "type": "string",
          "enum": [
            "daily",
            "lifetime"
          ]
        }
      },
      "required": [
        "amount_minor",
        "currency",
        "period"
      ]
    },
    "schedule": {
      "type": "object",
      "properties": {
        "start_time": {
          "type": "string",
          "description": "ISO 8601 timestamp."
        },
        "end_time": {
          "description": "ISO 8601 timestamp.",
          "type": "string"
        }
      },
      "required": [
        "start_time"
      ]
    },
    "status": {
      "type": "string"
    },
    "bid_amount": {
      "type": "integer",
      "minimum": -9007199254740991,
      "maximum": 9007199254740991
    },
    "optimization_goal": {
      "type": "string"
    },
    "billing_event": {
      "type": "string"
    },
    "promoted_object": {
      "description": "Promoted object for conversion/lead objectives, e.g. { pixel_id, custom_event_type } or { page_id }.",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {}
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "ad_set_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="update_campaign"></a>

## `update_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/campaigns/update_campaign.ts#L20)

Update a Meta campaign.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "campaign_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "name": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "budget": {
      "type": "object",
      "properties": {
        "amount_minor": {
          "type": "integer",
          "minimum": 0,
          "maximum": 9007199254740991
        },
        "currency": {
          "type": "string",
          "minLength": 3,
          "maxLength": 3
        },
        "period": {
          "type": "string",
          "enum": [
            "daily",
            "lifetime"
          ]
        }
      },
      "required": [
        "amount_minor",
        "currency",
        "period"
      ]
    },
    "bid_strategy": {
      "type": "string"
    },
    "meta_overrides": {
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {},
      "description": "Arbitrary Meta API override fields."
    }
  },
  "required": [
    "campaign_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="upload_image"></a>

## `upload_image`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/upload_image.ts#L13)

Upload an image to a Meta ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "image_url": {
      "type": "string"
    },
    "image_base64": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="upload_video"></a>

## `upload_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/creatives/upload_video.ts#L13)

Upload a video asset to a Meta ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    },
    "video_url": {
      "type": "string"
    },
    "video_base64": {
      "type": "string"
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

<a id="validate_account"></a>

## `validate_account`

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/brijr/meta-mcp/blob/664b20617a6aee529ff31f8093e85fca7db4b7be/src/tools/account/validate_account.ts#L10)

Run a pre-flight validation check for an ad account.

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "properties": {
    "account_id": {
      "type": "string",
      "minLength": 1,
      "description": "Meta object ID."
    }
  },
  "required": [
    "account_id"
  ],
  "$schema": "http://json-schema.org/draft-07/schema#"
}
```

</details>

