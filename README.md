# Awesome Meta & Instagram Ads MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Discover what you can do with Meta and Instagram advertising MCP tools — from launching campaigns to researching competitors and validating conversions.

**17 MCPs · 754 advertising tools.** Browse by task below, or [search every tool name](docs/tool-index.md). Each MCP page contains its full tool descriptions and input schemas.

Groups come from registered tools and their implementations. A server can appear in several groups. Supporting and unrelated tools remain visible on its full snapshot page, but unrelated tools do not earn advertising capabilities. Counts describe reviewed source or provider-schema snapshots; optional registrations are included where documented. Live advertising operations were not tested.

## Browse by task

- [Measure advertising performance](#measure-advertising-performance)
- [Inspect campaign structure](#inspect-campaign-structure)
- [Launch and change campaigns](#launch-and-change-campaigns)
- [Build and upload ad creatives](#build-and-upload-ad-creatives)
- [Find and manage audiences](#find-and-manage-audiences)
- [Send and validate conversion signals](#send-and-validate-conversion-signals)
- [Research public ads](#research-public-ads)
- [Manage advertising catalogs](#manage-advertising-catalogs)
- [Work with lead ads](#work-with-lead-ads)
- [Automate and control changes](#automate-and-control-changes)
- [Connect advertising accounts](#connect-advertising-accounts)
- [Discover and dispatch advertising operations](#discover-and-dispatch-advertising-operations)
- [Inspect and troubleshoot integrations](#inspect-and-troubleshoot-integrations)
- [CLI and SDK companions](docs/companions.md)
- [Extraction coverage](docs/coverage.md)

## Measure advertising performance

Query Insights, delivery, spend, attribution, and breakdowns.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [attainmentlabs/meta-ads-mcp](docs/mcp/attainmentlabs--meta-ads-mcp.md) | [`get_meta_insights`](docs/mcp/attainmentlabs--meta-ads-mcp.md#get_meta_insights) | 13 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`get_insights`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_insights) · [`get_bulk_insights`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_bulk_insights) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`compare_ads`](docs/mcp/brijr--meta-mcp.md#compare_ads) · [`get_ad_metrics`](docs/mcp/brijr--meta-mcp.md#get_ad_metrics) · [`get_adset_metrics`](docs/mcp/brijr--meta-mcp.md#get_adset_metrics) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_get_ad_dossier`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_ad_dossier) · [`ads_get_insights`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_insights) · [`ads_insights_performance_trend`](docs/mcp/byadsco--meta-ads-mcp.md#ads_insights_performance_trend) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`get_insights`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_insights) · [`search`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#search) · [`fetch`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#fetch) | 59 tools |
| [Draivix/aidvertaiser](docs/mcp/Draivix--aidvertaiser.md) | [`meta_get_insights`](docs/mcp/Draivix--aidvertaiser.md#meta_get_insights) | 255 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`create_insights_job`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_insights_job) · [`create_report`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_report) · [`list_ad_custom_derived_metrics`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#list_ad_custom_derived_metrics) | 125 tools |
| [gomarble-ai/facebook-ads-mcp-server](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md) | [`get_adaccount_insights`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_adaccount_insights) · [`get_campaign_insights`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_campaign_insights) · [`get_adset_insights`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_adset_insights) | 21 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`get_account_insights`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_account_insights) · [`get_campaign_insights`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_campaign_insights) · [`get_adset_insights`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_adset_insights) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_get_ad_account_activity`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_ad_account_activity) · [`meta_get_ad_studies`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_ad_studies) · [`meta_get_ad_study_results`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_ad_study_results) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`get_insights`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_insights) | 41 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`get_insights`](docs/mcp/serkanhaslak--meta-mcp.md#get_insights) · [`get_account_insights`](docs/mcp/serkanhaslak--meta-mcp.md#get_account_insights) · [`create_async_report`](docs/mcp/serkanhaslak--meta-mcp.md#create_async_report) | 77 tools |

## Inspect campaign structure

List and inspect campaigns, ad sets, ads, statuses, and object relationships.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [attainmentlabs/meta-ads-mcp](docs/mcp/attainmentlabs--meta-ads-mcp.md) | [`list_campaigns`](docs/mcp/attainmentlabs--meta-ads-mcp.md#list_campaigns) · [`list_ad_sets`](docs/mcp/attainmentlabs--meta-ads-mcp.md#list_ad_sets) · [`list_ads`](docs/mcp/attainmentlabs--meta-ads-mcp.md#list_ads) | 13 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`get_campaigns`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_campaigns) · [`get_campaign_details`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_campaign_details) · [`get_adsets`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_adsets) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`get_ad_set`](docs/mcp/brijr--meta-mcp.md#get_ad_set) · [`list_ad_sets`](docs/mcp/brijr--meta-mcp.md#list_ad_sets) · [`get_campaign`](docs/mcp/brijr--meta-mcp.md#get_campaign) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_get_campaigns`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_campaigns) · [`ads_get_campaign_details`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_campaign_details) · [`ads_get_ad_sets`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_ad_sets) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`get_campaigns`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_campaigns) · [`get_campaign_details`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_campaign_details) · [`get_adsets`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_adsets) | 59 tools |
| [Draivix/aidvertaiser](docs/mcp/Draivix--aidvertaiser.md) | [`meta_get_ad_details`](docs/mcp/Draivix--aidvertaiser.md#meta_get_ad_details) · [`meta_get_adset_details`](docs/mcp/Draivix--aidvertaiser.md#meta_get_adset_details) · [`meta_get_campaign_details`](docs/mcp/Draivix--aidvertaiser.md#meta_get_campaign_details) | 255 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`inspect_ad_object`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#inspect_ad_object) · [`list_ad_sets`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#list_ad_sets) · [`list_ads`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#list_ads) | 125 tools |
| [gomarble-ai/facebook-ads-mcp-server](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md) | [`get_ad_by_id`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_ad_by_id) · [`get_ads_by_adaccount`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_ads_by_adaccount) · [`get_ads_by_campaign`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_ads_by_campaign) | 21 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`list_campaigns`](docs/mcp/mikusnuz--meta-ads-mcp.md#list_campaigns) · [`get_campaign`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_campaign) · [`get_campaign_adsets`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_campaign_adsets) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_list_campaigns`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_campaigns) · [`meta_get_campaign`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_campaign) · [`meta_list_adsets`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_adsets) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`get_campaigns`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_campaigns) · [`get_campaign_details`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_campaign_details) · [`get_adsets`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_adsets) | 41 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`list_campaigns`](docs/mcp/serkanhaslak--meta-mcp.md#list_campaigns) · [`get_campaign`](docs/mcp/serkanhaslak--meta-mcp.md#get_campaign) · [`list_adsets`](docs/mcp/serkanhaslak--meta-mcp.md#list_adsets) | 77 tools |

## Launch and change campaigns

Create, update, pause, and delete campaigns, ad sets, and ads.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [attainmentlabs/meta-ads-mcp](docs/mcp/attainmentlabs--meta-ads-mcp.md) | [`create_meta_campaign`](docs/mcp/attainmentlabs--meta-ads-mcp.md#create_meta_campaign) · [`update_daily_budget`](docs/mcp/attainmentlabs--meta-ads-mcp.md#update_daily_budget) · [`pause_campaign`](docs/mcp/attainmentlabs--meta-ads-mcp.md#pause_campaign) | 13 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`create_campaign`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#create_campaign) · [`update_campaign`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#update_campaign) · [`create_adset`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#create_adset) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`create_ad_set`](docs/mcp/brijr--meta-mcp.md#create_ad_set) · [`delete_ad_set`](docs/mcp/brijr--meta-mcp.md#delete_ad_set) · [`duplicate_ad_set`](docs/mcp/brijr--meta-mcp.md#duplicate_ad_set) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_create_campaign`](docs/mcp/byadsco--meta-ads-mcp.md#ads_create_campaign) · [`ads_update_campaign`](docs/mcp/byadsco--meta-ads-mcp.md#ads_update_campaign) · [`ads_delete_campaign`](docs/mcp/byadsco--meta-ads-mcp.md#ads_delete_campaign) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`create_campaign`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#create_campaign) · [`update_campaign`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#update_campaign) · [`create_adset`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#create_adset) | 59 tools |
| [Draivix/aidvertaiser](docs/mcp/Draivix--aidvertaiser.md) | [`meta_create_ad`](docs/mcp/Draivix--aidvertaiser.md#meta_create_ad) · [`meta_create_adset`](docs/mcp/Draivix--aidvertaiser.md#meta_create_adset) · [`meta_create_campaign`](docs/mcp/Draivix--aidvertaiser.md#meta_create_campaign) | 255 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`clone_ad`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#clone_ad) · [`clone_ad_set`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#clone_ad_set) · [`clone_campaign`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#clone_campaign) | 125 tools |
| [Enriquefft/meta-cli](docs/mcp/Enriquefft--meta-cli.md) | [`meta_create_ad`](docs/mcp/Enriquefft--meta-cli.md#meta_create_ad) · [`meta_create_adset`](docs/mcp/Enriquefft--meta-cli.md#meta_create_adset) · [`meta_create_campaign`](docs/mcp/Enriquefft--meta-cli.md#meta_create_campaign) | 11 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`create_campaign`](docs/mcp/mikusnuz--meta-ads-mcp.md#create_campaign) · [`update_campaign`](docs/mcp/mikusnuz--meta-ads-mcp.md#update_campaign) · [`delete_campaign`](docs/mcp/mikusnuz--meta-ads-mcp.md#delete_campaign) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_create_campaign`](docs/mcp/oliverames--meta-mcp-server.md#meta_create_campaign) · [`meta_update_campaign`](docs/mcp/oliverames--meta-mcp-server.md#meta_update_campaign) · [`meta_delete_campaign`](docs/mcp/oliverames--meta-mcp-server.md#meta_delete_campaign) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`create_campaign`](docs/mcp/pipeboard-co--meta-ads-mcp.md#create_campaign) · [`update_campaign`](docs/mcp/pipeboard-co--meta-ads-mcp.md#update_campaign) · [`create_adset`](docs/mcp/pipeboard-co--meta-ads-mcp.md#create_adset) | 41 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`create_campaign`](docs/mcp/serkanhaslak--meta-mcp.md#create_campaign) · [`update_campaign`](docs/mcp/serkanhaslak--meta-mcp.md#update_campaign) · [`delete_campaign`](docs/mcp/serkanhaslak--meta-mcp.md#delete_campaign) | 77 tools |

## Build and upload ad creatives

Upload media, assemble creatives, and inspect ad assets.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [attainmentlabs/meta-ads-mcp](docs/mcp/attainmentlabs--meta-ads-mcp.md) | [`upload_ad_image`](docs/mcp/attainmentlabs--meta-ads-mcp.md#upload_ad_image) | 13 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`get_ad_creatives`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_ad_creatives) · [`get_creative_details`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_creative_details) · [`create_ad_creative`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#create_ad_creative) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`create_ad_creative`](docs/mcp/brijr--meta-mcp.md#create_ad_creative) · [`get_ad_preview`](docs/mcp/brijr--meta-mcp.md#get_ad_preview) · [`get_video_status`](docs/mcp/brijr--meta-mcp.md#get_video_status) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_get_ad_creatives`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_ad_creatives) · [`ads_get_creative_details`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_creative_details) · [`ads_create_ad_creative`](docs/mcp/byadsco--meta-ads-mcp.md#ads_create_ad_creative) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`get_ad_creatives`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_ad_creatives) · [`get_ad_image`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_ad_image) · [`save_ad_image_locally`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#save_ad_image_locally) | 59 tools |
| [Draivix/aidvertaiser](docs/mcp/Draivix--aidvertaiser.md) | [`meta_create_creative`](docs/mcp/Draivix--aidvertaiser.md#meta_create_creative) · [`meta_create_video_creative`](docs/mcp/Draivix--aidvertaiser.md#meta_create_video_creative) · [`meta_get_ad_creatives`](docs/mcp/Draivix--aidvertaiser.md#meta_get_ad_creatives) | 255 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`change_ad_labels`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#change_ad_labels) · [`create_ad_creative`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_ad_creative) · [`delete_ad_media`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#delete_ad_media) | 125 tools |
| [Enriquefft/meta-cli](docs/mcp/Enriquefft--meta-cli.md) | [`meta_create_creative`](docs/mcp/Enriquefft--meta-cli.md#meta_create_creative) · [`meta_upload_image`](docs/mcp/Enriquefft--meta-cli.md#meta_upload_image) · [`meta_upload_video`](docs/mcp/Enriquefft--meta-cli.md#meta_upload_video) | 11 tools |
| [gomarble-ai/facebook-ads-mcp-server](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md) | [`get_ad_creative_by_id`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_ad_creative_by_id) · [`get_ad_creatives_by_ad_id`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_ad_creatives_by_ad_id) | 21 tools |
| [markifact/markifact-mcp](docs/mcp/markifact--markifact-mcp.md) | [`upload_media`](docs/mcp/markifact--markifact-mcp.md#upload_media) · [`prepare_media_upload`](docs/mcp/markifact--markifact-mcp.md#prepare_media_upload) | 10 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`get_ad_preview`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_ad_preview) · [`list_creatives`](docs/mcp/mikusnuz--meta-ads-mcp.md#list_creatives) · [`get_creative`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_creative) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_get_promotable_posts`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_promotable_posts) · [`meta_list_ad_creatives`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_ad_creatives) · [`meta_create_ad_creative`](docs/mcp/oliverames--meta-mcp-server.md#meta_create_ad_creative) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`get_creative_details`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_creative_details) · [`get_ad_creatives`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_ad_creatives) · [`get_ad_image`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_ad_image) | 41 tools |
| [proxy-intell/facebook-ads-library-mcp](docs/mcp/proxy-intell--facebook-ads-library-mcp.md) | [`analyze_ad_video`](docs/mcp/proxy-intell--facebook-ads-library-mcp.md#analyze_ad_video) · [`analyze_ad_videos_batch`](docs/mcp/proxy-intell--facebook-ads-library-mcp.md#analyze_ad_videos_batch) | 8 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`list_creatives`](docs/mcp/serkanhaslak--meta-mcp.md#list_creatives) · [`get_creative`](docs/mcp/serkanhaslak--meta-mcp.md#get_creative) · [`create_creative`](docs/mcp/serkanhaslak--meta-mcp.md#create_creative) | 77 tools |

## Find and manage audiences

Search targeting, manage custom audiences, and build lookalikes.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`list_custom_audiences`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#list_custom_audiences) · [`search_interests`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#search_interests) · [`search_behaviors`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#search_behaviors) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`create_custom_audience`](docs/mcp/brijr--meta-mcp.md#create_custom_audience) · [`create_lookalike_audience`](docs/mcp/brijr--meta-mcp.md#create_lookalike_audience) · [`get_audience_size`](docs/mcp/brijr--meta-mcp.md#get_audience_size) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_search_interests`](docs/mcp/byadsco--meta-ads-mcp.md#ads_search_interests) · [`ads_get_interest_suggestions`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_interest_suggestions) · [`ads_search_behaviors`](docs/mcp/byadsco--meta-ads-mcp.md#ads_search_behaviors) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`search_interests`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#search_interests) · [`get_interest_suggestions`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_interest_suggestions) · [`estimate_audience_size`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#estimate_audience_size) | 59 tools |
| [Draivix/aidvertaiser](docs/mcp/Draivix--aidvertaiser.md) | [`meta_add_users_to_audience`](docs/mcp/Draivix--aidvertaiser.md#meta_add_users_to_audience) · [`meta_create_custom_audience`](docs/mcp/Draivix--aidvertaiser.md#meta_create_custom_audience) · [`meta_create_lookalike_audience`](docs/mcp/Draivix--aidvertaiser.md#meta_create_lookalike_audience) | 255 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`create_custom_audience`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_custom_audience) · [`create_lookalike_audience`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_lookalike_audience) · [`delete_custom_audience`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#delete_custom_audience) | 125 tools |
| [Enriquefft/meta-cli](docs/mcp/Enriquefft--meta-cli.md) | [`meta_search_targeting`](docs/mcp/Enriquefft--meta-cli.md#meta_search_targeting) | 11 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`get_adset_targeting_sentence`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_adset_targeting_sentence) · [`get_delivery_estimate`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_delivery_estimate) · [`list_custom_audiences`](docs/mcp/mikusnuz--meta-ads-mcp.md#list_custom_audiences) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_search_targeting_interests`](docs/mcp/oliverames--meta-mcp-server.md#meta_search_targeting_interests) · [`meta_search_targeting_geolocations`](docs/mcp/oliverames--meta-mcp-server.md#meta_search_targeting_geolocations) · [`meta_search_targeting_demographics`](docs/mcp/oliverames--meta-mcp-server.md#meta_search_targeting_demographics) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`search_interests`](docs/mcp/pipeboard-co--meta-ads-mcp.md#search_interests) · [`get_interest_suggestions`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_interest_suggestions) · [`estimate_audience_size`](docs/mcp/pipeboard-co--meta-ads-mcp.md#estimate_audience_size) | 41 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`get_delivery_estimate`](docs/mcp/serkanhaslak--meta-mcp.md#get_delivery_estimate) · [`list_custom_audiences`](docs/mcp/serkanhaslak--meta-mcp.md#list_custom_audiences) · [`create_custom_audience`](docs/mcp/serkanhaslak--meta-mcp.md#create_custom_audience) | 77 tools |

## Send and validate conversion signals

Work with pixels, conversion events, datasets, and tracking validation.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [aleksUIX/pixellint](docs/mcp/aleksUIX--pixellint.md) | [`validate_artifact`](docs/mcp/aleksUIX--pixellint.md#validate_artifact) · [`validate_har`](docs/mcp/aleksUIX--pixellint.md#validate_har) · [`validate_sessions`](docs/mcp/aleksUIX--pixellint.md#validate_sessions) | 5 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`get_pixel_info`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_pixel_info) · [`get_pixel_events`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_pixel_events) · [`get_event_stats`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_event_stats) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`get_custom_conversions`](docs/mcp/brijr--meta-mcp.md#get_custom_conversions) · [`get_pixels`](docs/mcp/brijr--meta-mcp.md#get_pixels) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_get_pixels`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_pixels) · [`ads_get_pixel_details`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_pixel_details) · [`ads_get_pixel_events`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_pixel_events) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`send_capi_event`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#send_capi_event) | 59 tools |
| [Draivix/aidvertaiser](docs/mcp/Draivix--aidvertaiser.md) | [`meta_create_custom_conversion`](docs/mcp/Draivix--aidvertaiser.md#meta_create_custom_conversion) · [`meta_create_offline_conversion_set`](docs/mcp/Draivix--aidvertaiser.md#meta_create_offline_conversion_set) · [`meta_create_pixel`](docs/mcp/Draivix--aidvertaiser.md#meta_create_pixel) | 255 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`create_custom_conversion`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_custom_conversion) · [`delete_custom_conversion`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#delete_custom_conversion) · [`list_business_datasets`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#list_business_datasets) | 125 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`send_conversion_event`](docs/mcp/mikusnuz--meta-ads-mcp.md#send_conversion_event) · [`send_offline_event`](docs/mcp/mikusnuz--meta-ads-mcp.md#send_offline_event) · [`list_offline_event_sets`](docs/mcp/mikusnuz--meta-ads-mcp.md#list_offline_event_sets) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_list_pixels`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_pixels) · [`meta_create_pixel`](docs/mcp/oliverames--meta-mcp-server.md#meta_create_pixel) · [`meta_get_pixel`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_pixel) | 199 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`send_conversion_event`](docs/mcp/serkanhaslak--meta-mcp.md#send_conversion_event) · [`list_pixels`](docs/mcp/serkanhaslak--meta-mcp.md#list_pixels) · [`get_pixel`](docs/mcp/serkanhaslak--meta-mcp.md#get_pixel) | 77 tools |

## Research public ads

Search the Ad Library and inspect competitor advertising.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_library_scrape`](docs/mcp/byadsco--meta-ads-mcp.md#ads_library_scrape) · [`ads_library_get_run_status`](docs/mcp/byadsco--meta-ads-mcp.md#ads_library_get_run_status) · [`ads_library_get_results`](docs/mcp/byadsco--meta-ads-mcp.md#ads_library_get_results) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`search_ads_archive`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#search_ads_archive) | 59 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`search_ads_archive`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#search_ads_archive) | 125 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`search_ad_library`](docs/mcp/mikusnuz--meta-ads-mcp.md#search_ad_library) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_search_ad_library`](docs/mcp/oliverames--meta-mcp-server.md#meta_search_ad_library) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`search_ads_archive`](docs/mcp/pipeboard-co--meta-ads-mcp.md#search_ads_archive) | 41 tools |
| [proxy-intell/facebook-ads-library-mcp](docs/mcp/proxy-intell--facebook-ads-library-mcp.md) | [`get_meta_platform_id`](docs/mcp/proxy-intell--facebook-ads-library-mcp.md#get_meta_platform_id) · [`get_meta_ads`](docs/mcp/proxy-intell--facebook-ads-library-mcp.md#get_meta_ads) | 8 tools |
| [RamsesAguirre777/facebook-ads-library-mcp](docs/mcp/RamsesAguirre777--facebook-ads-library-mcp.md) | [`search_ad_library`](docs/mcp/RamsesAguirre777--facebook-ads-library-mcp.md#search_ad_library) · [`scrape_ad_library_url`](docs/mcp/RamsesAguirre777--facebook-ads-library-mcp.md#scrape_ad_library_url) | 2 tools |

## Manage advertising catalogs

Work with product catalogs, feeds, and product sets for ads.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`get_catalog_info`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_catalog_info) · [`get_catalog_products`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_catalog_products) · [`get_product_sets`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_product_sets) | 57 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`batch_catalog_items`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#batch_catalog_items) · [`batch_products`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#batch_products) · [`configure_catalog_advertising`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#configure_catalog_advertising) | 125 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`list_catalogs`](docs/mcp/mikusnuz--meta-ads-mcp.md#list_catalogs) · [`get_catalog`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_catalog) · [`create_catalog`](docs/mcp/mikusnuz--meta-ads-mcp.md#create_catalog) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_get_instagram_available_catalogs`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_instagram_available_catalogs) · [`meta_search_instagram_catalog_products`](docs/mcp/oliverames--meta-mcp-server.md#meta_search_instagram_catalog_products) · [`meta_list_product_catalogs`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_product_catalogs) | 199 tools |

## Work with lead ads

Manage lead forms and retrieve advertising leads.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_get_lead_forms`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_lead_forms) · [`ads_get_leads`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_leads) · [`ads_get_ad_leads`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_ad_leads) | 142 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`create_lead_form`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_lead_form) · [`create_test_lead`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_test_lead) · [`delete_test_lead`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#delete_test_lead) | 125 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`get_campaign_leads`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_campaign_leads) · [`get_adset_leads`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_adset_leads) · [`get_form_leads`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_form_leads) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_list_leadgen_forms`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_leadgen_forms) · [`meta_get_leadgen_leads`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_leadgen_leads) | 199 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`get_lead_forms`](docs/mcp/serkanhaslak--meta-mcp.md#get_lead_forms) · [`get_leads`](docs/mcp/serkanhaslak--meta-mcp.md#get_leads) | 77 tools |

## Automate and control changes

Create rules, batch operations, and preview or confirm mutations.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [attainmentlabs/meta-ads-mcp](docs/mcp/attainmentlabs--meta-ads-mcp.md) | [`bulk_update_campaign_status`](docs/mcp/attainmentlabs--meta-ads-mcp.md#bulk_update_campaign_status) | 13 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`bulk_rename_objects`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#bulk_rename_objects) · [`delete_campaign_structure`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#delete_campaign_structure) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`bulk_create_ads`](docs/mcp/brijr--meta-mcp.md#bulk_create_ads) · [`bulk_update_status`](docs/mcp/brijr--meta-mcp.md#bulk_update_status) · [`clone_campaign_structure`](docs/mcp/brijr--meta-mcp.md#clone_campaign_structure) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_get_ad_rules`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_ad_rules) · [`ads_create_ad_rule`](docs/mcp/byadsco--meta-ads-mcp.md#ads_create_ad_rule) · [`ads_get_rule_details`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_rule_details) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`batch_request`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#batch_request) | 59 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`apply_mutation_plan`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#apply_mutation_plan) · [`build_mutation_plan`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#build_mutation_plan) · [`discard_mutation_plan`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#discard_mutation_plan) | 125 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`list_rules`](docs/mcp/mikusnuz--meta-ads-mcp.md#list_rules) · [`get_rule`](docs/mcp/mikusnuz--meta-ads-mcp.md#get_rule) · [`create_rule`](docs/mcp/mikusnuz--meta-ads-mcp.md#create_rule) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_list_ad_rules`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_ad_rules) · [`meta_create_ad_rule`](docs/mcp/oliverames--meta-mcp-server.md#meta_create_ad_rule) · [`meta_delete_ad_rule`](docs/mcp/oliverames--meta-mcp-server.md#meta_delete_ad_rule) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`create_budget_schedule`](docs/mcp/pipeboard-co--meta-ads-mcp.md#create_budget_schedule) · [`duplicate_campaign`](docs/mcp/pipeboard-co--meta-ads-mcp.md#duplicate_campaign) · [`duplicate_adset`](docs/mcp/pipeboard-co--meta-ads-mcp.md#duplicate_adset) | 41 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`batch_request`](docs/mcp/serkanhaslak--meta-mcp.md#batch_request) · [`list_ad_rules`](docs/mcp/serkanhaslak--meta-mcp.md#list_ad_rules) · [`create_ad_rule`](docs/mcp/serkanhaslak--meta-mcp.md#create_ad_rule) | 77 tools |

## Connect advertising accounts

Discover accounts, permissions, businesses, pages, and advertising identities.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [attainmentlabs/meta-ads-mcp](docs/mcp/attainmentlabs--meta-ads-mcp.md) | [`get_ad_account_summary`](docs/mcp/attainmentlabs--meta-ads-mcp.md#get_ad_account_summary) | 13 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`check_token_status`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#check_token_status) · [`get_ad_accounts`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_ad_accounts) · [`get_account_info`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#get_account_info) | 57 tools |
| [brijr/meta-mcp](docs/mcp/brijr--meta-mcp.md) | [`get_ad_accounts`](docs/mcp/brijr--meta-mcp.md#get_ad_accounts) · [`get_pages`](docs/mcp/brijr--meta-mcp.md#get_pages) · [`validate_account`](docs/mcp/brijr--meta-mcp.md#validate_account) | 39 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_get_ad_accounts`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_ad_accounts) · [`ads_get_account_info`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_account_info) · [`ads_get_pages_for_business`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_pages_for_business) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`get_ad_accounts`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_ad_accounts) · [`get_account_info`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_account_info) · [`search_pages_by_name`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#search_pages_by_name) | 59 tools |
| [Draivix/aidvertaiser](docs/mcp/Draivix--aidvertaiser.md) | [`meta_get_account_info`](docs/mcp/Draivix--aidvertaiser.md#meta_get_account_info) · [`meta_get_login_link`](docs/mcp/Draivix--aidvertaiser.md#meta_get_login_link) · [`meta_list_accounts`](docs/mcp/Draivix--aidvertaiser.md#meta_list_accounts) | 255 tools |
| [EfrainTorres/armavita-meta-ads-mcp](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md) | [`create_business_asset`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_business_asset) · [`create_page_backed_instagram_account`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_page_backed_instagram_account) · [`create_threads_account`](docs/mcp/EfrainTorres--armavita-meta-ads-mcp.md#create_threads_account) | 125 tools |
| [Enriquefft/meta-cli](docs/mcp/Enriquefft--meta-cli.md) | [`meta_list_accounts`](docs/mcp/Enriquefft--meta-cli.md#meta_list_accounts) · [`meta_list_pages`](docs/mcp/Enriquefft--meta-cli.md#meta_list_pages) | 11 tools |
| [gomarble-ai/facebook-ads-mcp-server](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md) | [`list_ad_accounts`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#list_ad_accounts) · [`get_details_of_ad_account`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#get_details_of_ad_account) | 21 tools |
| [markifact/markifact-mcp](docs/mcp/markifact--markifact-mcp.md) | [`list_connections`](docs/mcp/markifact--markifact-mcp.md#list_connections) | 10 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`list_block_lists`](docs/mcp/mikusnuz--meta-ads-mcp.md#list_block_lists) · [`create_block_list`](docs/mcp/mikusnuz--meta-ads-mcp.md#create_block_list) · [`add_to_block_list`](docs/mcp/mikusnuz--meta-ads-mcp.md#add_to_block_list) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_list_pages`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_pages) · [`meta_get_page`](docs/mcp/oliverames--meta-mcp-server.md#meta_get_page) · [`meta_list_instagram_accounts`](docs/mcp/oliverames--meta-mcp-server.md#meta_list_instagram_accounts) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`get_ad_accounts`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_ad_accounts) · [`get_account_info`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_account_info) · [`search_pages_by_name`](docs/mcp/pipeboard-co--meta-ads-mcp.md#search_pages_by_name) | 41 tools |
| [serkanhaslak/meta-mcp](docs/mcp/serkanhaslak--meta-mcp.md) | [`get_ad_accounts`](docs/mcp/serkanhaslak--meta-mcp.md#get_ad_accounts) · [`get_account_info`](docs/mcp/serkanhaslak--meta-mcp.md#get_account_info) · [`get_account_pages`](docs/mcp/serkanhaslak--meta-mcp.md#get_account_pages) | 77 tools |

## Discover and dispatch advertising operations

Find operation IDs, retrieve operation-specific input schemas, and dispatch read or write requests through a shared router.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [markifact/markifact-mcp](docs/mcp/markifact--markifact-mcp.md) | [`find_operations`](docs/mcp/markifact--markifact-mcp.md#find_operations) · [`get_operation_inputs`](docs/mcp/markifact--markifact-mcp.md#get_operation_inputs) · [`run_operation`](docs/mcp/markifact--markifact-mcp.md#run_operation) | 10 tools |

## Inspect and troubleshoot integrations

Inspect available APIs, authentication, validation rules, and local supporting data.

| MCP | Verified tool examples | Full inventory |
|---|---|---|
| [aleksUIX/pixellint](docs/mcp/aleksUIX--pixellint.md) | [`list_rulepacks`](docs/mcp/aleksUIX--pixellint.md#list_rulepacks) · [`list_vendors`](docs/mcp/aleksUIX--pixellint.md#list_vendors) | 5 tools |
| [brandu-mos/konquest-meta-ads-mcp](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md) | [`generate_names`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#generate_names) · [`read_client_vault`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#read_client_vault) · [`run_setup_check`](docs/mcp/brandu-mos--konquest-meta-ads-mcp.md#run_setup_check) | 57 tools |
| [byadsco/meta-ads-mcp](docs/mcp/byadsco--meta-ads-mcp.md) | [`ads_rate_status`](docs/mcp/byadsco--meta-ads-mcp.md#ads_rate_status) · [`ads_get_help_article`](docs/mcp/byadsco--meta-ads-mcp.md#ads_get_help_article) · [`ads_library_register_apify_token`](docs/mcp/byadsco--meta-ads-mcp.md#ads_library_register_apify_token) | 142 tools |
| [dengineproblem/meta-ads-mcp-extended](docs/mcp/dengineproblem--meta-ads-mcp-extended.md) | [`get_login_link`](docs/mcp/dengineproblem--meta-ads-mcp-extended.md#get_login_link) | 59 tools |
| [Enriquefft/meta-cli](docs/mcp/Enriquefft--meta-cli.md) | [`meta_auth_status`](docs/mcp/Enriquefft--meta-cli.md#meta_auth_status) | 11 tools |
| [gomarble-ai/facebook-ads-mcp-server](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md) | [`fetch_pagination_url`](docs/mcp/gomarble-ai--facebook-ads-mcp-server.md#fetch_pagination_url) | 21 tools |
| [markifact/markifact-mcp](docs/mcp/markifact--markifact-mcp.md) | [`get_file_url`](docs/mcp/markifact--markifact-mcp.md#get_file_url) · [`read_file`](docs/mcp/markifact--markifact-mcp.md#read_file) | 10 tools |
| [mikusnuz/meta-ads-mcp](docs/mcp/mikusnuz--meta-ads-mcp.md) | [`exchange_token`](docs/mcp/mikusnuz--meta-ads-mcp.md#exchange_token) · [`refresh_token`](docs/mcp/mikusnuz--meta-ads-mcp.md#refresh_token) · [`debug_token`](docs/mcp/mikusnuz--meta-ads-mcp.md#debug_token) | 134 tools |
| [oliverames/meta-mcp-server](docs/mcp/oliverames--meta-mcp-server.md) | [`meta_debug_token`](docs/mcp/oliverames--meta-mcp-server.md#meta_debug_token) · [`meta_health_check`](docs/mcp/oliverames--meta-mcp-server.md#meta_health_check) · [`meta_generate_chart`](docs/mcp/oliverames--meta-mcp-server.md#meta_generate_chart) | 199 tools |
| [pipeboard-co/meta-ads-mcp](docs/mcp/pipeboard-co--meta-ads-mcp.md) | [`compute_image_crops`](docs/mcp/pipeboard-co--meta-ads-mcp.md#compute_image_crops) · [`get_login_link`](docs/mcp/pipeboard-co--meta-ads-mcp.md#get_login_link) | 41 tools |
| [proxy-intell/facebook-ads-library-mcp](docs/mcp/proxy-intell--facebook-ads-library-mcp.md) | [`get_cache_stats`](docs/mcp/proxy-intell--facebook-ads-library-mcp.md#get_cache_stats) · [`search_cached_media`](docs/mcp/proxy-intell--facebook-ads-library-mcp.md#search_cached_media) · [`cleanup_media_cache`](docs/mcp/proxy-intell--facebook-ads-library-mcp.md#cleanup_media_cache) | 8 tools |

## Contributing

Add a source-backed tool snapshot and its evidence before adding a server. See [CONTRIBUTING.md](CONTRIBUTING.md).
