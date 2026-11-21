from sts2_trainer.Core.Models.offsets import CURRENT_BUILD, OFFSETS


def test_all_offsets_tagged_with_current_build():
    for name, off in OFFSETS.items():
        assert off.name == name
        assert off.build_id == CURRENT_BUILD
        assert off.module.endswith(".exe")


def test_offset_patterns_are_non_empty():
    for off in OFFSETS.values():
        assert len(off.pattern) >= 4
        assert off.extra >= 0