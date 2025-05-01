from django.shortcuts import render
from django.http import HttpResponse
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def home(request):
    context = {}
    if request.method == 'POST':
        url = request.POST.get('url', '')
        try:
            # YouTube URLからビデオIDを抽出
            parsed_url = urlparse(url)
            if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
                video_id = parse_qs(parsed_url.query).get('v', [None])[0]
                if video_id:
                    # 字幕を取得
                    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja'])
                    context['subtitles'] = transcript
                    context['video_url'] = url
                else:
                    context['error'] = '無効なYouTube URLです。'
            else:
                context['error'] = 'YouTube URLを入力してください。'
        except Exception as e:
            context['error'] = '字幕の取得に失敗しました。'
    
    return render(request, 'home.html', context)

def helloworld(request):
    return HttpResponse("<h1>Hello, World!</h1>")
