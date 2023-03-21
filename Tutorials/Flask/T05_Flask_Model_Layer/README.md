# Flaskr Carved Rock

Setting up the application for the start of the course. All users have the password `root`

```
git checkout start
pipenv install --dev
flask init-db
python demo_data.py
```

Different points in the code development are tagged with module and clip numbers. The 60-90s (free) trailer for the course is considered module 1 (m1), so the teaching and demos actually start at m2. Clip numbers are incremented with both non-demo and demo clips. All this means code changes from the first demo are completed at the tag `m2-clip2`, because the demo is the second clip in the second module.