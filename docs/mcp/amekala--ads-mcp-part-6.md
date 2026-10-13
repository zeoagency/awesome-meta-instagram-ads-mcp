# amekala/ads-mcp — tools 176–210

[All tools](amekala--ads-mcp.md) · [Tool index](../tool-index.md)

<a id="remove_campaign_label"></a>

## `remove_campaign_label`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Detach a label from a campaign (removes the tag; the label itself is not deleted).

Get the label_id from get_campaign_labels.

**Required:** campaign_id + label_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Detach a label from a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "label_id": {
      "description": "The label ID to detach (from get_campaign_labels).",
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
  "title": "RemoveCampaignLabelInput",
  "type": "object"
}
```

</details>

<a id="remove_display_ad"></a>

## `remove_display_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove (soft-delete) a Responsive Display Ad.

Sets the AdGroupAd status=REMOVED. The ad stops serving but historical reporting is preserved. Cannot be undone via the API.

**Parameters:** ad_group_id (REQUIRED), ad_id (REQUIRED)

**Execution time:** 2-4 seconds.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for remove_display_ad. Soft-delete one Responsive Display Ad.",
  "properties": {
    "ad_group_id": {
      "description": "Parent ad group ID.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "ad_id": {
      "description": "Ad (AdGroupAd) ID to remove.",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id",
    "ad_id"
  ],
  "title": "RemoveDisplayAdInput",
  "type": "object"
}
```

</details>

<a id="remove_display_ad_group"></a>

## `remove_display_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove (soft-delete) a Display ad group.

Google's API does not support hard deletion — this sets status=REMOVED, which stops serving but preserves historical data for reporting. Cannot be undone via the API.

**Parameters:** ad_group_id (REQUIRED)

**Execution time:** 2-4 seconds.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for remove_display_ad_group. Soft-delete (sets status=REMOVED).",
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
      "description": "Required for multi-account users.",
      "title": "Customer Id"
    }
  },
  "required": [
    "ad_group_id"
  ],
  "title": "RemoveDisplayAdGroupInput",
  "type": "object"
}
```

</details>

<a id="remove_display_criteria"></a>

## `remove_display_criteria`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove one or more AdGroupCriteria from a Display ad group by resource name.

Works for ANY criterion type — placements, topics, audiences, display keywords, demographic exclusions.

**How to get resource names:** use any of the `get_display_*` tools — each entry has `ad_group_id` and `criterion_id`. Construct the resource name as:
`customers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}`

**Example:**
```
criterion_resource_names: [
  "customers/5835090207/adGroupCriteria/197350763433~123456789"
]
```

**Execution time:** 2-5 seconds (destructive — cannot be undone).

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "criterion_resource_names": {
      "description": "List of AdGroupCriterion resource names to remove. Format: 'customers/{cid}/adGroupCriteria/{adGroupId}~{criterionId}'. Get these from any of the get_display_* tools.",
      "items": {
        "type": "string"
      },
      "title": "Criterion Resource Names",
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
    "criterion_resource_names"
  ],
  "title": "RemoveDisplayCriteriaInput",
  "type": "object"
}
```

</details>

<a id="remove_keywords"></a>

## `remove_keywords`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove keywords from an ad group.

**Parameters:**
- ad_group_id: The ad group containing the keywords (REQUIRED)
- keyword_ids: List of keyword IDs to remove (REQUIRED)
- customer_id: Optional

**Get keyword_ids from:**
Use get_campaign_structure to see all keywords with their IDs.

**WARNING: This is PERMANENT and IRREVERSIBLE.**
Keywords removed cannot be recovered. Always confirm with the user first.

**Execution time:** 2-4 seconds

**Example:**
User: "Remove the underperforming keywords"
Agent:
1. Uses get_campaign_structure to show keywords
2. Confirms with user which ones to remove
3. Uses remove_keywords with the keyword_ids

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing keywords",
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID the keywords belong to. Use get_campaign_structure to find this.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "keyword_ids": {
      "description": "List of keyword IDs to remove. Get from get_campaign_structure.",
      "items": {
        "type": "string"
      },
      "title": "Keyword Ids",
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
    "keyword_ids"
  ],
  "title": "RemoveKeywordsInput",
  "type": "object"
}
```

</details>

<a id="remove_negative_keywords"></a>

## `remove_negative_keywords`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove negative keywords from a campaign.

⚠️ **WARNING: This is PERMANENT and IRREVERSIBLE.**
Once removed, the negative keywords cannot be recovered.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED)
- keyword_ids: List of negative keyword IDs to remove (REQUIRED)
- customer_id: Optional

**Get keyword IDs from:**
Use `get_campaign_structure` to see all campaign negative keywords with their IDs.
Look for the "Campaign Negative Keywords" section.

**When to use:**
- Remove accidentally added negative keywords
- Clean up obsolete negative keywords
- Fix over-blocking that's limiting traffic

**Execution time:** 2-4 seconds

**Example:**
User: "Remove the negative keyword 'discount' I added by mistake"
Agent:
1. Uses get_campaign_structure to find the keyword ID
2. Uses remove_negative_keywords with campaign_id and keyword_ids

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing negative keywords from a campaign",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to remove negative keywords from.",
      "title": "Campaign Id",
      "type": "string"
    },
    "keyword_ids": {
      "description": "List of negative keyword IDs to remove. Get IDs from get_campaign_structure (Campaign Negative Keywords section).",
      "items": {
        "type": "string"
      },
      "title": "Keyword Ids",
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
    "keyword_ids"
  ],
  "title": "RemoveNegativeKeywordsInput",
  "type": "object"
}
```

</details>

<a id="remove_pmax_asset_group"></a>

## `remove_pmax_asset_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove (soft-delete) an asset group from a PMax campaign.

Sets status=REMOVED — the group stops serving permanently and disappears from
get_pmax_asset_groups. This cannot be undone via the API. The underlying
assets stay in the Asset Library and remain reusable.

Note: Google rejects removing a campaign's only serving asset group — pause it
instead (update_pmax_asset_group status=PAUSED) if you want to stop delivery.

