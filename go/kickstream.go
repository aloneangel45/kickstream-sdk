package kickstream

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

type Client struct {
	APIKey     string
	Host       string
	BaseURL    string
	HTTPClient *http.Client
}

func NewClient(apiKey string) *Client {
	host := "kickstream-live-telemetry-kasada-chat-api.p.rapidapi.com"
	return &Client{
		APIKey:  apiKey,
		Host:    host,
		BaseURL: fmt.Sprintf("https://%s/api/v1/kick", host),
		HTTPClient: &http.Client{
			Timeout: 10 * time.Second,
		},
	}
}

type ChannelInfoResponse struct {
	Status    string `json:"status"`
	Channel   string `json:"channel"`
	IsLive    bool   `json:"is_live"`
	Followers int    `json:"followers_count"`
}

func (c *Client) GetChannelInfo(channel string) (*ChannelInfoResponse, error) {
	payload := map[string]string{"channel": channel}
	b, _ := json.Marshal(payload)

	req, err := http.NewRequest("POST", c.BaseURL+"/channel-info", bytes.NewBuffer(b))
	if err != nil {
		return nil, err
	}

	req.Header.Set("x-rapidapi-key", c.APIKey)
	req.Header.Set("x-rapidapi-host", c.Host)
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.HTTPClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var result ChannelInfoResponse
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, err
	}
	return &result, nil
}
