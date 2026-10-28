import axios, { AxiosInstance } from 'axios';

export interface KickChannelInfo {
  status: string;
  channel: string;
  is_live: boolean;
  viewers_count?: number;
  livestream?: any;
}

export interface KasadaTelemetry {
  status: string;
  target_url: string;
  headers: Record<string, string>;
  latency_ms: number;
}

export class KickStreamClient {
  private http: AxiosInstance;

  constructor(
    private apiKey: string,
    private host: string = 'kickstream-live-telemetry-kasada-chat-api.p.rapidapi.com',
    baseUrl?: string
  ) {
    this.http = axios.create({
      baseURL: baseUrl || `https://${this.host}/api/v1/kick`,
      timeout: 10000,
      headers: {
        'x-rapidapi-key': this.apiKey,
        'x-rapidapi-host': this.host,
        'Content-Type': 'application/json',
        'User-Agent': 'KickStream-TS-SDK/1.0.4'
      }
    });
  }

  public async getKasadaTelemetry(targetUrl: string = 'https://kick.com', forceRefresh: bool = false): Promise<KasadaTelemetry> {
    const res = await this.http.post<KasadaTelemetry>('/solve', { target_url: targetUrl, force_refresh: forceRefresh });
    return res.data;
  }

  public async getChannelInfo(channel: string): Promise<KickChannelInfo> {
    const res = await this.http.post<KickChannelInfo>('/channel-info', { channel });
    return res.data;
  }

  public async getChatHistory(channel: string, limit: number = 50): Promise<any> {
    const res = await this.http.post('/chat-history', { channel, limit });
    return res.data;
  }
}
