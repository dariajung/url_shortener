# -*- coding: utf-8 -*-

from flask import (Flask, Response, request, render_template, redirect, url_for)
from shorten import SimpleUrlShortener
import redis

from urlparse import urlparse

app = Flask(__name__)

app.debug = True

urlShortener = SimpleUrlShortener()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def return_shortened():
    url_to_parse = request.form.get('url_to_parse')

    parsed = urlShortener.shorten(url_to_parse)

    return parsed['shorturl']

@app.route('/<path:slug>')
def fallback(slug):
    try:
        print slug
        original_url = urlShortener.redis.get(slug)

        print original_url

    except:
        return None

    if (original_url):
        return redirect(original_url, 301)

    else:
        return "No URL for that exists :("


if __name__ == '__main__':
    app.run()