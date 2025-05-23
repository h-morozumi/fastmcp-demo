import sys
import asyncio
import warnings

if sys.platform.startswith("win"):
    # --- Windows のときだけ subprocess-transport の __del__ を安全化 ---
    import asyncio.base_subprocess
    from asyncio.proactor_events import _ProactorBasePipeTransport

    # 元の __del__ を保持
    _orig_bp_del = asyncio.base_subprocess.BaseSubprocessTransport.__del__
    _orig_pp_del = _ProactorBasePipeTransport.__del__

    def _safe_bp_del(self):
        try:
            _orig_bp_del(self)
        except RuntimeError as e:
            # イベントループクローズ由来の例外だけを握り潰す
            if "Event loop is closed" not in str(e):
                raise

    def _safe_pp_del(self):
        try:
            _orig_pp_del(self)
        except Exception:
            # その他の細かい例外もすべて握り潰し
            pass

    # 差し替え
    asyncio.base_subprocess.BaseSubprocessTransport.__del__ = _safe_bp_del
    _ProactorBasePipeTransport.__del__ = _safe_pp_del

    # ResourceWarning だけは無効化しておく
    warnings.filterwarnings("ignore", category=ResourceWarning)
else:
    # Linux や macOS では何もしない
    pass

# --- HotPatch ---