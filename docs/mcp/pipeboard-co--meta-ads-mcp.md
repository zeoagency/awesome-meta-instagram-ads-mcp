# pipeboard-co/meta-ads-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/pipeboard-co/meta-ads-mcp) · [Machine-readable snapshot](../../catalog/pipeboard-co--meta-ads-mcp.json)

Complete registered tool snapshot. **41 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`093062c66556`](https://github.com/pipeboard-co/meta-ads-mcp/tree/093062c6655682a20ff0814b468e0e877263d494). Method: `runtime-tools-list`.

- 41-tool union with optional registrations enabled; default configuration exposes 35. Optional tools are labeled below.
- generate_report is an upgrade stub. Duplication forwards to Pipeboard; the hosted service may expose a different inventory.

## Tools

- [compute_image_crops](#compute_image_crops)
- [create_ad](#create_ad)
- [create_ad_creative](#create_ad_creative)
- [create_adset](#create_adset)
- [create_budget_schedule](#create_budget_schedule)
- [create_campaign](#create_campaign)
- [duplicate_ad](#duplicate_ad)
- [duplicate_adset](#duplicate_adset)
- [duplicate_campaign](#duplicate_campaign)
- [duplicate_creative](#duplicate_creative)
- [estimate_audience_size](#estimate_audience_size)
- [generate_report](#generate_report)
- [get_account_info](#get_account_info)
- [get_account_pages](#get_account_pages)
- [get_ad_accounts](#get_ad_accounts)
- [get_ad_creatives](#get_ad_creatives)
- [get_ad_details](#get_ad_details)
- [get_ad_image](#get_ad_image)
- [get_ad_video](#get_ad_video)
- [get_ads](#get_ads)
- [get_adset_details](#get_adset_details)
- [get_adsets](#get_adsets)
- [get_campaign_details](#get_campaign_details)
- [get_campaigns](#get_campaigns)
- [get_creative_details](#get_creative_details)
- [get_image_by_hash](#get_image_by_hash)
- [get_insights](#get_insights)
- [get_interest_suggestions](#get_interest_suggestions)
- [get_login_link](#get_login_link)
- [save_ad_image_locally](#save_ad_image_locally)
- [search_ads_archive](#search_ads_archive)
- [search_behaviors](#search_behaviors)
- [search_demographics](#search_demographics)
- [search_geo_locations](#search_geo_locations)
- [search_interests](#search_interests)
- [search_pages_by_name](#search_pages_by_name)
- [update_ad](#update_ad)
- [update_ad_creative](#update_ad_creative)
- [update_adset](#update_adset)
- [update_campaign](#update_campaign)
- [upload_ad_image](#upload_ad_image)

<a id="compute_image_crops"></a>

## `compute_image_crops`

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L1591)


Compute image_crops coordinates for a source image of the given dimensions.

Returns the image_crops dict ready to pass directly to create_ad_creative
or bulk_create_ad_creatives. For each crop key the result is the largest
centered region that fits within the source image while matching the key's
aspect ratio — equivalent to "Original" crop (no content is cut off beyond
what the ratio requires).

Args:
    image_width: Width of the source image in pixels (e.g. 1080).
    image_height: Height of the source image in pixels (e.g. 1080).
    crop_keys: Optional list of specific crop keys to compute. Defaults to
        all 6 keys accepted by Meta's API:
          "100x100"  — 1:1 square (Feed, Marketplace, Search)
          "100x72"   — ~1.39:1 horizontal (Marketplace, some placements)
          "400x500"  — 4:5 portrait (Feed on mobile, Stories fallback)
          "400x150"  — ~2.67:1 wide banner (Audience Network)
          "600x360"  — ~1.67:1 horizontal (Right column, some placements)
          "90x160"   — 9:16 tall portrait (Stories)

Returns:
    JSON with the image_crops dict (ready for copy-paste into create_ad_creative),
    plus validation notes for any invalid keys requested.


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "image_width": {
      "title": "Image Width",
      "type": "integer"
    },
    "image_height": {
      "title": "Image Height",
      "type": "integer"
    },
    "crop_keys": {
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
      "title": "Crop Keys"
    }
  },
  "required": [
    "image_width",
    "image_height"
  ],
  "title": "compute_image_cropsArguments",
  "type": "object"
}
```

</details>

<a id="create_ad"></a>

## `create_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L617)


Create a new ad with an existing creative.

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    name: Ad name
    adset_id: Ad set ID where this ad will be placed
    creative_id: ID of an existing creative to use
    status: Initial ad status (default: PAUSED)
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
      "default": "PAUSED",
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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L1762)


Create a new ad creative using an uploaded image hash, video ID, or an existing post.

Supports six creative modes:
- **Existing post**: Provide object_story_id (format: {page_id}_{post_id}) to promote an existing
  organic or published post. No image_hash or video_id required. Optionally combine with
  asset_customization_rules to attach a 9:16 video for Story/Reels placements.
- **Simple image/video**: Single image_hash or video_id with object_story_spec
- **Multi-variant copy**: Use plural text params (messages[], headlines[], descriptions[]) to test
  multiple text variants with a single image/video. No optimization_type or is_dynamic_creative needed.
- **Placement Asset Customization (dual-aspect, non-DC)**: Serve different aspect ratios per placement
  on a STANDARD ad set without is_dynamic_creative and without the one-ad-per-ad-set cap. Set
  optimization_type="PLACEMENT" and pass videos=[{video_id, label}, ...] (or images=[{image_hash,
  label}, ...]) together with asset_customization_rules whose customization_spec references those
  labels via video_label/image_label. Every label in the rules MUST appear on a videos[]/images[]
  entry, or Meta returns error_subcode=1487390 ("Adcreative Create Failed").
- **Dynamic Creative**: Multiple variants with dynamic_creative_spec (requires is_dynamic_creative on ad set)
- **FLEX/DOF (Advantage+)**: Set optimization_type="DEGREES_OF_FREEDOM" for Meta to auto-optimize
  across all asset combinations without requiring is_dynamic_creative on the ad set

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    image_hash: Hash of a single uploaded image (cannot be used with image_hashes or video_id)
    access_token: Meta API access token (optional - will use cached token if not provided)
    name: Creative name
    page_id: Facebook Page ID (string or int; coerced to string)
    link_url: Destination URL for the ad. Required unless using lead_gen_form_id or
             reminder_data — with one exception: if asset_customization_rules is also
             set, link_url is required even for Lead ads. Meta accepts the creative
             without link_urls but rejects the ad at create_ad time with error 1885800
             ("Asset Customization Ads require a link"). The URL is never shown to the
             user when lead_gen_form_id is set (the CTA opens the form), but Meta still
             demands one be present on the creative. Pass any valid URL in that case
             (e.g. the Facebook page URL or your site root).
    message: Single ad copy/text (cannot be used with messages)
    messages: List of primary text variants for multi-variant copy testing (cannot be used with message).
              Each entry can be a plain string, OR a dict {"text": "...", "adlabels": [{"name": "..."}]}
              when used with asset_customization_rules that reference body_label.
    headline: Single headline for simple ads (cannot be used with headlines)
    headlines: List of headline variants for multi-variant copy testing (cannot be used with headline).
              Each entry can be a plain string, OR a dict {"text": "...", "adlabels": [{"name": "..."}]}
              when used with asset_customization_rules that reference title_label.
              Meta enforces the actual length limit; do not pre-truncate.
    description: Single description for simple ads (cannot be used with descriptions)
    descriptions: List of description variants for multi-variant copy testing (cannot be used with description).
              Each entry can be a plain string, OR a dict {"text": "...", "adlabels": [{"name": "..."}]}
              when used with asset_customization_rules that reference description_label.
    image_hashes: List of image hashes for FLEX creatives (up to 10, cannot be used with image_hash or video_id).
                 IMPORTANT: When optimization_type="DEGREES_OF_FREEDOM" (FLEX/Advantage+ mode),
                 only ONE image is served at delivery time regardless of how many hashes you provide.
                 The Meta API accepts multiple hashes without error and they all appear in
                 asset_feed_spec, but Meta silently collapses to a single image at serving time.
                 Use image_hashes with multiple entries only in non-DOF (regular dynamic creative)
                 mode. In DOF mode, pass a single hash.
    video_id: Meta video ID for video creatives (cannot be used with image_hash or image_hashes).
              Upload a video first via the Meta API, then use the returned video ID here.
              IMPORTANT: When also providing instagram_actor_id, both instagram_actor_id AND
              ad_formats=["SINGLE_VIDEO"] must be present — otherwise Meta returns error 1443048
              ("object_story_spec ill formed"). This is handled automatically: video creatives
              that include instagram_actor_id are routed through asset_feed_spec so that
              ad_formats=["SINGLE_VIDEO"] is always included in the API request.
    thumbnail_url: Thumbnail image URL for video creatives. Recommended when using video_id.
                  Meta will auto-generate a thumbnail if not provided — Pipeboard
                  will fetch the best available frame from the uploaded video.
                  IMPORTANT: when the video was just uploaded via
                  bulk_upload_ad_videos, Meta needs a few seconds to transcode
                  it. If create_ad_creative is called before transcoding
                  completes, the only thumbnail Meta returns is a generic
                  processing-state placeholder, which would be permanently
                  stored on the creative. In that case create_ad_creative
                  returns an error with video_status: "processing" — wait
                  a few seconds (poll with get_ad_video until video_status
                  is "ready") and retry, or pass thumbnail_url explicitly
                  (any public image URL works).
    optimization_type: Optional. Valid values:
                      - "DEGREES_OF_FREEDOM": FLEX (Advantage+) creatives where Meta auto-optimizes
                        across all asset combinations. At least one multi-variant asset field required.
                        NOTE: Meta ignores asset_customization_rules for DOF creatives.
                        NOTE: When using DEGREES_OF_FREEDOM with image_hashes, providing multiple
                        hashes is accepted by the API without error, but Meta silently serves only
                        ONE image at delivery time. A warning is included in the response if multiple
                        hashes are detected. To serve multiple images, omit optimization_type and
                        enable is_dynamic_creative on the ad set instead.
                      - "PLACEMENT": Placement Asset Customization. Use with videos[]/images[] (with
                        labels) and asset_customization_rules (with video_label/image_label references)
                        to serve different aspect ratios per placement (e.g., 1:1 Feed + 9:16 Reels).
                      Other values are passed through to Meta as-is.
    dynamic_creative_spec: Dynamic creative optimization settings
    call_to_action_type: Call to action button type. Meta enum — free-form values
                        (e.g. 'MAKE_RESERVATION', 'RESERVE', 'BOOK_TABLE') are rejected with
                        code 100. Pick from the documented list. Common values:
                          BOOK_NOW         — restaurants, salons, clinics, appointments (use this for
                                             reservations — there is no MAKE_RESERVATION enum)
                          LEARN_MORE, SHOP_NOW, SIGN_UP, SUBSCRIBE, GET_QUOTE, CONTACT_US,
                          DOWNLOAD, WATCH_MORE, GET_OFFER, APPLY_NOW, CALL_NOW, MESSAGE_PAGE,
                          SEE_MENU, ORDER_NOW, BUY_NOW, WHATSAPP_MESSAGE, GET_DIRECTIONS,
                          BUY_TICKETS, EVENT_RSVP, BOOK_TRAVEL.
                        When using CALL_NOW, also provide phone_number.
    lead_gen_form_id: Lead generation form ID for lead generation campaigns. Required when using
                     lead generation CTAs like 'SIGN_UP', 'GET_OFFER', 'SUBSCRIBE', etc.
    instagram_actor_id: Instagram account ID for Instagram placements (must be a string
                       to avoid JavaScript integer precision loss for IDs exceeding
                       Number.MAX_SAFE_INTEGER). Sent as instagram_user_id inside
                       object_story_spec (Meta deprecated instagram_actor_id in Jan 2026).
                       IMPORTANT for video creatives: Meta requires ad_formats=["SINGLE_VIDEO"]
                       in asset_feed_spec alongside instagram_user_id in object_story_spec —
                       omitting either causes error 1443048 ("object_story_spec ill formed").
                       This is auto-handled: video_id + instagram_actor_id always routes through
                       asset_feed_spec so ad_formats=["SINGLE_VIDEO"] is included automatically.
    ad_formats: List of ad format strings for asset_feed_spec (e.g., ["AUTOMATIC_FORMAT"] for
               Flexible ads, ["SINGLE_IMAGE"] for single image, ["SINGLE_VIDEO"] for video).
               When optimization_type is "DEGREES_OF_FREEDOM" with image_hashes, defaults to
               ["AUTOMATIC_FORMAT"] (Flexible format). For video creatives, defaults to
               ["SINGLE_VIDEO"]. Otherwise defaults to ["SINGLE_IMAGE"].
    asset_customization_rules: List of placement-specific asset overrides for asset_feed_spec.
    phone_number: Phone number for CALL_NOW call-to-action ads (click-to-call).
                 Required when call_to_action_type is CALL_NOW. Use E.164 format
                 (e.g., "+18005551234"). The number is sent to Meta as
                 call_to_action.value.link = "tel:<phone_number>" (Meta v24
                 rejects a literal "phone_number" key with code 100). Common
                 use case: geo-routed call ads with different phone numbers
                 per ad set.
    creative_features_spec: Advantage+ Creative feature opt-ins/opt-outs. Controls individual
               creative enhancements like image_touchups, text_optimizations, inline_comment,
               add_text_overlay, music, 3d_animation, etc. Each feature is a dict with
               "enroll_status" set to "OPT_IN" or "OPT_OUT".
               Example: {"image_touchups": {"enroll_status": "OPT_IN"},
                        "inline_comment": {"enroll_status": "OPT_IN"}}
               Sent to Meta as degrees_of_freedom_spec.creative_features_spec.
    url_tags: URL tracking parameters appended to the destination URL (e.g.,
             "utm_source=facebook&utm_medium=cpc&utm_campaign=spring_sale").
             Sets the url_tags field on the creative.
    caption: Display URL shown in the ad (e.g., "example.com/shoes"). Sets the
            caption field in link_data. If not provided, Meta auto-generates it
            from the destination URL. Only applies to image (link_data) creatives.
    image_crops: Crop coordinates for different aspect ratios. Applied in link_data for
                image creatives.

                Use the compute_image_crops tool first to get the correct coordinates
                for your specific image dimensions — it computes centered crop boxes
                for any source size automatically.

                Valid crop keys (only these 6 are accepted by Meta's API):
                  "100x100"  — 1:1 square (Feed, Marketplace, Search)
                  "100x72"   — ~1.39:1 horizontal (Marketplace, some placements)
                  "400x500"  — 4:5 portrait (Feed on mobile, Stories fallback)
                  "400x150"  — ~2.67:1 wide banner (Audience Network)
                  "600x360"  — ~1.67:1 horizontal (Right column, some placements)
                  "90x160"   — 9:16 tall portrait (Stories)

                Format: {"100x100": [[x1,y1],[x2,y2]], "400x500": [[x1,y1],[x2,y2]]}
                Coordinates are pixel-based (top-left and bottom-right corners).
                The bounding box aspect ratio must match the key ratio as closely as possible.
                Image origin (0,0) is the upper-left corner.

                Omit to let Meta auto-crop (default for horizontal is 1.91:1 recommended).
    object_story_id: ID of an existing organic or published Facebook/Instagram post to promote
                    as an ad. Format: "{page_id}_{post_id}" (e.g., "124965744226834_3888007311337206").
                    When provided, image_hash and video_id are not required. page_id is also not
                    required (it is encoded in the story ID). Combine with asset_customization_rules
                    to attach a 9:16 video for Story/Reels placements while the organic post
                    serves as the feed creative — a common "Use Existing Post" workflow.
                    Example: object_story_id="124965744226834_3888007311337206",
                             asset_customization_rules=[{"placement_groups": ["STORY"],
                               "customization_spec": {"video_ids": ["890310874031162"]}}]
    disable_all_enhancements: When True, opts out of all Advantage+ Creative enhancements by
                    setting every known creative_features_spec key (image_touchups,
                    text_optimizations, video_auto_crop, etc.) to OPT_OUT and also
                    disabling contextual_multi_ads. Use when you want full creative
                    control without Meta's auto-modifications.
    event_id: Facebook Event ID for EVENT_RESPONSES campaigns. Required for
             event RSVP/ticket ads so the event card renders properly. Placed
             inside link_data.event_id, and also inside call_to_action.value
             when call_to_action_type is EVENT_RSVP or BUY_TICKETS. Use with
             link_url set to the Facebook event URL
             (https://www.facebook.com/events/EVENT_ID).
    asset_customization_rules: Lets you assign different images or videos to specific placement groups
               (e.g., feed vs. stories). Only valid with image_hashes or plural asset params.
               Each rule uses a user-friendly format that is automatically translated to
               Meta's API format (adlabels + customization_spec positions):
                 - placement_groups: list of placement group names
                   Valid values: FEED, STORY, MESSENGER, INSTREAM_VIDEO, SEARCH, SHOP,
                   AUDIENCE_NETWORK
                 - customization_spec: dict specifying the asset to use for those placements
                   Supported keys: image_hashes (list), video_ids (list),
                   bodies, titles, descriptions (text overrides)
               All image hashes referenced in rules must also be in image_hashes.
               Example (feed gets one image, stories gets another):
               [
                 {"placement_groups": ["FEED"],
                  "customization_spec": {"image_hashes": ["<feed_hash>"]}},
                 {"placement_groups": ["STORY"],
                  "customization_spec": {"image_hashes": ["<story_hash>"]}}
               ]
    videos: List of video objects for placement asset customization (multiple videos with
               different aspect ratios). Each entry: {"video_id": "...", "thumbnail_url": "...",
               "label": "my_label"}. The "label" field is converted to adlabels for use with
               asset_customization_rules video_label references. Cannot be used with video_id.
               Use with optimization_type="PLACEMENT" and asset_customization_rules.
    images: List of image objects for placement asset customization (multiple images with
               different aspect ratios). Each entry: {"image_hash": "...", "label": "my_label"}.
               The "label" field is converted to adlabels for use with asset_customization_rules
               image_label references. Cannot be used with image_hash or image_hashes.
               Use with optimization_type="PLACEMENT" and asset_customization_rules.
    reminder_data: Inline reminder event data for Instagram Reminder Ads
                  (REMINDERS_SET optimization goal). Placed in
                  object_story_spec.link_data.reminder_data. Use this instead of
                  upcoming_events (which requires an existing ig_upcoming_event_id).
                  Required fields:
                    - event_name (str): Display title of the reminder event
                    - start_time (int): Event start as a Unix timestamp (seconds)
                    - end_time (int): Event end as a Unix timestamp (seconds)
                  Example:
                    {"event_name": "Summer Sale", "start_time": 1745596800, "end_time": 1745611200}
                  The ad set must use optimization_goal=REMINDERS_SET and the placement
                  must be restricted to Instagram feeds/stories. link_url is still
                  recommended (the URL users visit after the reminder fires).
    facebook_branded_content: Branded content settings for Facebook partnership ads.
                  Used when a brand sponsors a creator's content on Facebook.
                  Format: {"sponsor_page_id": "<page_id>"} where sponsor_page_id is the
                  Facebook Page ID of the sponsoring brand. Passed as a top-level field
                  on the ad creative. The creator's page should be set as page_id.
    instagram_branded_content: Branded content settings for Instagram partnership ads.
                  Used when a brand sponsors a creator's content on Instagram.
                  Format: {"sponsor_id": "<instagram_user_id>"} where sponsor_id is the
                  Instagram account ID of the sponsoring brand. Passed as a top-level
                  field on the ad creative.

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
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Image Hash"
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
          "type": "integer"
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
    "messages": {
      "anyOf": [
        {
          "items": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Messages"
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
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
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
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
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
    "image_hashes": {
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
      "title": "Image Hashes"
    },
    "video_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Video Id"
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
    "optimization_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Optimization Type"
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
          "type": "integer"
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
    "ad_formats": {
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
      "title": "Ad Formats"
    },
    "asset_customization_rules": {
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
      "title": "Asset Customization Rules"
    },
    "creative_features_spec": {
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
      "title": "Creative Features Spec"
    },
    "phone_number": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Phone Number"
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
    "caption": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Caption"
    },
    "image_crops": {
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
      "title": "Image Crops"
    },
    "object_story_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Object Story Id"
    },
    "disable_all_enhancements": {
      "anyOf": [
        {
          "type": "boolean"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Disable All Enhancements"
    },
    "event_id": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Event Id"
    },
    "reminder_data": {
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
      "title": "Reminder Data"
    },
    "videos": {
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
      "title": "Videos"
    },
    "images": {
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
      "title": "Images"
    },
    "facebook_branded_content": {
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
      "title": "Facebook Branded Content"
    },
    "instagram_branded_content": {
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
      "title": "Instagram Branded Content"
    }
  },
  "required": [
    "account_id"
  ],
  "title": "create_ad_creativeArguments",
  "type": "object"
}
```

</details>

<a id="create_adset"></a>

## `create_adset`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/adsets.py#L86)


Create a new ad set in a Meta Ads account.

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    campaign_id: Meta Ads campaign ID this ad set belongs to
    name: Ad set name
    optimization_goal: Conversion optimization goal. Valid values depend on the campaign objective and destination_type.
                      OUTCOME_ENGAGEMENT + destination_type=WEBSITE: OFFSITE_CONVERSIONS, LANDING_PAGE_VIEWS, LINK_CLICKS, IMPRESSIONS, REACH.
                      OUTCOME_ENGAGEMENT + On Post (destination_type=ON_POST): POST_ENGAGEMENT, IMPRESSIONS, REACH. Also set promoted_object={page_id} at creation (immutable; without it create_ad fails with subcode 1885154). Do NOT use ON_AD here — ON_AD is the OUTCOME_LEADS instant-form destination and Meta rejects it for OUTCOME_ENGAGEMENT (subcode 1815715).
                      OUTCOME_ENGAGEMENT + On Video (destination_type=ON_VIDEO): THRUPLAY, TWO_SECOND_CONTINUOUS_VIDEO_VIEWS.
                      OUTCOME_ENGAGEMENT + On Event (destination_type=ON_EVENT): EVENT_RESPONSES, IMPRESSIONS, POST_ENGAGEMENT, REACH.
                      OUTCOME_ENGAGEMENT + On Page (destination_type=ON_PAGE): PAGE_LIKES.
                      OUTCOME_ENGAGEMENT + Messaging (MESSENGER/WHATSAPP/INSTAGRAM_DIRECT): CONVERSATIONS, LINK_CLICKS.
                      OUTCOME_ENGAGEMENT "Profile and Page visits" (PROFILE_AND_PAGE_ENGAGEMENT with destination_type INSTAGRAM_PROFILE / FACEBOOK_PAGE / INSTAGRAM_PROFILE_AND_FACEBOOK_PAGE) is shown in Ads Manager but NOT supported via the Marketing API — Meta rejects every variant (code 100). Closest API-supported option is POST_ENGAGEMENT + ON_POST.
                      OUTCOME_TRAFFIC + WEBSITE: LANDING_PAGE_VIEWS, LINK_CLICKS, IMPRESSIONS, REACH.
                      OUTCOME_AWARENESS: REACH, IMPRESSIONS, AD_RECALL_LIFT, THRUPLAY.
                      OUTCOME_LEADS: LEAD_GENERATION, QUALITY_LEAD (forms), QUALITY_CALL (calls), OFFSITE_CONVERSIONS, LINK_CLICKS (website).
                      OUTCOME_SALES: OFFSITE_CONVERSIONS, VALUE, CONVERSATIONS, LINK_CLICKS, IMPRESSIONS, REACH.
                      OUTCOME_APP_PROMOTION: APP_INSTALLS, APP_INSTALLS_AND_OFFSITE_CONVERSIONS, VALUE.
    billing_event: How you're charged (e.g., 'IMPRESSIONS', 'LINK_CLICKS')
    status: Initial ad set status (default: PAUSED)
    daily_budget: Daily budget in account currency (in cents) as a string.
                 CBO NOTE: Do NOT set this if the parent campaign already has a budget
                 (Campaign Budget Optimization / CBO mode). Meta only allows budgets at one
                 level: either the campaign OR the ad set, not both. If the campaign has a
                 daily_budget or lifetime_budget, omit this field — the ad set will
                 automatically use the campaign budget.
    lifetime_budget: Lifetime budget in account currency (in cents) as a string.
                    CBO NOTE: Do NOT set this if the parent campaign already has a budget
                    (Campaign Budget Optimization / CBO mode). Omit this field when the
                    campaign uses CBO — the ad set inherits the campaign budget automatically.
    targeting: Targeting specs (age, location, interests, etc).
              targeting_automation.advantage_audience defaults to 0 if not set (Meta API v24+ requirement).
              Set to 1 to enable Advantage+ Audience (requires age_max>=65). Use search_interests for interest IDs.
    bid_amount: Bid amount in account currency (in cents).
               REQUIRED for: LOWEST_COST_WITH_BID_CAP, COST_CAP, TARGET_COST.
               NOT USED by: LOWEST_COST_WITH_MIN_ROAS (uses bid_constraints instead).
               May also be required if the parent campaign's bid strategy requires it.
    bid_strategy: Bid strategy. Valid values:
                 - 'LOWEST_COST_WITHOUT_CAP' (recommended) - no bid_amount required
                 - 'LOWEST_COST_WITH_BID_CAP' - REQUIRES bid_amount
                 - 'COST_CAP' - REQUIRES bid_amount
                 - 'LOWEST_COST_WITH_MIN_ROAS' - REQUIRES bid_constraints with roas_average_floor,
                   and optimization_goal='VALUE'. Does NOT use bid_amount.
                 Note: 'LOWEST_COST' is NOT valid - use 'LOWEST_COST_WITHOUT_CAP'.
                 Campaign-level bid strategy may constrain ad set choices.
    bid_constraints: Bid constraints dict. Required for LOWEST_COST_WITH_MIN_ROAS.
                    Use {"roas_average_floor": <value>} where value = target ROAS * 10000.
                    Example: 2.0x ROAS -> {"roas_average_floor": 20000}
    bid_adjustments: Bid multipliers per targeting dimension. Pass-through to Meta.
                    Shape: {"user_groups": {"<dim>": {"<value>": <float>, "default": <float>}}}
                    Dims: age, gender, user_os, device_platform, position_type,
                          publisher_platform, user_bucket, home_location, locale, etc.
                    Multipliers are floats, typically 0.0-1.0.
                    Example: {"user_groups": {"user_os": {"iOS": 0.9, "Android": 0.7, "default": 1.0}}}
                    NOTE: Writing bid_adjustments requires a Meta app capability that must be
                          allowlisted. Apps without it get OAuthException (#3).
    start_time: Start time in ISO 8601 format (e.g., '2023-12-01T12:00:00-0800').
               To schedule future delivery: set start_time to a future date and status=ACTIVE.
               Meta will show effective_status as SCHEDULED and automatically begin delivery at start_time.
               NOTE: Only ad set start_time controls delivery scheduling. Campaigns do not support start_time.
    end_time: End time in ISO 8601 format. Required when lifetime_budget is specified.
    dsa_beneficiary: DSA beneficiary for European compliance (person/org that benefits from ads).
                    Required for EU-targeted ad sets along with dsa_payor.
    dsa_payor: DSA payor for European compliance (person/org paying for the ads).
               Required for EU-targeted ad sets along with dsa_beneficiary.
    promoted_object: For APP_INSTALLS: app config, required application_id + object_store_url.
                    For OUTCOME_ENGAGEMENT On-Post (destination_type=ON_POST): set {"page_id": "<id>"} at
                    creation — required for ads (else create_ad fails with subcode 1885154) and immutable
                    afterward (cannot be added via update_adset).
    destination_type: Conversion location / where users go. Pass-through to Meta (no client-side validation).
                     Common values: 'WEBSITE', 'WHATSAPP', 'MESSENGER', 'INSTAGRAM_DIRECT', 'APP', 'FACEBOOK',
                     'SHOP_AUTOMATIC'. OUTCOME_ENGAGEMENT on-asset locations: 'ON_POST' (post engagement; needs
                     promoted_object={page_id}), 'ON_PAGE' (PAGE_LIKES), 'ON_EVENT', 'ON_VIDEO'. 'ON_AD' is the
                     OUTCOME_LEADS instant-form destination — do NOT use it for OUTCOME_ENGAGEMENT (Meta rejects
                     it with subcode 1815715). Also supports multi-channel combos like 'MESSAGING_MESSENGER_WHATSAPP'.
    is_dynamic_creative: Enable Dynamic Creative for this ad set.
    frequency_control_specs: Frequency cap specs. MUST be set at creation time — Meta makes this field
                             immutable after the ad set is created (error 1815198).
                             Only works with OUTCOME_AWARENESS campaigns + optimization_goal REACH or THRUPLAY.
                             Example: [{"event": "IMPRESSIONS", "interval_days": 7, "max_frequency": 1}]
    multi_advertiser_ads: Set to 0 to opt out of Multi-Advertiser Ads, 1 to opt in.
                         This is a TOP-LEVEL ad set parameter — do NOT put it inside the targeting object.
    regional_regulated_categories: List of regional regulated categories for the ad set.
                                   Required for ads targeting regulated regions (Taiwan, Australia, etc.).
                                   Valid values: TAIWAN_FINSERV, TAIWAN_UNIVERSAL, AUSTRALIA_FINSERV,
                                   INDIA_FINSERV, SINGAPORE_UNIVERSAL, THAILAND_UNIVERSAL.
                                   Example: ["TAIWAN_UNIVERSAL"] or ["TAIWAN_FINSERV", "TAIWAN_UNIVERSAL"]
    regional_regulation_identities: Dict of verified identity IDs for regional transparency compliance.
                                    Required when regional_regulated_categories is set.
                                    The identity IDs come from completing advertiser verification in Meta Business Settings.
                                    Keys depend on the categories declared:
                                    - TAIWAN_UNIVERSAL: taiwan_universal_beneficiary, taiwan_universal_payer
                                    - TAIWAN_FINSERV: taiwan_finserv_beneficiary, taiwan_finserv_payer
                                    - AUSTRALIA_FINSERV: australia_finserv_beneficiary, australia_finserv_payer
                                    - SINGAPORE_UNIVERSAL: singapore_universal_beneficiary, singapore_universal_payer
                                    Example: {"taiwan_universal_beneficiary": "<id>", "taiwan_universal_payer": "<id>"}
    attribution_spec: Attribution window specification for the ad set. Controls how conversions are
                     attributed to ads. Default is 7-day click if not specified.
                     Example for 1-day click: [{"event_type": "CLICK_THROUGH", "window_days": 1}]
                     Example for 1-day click + 1-day view: [{"event_type": "CLICK_THROUGH", "window_days": 1}, {"event_type": "VIEW_THROUGH", "window_days": 1}]
                     Valid event_type values: CLICK_THROUGH, VIEW_THROUGH.
                     Valid window_days values: 1, 7, 28 (depends on event_type and optimization_goal).
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
      "default": "PAUSED",
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
    "bid_constraints": {
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
      "title": "Bid Constraints"
    },
    "bid_adjustments": {
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
      "title": "Bid Adjustments"
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
    "dsa_payor": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Dsa Payor"
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
    "multi_advertiser_ads": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Multi Advertiser Ads"
    },
    "regional_regulated_categories": {
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
      "title": "Regional Regulated Categories"
    },
    "regional_regulation_identities": {
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
      "title": "Regional Regulation Identities"
    },
    "attribution_spec": {
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
      "title": "Attribution Spec"
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

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/budget_schedules.py#L11)


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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/campaigns.py#L115)


Create a new Facebook or Instagram ad campaign in a Meta Ads account. Use this to start
a new campaign with an ODAX objective (OUTCOME_LEADS, OUTCOME_SALES, OUTCOME_AWARENESS,
OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT, OUTCOME_APP_PROMOTION), pick CBO (campaign budget
optimization) or ABO (ad-set-level budgets), and set bid strategy, spend cap, and special
ad categories. This is the first step of the campaign group → ad set → ad hierarchy on
Meta. Returns the new campaign id. Also known as: create campaign, new campaign, make
campaign, campaign group, ABO campaign, CBO campaign.

Note: Campaigns do not support start_time for scheduling — set start_time on the ad set instead.

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
    bid_strategy: Bid strategy (default: LOWEST_COST_WITHOUT_CAP). Must be one of: 'LOWEST_COST_WITHOUT_CAP', 'LOWEST_COST_WITH_BID_CAP', 'COST_CAP', 'LOWEST_COST_WITH_MIN_ROAS'. WARNING: If you use LOWEST_COST_WITH_BID_CAP or COST_CAP, all child ad sets will require bid_amount to be set.
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
      "default": "LOWEST_COST_WITHOUT_CAP",
      "title": "Bid Strategy",
      "type": "string"
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

<a id="duplicate_ad"></a>

## `duplicate_ad`

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/duplication.py#L135)


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
          "type": "integer"
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
    },
    "pb_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Pb Token"
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

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/duplication.py#L81)


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
    new_start_time: Override start time for the duplicated ad set (ISO 8601, e.g. 2026-03-10T00:00:00-0500)
    new_end_time: Override end time for the duplicated ad set (ISO 8601, e.g. 2026-03-20T23:59:59-0500)
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
          "type": "integer"
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
    "new_start_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Start Time"
    },
    "new_end_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New End Time"
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
    },
    "pb_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Pb Token"
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

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/duplication.py#L30)


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
    new_start_time: Override start time for duplicated ad sets (ISO 8601, e.g. 2026-03-10T00:00:00-0500)
    new_end_time: Override end time for duplicated ad sets (ISO 8601, e.g. 2026-03-20T23:59:59-0500)
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
    "new_start_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New Start Time"
    },
    "new_end_time": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "New End Time"
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
    },
    "pb_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Pb Token"
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

Scope: **meta-ads** · Capability: **automation** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/duplication.py#L177)


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
    new_creative_features_spec: Override / merge into the duplicate's
        degrees_of_freedom_spec.creative_features_spec. Use individual
        feature keys (e.g. image_touchups, image_uncrop, text_optimizations,
        video_auto_crop) with {"enroll_status": "OPT_IN" | "OPT_OUT"} values.
        Merged on top of the source creative's surviving creative_features_spec
        entries. NOTE: the legacy "standard_enhancements" key is rejected by
        Meta on POST (error_subcode 3858504); pass individual feature keys
        instead. The duplication response surfaces a warning when the source
        had standard_enhancements so callers know what to set here.


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
    },
    "new_creative_features_spec": {
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
      "title": "New Creative Features Spec"
    },
    "pb_token": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Pb Token"
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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/targeting.py#L68)


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
          "type": "integer"
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

<a id="generate_report"></a>

## `generate_report`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/reports.py#L14)


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

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/accounts.py#L76)


Get detailed information about a specific ad account.

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    access_token: Meta API access token (optional - will use cached token if not provided)
    fields: Optional comma-separated Graph API fields to return. When provided,
            replaces the default field set. Useful for fetching extras like
            funding_source_details, spend_cap, is_prepay_account, min_daily_budget,
            disable_reason, capabilities. Default fields:
            id, name, account_id, account_status, amount_spent, balance, currency,
            age, business_city, business_country_code, timezone_name.
            For prepaid accounts (is_prepay_account=true, common in Brazil), the
            Business Manager "available balance" is the sum of funding_source_details
            STORED_BALANCE entries plus coupons — the `balance` field alone is the
            amount due to be billed, not the available pre-paid funds.


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
    "fields": {
      "default": "",
      "title": "Fields",
      "type": "string"
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

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L3374)


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

Scope: **meta-ads** · Capability: **accounts** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/accounts.py#L42)


Get ad accounts accessible by a user.

amount_spent and balance are returned in currency units (e.g. USD dollars),
not cents.

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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L689)


Get creative details for a specific ad. Requires an ad_id (not account_id). Use get_ads first to find ad IDs.

Args:
    ad_id: Meta Ads ad ID (required)
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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L542)


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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L769)


Get, download, and visualize the image attached to an existing Meta ad.

Takes a Meta ad ID and returns the image the ad is currently serving.
If all you have is an image hash (no ad), use get_image_by_hash instead.

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

<a id="get_ad_video"></a>

## `get_ad_video`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L1005)


Get video details and source URL for a Meta ad video creative. Returns the video source URL
(direct download link), thumbnail URL, processing status, and metadata (title, description,
duration).

Also useful for polling after bulk_upload_ad_videos: ``video_status`` is
``"processing"`` while Meta is still transcoding and ``"ready"`` when the
real video frames (and a usable thumbnail) are available. Calling
create_ad_creative before status is "ready" returns an error because the
only thumbnail Meta returns during processing is a generic placeholder
that would be permanently stored on the creative.

Provide either ad_id (to auto-extract the video from the ad creative) or video_id directly.
Providing account_id is strongly recommended — it enables the advideos edge which works
with Business Manager tokens (avoids error 100/33 and error #10 on account-uploaded videos).

Args:
    ad_id: Meta Ads ad ID (will extract video_id from the ad creative)
    video_id: Meta video ID (use this if you already have it from get_ad_creatives)
    account_id: Ad account ID (e.g. "act_123" or "123"). Enables advideos edge lookup.
    access_token: Meta API access token (optional - will use cached token if not provided)


<details>
<summary>Full input schema</summary>

```json
{
  "properties": {
    "ad_id": {
      "default": "",
      "title": "Ad Id",
      "type": "string"
    },
    "video_id": {
      "default": "",
      "title": "Video Id",
      "type": "string"
    },
    "account_id": {
      "default": "",
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
  "title": "get_ad_videoArguments",
  "type": "object"
}
```

</details>

<a id="get_ads"></a>

## `get_ads`

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L497)


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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/adsets.py#L50)


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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/adsets.py#L10)


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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/campaigns.py#L88)


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

Scope: **meta-ads** · Capability: **campaigns-read** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/campaigns.py#L10)


Get campaigns for a Meta Ads account with optional filtering.

Note: By default, the Meta API returns a subset of available fields. 
Other fields like 'effective_status', 'spend_cap', 'budget_remaining',
'promoted_object', 'source_campaign_id', etc., might be available but
require specifying them in the API call (currently not exposed by this
tool's parameters).

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

<a id="get_creative_details"></a>

## `get_creative_details`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L565)

Get detailed information about a specific ad creative by its ID.

Args:
    creative_id: Meta Ads creative ID (required)
    access_token: Meta API access token (optional)


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
    }
  },
  "required": [
    "creative_id"
  ],
  "title": "get_creative_detailsArguments",
  "type": "object"
}
```

</details>

<a id="get_image_by_hash"></a>

## `get_image_by_hash`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L922)


Get, download, and visualize a Meta ad image by its hash.

Use this when you have an image_hash without an ad — e.g. the hash
returned by upload_ad_image / bulk_upload_ad_images, or one referenced
in a creative (object_story_spec.link_data.image_hash, asset_feed_spec
images[].hash, etc.). To view the image of an existing ad, prefer
get_ad_image(ad_id).

Args:
    account_id: Meta Ads account ID (act_XXXXXXXXX or bare numeric — both accepted)
    image_hash: Meta image hash
    access_token: Meta API access token (optional - will use cached token if not provided)

Returns:
    The image ready for direct visual analysis


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
    }
  },
  "required": [
    "account_id",
    "image_hash"
  ],
  "title": "get_image_by_hashArguments",
  "type": "object"
}
```

</details>

<a id="get_insights"></a>

## `get_insights`

Scope: **meta-ads** · Capability: **reporting** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/insights.py#L56)


Get performance insights for a campaign, ad set, ad or account.

Args:
    object_id: ID of the campaign, ad set, ad or account. You can also use the alias parameters below.
    account_id: Alias for object_id when querying account-level insights
    campaign_id: Alias for object_id when querying campaign-level insights
    adset_id: Alias for object_id when querying ad-set-level insights
    ad_id: Alias for object_id when querying ad-level insights
    access_token: Meta API access token (optional - will use cached token if not provided)
    time_range: Either a preset time range string or a dictionary with "since" and "until" dates in YYYY-MM-DD format
               Preset options: today, yesterday, this_month, last_month, this_quarter, maximum, data_maximum, 
               last_3d, last_7d, last_14d, last_28d, last_30d, last_90d, last_week_mon_sun, 
               last_week_sun_sat, last_quarter, last_year, this_week_mon_today, this_week_sun_today, this_year
               Dictionary example: {"since":"2023-01-01","until":"2023-01-31"}
    breakdown: Optional breakdown dimension. Valid values include:
               Demographic: age, gender, country, region, dma
               Platform/Device: device_platform, platform_position, publisher_platform, impression_device
               NOTE: platform_position is a Meta-restricted breakdown — Meta requires it to be paired
               with publisher_platform (otherwise "(#100) ... (action_type, platform_position) is invalid").
               When you pass platform_position, this tool auto-adds publisher_platform, and the
               action-typed fields (actions, action_values, conversions, cost_per_action_type) are
               returned per placement, so you get leads/CPL/conversions broken down by placement.
               Creative Assets: ad_format_asset, body_asset, call_to_action_asset, description_asset,
                              image_asset, link_url_asset, title_asset, video_asset, media_type,
                              creative_relaxation_asset_type, flexible_format_asset_type,
                              gen_ai_asset_type
               NOTE: Asset breakdowns (image_asset, video_asset, etc.) only return data for ads
               running with Dynamic Creative; for non-DCO ads, expect empty rows.
               NOTE: media_type collides with the default action_breakdowns=[action_type], so
               this tool auto-overrides action_breakdowns to [] when you pass media_type.
               Action-typed metrics (actions, action_values, conversions) are still returned
               but are no longer sliced by action_type alongside media_type.
               media_asset_url, media_creator, media_destination_url, media_format,
               media_origin_url, and media_text_content are NOT supported by Meta's Insights API
               (Meta returns "(#100) Tried accessing nonexisting field"). Use the asset breakdowns
               above instead.
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
    action_breakdowns: Optional list of action_breakdowns to apply to action-typed metrics. Pass [] to disable
               the default action_type slicing (required when combining action data with breakdowns that collide
               with action_type, e.g. media_type — auto-applied for media_type when not set).
               Meta supports values like action_type, action_target_id, action_destination, etc.
    compact: When True, strips redundant action-type duplicates from the response
             (omni_*, onsite_web_*, offsite_conversion.fb_pixel_*, etc.) to reduce
             payload size by ~60%. The canonical action types (purchase, add_to_cart,
             view_content, etc.) are always preserved. Default: False.

Note on response size: This tool always returns a fixed set of fields (impressions, clicks,
spend, cpc, cpm, ctr, reach, actions, action_values, etc.) and cannot filter to a subset.
For large result sets (50+ rows), the actions/action_values arrays can make responses very
large (1–2MB+). If you only need specific metrics like spend or impressions, consider using
bulk_get_insights with compact=true and the fields parameter:
    bulk_get_insights(level="ad", account_ids=[...], compact=true, fields=["spend", "impressions"])
bulk_get_insights supports level="ad", "adset", "campaign", and "account".


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
    },
    "action_breakdowns": {
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
      "title": "Action Breakdowns"
    },
    "compact": {
      "default": false,
      "title": "Compact",
      "type": "boolean"
    },
    "account_id": {
      "default": "",
      "title": "Account Id",
      "type": "string"
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
    },
    "ad_id": {
      "default": "",
      "title": "Ad Id",
      "type": "string"
    }
  },
  "title": "get_insightsArguments",
  "type": "object"
}
```

</details>

<a id="get_interest_suggestions"></a>

## `get_interest_suggestions`

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/targeting.py#L39)


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

Scope: **supporting** · Capability: **utilities** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/authentication.py#L45)


Get a clickable login link for Meta Ads authentication.

NOTE: This method requires your own Facebook app (META_APP_ID). If you would
rather not run one, use the hosted MCP at https://meta-ads.mcp.pipeboard.co/
instead, which authenticates with a Pipeboard API token.

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

<a id="save_ad_image_locally"></a>

## `save_ad_image_locally`

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L1154)


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

<a id="search_ads_archive"></a>

## `search_ads_archive`

Scope: **meta-ads** · Capability: **ad-library** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads_library.py#L14)


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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/targeting.py#L461)


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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/targeting.py#L486)


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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/targeting.py#L513)


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

Scope: **meta-ads** · Capability: **audiences** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/targeting.py#L10)


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

Scope: **supporting** · Capability: **accounts** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L3351)


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

<a id="update_ad"></a>

## `update_ad`

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L1279)


Update an ad with new settings.

Args:
    ad_id: Meta Ads ad ID
    name: New ad name
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
          "type": "integer"
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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L2964)


Update an existing ad creative's name or optimization settings.

IMPORTANT — Meta API limitation: The Meta API does NOT allow updating content
fields (message, headline, description, CTA, image, video, URL) on existing
creatives. Only the creative `name` and optimization settings (asset_feed_spec)
can be changed. To change ad content, create a new creative with the desired
content and update the ad to reference the new creative via `update_ad`.

Args:
    creative_id: Meta Ads creative ID to update
    access_token: Meta API access token (optional - will use cached token if not provided)
    name: New creative name (this is the most reliable update)
    message: New ad copy/text — NOTE: Meta API may reject this on existing creatives
    messages: List of primary text variants — NOTE: Meta API may reject this on existing creatives
    headline: Single headline — NOTE: Meta API may reject this on existing creatives
    headlines: New list of headlines — NOTE: Meta API may reject this on existing creatives
    description: Single description — NOTE: Meta API may reject this on existing creatives
    descriptions: New list of descriptions — NOTE: Meta API may reject this on existing creatives
    optimization_type: Set to "DEGREES_OF_FREEDOM" for FLEX (Advantage+) creatives
    dynamic_creative_spec: New dynamic creative optimization settings
    call_to_action_type: New call to action button type — NOTE: Meta API may reject this on existing creatives
    lead_gen_form_id: Lead generation form ID for lead generation campaigns
    ad_formats: List of ad format strings for asset_feed_spec (e.g., ["AUTOMATIC_FORMAT"] for
               Flexible ads, ["SINGLE_IMAGE"] for single image)
    creative_features_spec: Dict of Advantage+ Creative feature opt-ins/opt-outs.
               Each key is a feature name, value is {"enroll_status": "OPT_IN"|"OPT_OUT"}.
               Sent as a top-level field (not inside degrees_of_freedom_spec).

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
    "messages": {
      "anyOf": [
        {
          "items": {
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
          },
          "type": "array"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Messages"
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
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
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
            "anyOf": [
              {
                "type": "string"
              },
              {
                "additionalProperties": true,
                "type": "object"
              }
            ]
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
    "optimization_type": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Optimization Type"
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
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Lead Gen Form Id"
    },
    "ad_formats": {
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
      "title": "Ad Formats"
    },
    "creative_features_spec": {
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
      "title": "Creative Features Spec"
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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/adsets.py#L496)


Update an ad set with new settings including frequency caps and budgets.

Args:
    adset_id: Meta Ads ad set ID
    name: New ad set name
    frequency_control_specs: Frequency control specs
                             (e.g. [{"event": "IMPRESSIONS", "interval_days": 7, "max_frequency": 3}])
    bid_strategy: Bid strategy. Valid values:
                 - 'LOWEST_COST_WITHOUT_CAP' (recommended) - no bid_amount required
                 - 'LOWEST_COST_WITH_BID_CAP' - REQUIRES bid_amount
                 - 'COST_CAP' - REQUIRES bid_amount
                 - 'LOWEST_COST_WITH_MIN_ROAS' - REQUIRES bid_constraints with roas_average_floor
                 Note: 'LOWEST_COST' is NOT valid - use 'LOWEST_COST_WITHOUT_CAP'.
    bid_amount: Bid amount in cents. Required for LOWEST_COST_WITH_BID_CAP, COST_CAP, TARGET_COST.
               NOT USED by LOWEST_COST_WITH_MIN_ROAS (uses bid_constraints instead).
    bid_constraints: Bid constraints dict. Required for LOWEST_COST_WITH_MIN_ROAS.
                    Use {"roas_average_floor": <value>} where value = target ROAS * 10000.
                    Example: 2.0x ROAS -> {"roas_average_floor": 20000}
    bid_adjustments: Bid multipliers per targeting dimension. Pass-through to Meta.
                    Shape: {"user_groups": {"<dim>": {"<value>": <float>, "default": <float>}}}
                    See create_adset for full docs and dim list.
                    NOTE: Writing requires a Meta app capability that must be allowlisted.
    status: Update ad set status (ACTIVE, PAUSED, etc.)
    targeting: Complete targeting specifications (replaces existing targeting)
    optimization_goal: Conversion optimization goal (e.g., 'LINK_CLICKS', 'CONVERSIONS', 'VALUE')
    daily_budget: Daily budget in account currency (in cents)
    lifetime_budget: Lifetime budget in account currency (in cents)
    is_dynamic_creative: Enable/disable Dynamic Creative for this ad set.
                        WARNING: This field is immutable after ad set creation. Meta's API will
                        return success but silently ignore the change. To change this, create a new ad set.
    start_time: Start time in ISO 8601 format (e.g., '2023-12-01T12:00:00-0800').
               Use with status=ACTIVE to schedule the ad set for future delivery (effective_status will be SCHEDULED until start_time).
    end_time: End time in ISO 8601 format. Required when lifetime_budget is specified.
    dsa_beneficiary: DSA beneficiary for European compliance (person/org that benefits from ads).
                    Required for EU-targeted ad sets along with dsa_payor.
    dsa_payor: DSA payor for European compliance (person/org paying for the ads).
               Required for EU-targeted ad sets along with dsa_beneficiary.
    multi_advertiser_ads: Set to 0 to opt out of Multi-Advertiser Ads, 1 to opt in.
                         This is a TOP-LEVEL ad set parameter — do NOT put it inside the targeting object.
    regional_regulated_categories: List of regional regulated categories for the ad set.
                                   Required for ads targeting regulated regions (Taiwan, Australia, etc.).
                                   Valid values: TAIWAN_FINSERV, TAIWAN_UNIVERSAL, AUSTRALIA_FINSERV,
                                   INDIA_FINSERV, SINGAPORE_UNIVERSAL, THAILAND_UNIVERSAL.
                                   Set to null/empty to remove existing categories.
    regional_regulation_identities: Dict of verified identity IDs for regional transparency compliance.
                                    Required when regional_regulated_categories is set.
                                    Set individual keys to null to remove them.
    attribution_spec: Attribution window specification for the ad set.
                     WARNING: Meta no longer supports updating attribution_spec after ad set creation
                     (error 1504040). To change attribution windows, create a new ad set instead.
                     This parameter is kept for compatibility but will be rejected by Meta's API.
                     Valid event_type values: CLICK_THROUGH, VIEW_THROUGH.
                     Valid window_days values: 1, 7, 28 (depends on event_type and optimization_goal).
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
    "bid_constraints": {
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
      "title": "Bid Constraints"
    },
    "bid_adjustments": {
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
      "title": "Bid Adjustments"
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
    "dsa_payor": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Dsa Payor"
    },
    "multi_advertiser_ads": {
      "anyOf": [
        {
          "type": "integer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "title": "Multi Advertiser Ads"
    },
    "regional_regulated_categories": {
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
      "title": "Regional Regulated Categories"
    },
    "regional_regulation_identities": {
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
      "title": "Regional Regulation Identities"
    },
    "attribution_spec": {
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
      "title": "Attribution Spec"
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

Scope: **meta-ads** · Capability: **campaigns** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/campaigns.py#L263)


Update an existing campaign in a Meta Ads account.

Note: Campaigns do not support start_time for scheduling — set start_time on the ad set instead.

Migrating CBO (Advantage Campaign Budget) → ABO (ad set level budgets):
    Pass `adset_budgets` with one entry per ad set in the campaign. Meta atomically
    removes the campaign-level budget and assigns budgets at the ad set level in a
    single call. This is Meta's documented mechanism — the legacy
    `use_adset_level_budgets=true` flag attempts to clear `daily_budget`/`lifetime_budget`
    but Meta silently ignores the empty values, so the migration does not persist.

Args:
    campaign_id: Meta Ads campaign ID
    access_token: Meta API access token (optional - will use cached token if not provided)
    name: New campaign name
    status: New campaign status (e.g., 'ACTIVE', 'PAUSED')
    special_ad_categories: List of special ad categories if applicable
    daily_budget: New daily budget in account currency (in cents).
    lifetime_budget: New lifetime budget in account currency (in cents).
    bid_strategy: New bid strategy
    bid_cap: New bid cap in account currency (in cents) as a string
    spend_cap: New spending limit for the campaign in account currency (in cents) as a string
    campaign_budget_optimization: Enable/disable campaign budget optimization
    objective: New campaign objective (Note: May not always be updatable)
    use_adset_level_budgets: Deprecated for CBO → ABO migration — use `adset_budgets`
        instead. Kept for backwards compatibility; sends empty `daily_budget`/
        `lifetime_budget` which Meta silently ignores in most cases.
    adset_budgets: List of `{"adset_id": "...", "daily_budget": <cents>}` objects.
        Use to migrate from CBO to ABO: Meta removes the campaign-level Advantage
        budget and assigns the provided daily budgets at the ad set level in one
        atomic call. Example:
            [{"adset_id": "1234", "daily_budget": 5000},
             {"adset_id": "5678", "daily_budget": 7000}]


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
    },
    "adset_budgets": {
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
      "title": "Adset Budgets"
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

Scope: **meta-ads** · Capability: **creatives** · [Definition](https://github.com/pipeboard-co/meta-ads-mcp/blob/093062c6655682a20ff0814b468e0e877263d494/meta_ads_mcp/core/ads.py#L1368)


Upload an image to use in Meta Ads creatives.

Args:
    account_id: Meta Ads account ID (format: act_XXXXXXXXX)
    access_token: Meta API access token (optional - will use cached token if not provided)
    file: Data URL or raw base64 string of the image (e.g., "data:image/png;base64,iVBORw0KG...")
    image_url: Direct URL to an image to fetch and upload
    name: Optional name for the image (default: filename)

Returns:
    JSON object with:
      - image_hash: Pass this to create_ad_creative when building the ad,
        or to get_image_by_hash to view the image later.
      - images: List of {hash, url, width, height, name}. The url is a
        Meta CDN link you can fetch directly to view the image — no need
        to call any other tool right after upload.


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

