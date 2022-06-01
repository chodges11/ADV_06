from dataclasses import dataclass


@dataclass
class Timer:
    # The rest of the code is unchanged

    def __enter__(self):
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exc_info):
        """Stop the context manager timer"""
        self.stop()