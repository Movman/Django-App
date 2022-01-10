#!/bin/bash
./manage.py loaddata pages/fixtures/wagtailcore.locale.json
./manage.py loaddata pages/fixtures/wagtailcore.page.json
./manage.py loaddata pages/fixtures/wagtailcore.collection.json
./manage.py loaddata pages/fixtures/wagtailimages.image.json
./manage.py loaddata pages/fixtures/pages.blogpage.json