**Parameters:**
- campaign_id: The PMax campaign ID (REQUIRED)
- asset_group_id: The group to remove (REQUIRED — never auto-picked)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-4 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing (soft-deleting) an asset group.",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "asset_group_id": {
      "description": "The asset group ID to remove (REQUIRED — never auto-picked). Get from get_pmax_asset_groups.",
      "title": "Asset Group Id",
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
    "campaign_id",
    "asset_group_id"
  ],
  "title": "RemovePMaxAssetGroupInput",
  "type": "object"
}
```

</details>

<a id="remove_pmax_asset_group_asset"></a>

## `remove_pmax_asset_group_asset`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Unlink a text or video asset from a Performance Max asset group.

The underlying asset stays in the Asset Library (reusable). Google rejects a
removal that would drop a group below its required minimum for a field type
(e.g. fewer than 3 headlines) — that constraint is surfaced as a clean error.

Pass `asset_group_asset_resource_name` (preferred — from
list_pmax_asset_group_assets) OR `asset_id` (with asset_group_id / field_type
to disambiguate if the same asset is linked more than once).

**Parameters:**
- campaign_id: The PMax campaign ID (REQUIRED)
- asset_group_asset_resource_name: The link to remove (preferred)
- asset_id / field_type / asset_group_id: Alternative lookup by asset ID
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 2-4 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for unlinking a text/video asset from a PMax asset group.",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "asset_group_asset_resource_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Preferred — the link resource name from list_pmax_asset_group_assets.",
      "title": "Asset Group Asset Resource Name"
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
      "description": "Alternative to the resource name: the Asset ID. Pass asset_group_id and/or field_type to disambiguate.",
      "title": "Asset Id"
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
      "description": "Optional disambiguator when using asset_id.",
      "title": "Field Type"
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
      "description": "Optional disambiguator when using asset_id.",
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
  "title": "RemovePMaxAssetGroupAssetInput",
  "type": "object"
}
```

</details>

<a id="remove_pmax_asset_group_image"></a>

## `remove_pmax_asset_group_image`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Unlink an image from a PMax asset group.

This UNLINKS the image — it does NOT delete the underlying Asset. The asset
stays in the Asset Library so it can be re-linked elsewhere or re-added to
the same group later. This matches Google's own UI behavior and is reversible.

**Lookup patterns (pass ONE):**
- A) `asset_group_asset_resource_name` — preferred, get it from
  `list_pmax_asset_group_images`
- B) `asset_id` (+ optional `asset_group_id` if the same asset is linked
  into more than one group)

**Parameters:**
- campaign_id: The PMax campaign ID
- asset_group_asset_resource_name OR asset_id
- asset_group_id: optional disambiguator

**Execution time:** 2-4 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for unlinking an image from a PMax asset group.\n\nPass either `asset_group_asset_resource_name` (preferred — get it from\nlist_pmax_asset_group_images) OR `asset_id` (the underlying Asset ID;\nthe tool will look up the link).",
  "properties": {
    "campaign_id": {
      "description": "The PMax campaign ID (numeric). Example: '21854471508'",
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
      "description": "Asset ID to unlink (numeric). Pass `asset_group_id` too if the same asset is linked into multiple groups.",
      "title": "Asset Id"
    },
    "asset_group_asset_resource_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Direct resource name for the link. Get from list_pmax_asset_group_images. Example: 'customers/123/assetGroupAssets/456~789~MARKETING_IMAGE'",
      "title": "Asset Group Asset Resource Name"
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
      "description": "Optional disambiguator when `asset_id` is linked into more than one asset group.",
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
  "title": "RemovePMaxAssetGroupImageInput",
  "type": "object"
}
```

</details>

<a id="remove_pmax_audience_signal"></a>

## `remove_pmax_audience_signal`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove a specific audience signal from a Performance Max campaign.

Use get_pmax_audience_signals first to get the signal_resource_name.

**Parameters:**
- campaign_id: The PMax campaign ID
- signal_resource_name: Resource name from get_pmax_audience_signals

**Execution time:** 2-5 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing an audience signal from a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Google Ads campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "signal_resource_name": {
      "description": "The resource name of the audience signal to remove. Get from get_pmax_audience_signals tool. Example: 'customers/1234567890/assetGroupSignals/123~456'",
      "title": "Signal Resource Name",
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
    "campaign_id",
    "signal_resource_name"
  ],
  "title": "RemovePMaxAudienceSignalInput",
  "type": "object"
}
```

</details>

<a id="remove_pmax_search_themes"></a>

## `remove_pmax_search_themes`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove specific search themes from a Performance Max campaign.

Matches themes by text (case-insensitive). Use get_pmax_search_themes first to see current themes.

**Parameters:**
- campaign_id: The PMax campaign ID
- themes_to_remove: List of theme text strings to remove

**Execution time:** 2-5 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing search themes from a PMax campaign.",
  "properties": {
    "campaign_id": {
      "description": "The Google Ads campaign ID (numeric). Example: '21854471508'",
      "title": "Campaign Id",
      "type": "string"
    },
    "themes_to_remove": {
      "description": "List of search theme texts to remove (case-insensitive match). Example: ['AI ad management', 'automate google ads']",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "title": "Themes To Remove",
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
    "themes_to_remove"
  ],
  "title": "RemovePMaxSearchThemesInput",
  "type": "object"
}
```

</details>

<a id="remove_product_group"></a>

## `remove_product_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove a product-group node from a Shopping ad group's tree (and its subtree).

Get the criterion_id from get_product_groups. Removing a subdivision removes everything under it.

**Required:** ad_group_id, criterion_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Remove a product-group node (and its subtree).",
  "properties": {
    "ad_group_id": {
      "description": "The Shopping ad group ID.",
      "title": "Ad Group Id",
      "type": "string"
    },
    "criterion_id": {
      "description": "The product-group criterion ID to remove (from get_product_groups).",
      "title": "Criterion Id",
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
    "criterion_id"
  ],
  "title": "RemoveProductGroupInput",
  "type": "object"
}
```

</details>

<a id="remove_sitelinks"></a>

## `remove_sitelinks`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove sitelink extensions from a campaign.

Unlinks sitelinks from THIS campaign. The underlying Asset stays in your account and can be re-linked elsewhere.

**Why this matters:**
- Old policy-violating sitelinks keep serving until removed
- Stale URLs / outdated promotional copy must be removed before adding new ones
- A campaign can only show 8 sitelinks max — must remove older ones to make room

**Parameters:**
- campaign_id: Campaign whose sitelinks to remove (REQUIRED)
- asset_ids: Optional list of asset IDs (or full resource_names) to remove specifically. Get IDs from `list_campaign_extensions`. If omitted, ALL sitelinks on this campaign are removed.
- customer_id: Optional (uses connected account if omitted)

**Workflow:**
1. Call `list_campaign_extensions(campaign_id)` to see what's currently linked
2. Identify which sitelinks to remove by their asset_id or text
3. Call this tool with those asset_ids (or omit to clear ALL)
4. Use `add_sitelinks` to add fresh ones if needed

**Example:**
User: "Remove the old sitelinks from my Krav Maga campaign — they have outdated promo copy"
Agent:
1. list_campaign_extensions → shows 4 sitelinks with their asset_ids
2. Confirms: "I'll remove sitelinks 'Free Trial' and 'Summer Sale 2024'. Proceed?"
3. Calls remove_sitelinks(campaign_id, asset_ids=['12345', '67890'])

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing sitelink extensions from a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to remove sitelinks from. Use list_campaigns first to find campaigns.",
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
      "description": "Optional list of asset IDs (or full resource_names) to remove. Get IDs from list_campaign_extensions. If omitted, ALL sitelinks linked to this campaign are removed.",
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
  "title": "RemoveSitelinksInput",
  "type": "object"
}
```

</details>

<a id="remove_structured_snippets"></a>

