import httpx
from typing import Optional, Dict, Any

class KickStreamClient:
    """
    Synchronous KickStream Client for Kasada Telemetry & Live Data.
    Powered by Aether Protocol Labs on RapidAPI.
    """
    def __init__(
        self,
        api_key: str,
        host: str = "kickstream-live-telemetry-kasada-chat-api.p.rapidapi.com",
        base_url: Optional[str] = None
    ):
        self.api_key = api_key
        self.host = host
        self.base_url = base_url or f"https://{self.host}/api/v1/kick"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.host,
            "Content-Type": "application/json",
            "User-Agent": "KickStream-Python-SDK/1.0.4"
        }

    def get_kasada_telemetry(self, target_url: str = "https://kick.com", force_refresh: bool = False) -> Dict[str, Any]:
        """Fetch pre-warmed Kasada kpsdk telemetry tokens (latency < 30ms)."""
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{self.base_url}/solve",
                headers=self.headers,
                json={"target_url": target_url, "force_refresh": force_refresh}
            )
            resp.raise_for_status()
            return resp.json()

    def get_channel_info(self, channel: str) -> Dict[str, Any]:
        """Get live status, stream metadata, viewer counts, and playback URLs."""
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{self.base_url}/channel-info",
                headers=self.headers,
                json={"channel": channel}
            )
            resp.raise_for_status()
            return resp.json()

    def get_chat_history(self, channel: str, limit: int = 50) -> Dict[str, Any]:
        """Fetch recent chat messages and pinned badges."""
        with httpx.Client(timeout=10.0) as client:
            resp = client.post(
                f"{self.base_url}/chat-history",
                headers=self.headers,
                json={"channel": channel, "limit": limit}
            )
            resp.raise_for_status()
            return resp.json()

class AsyncKickStreamClient:
    """Async Client for high-throughput stream crawlers and Discord/Telegram bots."""
    def __init__(
        self,
        api_key: str,
        host: str = "kickstream-live-telemetry-kasada-chat-api.p.rapidapi.com",
        base_url: Optional[str] = None
    ):
        self.api_key = api_key
        self.host = host
        self.base_url = base_url or f"https://{self.host}/api/v1/kick"
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.host,
            "Content-Type": "application/json",
            "User-Agent": "KickStream-Async-SDK/1.0.4"
        }

    async def get_kasada_telemetry(self, target_url: str = "https://kick.com", force_refresh: bool = False) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(
                f"{self.base_url}/solve",
                headers=self.headers,
                json={"target_url": target_url, "force_refresh": force_refresh}
            )
            resp.raise_for_status()
            return resp.json()

    async def get_channel_info(self, channel: str) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(
                f"{self.base_url}/channel-info",
                headers=self.headers,
                json={"channel": channel}
            )
            resp.raise_for_status()
            return resp.json()
