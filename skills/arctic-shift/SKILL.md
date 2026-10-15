---
name: arctic-shift
description: Query archived Reddit posts, comments, subreddits, and users through the free Arctic Shift HTTP API, since reddit.com and Reddit's own API block automated access. Use when you need to read Reddit threads, search a subreddit or user's history, pull a full comment tree, sweep a topic over a date range, count activity over time, or fetch subreddit rules and wikis, for research or analysis at any scale.
---

# Arctic Shift

Arctic Shift is a public archive of Reddit with a JSON API. Use it instead of fetching reddit.com, old.reddit.com, or `.json` URLs, which fail for automated clients.

Base URL: `https://arctic-shift.photon-reddit.com` (no auth). Docs: <https://github.com/ArthurHeitmann/arctic_shift/tree/master/api>. Status: <https://status.arctic-shift.photon-reddit.com>.

## When to use
- Read a Reddit thread or a user's history when direct access is blocked.
- Find what a community says about a topic, over time or in a window.
- Build a dataset of posts or comments from a subreddit.
- Resolve a Reddit short link, or look up subreddit rules and wikis.

## Steps
1. Pick the endpoint. Known post or comment IDs: `/api/posts/ids`, `/api/comments/ids`. Whole thread: `/api/comments/tree`. Keyword or filter search: `/api/posts/search`, `/api/comments/search`. Counts and rankings: the `/aggregate` variants or `/api/time_series`. Full parameter tables: `references/endpoints.md`.
2. Always scope searches with `subreddit`, `author`, `link_id`, or `parent_id`. Keyword params (`title`, `selftext`, `body`, `query`) need at least one of these and fail on very active subreddits or users.
3. Always pass `fields=` to cut payload and latency. Posts: `id,title,selftext,score,created_utc,author,num_comments`. Comments: `id,body,score,created_utc,author,link_id,parent_id`.
4. Fetch with `curl -s` or any HTTP client and read the `data` array. Errors come back as `{"data":null,"error":"..."}`.
5. Paginate by date, not by offset. Use `sort=asc`, `limit=100`, and set the next `after` to the last row's `created_utc`. Stop on an empty `data`. `limit=auto` returns 100 to 1000 rows per call depending on server load.

```bash
B=https://arctic-shift.photon-reddit.com
# keyword search in one subreddit
curl -s "$B/api/posts/search?subreddit=worldnews&title=wuhan&after=2019-12-30&sort=asc&limit=10&fields=id,title,score"
# comments containing a phrase, bounded in time
curl -s "$B/api/comments/search?subreddit=Replika&body=remembers+me&after=2024-01-01&before=2025-01-01&limit=100&fields=body,score,link_id"
# whole thread
curl -s "$B/api/comments/tree?link_id=t3_x8i09x&limit=9999"
# activity per year
curl -s "$B/api/comments/search/aggregate?aggregate=created_utc&frequency=year&subreddit=Replika&after=2020-01-01"
```

## Keyword syntax
Post search is plain keyword matching. Comment search uses Postgres `websearch_to_tsquery`: `a b` is AND in any order, `"a b"` is a phrase, `a OR b`, `a -b`. The docs mark this section out of date, so test a query before relying on a feature.

## Cautions
- **Timeouts and 422s are normal on big subreddits.** `{"error":"Timeout. Maybe slow down a bit"}` and 422 on `query` are the usual signs. Narrow with `after`/`before`, swap `query` for `title` or `body`, drop `sort`, or request fewer `fields`. If the status page is red, wait.
- **Rate limit.** On 429, sleep until the `X-RateLimit-Reset` header (seconds). Send requests serially, with a short pause between pages.
- **Data is a snapshot.** Scores and bodies reflect when the item was archived (`retrieved_on`), not now. Recent items may be missing or lag by hours. Deleted content may show `[deleted]` or `[removed]`.
- **IDs.** Base 36. `t3_` prefix means post, `t1_` means comment. `link_id` on a comment is the post's `t3_` ID; `comments/tree` takes it with or without the prefix.
- **`comments/tree` collapses past `limit`.** Collapsed nodes have `"kind":"more"` and a `children` ID list. Use `limit=9999` for everything (max 25000), or fetch the IDs via `/api/comments/ids` (max 500 per call).
- **Bulk work.** For whole-subreddit or multi-year sweeps, the API is the wrong tool. The project publishes monthly dumps; see its GitHub README.
- **No guarantees.** The service is free and best-effort. Cache results you need again.
- **Citing.** Name the source and year: `r/<subreddit>, via Arctic Shift, <year>`, and keep the post ID or permalink so a reader can verify.