## `remove_structured_snippets`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove structured snippet extensions from a campaign.

Unlinks structured snippets from THIS campaign. The underlying Asset stays in your account and can be re-linked elsewhere.

**Why this matters:**
- Stale snippet headers/values (e.g. last season's "Styles" or discontinued "Brands") look bad to users
- Must remove old snippets before fresh ones take their place
- The sibling of `add_structured_snippets` — completes the add/remove pair (like remove_sitelinks / remove_callouts)

**Parameters:**
- campaign_id: Campaign whose structured snippets to remove (REQUIRED)
- asset_ids: Optional list of asset IDs (or full resource_names) to remove specifically. Get IDs from `list_campaign_extensions`. If omitted, ALL structured snippets on this campaign are removed.
- customer_id: Optional (uses connected account if omitted)

**Workflow:**
1. Call `list_campaign_extensions(campaign_id)` to see what's currently linked
2. Identify which snippets to remove by their asset_id
3. Call this tool with those asset_ids (or omit to clear ALL)
4. Use `add_structured_snippets` to add fresh ones if needed

**Example:**
User: "Remove the old structured snippets from my campaign"
Agent:
1. list_campaign_extensions → shows current structured snippets with asset_ids
2. Confirms: "I'll remove all structured snippets. Proceed?"
3. Calls remove_structured_snippets(campaign_id)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for removing structured snippet extensions from a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to remove structured snippets from. Use list_campaigns first to find campaigns.",
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
      "description": "Optional list of asset IDs (or full resource_names) to remove. Get IDs from list_campaign_extensions. If omitted, ALL structured snippets linked to this campaign are removed.",
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
  "title": "RemoveStructuredSnippetsInput",
  "type": "object"
}
```

</details>

<a id="replace_demandgen_audiences"></a>

## `replace_demandgen_audiences`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Replace the grouped audience on a Demand Gen (or YouTube) ad group.

Demand Gen uses a single grouped audience per ad group — you cannot add one more segment
to a live ad group, so this REPLACES the whole audience (removes the old one and builds a
new grouped audience from the segment IDs you pass).

⚠️ Use `search_audiences` FIRST to find real audience IDs — NEVER fabricate IDs (wrong IDs
target unrelated audiences and waste budget).

**Accepts:** in_market_audience_ids, affinity_audience_ids, custom_audience_ids, user_list_ids.
**Required:** ad_group_id + at least one audience ID. Only works on Demand Gen ad groups.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Replace the grouped audience on a Demand Gen ad group. Demand Gen uses a single\ngrouped audience per ad group, so this REPLACES it entirely (remove old + build new).\nUse search_audiences FIRST to find real IDs — never fabricate. At least one required.",
  "properties": {
    "ad_group_id": {
      "description": "Demand Gen ad group ID (from get_campaign_structure).",
      "title": "Ad Group Id",
      "type": "string"
    },
    "in_market_audience_ids": {
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
      "title": "In Market Audience Ids"
    },
    "affinity_audience_ids": {
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
      "title": "Affinity Audience Ids"
    },
    "custom_audience_ids": {
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
      "description": "Custom audience resource names.",
      "title": "Custom Audience Ids"
    },
    "user_list_ids": {
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
      "description": "Remarketing/user-list resource names.",
      "title": "User List Ids"
    },
    "audience_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional name for the new grouped audience.",
      "title": "Audience Name"
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
  "title": "ReplaceDemandGenAudiencesInput",
  "type": "object"
}
```

</details>

<a id="research_keywords"></a>

## `research_keywords`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Research high-intent keywords using Google Keyword Planner API.

⚠️ IMPORTANT: This is a READ-ONLY tool. Safe to call multiple times.

🎯 **What This Tool Does:**
- Researches keywords via Google Keyword Planner API
- Returns keywords with real CPC data, search volume, and competition metrics
- Groups keywords by commercial intent (HIGH/MEDIUM/LOW based on dynamic CPC thresholds)
- Selects top 15-20 keywords optimized for conversions
- Provides budget recommendations based on actual keyword costs

**When to Use:**
- BEFORE creating a Google Search campaign
- When you need data-driven keyword insights
- To understand keyword costs and search volume
- To get budget recommendations

**Parameters:**
- business_description (required): What the business sells/offers
- website_url (optional): Business website for better keyword suggestions
- target_location (optional): Geographic target (default: "United States")
- language (optional): 'de' / 'German' / '1001' — defaults to the language the
  account's campaigns target (auto-detected), falling back to English. For
  non-English seeds, location AND language should match (e.g. German seeds →
  target_location "Germany" + language auto/de).
- seed_keywords (optional): 5-10 seed keywords (will auto-extract if not provided)
- customer_id (optional): Google Ads account ID

**Returns:**
- Keyword table with dynamic CPC thresholds (adapts to any industry)
- HIGH/MEDIUM/LOW intent grouping
- Budget recommendations (Conservative/Moderate/Aggressive)
- Top 15-20 recommended keywords for campaign

**Execution time:** 3-8 seconds (calls live Google Ads API)

📊 **Example Usage:**
1. User: "I want to create a campaign for my plumbing business"
2. YOU call: research_keywords with business_description="Emergency plumbing services"
3. Tool returns: Keyword table with 100+ keywords, 20 recommended, budget suggestions
4. YOU show user: The keyword table and ask if they want modifications
5. User approves or requests changes
6. YOU call: create_search_campaign with approved keywords

💡 **Dynamic Thresholds:** This tool automatically adapts CPC thresholds to any industry:
- Plumbing: HIGH ≥$6, MEDIUM $3-6, LOW <$3
- Legal: HIGH ≥$95, MEDIUM $45-95, LOW <$45
- E-commerce: HIGH ≥$2, MEDIUM $0.50-2, LOW <$0.50

