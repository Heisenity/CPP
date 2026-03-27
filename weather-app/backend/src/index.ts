import express, { Request, Response } from 'express';
import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

export const app = express();
const port = process.env.PORT || 3000;
const apiKey = process.env.OPENWEATHERMAP_API_KEY;

app.get('/health', (req: Request, res: Response) => {
  res.status(200).json({ status: 'ok' });
});

app.get('/api/weather', async (req: Request, res: Response) => {
  const { city } = req.query;

  if (!city) {
    return res.status(400).json({ error: 'City is required' });
  }

  if (!apiKey) {
    return res.status(500).json({ error: 'API key is missing' });
  }

  try {
    // Step 1: Geocoding to get lat and lon
    const geoUrl = `http://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=1&appid=${apiKey}`;
    const geoResponse = await axios.get(geoUrl);

    if (geoResponse.data.length === 0) {
      return res.status(404).json({ error: 'City not found' });
    }

    const { lat, lon } = geoResponse.data[0];

    // Step 2: Get weather data using One Call API
    const weatherUrl = `https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude=minutely,alerts&units=metric&appid=${apiKey}`;
    const weatherResponse = await axios.get(weatherUrl);
    const weather = weatherResponse.data;

    // Step 3: Get Air Quality data
    const airUrl = `http://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${apiKey}`;
    const airResponse = await axios.get(airUrl);
    const airQuality = airResponse.data.list[0];

    // Step 4: Normalize the data to match the frontend's expectations
    const normalizedData = {
      current: {
        temp: Math.round(weather.current.temp),
        feels_like: Math.round(weather.current.feels_like),
        condition: weather.current.weather[0].main,
        icon: weather.current.weather[0].icon,
        local_time: new Date(weather.current.dt * 1000).toLocaleTimeString(),
        place_name: geoResponse.data[0].name,
      },
      hourly: weather.hourly.slice(0, 24).map((h: any) => ({
        time: new Date(h.dt * 1000).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        icon: h.weather[0].icon,
        temp: Math.round(h.temp),
        rain_chance: Math.round(h.pop * 100),
      })),
      daily: weather.daily.slice(0, 7).map((d: any) => ({
        day: new Date(d.dt * 1000).toLocaleDateString([], { weekday: 'long' }),
        min_temp: Math.round(d.temp.min),
        max_temp: Math.round(d.temp.max),
        summary: d.weather[0].main,
        sunrise: new Date(d.sunrise * 1000).toLocaleTimeString(),
        sunset: new Date(d.sunset * 1000).toLocaleTimeString(),
      })),
      aqi: {
        value: airQuality.main.aqi,
        pollutants: airQuality.components,
        guidance: `AQI ${airQuality.main.aqi} - Air quality is acceptable.`, // Simplified guidance
      },
      alerts: [], // Alerts not included in this API version
    };

    res.status(200).json(normalizedData);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to fetch weather data' });
  }
});

if (require.main === module) {
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
}
