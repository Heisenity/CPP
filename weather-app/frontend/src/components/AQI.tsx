interface AQIProps {
  data: {
    value: number;
    pollutants: {
      pm25: number;
      o3: number;
    };
    guidance: string;
  };
}

const AQI = ({ data }: AQIProps) => {
  const getAQIColor = (value: number) => {
    if (value <= 50) return 'text-green-500';
    if (value <= 100) return 'text-yellow-500';
    if (value <= 150) return 'text-orange-500';
    if (value <= 200) return 'text-red-500';
    if (value <= 300) return 'text-purple-500';
    return 'text-red-700';
  };

  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-md mb-8">
      <h2 className="text-2xl font-bold mb-4">Air Quality</h2>
      <div className="flex items-center">
        <p className={`text-5xl font-bold ${getAQIColor(data.value)}`}>{data.value}</p>
        <div className="ml-4">
          <p className="font-semibold">Pollutants:</p>
          <p>PM2.5: {data.pollutants.pm25}</p>
          <p>O3: {data.pollutants.o3}</p>
        </div>
      </div>
      <p className="mt-4">{data.guidance}</p>
    </div>
  );
};

export default AQI;
