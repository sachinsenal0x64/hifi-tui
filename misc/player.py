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
             ""        
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
