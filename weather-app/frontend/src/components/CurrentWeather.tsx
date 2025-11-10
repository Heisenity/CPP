interface CurrentWeatherProps {
  data: {
    temp: number;
    feels_like: number;
    condition: string;
    icon: string;
    local_time: string;
    place_name: string;
  };
}

const CurrentWeather = ({ data }: CurrentWeatherProps) => {
  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md mb-8">
      <h2 className="text-2xl font-bold mb-2">{data.place_name}</h2>
      <p className="text-gray-600 dark:text-gray-400 mb-4">{data.local_time}</p>
      <div className="flex items-center">
        <img src={`http://openweathermap.org/img/wn/${data.icon}@2x.png`} alt={data.condition} className="w-16 h-16 mr-4" />
        <div>
          <p className="text-5xl font-bold">{data.temp}°</p>
          <p className="text-gray-600 dark:text-gray-400">Feels like {data.feels_like}°</p>
        </div>
      </div>
      <p className="text-xl mt-4">{data.condition}</p>
    </div>
  );
};

export default CurrentWeather;
