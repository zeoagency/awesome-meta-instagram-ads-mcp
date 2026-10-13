# proxy-intell/facebook-ads-library-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/proxy-intell/facebook-ads-library-mcp) · [Machine-readable snapshot](../../catalog/proxy-intell--facebook-ads-library-mcp.json)

Complete registered tool snapshot. **8 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`3a3bf3c84c47`](https://github.com/proxy-intell/facebook-ads-library-mcp/tree/3a3bf3c84c474ff5079c00c2445a642609e42146). Method: `runtime-tools-list`.

- Uses third-party ScrapeCreators for Ad Library retrieval. The full self-hosted inventory is captured; hosted-service parity is not established.
- analyze_ad_image has a source-level handler bug at this revision; its full schema remains visible, with the limitation labeled.

## Tools

- [analyze_ad_image](#analyze_ad_image)
- [analyze_ad_video](#analyze_ad_video)
- [analyze_ad_videos_batch](#analyze_ad_videos_batch)
- [cleanup_media_cache](#cleanup_media_cache)
- [get_cache_stats](#get_cache_stats)
- [get_meta_ads](#get_meta_ads)
- [get_meta_platform_id](#get_meta_platform_id)
- [search_cached_media](#search_cached_media)

<a id="analyze_ad_image"></a>

## `analyze_ad_image`

Scope: **supporting** · Capability: **creatives** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L380)

REQUIRED for analyzing images from Facebook ads. Download and analyze ad images to extract visual elements, text content, colors, people, brand elements, and composition details. This tool should be used for EVERY image URL returned by get_meta_ads when doing comprehensive analysis. Uses intelligent caching so multiple image analysis calls are efficient and cost-free.

Implementation note: At this revision, the handler references undefined media_url instead of its media_urls argument before its exception block. Image analysis cannot run as advertised; this tool is excluded from capability grouping.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "media_urls": {
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
      "title": "Media Urls"
    },
    "brand_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Brand Name"
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
    }
  },
  "required": [
    "media_urls"
  ],
  "title": "analyze_ad_imageArguments",
  "type": "object"
}
```

</details>

<a id="analyze_ad_video"></a>

## `analyze_ad_video`

Scope: **supporting** · Capability: **creatives** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L794)

REQUIRED for analyzing video ads from Facebook. Download and analyze ad videos using Gemini's advanced video understanding capabilities. Extracts visual storytelling, audio elements, pacing, scene transitions, brand messaging, and marketing strategy insights. Uses intelligent caching for efficiency and includes comprehensive video analysis.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "media_url": {
      "title": "Media Url",
      "type": "string"
    },
    "brand_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Brand Name"
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
    }
  },
  "required": [
    "media_url"
  ],
  "title": "analyze_ad_videoArguments",
  "type": "object"
}
```

</details>

<a id="analyze_ad_videos_batch"></a>

## `analyze_ad_videos_batch`

Scope: **supporting** · Capability: **creatives** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L1044)

REQUIRED for batch analyzing multiple video ads from Facebook for maximum token efficiency. Download and analyze multiple ad videos using Gemini's advanced video understanding in a single API call. This significantly reduces token costs compared to individual video analysis. Uses intelligent caching and includes comprehensive batch video analysis with shared prompt optimization.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "media_urls": {
      "items": {
        "type": "string"
      },
      "title": "Media Urls",
      "type": "array"
    },
    "brand_names": {
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
      "title": "Brand Names"
    },
    "ad_ids": {
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
      "title": "Ad Ids"
    }
  },
  "required": [
    "media_urls"
  ],
  "title": "analyze_ad_videos_batchArguments",
  "type": "object"
}
```

</details>

<a id="cleanup_media_cache"></a>

## `cleanup_media_cache`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L723)

REQUIRED for cleaning up old cached media files (images and videos) and freeing disk space. Use this tool when users want to remove old cached media, clean up storage space, or when cache becomes too large. Essential for cache maintenance and storage management.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "max_age_days": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 30,
      "title": "Max Age Days"
    }
  },
  "title": "cleanup_media_cacheArguments",
  "type": "object"
}
```

</details>

<a id="get_cache_stats"></a>

## `get_cache_stats`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L590)

REQUIRED for checking media cache status and storage usage. Use this tool when users ask about cache statistics, storage space used by cached media (images and videos), or how many files have been analyzed and cached. Essential for cache management and monitoring.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {},
  "title": "get_cache_statsArguments",
  "type": "object"
}
```

</details>

<a id="get_meta_ads"></a>

## `get_meta_ads`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L189)

Retrieve currently running ads for a brand using their Meta Platform ID. Use this tool after getting a platform ID from get_meta_platform_id. This tool fetches active advertisements from the Meta Ad Library, including ad content, media URLs, dates, and targeting information. For complete analysis of visual elements, colors, design, or image content, you MUST also use analyze_ad_image on the media_url from each ad.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "platform_ids": {
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
      "title": "Platform Ids"
    },
    "limit": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 50,
      "title": "Limit"
    },
    "country": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Country"
    },
    "trim": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": true,
      "title": "Trim"
    }
  },
  "required": [
    "platform_ids"
  ],
  "title": "get_meta_adsArguments",
  "type": "object"
}
```

</details>

<a id="get_meta_platform_id"></a>

## `get_meta_platform_id`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L34)

Search for companies or brands in the Meta Ad Library and return their platform IDs. Use this tool when you need to find a brand's Meta Platform ID before retrieving their ads. This tool searches the Facebook Ad Library to find matching brands and their associated Meta Platform IDs for ad retrieval.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "brand_names": {
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
      "title": "Brand Names"
    }
  },
  "required": [
    "brand_names"
  ],
  "title": "get_meta_platform_idArguments",
  "type": "object"
}
```

</details>

<a id="search_cached_media"></a>

## `search_cached_media`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/proxy-intell/facebook-ads-library-mcp/blob/3a3bf3c84c474ff5079c00c2445a642609e42146/mcp_server.py#L637)

REQUIRED for finding previously analyzed ad media (images and videos) in cache. Use this tool when users want to search for cached media by brand name, find media with people, search by colors, or filter by media type. Essential for retrieving past analysis results without re-downloading media.

<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "brand_name": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Brand Name"
    },
    "has_people": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Has People"
    },
    "color_contains": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Color Contains"
    },
    "media_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Media Type"
    },
    "limit": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": 20,
      "title": "Limit"
    }
  },
  "title": "search_cached_mediaArguments",
  "type": "object"
}
```

</details>

