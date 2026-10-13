# RamsesAguirre777/facebook-ads-library-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/RamsesAguirre777/facebook-ads-library-mcp) · [Machine-readable snapshot](../../catalog/RamsesAguirre777--facebook-ads-library-mcp.json)

Complete registered tool snapshot. **2 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`ea3c877855c1`](https://github.com/RamsesAguirre777/facebook-ads-library-mcp/tree/ea3c877855c16fb4594f640634d06f85e414eadb). Method: `runtime-tools-list`.

- Uses headless-browser Ad Library scraping. Source parameter notes are included separately; prose options are not enforced schema enums.

## Tools

- [scrape_ad_library_url](#scrape_ad_library_url)
- [search_ad_library](#search_ad_library)

<a id="scrape_ad_library_url"></a>

## `scrape_ad_library_url`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://github.com/RamsesAguirre777/facebook-ads-library-mcp/blob/ea3c877855c16fb4594f640634d06f85e414eadb/facebook_ads_mcp_complete.py#L260)

Scrape any Facebook Ad Library URL you already have (a prefilled search, an advertiser's 'view all ads' page, a shared filter link) and return structured ad cards plus the raw rendered text.

### Source parameter notes

Args:
    url: a facebook.com/ads/library/... URL
    wait_seconds: SPA hydration wait before scraping
    scroll_rounds: infinite-scroll cycles to load more cards (0 = first render only)

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "url": {
      "type": "string"
    },
    "wait_seconds": {
      "default": 8,
      "type": "integer"
    },
    "scroll_rounds": {
      "default": 8,
      "type": "integer"
    }
  },
  "required": [
    "url"
  ]
}
```

</details>

<a id="search_ad_library"></a>

## `search_ad_library`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://github.com/RamsesAguirre777/facebook-ads-library-mcp/blob/ea3c877855c16fb4594f640634d06f85e414eadb/facebook_ads_mcp_complete.py#L176)

Search the public Facebook Ad Library for a keyword in a given country (works for commercial ads, any country — no token). Renders the SPA with a headless browser, scrolls past the first page, and returns structured ad cards: advertiser, run date, creative count, landing domain, CTA button, headline and body copy. Pass advertiser_page_id to pull every ad from one Page.

### Source parameter notes

Args:
    query: keyword(s) to search (advertiser name, product, angle...). Optional if
           advertiser_page_id is given.
    country: ISO country code the ads were delivered in (MX, US, ES, ...)
    active_status: active | inactive | all
    ad_type: all | political_and_issue_ads | employment_ads | housing_ads | financial_products_and_services_ads
    media_type: all | image | meme | video | none
    advertiser_page_id: if set, target that Page's "all ads" view instead of a keyword
           search. This view is heavier client-rendered and does not always hydrate
           headless — a keyword search of the advertiser's name is the more reliable path.
    wait_seconds: how long to let the SPA hydrate before scraping (raise if results are empty)
    scroll_rounds: infinite-scroll cycles to load more ads past the first ~24
           (0 = first render only, fast; 8 default; 15+ for a deep sweep)

<details>
<summary>Full input schema</summary>

```json
{
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "query": {
      "default": "",
      "type": "string"
    },
    "country": {
      "default": "MX",
      "type": "string"
    },
    "active_status": {
      "default": "active",
      "type": "string"
    },
    "media_type": {
      "default": "all",
      "type": "string"
    },
    "ad_type": {
      "default": "all",
      "type": "string"
    },
    "advertiser_page_id": {
      "default": "",
      "type": "string"
    },
    "wait_seconds": {
      "default": 8,
      "type": "integer"
    },
    "scroll_rounds": {
      "default": 8,
      "type": "integer"
    }
  }
}
```

</details>

