from __future__ import annotations

def terminate_main_process(*args, **kwargs) -> None:
    try:
        from app_process_lifecycle.shutdown import terminate_main_process as _t
        _t(*args, **kwargs)
    except Exception:
        import os, signal
        os.kill(os.getpid(), signal.SIGTERM)
