import requests

urls = [
    "../static/css/anime.min.css",
    "../static/css/episode.min.css",
    "../static/css/home.min.css",
    "../static/css/search.min.css",
    "../static/css/video.min.css",
    "../static/js/home.min.js",
    "../static/js/player.min.js",
]


for url in urls:
    url = url[24:]
    r = requests.get("https://purge.jsdelivr.net" + url)
    print(r.json().get("status"), url)
