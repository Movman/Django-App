#!/bin/bash
./manage.py dumpdata --indent 2 wagtailcore.locale > pages/fixtures/wagtailcore.locale.json
./manage.py dumpdata --indent 2 wagtailcore.page > pages/fixtures/wagtailcore.page.json
./manage.py dumpdata --indent 2 wagtailcore.collection > pages/fixtures/wagtailcore.collection.json
./manage.py dumpdata --indent 2 wagtailimages.image > pages/fixtures/wagtailimages.image.json
./manage.py dumpdata --indent 2 pages.blogpage > pages/fixtures/pages.blogpage.json