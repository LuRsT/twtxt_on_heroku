# ToH: a write-only twtxt client on Heroku

This repo is a write-only client for [twtxt](https://github.com/buckket/twtxt).

## How to use

Fork this repo, create a heroku app, deploy it and just add the following configs:

- GSHEET_URL (The URL to a CSV with rows like this: `25/08/2019 20:07:20,Another test`)
- TWTXT_USERNAME (Your username in twtxt)
- TWTXT_URL (The URL to your heroku app (this same app URL))

Example of this running here: https://twtxt.herokuapp.com/, follow me @gil (twtxt)
