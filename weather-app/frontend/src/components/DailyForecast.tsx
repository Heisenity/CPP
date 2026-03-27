interface DailyForecastProps {
  data: {
    day: string;
    min_temp: number;
    max_temp: number;
    summary: string;
    sunrise: string;
    sunset: string;
  }[];
}

const DailyForecast = ({ data }: DailyForecastProps) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-4">Daily Forecast</h2>
      <div>
        {data.map((day, index) => (
          <div key={index} className="flex justify-between items-center py-2 border-b border-gray-200 dark:border-gray-700">
            <p className="font-semibold">{day.day}</p>
            <p className="text-gray-600 dark:text-gray-400">{day.summary}</p>
            <p className="font-semibold">{day.max_temp}° / {day.min_temp}°</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default DailyForecast;
