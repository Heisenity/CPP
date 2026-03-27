import { useState } from 'react';
import CurrentWeather from './components/CurrentWeather';
import HourlyForecast from './components/HourlyForecast';
import DailyForecast from './components/DailyForecast';
import AQI from './components/AQI';

interface WeatherData {
  current: any;
  hourly: any[];
  daily: any[];
  aqi: any;
  alerts: any[];
}

function App() {
  const [city, setCity] = useState('');
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setWeatherData(null);

    try {
      const response = await fetch(`/api/weather?city=${city}`);
      if (!response.ok) {
        throw new Error('City not found');
      }
      const data = await response.json();
      setWeatherData(data);
    } catch (err) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100 flex flex-col items-center p-4">
      <header className="w-full max-w-4xl mx-auto mb-8">
        <h1 className="text-4xl font-bold text-center">Weather App</h1>
      </header>
      <main className="w-full max-w-4xl mx-auto">
        <form onSubmit={handleSearch} className="flex justify-center mb-8">
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            placeholder="Enter city, e.g., Mumbai or City, Country"
            className="w-full max-w-md px-4 py-2 text-gray-900 bg-white border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            className="px-4 py-2 text-white bg-blue-500 rounded-r-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            Search
          </button>
        </form>

        {loading && <p className="text-center">Fetching weather...</p>}
        {error && <p className="text-center text-red-500">{error}</p>}

        {weatherData && (
          <div>
            <CurrentWeather data={weatherData.current} />
            <HourlyForecast data={weatherData.hourly} />
            <DailyForecast data={weatherData.daily} />
            <AQI data={weatherData.aqi} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
