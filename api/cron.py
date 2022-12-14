import os
# Cron Job
from django_cron import CronJobBase, Schedule

# Google API
from apiclient.discovery import build
import apiclient

from .models import *
from youtube_fetch_api import settings
from datetime import datetime, timedelta


class CallYoutubeApi(CronJobBase):
    RUN_EVERY_MINS = 15  # the cron job will run after every 15 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.call_youtube_api'    # a unique code

    def do(self):
        apiKeys = settings.GOOGLE_API_KEYS
        time_now = datetime.now()
        last_request_time = time_now - timedelta(minutes=15)

        # to check the availability of a valid api key
        valid = False

        for apiKey in apiKeys:
            try:
                youtube = build("youtube", "v3", developerKey=apiKey)
                req = youtube.search().list(q="football", part="snippet", order="date", maxResults=50,
                                            publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z'))
                res = req.execute()
                valid = True
            except apiclient.errors.HttpError as err:
                code = err.resp.status
                if not(code == 400 or code == 403):
                    break

            if valid:
                break
        


        if valid:

            # if the used key is valid, then api get some data, now we have to store that data to db

            for item in res['items']:
                video_id = item['id']['videoId']
                publishedDateTime = item['snippet']['publishedAt']
                title = item['snippet']['title']
                description = item['snippet']['description']
                thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
                channel_id = item['snippet']['channelId']
                channel_title = item['snippet']['channelTitle']
                print(title)
                Videos.objects.create(
                    video_id=video_id,
                    title=title,
                    description=description,
                    channel_id=channel_id,
                    channel_title=channel_title,
                    publishedDateTime=publishedDateTime,
                    thumbnailsUrls=thumbnailsUrls,
                )
