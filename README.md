# NBA Prop Research Lab

Free static research dashboard. It automatically retrieves an NBA game schedule via ESPN's publicly accessible scoreboard endpoint using GitHub Actions. It does **not** currently retrieve live PrizePicks lines, injury feeds, or player trends. It does **not** fabricate projections or picks.

## iPhone setup

1. Upload the contents of this ZIP into the root of your GitHub repository. Keep the `.github/workflows/update.yml` file and folder structure intact.
2. GitHub Settings > Pages > Deploy from a branch > main > /(root) > Save.
3. Actions > Refresh NBA schedule > Run workflow. GitHub may require Actions workflow permissions for commits.
4. Visit https://minamekhaeil.github.io/PrizePicks-ai/ once deployed.

GitHub Pages is public. Never commit API keys or personal secrets. ESPN's endpoint is unofficial for this use and may change. No sportsbook's private API should be scraped without authorization. To build a real automatic prop analyzer, obtain a permitted live line feed and a player-stat/injury source, then validate predictions on historical data.
