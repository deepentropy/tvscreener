class MalformedRequestException(Exception):
    def __init__(self, code, response_msg, url, payload):
        message = f"Error: {code}: {response_msg}\n"
        message += f"Request: {url}\n"
        message += "Payload:\n"
        message += payload
        super().__init__(message)


class ForexScreenerError(Exception):
    """Base exception for ForexOpportunityScreener."""

    pass


class InvalidPairError(ForexScreenerError):
    """Raised when forex pair symbol is invalid."""

    pass


class FilterConfigurationError(ForexScreenerError):
    """Raised when filter configuration is invalid."""

    pass


class RateLimitError(ForexScreenerError):
    """Raised when API rate limit is exceeded."""

    pass
