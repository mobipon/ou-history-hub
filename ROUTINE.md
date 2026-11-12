# Daily routine: 5 new OU football history & trivia posts

You run once a day (early morning US Central time). Your job: research, write, fact-check
and publish **5** new posts for the OU History & Trivia Hub on
https://oklahomasoonerfootball.com/history/ (an **unofficial** Oklahoma Sooners football fan site).
The site reads this repo's `index.json` and `posts/*.json` on its own; pushing to `main` is publishing.

## Steps

1. `git pull`. Read `index.json` to see every existing post (slug, question, people, year, category).
2. Pick 5 topics that are **not already covered** (no repeated question; a player may reappear
   only with a clearly different angle, and not within 14 days of their last post). Aim for this mix:
   - 1 **"on this date"** moment if one exists (search e.g. `Oklahoma Sooners football "November 13"`),
     otherwise any historic moment (category `moments`)
   - 1 `legends` (award winners, All-Americans, Hall of Famers, iconic players or coaches)
   - 1 `records` (program, NCAA or bowl records, streaks, firsts)
   - 1 `after-football` (businesses founded, public office, coaching, broadcasting, medicine,
     philanthropy, other careers of former OU **players**; name their OU playing years)
   - 1 of any category
   Spread the eras: 1895-1945, Wilkinson, Switzer, Stoops, and recent seasons all count.
3. Research each topic with WebSearch/WebFetch. Open the pages you cite. Prefer soonersports.com,
   NCAA record books, sports-reference.com, heisman.com, footballfoundation.org, profootballhof.com,
   okhistory.org, congress.gov/bioguide, and established newspapers. Wikipedia can help find leads,
   but every post needs **at least 2 sources, at least one not Wikipedia**.
4. Write the post (format below). Original prose, warm fan voice, factual. No copied sentences,
   no quotes over 12 words, no emoji, no images, never imply the site is affiliated with OU.
5. **Fact-check before publishing.** For every post, re-open each source and confirm every name,
   date, score, number, award, office and business claim. Fix or delete anything you cannot confirm.
   If the core answer can't be confirmed, drop the topic and pick another.
   Living people: only well-documented positive or neutral facts. No rumors, legal or health
   matters, money speculation, or betting content.
6. Set `publish_at` for the 5 posts to **today** at 08:00, 11:00, 14:00, 17:00 and 20:00
   America/Chicago, with the correct UTC offset for the date (-05:00 in daylight time, -06:00 in
   standard time). The site shows each post only once its time has passed.
7. Run `python3 scripts/build_index.py`. Fix every error it reports and run it again until it says OK.
8. Commit only `posts/` and `index.json`: `git commit -m "Add 5 OU history posts for YYYY-MM-DD"`,
   then `git push origin main`. If the push is rejected, `git pull --rebase` and push again.
9. Wake the site so it syncs right away (harmless GETs):
   `curl -s -o /dev/null https://oklahomasoonerfootball.com/history/` and
   `curl -s -o /dev/null https://oklahomasoonerfootball.com/`
10. Reply with the 5 titles and their publish times, plus any topic you dropped and why.

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
  "publish_at": "2026-11-14T08:00:00-06:00"
}
```

- `slug`: lowercase words joined by hyphens, 4-9 words, player/topic/year keywords, must equal the file name.
- `category`: `legends`, `moments`, `records` or `after-football`.
- `title` up to 70 characters; `question` phrased the way a fan would search it; `answer` 1-2 sentences.
- Corrections later: edit the file, add `"updated_at"` (ISO time), rebuild the index, push.
