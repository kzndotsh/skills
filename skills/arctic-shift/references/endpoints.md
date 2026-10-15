# Arctic Shift endpoint reference

Condensed from the upstream API README (<https://github.com/ArthurHeitmann/arctic_shift/blob/master/api/README.md>). Check upstream if a parameter here is rejected.

## Contents
- Conventions
- Search: posts and comments
- Comment tree
- Aggregations
- Subreddits
- Users
- Short links and time series
- Selectable fields

## Conventions
- **Date** (`after`, `before`): epoch seconds or milliseconds; ISO 8601 (`2020-01-01`, `2020-01-01 00:00:00`, `2020-01-01T00:00:00.000Z`); or an offset from now (`1year`, `3m`, `2d`, `1hour`, `5min`, `10s`).
- **Boolean**: `true/1/yes/y`, `false/0/no/n`.
- **ID**: base 36, optional `t3_` (post) or `t1_` (comment) prefix.
- `u/` and `r/` prefixes on `author` and `subreddit` are ignored.
- List parameters are comma separated.

## Search: posts and comments
`GET /api/posts/search`, `GET /api/comments/search`

Common: `author`, `subreddit`, `author_flair_text` (keyword), `after`, `before`, `limit` (1-100 or `auto`, default 25), `sort` (`asc`|`desc` by `created_utc`), `md2html`, `fields`, `format` (`json`|`rss`|`jsonfeed`).

Posts only: `title`, `selftext`, `link_flair_text`, `query` (title + selftext) are keyword searches and need `author` or `subreddit`; also `crosspost_parent_id`, `over_18`, `spoiler`, `url` (prefix match), `url_exact`.

Comments only: `body` (keyword; needs `author`, `subreddit`, `link_id`, or `parent_id`), `link_id` (post), `parent_id` (empty means top-level only).

## Comment tree
`GET /api/comments/tree` — `link_id` (required), `parent_id`, `limit` (1-25000, default 50), `start_breadth` (default 4), `start_depth` (default 4), `md2html`. Over-limit branches collapse into `"kind":"more"` nodes with a `children` list.

## Aggregations
`GET /api/posts/search/aggregate`, `GET /api/comments/search/aggregate`

`aggregate` = `created_utc` | `author` | `subreddit`. `frequency` is required with `created_utc` (for example `year`, `month`, `day`). Also `limit` (empty means no limit), `min_count` (not with `created_utc`), `sort`. Accepts all search filters. Busy subreddits and users time out; narrow the date range.

## Subreddits
- `GET /api/subreddits/search`: `subreddit`, `subreddit_prefix`, `after`/`before` (creation date), `min_subscribers`, `max_subscribers`, `over18`, `limit` (1-1000), `sort`, `sort_type` (`created_utc`|`subscribers`|`subreddit`). The list updates infrequently.
- `GET /api/subreddits/ids?ids=...` (max 500).
- `GET /api/subreddits/rules?subreddits=a,b` (max 1000).
- `GET /api/subreddits/wikis?subreddit=x` or `?paths=/r/x/wiki/faq,...` (max 100); `GET /api/subreddits/wikis/list?subreddit=x` lists page paths.

## Users
- `GET /api/users/search`: `author`, `author_prefix`, `min_num_posts`, `min_num_comments`, `active_since`, `min_karma`, `limit` (1-1000), `sort`, `sort_type` (`author`|`total_karma`). Aggregate data only; updated infrequently.
- `GET /api/users/interactions/users` (counts) and `/users/list` (each interaction): `author` (required), `subreddit`, `after`, `before`, `min_count`, `limit`.
- `GET /api/users/interactions/subreddits`: `author` (required), `weight_posts`, `weight_comments`, `after`, `before`, `min_count`, `limit`.
- `GET /api/users/aggregate_flairs?author=x`.
- Very active users and bots time out; narrow with `after`/`before`.

## Short links and time series
- `GET /api/short_links?paths=/r/running/s/3TzXiyxaMD` (max 1000, case sensitive) returns the full link.
- `GET /api/time_series?key=...&precision=year|quarter|month|week|day|hour|minute&after=&before=`. Keys: `global/{posts,comments}/{count,sum_score,sum_retrieved_after_seconds}`, `r/<subreddit>/{posts,comments}/{count,sum_score}`, `r/<subreddit>/subscribers`. Can lag by hours or days.

## Selectable fields
- Both: `author`, `author_fullname`, `author_flair_text`, `created_utc`, `distinguished`, `id`, `retrieved_on`, `subreddit`, `subreddit_id`, `score`.
- Posts: `crosspost_parent`, `link_flair_text`, `num_comments`, `over_18`, `post_hint`, `selftext`, `spoiler`, `title`, `url`.
- Comments: `body`, `link_id`, `parent_id`.
- Subreddits: `created_utc`, `description`, `public_description`, `display_name`, `id`, `over18`, `retrieved_on`, `subscribers`, `title`.