All keywords returned will use **BROAD match** (Google's 2025 recommendation with Smart Bidding).


<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for keyword research using Google Keyword Planner",
  "properties": {
    "business_description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Description of what the business sells/does. Required if seed_keywords not provided. If omitted, inferred from website_url domain.",
      "title": "Business Description"
    },
    "website_url": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Business website URL (helps generate more relevant keywords)",
      "title": "Website Url"
    },
    "target_location": {
      "default": "United States",
      "description": "Geographic target for keyword research (e.g., 'New York, NY', 'Chicago, IL', 'United States', 'Germany')",
      "title": "Target Location",
      "type": "string"
    },
    "language": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Language for keyword research — ISO code ('de'), name ('German'), or Google language ID ('1001'). Default: auto-detected from the account's campaign language targeting (falls back to English). Set this for non-English advertisers if auto-detection picks the wrong language.",
      "title": "Language"
    },
    "seed_keywords": {
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
      "description": "Optional: Provide 5-10 seed keywords. If not provided, they will be extracted from business_description automatically.",
      "title": "Seed Keywords"
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
  "title": "KeywordResearchInput",
  "type": "object"
}
```

</details>

<a id="resolve_google_locations"></a>

## `resolve_google_locations`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Resolve free-text location queries (country, state/province, city, district, postal code) into Google's exact `geoTargetConstants/<id>` resource names.

**WHEN TO USE:**
Call this tool BEFORE `create_display_campaign`, `create_search_campaign`, `create_pmax_campaign`, or `create_demandgen_campaign` whenever the user requests targeting by location. This gets you the precise geoTargetConstants/<id> values the Google Ads API accepts — eliminating ambiguity (e.g., "London" could be London UK, Londonderry, or London Ontario).

**INPUT:** JSON array of free-text queries, optional locale + country_code filter.
**OUTPUT:** For each query, up to N candidate geoTargetConstants with canonical_name, target_type (Country/State/City/District/etc.), country_code, reach estimate. The AI client picks the right ID and passes it to the campaign-creation tool.

**WORKFLOW EXAMPLE:**
1. User says "target London and California"
2. Call `resolve_google_locations` with `queries: ["London","California"]`
3. Disambiguate with the user if multiple candidates exist (e.g., London UK vs London Ontario)
4. Pass chosen resource names (e.g., `["geoTargetConstants/1006886","geoTargetConstants/21137"]`) as `target_locations` to the campaign-creation tool.

Display campaign creation accepts BOTH formats (free-text OR resource names / bare IDs) but the API is most reliable with pre-resolved IDs.

**Execution time:** 1-3 seconds. Redis-cached 5 minutes.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input for resolve_google_locations — resolves free-text queries to geoTargetConstants.\n\nAliases for `queries` accepted for LLM-friendliness:\n  `location_names`, `locations`, `query`",
  "properties": {
    "queries": {
      "description": "JSON ARRAY of free-text location queries. Can be country, state/province, city, district, postal code, etc. Examples: [\"London\", \"California\", \"90210\", \"South Delhi\"]. Max 25 queries per call. (Also accepts the alternate field names `location_names`, `locations`, or `query`.)",
      "items": {
        "type": "string"
      },
      "maxItems": 25,
      "minItems": 1,
      "title": "Queries",
      "type": "array"
    },
    "locale": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "en",
      "description": "ISO locale for match results (e.g., 'en', 'es', 'fr'). Default 'en'.",
      "title": "Locale"
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
      "description": "Optional ISO country code (e.g., 'US', 'IN', 'GB') to CONSTRAIN suggestions. Leave null for GLOBAL matching (recommended when user hasn't specified a country).",
      "title": "Country Code"
    },
    "max_suggestions_per_query": {
      "anyOf": [
        {
          "maximum": 20,
          "minimum": 1,
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 10,
      "description": "Max suggestions returned per query. Default 10, max 20.",
      "title": "Max Suggestions Per Query"
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
    "queries"
  ],
  "title": "ResolveGoogleLocationsInput",
  "type": "object"
}
```

</details>

<a id="resume_ad"></a>

## `resume_ad`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Resume a paused ad to start showing it again.

Only works on PAUSED ads (not REMOVED).

**Parameters:**
- ad_id: The ad ID to resume (REQUIRED)
- ad_group_id: The ad group ID (REQUIRED)
- customer_id: Optional

**Execution time:** 1-2 seconds

**When to use:**
- User says "resume", "turn it back on", "enable"
- User finished making changes
- User wants to reactivate a paused A/B test variant

**Example:**
User: "Turn my paused ad back on"
Agent:
1. Uses get_campaign_structure to find the paused ad
2. Uses resume_ad to enable it

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for resuming a paused ad",
  "properties": {
    "ad_id": {
      "description": "The ad ID to resume. Get from get_campaign_structure.",
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
  "title": "ResumeAdInput",
  "type": "object"
}
```

</details>

<a id="resume_ad_group"></a>

## `resume_ad_group`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Resume a paused ad group (any channel).

Reverses a previous `pause_ad_group`. Only works on PAUSED ad groups (not REMOVED).

**Parameters:**
- ad_group_id: The ad group ID to resume (REQUIRED)
- customer_id: Optional

**Execution time:** 1-2 seconds

**When to use:**
- User finished pre-launch review of a PAUSED ad group and wants it live
- User wants to reactivate a paused A/B-test ad group
- Lifting a temporary pause on a themed ad group

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for resuming a paused ad group (any channel).",
  "properties": {
    "ad_group_id": {
      "description": "The ad group ID to resume. Get from get_campaign_structure or list_ad_groups.",
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
  "title": "ResumeAdGroupInput",
  "type": "object"
}
```

</details>

<a id="resume_campaign"></a>

## `resume_campaign`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Resume a paused campaign.

Resuming a campaign makes ads start showing again.
Only works on PAUSED campaigns (not REMOVED).

**Parameters:**
- campaign_id: The campaign ID (REQUIRED - get from list_campaigns)
- customer_id: Optional (uses connected account if omitted)

**Execution time:** 1-2 seconds

**Returns:**
- Campaign name
- Before status (e.g., PAUSED)
- After status (ENABLED)
- Confirmation message

**When to use:**
- User says "resume", "turn it back on", "start it again"
- User wants to re-enable a paused campaign
- User finished making changes and wants ads to run

**Example:**
User: "Turn my campaign back on"
Agent: Uses resume_campaign with the campaign_id

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for resuming a paused campaign",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to resume. Use list_campaigns first to get available campaign IDs.",
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
  "title": "ResumeCampaignInput",
  "type": "object"
}
```

</details>

<a id="resume_meta_campaign"></a>

## `resume_meta_campaign`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to resume a paused Meta campaign.

IMPORTANT: Resuming a campaign restarts ad delivery. Budget will start being spent again.

Returns:
- Confirmation that campaign is active
- Campaign details
- Ads Manager URL

When to use this tool:
- "Resume my Meta campaign"
- "Turn on my Facebook ads"
- "Reactivate campaign 123456"
- "Start my paused Instagram campaign"

Parameters:
- campaign_id: The Meta Campaign ID to resume (required)

Execution time: 2-5 seconds
Effect: Campaign status changes to ACTIVE immediately

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for resuming a Meta campaign",
  "properties": {
    "campaign_id": {
      "description": "The Meta Campaign ID to resume (required)",
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
  "title": "ResumeMetaCampaignInput",
  "type": "object"
}
```

</details>

<a id="save_business_profile"></a>

## `save_business_profile`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Save or update the user's business profile with provided details.

⚠️ IMPORTANT: This tool WRITES data. Use when user confirms their business profile.

🎯 **What This Tool Does (Performance Agent - Phase 1 Feature 5):**
- Saves user's business profile to database
- Updates existing profile if one exists
- Sets profile source as 'user_confirmed' or 'user_mcp'
- Enables personalized recommendations going forward

**Required Parameters:**
- **business_vertical**: retail, services, technology, healthcare, finance, education, travel, food_beverage, automotive, real_estate
- **business_size**: small (<$50K/month), medium ($50K-$500K/month), large (>$500K/month)
- **primary_goal**: leads, sales, awareness, traffic, engagement, app_installs

