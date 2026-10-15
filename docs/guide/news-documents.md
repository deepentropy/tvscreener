# News and Filings

## News

`get_news()` returns up to 200 headlines, newest first. Without arguments it returns global news.

```python
from tvscreener import get_news, get_article

df = get_news("NASDAQ:AAPL")
df = get_news("NASDAQ:AAPL", corp_activity="insider_trading")
df = get_news(provider="reuters", market="stock", country="US")
df = get_news(market="crypto", priority="important")
```

| Filter | Values |
|--------|--------|
| `symbol` | Exchange-prefixed symbol |
| `provider` | e.g. `reuters`, `dow-jones`, `business_wire`, `tradingview`, `zacks`, `benzinga` |
| `market` | `stock`, `etf`, `crypto`, `forex`, `index`, `futures`, `bond`, `corp_bond`, `economic` |
| `sector` | Stock sector, e.g. `Finance` |
| `corp_activity` | `ipo`, `earnings`, `earnings_calls`, `dividends`, `share_buybacks`, `strategy_business_products`, `mergers_and_acquisitions`, `management`, `insider_trading`, `ownership_changes`, `esg`, `recommendation` (analyst ratings), `credit_ratings` |
| `country` | ISO code of the market, e.g. `US` |
| `priority` | `flash`, `important`, `top_stories`, `key_facts` |
| `lang` | Language, default `en` |

Filters are combined with AND, and each takes one value.

Columns: `id`, `title`, `published` (UTC), `provider`, `related_symbols`, `story_path`, `urgency`.

### Article Text

`get_article()` returns the text of a story.

```python
text = get_article(df["id"].iloc[0])           # news API (recommended)
text = get_article(df["story_path"].iloc[0])   # web page
```

- Paragraphs are separated by blank lines.
- Paywalled stories return their summary.

## Filings and Transcripts

`get_documents()` lists a company's filings, reports and transcripts (provider: Quartr).

```python
from tvscreener import get_documents, get_document

docs = get_documents("NASDAQ:AAPL")
docs = get_documents("NASDAQ:AAPL", category="call_transcript", start="2025-01-01")
docs = get_documents("NASDAQ:AAPL", category=["quarterly_report", "annual_report"])

text = get_document(docs["transcript_id"].iloc[0])     # full transcript, with speaker names
summary = get_document(docs["summary_id"].iloc[0])     # AI summary
```

| Column | Description |
|--------|-------------|
| `date` | Publication date (UTC) |
| `category` | `quarterly_report`, `annual_report`, `interim_report`, `earnings_release`, `call_transcript`, `event_transcript`, `slides` |
| `event` | `earning` or `corporate_event` |
| `fiscal_year`, `fiscal_period`, `form` | e.g. 2026, `Q3`, `10-Q` |
| `transcript_id`, `summary_id` | Pass to `get_document()` for the text |
| `pdf_id` | Id of the PDF report. `get_document()` cannot read PDFs |

## Earnings Calls

`get_earnings_calls()` lists past and scheduled earnings calls, with links to the live transcript and the recording.

```python
from tvscreener import get_earnings_calls

calls = get_earnings_calls("NASDAQ:AAPL")                       # last year and next 90 days
calls = get_earnings_calls("NASDAQ:AAPL", start="2023-01-01")
```

Columns: `date` (UTC), `title`, `fiscal_year`, `fiscal_period`, `state` (`scheduled`, `completed`...), `transcript_url` (JSON lines), `audio_url`, `audio_duration` (seconds), `id`.

!!! warning "Third-party content"
    News stories, filings, transcripts and recordings belong to their providers and have their own licences.
