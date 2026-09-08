import importlib.util
from pathlib import Path


def load_module():
    module_path = Path(__file__).parents[1] / "video_build.py"
    spec = importlib.util.spec_from_file_location("video_build", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_video_plan_has_two_outputs_for_each_source():
    m = load_module()
    plan = m.video_plan()
    assert set(plan) == {"intro", "sample", "six_steps", "map", "report"}
    for item in plan.values():
        assert item["nomusic"].endswith("_NOMUSIC.mp4")
        assert item["music"].endswith("_MUSIC.mp4")


def test_music_mapping_matches_approved_tracks():
    m = load_module()
    plan = m.video_plan()
    assert plan["intro"]["bgm"].endswith("mixkit-summers-here-91.mp3")
    assert plan["sample"]["bgm"].endswith("mixkit-feeling-happy-5.mp3")
    assert plan["six_steps"]["bgm"].endswith("mixkit-dance-with-me-3.mp3")
    assert plan["map"]["bgm"].endswith("mixkit-i-love-you-mommy-831.mp3")
    assert plan["report"]["bgm"] is None


def test_duck_filter_keeps_original_audio_foreground():
    m = load_module()
    f = m.duck_filter()
    assert "sidechaincompress" in f
    assert "amix" in f
    assert "normalize=0" in f


def test_capture_plan_records_live_pages_without_visual_transform():
    m = load_module()
    plan = m.capture_plan()
    assert plan["viewport"] == (1280, 720)
    assert plan["intro"]["url"] == "https://hsam05.com/auto-show1"
    assert plan["sample"]["url"] == "https://hsam05.com/sample-test"
    assert plan["six_steps"]["url"] == "https://hsam05.com/learning"
    assert plan["preserve_live_page"] is True
    assert plan["no_crop"] is True
    assert plan["no_scale"] is True