**Optional Parameters:**
- **target_audience**: Free-text description (e.g., "B2B enterprise clients")
- **geographic_focus**: local, regional, national, international
- **seasonality**: none, holiday_heavy, summer_peak, winter_peak, q4_heavy, back_to_school
- **customer_id**: Optional (uses connected account if omitted)

**Use this tool when:**
- User provides their business details
- User confirms an inferred profile
- User wants to update their business profile
- After asking user clarifying questions about their business

**Example Usage:**
User: "I run a small local plumbing business targeting homeowners"
→ Call save_business_profile with:
  - business_vertical: "services"
  - business_size: "small"
  - primary_goal: "leads"
  - target_audience: "homeowners"
  - geographic_focus: "local"

**Execution time:** 1-2 seconds (database write)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for saving/updating business profile",
  "properties": {
    "business_vertical": {
      "description": "Business vertical (e.g., 'retail', 'services', 'technology', 'healthcare', 'finance', 'education', 'travel', 'food_beverage', 'automotive', 'real_estate')",
      "title": "Business Vertical",
      "type": "string"
    },
    "business_size": {
      "description": "Business size: 'small' (<$50K/month ad spend), 'medium' ($50K-$500K/month), 'large' (>$500K/month)",
      "title": "Business Size",
      "type": "string"
    },
    "primary_goal": {
      "description": "Primary advertising goal: 'leads', 'sales', 'awareness', 'traffic', 'engagement', 'app_installs'",
      "title": "Primary Goal",
      "type": "string"
    },
    "target_audience": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Target audience description (e.g., 'B2B enterprise clients', 'young professionals 25-35')",
      "title": "Target Audience"
    },
    "geographic_focus": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Geographic focus: 'local', 'regional', 'national', 'international'",
      "title": "Geographic Focus"
    },
    "seasonality": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Seasonality pattern: 'none', 'holiday_heavy', 'summer_peak', 'winter_peak', 'q4_heavy', 'back_to_school'",
      "title": "Seasonality"
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
    "business_vertical",
    "business_size",
    "primary_goal"
  ],
  "title": "BusinessProfileSaveInput",
  "type": "object"
}
```

</details>

<a id="search_audiences"></a>

## `search_audiences`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Search for available audience segments (in-market, affinity, custom).

Use this tool to discover audience segment IDs for:
- **PMax campaigns:** Use IDs with `add_pmax_audience_signal` (audience signals/hints)
- **Demand Gen / YouTube campaigns:** Pass IDs via `audience_segments` parameter in `create_demandgen_campaign` or `create_youtube_campaign` (direct targeting)

**Audience types:**
- **In-market:** Users actively researching products/services (e.g., "Business Software")
- **Affinity:** Users with long-term interests (e.g., "Technology Enthusiasts")
- **Custom:** Your account's existing remarketing/customer match lists

**Parameters:**
- query: Search term (e.g., "advertising services", "SaaS tools")

**Execution time:** 2-5 seconds

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for searching available audiences.",
  "properties": {
    "query": {
      "description": "Search query for discovering audiences. Example: 'business software', 'advertising services', 'technology'",
      "title": "Query",
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
    "query"
  ],
  "title": "SearchAudiencesInput",
  "type": "object"
}
```

</details>

<a id="search_meta_targeting"></a>

## `search_meta_targeting`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to find targeting options for their Meta (Facebook/Instagram) ad campaigns.

This tool searches the Meta Marketing API to find targeting options including interests, behaviors, demographics, locations, and more.

Returns:
- List of targeting options with IDs, names, and audience sizes
- Category/path information for interests and behaviors
- Location details including country, region for geo-targeting

When to use this tool:
- "Find interests related to fitness"
- "What targeting options are available for travel?"
- "Search for locations in California"
- "Find behaviors for online shoppers"
- "What demographics can I target?"
- "Find job titles for marketing professionals"
- "Search for schools like Harvard"

Search Types Available:
- interest: Topics and activities (e.g., 'fitness', 'cooking', 'travel')
- behavior: User behaviors (e.g., 'frequent travelers', 'online shoppers')
- demographic: Demographics (e.g., 'new parents', 'college educated')
- life_event: Life events (e.g., 'recently moved', 'newly engaged')
- location: Geo-targeting (e.g., 'New York', 'California', '90210')
- locale: Language targeting (e.g., 'Spanish', 'French')
- employer: Employer targeting (e.g., 'Google', 'Microsoft')
- job_title: Job title targeting (e.g., 'Software Engineer')
- school: Education school targeting (e.g., 'Harvard', 'Stanford')
- major: Education major targeting (e.g., 'Computer Science')

Parameters:
- search_type: Type of targeting to search (required)
- query: Search query string (required)
- limit: Maximum results (1-100, default: 50)
- locale: Locale for results (default: en_US)
- location_types: For location search - filter by types (country, region, city, zip)
- country_code: For location search - filter by country (e.g., 'US')
- ad_account_id: Required for multi-account users. Get from list_connected_accounts

Execution time: 1-3 seconds
Data source: Meta Marketing API Targeting Search

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for Meta targeting search",
  "properties": {
    "search_type": {
      "description": "Type of targeting to search for:\n- 'interest': Find interests for targeting (e.g., 'fitness', 'cooking', 'travel')\n- 'behavior': Find behaviors for targeting (e.g., 'frequent travelers', 'online shoppers')\n- 'demographic': Find demographic targeting options (e.g., 'new parents', 'college educated')\n- 'life_event': Find life event targeting (e.g., 'recently moved', 'newly engaged')\n- 'location': Find locations for geo-targeting (e.g., 'New York', 'California', '90210')\n- 'locale': Find language targeting options (e.g., 'Spanish', 'French')\n- 'employer': Find employer targeting (e.g., 'Google', 'Microsoft')\n- 'job_title': Find job title targeting (e.g., 'Software Engineer', 'Marketing Manager')\n- 'school': Find education school targeting (e.g., 'Harvard', 'Stanford')\n- 'major': Find education major targeting (e.g., 'Computer Science', 'Business')",
      "title": "Search Type",
      "type": "string"
    },
    "query": {
      "description": "Search query string (e.g., 'fitness' for interests, 'New York' for locations)",
      "title": "Query",
      "type": "string"
    },
    "limit": {
      "default": 50,
      "description": "Maximum number of results to return (1-100). Default is 50.",
      "title": "Limit",
      "type": "integer"
    },
    "locale": {
      "default": "en_US",
      "description": "Locale for results (e.g., 'en_US', 'es_ES', 'fr_FR'). Default is 'en_US'.",
      "title": "Locale",
      "type": "string"
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
      "description": "For location search only: filter by location types. Options: 'country', 'region', 'city', 'zip', 'geo_market', 'place'. Example: ['city', 'region']",
      "title": "Location Types"
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
      "description": "For location search only: filter results to a specific country (e.g., 'US', 'GB', 'CA')",
      "title": "Country Code"
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
    "search_type",
    "query"
  ],
  "title": "SearchMetaTargetingInput",
  "type": "object"
}
```

</details>

<a id="search_tools"></a>

## `search_tools`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Find the right Adspirer tool(s) for a task by describing what you want to do in natural language. Returns the best-matching tool names with a one-line summary — then call `get_tool_schema` with a name to get its exact parameters before calling it. Use this instead of guessing tool names. Optionally filter by `platform` (google-ads, meta-ads, tiktok-ads, linkedin-ads, amazon-ads, chatgpt-ads, microsoft-ads).

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "query": {
      "description": "Natural-language description of what you want to do, e.g. 'pause a campaign', 'add UTM tracking', 'set a frequency cap'.",
      "title": "Query",
      "type": "string"
    },
    "platform": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "STRONGLY RECOMMENDED when you know it: the ad platform for this task — one of google-ads, meta-ads, tiktok-ads, linkedin-ads, amazon-ads, chatgpt-ads, microsoft-ads. Passing it greatly improves results, since many platforms have similar tools. Infer it from context (the campaign/account the user is working with).",
      "title": "Platform"
    },
    "top_k": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 10,
      "description": "How many matching tools to return (default 10, max 25).",
      "title": "Top K"
    }
  },
  "required": [
    "query"
  ],
  "title": "SearchToolsInput",
  "type": "object"
}
```

