# 03 Evidence Extraction

## Purpose
Extract structured facts from permitted public sources.

## Required fields where available
- Job title
- Job URL
- Company name and domain
- Technology terms
- Location
- Employment type
- Published or updated date
- Current status evidence

## Output
Evidence items with claim, classification, source URL, retrieval timestamp, and confidence.

## Hard rules
- Never invent dates or job status.
- A missing date is `unknown`.
- Preserve the original URL.
- Do not bypass access controls or collect private data.
