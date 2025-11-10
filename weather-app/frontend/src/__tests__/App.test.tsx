import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from '../App';

// Mock the fetch function
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () =>
      Promise.resolve({
        current: { place_name: 'London', temp: 15 },
        hourly: [],
        daily: [],
        aqi: { value: 50, pollutants: { pm25: 10, o3: 20 }, guidance: 'Good' },
      }),
  })
) as jest.Mock;

describe('App', () => {
  it('searches for a city and displays the weather', async () => {
    render(<App />);

    // Find the input and search button
    const searchInput = screen.getByPlaceholderText(/Enter city/i);
    const searchButton = screen.getByRole('button', { name: /Search/i });

    // Simulate user input
    fireEvent.change(searchInput, { target: { value: 'London' } });
    fireEvent.click(searchButton);

    // Wait for the weather data to be displayed
    await waitFor(() => {
      expect(screen.getByText('London')).toBeInTheDocument();
    });

    // Check that the current temperature is displayed
    expect(screen.getByText(/15/)).toBeInTheDocument();
  });
});