</details>

<a id="select_google_campaign_type"></a>

## `select_google_campaign_type`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

**USE THIS TOOL FIRST WHEN:** User wants to create a Google Ads campaign but hasn't specified the campaign type.

**IMPORTANT:** Call BEFORE any keyword research, asset discovery, or campaign creation when the user says things like:
- "Create a Google Ads campaign"
- "I want to run Google Ads"
- "Set up a Google advertising campaign"
- "Help me create ads on Google"
- "Create a campaign"
- "Run ads"

This tool guides the user to select their campaign TYPE, then returns a step-by-step workflow with which tools to call next.

**Campaign Types Available:**
1. **search** — Text ads in Google Search results (best for high-intent keywords, lead gen, local services)
2. **pmax** — Performance Max across all Google channels (best for ecommerce, brand awareness, multi-channel reach)
3. **youtube** — Video ads on YouTube (best for video content, brand storytelling, product demos)
4. **demandgen** — Demand Gen across YouTube + Gmail + Discover + Display (best for cross-channel mid-funnel)
5. **display** — Responsive Display Ads on the Google Display Network (GDN) — banner placements on millions of websites, apps, and YouTube display slots. Smart Display (`smart_display=true`) is a Google-managed variant within this type.

**Returns:** step-by-step workflow, requirements, and a natural follow-up question for the chosen type.

**Do NOT use this tool if:**
- User specifically asks for "search campaign" or "text ads" → go directly to research_keywords then create_search_campaign
- User specifically asks for "PMax" or "Performance Max" → go directly to discover_existing_assets then create_pmax_campaign
- User specifically asks for "YouTube campaign" or "video campaign" → go directly to validate_video then create_youtube_campaign
- User specifically asks for "Demand Gen" → go directly to create_demandgen_campaign
- User specifically asks for "Display campaign", "banner ads", or "GDN" → go directly to create_display_campaign
- User is asking about performance/analytics → use get_campaign_performance
- User is asking about existing campaigns → use list_campaigns

**Parameters:**
- campaign_type: 'search' | 'pmax' | 'youtube' | 'demandgen' | 'display'

**Execution time:** Instant (no API call)

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for selecting Google Ads campaign type",
  "properties": {
    "campaign_type": {
      "description": "Type of Google Ads campaign to create. Options: 'search' (text ads in search results), 'pmax' (Performance Max across all Google channels), 'youtube' (video ads on YouTube), 'demandgen' (Demand Gen across YouTube/Gmail/Discover/Display), 'display' (Responsive Display Ads on the Google Display Network)",
      "title": "Campaign Type",
      "type": "string"
    }
  },
  "required": [
    "campaign_type"
  ],
  "title": "SelectGoogleCampaignTypeInput",
  "type": "object"
}
```

</details>

<a id="select_meta_campaign_type"></a>

## `select_meta_campaign_type`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://mcp.adspirer.com/api/v1/tools)

User wants to create a Meta (Facebook/Instagram) ad campaign but hasn't specified the campaign type (image, video, carousel, or app).

IMPORTANT: This tool should be called BEFORE any asset discovery or campaign creation when the user says things like:
- "Create a Meta campaign"
- "Create a Facebook ad"
- "I want to run Instagram ads"
- "Set up a Meta advertising campaign"
- "Help me create ads on Facebook"
- "Promote my mobile app on Meta / drive app installs"

This tool asks the user what TYPE of campaign they want to create, then provides guidance on the next steps.

Campaign Types Available:
1. image - Single image ad (most common, good for static visuals)
2. video - Video ad including Reels (good for engagement, storytelling)
3. carousel - 2-10 swipeable cards (good for showcasing multiple products)
4. app - Mobile App Promotion (OUTCOME_APP_PROMOTION). Optimizes for app installs or in-app events. Requires Facebook App ID + App/Play Store URL. Picks creative format (image/video/carousel/DCO) inside the workflow.

Do NOT use this tool if:
- User specifically asks for "image campaign" - use create_meta_image_campaign
- User specifically asks for "video campaign" or "Reels" - use create_meta_video_campaign
- User specifically asks for "carousel campaign" - use create_meta_carousel_campaign
- User is asking about performance/analytics - use performance analysis tools

For app campaigns: ALWAYS use this tool first (with campaign_type='app') even when the user is specific about app — the workflow gathers required app_id + app_store_url and explains the FB App ID vs bundle/package ID distinction (a common customer trip-up).

Parameters:
- campaign_type: 'image', 'video', 'carousel', or 'app'

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for selecting Meta campaign type",
  "properties": {
    "campaign_type": {
      "description": "Type of Meta campaign to create. Options: 'image' (single image ad), 'video' (video/Reels ad), 'carousel' (2-10 swipeable cards), 'app' (mobile app promotion — install or in-app event optimization), 'catalog' (Advantage+ Catalog / Dynamic Product Ads — automatically show products from a Meta product catalog).",
      "title": "Campaign Type",
      "type": "string"
    }
  },
  "required": [
    "campaign_type"
  ],
  "title": "SelectMetaCampaignTypeInput",
  "type": "object"
}
```

</details>

<a id="set_ad_group_device_bid_modifiers"></a>

## `set_ad_group_device_bid_modifiers`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Set device bid modifiers on an AD GROUP — bid up/down per device, finer than the campaign level.

Adjusts (or creates) MOBILE/TABLET/DESKTOP bid modifiers on ONE ad group. Update-or-
create: existing device bids are updated, missing ones are created. Idempotent on re-set.

**Each entry:**
- device: MOBILE | TABLET | DESKTOP
- bid_modifier: 1.2 = +20%, 0.8 = -20%, 1.0 = no change

**Required:** ad_group_id + 1+ devices.

