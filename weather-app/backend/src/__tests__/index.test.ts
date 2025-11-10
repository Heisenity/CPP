import request from 'supertest';
import { app } from '../index'; // Import the app from your main file
import axios from 'axios';

jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe('GET /api/weather', () => {
  it('should return weather data for a valid city', async () => {
    mockedAxios.get.mockImplementation((url) => {
      if (url.includes('geo')) {
        return Promise.resolve({
          data: [{ lat: 51.5074, lon: -0.1278, name: 'London' }],
        });
      }
      if (url.includes('onecall')) {
        return Promise.resolve({
          data: {
            current: { temp: 15, feels_like: 14, weather: [{ main: 'Clouds', icon: '04d' }], dt: 1620000000 },
            hourly: [],
            daily: [],
          },
        });
      }
      if (url.includes('air_pollution')) {
        return Promise.resolve({
          data: { list: [{ main: { aqi: 2 }, components: { pm25: 5, o3: 30 } }] },
        });
      }
      return Promise.reject(new Error('not found'));
    });

    const res = await request(app).get('/api/weather?city=London');
    expect(res.statusCode).toEqual(200);
    expect(res.body.current.place_name).toEqual('London');
  });

  it('should return 404 for an invalid city', async () => {
    mockedAxios.get.mockResolvedValue({ data: [] });
    const res = await request(app).get('/api/weather?city=InvalidCity');
    expect(res.statusCode).toEqual(404);
  });
});
