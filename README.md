# OU History & Trivia Hub content

Posts for the History & Trivia Hub on [OklahomaSoonerFootball.com](https://oklahomasoonerfootball.com/history/),
an unofficial Oklahoma Sooners football fan site.

- `posts/<slug>.json`: one post each (see `ROUTINE.md` for the format).
- `index.json`: built by `scripts/build_index.py` (and by the GitHub Action on push). The site syncs
  from this file about every 10 minutes and shows a post once its `publish_at` time has passed.
- A daily cloud routine follows `ROUTINE.md` to add 5 researched, fact-checked posts.

Not affiliated with the University of Oklahoma or OU Athletics.