Note: DemandGen ad groups use smart bidding and don't support device bid modifiers
(guarded cleanly). CONNECTED_TV/OTHER are campaign-level only.

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "_DeviceBid": {
      "description": "One device bid modifier.",
      "properties": {
        "device": {
          "description": "MOBILE | TABLET | DESKTOP | CONNECTED_TV | OTHER.",
          "title": "Device",
          "type": "string"
        },
        "bid_modifier": {
          "description": "Bid adjustment (1.2 = +20%, 0.8 = -20%, 1.0 = no change).",
          "maximum": 10.0,
          "minimum": 0.1,
          "title": "Bid Modifier",
          "type": "number"
        }
      },
      "required": [
        "device",
        "bid_modifier"
      ],
      "title": "_DeviceBid",
      "type": "object"
    }
  },
  "description": "Set device bid modifiers on an AD GROUP (update existing, create if absent).\n\nFiner-grained than set_campaign_device_bid_modifiers — lets you bid up/down per\ndevice on a single ad group. Ad-group device modifiers cover MOBILE/TABLET/DESKTOP.",
  "properties": {
    "ad_group_id": {
      "description": "Ad group ID (from get_campaign_structure).",
      "title": "Ad Group Id",
      "type": "string"
    },
    "devices": {
      "description": "1+ device bid modifiers (device = MOBILE|TABLET|DESKTOP). e.g. [{'device':'MOBILE','bid_modifier':1.2}].",
      "items": {
        "$ref": "#/$defs/_DeviceBid"
      },
      "minItems": 1,
      "title": "Devices",
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
    "ad_group_id",
    "devices"
  ],
  "title": "SetAdGroupDeviceBidModifiersInput",
  "type": "object"
}
```

</details>

<a id="set_call_asset_status"></a>

## `set_call_asset_status`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Pause or re-enable phone (CALL) asset links on a campaign — without deleting them.

Pausing stops the number from showing while keeping it linked; enabling turns
it back on. To fully unlink, use remove_call_assets.

**Parameters:**
- campaign_id: The campaign ID (REQUIRED)
- status: 'PAUSED' or 'ENABLED' (REQUIRED)
- asset_ids: Optional list of asset IDs / resource_names (get from
  list_call_assets). OMIT to change ALL call assets on the campaign.
- customer_id: Optional Google Ads customer ID

**Execution time:** 2-4 seconds

**Example:**
User: "Pause the old phone number before I add the new one"
Agent:
1. list_call_assets to find the old asset ID
2. set_call_asset_status(campaign_id="19850524478", status="PAUSED", asset_ids=["..."])

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for pausing / re-enabling CALL asset links on a campaign.",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID (numeric). Get from list_campaigns.",
      "title": "Campaign Id",
      "type": "string"
    },
    "status": {
      "description": "New status for the call asset link: 'PAUSED' to stop showing the number (without deleting it) or 'ENABLED' to turn it back on. To fully unlink, use remove_call_assets instead.",
      "title": "Status",
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
      "description": "Optional list of asset IDs (or full resource_names) to change. Get IDs from list_call_assets. If omitted, ALL call assets on the campaign are set to this status.",
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
    "campaign_id",
    "status"
  ],
  "title": "SetCallAssetStatusInput",
  "type": "object"
}
```

</details>

<a id="set_campaign_ad_schedule"></a>

## `set_campaign_ad_schedule`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Add ad-schedule (day/hour) targeting to a campaign — control WHEN ads run.

⚠️ Adding any schedule restricts ads to ONLY the windows you specify (all other
times are off). Add every window you want ads to run in.

**Each window:**
- day_of_week: MONDAY..SUNDAY
- start_hour (0-23) + end_hour (0-24; 24 = midnight)
- start_minute/end_minute: ZERO | FIFTEEN | THIRTY | FORTY_FIVE (optional)
- bid_modifier (optional, 1.2 = +20%)

**Example:** business hours = [{day_of_week:'MONDAY',start_hour:9,end_hour:17}, ...Tue-Fri].

**Note:** this APPENDS schedule windows (re-adding the same window errors). To fully
replace a schedule, remove the existing ad-schedule criteria first.

