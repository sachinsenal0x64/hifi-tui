from threading import Thread
from textual.app import App, ComposeResult
from textual.containers import Center, Middle
from textual.timer import Timer
from textual.widgets import Footer, ProgressBar
import locale
import mpv

locale.setlocale(locale.LC_NUMERIC, "C")

player = mpv.MPV(
    input_default_bindings=True,
    input_vo_keyboard=True,
    terminal=True,
    input_terminal=True,
    really_quiet=True,
)


class IndeterminateProgressBar(App[None]):
    progress_timer: Timer
    """Timer to simulate progress happening."""
    is_paused: bool = False

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                yield ProgressBar()

    def on_mount(self) -> None:
        """Set up a timer to simulate progress happening."""
        self.progress_timer = self.set_interval(
            1 / 60, self.update_progress, pause=True
        )

        player.play(
            "https://rr3---sn-npoe7nz7.googlevideo.com/videoplayback?expire=1699822618&ei=uudQZZLpI4rSjMwPxdyf0Ag&ip=168.138.165.25&id=o-ADGfCO95m-AVR2pu8baB02S7dXGu9ojDNtoBBtd2-ZGE&itag=251&source=youtube&requiressl=yes&mh=z-&mm=31%2C26&mn=sn-npoe7nz7%2Csn-oguelnsy&ms=au%2Conr&mv=m&mvi=3&pl=26&initcwndbps=2101250&spc=UWF9fxXh4i6MvzRZCWBsR1x1bAMMQYE&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=4437319&dur=279.701&lmt=1696617536736693&mt=1699800546&fvip=3&keepalive=yes&fexp=24007246&beids=24350018&c=ANDROID&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=ANLwegAwRQIgU8AZonXELjktkqRnxAsmQ-extMpZ4FpDfctequ62jwECIQCWEAfgHnCaaq2o2-d98MzQTRszfRhywd6qbOcp6AFQWw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AM8Gb2swRAIgSrK5HJcXi9i9UasprO0RdrrNm2V1Uk_0yTtoHvO0rq4CICUo1syDpzrhYT5qQMycknK96h8VEhWD8jifob8cgRGi"
        )
        self.progress_timer.resume()

    def update_progress(self) -> None:
        """Update the progress bar based on the song's position."""
        if not self.is_paused:
            position = player.time_pos
            duration = player.duration
            if position is not None and duration is not None:
                self.query_one(ProgressBar).update(
                    progress=position + 1, total=duration
                )

    def on_stop(self) -> None:
        """Stop the progress timer when the application is stopped."""
        self.progress_timer.cancel()

    def action_increase_progress(self) -> None:
        """Increase the progress bar."""
        self.query_one(ProgressBar).advance(1)

    def action_decrease_progress(self) -> None:
        """Decrease the progress bar."""
        self.query_one(ProgressBar).advance(-1)

    def action_pause_progress(self) -> None:
        """Pause the progress bar and the song."""
        self.is_paused = True
        player.pause()

    def action_resume_progress(self) -> None:
        """Resume the progress bar and the song."""
        self.is_paused = False
        player.resume()


if __name__ == "__main__":
    IndeterminateProgressBar().run()
