"""Retry Pattern.

The retry pattern is a design pattern that allows you to automatically retry a failed operation a
certain number of times before giving up. This can be useful for handling transient errors, such as
network issues or temporary unavailability of a service.
"""

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential


def log_before_sleep(retry_state):
    """Log retry attempt information.

    Args:
        retry_state: Contains retry metadata with attributes:
            - attempt_number: Current attempt number (int)
            - outcome: Result/exception from the attempt
            - outcome_timestamp: When the attempt occurred
            - idle_for: Time already waited (float)
            - next_action: NextAction object with sleep duration
            - next_action.sleep: Seconds to wait before next try (float)
    """
    print(
        f"Attempt {retry_state.attempt_number} failed. Waiting {retry_state.next_action.sleep}s before next try..."
    )


@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    before_sleep=log_before_sleep,
)
def fetch_joke() -> str:
    """Fetch a random Chuck Norris joke from the API."""

    with httpx.Client() as client:
        response = client.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()
        data: dict[str, str] = response.json()
        return data["value"]


def main() -> None:
    print(fetch_joke())


if __name__ == "__main__":
    main()