**Required:** campaign_id + 1+ schedules.

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "_AdScheduleWindow": {
      "description": "One ad-schedule window: a day + hour range, optional bid modifier.",
      "properties": {
        "day_of_week": {
          "description": "MONDAY | TUESDAY | ... | SUNDAY.",
          "title": "Day Of Week",
          "type": "string"
        },
        "start_hour": {
          "description": "Start hour 0-23.",
          "maximum": 23,
          "minimum": 0,
          "title": "Start Hour",
          "type": "integer"
        },
        "end_hour": {
          "description": "End hour 0-24 (24 = midnight).",
          "maximum": 24,
          "minimum": 0,
          "title": "End Hour",
          "type": "integer"
        },
        "start_minute": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": "ZERO",
          "description": "ZERO | FIFTEEN | THIRTY | FORTY_FIVE.",
          "title": "Start Minute"
        },
        "end_minute": {
          "anyOf": [
            {
              "type": "string"
            },
            {
              "type": "null"
            }
          ],
          "default": "ZERO",
          "description": "ZERO | FIFTEEN | THIRTY | FORTY_FIVE.",
          "title": "End Minute"
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
          "description": "Optional bid adjustment (1.2 = +20%).",
          "title": "Bid Modifier"
        }
      },
      "required": [
        "day_of_week",
        "start_hour",
        "end_hour"
      ],
      "title": "_AdScheduleWindow",
      "type": "object"
    }
  },
  "description": "Add ad-schedule (day/hour) targeting to a campaign.\n\nEach window narrows WHEN ads can show. Adding any schedule means ads only run\nduring the windows you specify (all other times are off). Add all the windows\nyou want ads to run in.",
  "properties": {
    "campaign_id": {
      "description": "Campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "schedules": {
      "description": "1+ day/hour windows. e.g. [{'day_of_week':'MONDAY','start_hour':9,'end_hour':17}].",
      "items": {
        "$ref": "#/$defs/_AdScheduleWindow"
      },
      "minItems": 1,
      "title": "Schedules",
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
    "schedules"
  ],
  "title": "SetCampaignAdScheduleInput",
  "type": "object"
}
```

</details>

<a id="set_campaign_device_bid_modifiers"></a>

## `set_campaign_device_bid_modifiers`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Set device bid modifiers on a campaign — bid up/down per device.

Campaigns automatically have MOBILE/DESKTOP/TABLET criteria; this updates their
bid adjustments (creates CONNECTED_TV/OTHER if you target them).

**Each entry:**
- device: MOBILE | TABLET | DESKTOP | CONNECTED_TV | OTHER
- bid_modifier: 1.2 = +20%, 0.8 = -20%, 1.0 = no change

**Required:** campaign_id + 1+ devices.

<details>
<summary>Full input schema</summary>

```json
{
  "$defs": {
    "_DeviceBid": {
      "description": "One device bid modifier.",
      "properties": {
        "device": {
          "description": "MOBILE | TABLET | DESKTOP | CONNECTED_TV | OTHER.",
          "title": "Device",
          "type": "string"
        },
        "bid_modifier": {
          "description": "Bid adjustment (1.2 = +20%, 0.8 = -20%, 1.0 = no change).",
          "maximum": 10.0,
          "minimum": 0.1,
          "title": "Bid Modifier",
          "type": "number"
        }
      },
      "required": [
        "device",
        "bid_modifier"
      ],
      "title": "_DeviceBid",
      "type": "object"
    }
  },
  "description": "Set device bid modifiers on a campaign (update existing, create if absent).\n\nCampaigns auto-have MOBILE/DESKTOP/TABLET criteria; this updates their bid\nadjustments so you can bid up/down per device.",
  "properties": {
    "campaign_id": {
      "description": "Campaign ID (from list_campaigns).",
      "title": "Campaign Id",
      "type": "string"
    },
    "devices": {
      "description": "1+ device bid modifiers. e.g. [{'device':'MOBILE','bid_modifier':1.2}].",
      "items": {
        "$ref": "#/$defs/_DeviceBid"
      },
      "minItems": 1,
      "title": "Devices",
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
    "devices"
  ],
  "title": "SetCampaignDeviceBidModifiersInput",
  "type": "object"
}
```

</details>

<a id="start_here"></a>

## `start_here`

Scope: **supporting** · Capability: **utilities** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Show the user where to start and what to try next with Adspirer — a visual 'first wins' guide personalized to their connected platforms, real account data, and what they've already done.

**Call this when:**
- A user has just connected Adspirer (first session, few or no tool calls yet)
- The user asks "what can you do?", "where do I start?", "what should I try?", or anything about Adspirer's capabilities
- The user seems unsure what to do next

Free — never counts against the user's quota. Renders an interactive getting-started card; the text fallback lists the same steps.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "start_here takes no arguments — everything is resolved from the user.",
  "properties": {},
  "title": "StartHereInput",
  "type": "object"
}
```

</details>

<a id="suggest_ad_content"></a>

## `suggest_ad_content`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Generate AI-suggested headlines and descriptions based on campaign keywords.

Analyzes campaign keywords and generates optimized ad content following creative guidelines:
- 15 headlines across 3 categories (What It Is, Benefits, Pain/Proof/CTA)
- 4 descriptions with value props and CTAs
- All validated for character limits

**Parameters:**
- campaign_id: The campaign to analyze (REQUIRED)
- business_description: Optional context about the business
- key_benefits: Optional list of benefits (e.g., ["fast setup", "no dashboard"])
- proof_points: Optional proof points (e.g., [{"number": "2000+", "metric": "campaigns"}])
- pain_points: Optional pain points (e.g., ["manual ads", "complex UI"])
- customer_id: Optional

**Returns:**
- suggested_headlines: 15 headlines ready to use
- suggested_descriptions: 4 descriptions ready to use
- headline_categories: Headlines organized by category
- keyword_themes: Top themes from campaign keywords

**Use this when:**
- User wants fresh ad copy ideas
- User asks "what should my headlines be?"
- Starting a new A/B test
- Refreshing stale ad content

**Execution time:** 3-5 seconds

**Example:**
User: "Suggest some better headlines for my campaign"
Agent:
1. Uses suggest_ad_content to generate ideas
2. Shows suggestions organized by category
3. User picks favorites
4. Uses update_ad_headlines to apply selected headlines

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for AI-powered ad content suggestions",
  "properties": {
    "campaign_id": {
      "description": "The campaign ID to analyze for keyword themes. Use list_campaigns first.",
      "title": "Campaign Id",
      "type": "string"
    },
    "business_description": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Optional: Description of what the business does. Helps generate better suggestions.",
      "title": "Business Description"
    },
    "key_benefits": {
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
      "description": "Optional: List of key benefits (e.g., ['30 second launch', 'no dashboard required']).",
      "title": "Key Benefits"
    },
    "proof_points": {
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
      "description": "Optional: Proof points. Each with 'number' and 'metric' (e.g., {'number': '2000+', 'metric': 'campaigns'}).",
      "title": "Proof Points"
    },
    "pain_points": {
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
      "description": "Optional: Pain points customers face (e.g., ['manual ads', 'complex UI']).",
      "title": "Pain Points"
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
  "title": "SuggestAdContentInput",
  "type": "object"
}
```

</details>

<a id="switch_primary_account"></a>

## `switch_primary_account`

Scope: **supporting** · Capability: **accounts** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Activate ad accounts for a platform.

Two modes:

1. `account_id` (singular) — ADDS this account to the active set. Other
   already-active accounts stay active. Safe to call multiple times to
   activate accounts one by one.

2. `account_ids` (plural, list) — REPLACES the full active set with this
   exact list. Any account NOT in the list becomes inactive. Use this only
   when the user explicitly wants to set a specific group of accounts as
   the complete active set (e.g., "only use accounts A, B, C").

Use this tool when:
- User wants to activate a different ad account (use account_id — singular)
- User wants to activate multiple specific accounts (use account_ids — plural)
- User says "also use my other account" (use account_id — additive)
- User says "only use accounts X, Y" (use account_ids — replace)

Get account IDs from get_connections_status.

IMPORTANT: Returns updated connections list after activation.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Input schema for switch_primary_account tool",
  "properties": {
    "platform": {
      "description": "Platform to switch primary account for: google_ads, tiktok_ads, meta_ads, or linkedin_ads",
      "title": "Platform",
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
      "description": "Single account ID to activate (e.g., '1234567890' for Google Ads). This ADDS the account to the active set — other already-active accounts stay active. Use this OR account_ids, not both.",
      "title": "Account Id"
    },
    "account_ids": {
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
      "description": "EXPLICIT full list of account IDs that should be active. Any account NOT in this list is set to inactive. Use this ONLY when you want to replace the entire active-account set in one call. If you just want to activate one more account, use `account_id` (singular) instead — it adds without deactivating others. Get account IDs from get_connections_status.",
      "title": "Account Ids"
    }
  },
  "required": [
    "platform"
  ],
  "title": "SwitchPrimaryAccountInput",
  "type": "object"
}
```

</details>

<a id="unlink_merchant_center"></a>

## `unlink_merchant_center`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://mcp.adspirer.com/api/v1/tools)

Remove a Merchant Center link from this Google Ads account.

Detaches the Merchant Center account; Shopping campaigns relying on it will stop
serving. The Merchant Center account itself is not deleted. Get the merchant_center_id
from get_merchant_center_links.

**Required:** merchant_center_id.

<details>
<summary>Full input schema</summary>

```json
{
  "description": "Remove a Merchant Center link from this Google Ads account.",
  "properties": {
    "merchant_center_id": {
      "description": "The Merchant Center account ID to unlink (from get_merchant_center_links).",
      "title": "Merchant Center Id",
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
    "merchant_center_id"
  ],
  "title": "UnlinkMerchantCenterInput",
  "type": "object"
}
```

</details>

