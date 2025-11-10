interface HourlyForecastProps {
  data: {
    time: string;
    icon: string;
    temp: number;
    rain_chance: number;
  }[];
}

const HourlyForecast = ({ data }: HourlyForecastProps) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md mb-8">
      <h2 className="text-2xl font-bold mb-4">Hourly Forecast</h2>
      <div className="flex overflow-x-auto space-x-4">
        {data.map((hour, index) => (
          <div key={index} className="flex-shrink-0 w-24 text-center">
            <p className="font-semibold">{hour.time}</p>
            <img src={`http://openweathermap.org/img/wn/${hour.icon}.png`} alt="" className="w-12 h-12 mx-auto" />
            <p className="text-xl font-bold">{hour.temp}°</p>
            <p className="text-sm text-gray-600 dark:text-gray-400">{hour.rain_chance}% rain</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default HourlyForecast;
