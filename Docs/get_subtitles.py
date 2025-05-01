from youtube_transcript_api import YouTubeTranscriptApi


def get_subtitles(video_url, language='ja'):
    try:
        # 動画IDを抽出
        video_id = video_url.split('v=')[1]
        
        # 指定した言語の字幕を取得
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
        
        # 字幕を整形して返す
        return '\n'.join([f"[{entry['start']:.2f}s] {entry['text']}" for entry in transcript])
    except Exception as e:
        return f"字幕の取得中にエラーが発生しました: {e}"


if __name__ == "__main__":
    video_url = input("字幕を取得したいYouTube動画のURLを入力してください: ")
    language = input("取得したい字幕の言語コードを入力してください（例: ja, en）: ")
    subtitles = get_subtitles(video_url, language)
    print(subtitles)