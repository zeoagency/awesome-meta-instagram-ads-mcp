# markifact/markifact-mcp

[Directory](../../README.md) · [Tool index](../tool-index.md) · [Upstream](https://github.com/markifact/markifact-mcp) · [Machine-readable snapshot](../../catalog/markifact--markifact-mcp.json)

Complete registered tool snapshot. **10 tools captured.**

Descriptions and input schemas reproduce upstream definitions. Capability labels come from source review.

Repository revision: [`ac9c18645e45`](https://github.com/markifact/markifact-mcp/tree/ac9c18645e4555a7a9bf22240daa2972b2461dd2). Method: `published-schema`.

- All ten tools in the provider’s version 1.0.6 manifest captured on 2026-10-13. Anonymous runtime enumeration requires authentication; repository revision pins client configuration only.
- These tools discover and dispatch dynamic operation IDs, including Meta advertising operations. Operation-specific schemas require authenticated discovery; the registered input_data objects remain open exactly as published.

## Tools

- [find_operations](#find_operations)
- [get_file_url](#get_file_url)
- [get_operation_inputs](#get_operation_inputs)
- [list_connections](#list_connections)
- [prepare_media_upload](#prepare_media_upload)
- [read_file](#read_file)
- [report_markifact_feedback](#report_markifact_feedback)
- [run_operation](#run_operation)
- [run_write_operation](#run_write_operation)
- [upload_media](#upload_media)

<a id="find_operations"></a>

## `find_operations`

Scope: **supporting** · Capability: **dispatch** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Search for available Markifact operations that can be executed by the authenticated user.

Workflow: find_operations → get_operation_inputs → run_operation (read-only) or run_write_operation (when requires_approval: true).
After selecting an operation_id, always call get_operation_inputs next. Never call run_operation / run_write_operation without first inspecting the schema via get_operation_inputs. Input shapes, nested objects, and field names vary per operation and cannot be guessed.
Returned operation IDs are registry-backed Markifact operation IDs, not arbitrary action names.

Returns JSON with matching operations containing operation_id, description, and app metadata.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "query": {
      "default": "",
      "type": "string",
      "description": "Keyword search over operation ids and descriptions. Use two to four words: the app name plus the entity or action, e.g. \"meta ads list ads\", \"gtm create tag\". Long sentences match too many operations. If the expected operation is not in the results, search again with a shorter query or a higher limit before concluding it does not exist."
    },
    "limit": {
      "default": 5,
      "type": "integer",
      "description": "Maximum results to return (default 5)."
    }
  },
  "type": "object"
}
```

</details>

<a id="get_file_url"></a>

## `get_file_url`

Scope: **supporting** · Capability: **utilities** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Get a signed URL for a private file.

Use this when an operation returns a `file_id` and you need a temporary,
directly accessible URL. Operation `file_url` values are user-facing app URLs
that require Markifact authentication; call this tool to generate a signed URL that
the model or external tools can open directly. The signed URL expires after 1 hour.

Returns a signed GCS URL for the file.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "file_id": {
      "type": "string",
      "description": "The file identifier or filename (e.g. \"file-abc123.json\", \"chart.png\")\nPass the full filename including its extension. If an extensionless prefix\nmatches multiple files, the tool returns an ambiguity error."
    }
  },
  "required": [
    "file_id"
  ],
  "type": "object"
}
```

</details>

<a id="get_operation_inputs"></a>

## `get_operation_inputs`

Scope: **supporting** · Capability: **dispatch** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Get the input schema, required fields, defaults and constraints for an operation.

Required step between find_operations and run_operation/run_write_operation. Call this once per operation_id before executing it — schemas contain nested objects, account selectors, and field names that vary per operation and cannot be guessed.
If you already retrieved the schema for this operation_id earlier in the conversation, reuse it instead of calling again.
Only pass fields from this schema in run_operation/run_write_operation input_data for the same operation_id.

Returns JSON schema describing the operation's inputs.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "operation_id": {
      "type": "string",
      "description": "Exact Markifact operation ID returned by find_operations, e.g. 'gads_get_report'."
    }
  },
  "required": [
    "operation_id"
  ],
  "type": "object"
}
```

</details>

<a id="list_connections"></a>

## `list_connections`

Scope: **supporting** · Capability: **accounts** · [Definition](https://api.markifact.com/.well-known/mcp.json)

List saved Markifact connections for an app/platform.

A connection is a saved authenticated integration in Markifact. The
returned `id` is the `connection_id` used to choose which saved
login/integration an operation should use.

Important:
- `connection_id` is not an external platform account ID.
- External account IDs, customer IDs, property IDs, and similar values are
  separate operation inputs.
- One connection may have access to multiple external accounts.
    - In most cases, you don not need to provide `connection_id`.
    If the user has only one connected login for a platform in their workspace,
    operations usually use that connection automatically. Use this tool only
    when the user wants a specific saved integration or has multiple
    connections for the same platform.

Returns JSON with available connections containing `id`, `type`, and
`display_name`.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "connection_type": {
      "default": "",
      "type": "string",
      "description": "Optional app/platform filter. Examples: 'gads', 'ga4',\n'meta_ads', 'hubspot', 'slack'. Leave empty to list all available\nconnections."
    }
  },
  "type": "object"
}
```

</details>

<a id="prepare_media_upload"></a>

## `prepare_media_upload`

Scope: **supporting** · Capability: **creatives** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Create a signed upload URL for a media file selected in the upload UI.

Returns upload details including file_id, file_url, upload_url and upload_token,
or a validation error.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "file_name": {
      "type": "string",
      "description": "Name of the selected media file."
    },
    "content_type": {
      "type": "string",
      "description": "Image or video MIME type of the selected file."
    },
    "file_size": {
      "default": 0,
      "type": "integer",
      "description": "File size in bytes. Defaults to 0 if omitted."
    }
  },
  "required": [
    "file_name",
    "content_type"
  ],
  "type": "object"
}
```

</details>

<a id="read_file"></a>

## `read_file`

Scope: **supporting** · Capability: **utilities** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Inspect a file returned by a previous operation as numbered lines of text.

Use this when an operation returns a `file_id` and you want to inspect the
file contents before deciding what to do next. This is mainly useful for
exported JSON, CSV, logs, and similar files produced by Markifact
operations.

It returns the file as numbered text lines so you can quickly review the
structure, schema, headers, sample rows, or specific sections in chunks.

Returns formatted text with line numbers.

After inspecting, you can use {{file-id}} in other tool inputs
to pass the full parsed content for processing.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "file_id": {
      "type": "string",
      "description": "File identifier from previous operations (e.g., \"file-WWIIe\")"
    },
    "offset": {
      "default": 0,
      "type": "integer",
      "description": "Starting line number (0-indexed, default: 0)"
    },
    "limit": {
      "default": 100,
      "type": "integer",
      "description": "Number of lines to read (default: 100, max: 5000)"
    }
  },
  "required": [
    "file_id"
  ],
  "type": "object"
}
```

</details>

<a id="report_markifact_feedback"></a>

## `report_markifact_feedback`

Scope: **unrelated** · Capability: **unrelated** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Submit actionable product feedback to Markifact with the user's authorization.

When you encounter a likely Markifact bug, missing capability, or product
limitation while completing a task, proactively tell the user what you found
and offer to report it to Markifact. You may draft a concise proposed report
for the user to review.

Call this tool only after either:
1. the user explicitly asks you to submit the feedback, or
2. you offered to report a discovered issue and the user explicitly agreed.

If the user's request already clearly authorizes submission, do not ask for
redundant confirmation. Do not call this tool merely to ask for permission,
and do not submit feedback silently.

This tool creates an irreversible feedback submission in Markifact's support
workflow. The submission contains the supplied feedback, relevant operation
IDs, and account-associated contact and reference identifiers. After a
successful call, briefly tell the user that the feedback was submitted.

Report only issues Markifact itself caused. Low-level operations such as
gads_mutate or meta_ads_update_adset pass requests straight to the platform,
so their responses are the platform's, not Markifact's. A write the platform
accepted is complete; if the state differs later, something else changed it.
If you are unsure how a platform behaves, research its documentation. Never
report third-party policies, outages, rate limits, rejected content, campaign
performance, or user configuration.

For a potentially missing integration capability, use the normal operation
discovery flow to check whether Markifact already provides a dedicated or
generic operation that supports the requested action. Do not execute a write
operation merely to test whether a capability exists.

Include only the minimum non-sensitive concrete evidence needed to understand the
issue. Never include passwords, API keys, access tokens, authentication
details, payment information, raw conversation history, complete request or
response payloads, or unrelated personal or customer data. Summarize relevant
errors and behavior instead of copying raw data.

Avoid duplicate or repetitive reports. Use `other` only when the feedback
does not fit another category. Write the title and description in English.
Do not promise that Markifact will respond or implement a fix.

Returns JSON confirming whether the feedback was successfully submitted to
Markifact support.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "category": {
      "enum": [
        "bug",
        "feature_request",
        "improvement",
        "other"
      ],
      "type": "string",
      "description": "Feedback type: bug, feature_request, improvement, or other."
    },
    "title": {
      "type": "string",
      "description": "Concise English title describing the Markifact issue, up to 140\ncharacters."
    },
    "description": {
      "type": "string",
      "description": "Concise English explanation of the expected behavior, actual\nbehavior, user impact, and minimal non-sensitive evidence, up to\n10,000 characters."
    },
    "impact": {
      "enum": [
        "low",
        "medium",
        "high"
      ],
      "type": "string",
      "description": "Severity based on blocked work and affected scope: low, medium,\nor high."
    },
    "operation_ids": {
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
      "description": "Relevant Markifact operation IDs, when known."
    }
  },
  "required": [
    "category",
    "title",
    "description",
    "impact"
  ],
  "type": "object"
}
```

</details>

<a id="run_operation"></a>

## `run_operation`

Scope: **meta-ads** · Capability: **dispatch** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Execute a **read-only** Markifact operation, such as fetching reports,
listing records, selecting accounts, or looking up account details.

Use this in direct response to the user's current request. Do not use it for startup checks or background context gathering.

For write/create/update/delete actions, use `run_write_operation` instead.
Operations returned by `find_operations` with `requires_approval: true` MUST be executed via `run_write_operation`.
operation_id must be an exact Markifact operation ID returned by find_operations for the authenticated user.

Never call this without first inspecting the schema via `get_operation_inputs`. Input shapes, nested objects, and field names vary per operation and cannot be guessed.
input_data must contain only fields from the get_operation_inputs schema for the same operation_id.

Reporting tips
- Reporting operations (GA4, Google Ads, Meta Ads, etc.) require account IDs. Use the relevant `select_accounts` operation first, treating user-provided account names as substring matches.
- Never guess metric or dimension values. Use the relevant `list_report_fields` operation to confirm available fields before building a report.
- For Google Ads, always prefer using the `gads_get_report` operation. Use `gads_run_gaql_query` only for advanced or unsupported reporting queries.

Files
- Some operations may return `file_id` when datasets are too large. You will also receive a small `data_preview` for context.
- You can reference any file ID in other operation inputs using this syntax: `{{file-id}}`, for example: `{"data": "{{file-xe3fw}}"}` (exactly as provided—do not modify or invent file ids).
- When you pass a `file_id` to another operation, the file content will be automatically loaded and converted to the correct data type. JSON becomes Python dict/list, CSV/XLSX becomes a list of dicts (rows), and images/binary files become raw bytes. You do **not** need to handle parsing or conversion—just pass `{{file-id}}`.
- The file ID is for you to move data between operations efficiently. When sharing results with the user, always share links using the `get_file_url` tool.

Returns JSON with the operation result.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "operation_id": {
      "type": "string",
      "description": "Exact Markifact read operation ID returned by find_operations, e.g. \"meta_ads_select_accounts\", \"gads_list_report_fields\", \"ga4_get_report\"."
    },
    "input_data": {
      "additionalProperties": true,
      "type": "object",
      "description": "Dict matching the selected operation's schema from get_operation_inputs. Pass {} if no inputs are needed."
    }
  },
  "required": [
    "operation_id",
    "input_data"
  ],
  "type": "object"
}
```

</details>

<a id="run_write_operation"></a>

## `run_write_operation`

Scope: **meta-ads** · Capability: **dispatch** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Execute a **write** operation that creates, updates, or deletes external data.

Use this tool ONLY for operations marked with `requires_approval: true` in
`find_operations` results. These are destructive actions like creating campaigns,
updating ad statuses, sending emails, etc.
operation_id must be an exact Markifact operation ID returned by find_operations for the authenticated user.

**APPROVAL REQUIRED**: Every call writes irreversibly to the user's live external accounts.
Before each invocation, summarize the exact change in plain language (operation, target account/resource, key field values)
and wait for explicit user confirmation. Never call without user's confirmation, approval is CRITICAL.

Never call this without first inspecting the schema via `get_operation_inputs`. Input shapes, nested objects, and field names vary per operation and cannot be guessed.
input_data must contain only fields from the get_operation_inputs schema for the same operation_id.

Write-operation tips
- Always prefer a dedicated operation when one already matches the task.
- Some platforms have a generic fallback operation for create, update, or remove mutations not covered by a dedicated operation, for example `gads_mutate` for Google Ads. Use the fallback before reporting a missing write feature.

Files
- Some operations may return `file_id` when datasets are too large. You will also receive a small `data_preview` for context.
- You can reference any file ID in other operation inputs using this syntax: `{{file-id}}`, for example: `{"data": "{{file-xe3fw}}"}` (exactly as provided—do not modify or invent file ids).
- When you pass a `file_id` to another operation, the file content will be automatically loaded and converted to the correct data type. JSON becomes Python dict/list, CSV/XLSX becomes a list of dicts (rows), and images/binary files become raw bytes. You do **not** need to handle parsing or conversion—just pass `{{file-id}}`.
- The file ID is for you to move data between operations efficiently. When sharing results with the user, always share links using the `get_file_url` tool.

Returns JSON with the operation result.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {
    "operation_id": {
      "type": "string",
      "description": "Exact Markifact write operation ID returned by find_operations, e.g. \"gads_create_campaign\", \"gads_edit_responsive_search_ad\", \"meta_ads_update_campaign_budget\", \"sheets_write_data\"."
    },
    "input_data": {
      "additionalProperties": true,
      "type": "object",
      "description": "Dict matching the selected operation's schema from get_operation_inputs. Pass {} if no inputs are needed."
    }
  },
  "required": [
    "operation_id",
    "input_data"
  ],
  "type": "object"
}
```

</details>

<a id="upload_media"></a>

## `upload_media`

Scope: **supporting** · Capability: **creatives** · [Definition](https://api.markifact.com/.well-known/mcp.json)

Upload an image or video asset for later operations.

Use this when the user needs to provide media that will be reused in later tool calls, for example
creating Facebook ad image or video asset, or a Google Ads creative flow.
The tool returns file URLs that can be passed into later operations that accept uploaded media.
Only image and video uploads are supported.

<details>
<summary>Full input schema</summary>

```json
{
  "additionalProperties": false,
  "properties": {},
  "type": "object"
}
```

</details>

