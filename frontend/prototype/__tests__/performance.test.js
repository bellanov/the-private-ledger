import { render, screen } from '@testing-library/svelte';
import Performance from '../views/performance.html';

describe('Performance Component', () => {
  it('renders the performance section heading', () => {
    render(Performance);
    expect(screen.getByText('Performance')).toBeInTheDocument();
  });

  it('displays the date field with default value', () => {
    render(Performance);
    expect(screen.getByDisplayValue('2024-06-01')).toBeInTheDocument();
  });

  it('displays the record field with default value', () => {
    render(Performance);
    expect(screen.getByDisplayValue('Positive')).toBeInTheDocument();
  });

  it('displays return on investment percentage', () => {
    render(Performance);
    expect(screen.getByText('20%')).toBeInTheDocument();
  });

  it('displays return on investment dollar amount', () => {
    render(Performance);
    expect(screen.getByText('$200.00')).toBeInTheDocument();
  });

  it('displays shares field with default value', () => {
    render(Performance);
    expect(screen.getByText('100')).toBeInTheDocument();
  });

  it('displays share price with currency formatting', () => {
    render(Performance);
    expect(screen.getByText('$12.00')).toBeInTheDocument();
  });

  it('displays total bankroll with currency formatting', () => {
    render(Performance);
    expect(screen.getByText('$1,200.00')).toBeInTheDocument();
  });

  it('displays units won field', () => {
    render(Performance);
    expect(screen.getByText('10')).toBeInTheDocument();
  });

  it('displays unit price with currency formatting', () => {
    render(Performance);
    expect(screen.getByText('$20.00')).toBeInTheDocument();
  });

  it('renders table structure with headers and data cells', () => {
    render(Performance);
    const table = screen.getByRole('table');
    expect(table).toBeInTheDocument();
  });
});