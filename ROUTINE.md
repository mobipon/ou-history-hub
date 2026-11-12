# Routine: new OU football history & trivia, 5 times a day

You run **5 times a day** (about 7 a.m., 10 a.m., 1 p.m., 4 p.m. and 7 p.m. Central). Each run
**publishes 1 new post immediately** and **refreshes 1 existing post** with any new information,
for the OU History & Trivia Hub on https://oklahomasoonerfootball.com/history/ (an **unofficial**
Oklahoma Sooners football fan site). The site reads this repo's `index.json` and `posts/*.json`
about every 10 minutes; pushing to `main` is publishing.

## Steps

1. `git pull`. Read `index.json` to see every existing post (slug, question, people, year, category,
   publish_at, updated_at).
2. **New post.** Pick 1 topic that is **not already covered** (no repeated question; a player may
   reappear only with a clearly different angle, and not within 14 days of their last post).
   Rotate categories through the day so each day gets a mix:
   - 7 a.m. run: an **"on this date"** moment if one exists (search e.g.
     `Oklahoma Sooners football "November 13"`), otherwise any `moments` topic
   - 10 a.m.: `legends` (award winners, All-Americans, Hall of Famers, iconic players or coaches)
   - 1 p.m.: `records` (program, NCAA or bowl records, streaks, firsts)
   - 4 p.m.: `after-football` (businesses founded, public office, coaching, broadcasting, medicine,
     philanthropy, other careers of former OU **players**; name their OU playing years)
   - 7 p.m.: any category, preferring something tied to this week's OU news
   Spread the eras: 1895-1945, Wilkinson, Switzer, Stoops, and recent seasons all count.
3. Research it with WebSearch/WebFetch. Open the pages you cite. Prefer soonersports.com,
   NCAA record books, sports-reference.com, heisman.com, footballfoundation.org, profootballhof.com,
   okhistory.org, congress.gov/bioguide, and established newspapers. Wikipedia can help find leads,
   but every post needs **at least 2 sources, at least one not Wikipedia**.
4. Write the post (format below). Original prose, warm fan voice, factual. No copied sentences,
   no quotes over 12 words, no emoji, no images, never imply the site is affiliated with OU.
5. **Fact-check before publishing.** Re-open each source and confirm every name, date, score,
   number, award, office and business claim. Fix or delete anything you cannot confirm. If the core
   answer can't be confirmed, drop the topic and pick another. Living people: only well-documented
   positive or neutral facts. No rumors, legal or health matters, money speculation, or betting content.
6. Set `publish_at` to **now** (current America/Chicago time, ISO 8601 with the correct offset:
   -06:00 in standard time, -05:00 in daylight time), so it goes live as soon as the site syncs.
7. **Refresh one existing post.** Pick the post with the oldest `updated_at` among those whose facts
   can change (records stated "through" a season, active or recently retired players, coaches,
   people's current careers, all-time series records). Check for newer information. If something
   changed, correct the post, keep its sources current, and set `"updated_at"` to now. If nothing
   changed, leave the file alone.
8. Run `python3 scripts/build_index.py`. Fix every error it reports and run it again until it says OK.
9. Commit only `posts/` and `index.json`: `git commit -m "OU history: <new slug> (+ refresh <slug>)"`,
   then `git push origin main`. If the push is rejected, `git pull --rebase` and push again.
10. Wake the site so it syncs right away (harmless GETs):
    `curl -s -o /dev/null https://oklahomasoonerfootball.com/history/` and
    `curl -s -o /dev/null https://oklahomasoonerfootball.com/`
11. Reply with the new post's title and URL (`https://oklahomasoonerfootball.com/history/<slug>`),
    what you refreshed (or "no changes found"), and any topic you dropped and why.

## Post format: `posts/<slug>.json`

```json
{
  "slug": "billy-sims-1978-heisman-trophy-oklahoma",
  "category": "legends",
  "title": "Billy Sims Wins the 1978 Heisman Trophy",
  "question": "Which Oklahoma running back won the 1978 Heisman Trophy?",
  "answer": "Billy Sims, a junior running back, won the 1978 Heisman Trophy ...",
  "summary": "140-160 character meta description written for searchers.",
  "body": ["3-5 short paragraphs, 180-320 words in total."],
  "people": ["Billy Sims"],
  "year": 1978,
  "sources": [
    {"title": "Billy Sims - Heisman.com", "url": "https://www.heisman.com/...", "supports": "1978 award, junior season"},
    {"title": "...", "url": "https://...", "supports": "..."}
  ],
  "publish_at": "2026-11-14T10:05:00-06:00"
}
```

- `slug`: lowercase words joined by hyphens, 4-9 words, player/topic/year keywords, must equal the file name.
- `category`: `legends`, `moments`, `records` or `after-football`.
- `title` up to 70 characters; `question` phrased the way a fan would search it; `answer` 1-2 sentences.
- Corrections later: edit the file, add `"updated_at"` (ISO time), rebuild the index, push.
