from dataclasses import dataclass


@dataclass
class HttpRequest:
    method: str
    url: str
    headers: dict[str, str]
    params: dict[str, str]
    body: str | None
    timeout: int

    def __repr__(self) -> str:
        parts = [f"{self.method} {self.url}"]
        if self.params:
            query = "&".join(f"{k}={v}" for k, v in self.params.items())
            parts[0] += f"?{query}"
        for key, value in self.headers.items():
            parts.append(f"{key}: {value}")
        if self.body:
            parts.append(f"\n{self.body}")
        return "\n".join(parts)


class HttpRequestBuilder:
    def __init__(self, method: str, url: str) -> None:
        self._method = method.upper()
        self._url = url
        self._headers: dict[str, str] = {}
        self._params: dict[str, str] = {}
        self._body: str | None = None
        self._timeout: int = 30

    def header(self, key: str, value: str) -> "HttpRequestBuilder":
        self._headers[key] = value
        return self

    def param(self, key: str, value: str) -> "HttpRequestBuilder":
        self._params[key] = value
        return self

    def body(self, content: str) -> "HttpRequestBuilder":
        self._body = content
        return self

    def timeout(self, seconds: int) -> "HttpRequestBuilder":
        self._timeout = seconds
        return self

    def build(self) -> HttpRequest:
        if not self._url:
            raise ValueError("URL is required")
        if self._method in ("GET", "DELETE") and self._body:
            raise ValueError(f"{self._method} requests should not have a body")
        return HttpRequest(
            method=self._method,
            url=self._url,
            headers=self._headers,
            params=self._params,
            body=self._body,
            timeout=self._timeout,
        )


def main() -> None:
    get_request = (
        HttpRequestBuilder("GET", "https://api.example.com/users")
        .header("Accept", "application/json")
        .header("Authorization", "Bearer token123")
        .param("page", "1")
        .param("limit", "25")
        .timeout(10)
        .build()
    )
    print(get_request)
    # GET https://api.example.com/users?page=1&limit=25
    # Accept: application/json
    # Authorization: Bearer token123

    print()

    post_request = (
        HttpRequestBuilder("POST", "https://api.example.com/users")
        .header("Content-Type", "application/json")
        .header("Authorization", "Bearer token123")
        .body('{"name": "Alice", "email": "alice@example.com"}')
        .timeout(30)
        .build()
    )
    print(post_request)
    # POST https://api.example.com/users
    # Content-Type: application/json
    # Authorization: Bearer token123
    #
    # {"name": "Alice", "email": "alice@example.com"}


if __name__ == "__main__":
    main()
