using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace KickStream
{
    public class KickClient
    {
        private readonly HttpClient _httpClient;
        private readonly string _host;

        public KickClient(string apiKey, string host = "kickstream-live-telemetry-kasada-chat-api.p.rapidapi.com")
        {
            _host = host;
            _httpClient = new HttpClient
            {
                BaseAddress = new Uri($"https://{_host}/api/v1/kick/")
            };
            _httpClient.DefaultRequestHeaders.Add("x-rapidapi-key", apiKey);
            _httpClient.DefaultRequestHeaders.Add("x-rapidapi-host", _host);
        }

        public async Task<string> GetChannelInfoAsync(string channel)
        {
            var content = new StringContent(
                JsonSerializer.Serialize(new { channel }),
                Encoding.UTF8,
                "application/json"
            );
            var response = await _httpClient.PostAsync("channel-info", content);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }
    }
}
