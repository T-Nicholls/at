"""Custom error and warning classes for subclassing exceptions specific to AT."""

__all__ = ["ATError", "ATWarning"]


class ATError(Exception):
    """The base Error class for all errors within AT."""

    pass


class ATWarning(UserWarning):
    """The base Warning class for all errors within AT."""

    pass
