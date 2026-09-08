from pathlib import Path


def video_plan():
    out = Path("outputs")
    return {
        "intro": {
            "source": "https://hsam05.com/auto-show1",
            "nomusic": str(out / "WORDMATE_INTRO_NOMUSIC.mp4"),
            "music": str(out / "WORDMATE_INTRO_MUSIC.mp4"),
            "bgm": "music/mixkit-summers-here-91.mp3",
        },
        "sample": {
            "source": "https://hsam05.com/sample-test",
            "nomusic": str(out / "WORDMATE_SAMPLE_NOMUSIC.mp4"),
            "music": str(out / "WORDMATE_SAMPLE_MUSIC.mp4"),
            "bgm": "music/mixkit-feeling-happy-5.mp3",
        },
        "six_steps": {
            "source": "https://hsam05.com/learning",
            "nomusic": str(out / "WORDMATE_6STEPS_NOMUSIC.mp4"),
            "music": str(out / "WORDMATE_6STEPS_MUSIC.mp4"),
            "bgm": "music/mixkit-dance-with-me-3.mp3",
        },
        "map": {
            "source": "videos/map-video.mp4",
            "nomusic": str(out / "WORDMATE_MAP_NOMUSIC.mp4"),
            "music": str(out / "WORDMATE_MAP_MUSIC.mp4"),
            "bgm": "music/mixkit-i-love-you-mommy-831.mp3",
        },
        "report": {
            "source": "videos/report-nomusic.mp4",
            "nomusic": str(out / "WORDMATE_REPORT_NOMUSIC.mp4"),
            "music": str(out / "WORDMATE_REPORT_MUSIC.mp4"),
            "bgm": None,
            "music_source": "videos/report-video.mp4",
        },
    }


def duck_filter():
    # Sidechain ducking: preserve spoken/word audio; lower BGM when original audio is present.
    # Then mix original audio with ducked music without normalization pumping.
    return (
        "[1:a]volume=0.20[bgm];"
        "[bgm][0:a]sidechaincompress=threshold=0.025:ratio=8:attack=15:release=350[ducked];"
        "[0:a][ducked]amix=inputs=2:duration=first:normalize=0[aout]"
    )
